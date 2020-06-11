# coding=utf-8

import urllib
import base64
import json

####################——————tak制作  vol.605——————####################
####################——————tak制作移植 2.X版——————####################

while True:
    # BP解密 （urldecode+base64）
    A = input("请输入解密内容：")
    if type == "":
        continue
    B = urllib.unquote(A)  # urldecode解密
    # print(B)
    C = base64.b64decode(B)  # base64解密
    print("\n" + C)

    # json格式化校验
    D = input("\033[1;31m 请复制上面这段返回内容，并黏贴进行格式化校验 \033[0m" + "\n")
    print(json.dumps(D, sort_keys=True, indent=4, ensure_ascii=False))

####################——————tak制作  vol.605——————####################
####################——————tak制作移植 2.X版——————####################
"""
Code producer：aotak
Mobile：+86 18817762560
E-Mail：hujunyi@021.com 
"""
