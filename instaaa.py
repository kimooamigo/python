import os
try:
    import termcolor,time,pyfiglet
    import webbrowser
    import requests
    import time, os, sys, json
except:
    os.system('pip install termcolor')
    os.system('pip install time')
    os.system('pip install pyfiglet')
    os.system('pip install requests')
    os.system('pip install webbrowser')
    os.system('pip install sys')
    os.system('pip install json')
    os.system('clear')
    print('\033[1;31mDone installed All libraries \n \033[1;32mDeveloper: \033[1;33m@\033[1;36mPPRRO0 ✅ \n.          \033[1;33mPLEASE WAIT.... ')
    time.sleep(2)
    os.system('clear')
F = '\033[1;32m' #اخضر
B="\033[1;30m" # Black
R="\033[1;31m" # Red
G="\033[1;32m" # Green
Y="\033[1;33m" # Yellow
Bl="\033[1;34m" # Blue
P="\033[1;35m" # Purple
C="\033[1;36m" # Cyan
W="\033[1;37m" # White
PN='\033[1;35m' #BINK
print('-'*50)
print('-'*60)
print('-'*40)
print()
pro="""
               [!] Coded BY Whitepro <\>.
"""
logo = pyfiglet.figlet_format(' INSTA &      SERVICE')
print(termcolor.colored(logo, color="red"),termcolor.colored(pro, color="yellow"),)
print('-'*40)
print('-'*60)
print('-'*50)
print()
print(G+f'          Please join in my channel {R}@l_e_a_r_n')
print('\n')
chos=f"""
{C}>>{Y}╭──────── {G}•{R}◈{G}•{Y}────────╮🖇️
{C}>>{Y}[{C}1{Y}] {G}server 1 {Y}({R}collect coins{Y})
{C}>>{Y}[{C}2{Y}] {G}server 2 {Y}({R}check coins{Y})
{C}>>{Y}[{C}3{Y}] {G}server 3 {Y}({R}send likes{Y})
{C}>>{Y}[{C}4{Y}] {G}server 4 {Y}({R}send members{Y})
{C}>>{Y}╰──────── {G}•{R}◈{G}•{Y}────────╯🖇️
"""
print(chos)
webbrowser.open('https://t.me/L_e_a_r_n')
choses=input(f'{C}>>{Y}Choose Server please : '+Bl)
print()
print(PN+'---->START SERVERING..<----')
if choses == "1":
    try:
        username = input(f'{C}>>{Y}Enter your username : '+Bl)
        cookies = {'s593c5a87': 'v7su176m20pbo6k2g0tjtlrd1a',}
        headers = {
    'Host': 'i.abctiktok.top',
    'Connection': 'keep-alive',
    # 'Content-Length': '18',
    'package': 'com.ins.ttok',
    'apptype': 'android',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; M2004J19C Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.101 Mobile Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
    'idfa': '0028ad81-0f8a-4a55-bb56-9ee634e16564',
    'Accept': 'application/json, text/plain, */*',
    'version': '1.0',
    'Origin': 'http://i.abctiktok.top',
    'X-Requested-With': 'com.ins.ttok',
    'Referer': 'http://i.abctiktok.top/h5_v7/',
    # 'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    # 'Cookie': 's593c5a87=v7su176m20pbo6k2g0tjtlrd1a',
}

        data = {'username': username }

        response = requests.post('http://i.abctiktok.top/api/v7/user', headers=headers, data=data).json()
        pk = response["data"]["userPk"]
        cookies = {'s593c5a87': 'v7su176m20pbo6k2g0tjtlrd1a',}
        headers = {
        'Host': 'i.abctiktok.top',
        'Connection': 'keep-alive',
        # 'Content-Length': '0',
        'package': 'com.ins.ttok',
        'apptype': 'android',
        'pk': pk,
        'User-Agent': 'Mozilla/5.0 (Linux; Android 10; M2004J19C Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.101 Mobile Safari/537.36',
        'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
        'idfa': '0078ad81-0f8a-4a55-bb56-9ee634e16564',
        'Accept': 'application/json, text/plain, */*',
        'username': username,
        'version': '1.0',
        'Origin': 'http://i.abctiktok.top',
        'X-Requested-With': 'com.ins.ttok',
        'Referer': 'http://i.abctiktok.top/h5_v7/',
        # 'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
        # 'Cookie': 's593c5a87=v7su176m20pbo6k2g0tjtlrd1a',
        }
        response = requests.post('http://i.abctiktok.top/api/v6/task/signin/record', cookies=cookies, headers=headers)
        header = {
    'Host': 'i.abctiktok.top',
    'Connection': 'keep-alive',
    # 'Content-Length': '28',
    'package': 'com.ins.ttok',
    'apptype': 'android',
    'pk': pk,
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; M2004J19C Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.101 Mobile Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
    'idfa': '0078ad81-0f8a-4a55-bb56-9ee634e16564',
    'Accept': 'application/json, text/plain, */*',
    'username': username,
    'version': '1.0',
    'Origin': 'http://i.abctiktok.top',
    'X-Requested-With': 'com.ins.ttok',
    'Referer': 'http://i.abctiktok.top/h5_v7/',
    # 'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    # 'Cookie': 's593c5a87=v7su176m20pbo6k2g0tjtlrd1a',
    }

        x = 0
        for i in range(14):
                x=x+1
                data = {'action': 'download','taskAppId': f'{x}',}
                res = requests.post('http://i.abctiktok.top/api/v7/task/app/status', headers=headers, data=data).json()
                try:
                    add = res["data"]["itemCoin"]
                    coins = res["data"]["coin"]
                    print(f"{C}◍ {G}Done Add {Y}> {G}{add} {PN}¦ {B}Total {Bl}> {G}{coins} {PN}¦ {Y}Dev {B}: {Bl}@{C}PPRRO0 ")
                except:
                    print(Y+'Invalid username!')
        print(G+f'- Done collect all coins {C}¦¦ {Bl}Dev{R}: {PN}@PPRRO0 ')
    except:
        print(Y+'Invalid username ')
