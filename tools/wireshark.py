import os
import subprocess
import sys
import urllib.request

def download():
    wireshark_path = "C:\\Program Files\\Wireshark\\Wireshark.exe"
    if os.path.exists(wireshark_path):
        print("Wireshark is already installed. Launching...")
        subprocess.Popen([wireshark_path])
    else:
        print("Wireshark is not installed. Downloading and installing...")
        installer_url = "https://2.na.dl.wireshark.org/win64/Wireshark-win64-4.0.6.exe"
        installer_path = "WiresharkInstaller.exe"
        urllib.request.urlretrieve(installer_url, installer_path)
        subprocess.check_call([installer_path, '/S'])
        os.remove(installer_path)
        print("Wireshark installed successfully. Launching...")
        subprocess.Popen([wireshark_path])

download()