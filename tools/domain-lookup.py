import whois
from pystyle import Colors, Colorate
import os
from datetime import datetime

def fade(text: str) -> str:
    return Colorate.Color(Colors.red, text, 1)

def info(domain):
    try:
        domain_info = whois.whois(domain)
        for key, value in domain_info.items():
            time = datetime.now().strftime("%H:%M:%S")
            print(f"{fade("[")}{time}{fade("]")} {fade('[')}{Colorate.Color(Colors.green, '+')}{fade(']')} {key}: {value}")
    except Exception as e:
        print(f"{fade("[")}{time}{fade("]")} {fade('[')}{Colorate.Color(Colors.red, '-')}{fade(']')} Error: {Colorate.Color(Colors.red, f"{e}")}")

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

    print(Colorate.Vertical(Colors.red_to_black, banner, 1))

    time = datetime.now().strftime("%H:%M:%S")
    domain = input(f"\n{fade("[")}{time}{fade("]")} > Enter URL (Without https:// or www): ")

    info(domain)


    time = datetime.now().strftime("%H:%M:%S")
    input(f"{fade("[")}{time}{fade("]")} Press any key to go back.")
    os.system("python hell.py")
