#! /usr/bin/python3
from colorama import Fore, Style, Back
from os import system as cmd
from time import sleep
from src.menu.logo import logo, toolsLogo
from src.core.whitepages import whitepages
from src.core.phishing import pyphisher
from src.core.ToLazyToTypeOver import clear


def Mainmenu():

    choice ='0'
    while choice =='0':
        print(Fore.WHITE + u"""
    1.tools
    2.Check for updates
    3.TrAiN
    4.exit
                """)
        choice = input ("Please make a choice: ")
        if choice == "4":
            print(Fore.RED + "\nThanks for stalking by" + Fore.WHITE)
        elif choice == "3":
            print("doesnt work really sorry train dude")
            # TrAiN()
            sleep(1)
            clear()
            logo()
            Mainmenu()
        elif choice == "2":
            print("im working on it")
            #cmd("git clone --depth=1 https://github.com/TIBTHINK/Dead-Watchman.git")
            sleep(3)
            clear()
            logo()
            Mainmenu()
        elif choice == "1":
            clear()
            toolsLogo()
            tools()   
        else:
            print("I don't understand your choice.")
            sleep(4)
            clear()
            logo()
            Mainmenu()

def TrAiN():
    cmd("sl")

def tools():
    Tchoice = '0'
    while Tchoice =='0':
        print(Fore.WHITE + u"""
    1.Winfo
    2.Pyphisher
    3.Pinfo
    99.go back
                """)
        Tchoice = input("Please make a choice: ")
        if Tchoice == "1":
            whitepages.winfo()
            Mainmenu()
        elif Tchoice == "2":
            pyphisher()
            sleep(4)
            clear()
            toolsLogo() 
            Mainmenu()
        elif Tchoice == "3":
            whitepages.pinfo()
        elif Tchoice == "99":
            Mainmenu()
        else:
            print("I don't understand your choice.")
            sleep(4)
            clear()
            toolsLogo()
            tools()