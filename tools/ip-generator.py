import random
import threading
from pystyle import Colors, Colorate
import os
from datetime import datetime

def fade(text: str) -> str:
    return Colorate.Color(Colors.red, text, 1)

def gen():
    return '.'.join(str(random.randint(0, 255)) for _ in range(4))

def valid(ip):
    octets = ip.split('.')
    
    if len(octets) != 4:
        return False
    
    for octet in octets:
        if not octet.isdigit():
            return False
        if not (0 <= int(octet) <= 255):
            return False
    
    return True

def check():
    random_ip = gen()
    if valid(random_ip):
        time = datetime.now().strftime("%H:%M:%S")
        print(f"{fade("[")}{time}{fade("]")} {fade("[")}{Colorate.Color(Colors.green, "+")}{fade("]")} {random_ip} ~ {Colorate.Color(Colors.green, "valid")}.")
    else:
        time = datetime.now().strftime("%H:%M:%S")
        print(f"{fade("[")}{time}{fade("]")} {fade("[")}{Colorate.Color(Colors.red, "-")}{fade("]")} {random_ip} ~ {Colorate.Color(Colors.red, "invalid")}.")

def start(num_checks):
    threads = []
    for _ in range(num_checks):
        thread = threading.Thread(target=check)
        threads.append(thread)
        thread.start()
    
    for thread in threads:
        thread.join()



if __name__ == "__main__":
    times = datetime.now().strftime("%H:%M:%S")
    num_checks = int(input(f"\n{fade('[')}{times}{fade(']')} > Ammount: "))
    num_checks = min(num_checks, 50)

    start(num_checks)

    time = datetime.now().strftime("%H:%M:%S")
    input(f"{fade("[")}{time}{fade("]")} Press any key to go back.")
    os.system("python hell.py")