# # coding=utf-8
import requests
import json

s = requests.Session()
url = "http://dc.021.com/strategic-hub/dispatch/ToolWeb/encryptionDecode"
headers = {
    'Host': 'dc.021.com',
    'Accept': 'application/json, text/plain, */*',
    'Authorization': '4D71BF611AEE857BB8F4F7C31774614F',
    'Accept-Language': 'zh-cn',
    'Accept-Encoding': 'gzip, deflate',
    'Content-Type': 'application/json;charset=utf-8',
    'Origin': 'http://dc.021.com',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
    'Referer': 'http://dc.021.com/ocelot/',
    'Content-Length': '2044',
    'Cookie': 'OCELOT_USER_NAME=%E8%83%A1%E4%BF%8A%E6%AF%85; OCELOT_USER_TOKEN=4D71BF611AEE857BB8F4F7C31774614F; STRATEGICJSESSIONID=FB7D1804515281DCF4988E205725B1C0; userName=%E8%83%A1%E4%BF%8A%E6%AF%85',
    'Connection': 'keep-alive',
}
while True:
    type = input("\033[30m \n 请输入加密字符串\n")
    data1 = {
            "bpStr": type
        }
    json1 = (s.post(url, headers=headers,data=json.dumps(data1)).json().get('decodeStr'))
    print(json1)