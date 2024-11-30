import requests
import threading
from pystyle import Colors, Colorate
import re
from datetime import datetime
from queue import Queue
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

semaphore = threading.Semaphore(50)
successful_messages = 0
successful_messages_lock = threading.Lock()

def color(text: str) -> str:
    def apply(match):
        return Colorate.Color(Colors.red, match.group(0))

    pattern = r"[^a-zA-Z0-9-$:.{}]+"
    return re.sub(pattern, apply, text)

def fade(text: str) -> str:
    return Colorate.Color(Colors.red, text, 1)

def send(url, message, queue):
    pfp = load_config()
    global successful_messages
    while True:
        try:
            with semaphore:
                headers = {
                    "Content-Type": "application/json"
                }
                data = {
                    "content": message,
                    "username": "HELL",
                    "avatar_url": pfp
                }

                response = requests.post(url, headers=headers, json=data)

                if response.status_code == 204:
                    time = datetime.now().strftime("%H:%M:%S")
                    with successful_messages_lock:
                        successful_messages += 1
                    print(f"{fade('[')}{time}{fade(']')} {fade('[')}{Colorate.Color(Colors.green, '+')}{fade(']')} Message sent successfully.")
                    queue.task_done()
                    break
                else:
                    time = datetime.now().strftime("%H:%M:%S")
                    print(f"{fade('[')}{time}{fade(']')} {fade('[')}{Colorate.Color(Colors.red, 'x')}{fade(']')} Failed to send message. Retrying...")

        except Exception as e:
            time = datetime.now().strftime("%H:%M:%S")
            print(f"{fade('[')}{time}{fade(']')} {fade('[')}{Colorate.Color(Colors.red, 'x')}{fade(']')} Error: {e}. {Colorate.Color(Colors.yellow, 'Retrying...')}")

def threaded(url, message, amount):
    amount = int(amount)
    queue = Queue()

    for _ in range(amount):
        queue.put(None)

    threads = []
    for _ in range(50):
        thread = threading.Thread(target=send, args=(url, message, queue))
        thread.start()
        threads.append(thread)

    queue.join()

    for thread in threads:
        thread.join()


if __name__ == "__main__":
    time = datetime.now().strftime("%H:%M:%S")
    url = input(f"\n{fade('[')}{time}{fade(']')} > Enter Webhook URL: ")
    message = input(f"{fade('[')}{time}{fade(']')} > Enter Message: ")
    amount = input(f"{fade('[')}{time}{fade(']')} > Enter Amount: ")

    threaded(url, message, amount)


    time = datetime.now().strftime("%H:%M:%S")
    input(f"{fade('[')}{time}{fade(']')} Press any key to go back.")
    os.system("python hell.py")
