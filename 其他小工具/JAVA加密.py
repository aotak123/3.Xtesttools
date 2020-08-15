# # coding=utf-8
import requests
import json

s = requests.Session()
url = "http://49.232.45.133/ToolWeb/encryptionDecode"
while True:
    type = input("\033[30m \n 请输入参数\n")
    data1 = {
            "bpStr": type
        }
    json1 = (s.post(url, data=data1).json().get('decodeStr'))
    print(json1)