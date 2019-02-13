#!/usr/bin/env python3

import os, sys, logging, math
from time import sleep
from command_injection import *
BLUE, RED, WHITE, YELLOW, MAGENTA, GREEN = '\33[94m', '\033[91m', '\33[97m', '\33[93m', '\033[1;35m', '\033[1;32m'


try:
    if os.geteuid() != 0:
        print('{}ERROR{}: Krokmou must be run with root privileges. Try again !\n'.format(RED,GREEN))
        os._exit(1)
except:
    pass


def head():
    os.system("clear")
    sys.stdout.write(GREEN + """
    ██╗  ██╗██████╗  ██████╗ ██╗  ██╗███╗   ███╗ ██████╗ ██╗   ██╗
    ██║ ██╔╝██╔══██╗██╔═══██╗██║ ██╔╝████╗ ████║██╔═══██╗██║   ██║
    █████╔╝ ██████╔╝██║   ██║█████╔╝ ██╔████╔██║██║   ██║██║   ██║
    ██╔═██╗ ██╔══██╗██║   ██║██╔═██╗ ██║╚██╔╝██║██║   ██║██║   ██║
    ██║  ██╗██║  ██║╚██████╔╝██║  ██╗██║ ╚═╝ ██║╚██████╔╝╚██████╔╝
    ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝ ╚═════╝  ╚═════╝
    """ + '\n' + '{}Take control of any {}ARDrone2.0{} nearby and make him do funny things !\n'.format(YELLOW,RED,YELLOW))

def menu():
    print('\n{}Choose what you want to do: \n'.format(GREEN))
    print('\t{}1{} - Take control !'.format(RED, GREEN))
    print('\t{}2{} - Replace video stream by Krokmou'.format(RED,GREEN))
    print('\t{}3{} - Send control commands to make him crazy'.format(RED,GREEN))
    print("\t{}4{} - Let's just be root !".format(RED,GREEN))
    print('\t{}5{} - Leave a Christmas present for USB keys'.format(RED,GREEN))
    print('\n\t{}E{} - Exit\n'.format(RED,GREEN))

def shutdown():
    print('\n{}Exiting...\n'.format(GREEN))
    os._exit(0)

def check_dependencies():
    try:
        import nmap
        import spoof
    except KeyboardInterrupt:
        shutdown()
    except:
        print("\n{}ERROR{}: System do not meet requirements. Please check the dependencies needed by Krokmou in README\n".format(RED,GREEN))
        os._exit(1)

def main():
    check_dependencies()
    head()
    try:
        while True:
            menu()
            header = '{}Krokmou{} > '.format(GREEN,WHITE)
            choice = input(header)

            if choice.upper() == 'E' or choice.upper() == 'EXIT':
                shutdown()
            elif choice == '1':
                take_control()
            elif choice =='2':
                stream_hack()
            elif choice == '3':
                ci_main()
            elif choice == '4':
                root()
            elif choice == '5':
                send_virus()
            else:
                print('\n{}ERROR{}: Bad option. Please select a valid option.\n)'.format(RED,GREEN))
    except KeyboardInterrupt:
        shutdown()


#if __name__ == 'main':
main()
