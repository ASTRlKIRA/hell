import re
import dns.resolver
import socket
from pystyle import Colors, Colorate
import os
from datetime import datetime

def fade(text: str) -> str:
    return Colorate.Color(Colors.red, text, 1)

def lookup_email(email):
    email_regex = r'^([a-zA-Z0-9._%+-]+)@([a-zA-Z0-9.-]+)\.([a-zA-Z]{2,})$'
    match = re.match(email_regex, email)
    
    if not match:
        return f"{fade('[')}{Colorate.Color(Colors.red, '-')}{fade(']')} Invalid email format."

    local_part, domain, tld = match.groups()
    domain_all = f"{domain}.{tld}"

    try:
        mx_records = dns.resolver.resolve(domain_all, 'MX')
        servers = [str(record.exchange).strip('.') for record in mx_records]
    except dns.resolver.NoAnswer:
        servers = []
    except dns.resolver.NXDOMAIN:
        return f"{fade('[')}{Colorate.Color(Colors.red, '-')}{fade(']')} Domain {domain_all} does not exist."

    try:
        spf_records = dns.resolver.resolve(domain_all, 'TXT')
        spf = next((txt.to_text().strip('"') for txt in spf_records if txt.to_text().startswith('"v=spf1')), "None")
    except dns.resolver.NoAnswer:
        spf = "None"
    except dns.resolver.NXDOMAIN:
        spf = "None"

    try:
        dmarc_records = dns.resolver.resolve(f"_dmarc.{domain_all}", 'TXT')
        dmarc = dmarc_records[0].to_text().strip('"')
    except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN):
        dmarc = "None"

    workspace = "True" if "google.com" in " ".join(servers) else "False"

    result = {
        "Email": email,
        "Name": local_part,
        "Domain": domain,
        "Tld": f".{tld}",
        "Domain All": domain_all,
        "Servers": " / ".join(servers) if servers else "None",
        "Spf": spf,
        "Dmarc": dmarc,
        "Workspace": workspace
    }
    
    return result

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
    email = input(f"\n{fade("[")}{time}{fade("]")} > Enter Email: ")
    info = lookup_email(email)

    for key, value in info.items():
        time = datetime.now().strftime("%H:%M:%S")
        print(f"{fade("[")}{time}{fade("]")} {fade('[')}{Colorate.Color(Colors.green, '+')}{fade(']')} {key:<10}: {value}")

    time = datetime.now().strftime("%H:%M:%S")
    input(f"{fade("[")}{time}{fade("]")} Press any key to go back.")
    os.system("python hell.py")
