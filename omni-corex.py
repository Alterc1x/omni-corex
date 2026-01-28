import os,sys
import time
import requests
from colorama import init, Style, Fore

os.system("clear" if os.name != "nt" else "cls")

# Software Utilities
init(autoreset=True)

W = Fore.WHITE
G = Fore.GREEN
R = Fore.RED
B = Fore.BLACK
b = Fore.BLUE
C = Fore.CYAN
r = Style.RESET_ALL

# Software INFO

app_name = os.path.basename(__file__)
app_path = os.getcwd()
app_vers = 0.1
authors = ("Alterc1x", "Bullsux")
hash_ver = "" # currently empty please get back on this asap

def auto_update():
    pass # will check for internet, if fails then it will cancel else it will auto update

class ART_BANNER:

    logo = fr"""{R}
                           ▒█████   ███▄ ▄███▓ ███▄    █  ██▓     
                          ▒██▒  ██▒▓██▒▀█▀ ██▒ ██ ▀█   █ ▓██▒     
                          ▒██░  ██▒▓██    ▓██░▓██  ▀█ ██▒▒██▒     
                          ▒██   ██░▒██    ▒██ ▓██▒  ▐▌██▒░██░     
                          ░ ████▓▒░▒██▒   ░██▒▒██░   ▓██░░██░     
                          ░ ▒░▒░▒░ ░ ▒░   ░  ░░ ▒░   ▒ ▒ ░▓       
                            ░ ▒ ▒░ ░  ░      ░░ ░░   ░ ▒░ ▒ ░     
                          ░ ░ ░ ▒  ░      ░      ░   ░ ░  ▒ ░     
                              ░ ░         ░            ░  ░       
                                                                 {C} 
                        ▄████▄   ▒█████   ██▀███  ▓█████ ▒██   ██▒
                       ▒██▀ ▀█  ▒██▒  ██▒▓██ ▒ ██▒▓█   ▀ ▒▒ █ █ ▒░
                       ▒▓█    ▄ ▒██░  ██▒▓██ ░▄█ ▒▒███   ░░  █   ░
                       ▒▓▓▄ ▄██▒▒██   ██░▒██▀▀█▄  ▒▓█  ▄  ░ █ █ ▒ 
                       ▒ ▓███▀ ░░ ████▓▒░░██▓ ▒██▒░▒████▒▒██▒ ▒██▒
                       ░ ░▒ ▒  ░░ ▒░▒░▒░ ░ ▒▓ ░▒▓░░░ ▒░ ░▒▒ ░ ░▓ ░
                         ░  ▒     ░ ▒ ▒░   ░▒ ░ ▒░ ░ ░  ░░░   ░▒ ░
                       ░        ░ ░ ░ ▒    ░░   ░    ░    ░    ░  
                       ░ ░          ░ ░     ░        ░  ░ ░    ░  
                       ░                                          {r}

          =====================|| MULTI PURPOSE TOOL ||======================
                            {R}Author(s) : @{authors[0]}, @{authors[1]}
                            {b}App Versi : {app_vers}v
"""
    
class Main:

    def main_menu(self):
        print(ART_BANNER.logo)
        input(f"{G}Press ENTER To Continue...")
        time.sleep(1)
        pass
    
    def main(self):
        pass

if __name__ == "__main__":
    try:
        Main = Main()
        Main.main_menu()

    except KeyboardInterrupt:
        sys.exit()
