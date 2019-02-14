# -*- coding: utf-8 -*-

import wifi, os
import netifaces

BLUE, RED, WHITE, YELLOW, MAGENTA, GREEN = '\33[94m', '\033[91m', '\33[97m', '\33[93m', '\033[1;35m', '\033[1;32m'
drone_macs = [ r"^90:03:B7", r"^A0:14:3D", r"^90:3A:E6", r"^00:26:7E", r"^00:12:1C"]

def init_iface():
    iface_list = netifaces.interfaces()
    n = len(iface_list)
    c = 0;
    print("\n{}Choose the interface you want to use:\n".format(GREEN))
    while n>c:
        print("\t{0}{2}{1} : {3}".format(RED, GREEN, c,iface_list[c]))
        c+=1
    print("\n")
    header = '{}Krokmou > '.format(GREEN,WHITE)
    id_iface = input(header)
    iface = iface_list[int(id_iface)]
    return iface


def search(interface):
    wifilist = []
    cells = wifi.Cell.all(interface)

    for cell in cells:
        wifilist.append(cell)

    return wifilist


def add(interface, cell, password=None):
    #try:
    scheme = wifi.Scheme.for_cell(interface, cell.ssid, cell, password)
    scheme.save()
    print("save ok")
    """except:
        print("\n{}ERROR{}: Can't create the configuration for the connection to the UAV.\n".format(RED,GREEN))
        os._exit(1)
"""
    return scheme


def connect(interface, cell, password=None):

    scheme = wifi.Scheme.find(interface, cell.ssid)
    if scheme == "None":
        scheme = add(interface,cell)
    try:
        scheme.activate()
        print("activate ok")
    except wifi.exceptions.ConnectionError:
        print("\n{}ERROR{}: Can't connect to UAV Wifi.\n".format(RED,GREEN))
        try:
            cell.delete()
        except:
            print("\n{}ERROR{}: Can't delete the configuration on the interface.\n".format(RED,GREEN))
            os._exit(1)
