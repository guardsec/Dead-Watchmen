#! /bin/python3
#  
import src.menu as menu
import src.core as core
import src.var as var

from colorama import Fore, Style
from os import system as cmd
import os
import sys

if not os.path.isfile("src/agreement4"):
        with open("readme/LICENSE") as fileopen:
            for line in fileopen:
                print((line.rstrip()))

        print(var.agrrement())
       
        choice = input("\nDo you agree to the terms of service [y/n]: ")
        choice += " "  # b/c method below
        if choice[0].lower() == "y":
            with open("src/agreement", "w") as filewrite:
                filewrite.write("user accepted")

        else:
            exit("Welp have a good day")





        
if os.geteuid() != 0:
    exit(Fore.RED + u"please run me as root")



menu.boot.load_animtion()
    

menu.Menu()


