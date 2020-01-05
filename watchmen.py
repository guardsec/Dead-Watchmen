#! /usr/bin/python3
import src.core.ToLazyToTypeOver.clear
import src.core as core
import src.core.var as vars
import src.menu as menu
from colorama import Fore, Style, Back
from os import system as cmd
from time import sleep
import os
import sys
import colorama
import platform

try:
    system = platform.system()
    if system == "Windows":
        exit(Fore.RED + u"Sorry but Dead Watchmen cant run on Windows, you pretend hacker" + Fore.WHITE)

    if os.geteuid() != 0:
        exit(Fore.RED + u"please run me as root" + Fore.WHITE)

    if not os.path.isfile("src/agreement.txt"):
        cmd("clear")
        sleep(2)
        vars.text.aggrement()
        
        choice = input("\nDo you agree to the terms of service [y/n]: ")
        choice += " "  # b/c method below
        if choice[0].lower() == "y":
            with open("src/agreement.txt", "w") as filewrite:
                filewrite.write("user accepted")
            print("good choice")
            sleep(3)
            src.core.ToLazyToTypeOver.clear()
            


        else:
            exit("\nwell have a good day, \ncome back when you want to play fair\n" + Fore.WHITE)
    menu.boot()
    menu.logo.logo()
    menu.menu.Mainmenu()

except KeyboardInterrupt:
    print(Fore.RED + "\nThanks for stalking by" + Fore.WHITE)
