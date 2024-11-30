import requests
from pystyle import Colors, Colorate
import re
from datetime import datetime
import os
import json

folder = "config"
file = os.path.join(folder, "config.json")

def load_config():
    if os.path.exists(file):
        with open(file, "r") as f:
            data = json.load(f)
            pfp_url = data.get("pfp_url", "")
            return pfp_url

def color(text: str) -> str:
    def apply(match):
        return Colorate.Color(Colors.red, match.group(0))

    pattern = r"[^a-zA-Z0-9-$:.{}]+"
    return re.sub(pattern, apply, text)

def fade(text: str) -> str:
    return Colorate.Color(Colors.red, text, 1)

def send(url, file_url):
    pfp = load_config()
    time = datetime.now().strftime("%H:%M:%S")
    headers = {
        "Content-Type": "application/json"
    }
    data = {
        "content": f"{file_url}",
        "username": "HELL",
        "avatar_url": pfp
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 204:
        print(f"{fade('[')}{time}{fade(']')} {fade('[')}{Colorate.Color(Colors.green, '+')}{fade(']')} File sent successfully.")
    else:
        print(f"{fade('[')}{time}{fade(']')} {fade('[')}{Colorate.Color(Colors.red, 'x')}{fade(']')} Failed to send file URL. Status code: {Colorate.Color(Colors.red, str(response.status_code))}")

if __name__ == "__main__":
    time = datetime.now().strftime("%H:%M:%S")
    url = input(f"\n{fade('[')}{time}{fade(']')} > Enter Webhook URL: ")
    file_url = input(f"{fade('[')}{time}{fade(']')} > Enter file URL: ")

    send(url, file_url)

    time = datetime.now().strftime("%H:%M:%S")
    input(f"{fade('[')}{time}{fade(']')} Press any key to go back.")
    os.system("python hell.py")
