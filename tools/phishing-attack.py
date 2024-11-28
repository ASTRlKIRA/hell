import os
import re
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
from pystyle import Colors, Colorate
import os
from datetime import datetime

def fade(text: str) -> str:
    return Colorate.Color(Colors.red, text, 1)

def name(filename):
    return re.sub(r'[<>:"/\\|?*]', '_', filename)

def save_file(content, folder, filename):
    os.makedirs(folder, exist_ok=True)
    sanitized_filename = name(filename)
    filepath = os.path.join(folder, sanitized_filename)
    with open(filepath, 'wb') as f:
        f.write(content)
    time = datetime.now().strftime("%H:%M:%S")
    print(f"{fade("[")}{time}{fade("]")} {fade("[")}{Colorate.Color(Colors.green, "+")}{fade("]")} Saved {sanitized_filename} to {folder}.")

def fetch(url, output_folder="output"):
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.RequestException as e:
        time = datetime.now().strftime("%H:%M:%S")
        print(f"{fade("[")}{time}{fade("]")} {fade("[")}{Colorate.Color(Colors.red, "-")}{fade("]")} Error fetching {url}: {Colorate.Color(Colors.red, f"{e}")}.")
        return

    parsed_url = urlparse(url)
    domain_name = parsed_url.netloc
    site_folder = os.path.join(output_folder, domain_name)

    save_file(response.content, site_folder, "index.html")

    soup = BeautifulSoup(response.text, 'html.parser')

    for link in soup.find_all("link", rel="stylesheet"):
        css_url = urljoin(url, link.get("href"))
        try:
            css_response = requests.get(css_url)
            css_response.raise_for_status()
            css_filename = os.path.basename(link.get("href")) or "style.css"
            save_file(css_response.content, site_folder, css_filename)
        except requests.RequestException as e:
            time = datetime.now().strftime("%H:%M:%S")
            print(f"{fade("[")}{time}{fade("]")} {fade("[")}{Colorate.Color(Colors.red, "-")}{fade("]")} Error fetching CSS {css_url}: {Colorate.Color(Colors.red, f"{e}")}.")

    for script in soup.find_all("script", src=True):
        js_url = urljoin(url, script.get("src"))
        try:
            js_response = requests.get(js_url)
            js_response.raise_for_status()
            js_filename = os.path.basename(script.get("src")) or "script.js"
            save_file(js_response.content, site_folder, js_filename)
        except requests.RequestException as e:
            time = datetime.now().strftime("%H:%M:%S")
            print(f"{fade("[")}{time}{fade("]")} {fade("[")}{Colorate.Color(Colors.red, "-")}{fade("]")} Error fetching JS {js_url}: {Colorate.Color(Colors.red, f"{e}")}.")

if __name__ == "__main__":
    banner = r'''
⠀⠀⠀⠀⣀⣤⠶⠒⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣤⣴⠛⢦
⠀⣠⣴⠟⠋⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⠿⠋⠁⠙⠒⠋
⣰⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⠟⠁⠀⠀⠀⠀⠀⠀
⣿⡁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡾⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀
⠸⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⠾⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠙⢷⣤⡀⠀⠀⠀⠀⠀⠀⠀⣀⣤⡾⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠉⠻⠷⢶⣶⣶⣶⠶⠟⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
'''

    print(Colorate.Vertical(Colors.red_to_black, banner, 1))

    times = datetime.now().strftime("%H:%M:%S")
    url = input(f"\n{fade('[')}{times}{fade(']')} > Enter URL: ").strip()
    fetch(url)
    
    time = datetime.now().strftime("%H:%M:%S")
    input(f"{fade("[")}{time}{fade("]")} Press any key to go back.")
    os.system("python hell.py")
