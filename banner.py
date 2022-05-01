from colorama import Fore as color
from time import sleep 

bold = '\033[1m'
endbold = '\033[0m'

def banner():
    print(color.RED+"""
 __   __ _          __  __      
 |  \/  | |__  _ __ \ \/ /_ __  
 | |\/| | '_ \| '_ \ \  /| '_ \ 
 | |  | | | | | | | |/  \| |_) |
 |_|  |_|_| |_|_| |_/_/\_\ .__/ 
                         |_|     version 1.0 --- Hex Rot13 Base64 """)
    sleep(0.1)

    print(bold+color.WHITE+'''
    ----------------------------------    
    ⚒  Telegram : Mahan_Unique      ⚒
    ----------------------------------
     '''+endbold)  
    sleep(1)
def menu():

    print(bold+color.WHITE+"[1]" +color.LIGHTYELLOW_EX+" Base64")
    print(color.CYAN+"*********************")
    sleep(0.1)
    print(bold+color.WHITE+"[2]"+color.LIGHTYELLOW_EX+" Hex")
    print(color.CYAN+"*********************")
    sleep(0.1)
    print(bold+color.WHITE+"[3]"+color.LIGHTYELLOW_EX+" Rot13")
    print(color.CYAN+"*********************")
    sleep(0.1)
    print(bold+color.WHITE+"[4]"+color.LIGHTYELLOW_EX+" Decoder")
    print(color.CYAN+"*********************")
    sleep(0.1)
    print(bold+color.WHITE+"[0]"+color.LIGHTYELLOW_EX+" exit"+endbold)



def decoder_menu():
    print(bold+color.WHITE+"[1]" +color.LIGHTYELLOW_EX+" Base64")
    print(color.CYAN+"*********************")
    sleep(0.1)
    print(bold+color.WHITE+"[2]"+color.LIGHTYELLOW_EX+" Hex")
    print(color.CYAN+"*********************")
    sleep(0.1)
    print(bold+color.WHITE+"[3]"+color.LIGHTYELLOW_EX+" Rot13")
    print(color.CYAN+"*********************")
    sleep(0.1)
    print(bold+color.WHITE+"[0]"+color.LIGHTYELLOW_EX+" back"+endbold)