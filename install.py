#! /usr/bin/python3
from os import system as cmd
from time import sleep
from colorama import Fore, Style
import platform
import os

try:
    system = platform.system()
    if system == "Windows":
        exit("this isnt linux you dingus")


    if os.geteuid() != 0:
        exit("please run me as root")

    cmd("chmod +x ./watchmen.py")
    #installing the train option and some other stuff since im to lazy to make it myself
    cmd("apt install -y sl python3-pip python3 python-pip")
    sleep(1)
    cmd("pip3 install -r requirements.txt")




except KeyboardInterrupt:
    print("\nINSTALL FAILED!!")
