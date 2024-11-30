import requests
import time
from concurrent.futures import ThreadPoolExecutor
from pystyle import Colors, Colorate
import os
from datetime import datetime

def fade(text: str) -> str:
    return Colorate.Color(Colors.red, text, 1)

websites = {
    "TikTok": "https://www.tiktok.com/@{}",
    "Telegram": "https://t.me/{}",
    "WeChat": "https://www.wechat.com/en/{}",
    "WhatsApp": "https://wa.me/{}",
    "Twitter": "https://x.com/{}",
    "Reddit": "https://www.reddit.com/user/{}",
    "Pinterest": "https://www.pinterest.com/{}/",
    "Discord": "https://discord.com/users/{}",
    "Quora": "https://www.quora.com/profile/{}",
    "LinkedIn": "https://www.linkedin.com/in/{}",
    "Snapchat": "https://www.snapchat.com/add/{}",
    "Instagram": "https://www.instagram.com/{}/",
    "Facebook": "https://www.facebook.com/{}",
    "YouTube": "https://www.youtube.com/c/{}",
    "Twitch": "https://www.twitch.tv/{}",
    "Spotify": "https://open.spotify.com/user/{}",
    "Tumblr": "https://{}.tumblr.com/",
    "Medium": "https://medium.com/@{}",
    "Vimeo": "https://vimeo.com/{}",
    "GitHub": "https://github.com/{}",
    "GitLab": "https://gitlab.com/{}",
    "Behance": "https://www.behance.net/{}",
    "Dribbble": "https://dribbble.com/{}",
    "Steam": "https://steamcommunity.com/id/{}",
    "Flickr": "https://www.flickr.com/photos/{}",
    "StackOverflow": "https://stackoverflow.com/users/{}",
    "Grindr": "https://grindr.com/{}",
    "OkCupid": "https://www.okcupid.com/profile/{}",
    "Bumble": "https://bumble.com/user/{}",
    "Tinder": "https://tinder.com/@{}",
    "Hinge": "https://www.hinge.co/users/{}",
    "Badoo": "https://badoo.com/en/{}",
    "Match": "https://www.match.com/profile/{}",
    "Rumble": "https://rumble.com/user/{}",
    "Clubhouse": "https://www.joinclubhouse.com/@{}",
    "Xiaohongshu (RED)": "https://www.xiaohongshu.com/user/profile/{}",
    "Vero": "https://vero.co/{}",
    "Ravelry": "https://www.ravelry.com/people/{}",
    "ShareChat": "https://www.sharechat.com/{}/",
    "Threads": "https://www.threads.net/@{}",
    "Viber": "https://www.viber.com/en/users/{}",
    "Zalo": "https://zalo.me/{}",
    "Line": "https://line.me/{}",
    "VK (Vkontakte)": "https://vk.com/{}",
    "Microsoft Teams": "https://teams.microsoft.com/l/team/{}",
    "Riot Games": "https://www.riotgames.com/en/{}",
    "Trello": "https://trello.com/{}",
    "hellList": "https://hell.co/u/{}",
    "Product Hunt": "https://www.producthunt.com/@{}",
    "Goodreads": "https://www.goodreads.com/user/show/{}",
    "SoundCloud": "https://soundcloud.com/{}",
    "DeviantArt": "https://www.deviantart.com/{}",
    "Kickstarter": "https://www.kickstarter.com/profile/{}",
    "Etsy": "https://www.etsy.com/people/{}",
    "Couchsurfing": "https://www.couchsurfing.com/people/{}",
    "Foursquare": "https://foursquare.com/{}",
    "Mixcloud": "https://www.mixcloud.com/{}",
    "Bandcamp": "https://bandcamp.com/{}",
    "Gaia Online": "https://www.gaiaonline.com/profiles/{}/",
    "ArtStation": "https://www.artstation.com/{}",
    "Crunchyroll": "https://www.crunchyroll.com/user/{}",
    "MyAnimeList": "https://myanimelist.net/profile/{}",
    "Nexus Mods": "https://www.nexusmods.com/users/{}",
    "ReverbNation": "https://www.reverbnation.com/{}",
    "Newgrounds": "https://{}.newgrounds.com/",
    "FanFiction.net": "https://www.fanfiction.net/u/{}/",
    "Wattpad": "https://www.wattpad.com/user/{}",
    "Chess.com": "https://www.chess.com/member/{}",
    "Lichess": "https://lichess.org/@/{}",
    "Geocaching": "https://www.geocaching.com/p/default.aspx?u={}",
    "Runescape": "https://secure.runescape.com/m=community/c={}/",
    "Roblox": "https://www.roblox.com/users/{}/profile",
    "EVE Online": "https://zkillboard.com/character/{}/",
    "Star Citizen": "https://robertsspaceindustries.com/citizens/{}",
    "Epic Games": "https://www.epicgames.com/id/{}",
    "Overwatch": "https://playoverwatch.com/en-us/career/pc/{}",
    "Fortnite Tracker": "https://fortnitetracker.com/profile/all/{}",
    "League of Legends": "https://na.op.gg/summoners/na/{}",
    "Minecraft": "https://namemc.com/profile/{}",
    "Amino": "https://aminoapps.com/u/{}",
    "Kik": "https://kik.me/{}",
    "Smule": "https://www.smule.com/{}",
    "Dubsmash": "https://www.dubsmash.com/{}",
    "Byte": "https://byte.co/{}",
    "Flipboard": "https://flipboard.com/@{}",
    "Blizzard": "https://battle.net/{}",
    "PSN Profiles": "https://psnprofiles.com/{}",
    "Xbox Live": "https://www.xboxgamertag.com/search/{}/",
    "Nintendo Switch": "https://www.nintendo.com/profile/{}",
    "Taringa": "https://www.taringa.net/{}/",
    "Pheed": "https://www.pheed.com/{}",
    "Weibo": "https://weibo.com/u/{}",
    "Douyin": "https://www.douyin.com/user/{}",
    "Snapfish": "https://www.snapfish.com/user/{}",
    "Qzone": "https://user.qzone.qq.com/{}/",
    "MeWe": "https://mewe.com/i/{}",
    "Gab": "https://gab.com/{}",
    "Minds": "https://www.minds.com/{}",
    "Hive": "https://www.hivesocial.app/@{}",
    "Parler": "https://parler.com/profile/{}",
    "Truth Social": "https://truthsocial.com/@{}",
    "Care2": "https://www.care2.com/c2c/people/profile.html?pid={}",
    "Plurk": "https://www.plurk.com/{}",
    "Ko-fi": "https://ko-fi.com/{}",
    "Patreon": "https://www.patreon.com/{}",
    "Buy Me a Coffee": "https://www.buymeacoffee.com/{}",
    "Itch.io": "https://{}.itch.io/",
    "Letterboxd": "https://letterboxd.com/{}",
    "Last.fm": "https://www.last.fm/user/{}",
    "Ravelry": "https://www.ravelry.com/people/{}",
    "Canva": "https://www.canva.com/{}",
    "Notion": "https://www.notion.so/{}",
    "Strava": "https://www.strava.com/athletes/{}",
    "RunKeeper": "https://runkeeper.com/user/{}",
    "Garmin Connect": "https://connect.garmin.com/profile/{}",
    "Fitbit": "https://www.fitbit.com/user/{}",
    "MapMyRun": "https://www.mapmyrun.com/profile/{}",
    "Smash.gg": "https://smash.gg/u/{}",
    "Challonge": "https://challonge.com/users/{}",
}

