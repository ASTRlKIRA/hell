import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
from concurrent.futures import ThreadPoolExecutor, as_completed
import threading
from pystyle import Colors, Colorate
import os
from datetime import datetime
import time as _time
import random

def fade(text: str) -> str:
    return Colorate.Color(Colors.red, text, 1)

class Crawler:
    def __init__(self, base_url, max_threads=100, max_depth=10):
        self.base_url = base_url
        self.visited = set()
        self.lock = threading.Lock()
        self.executor = ThreadPoolExecutor(max_threads)
        self.futures = []
        self.max_depth = max_depth

    def crawl(self, url, depth=0):
        if depth > self.max_depth:
            return

        with self.lock:
            if url in self.visited:
                return
            self.visited.add(url)

        try:
            response = requests.get(url, timeout=5)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, 'html.parser')
        except requests.exceptions.RequestException as e:
            time = datetime.now().strftime("%H:%M:%S")
            print(f"{fade('[')}{time}{fade(']')} {fade('[')}{Colorate.Color(Colors.red, 'x')}{fade(']')} Failed to fetch {url}: {Colorate.Color(Colors.red, f'{e}')}")
            return

        title = soup.title.string.strip() if soup.title else "No Title"
        time = datetime.now().strftime("%H:%M:%S")
        print(f"{fade('[')}{time}{fade(']')} {fade('[')}{Colorate.Color(Colors.green, '+')}{fade(']')} {title} > {url}")

        self.handle_links(soup, url, depth)
        self.handle_resources(soup, url)

    def handle_links(self, soup, base_url, depth):
        for link in soup.find_all('a', href=True):
            absolute_url = urljoin(base_url, link['href'])
            if absolute_url.startswith(self.base_url) and absolute_url not in self.visited:
                future = self.executor.submit(self.crawl, absolute_url, depth + 1)
                self.futures.append(future)

    def handle_resources(self, soup, base_url):
        for tag in soup.find_all(['img', 'script', 'link', 'iframe'], src=True):
            src = tag.get('src') or tag.get('href')
            if not src:
                continue

            absolute_url = urljoin(base_url, src)
            resource_type = tag.name

            if absolute_url.startswith(self.base_url) and absolute_url not in self.visited:
                time = datetime.now().strftime("%H:%M:%S")
                print(f"{fade('[')}{time}{fade(']')} {fade('[')}{Colorate.Color(Colors.green, '+')}{fade(']')} {resource_type.capitalize()}: {absolute_url}")
                future = self.executor.submit(self.crawl, absolute_url)
                self.futures.append(future)

    def start(self):
        future = self.executor.submit(self.crawl, self.base_url, 0)
        self.futures.append(future)

        for future in as_completed(self.futures):
            future.result()

        self.executor.shutdown()

if __name__ == "__main__":
    banner = r"""
  .  .
 .|  |.
 ||  ||
 \\()//
 .={}=.
/ /`'\ \
` \  / '
   `'"""

    print(Colorate.Vertical(Colors.red_to_black, banner, 1))
    time = datetime.now().strftime("%H:%M:%S")
    base_url = input(f"\n{fade('[')}{time}{fade(']')} > Enter URL: ")
    spider = Crawler(base_url, max_threads=100, max_depth=10)
    spider.start()

    time = datetime.now().strftime("%H:%M:%S")
    input(f"{fade('[')}{time}{fade(']')} Press any key to go back.")
    os.system("python hell.py")
