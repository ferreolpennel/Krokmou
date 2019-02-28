#!/usr/bin/env python3

import os, sys, logging, math, time, subprocess
from time import sleep

BLUE, RED, WHITE, YELLOW, MAGENTA, GREEN = '\33[94m', '\033[91m', '\33[97m', '\33[93m', '\033[1;35m', '\033[1;32m'

import pip
from pip.req import parse_requirements
import pkg_resources
from pkg_resources import DistributionNotFound, VersionConflict

#Check if Krokmou was launched with root privileges
try:
    if os.geteuid() != 0:
        print('{}ERROR{}: Krokmou must be run with root privileges. Try again !\n'.format(RED,GREEN))
        os._exit(1)
except:
    pass

def check_dependencies(requirement_file_name):
    """Checks to see if the python dependencies are fullfilled. If check passes return 0. Otherwise print error and return 1"""
    dependencies = []
    session = pip.download.PipSession()
    for req in parse_requirements(requirement_file_name, session=session):
        if req.req is not None:
            dependencies.append(str(req.req))
        else: # The req probably refers to a url. Depending on the # format req.link.url may be able to be parsed to find the # required package.
            pass
    try:
        pkg_resources.working_set.require(dependencies)

    except VersionConflict as e:
        try:
            print("{} was found on your system, " "but {} is required.\n".format(e.dist, e.req))
            return 1
        except AttributeError:
            print(e)
            return 1

    except DistributionNotFound as e:
        print(e)
        return 1

    try:
        status = subprocess.check_output("apt list | grep aircrack-ng", shell=True)
    except:
        print("\n{}ERROR{}: Can't check the list of installed packages to check if aircrack-ng is installed\n".format(RED,GREEN))
        os._exit(1)

    if b'aircrack-ng' not in status:
        print("\n{}ERROR{}: Aircrack suite not installed. Please install it manually before running Krokmou.\n".format(RED,GREEN))
        os._exit(1)

    #print("\n{}Aircrack-ng suite is available. Continuing...\n".format(GREEN))

    return 0

if(check_dependencies("requirements.txt")==1):
    print("\n{}ERROR{}: Your system don't have the required dependencies to run Krokmou.\n".format(RED,GREEN))
    print("{}Please check the README and install all the dependencies manually before running Krokmou\n".format(GREEN))
    os._exit(1)

#if dependencies ok importing modules
from command_injection import *
from christmas_present import *
from take_control import *
from search_uav import *
from detect_uav import *

#print("{}\nAll dependencies checked ! Everything ok ! Continuing...\n".format(GREEN))

#Header of the program
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

#Display menu with options of the program
def menu():
    os.system("clear")
    head()

    print('\n{}Choose what you want to do: \n'.format(GREEN))
    print('\t{}1{} - Take control !'.format(RED, GREEN))
    print('\t{}2{} - Send control commands to make him crazy'.format(RED,GREEN))
    print('\t{}3{} - Leave a Christmas present for USB keys'.format(RED,GREEN))
    print('\n\t{}E{} - Exit\n'.format(RED,GREEN))


#Function to call to exit Krokmou
def shutdown():
    #stop_search_uav()      #A decommenter quand la gestion du module wifi sera correctement gérer
    print('\n{}Exiting...'.format(GREEN))
    print("\n{}Printing an image of Krokmou while restoring services...\n".format(GREEN))
    os.system("sudo service NetworkManager start")  # restart NetworkManager
    animate_krokmou()
    os.system("clear")
    os._exit(0)

#Function to animate info Display
def animate_krokmou():
    krokmou =  """
                        ;#+`               +#'`
                       ####;              ,+###.
                      ###'#'              ,#'+##,
                     ###'+#.         `    .#+''@#`
                    +#++''#.   ++@ `#++    #+++'##
                   :##++++#,  ###@` ####. `#+++'##'`
                   ##+++++#'`##'+# .@++## :#+++'+##`
                  ;##+++++#'@#+++#@#++''##.##++++'#+
                  ##++++++#+@#+########++#'##+++''##
                 `##+++++########@#'@@@###@#@++++++#.
                 ,#+++++###++++++''+++++''+###+++'+#;
                 ;#+++++++++++++''+++++++++++++++++#'
                 ;#+++#'++++++++''+++++++++++++++++#'
                 ,#++#'++++++++++'++++++++++++++@++#;
                  #+##+++++++++++++++++++++++++++@+@.
                  ##@+++++++++++++##+++++++++++++@##
                '@#@@++++++++++++++++'+++++++++++###@# `
               `+####+++++++++++++++++++++++++++++##@#.
                #+#@#+++++++++++++++++++++++++++++##'#
                #+'###+#@#@@++++++++++++++#@###++@@++#
                ;#++#+@#,,:@@++++++++++++@##,,.@++@++;
                 @###+#.,,####++++++++++##@##,,#++@##
                  @####.,+ ###@#++++++##,@###,,#++@#
                  #@#+++:;@##@,+++++++###@@##,,@+###`
                  ##@#+#:.#@@+.#++++++#..@#@,,@++#'+
                 ``##@+++@;,.'##++++++++@','@++++@+,
                 `  @####+++###+++++++#++##++++#@#
                    ``@#@#++##+++@++##+#+++####+``
                       `@#+#@@@##+#+++#@@#++##.
                          ,#@##+#@#@@@+#@#+.
                               `'@####.
    """

    for i in krokmou:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.005)

    time.sleep(2)


#Main function of Krokmou
def main():

    head()
    
    try:
        #Choix de l'interface de Connection
        try:
            iface = init_iface()  #fonction de connect_to_uav.py
        except KeyboardInterrupt:
            shutdown()
        except:
            print("{}ERROR{}: No interfaces available\n".format(RED,GREEN))
            os._exit(1)

        print("\n{}Scanning for vulnerable UAVs...".format(GREEN))
        (test,drone) = detect_uav_main(iface)

        #Check if computer connect to the drone
        try:
            test = ap_info(iface, drone)
        except :
            os._exit(1)

        if test == False:
            try:
                connect_to_uav(drone, iface)   # try to connect to the uav

            except:
                print("{}ERROR{}: Can't connect to Krokmou\n".format(RED,GREEN))
                os._exit(1)
        try:
            test = ap_info(iface, drone)
        except :
            os._exit(1)

        #If automatic connection doesn't work, restart NetworkManager to allow manual connection
        if test == False:
            try:
                os.system("service NetworkManager start")
            except:
                print("{}ERROR{}: Can't restart NetworkManager service. Please restart it manually\n".format(RED,GREEN))

            print("{}ERROR{}: You are not connected to a UAV. Please do it manually.".format(RED,GREEN))

        while test == False:
            try:
                (test,drone) = detect_uav_main(iface)
            except:
                print("{}ERROR{}: Can't detect any UAV".format(RED, GREEN))
                os._exit(1)
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
