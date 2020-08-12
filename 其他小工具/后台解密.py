# # coding=utf-8
import requests
import json

setting = 1  # 1为正式环境链接、0为测试环境链接
s = requests.Session()
if setting == 1:
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
        'Cookie': 'PHPSESSID=vmph8k4dtqca1a6sc15fjise18; requestUUID=92b6859a-42cf-cd33-04a6-d0252ccc801e',
        'Connection': 'keep-alive',
    }

if setting == 0:
    url = "http://test-gm-fkccy.tiantianshuibaobao.com/Admin/Decode/index"
    headers = {
        'Host': 'test-gm-fkccy.tiantianshuibaobao.com',
        'Accept': '*/*',
        'X-Requested-With': 'XMLHttpRequest',
        'Accept-Language': 'zh-cn',
        'Accept-Encoding': 'gzip, deflate',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Origin': 'http://test-gm-fkccy.tiantianshuibaobao.com',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
        'Referer': 'http://test-gm-fkccy.tiantianshuibaobao.com/Admin/Decode/index',
        'Content-Length': '1016',
        'Cookie': 'requestUUID=0d70df67-0243-d7f2-a161-ba3344b01f6d; PHPSESSID=c5nqm9r19bealgm0v841s363ji',
        'Connection': 'keep-alive',
    }
while True:
    type = input("\033[30m \n 请输入加密字符串\n")
    data1 = {
        "event": "decode",
        "data": type
    }
    json1 = (s.post(url, headers=headers, data=data1).json())
    print(json1)
