#!/usr/bin/env python3
# -.- coding: utf-8 -.-
# connect_to_uav.py
import os

#mac addres of parrot drones: A0:14:3D 90:3A:E6 90:03:B7 00:26:7E 00:12:1C

drone_macs = [ "A0:14:3D", "90:3A:E6", "90:03:B7", "00:26:7E", "00:12:1C"]

#interfaces of wifi card

interface = "wlo1"
interface_mon = "wlo1mon"

#switch wifi to monitor mode to detect the wifi's drone
cmd = "sudo ifconfig {0} down".format(interface)
os.system(cmd)

os.system("sudo airmon-ng check kill")
cmd = "sudo airmon-ng start {0}".format(interface)
os.system(cmd)

#file of AP
drone_list = "drone_list.csv"

#find AP in proximity
try:
    cmd = "sudo airodump-ng --output-format csv -w {0} {1} >>/dev/null 2>>/dev/null".format(drone_list, interface_mon)
    os.system(cmd)
except Exception as e:
    print("Can't run airodump-ng")


#find drone AP

cmd = "sudo airmon-ng stop {0}".format(interface_mon)
os.system(cmd)
cmd = "sudo ifconfig {0} up".format(interface)
os.system(cmd)
os.system("sudo service NetworkManager start")
