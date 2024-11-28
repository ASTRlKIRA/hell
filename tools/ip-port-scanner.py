import socket
import threading
from queue import Queue
from pystyle import Colors, Colorate
import os
from datetime import datetime

def fade(text: str) -> str:
    return Colorate.Color(Colors.red, text, 1)

THREADSCOUNT = 50

def scanport(ip, port, results):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(0.1)
        try:
            s.connect((ip, port))
            try:
                protocol = socket.getservbyport(port)
            except OSError:
                protocol = "Unknown"
            results[port] = f"{Colorate.Color(Colors.green, "OPEN")} {fade("[")}{protocol}{fade("]")}"
        except (socket.timeout, ConnectionRefusedError):
            results[port] = "CLOSED"
        except Exception as e:
            results[port] = f"{fade('[')}{Colorate.Color(Colors.red, 'x')}{fade(']')} Error: {fade('[')}{Colorate.Color(Colors.red, f'{e}')}{fade(']')}"

def worker(ip, port_queue, results):
    while not port_queue.empty():
        port = port_queue.get()
        scanport(ip, port, results)
        port_queue.task_done()

def scanports(ip, port_range):
    port_queue = Queue()
    for port in range(port_range[0], port_range[1] + 1):
        port_queue.put(port)

    results = {}

    threads = []
    for _ in range(THREADSCOUNT):
        thread = threading.Thread(target=worker, args=(ip, port_queue, results))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    for port in sorted(results):
        status = results[port]
        if "OPEN" in status:
            time = datetime.now().strftime("%H:%M:%S")
            print(f"{fade("[")}{time}{fade("]")} {fade('[')}{Colorate.Color(Colors.green, '+')}{fade(']')} {port} {status}")

if __name__ == "__main__":
    banner = r"""
            ______              
         .-'      `-.           
       .'            `.         
      /                \        
     ;                 ;`       
     |                 |;       
     ;                 ;|
     '\               / ;       
      \`.           .' /        
       `.`-._____.-' .'         
         / /`_____.-'           
        / / /                   
       / / /
      / / /
     / / /
    / / /
   / / /
  / / /
 / / /
/ / /
\/_/
"""

    print(Colorate.Color(Colors.red, banner, 1))
    time = datetime.now().strftime("%H:%M:%S")
    ip = input(f"\n{fade("[")}{time}{fade("]")} > Enter IP: ")
    scanports(ip, (1, 1024))

    time = datetime.now().strftime("%H:%M:%S")
    input(f"{fade("[")}{time}{fade("]")} Press any key to go back.")
    os.system("python hell.py")
    