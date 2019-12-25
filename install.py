#! /usr/bin/python3
from os import system as cmd
from time import sleep
import platform
import os

system = platform.system()
if system == "Windows":
    exit("this isnt linux you dingus")


if os.geteuid() != 0:
    exit(u"please run me as root")

cmd("chmod +x ./watchmen.py")
sleep(1)
cmd("pip3 install -r requirements.txt")

#installing the train option since im to lazy to make it myself
cmd("apt install sl")
