#!/usr/bin/env python3
# -.- coding: utf-8 -.-
# connect_to_uav.py
import os

#mac addres of parrot drones: A0:14:3D 90:3A:E6 90:03:B7 00:26:7E 00:12:1C

drone_macs = [ "A0:14:3D", "90:3A:E6", "90:03:B7", "00:26:7E", "00:12:1C"]

#interfaces of wifi card

interface = "wlo1"
interface_mon = "wlo1_mon"

#switch wifi to monitor mode to detect the wifi's drone
cmd = "sudo ifconfig"+interface+"down"
os.system(cmd)
cmd = "sudo airmon-ng start" + interface_mon
os.system(cmd)

#find AP in proximity

#find drone AP
