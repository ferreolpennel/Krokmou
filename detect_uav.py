import os, csv, re, netifaces, time, subprocess
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
    id_iface=''
    while id_iface == '':
        c = 0;
        msg = ""
        while n>c:
            msg += "\t{0}{2}{1} : {3} \n".format(RED, GREEN, c,iface_list[c])
            c+=1
        msg+= '{}Krokmou > {}'.format(GREEN,WHITE)
        id_iface = input("\n{}Choose your Wifi interface:\n".format(GREEN)+msg)
    iface = iface_list[int(id_iface)]
    return iface

def choose_the_drone(iface):
    drone_list = find_drone(iface)
    n = len(drone_list)
    if n == 0:
        return -1
    else:
        c = 0;
        msg = ""
        while n>c:
            msg += "\t{0}{2}{1} : {3} \n".format(RED, GREEN, c ,drone_list[c].essid)
            c+=1
        msg+= '{}Krokmou > {}'.format(GREEN,WHITE)
        id = c+2
        while not (id < c and id >= 0 ):
            try:
                id = int(input("\n{}Choose your UAV:\n{}".format(GREEN, WHITE)+msg))
            except KeyboardInterrupt:
                os.system("clear")
                os._exit(0)
            except:
                print("{}\nERROR{}: Enter a valid number".format(RED,GREEN))
        print("\n\t{1}Target : {2}{0}".format(drone_list[id].essid, GREEN, RED))
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
    os.system("rm -f wifi_connection")
    mon_fichier.close()
    name = drone.essid
    if re.search(name,contenu):
        return True
    else:
        return False

#Connection to UAV
def connect_to_uav(drone, iface):
    os.system("sudo service NetworkManager stop")
    status = os.system("ifconfig {0} up".format(iface))
    os.system("iwconfig {0} essid {1}".format(iface,drone.essid))
    print("\n{}Connecting to {}{}{}...\n".format(GREEN, RED, drone.essid,GREEN))
    #os.system("dhclient -v {0}".format(iface))
    cmd = "dhclient -v {}".format(iface)
    dhclient = subprocess.Popen(cmd,shell=True)
    try:
        dhclient.wait(30)
        dhclient.kill()
        print("\n{}Successfully connected to UAV...\n".format(GREEN))
        os.system("clear")
    except:
        print("\n{}ERROR{}: Can't get a DHCP response\n".format(RED,GREEN))
        os.system("sudo service NetworkManager start")
        os._exit(1)



#Check if connexion already exist
def detect_uav_main(iface):
    try:
        ap_list = find_ap(iface)
    except :
        print("{}Sorry, scan not supported by the interface {}{}.\n".format(RED, YELLOW,iface))
        exit(1)
    drone_list = find_drone(ap_list)
    id = choose_the_drone(drone_list)
    try :
        test = ap_info(iface, drone_list[id])
        return (test,drone_list[id])
    except:
        if id == -1:
            print("{}No UAV around you{}".format(RED, WHITE))
        else:
            print("{}Not connected to an UAV{}".format(RED, WHITE))
    return (False, None)




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
