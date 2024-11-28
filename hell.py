import os
import platform
import re
import json
from datetime import datetime
import time
import subprocess
import sys
import urllib.request
from pystyle import Colors, Colorate, System, Add

def cls():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

icon = r"""
  |\___/|
 /       \
|    /\__/|
||\  <.><.>
| _     > )
 \   /----
  |   -\/
 /     \ """

banner = r"""
   ▄█    █▄       ▄████████  ▄█        ▄█       
  ███    ███     ███    ███ ███       ███       
  ███    ███     ███    █▀  ███       ███       
 ▄███▄▄▄▄███▄▄  ▄███▄▄▄     ███       ███       
▀▀███▀▀▀▀███▀  ▀▀███▀▀▀     ███       ███       
  ███    ███     ███    █▄  ███       ███       
  ███    ███     ███    ███ ███▌    ▄ ███▌    ▄ 
  ███    █▀      ██████████ █████▄▄██ █████▄▄██ 
                            ▀         ▀         """

def color(text: str) -> str:
    def apply(match):
        return Colorate.Color(Colors.red, match.group(0))

    pattern = r"[^a-zA-Z0-9-$:.{}]+"

    return re.sub(pattern, apply, text)

def fade(text: str) -> str:
    return Colorate.Color(Colors.red, text, 1)

menu1 = color(f"""
┌─┬─────────────────┬─────────────────────┬─────────────────┬─────────────────────┬─────────────────┬────────┐
│1│     Network     │                     │      OSINT      │                     │      UTILS      │N - Next│
├─┴─────────────────┴─────────────────────┼─────────────────┴─────────────────────┼─────────────────┴────────┘
├─ [01] Website Vulnerability Scanner     └─ Lookups                              ├─ [12] Phishing Attack
├─ [02] Website Crawler                      ├─ Social                            ├─ [13] IP Generator
├─ [03] Website Pinger                       │  ├─ [07] Username                  └─ [00] Exit
├─ [04] IP Port Scanner                      │  ├─ [08] Phone Number
├─ [05] IP Info                              │  ├─ [09] Email
├─ [06] Wireshark               [PC ONLY]    │  └─ [10] IP
│                                            └─ Other
│                                               └─ [11] Domain""")

menu2 = color(f"""
┌─┬────────────────────────────────────────────────────────────────────────────────────────┬─────────────────┐
│2│                                 Discord [COMING SOON]                                  │N - Next B - Back│
├─┴──────────────────────────┬────────────────────────────┬────────────────────────────┬───┴─────────────────┘
├─ Webhook                   └─ Server                    └─ Account                   └─ Other
│  ├─ [14] Send Message         ├─ [19] Server Info          ├─ [22] Account Info         ├─ [27] Nitro Generator
│  ├─ [15] Send File            ├─ [20] Server Nuker         ├─ [23] Account Nuker        │
│  ├─ [16] Spam Message         ├─ [21] Server Joiner        ├─ [24] Hypesquad Changer    │
│  ├─ [17] Delete Webhook       │                            ├─ [25] Status Changer       │
│  └─ [18] Webhook Info         │                            ├─ [26] User + Nick Changer  │
├───────────────────────────────┴────────────────────────────┴────────────────────────────┘
│""")


folder = "config"
file = os.path.join(folder, "config.json")

if not os.path.exists(folder):
    os.makedirs(folder)

def load_config():
    global page
    if os.path.exists(file):
        with open(file, "r") as f:
            data = json.load(f)
            page = data.get("page", 1)
    else:
        page = 1

def save_config():
    with open(file, "w") as f:
        json.dump({"page": page}, f)

username = os.getlogin()
page = 1
max_pages = 2

load_config()

def next_page():
    global page
    if page < max_pages:
        page += 1
        save_config()

def back_page():
    global page
    if page > 1:
        page -= 1
        save_config()

def exit():
    save_config()
    sys.exit()

commands = {
    "01": lambda: print("Website Vulnerability Scanner"),
    "02": lambda: print("Website Crawler"),
    "03": lambda: print("Website Pinger"),
    "04": lambda: print("IP Port Scanner"),
    "05": lambda: print("IP Info"),
    "06": lambda: print("Wireshark"),
    "07": lambda: print("Lookup Username"),
    "08": lambda: print("Lookup Phone Number"),
    "09": lambda: print("Lookup Email"),
    "10": lambda: print("Lookup IP"),
    "11": lambda: print("Lookup Domain"),
    "12": lambda: print("Phishing Attack"),
    "13": lambda: print("IP Generator"),
    "N": next_page,
    "B": back_page,
    "00": exit
}

def render():
    cls()
    global page
    print(Colorate.Vertical(Colors.red_to_black, Add.Add(banner, icon, 0)))
    
    if page == 1:
        os.system("title H Ǝ L L ~ 1")
        print(menu1)
    elif page == 2:
        os.system("title H Ǝ L L ~ 2")
        print(menu2)
    else:
        pass

def main():
    while True:
        os.system("mode 120, 30")
        render()
        cmd = input(color("└─$ ")).strip()
        if cmd in commands:
            commands[cmd]()
        else:
            print(f"{fade('[')}{datetime.now().strftime('%H:%M:%S')}{fade(']')} {fade('[')}{Colorate.Color(Colors.red, "-")}{fade(']')} Invalid command.")
            time.sleep(2)

if __name__ == "__main__":
    main()
