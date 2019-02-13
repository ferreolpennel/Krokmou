#!/usr/bin/env python3
# -.- coding: utf-8 -.-
# connect_to_uav.py
import os
import csv
import re
import netifaces
import time
import wifi

#Class object for the UAV
class AP_drone:
    """Class which defines AP of the UAV, caracterized by:
        - BSSID Mac address of the UAV
        - ESSID Name of the Wifi"""
    def __init__(self, bssid, essid):
        self.bssid = bssid
        self.essid = essid

#Class object for the clients of the UAV
class Client:
    """ Class which defines clinets connected to the UAV and caracterized by:
        - Mac address
        - IP address """
    def __init__(self, mac, ip):
        self.mac = mac
        self.ip = ip


#mac addres of parrot drones: A0:14:3D 90:3A:E6 90:03:B7 00:26:7E 00:12:1C. Regex
drone_macs = [ r"^90:03:B7", r"^A0:14:3D", r"^90:3A:E6", r"^00:26:7E", r"^00:12:1C"]
drone_list = []

client_list = []

# iface = ""
# iface_mon = ""

#ifaces of wifi card

iface_list = netifaces.interfaces()
n = len(iface_list)
c = 0;
msg = ""
while n>c:
    msg += "{0} : {1} \n".format(iface_list[c], c)
    c+=1
msg+= "Your choice ? :"

id_iface = input("Choose your iface:\n"+msg)
iface = iface_list[int(id_iface)]
iface_mon = iface+"mon"

def start_airmon():
    #switch wifi to monitor mode to detect the wifi's drone
    cmd = "sudo ifconfig {0} down >>/dev/null 2>>/dev/null".format(iface)
    os.system(cmd)

    os.system("sudo airmon-ng check kill >>/dev/null 2>>/dev/null")
    cmd = "sudo airmon-ng start {0} >>/dev/null 2>>/dev/null".format(iface)
    os.system(cmd)

def stop_airmon():
    cmd = "sudo airmon-ng stop {0} >>/dev/null 2>>/dev/null".format(iface_mon)
    os.system(cmd)
    cmd = "sudo ifconfig {0} up >>/dev/null 2>>/dev/null".format(iface)
    os.system(cmd)
    os.system("sudo service NetworkManager start")

#find AP in proximity
def scan_wifi():
    #file of AP
    drone_list = "drone_list"
    try:
        cmd = "sudo airodump-ng -t OPN --output-format csv -w {0} {1} >>/dev/null 2>>/dev/null".format(drone_list, iface_mon)
        os.system("gnome-terminal -- {0}".format(cmd))
        os.system("sleep 5")
    except Exception as e:
        print("Can't run airodump-ng")

#find drone AP
def find_drone():
    with open("drone_list-01.csv", newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            n = len(row)
            if n == 15:
                if re.match(drone_macs[0],row[0]) or re.match(drone_macs[1],row[0]) or re.match(drone_macs[2],row[0]) or re.match(drone_macs[3],row[0]) or re.match(drone_macs[4],row[0]) :
                    drone_list.append(AP_drone(row[0], row[13]))
        print("Target : {0}".format(drone_list[0].essid))
    cmd = "sudo rm drone_list-0*"
    os.system(cmd)

def search_ap(netlist,drone):
    for ap in netlist:
        if ' '+ap.ssid == drone.essid:
            return ap
    return False

def connect(drone):
    netlist = wifi.Cell.all(iface)
    uav = search_ap(netlist, drone)
    print(uav.ssid)
    scheme = wifi.Scheme.for_cell(iface, uav.ssid, uav, None)
    scheme.activate()



def main():
    #init_iface()
    start_airmon()
    scan_wifi()
    find_drone()
    stop_airmon()
    connect(drone_list[0])

#if __name__ == 'main':
main()
