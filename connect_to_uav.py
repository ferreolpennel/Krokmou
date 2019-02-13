#!/usr/bin/env python3
# -.- coding: utf-8 -.-
# connect_to_uav.py
import os
import csv
import re

#création d'objet correspondant au drones
class AP_drone:
    """Classe définissant un Wifi de drone caractérisée par:
        - BSSID @Mac du drone
        - ESSID Nom du réseau Wifi"""
    def __init__(self, bssid, essid):
        self.bssid = bssid
        self.essid = essid


#mac addres of parrot drones: A0:14:3D 90:3A:E6 90:03:B7 00:26:7E 00:12:1C. Regex
drone_macs = [ r"^90:03:B7", r"^A0:14:3D", r"^90:3A:E6", r"^00:26:7E", r"^00:12:1C"]
drone_list = []
#interfaces of wifi card
interface = "wlo1"
interface_mon = interface+"mon"

def start_airmon():
    #switch wifi to monitor mode to detect the wifi's drone
    cmd = "sudo ifconfig {0} down".format(interface)
    os.system(cmd)

    os.system("sudo airmon-ng check kill")
    cmd = "sudo airmon-ng start {0}".format(interface)
    os.system(cmd)

def stop_airmon():
    cmd = "sudo airmon-ng stop {0}".format(interface_mon)
    os.system(cmd)
    cmd = "sudo ifconfig {0} up".format(interface)
    os.system(cmd)
    os.system("sudo service NetworkManager start")

#find AP in proximity
def scan_wifi():
    #file of AP
    drone_list = "drone_list"
    try:
        cmd = "sudo airodump-ng -t OPN --output-format csv -w {0} {1} >>/dev/null 2>>/dev/null".format(drone_list, interface_mon)
        os.system("gnome-terminal -- {0}".format(cmd))
        os.system("sleep 15")
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
        print(drone_list[0].essid)
    cmd = "sudo rm drone_list-01.csv"
    os.system(cmd)


def main():
    start_airmon()
    scan_wifi()
    stop_airmon()
    find_drone()

#if __name__ == 'main':
main()
