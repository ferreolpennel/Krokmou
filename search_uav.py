from wifi_func import *
import sys, os, re, 

BLUE, RED, WHITE, YELLOW, MAGENTA, GREEN = '\33[94m', '\033[91m', '\33[97m', '\33[93m', '\033[1;35m', '\033[1;32m'
drone_macs = [ r"^90:03:B7", r"^A0:14:3D", r"^90:3A:E6", r"^00:26:7E", r"^00:12:1C"]

def animate(length):
    for value in range(1,length):
        sys.stdout.write(GREEN + '.')
        sys.stdout.flush()
        time.sleep(0.05)

def launch_uav_search():
    print('\n{}Initializing interface for search'.format(GREEN),end='')
    animate(10)
    try:
        os.system("sudo service network-manager stop")
    except:
        print("\n{}ERROR{}: Can't stop network-manager service.\n".format(RED,GREEN))
        os._exit(1)

    try:
        interface = init_iface()
    except:
        print("\n{}ERROR{}: Can't find any interfaces available.\n".format(RED,GREEN))
        os._exit(1)

    print('\n{}Searching for vulnerable UAVs'.format(GREEN),end='')
    animate(10)

    drone_list = []

    try:
        wifilist = search(interface)
        for cell in wifilist:
            if re.match(drone_macs[0],cell.address) or re.match(drone_macs[1],cell.address) or re.match(drone_macs[2],cell.address) or re.match(drone_macs[3],cell.address) or re.match(drone_macs[4],cell.address):
                drone_list.append(cell)

    except:
        print("\n{}ERROR{}: Can't detect any vulnerable UAV.\n".format(RED,GREEN))
        os._exit(1)

    print("\n{}List of vulnerable UAVs :\n".format(GREEN))
    for i in range(len(drone_list)):
        print("{}{} : {} - {}\n".format(GREEN, i, drone_list[i].ssid, drone_list[i].address))

    while True:
        print("{}Choose wich Krokmou you want to discuss with :\n".format(GREEN))
        header = '{}Krokmou > '.format(GREEN,WHITE)
        choice = input(header)

        if choice.upper() == 'B' or choice.upper() == 'BACK':
            break
        elif int(choice) <= len(drone_list):
            selected_UAV = drone_list[int(choice)]
            try:
                connect(interface, selected_UAV)
                os.system("sudo dhclient {}".format(interface))
                print("\n{}Connected to UAV Wifi network.\n".format(GREEN))
                break
            except:
                print("\n{}ERROR{}: Unable to connect to UAV.\n".format(RED,GREEN))
                os._exit(1)

        else:
            print("{}ERROR{}: Choose a UAV in the list.".format(RED,GREEN))

def stop_search_uav():
    print("\n{}Restoring network-manager service...\n".format(GREEN))
    try:
        os.system("sudo service network-manager start\n")
        print("\n{}Service restored.\n".format(GREEN))
    except:
        print("\n{}ERROR{}: Can't start network-manager service.\n".format(RED,GREEN))
