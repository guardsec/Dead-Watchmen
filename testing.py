# importing the necessary packages 
import time 
import sys 
import os 
from colorama import Fore, Style

__authors__ = u'"Tibthink, Faded-Atlas"'
__version__ = '0.1'
  
# Function for implementing the loading animation 
def load_animation(): 
  
    # String to be displayed when the application is loading 
    load_str = "Starting DeadWatch Men"
    ls_len = len(load_str) 

    animation = "|/-\\"
    anicount = 0

    counttime = 0        
      

    i = 0                     
  
    while (counttime != 100): 
        time.sleep(0.075)                        
        load_str_list = list(load_str)  
        x = ord(load_str_list[i]) 
        y = 0                             
        if x != 32 and x != 46:              
            if x>90: 
                y = x-32
            else: 
                y = x + 32
            load_str_list[i]= chr(y) 
        res =''              
        for j in range(ls_len): 
            res = res + load_str_list[j] 
        sys.stdout.write("\r"+res + animation[anicount]) 
        sys.stdout.flush() 
        load_str = res 
        anicount = (anicount + 1)% 4
        i =(i + 1)% ls_len 
        counttime = counttime + 1
      
    # for windows OS 
    if os.name =="nt": 
        os.system("cls") 
         
    # for linux / Mac OS 
    else: 
        os.system("clear") 
  
# Driver program 
if __name__ == '__main__':  
    load_animation() 
  
    # Your desired code continues from here  
    # s = input("Enter your name: ") 
    s = (Fore.RED + u"""

▓█████▄ ▓█████ ▄▄▄      ▓█████▄     █     █░ ▄▄▄     ▄▄▄█████▓ ▄████▄   ██░ ██  ███▄ ▄███▓▓█████  ███▄    █ 
▒██▀ ██▌▓█   ▀▒████▄    ▒██▀ ██▌   ▓█░ █ ░█░▒████▄   ▓  ██▒ ▓▒▒██▀ ▀█  ▓██░ ██▒▓██▒▀█▀ ██▒▓█   ▀  ██ ▀█   █ 
░██   █▌▒███  ▒██  ▀█▄  ░██   █▌   ▒█░ █ ░█ ▒██  ▀█▄ ▒ ▓██░ ▒░▒▓█    ▄ ▒██▀▀██░▓██    ▓██░▒███   ▓██  ▀█ ██▒
░▓█▄   ▌▒▓█  ▄░██▄▄▄▄██ ░▓█▄   ▌   ░█░ █ ░█ ░██▄▄▄▄██░ ▓██▓ ░ ▒▓▓▄ ▄██▒░▓█ ░██ ▒██    ▒██ ▒▓█  ▄ ▓██▒  ▐▌██▒
░▒████▓ ░▒████▒▓█   ▓██▒░▒████▓    ░░██▒██▓  ▓█   ▓██▒ ▒██▒ ░ ▒ ▓███▀ ░░▓█▒░██▓▒██▒   ░██▒░▒████▒▒██░   ▓██░
▒▒▓  ▒ ░░ ▒░ ░▒▒   ▓▒█░ ▒▒▓  ▒    ░ ▓░▒ ▒   ▒▒   ▓▒█░ ▒ ░░   ░ ░▒ ▒  ░ ▒ ░░▒░▒░ ▒░   ░  ░░░ ▒░ ░░ ▒░   ▒ ▒ 
░ ▒  ▒  ░ ░  ░ ▒   ▒▒ ░ ░ ▒  ▒      ▒ ░ ░    ▒   ▒▒ ░   ░      ░  ▒    ▒ ░▒░ ░░  ░      ░ ░ ░  ░░ ░░   ░ ▒░
░ ░  ░    ░    ░   ▒    ░ ░  ░      ░   ░    ░   ▒    ░      ░         ░  ░░ ░░      ░      ░      ░   ░ ░ 
░       ░  ░     ░  ░   ░           ░          ░  ░        ░ ░       ░  ░  ░       ░      ░  ░         ░ 
░                       ░                                    ░                                             
    
Code name: bassoon
Created by {__authors__}
Version: {__version__} 
    """.format(__authors__=__authors__, __version__=__version__))
    sys.stdout.write(str(s))