if choses == "2":
    try:
        username = input(f'{C}>>{Y}Enter your username : '+Bl)
        headers = {
    'Host': 'i.abctiktok.top',
    'Connection': 'keep-alive',
    # 'Content-Length': '18',
    'package': 'com.ins.ttok',
    'apptype': 'android',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; M2004J19C Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.101 Mobile Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
    'idfa': '0028ad81-0f8a-4a55-bb56-9ee634e16564',
    'Accept': 'application/json, text/plain, */*',
    'version': '1.0',
    'Origin': 'http://i.abctiktok.top',
    'X-Requested-With': 'com.ins.ttok',
    'Referer': 'http://i.abctiktok.top/h5_v7/',
    # 'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    # 'Cookie': 's593c5a87=v7su176m20pbo6k2g0tjtlrd1a',
}

        data = {'username': username }

        response = requests.post('http://i.abctiktok.top/api/v7/user', headers=headers, data=data).json()
        pk = response["data"]["userPk"]
        header = {
    'Host': 'i.abctiktok.top',
    'Connection': 'keep-alive',
    # 'Content-Length': '28',
    'package': 'com.ins.ttok',
    'apptype': 'android',
    'pk': pk,
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; M2004J19C Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.101 Mobile Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
    'idfa': '0078ad81-0f8a-4a55-bb56-9ee634e16564',
    'Accept': 'application/json, text/plain, */*',
    'username': username,
    'version': '1.0',
    'Origin': 'http://i.abctiktok.top',
    'X-Requested-With': 'com.ins.ttok',
    'Referer': 'http://i.abctiktok.top/h5_v7/',
    # 'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    # 'Cookie': 's593c5a87=v7su176m20pbo6k2g0tjtlrd1a',
    }
        data = {'action': 'download','taskAppId': '2',}
        res = requests.post('http://i.abctiktok.top/api/v7/task/app/status', headers=headers, data=data).json()
        coins = res["data"]["coin"]
        print(f"{C}◍ {G}Done Checked {B}Total {Bl}> {G}{coins} {PN}¦ {Y}Dev {B}: {Bl}@{C}PPRRO0 ")
    except:
              print(Y+'Invalid username!')
