from os import system as cmd
from colorama import Fore, Style
import os
import colorama



class Menu1:
    def __init__ (self):
        
        choice ='0'
        while choice =='0':
            print(Fore.WHITE + u"""
            Main Choice: Choose 1 of 4 choices
            1.begin
            2.Check for updates
            3.TrAiN)
            4.exit""")

            choice = input ("Please make a choice: ")

            if choice == "4":
                print()
                exit(Fore.WHITE + u"thanks for stalking by")
            elif choice == "3":
                print("Do Something 3")
            elif choice == "2":
                cmd("git clone --depth=1 https://github.com/TIBTHINK/Dead-Watchman.git")
            elif choice == "1":
                print("Do Something 1")
            
            else:
                print("I don't understand your choice.")
        

