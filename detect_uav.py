# -.- coding: utf-8 -.-
# detect_uav.py
import os
import csv
import re
import netifaces
import time
import wifi
from wifi_func import *

BLUE, RED, WHITE, YELLOW, MAGENTA, GREEN = '\33[94m', '\033[91m', '\33[97m', '\33[93m', '\033[1;35m', '\033[1;32m'

#Class object for the UAV
class AP_drone:
    """Class which defines AP of the UAV, caracterized by:
        - BSSID Mac address of the UAV
        - ESSID Name of the Wifi"""
    def __init__(self, bssid, essid):
        self.bssid = bssid
        self.essid = essid


#mac addres of parrot drones: A0:14:3D 90:3A:E6 90:03:B7 00:26:7E 00:12:1C. Regex
drone_macs = [ r"^90:03:B7", r"^A0:14:3D", r"^90:3A:E6", r"^00:26:7E", r"^00:12:1C"]


#ifaces of wifi card
def init_iface():
    iface_list = netifaces.interfaces()
    n = len(iface_list)
    c = 0;
    msg = ""
    while n>c:
        msg += "\t{0}{2}{1} : {3} \n".format(RED, GREEN, c,iface_list[c])
        c+=1
    msg+= "{}Your choice ? :{}".format(GREEN,WHITE)
    id_iface = int(input("\n{}Choose your iface:\n".format(GREEN)+msg))
    iface = iface_list[id_iface]
    return iface

def choose_the_drone(iface):
    drone_list = find_drone(iface)
    n = len(drone_list)
    c = 0;
    msg = ""
    while n>c:
        msg += "\t{0}{2}{1} : {3} \n".format(RED, GREEN, c ,drone_list[c].essid)
        c+=1
    msg+= "{}Your choice ? :".format(GREEN)
    id = int(input("\n{}Choose your uav:{}\n".format(GREEN, WHITE)+msg))
    print("\t{1}Target : {2}{0}".format(drone_list[id].essid, GREEN, RED))
    return id


#find ap around
def find_ap(iface):
    ap_list = []
    wifi = search(iface)
    for cell in wifi:
        ap_list.append(AP_drone(cell.address, cell.ssid))
    return ap_list


# #find drone AP
def find_drone(ap_list):
    drone_list =[]
    for ap in ap_list:
        if re.match(drone_macs[0],ap.bssid) or re.match(drone_macs[1],ap.bssid) or re.match(drone_macs[2],ap.bssid) or re.match(drone_macs[3],ap.bssid) or re.match(drone_macs[4],ap.bssid) :
            drone_list.append(AP_drone(ap.bssid, ap.essid))
    return drone_list

#find ap connected address
def ap_info(iface, drone):
    cmd = "iw {0} info |grep ssid > wifi_connection".format(iface)
    os.system(cmd)
    mon_fichier = open("wifi_connection", "r")
    contenu = mon_fichier.read()
    mon_fichier.close()
    # print(contenu)
    name = drone.essid
    if re.search(name,contenu):
        return True
    else:
        return False


#Check if connexion already exist
def detect_uav_main(iface):
    ap_list = find_ap(iface)
    drone_list = find_drone(ap_list)
    id = choose_the_drone(drone_list)
    try :
        test = ap_info(iface, drone_list[id])
        return (test,drone_list[id])
    except:
        print("Not connected to an UAV")
    return (False, None)
