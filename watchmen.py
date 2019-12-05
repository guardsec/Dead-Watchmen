#! /bin/python3
import src.menu as menu
import src.core as core
import src.core.var as var
from colorama import Fore, Style, Back
from os import system as cmd
from time import sleep
import os
import sys
import colorama

if os.geteuid() != 0:
    exit(Fore.RED + u"please run me as root")

if not os.path.isfile("src/agreement.txt"):
    cmd("clear")
    sleep(2)
    var.text.aggrement()
       
    choice = input("\nDo you agree to the terms of service [y/n]: ")
    choice += " "  # b/c method below
    if choice[0].lower() == "y":
        with open("src/agreement.txt", "w") as filewrite:
            filewrite.write("user accepted")

    else:
       exit("Welp have a good day, \n come back when you want to play fair")
print(Fore.WHITE)
menu.boot.load_animtion()

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
        print("Do Something 3")
    elif choice == "2":
        print("im working on it")
        #cmd("git clone --depth=1 https://github.com/TIBTHINK/Dead-Watchman.git")
    elif choice == "1":
        core.whitepages.info()        
    else:
        print("I don't understand your choice.")