if choses == "3":
    try:
        username = input(f'{C}>>{Y}Enter your username : '+Bl)
        url=input(f'{C}>>{Y}Enter your link : '+Bl)
        headers = {
    'Host': 'i.abctiktok.top',
    'Connection': 'keep-alive',
    # 'Content-Length': '18',
    'package': 'com.ins.ttok',
    'apptype': 'android',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; M2004J19C Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.101 Mobile Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
    'idfa': '0028ad81-0f8a-4a55-bb56-9ee634e16564',
    'Accept': 'application/json, text/plain, */*',
    'version': '1.0',
    'Origin': 'http://i.abctiktok.top',
    'X-Requested-With': 'com.ins.ttok',
    'Referer': 'http://i.abctiktok.top/h5_v7/',
    # 'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    # 'Cookie': 's593c5a87=v7su176m20pbo6k2g0tjtlrd1a',
}

        data = {'username': username }

        response = requests.post('http://i.abctiktok.top/api/v7/user', headers=headers, data=data).json()
        pk = response["data"]["userPk"]
        headers = {
    'Host': 'i.abctiktok.top',
    'Connection': 'keep-alive',
    # 'Content-Length': '81',
    'package': 'com.ins.ttok',
    'apptype': 'android',
    'pk': pk,
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; M2004J19C Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.101 Mobile Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
    'idfa': '0078ad81-0f8a-4a55-bb56-9ee634e16564',
    'Accept': 'application/json, text/plain, */*',
    'username': username ,
    'version': '1.0',
    'Origin': 'http://i.abctiktok.top',
    'X-Requested-With': 'com.ins.ttok',
    'Referer': 'http://i.abctiktok.top/h5_v7/',
    # 'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    # 'Cookie': 's593c5a87=v7su176m20pbo6k2g0tjtlrd1a',
}

        data = {'productId': '980','link': url,'startCount': '0',}
        response = requests.post('http://i.abctiktok.top/api/v1/order',  headers=headers, data=data).json()
        if response["msg"] == "ok":
            coins = response['data']['coin']
            print(f"{C}◍ {G}Done send 50 Likes {B}Total {Bl}> {G}{coins} {PN}¦ {Y}Dev {B}: {Bl}@{C}PPRRO0 ")
        else:
            print(R+"You don't have enough coins please collect more.")
    except:
        print(Y+'Invalid username!')
if choses == "4":
    try:
        username = input(f'{C}>>{Y}Enter your username : '+Bl)
        url=input(f'{C}>>{Y}Enter your link : '+Bl)
        headers = {
    'Host': 'i.abctiktok.top',
    'Connection': 'keep-alive',
    # 'Content-Length': '18',
    'package': 'com.ins.ttok',
    'apptype': 'android',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; M2004J19C Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.101 Mobile Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
    'idfa': '0028ad81-0f8a-4a55-bb56-9ee634e16564',
    'Accept': 'application/json, text/plain, */*',
    'version': '1.0',
    'Origin': 'http://i.abctiktok.top',
    'X-Requested-With': 'com.ins.ttok',
    'Referer': 'http://i.abctiktok.top/h5_v7/',
    # 'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    # 'Cookie': 's593c5a87=v7su176m20pbo6k2g0tjtlrd1a',
}

        data = {'username': username }

        response = requests.post('http://i.abctiktok.top/api/v7/user', headers=headers, data=data).json()
        pk = response["data"]["userPk"]
        headers = {
    'Host': 'i.abctiktok.top',
    'Connection': 'keep-alive',
    # 'Content-Length': '81',
    'package': 'com.ins.ttok',
    'apptype': 'android',
    'pk': pk,
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; M2004J19C Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.101 Mobile Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
    'idfa': '0078ad81-0f8a-4a55-bb56-9ee634e16564',
    'Accept': 'application/json, text/plain, */*',
    'username': username ,
    'version': '1.0',
    'Origin': 'http://i.abctiktok.top',
    'X-Requested-With': 'com.ins.ttok',
    'Referer': 'http://i.abctiktok.top/h5_v7/',
    # 'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    # 'Cookie': 's593c5a87=v7su176m20pbo6k2g0tjtlrd1a',
}

        data = {'productId': '988','link': url,'startCount': '0',}
        response = requests.post('http://i.abctiktok.top/api/v1/order',  headers=headers, data=data).json()
        if response["msg"] == "ok":
            coins = response['data']['coin']
            print(f"{C}◍ {G}Done send 25 Members {B}Total {Bl}> {G}{coins} {PN}¦ {Y}Dev {B}: {Bl}@{C}PPRRO0 ")
        else:
            print(R+"You don't have enough coins please collect more.")
    except:
        print(Y+'Invalid username!')
       
#whitepro 🦦 🔥
#Kdm 💻 ⌨
#خش_هتجيبك
#تخمط_اذكر_المصدر ❤️ 🔥 