
from colorama import Fore, Style, Back
from os import system as cmd
from time import sleep
from src.menu.logo import logo
from src.core.whitepages import whitepages

def Mainmenu():
    choice ='0'
    while choice =='0':
        print(Fore.WHITE + u"""
    1.begin
    2.Check for updates
    3.TrAiN
    4.exit
                """)
        choice = input ("Please make a choice: ")
        if choice == "4":
            print()
            exit(Fore.WHITE + u"thanks for stalking by")
        elif choice == "3":
            TrAiN()
            sleep(1)
            cmd("clear")
            logo()
            Mainmenu()
        elif choice == "2":
            print("im working on it")
            #cmd("git clone --depth=1 https://github.com/TIBTHINK/Dead-Watchman.git")
        elif choice == "1":
            whitepages.info()        
        else:
            print("I don't understand your choice.")
            sleep(4)
            cmd("clear")
            logo()
            Mainmenu()

def TrAiN():
    cmd("sl")