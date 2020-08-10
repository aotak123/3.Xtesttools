# # coding=utf-8
import requests
import json

s = requests.Session()
url = "http://gm.crazyccy.com/Admin/Decode/index"
headers = {
    'Host': 'gm.crazyccy.com',
    'Accept': '*/*',
    'X-Requested-With': 'XMLHttpRequest',
    'Accept-Language': 'zh-cn',
    'Accept-Encoding': 'gzip, deflate',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Origin': 'http://gm.crazyccy.com',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
    'Referer': 'http://gm.crazyccy.com/Admin/Decode/index',
    'Content-Length': '1016',
    'Cookie': 'PHPSESSID=jjhks6ttstuugvfgmi8bc5oqn3; requestUUID=0f51bbb7-919f-49d4-6148-b8dc93c13f24',
    'Connection': 'keep-alive',
}

while True:
    type = input("\033[30m \n 请输入加密字符串\n")
    data1 = {
        "event": "decode",
        "data": type
    }
    json1 = (s.post(url, headers=headers, data=data1).json().get("info").get("data").get("body").get("idioms"))
    print(json1)
