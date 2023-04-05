# = = = = = = = = = = = = «COLOR» = = = = = = = = = = = #

R     ="\033[1;31m"      # Red
G     ="\033[1;32m"      # Green
Y     ="\033[1;33m"      # Yellow
B     ="\033[1;34m"      # Blue
P     ="\033[1;35m"      # Purple
C     ="\033[1;36m"      # Cyan
W    ="\033[1;37m"      # White
R1   = '\033[2;31m'      #Red_2
P1   = '\033[2;35m'      # Pink
LB   = '\033[2;36m'      # Cloud 
L      = '\033[1;34m    ' # Light_Blue

# = = = = = = = = = = = = «LIBRARY» = = = = = = = = = = = #

import uuid,random,user_agent,datetime,string,time,threading,json,secrets,subprocess,hashlib
import requests, pyfiglet, termcolor, sys, os, webbrowser as time, datetime, time
from random import *
from user_agent import generate_user_agent
from datetime import datetime
from user_agent import generate_user_agent
from datetime import datetime
from random import *
from time import sleep
from colorama import Fore, Style
from uuid import uuid4
from secrets import token_hex
from bs4 import BeautifulSoup
aa = 0
zz = 0

# = = = = = = = = = = = = = = = = = = = = = = = 


print (R+'    --------- / Start The Hunt pls Wait / ----------')
sleep(5)
os.system("clear")
lucifer = pyfiglet.figlet_format(' L U C I F E R ')
def jalan(z):
 for e in z + '\n':
  sys.stdout.write(e)
  sys.stdout.flush()
  time.sleep(00000.01)
jalan('''\033[1;33m All Scripts ON TELEGRAM CHANNEL : https://t.me/mohtrfandroid ''')
print('')
def j(z):
    for e in z:
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(3/100)
j('*'*60)
print('  ')
print(f'{W} ')
print(lucifer)
def j(z):
    for e in z:
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(3/100)
j(Y+'*'*60)
print('\n')
os.system('clear')
print()
num=input(f'🔺  {P}Enter Your Number    {G}> ')
pwd=input(f'🔺  {P}Enter Your Password    {G}> ')
print()
url="http://api.leadingiot.com/login"
headers={'accept': '*/*',
'access-control-request-method': 'POST',
'access-control-request-headers': 'content-type,token',
'origin': 'https://www.leadingiot.com',
'user-agent': 'Mozilla/5.0 (Linux; Android 8.1.0; SM-T585) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
'sec-fetch-mode': 'cors',
'sec-fetch-site': 'same-site',
'sec-fetch-dest': 'empty',
'referer': 'https://www.leadingiot.com/',
'acc/ept-encoding': 'gzip, deflate, br',
'accept-language': 'ar-AE,ar;q=0.9,en-US;q=0.8,en;q=0.7'}

r=requests.options(url, headers=headers).text
print(r)
if "" in r:
 print("Done Access")
else:
 print(R+"Fail Access")
 sys.exit()
print()
time.sleep(5)
print()
uri="http://api.leadingiot.com/login"

hd={'content-length': '120' ,'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"', 'content-type': 'application/json', 'sec-ch-ua-mobile': '?0', 'content-type': 'application/json', 'user-agent': 'Mozilla/5.0 (Linux; Android 8.1.0; SM-T585) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36', 'token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiIhQCMkJSomKiIsImF1ZCI6IiIsImlhdCI6MTY3NTA0NTczMywibmJmIjoxNjc1MDQ1NzM2LCJleHAiOjE2NzUxMzIxMzMsImRhdGEiOjE0MzcyOX0.rVeqKdlMcs0CJ_LDyJBXAm_JtJCDBa2l0wqShfn8QpA','sec-ch-ua-platform': '"Android"', 'accept': '*/*', 'origin': 'https://www.leadingiot.com', 'sec-fetch-site': 'same-site', 'sec-fetch-mode': 'cors', 'sec-fetch-dest': 'empty', 'referer': 'https://www.leadingiot.com/', 'accept-encoding': 'gzip, deflate, br', 'accept-language': 'ar-AE,ar;q=0.9,en-US;q=0.8,en;q=0.7'}

data={"username":num,"password":pwd,"device":"SM-T585","driver":"android","userAgent":"H5","google_code":""}
    
r2=requests.post(url, headers=hd, data=data)
print(r2)
if "msgok" in r2:
 print(G+"SUCCESS LOGIN")
else:
 print(R+"ERROR ")