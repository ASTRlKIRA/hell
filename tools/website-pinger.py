import requests
import time
from pystyle import Colors, Colorate
import os
from datetime import datetime

def fade(text: str) -> str:
    return Colorate.Color(Colors.red, text, 1)

def ping(url):
    try:
        start_time = time.time()
        response = requests.get(url, timeout=10)
        end_time = time.time()
        
        response_time = round((end_time - start_time) * 1000, 2)
        times = datetime.now().strftime("%H:%M:%S")
        
        if response.status_code == 200:
            return f"{fade('[')}{times}{fade(']')} {fade('[')}{Colorate.Color(Colors.green, '+')}{fade(']')} {url} > {response.status_code} | Response time: {response_time}ms"
        else:
            return f"{fade('[')}{times}{fade(']')} {fade('[')}{Colorate.Color(Colors.red, 'x')}{fade(']')} {url} > {response.status_code} | Response time: {response_time}ms"
    except requests.exceptions.RequestException as e:
        times = datetime.now().strftime("%H:%M:%S")
        return f"{fade('[')}{times}{fade(']')} {fade('[')}{Colorate.Color(Colors.red, 'x')}{fade(']')} Error: {Colorate.Color(Colors.red, f"{e}")}"

if __name__ == "__main__":
    times = datetime.now().strftime("%H:%M:%S")
    url = input(f"\n{fade('[')}{times}{fade(']')} > Enter URL: ").strip()
    times = datetime.now().strftime("%H:%M:%S")
    
    try:
        pings = int(input(f"{fade('[')}{times}{fade(']')} > Pings: "))
    except ValueError:
        print(f"{fade('[')}{datetime.now().strftime('%H:%M:%S')}{fade(']')} {fade('[')}{Colorate.Color(Colors.red, 'x')}{fade(']')} Invalid input. Please enter a number.")
        exit()

    if not url.startswith("http://") and not url.startswith("https://"):
        url = "http://" + url
    
    for i in range(pings):
        print(ping(url))
        if i < pings - 1:
            time.sleep(1)

    time = datetime.now().strftime("%H:%M:%S")
    input(f"{fade("[")}{time}{fade("]")} Press any key to go back.")
    os.system("python hell.py")
