# coding=utf-8

import urllib.request
import re
import ssl
import time

####################——————tak制作  vol.605——————####################

key = "sLQq2_jaKLknsqAwZ"  # 后台使用的key

while True:
    type = input("\033[30m \n 请输入验证码类型：\n 1：测试登录\n 2：测试绑定\n 3：正式登录\n 4：正式绑定 \033[0m\n")
    # 3仅支持input输入，不支持raw_input输入
    if type == "1":  # 测试登录
        url = "http://test-u.yiqibuduoduo.com/login/main_login/testtool"

    if type == "2":  # 测试绑定
        url = "http://test-u.yiqibuduoduo.com/login/main_login/testtool"

    if type == "3":
        type = "1"  # 正式登录
        url = "http://u.yiqibuduoduo.com/login/main_login/testtool"

    if type == "4":
        type = "2"  # 正式绑定
        url = "http://u.yiqibuduoduo.com/login/main_login/testtool"

    while True:  # 无限循环语句
        mobile = input("\033[30m 请输入要查询的手机号\返回请输入:0 \033[0m \n")  # 手机号的输入
        context = ssl._create_unverified_context()  # ssl证书免验证，python3需要验证https证书
        right = re.match(r"^1[35789]\d{9}$", mobile)
        # 手机号都为11位，所以必须限定匹配的数字的位数，通过$来限定以9位数字结尾，又因为手机号都以1开头，所以通过^1限定以1开头，
        # 然后手机号第二位貌似只有3,5,6,7,8,这几个数字，所以通过[3,5,7,8,9]来匹配其中的任一数字，后续推出新的号段，需在这里做添加
        # 最后｛9｝匹配9个/d。【补】：/d 表示匹配数字

        if mobile == "0":  # 返回请输入:0
            break
        # if mobile == "":  #输入空不执行
        #     continue
        if right:
            # print ("检验通过")    #手机号校验打印
            fullurl = url + "?key=" + key + "&type=" + type + "&mobile=" + mobile  # 拼接完整请求url
            # print (fullurl)       #打印拼接url
            request = urllib.request.Request(fullurl)  # 构建请求url
            response = urllib.request.urlopen(request, context=context)  # ssl证书免验证加入,context = context
            # 打开请求url链接
            num = response.read()  # 读取页面返回信息，python3返回数据为bytes类型的对象 (即b为前缀, bytes类型)
            sss = num.decode()  # 字节编码处理decode为str
            print(sss)  # 打印页面内容

        else:
            print("\033[1;31m！！!手机号码错误，请重新输入！！!\033[0m")

####################——————tak制作  vol.605——————####################
