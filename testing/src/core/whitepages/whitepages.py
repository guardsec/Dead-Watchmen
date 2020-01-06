from colorama import Fore, Style, Back
from ...core.ToLazyToTypeOver import clear
import os


def winfo():
    clear()
    print(Fore.RED + u""" 
█     █░ ██▓ ███▄    █   █████▒▒█████  
▓█░ █ ░█░▓██▒ ██ ▀█   █ ▓██   ▒▒██▒  ██▒
▒█░ █ ░█ ▒██▒▓██  ▀█ ██▒▒████ ░▒██░  ██▒
░█░ █ ░█ ░██░▓██▒  ▐▌██▒░▓█▒  ░▒██   ██░
░░██▒██▓ ░██░▒██░   ▓██░░▒█░   ░ ████▓▒░
░ ▓░▒ ▒  ░▓  ░ ▒░   ▒ ▒  ▒ ░   ░ ▒░▒░▒░ 
  ▒ ░ ░   ▒ ░░ ░░   ░ ▒░ ░       ░ ▒ ▒░ 
  ░   ░   ▒ ░   ░   ░ ░  ░ ░   ░ ░ ░ ▒  
    ░     ░           ░            ░ ░  
                                        """)

    FN = input(Fore.WHITE + "First Name: ")
    LN = input("Last Name: ")
    CSA = input("City/State/Area code: ")

    print("https://www.whitepages.com/name/" + FN + "-" + LN + "/" + CSA + "?fs=1&l=" + CSA + "&q=" + FN + "+" + LN)
    input("press enter to return to tools screen")

def pinfo():
    clear()
    print(Fore.RED + u"""
    
 ██▓███   ██▓ ███▄    █   █████▒▒█████  
▓██░  ██▒▓██▒ ██ ▀█   █ ▓██   ▒▒██▒  ██▒
▓██░ ██▓▒▒██▒▓██  ▀█ ██▒▒████ ░▒██░  ██▒
▒██▄█▓▒ ▒░██░▓██▒  ▐▌██▒░▓█▒  ░▒██   ██░
▒██▒ ░  ░░██░▒██░   ▓██░░▒█░   ░ ████▓▒░
▒▓▒░ ░  ░░▓  ░ ▒░   ▒ ▒  ▒ ░   ░ ▒░▒░▒░ 
░▒ ░      ▒ ░░ ░░   ░ ▒░ ░       ░ ▒ ▒░ 
░░        ▒ ░   ░   ░ ░  ░ ░   ░ ░ ░ ▒  
          ░           ░            ░ ░  
                                        """)

    AC = input(Fore.WHITE + "area code of the person: ")
    PN = input("phone number (ex: 111-111-1111): ")
    print("https://www.whitepages.com/phone/" + AC + "-" + PN)