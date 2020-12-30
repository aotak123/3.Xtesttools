# # coding=utf-8
import requests
import json
import pyperclip

s = requests.Session()
url = "http://test-ugcqt-qtzb.qingtianlive.com/zkui/encryption/decrypt"
headers = {
    'Host': 'test-ugcqt-qtzb.qingtianlive.com',
    'Accept': 'application/json, text/plain, */*',
    'Authorization': '4D71BF611AEE857BB8F4F7C31774614F',
    'Accept-Language': 'zh-cn',
    'Accept-Encoding': 'gzip, deflate',
    'Content-Type': 'application/json;charset=utf-8',
    'Origin': 'http://test-ugcqt-qtzb.qingtianlive.com',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/610.2.11 (KHTML, like Gecko) Version/14.0.1 Safari/610.2.11 Maxthon/5.1.60',
    'Referer': 'http://test-ugcqt-qtzb.qingtianlive.com/useless.platform/index.html',
    'Content-Length': '2044',
    'Cookie': 'OCELOT_USER_NAME=%E8%83%A1%E4%BF%8A%E6%AF%85; OCELOT_USER_TOKEN=4D71BF611AEE857BB8F4F7C31774614F; STRATEGICJSESSIONID=FB7D1804515281DCF4988E205725B1C0; userName=%E8%83%A1%E4%BF%8A%E6%AF%85',
    'Connection': 'keep-alive',
}
while True:
    type = input("\033[30m \n 请输入加密字符串\n")
    data1 = {"data": type}
    json1 = (s.post(url, headers=headers, data=json.dumps(data1)).json().get('data'))
    print(json1)
    pyperclip.copy(str(json1))  # 自动添加到剪贴板。
    spam = pyperclip.paste()
