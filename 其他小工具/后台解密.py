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
        'Cookie': 'PHPSESSID=bcolasi5vg9o90l402t59fql1t; requestUUID=5622fcf5-61e9-ab80-81be-dc1c61c85395',
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
        'Cookie': 'PHPSESSID=7u2kgtjtjlcu77a9hf4h77rq9v; requestUUID=eb611f95-e5da-6a1c-9c4a-74e8539836e6',
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
