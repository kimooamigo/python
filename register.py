import requests,random
from uuid import uuid4
from time import sleep as slep
num = input("[=] NUM : ")
#========================================================#
#========================================================#
#========================================================#
slep(2)
uid=(uuid4())
num=f"{random.choice(['010','011','012','015'])}"+''.join(random.choice("0987654321")for _ in range(8))
js={"countryId":40,"inviteCode":"","mobile":num,"password":"Kk010193#","uuid":f"37388{uid}"}
url= "https://enbwpro.com/user/api/member/register"
hd={
	"Host": "enbwpro.com",
	"content-length": "125",
	"user-agent": "Mozilla/5.0 (Linux; Android 11; SM-A025F Build/RP1A.200720.012) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Mobile Safari/537.36 Html5Plus/1.0",
	"client": "app",
	"content-type": "application/json;charset=UTF-8",
	"accept": "*/*",
	"origin": "https://enbwpro.com",
	"x-requested-with": "plus.H511ED976",
	"sec-fetch-site": "same-origin",
	"sec-fetch-mode": "cors",
	"sec-fetch-dest": "empty",
	"referer": "https://enbwpro.com/",
	"accept-encoding": "gzip, deflate",
	"accept-language": "en-US,en;q=0.9,ar-AE;q=0.8,ar;q=0.7",
	"cookie": "_lang=en_US"
	}
r=requests.post(url,headers=hd,json=js).text
response = r.json()["message"]
print("[=] "+response)