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

lucifer2 = pyfiglet.figlet_format(' 1G - VF ')
lucifer = pyfiglet.figlet_format(' L U C I F E R ')
def jalan(z):
 for e in z + '\n':
  sys.stdout.write(e)
  sys.stdout.flush()
  time.sleep(00000.01)
jalan('''\033[1;33m PASSWORD ON TELEGRAM CHANNEL : https://t.me/mohtrfandroid ''')
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
print(f'{B} ')
print(lucifer2)
def j(z):
    for e in z:
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(3/100)
j(Y+'*'*60)
print('\n')
def number(z):
 for e in z:
  sys.stdout.write(e)
  sys.stdout.flush()
  time.sleep(00000.01)
number = input(f'🔺  {Y}Enter Your Number    {G}> ').strip()
sleep(2)
print('\n')
def pwd(z):
 for e in z:
  sys.stdout.write(e)
  sys.stdout.flush()
  time.sleep(00000.01)
pwd = input(f'🔺  {Y}Enter Your Password    {G}> ').strip()
with requests.Session() as req:
    def generationLink(stringLingth):
        latters = string.ascii_lowercase
        return ''.join(random.choice(latters) for i in range(stringLingth))
    url = f'https://web.vodafone.com.eg/auth/realms/vf-realm/protocol/openid-connect/auth?client_id=website&redirect_uri=https%3A%2F%2Fweb.vodafone.com.eg%2Far%2FKClogin&state=286d1217-db14-4846-86c1-9539beea01ed&response_mode=query&response_type=code&scope=openid&nonce={generationLink(10)}&kc_locale=en'
    responsePageLogin = req.get(url)
    soup = BeautifulSoup(responsePageLogin.content, 'html.parser')
    getUrlAction = soup.find('form').get('action')
    headerRequest = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-GB,en;q=0.9,ar;q=0.8,ar-EG;q=0.7,en-US;q=0.6',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Host': 'web.vodafone.com.eg',
    'Origin': 'https://web.vodafone.com.eg',
    'Referer': url,
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'
    }
    formData = {
    'username':number,
    'password':pwd
    }
    sendUserData = req.post(getUrlAction,headers=headerRequest,data=formData)
    checkRegistry = sendUserData.url
    _checkRegistry = checkRegistry.find('KClogin')
    
    if _checkRegistry != -1:
        code = checkRegistry
        _code = code[code.index('code=') + 5:]
        header = {
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-GB,en;q=0.9,ar;q=0.8,ar-EG;q=0.7,en-US;q=0.6',
        'Connection': 'keep-alive',
        'Content-type': 'application/x-www-form-urlencoded',
        'Host': 'web.vodafone.com.eg',
        'Origin': 'https://web.vodafone.com.eg',
        'Referer': 'https://web.vodafone.com.eg/ar/KClogin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'
        }
        formDataAccessToken = {
'code': _code,
        'grant_type': 'authorization_code',
        'client_id': 'website',
        'redirect_uri': 'https://web.vodafone.com.eg/ar/KClogin'
        }
        sendDataAccessToken = req.post('https://web.vodafone.com.eg/auth/realms/vf-realm/protocol/openid-connect/token',headers=header,data=formDataAccessToken)
        access_token = sendDataAccessToken.json()['access_token']
headers={'Host':'web.vodafone.com.eg',
'msisdn':number,
'Authorization':f'Bearer {access_token}',
'Connection':'Keep-Alive',
'User-Agent':'Mozilla/5.0 (Linux; Android 8.1.0; DRA-LX2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Mobile Safari/537.36',
'Content-Type':'application/json',
'Accept':'application/json'}
url="https://web.vodafone.com.eg/services/dxl/pom/productOrder"
data='{"channel":{"name":"MobileApp"},"orderItem":[{"action":"delete","product":{"characteristic":[{"name":"ExecutionType","value":"Sync"},{"name":"LangId","value":"en"}],"relatedParty":[{"id":"%s","name":"MSISDN","role":"Subscriber"}],"id":"120","@type":"MI"}}],"@type":"MIProfile"}' %(number)
data2='{"channel":{"name":"MobileApp"},"orderItem":[{"action":"add","product":{"characteristic":[{"name":"ExecutionType","value":"Sync"},{"name":"LangId","value":"en"}],"relatedParty":[{"id":"%s","name":"MSISDN","role":"Subscriber"}],"id":"120","@type":"MI"}}],"@type":"MIProfile"}' %(number)
r=requests.post(url,headers=headers,data=data).text
r2=requests.post(url,headers=headers,data=data2).text
if "Completed" in r:
 print("\033[0;22mDone deleted 💢")
 print()
 print("🌚Done Login ")
 print()
 sleep(2)
 print(G+"🔰 DONE ADD 1G ✔️.....")
elif "Completed" in r2:
 print("🌚Done Login ")
 sleep(2)
 print()
 print(G+"🔰 DONE ADD 1G ✔️.....")
else:
  print("🌚Done Login ")
  sleep(2)
  print()
  print(R+"🔰 YOU GET 1G BEFORE 😑.....")