def checkusersite(site, url, username):
    try:
        formatted_url = url.format(username)
        response = requests.get(formatted_url)
        
        if response.status_code == 200:
            time = datetime.now().strftime("%H:%M:%S")
            return f"{fade("[")}{time}{fade("]")} {fade('[')}{Colorate.Color(Colors.green, '+')}{fade(']')} {site} : {Colorate.Color(Colors.green, "TRUE")} > {formatted_url}"
    except requests.RequestException as e:
        return None
    
    return None

def checkuser(username):
    results = []

    with ThreadPoolExecutor(max_workers=99) as executor:
        futures = [
            executor.submit(checkusersite, site, url, username)
            for site, url in websites.items()
        ]

        for future in futures:
            result = future.result()
            if result:
                results.append(result)
    
    return results

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
    user = input(f"\n{fade("[")}{time}{fade("]")} > Enter Username: ")
    results = checkuser(user)

    if results:
        for result in results:
            print(result)
    else:
        time = datetime.now().strftime("%H:%M:%S")
        print(f"\n{fade("[")}{time}{fade("]")} {fade('[')}{Colorate.Color(Colors.red, 'x')}{fade(']')} Username not found.")

    time = datetime.now().strftime("%H:%M:%S")
    input(f"{fade("[")}{time}{fade("]")} Press any key to go back.")
    os.system("python hell.py")
