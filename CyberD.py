from termcolor import colored
import os
import time

#import logo
from fun.logo import logo, social_media, tools, toolsop, startedup, toolsun

#import openfunction
from fun.openfunction import zphisherop, Red_Hawkop, ngrokop, MaskPhishop, infectop, AndroRatop, IPTrackerop, PyPhisherop, tunnelop, kalimuxop, exitop, PhoneInfogaop, T_Bomberop, metasploitop, mrphishop, IpHackop, Slowlorisop, social_boxop, osi_igop, cmatrixop

# import uninstall function
from fun.uninstallfunction import osi_igun, zphisherun, Red_Hawkun, ngrokun, MaskPhishun,infectun,AndroRatun,IPTrackerun,PyPhisherun,kalimuxun,PhoneInfogaun,metasploitun,T_Bomberun,mrphishun,IpHackun,tunnelun,Slowlorisun,social_boxun, osi_igun
# import function
from fun.function import zphisher, Red_Hawk, ngrok, MaskPhish, infect, AndroRat, IPTracker, PyPhisher, kalimux, PhoneInfoga, T_Bomber, metasploit, mrphish, IpHack, tunnel, Slowloris, social_box,osi_ig, about, exit,update, uninstall, cmatrix

# main coding
os.system("clear")
print(colored(logo,'blue')   + colored(social_media,'red') +colored(startedup,"green"))
open=input(colored("Choose a Option:","yellow"))
if open=="1":
    os.system("clear")  
    print(colored(logo,'blue') + colored(social_media,'red') + colored(toolsop,'green'))
    choose=input(colored("Choose a Option:",'yellow'))
    if choose == "1":
        zphisherop() 
    elif choose == "2":
        Red_Hawkop()
    elif choose == "3":
        ngrokop()
    elif choose == "4":
        MaskPhishop()
    elif choose == "5":
        infectop()
    elif choose == "6":
        AndroRatop()
    elif choose == "7":
        IPTrackerop()
    elif choose == "8":
        PyPhisherop()
    elif choose == "9":
        kalimuxop()
    elif choose == "10":
        PhoneInfogaop()
    elif choose == "11":
        T_Bomberop()
    elif choose == "12":
        metasploitop()
    elif choose == "13":
        mrphishop()
    elif choose == "14":
        IpHackop()
    elif choose== "15":
        tunnelop()
    elif choose== "16":
        Slowlorisop()
    elif choose=="17":
        social_boxop()
    elif choose=="18":
        osi_igop()
    elif choose=="19":
        cmatrixop()
    

# fixed nochange
    elif choose == "0":
        update()
    elif choose=="00":
        about()
    elif choose== "999":
        exitop()
    else:
        print(colored("[!] Invalid Option, Try Again...","red"))
        time.sleep(0.5)
        os.system("clear")
        os.system("python3 CyberD.py")

elif open=="2":
    os.system("clear")  
    print(colored(logo,'blue') + colored(social_media,'red') + colored(tools,'green'))
    choose=input(colored("Choose a Option:",'yellow'))
    if choose == "1":
        zphisher() 
    elif choose == "2":
        Red_Hawk()
    elif choose == "3":
        ngrok()
    elif choose == "4":
        MaskPhish()
    elif choose == "5":
        infect()
    elif choose == "6":
        AndroRat()
    elif choose == "7":
        IPTracker()
    elif choose == "8":
        PyPhisher()
    elif choose == "9":
        kalimux()
    elif choose == "10":
        PhoneInfoga()
    elif choose == "11":
        T_Bomber()
    elif choose == "12":
        metasploit()
    elif choose == "13":
        mrphish()
    elif choose == "14":
        IpHack()
    elif choose== "15":
        tunnel()
    elif choose== "16":
        Slowloris()
    elif choose=="17":
        social_box()
    elif choose=="18":
        osi_ig()
    elif choose=="19":
        cmatrix()

# fixed nochange
    elif choose=="00":
        about()
    elif choose == "0":
        update()
    elif choose== "999":
        exitop()
    else:
        print(colored("[!] Invalid Option, Try Again...","red"))
        time.sleep(0.5)
        os.system("clear")
        os.system("python3 CyberD.py")


elif open=="3":
    os.system("clear")  
    print(colored(logo,'blue') + colored(social_media,'red') + colored(toolsun,'green'))
    choose=input(colored("Choose a Option:",'yellow'))
    if choose == "1":
        zphisherun() 
    elif choose == "2":
        Red_Hawkun()
    elif choose == "3":
        ngrokun()
    elif choose == "4":
        MaskPhishun()
    elif choose == "5":
        infectun()
    elif choose == "6":
        AndroRatun()
    elif choose == "7":
        IPTrackerun()
    elif choose == "8":
        PyPhisherun()
    elif choose == "9":
        kalimuxun()
    elif choose == "10":
        PhoneInfogaun()
    elif choose == "11":
        T_Bomberun()
    elif choose == "12":
        metasploitun()
    elif choose == "13":
        mrphishun()
    elif choose == "14":
        IpHackun()
    elif choose== "15":
        tunnelun()
    elif choose== "16":
        Slowlorisun()
    elif choose=="17":
        social_boxun()
    elif choose=="18":
        osi_igun()
    # fixed no change
    elif choose=="000":
        uninstall()
    elif choose=="00":
        about()
    elif choose == "0":
        update()
    elif choose== "999":
        exitop()
    else:
        print(colored("[!] Invalid Option, Try Again...","red"))
        time.sleep(0.5)
        os.system("clear")
        os.system("python3 CyberD.py")


elif open =="4":
    update()

elif open=="00":
    exit()

elif open=="0":
    about()
else:
        print(colored("[!] Invalid Option, Try Again...","red"))
        time.sleep(0.4)
        os.system("clear")
        os.system("python3 CyberD.py")
