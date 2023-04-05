import requests,random
from uuid import uuid4
from time import sleep as slep
num = input("[=] NUM : ")
slep(2)
json={"countryId":40,"userName":"1278352660","password":"Kk010193#"}
file=open("acc.text","w+")
file.write(f"{json}\n")
file.close()
print("[=] "+requests.post("https://enbwpro.com/user/api/login",
headers={
	"Host": "enbwpro.com",
	"content-length": "63",
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
	"cookie": "JSESSIONID=15DCA6379E7A747D60ED599C69A55514",

	"cookie": "_lang=en_US",
    "cookie": "SessionId=9718d7bb-08dd-46c3-99a0-f80ee86e3fe1",
},
json=json).json()["message"])
#========================================================#
#========================================================#
#========================================================#
slep(2)
js={""}
url= "https://enbwpro.com/user/api/member/mining/income"
hd={
	"Host": "enbwpro.com",
	"user-agent": "Mozilla/5.0 (Linux; Android 11; SM-A025F Build/RP1A.200720.012) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Mobile Safari/537.36 Html5Plus/1.0",
	"client": "app",
	"content-type": "application/json;charset=UTF-8",
	"accept": "*/*",
	"x-requested-with": "plus.H511ED976",
	"sec-fetch-site": "same-origin",
	"sec-fetch-mode": "cors",
	"sec-fetch-dest": "empty",
	"referer": "https://enbwpro.com/",
	"accept-encoding": "gzip, deflate",
	"accept-language": "en-US,en;q=0.9,ar-AE;q=0.8,ar;q=0.7",
	"cookie": "JSESSIONID=15DCA6379E7A747D60ED599C69A55514",

	"cookie": "_lang=en_US",
    "cookie": "SessionId=9718d7bb-08dd-46c3-99a0-f80ee86e3fe1",
	}
r=requests.get(url,headers=hd)
response = r.json()["message"]
print("[=] "+response)