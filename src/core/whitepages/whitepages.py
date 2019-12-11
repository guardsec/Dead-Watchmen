from colorama import Fore, Style, Back
import os


def info():
    os.system("clear")
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

    FN = input("First Name: ")
    LN = input("Last Name: ")
    CSA = input("City/State/Area code: ")

    print("https://www.whitepages.com/name/" + FN + "-" + LN + "/" + CSA + "?fs=1&l=" + CSA + "&q=" + FN + "+" + LN)




