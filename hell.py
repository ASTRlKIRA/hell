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

def vuln_scan():
    os.system("python tools/website-vulnerability-scanner.py")

def website_crawler():
    os.system("python tools/website-crawler.py")

def website_pinger():
    os.system("python tools/website-pinger.py")

def ip_port_scanner():
    os.system("python tools/ip-port-scanner.py")

def ip_info():
    os.system("python tools/ip-info.py")

def wireshark():
    os.system("python tools/wireshark.py")

def username_lookup():
    os.system("python tools/username-lookup.py")

def phone_number_lookup():
    os.system("python tools/phone-number-lookup.py")

def email_lookup():
    os.system("python tools/email-lookup.py")

def ip_lookup():
    os.system("python tools/ip-lookup.py")

def domain_lookup():
    os.system("python tools/domain-lookup.py")

def phishing_attack():
    os.system("python tools/phishing-attack.py")

def ip_generator():
    os.system("python tools/ip-generator.py")

def webhook_message_send():
    os.system("python tools/webhook-message-send.py")

def webhook_file_send():
    os.system("python tools/webhook-file-send.py")

def webhook_spam_message():
    os.system("python tools/webhook-spam-message.py")

def webhook_delete():
    os.system("python tools/webhook-delete.py")

def webhook_info():
    os.system("python tools/webhook-info.py")

commands = {
    "01": vuln_scan,
    "02": website_crawler,
    "03": website_pinger,
    "04": ip_port_scanner,
    "05": ip_info,
    "06": wireshark,
    "07": username_lookup,
    "08": phone_number_lookup,
    "09": email_lookup,
    "10": ip_lookup,
    "11": domain_lookup,
    "12": phishing_attack,
    "13": ip_generator,
    "14": webhook_message_send,
    "15": webhook_file_send,
    "16": webhook_spam_message,
    "17": webhook_delete,
    "18": webhook_info,
    "N": next_page,
    "B": back_page,
    "00": exit
}

def render():
    cls()
    global page
    print(Colorate.Vertical(Colors.red_to_black, Add.Add(banner, icon, 0)))
    
    if page == 1:
        if platform.system() == "Windows":
            os.system("title H Ǝ L L ~ 1")
        else:
            pass
        print(menu1)
    elif page == 2:
        if platform.system() == "Windows":
            os.system("title H Ǝ L L ~ 2")
        else:
            pass
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
