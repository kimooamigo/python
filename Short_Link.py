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
a = 0

# = = = = = = = = = = = = = = = = = = = = = = = 

linkk = input(f'{W}Enter Phone Number {P}:{C} ')

url = "https://api.apilayer.com/short_url/hash"

payload = linkk.encode("utf-8")
headers= {
  "apikey": "nfuiyo8UcgthTpsXsHXMCOBxzXNhMrkk"
}

response = requests.request("POST", url, headers=headers, data = payload)

status_code = response.status_code
result = response.text
g2 = response.json()['short_url']
g1 = response.json()['long_url']
if "short_url" in result:
	print()
	print(f'{P}• {G}Done Created')
	print(f'{P}• {G}Original Link {P}:{W} {g1} ')
	print(f'{P}• {G}Short Link {P}:{W} {g2} ')
	print()
else:
    	print()
    	print(f"{R}• There's a mistake")
    	print('')
    	exit()

print('')