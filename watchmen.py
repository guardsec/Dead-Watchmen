import src.menu as menu
import src.core as core
import src.core.var as var
from src.core.phishing.ngrok import ngrok
from colorama import Fore, Style, Back
from os import system as cmd
from time import sleep
import os
import sys
import colorama
import platform

system = platform.system()
if system == "Windows":
    exit(Fore.RED + u"sorry but Dead Watchmen cant run on Windows you boomer")
    print(Fore.WHITE)

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
       exit("\nwell have a good day, \ncome back when you want to play fair\n")
       print(Fore.WHITE)
print(Fore.WHITE)
menu.boot()
menu.logo.logo()
menu.menu.Mainmenu()
