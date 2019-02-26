#!/usr/bin/env python3

import os, sys, logging, math
from time import sleep
from command_injection import *
from christmas_present import *
from take_control import *
from search_uav import *
from detect_uav import *
BLUE, RED, WHITE, YELLOW, MAGENTA, GREEN = '\33[94m', '\033[91m', '\33[97m', '\33[93m', '\033[1;35m', '\033[1;32m'

#Check if Krokmou was launched with root privileges
try:
    if os.geteuid() != 0:
        print('{}ERROR{}: Krokmou must be run with root privileges. Try again !\n'.format(RED,GREEN))
        os._exit(1)
except:
    pass

#Header of the program
def head():
    os.system("clear")
    # sys.stdout.write(GREEN + """
    #                     ;#+`               +#'`
    #                    ####;              ,+###.
    #                   ###'#'              ,#'+##,
    #                  ###'+#.         `    .#+''@#`
    #                 +#++''#.   ++@ `#++    #+++'##
    #                :##++++#,  ###@` ####. `#+++'##'`
    #                ##+++++#'`##'+# .@++## :#+++'+##`
    #               ;##+++++#'@#+++#@#++''##.##++++'#+
    #               ##++++++#+@#+########++#'##+++''##
    #              `##+++++########@#'@@@###@#@++++++#.
    #              ,#+++++###++++++''+++++''+###+++'+#;
    #              ;#+++++++++++++''+++++++++++++++++#'
    #              ;#+++#'++++++++''+++++++++++++++++#'
    #              ,#++#'++++++++++'++++++++++++++@++#;
    #               #+##+++++++++++++++++++++++++++@+@.
    #               ##@+++++++++++++##+++++++++++++@##
    #             '@#@@++++++++++++++++'+++++++++++###@# `
    #            `+####+++++++++++++++++++++++++++++##@#.
    #             #+#@#+++++++++++++++++++++++++++++##'#
    #             #+'###+#@#@@++++++++++++++#@###++@@++#
    #             ;#++#+@#,,:@@++++++++++++@##,,.@++@++;
    #              @###+#.,,####++++++++++##@##,,#++@##
    #               @####.,+ ###@#++++++##,@###,,#++@#
    #               #@#+++:;@##@,+++++++###@@##,,@+###`
    #               ##@#+#:.#@@+.#++++++#..@#@,,@++#'+
    #              ``##@+++@;,.'##++++++++@','@++++@+,
    #              `  @####+++###+++++++#++##++++#@#
    #                 ``@#@#++##+++@++##+#+++####+``
    #                    `@#+#@@@##+#+++#@@#++##.
    #                       ,#@##+#@#@@@+#@#+.
    #                            `'@####.
    # """)
    sys.stdout.write(GREEN + """
    ██╗  ██╗██████╗  ██████╗ ██╗  ██╗███╗   ███╗ ██████╗ ██╗   ██╗
    ██║ ██╔╝██╔══██╗██╔═══██╗██║ ██╔╝████╗ ████║██╔═══██╗██║   ██║
    █████╔╝ ██████╔╝██║   ██║█████╔╝ ██╔████╔██║██║   ██║██║   ██║
    ██╔═██╗ ██╔══██╗██║   ██║██╔═██╗ ██║╚██╔╝██║██║   ██║██║   ██║
    ██║  ██╗██║  ██║╚██████╔╝██║  ██╗██║ ╚═╝ ██║╚██████╔╝╚██████╔╝
    ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝ ╚═════╝  ╚═════╝
    """ + '\n' + '{}Take control of any {}ARDrone2.0{} nearby and make him do funny things !\n'.format(YELLOW,RED,YELLOW))

#Display menu with options of the program
def menu():
    print('\n{}Choose what you want to do: \n'.format(GREEN))
    print('\t{}1{} - Take control !'.format(RED, GREEN))
    print('\t{}2{} - Send control commands to make him crazy'.format(RED,GREEN))
    print('\t{}3{} - Leave a Christmas present for USB keys'.format(RED,GREEN))
    print('\n\t{}E{} - Exit\n'.format(RED,GREEN))


#Function to call to exit Krokmou
def shutdown():
    #stop_search_uav()      #A decommenter quand la gestion du module wifi sera correctement gérer
    print('\n{}Exiting...\n{}'.format(GREEN,WHITE))
    os.system("sudo service NetworkManager start")  # restart NetworkManager
    os.system("clear")
    os._exit(0)

#Checking depencies needed by Krokou
def check_dependencies():
    try:
        import nmap
        import netifaces
        import scapy
        import wifi
    except KeyboardInterrupt:
        shutdown()
    except:
        print("\n{}ERROR{}: System do not meet requirements. Please check the dependencies needed by Krokmou in README\n".format(RED,GREEN))
        os._exit(1)


#Main function of Krokmou
def main():
    check_dependencies()
    head()
    #launch_uav_search()    #A décommenter quand la gestion du module wifi sera correctement gérer
    try:
        #Choix de l'interface de Connection
        try:
            iface = init_iface()  #fonction de connect_to_uav.py
        except KeyboardInterrupt:
            shutdown()
        except:
            print("{}No interfaces available \n".format(RED))


        (test,drone) = detect_uav_main(iface)


        #Check if computer connect to the drone
        try:
            test = ap_info(iface, drone)
        except :
            pass
        if test == False:
            try:
                connect_to_uav(drone, iface)   # try to connect to the uav
            except:
                pass
        try:
            test = ap_info(iface, drone)
        except Exception as e:
            pass
        #If automatic connection doesn't work, restart NetworkManager to allow manual connection
        if test == False:
            os.system("service NetworkManager start")

        while  test == False:
            print("{}You are not connected to a UAV. Please do it manually.{}".format(RED, WHITE))
            (test,drone) = detect_uav_main(iface)
            sleep(2)

        while True:
            menu()
            header = '{}Krokmou{} > '.format(GREEN,WHITE)

            choice = input(header)

            if choice.upper() == 'E' or choice.upper() == 'EXIT':
                shutdown()
            elif choice == '1':
                take_control_main(drone, iface)
            elif choice == '2':
                ci_main(drone, iface)
            elif choice == '3':
                christmas_present_main()
            else:
                print('\n{}ERROR{}: Bad option. Please select a valid option.\n'.format(RED,GREEN))
    except KeyboardInterrupt:
        shutdown()


#if __name__ == 'main':
main()
