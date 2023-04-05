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

os.system("clear")
print (R+'    --------- / Start The Hunt pls Wait / ----------')
sleep(5)
os.system("clear")

lucifer2 = pyfiglet.figlet_format(' 200MB - VF ')
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
    urlLoginPage = f'https://web.vodafone.com.eg/auth/realms/vf-realm/protocol/openid-connect/auth?client_id=website&redirect_uri=https%3A%2F%2Fweb.vodafone.com.eg%2Far%2FKClogin&state=286d1217-db14-4846-86c1-9539beea01ed&response_mode=query&response_type=code&scope=openid&nonce={generationLink(10)}&kc_locale=en'
    responsePageLogin = req.get(urlLoginPage)
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
    'Referer': urlLoginPage,
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
        headerAccessToken = {
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
        sendDataAccessToken = req.post('https://web.vodafone.com.eg/auth/realms/vf-realm/protocol/openid-connect/token',headers=headerAccessToken,data=formDataAccessToken)
jwt = sendDataAccessToken.json()['access_token']
url="https://mobile.vodafone.com.eg:443/mobile-app/promo/unifiedRedeemPromo"
headers={"Authorization": "Bearer "+(jwt)+"", "operatingSystem": "V11.0.8.0.PCOMIXM", "platform": "Android", "deviceType": "ginkgo", "buildNumber": "414",
"Content-Type": "application/json; charset=UTF-8", "Connection": "close", "Accept-Encoding": "gzip, deflate", "User-Agent": "okhttp/3.12.1"}
json={"channelId": 3, "contextualOperationId": 0, "contextualPromoId": 0, "operationId": 0, "param1": "Vodafone", "promoId": 3336, "triggerId": 332, "triggerType": "6", "wlistId": 3256}
r=requests.post(url, headers=headers, json=json)
g=r.json()['giftQuota']
print("")
if g == "200":
    print("🌚Done Login ")
    sleep(2)
    print(G+"🔰 DONE ADD 200MG ✔️ ")
else:
	print("🌚Done Login ")
	sleep(2)
	print(R+"🔰 Try Later ❌")