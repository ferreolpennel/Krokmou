#!/usr/bin/env python3
# -.- coding: utf-8 -.-
# connect_to_uav.py
import os
import csv
import re
import netifaces
import time
import wifi

BLUE, RED, WHITE, YELLOW, MAGENTA, GREEN = '\33[94m', '\033[91m', '\33[97m', '\33[93m', '\033[1;35m', '\033[1;32m'

#Class object for the UAV
class AP_drone:
    """Class which defines AP of the UAV, caracterized by:
        - BSSID Mac address of the UAV
        - ESSID Name of the Wifi"""
    def __init__(self, bssid, essid, cell):
        self.bssid = bssid
        self.essid = essid
        self.cell = cell


#mac addres of parrot drones: A0:14:3D 90:3A:E6 90:03:B7 00:26:7E 00:12:1C. Regex
drone_macs = [ r"^90:03:B7", r"^A0:14:3D", r"^90:3A:E6", r"^00:26:7E", r"^00:12:1C"]

# client_list = []
# iface = ""
# iface_mon = ""
# def start_airmon(iface):
#     #switch wifi to monitor mode to detect the wifi's drone
#     cmd = "sudo ifconfig {0} down >>/dev/null 2>>/dev/null".format(iface)
#     os.system(cmd)
#
#     os.system("sudo airmon-ng check kill >>/dev/null 2>>/dev/null")
#     cmd = "sudo airmon-ng start {0} >>/dev/null 2>>/dev/null".format(iface)
#     os.system(cmd)
#
# def stop_airmon(iface, iface_mon):
#     cmd = "sudo airmon-ng stop {0} >>/dev/null 2>>/dev/null".format(iface_mon)
#     os.system(cmd)
#     os.system("sudo service NetworkManager start")
#     cmd = "sudo ifconfig {0} up >>/dev/null 2>>/dev/null".format(iface)
#     os.system(cmd)
#
# #find AP in proximity
# def scan_wifi(iface_mon):
#     #file of AP
#     drone_file = "drone_list"
#     try:
#         cmd = "sudo airodump-ng -t OPN --output-format csv -w {0} {1} >>/dev/null 2>>/dev/null".format(drone_file, iface_mon)
#         os.system("gnome-terminal -- {0}".format(cmd))
#         os.system("sleep 5")
#     except Exception as e:
#         print("Can't run airodump-ng")
#
# #find drone AP
# def find_drone():
#     with open("drone_list-01.csv", newline="") as file:
#         reader = csv.reader(file)
#         for row in reader:
#             n = len(row)
#             if n == 15:
#                 if re.match(drone_macs[0],row[0]) or re.match(drone_macs[1],row[0]) or re.match(drone_macs[2],row[0]) or re.match(drone_macs[3],row[0]) or re.match(drone_macs[4],row[0]) :
#                     drone_list.append(AP_drone(row[0], row[13]))
#     # print("Target : {0}".format(drone_list[0].essid))
#     cmd = "sudo rm drone_list-0*"
#     os.system(cmd)
#     return drone_list
# def connect(drone, iface):
#     status = os.popen("ifconfig {0} up".format(iface)).read()
#     os.popen("iwconfig {0} essid{1}".format(iface,drone.essid))
#     print("Connecting to {1}{0}......".format(drone.essid, GREEN))
#     os.popen("dhclient {0}".format(iface))
#

#ifaces of wifi card
def init_iface():
    iface_list = netifaces.interfaces()
    n = len(iface_list)
    c = 0;
    msg = ""
    while n>c:
        msg += "\t{0}{2}{1} : {3} \n".format(RED, GREEN, c,iface_list[c])
        c+=1
    msg+= "{}Your choice ? :".format(GREEN)

    id_iface = input("\n{}Choose your iface:\n".format(GREEN)+msg)
    iface = iface_list[int(id_iface)]
    iface_mon = iface+"mon"
    return (iface, iface_mon)


def choose_the_drone(drone_list):
    n = len(drone_list)
    c = 0;
    msg = ""
    while n>c:
        msg += "\t{0}{2}{1} : {3} \n".format(RED, GREEN, c ,drone_list[c].essid)
        c+=1
    msg+= "{}Your choice ? :".format(GREEN)
    id = int(input("\n{}Choose your uav:\n".format(GREEN)+msg))
    print("\t{1}Target : {2}{0}".format(drone_list[id].essid, GREEN, RED))
    return id

def search_ap(netlist):
    drone_list = []
    for ap in netlist:
            if re.match(drone_macs[0],ap.address) or re.match(drone_macs[1],ap.address) or re.match(drone_macs[2],ap.address) or re.match(drone_macs[3],ap.address) or re.match(drone_macs[4],ap.address) :
                drone_list.append(AP_drone(ap.address, ap.ssid, ap))

    return drone_list

def connect(iface):
    netlist = wifi.Cell.all(iface)
    list_of_drone = search_ap(netlist)
    id = choose_the_drone(list_of_drone)
    uav = list_of_drone[id]
    print(uav.essid)
    scheme = wifi.Scheme.for_cell(iface, uav.essid, uav.cell, None)
    scheme.save()
    scheme.activate()


def main():
    (iface,iface_mon) = init_iface()
    connect(iface)
    #start_airmon(iface)
    #scan_wifi(iface_mon)
    # = find_drone()
    #stop_airmon(iface, iface_mon)
    #id = choose_the_drone(list_of_drone)

#if __name__ == 'main':
main()
