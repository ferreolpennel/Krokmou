from wifi_func import *
import sys, os, re, time

BLUE, RED, WHITE, YELLOW, MAGENTA, GREEN = '\33[94m', '\033[91m', '\33[97m', '\33[93m', '\033[1;35m', '\033[1;32m'

def animate(length):
    for value in range(1,length):
        sys.stdout.write(GREEN + '.')
        sys.stdout.flush()
        time.sleep(0.05)

def launch_uav_search():
    print('\n{}Initializing interface for search'.format(GREEN),end='')
    animate(10)

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
                print(cell.address)

    except:
        print("\n{}ERROR{}: Can't detect any vulnerable UAV.\n".format(RED,GREEN))
        os._exit(1)

    print("\n{}List of vulnerable UAVs :\n".format(GREEN))
    for i in range(len(drone_list)):
        print("{}{} : {} - {}\n".format(GREEN, i, cell.ssid, cell.address))

    while True:
        print("{}Choose wich Krokmou you want to discuss with :\n".format(GREEN))
        header = '{}Krokmou > '.format(GREEN,WHITE)
        choice = input(header)

        if choice.upper() == 'B' or choice.upper() == 'BACK':
            break
        elif int(choice) <= len(drone_list):
            selected_UAV = drone_list[int(choice)]
            #try:
            connect(interface, selected_UAV)
            print("\n{}Connected to UAV Wifi network.\n".format(GREEN))
            break
            """except:
                print("\n{}ERROR{}: Unable to connect to UAV.\n".format(RED,GREEN))
                os._exit(1)
"""
        else:
            print("{}ERROR{}: Choose a UAV in the list.".format(RED,GREEN))
