# coding=utf-8

import urllib.request
import re
import ssl
import time

####################——————tak制作  vol.201102——————####################
context = ssl._create_unverified_context()  # ssl证书免验证，python3需要验证https证书

while True:
    accid = input("\033[30m \n 请输入用户accid：\n")
    # 3仅支持input输入，不支持raw_input输入
    url = "http://test-u-douni.tt.cn/index/Edit_shiming/edit"
    fullurl = url + "?accid=" + accid# 拼接完整请求url
    request = urllib.request.Request(fullurl)  # 构建请求url
    response = urllib.request.urlopen(request, context=context)  # ssl证书免验证加入,context = context
    # 打开请求url链接
    num = response.read()  # 读取页面返回信息，python3返回数据为bytes类型的对象 (即b为前缀, bytes类型)
    sss = num.decode()  # 字节编码处理decode为str
    # print(sss)  # 打印页面内容
