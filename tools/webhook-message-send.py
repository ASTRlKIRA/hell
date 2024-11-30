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

def fade(text: str) -> str:
    return Colorate.Color(Colors.red, text, 1)

def send(url, message):
    pfp = load_config()
    headers = {
        "Content-Type": "application/json"
    }
    data = {
        "content": message,
        "username": "HELL",
        "avatar_url": pfp
    }
    try:
        response = requests.post(url, headers=headers, json=data)
        if response.status_code == 204:
            print(f"{fade('[')}{time}{fade(']')} {fade('[')}{Colorate.Color(Colors.green, '+')}{fade(']')} Message sent successfully.")
        else:
            print(f"{fade('[')}{time}{fade(']')} {fade('[')}{Colorate.Color(Colors.red, 'x')}{fade(']')} Failed to send message. Status code: {Colorate.Color(Colors.red, response.status_code)}")
    except requests.exceptions.RequestException as e:
        print(f"{fade('[')}{time}{fade(']')} {fade('[')}{Colorate.Color(Colors.red, 'x')}{fade(']')} Error occurred: {Colorate.Color(Colors.red, str(e))}")

if __name__ == "__main__":
    time = datetime.now().strftime("%H:%M:%S")
    url = input(f"\n{fade('[')}{time}{fade(']')} > Enter Webhook URL: ")
    message = input(f"{fade('[')}{time}{fade(']')} > Enter Message: ")

    send(url, message)

    time = datetime.now().strftime("%H:%M:%S")
    input(f"{fade('[')}{time}{fade(']')} Press any key to go back.")
    os.system("python hell.py")  
