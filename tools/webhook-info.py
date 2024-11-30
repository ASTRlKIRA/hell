import requests
from datetime import datetime
import json
from pystyle import Colors, Colorate
from datetime import datetime
import os

def fade(text: str) -> str:
    return Colorate.Color(Colors.red, text, 1)

def info(webhook_url):
    time = datetime.now().strftime("%H:%M:%S")
    try:
        response = requests.get(webhook_url)

        if response.status_code == 200:
            webhook_info = response.json()
            time = datetime.now().strftime("%H:%M:%S")
            print(f"{fade('[')}{time}{fade(']')} Raw Data:")
            print(json.dumps(webhook_info, indent=4))

            time = datetime.now().strftime("%H:%M:%S")
            print(f"{fade('[')}{time}{fade(']')} Summary:")
            print(f"{fade('[')}{time}{fade(']')} {fade('[')}{Colorate.Color(Colors.green, '+')}{fade(']')} Webhook Name: {webhook_info.get('name')}")
            print(f"{fade('[')}{time}{fade(']')} {fade('[')}{Colorate.Color(Colors.green, '+')}{fade(']')} Webhook ID: {webhook_info.get('id')}")
            print(f"{fade('[')}{time}{fade(']')} {fade('[')}{Colorate.Color(Colors.green, '+')}{fade(']')} Guild ID: {webhook_info.get('guild_id')}")
            print(f"{fade('[')}{time}{fade(']')} {fade('[')}{Colorate.Color(Colors.green, '+')}{fade(']')} Channel ID: {webhook_info.get('channel_id')}")
        else:
            print(f"{fade('[')}{time}{fade(']')} {fade('[')}{Colorate.Color(Colors.red, 'x')}{fade(']')} Failed to fetch webhook info. Status code: {response.status_code}")
    except Exception as e:
        print(f"[{time}] Error: {e}")

if __name__ == "__main__":
    time = datetime.now().strftime("%H:%M:%S")
    webhook_url = input(f"\n{fade('[')}{time}{fade(']')} > Enter Webhook URL: ")
    info(webhook_url)

    time = datetime.now().strftime("%H:%M:%S")
    input(f"{fade('[')}{time}{fade(']')} Press any key to go back.")
    os.system("python hell.py")
