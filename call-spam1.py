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
j(R+'*'*60)
print('\n')
number = input(f'🔺  {P}Enter Target    {G}> ')
asa = '123456789'
gigk = str(''.join(random.choice(asa) for i in range(10)))

md5 = hashlib.md5(gigk.encode()).hexdigest()[:16]


headers = {
    "Host": "account-asia-south1.truecaller.com",
    "content-type": "application/json; charset\u003dUTF-8",
    "content-length": "680",
    "accept-encoding": "gzip",
    "user-agent": "Truecaller/12.34.8 (Android;8.1.2)",
    "clientsecret": "lvc22mp3l1sfv6ujg83rd17btt"
  }

url = "https://account-asia-south1.truecaller.com/v3/sendOnboardingOtp"

data = '{"countryCode":"eg","dialingCode":20,"installationDetails":{"app":{"buildVersion":8,"majorVersion":12,"minorVersion":34,"store":"GOOGLE_PLAY"},"device":{"deviceId":"'+md5+'","language":"ar","manufacturer":"Xiaomi","mobileServices":["GMS"],"model":"Redmi Note 8A Prime","osName":"Android","osVersion":"7.1.2","simSerials":["8920022021714943876f","8920022022805258505f"]},"language":"ar","sims":[{"imsi":"602022207634386","mcc":"602","mnc":"2","operator":"vodafone"},{"imsi":"602023133590849","mcc":"602","mnc":"2","operator":"vodafone"}],"storeVersion":{"buildVersion":8,"majorVersion":12,"minorVersion":34}},"phoneNumber":"'+number+'","region":"region-2","sequenceNo":1}'

r=requests.post(url, headers=headers, data=data).text
if 'limited' in r:
	print('')
else:
	print(G+'DONE')