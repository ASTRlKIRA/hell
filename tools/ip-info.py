import requests
import ipaddress
from pystyle import Colors, Colorate
import os
from datetime import datetime

def fade(text: str) -> str:
    return Colorate.Color(Colors.red, text, 1)

def version(ip_address):
    try:
        ip = ipaddress.ip_address(ip_address)
        ip_version = "IPv4" if ip.version == 4 else "IPv6"
        return ip_version
    except ValueError:
        return "Invalid IP", "Unknown"

def info(ip_address=""):
    try:
        url = f"https://ipinfo.io/{ip_address}/json"
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        ip = data.get("ip", "N/A")
        hostname = data.get("hostname", "N/A")
        city = data.get("city", "N/A")
        region = data.get("region", "N/A")
        country = data.get("country", "N/A")
        loc = data.get("loc", "N/A")
        org = data.get("org", "N/A")
        postal = data.get("postal", "N/A")
        timezone = data.get("timezone", "N/A")

        ip_version = version(ip)

        time = datetime.now().strftime("%H:%M:%S")

        print(f"{fade("[")}{time}{fade("]")} {fade('[')}{Colorate.Color(Colors.green, '+')}{fade(']')} IP: {ip}")
        print(f"{fade("[")}{time}{fade("]")} {fade('[')}{Colorate.Color(Colors.green, '+')}{fade(']')} Host Name: {hostname}")
        print(f"{fade("[")}{time}{fade("]")} {fade('[')}{Colorate.Color(Colors.green, '+')}{fade(']')} Host Country: {country}")
        print(f"{fade("[")}{time}{fade("]")} {fade('[')}{Colorate.Color(Colors.green, '+')}{fade(']')} Region: {region}")
        print(f"{fade("[")}{time}{fade("]")} {fade('[')}{Colorate.Color(Colors.green, '+')}{fade(']')} City: {city}")
        print(f"{fade("[")}{time}{fade("]")} {fade('[')}{Colorate.Color(Colors.green, '+')}{fade(']')} Location (Lat, Long): {loc}")
        print(f"{fade("[")}{time}{fade("]")} {fade('[')}{Colorate.Color(Colors.green, '+')}{fade(']')} Postal Code: {postal}")
        print(f"{fade("[")}{time}{fade("]")} {fade('[')}{Colorate.Color(Colors.green, '+')}{fade(']')} Timezone: {timezone}")
        print(f"{fade("[")}{time}{fade("]")} {fade('[')}{Colorate.Color(Colors.green, '+')}{fade(']')} ISP/Organization: {org}")
        print(f"{fade("[")}{time}{fade("]")} {fade('[')}{Colorate.Color(Colors.green, '+')}{fade(']')} IP Version: {ip_version}")

    except requests.exceptions.RequestException as e:
        time = datetime.now().strftime("%H:%M:%S")
        print(f"{fade("[")}{time}{fade("]")} {fade('[')}{Colorate.Color(Colors.red, 'x')}{fade(']')} Error fetching IP info: {Colorate.Color(Colors.red, f"{e}")}")
    except ValueError as ve:
        time = datetime.now().strftime("%H:%M:%S")
        print(f"{fade("[")}{time}{fade("]")} {fade('[')}{Colorate.Color(Colors.red, 'x')}{fade(']')} Invalid IP address: {Colorate.Color(Colors.red, f"{ve}")}")

if __name__ == "__main__":
    banner = r"""

             ..,,;;;;;;,,,,
       .,;'';;,..,;;;,,,,,.''';;,..
    ,,''                    '';;;;,;''
   ;'    ,;@@;'  ,@@;, @@, ';;;@@;,;';.
  ''  ,;@@@@@'  ;@@@@; ''    ;;@@@@@;;;;
     ;;@@@@@;    '''     .,,;;;@@@@@@@;;;
    ;;@@@@@@;           , ';;;@@@@@@@@;;;.
     '';@@@@@,.  ,   .   ',;;;@@@@@@;;;;;;
        .   '';;;;;;;;;,;;;;@@@@@;;' ,.:;'
          ''..,,     ''''    '  .,;'
               ''''''::''''''''
"""

    print(Colorate.Vertical(Colors.red_to_black, banner, 1))
    time = datetime.now().strftime("%H:%M:%S")
    ip = input(f"\n{fade("[")}{time}{fade("]")} > Enter IP: ").strip()
    info(ip)

    time = datetime.now().strftime("%H:%M:%S")
    input(f"{fade("[")}{time}{fade("]")} Press any key to go back.")
    os.system("python hell.py")
