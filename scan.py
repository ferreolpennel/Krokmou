#!/usr/bin/env python3
# -.- coding: utf-8 -.-
# scan.py

"""
Copyright (C) 2017-18 Nikolaos Kamarinakis (nikolaskam@gmail.com) & David Schütz (xdavid@protonmail.com)
See License at nikolaskama.me (https://nikolaskama.me/kickthemoutproject)
"""

"""
This fonction give back the list of client connected to the AP
"""

import nmap


#Class object for the clients of the UAV
class Client:
    """ Class which defines clinets connected to the UAV and caracterized by:
        - Mac address
        - IP address """
    def __init__(self,ip, mac):
        self.ip = ip
        self.mac = mac

# perform a network scan with nmap
def scanNetwork(network):
    returnlist = []
    nm = nmap.PortScanner()
    a = nm.scan(hosts=network, arguments='-sn')

    for k, v in a['scan'].items():
        if str(v['status']['state']) == 'up':
            try:
                returnlist.append(Client(str(v['addresses']['ipv4']), str(v['addresses']['mac'])))
            except:
                pass

    return returnlist
