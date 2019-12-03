#! /bin/python3 
from colorama import Fore, Style
from os import system as cmd
import os
import src


        
if os.geteuid() != 0:
    exit(Fore.RED + u"please run me as root")

src.menu.boot.load_animtion()
    

src.menu.Menu()


