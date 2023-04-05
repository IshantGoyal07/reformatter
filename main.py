import os
import time
import fade
import colorama
from dataclasses import replace
from colorama import init, Fore
from dataclasses import replace

init(autoreset=True)

os.system('mode con: cols=130 lines=25')

colorama.deinit()
os.system("title EGYPT VCC REFORMATTER")
os.system('cls' if os.name == 'nt' else 'clear')

print(fade.purpleblue("""  
██████   ██████   ██████  ███████ ████████     ██    ██ ███    ██ ██ ██    ██ ███████ ██████  ███████ ███████ 
██   ██ ██    ██ ██    ██ ██         ██        ██    ██ ████   ██ ██ ██    ██ ██      ██   ██ ██      ██      
██████  ██    ██ ██    ██ ███████    ██        ██    ██ ██ ██  ██ ██ ██    ██ █████   ██████  ███████ █████   
██   ██ ██    ██ ██    ██      ██    ██        ██    ██ ██  ██ ██ ██  ██  ██  ██      ██   ██      ██ ██      
██████   ██████   ██████  ███████    ██         ██████  ██   ████ ██   ████   ███████ ██   ██ ███████ ███████ 
                                                                                                              
                                                                                                              

"""))
colorama.init(autoreset=True)
time.sleep(2)

with open("input.txt", "r", encoding="utf-8") as f:
    input = f.readlines()

colorama.deinit()
print(fade.purpleblue("Reformatting..."))
time.sleep(2)
colorama.init(autoreset=True)

for i in input:
    i.replace("\n", "")
    if(i.find("URL:") != -1):
        input.remove(i)
    if(i.find("Online Payment Card Details: ") != -1):
        input.remove(i)
    if(i.find("Card value: 1.00 EGP ") != -1):
        input.remove(i)

haunt = ""

for i in input:
    if(i.find("Card number: ") != -1):
        haunt = haunt + i.replace("Card number: ", "").replace("\n", "")
    if(i.find("Exp Date: ") != -1):
        haunt = haunt + ":" + i.replace("Exp Date: ", "").replace("\n", "")
    if(i.find("CVC: ") != -1):
        haunt = haunt + ":" + i.replace("CVC: ", "")

haunt = haunt.replace(" ", "").replace("/", "")
with open("output.txt", "w", encoding="utf-8") as f:
    f.write(haunt)
    f.close

print(Fore.RED + "Successfully Formatted Vcc")
print(Fore.GREEN + "Saved In Output.Txt")
time.sleep(1)
colorama.deinit()
print(fade.purpleblue("Closing..."))
time.sleep(2)
colorama.init(autoreset=True)
time.sleep(1)
os._exit(1) 