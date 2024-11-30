import requests
from pystyle import Colors, Colorate
from datetime import datetime
import os

def fade(text: str) -> str:
    return Colorate.Color(Colors.red, text, 1)

def delete(webhook_url):
    time = datetime.now().strftime("%H:%M:%S")
    try:
        response = requests.delete(webhook_url)

        if response.status_code == 204:
            print(f"{fade('[')}{time}{fade(']')} {fade('[')}{Colorate.Color(Colors.green, '+')}{fade(']')} Webhook deleted successfully.")
        else:
            print(f"{fade('[')}{time}{fade(']')} {fade('[')}{Colorate.Color(Colors.red, 'x')}{fade(']')} Failed to delete webhook. Status code: {Colorate.Color(Colors.red, response.status_code)}")
    except Exception as e:
        print(f"{fade('[')}{time}{fade(']')} {fade('[')}{Colorate.Color(Colors.red, 'x')}{fade(']')} Error: {e}")


if __name__ == "__main__":
    time = datetime.now().strftime("%H:%M:%S")
    webhook_url = input(f"\n{fade('[')}{time}{fade(']')} > Enter Webhook URL: ")

    delete(webhook_url)

    time = datetime.now().strftime("%H:%M:%S")
    input(f"{fade('[')}{time}{fade(']')} Press any key to go back.")
    os.system("python hell.py")
