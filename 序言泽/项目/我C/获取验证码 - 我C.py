# coding=utf-8

import urllib.request
import re
import ssl
import time

####################——————tak制作  vol.201102——————####################

key = "SCq2_jaKLknsqAwZ"  # 后台使用的key
# testmobile = '测试手机号名单.xlsx'  # 测试记录文件的地址
# realmobile = '正式手机号名单.xlsx'  # 正式记录文件的地址
context = ssl._create_unverified_context()  # ssl证书免验证，python3需要验证https证书

while True:
    type = input("\033[30m \n 请输入验证码类型：\n 1：测试登录\n 2：测试绑定\n 3：正式登录\n 4：正式绑定 \033[0m\n")
    # 3仅支持input输入，不支持raw_input输入
    if type == "1":  # 测试登录
        url = "http://test-ic.hnzhouyi.com/login/main_login/testtool"

    if type == "2":  # 测试绑定
        url = "http://test-ic.hnzhouyi.com/login/main_login/testtool"

    if type == "3":
        type = "1"  # 正式登录
        url = "https://u-ic.hnzhouyi.com/login/main_login/testtool"

    if type == "4":
        type = "2"  # 正式绑定
        url = "https://u-ic.hnzhouyi.com/login/main_login/testtool"

    while True:  # 无限循环语句
        mobile = input("\033[30m 请输入要查询的手机号\返回请输入:0 \033[0m \n")  # 手机号的输入
        right = re.match(r"^1[3456789]\d{9}$", mobile)
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
            request = urllib.request.Request(fullurl)  # 构建请求url
            response = urllib.request.urlopen(request, context=context)  # ssl证书免验证加入,context = context
            # 打开请求url链接
            num = response.read()  # 读取页面返回信息，python3返回数据为bytes类型的对象 (即b为前缀, bytes类型)
            sss = num.decode()  # 字节编码处理decode为str
            print(sss)  # 打印页面内容

            # if url == "http://test-uc.crazyccy.com/login/main_login/testtool":  # 测试环境写入手机号纪录
            #     with open(testmobile, 'r+', encoding="utf-8") as file_object:  # 打开记录记录文件
            #         pi_string = ''
            #         for lines in file_object:
            #             pi_string += lines.strip()
            #         if mobile in pi_string:  # 判断手机号是否存在于表内
            #             print("该手机号已在表内|" + " \033[1;31m 您的验证码： \033[0m" + sss)
            #         else:
            #             print("该手机号为新账号|" + " \033[1;31m 您的验证码： \033[0m" + sss)
            #             remark = input("\033[30m 备注师傅信息: \033[0m")  # 手机号的输入
            #             if remark == "0":
            #                 master = "无"
            #             if remark == "1":
            #                 master = "18817762560"
            #             if remark == "2":
            #                 master = "13401139442"
            #
            #     if sss == '查不到！':  # 如果接口没有返回没有查到则不记录
            #         continue  # 表内不做写入
            #     else:
            #         with open(testmobile, 'r+', encoding="utf-8") as file_object:  # 打开记录记录文件
            #             pi_string = ''
            #             for lines in file_object:
            #                 pi_string += lines.strip()
            #             if mobile in pi_string:  # 判断手机号是否存在于表内
            #                 continue  # 表内不做写入
            #             else:
            #                 nowtime = time.strftime('%Y-%m-%d% %H:%M:%S')  # 获取当前时间
            #                 file_object.write(mobile + "\t")  # \t = tab  \n = 换行
            #                 file_object.write(nowtime + "\t")
            #                 file_object.write(master + "\n")
            #
            # if url == "https://uc.crazyccy.com/login/main_login/testtool":  # 正式环境写入手机号纪录
            #     with open(realmobile, 'r+', encoding="utf-8") as file_object:  # 打开记录execl文件
            #         pi_string = ''
            #         for lines in file_object:
            #             pi_string += lines.strip()
            #         if mobile in pi_string:  # 判断手机号是否存在于表内
            #             print("该手机号已在表内|" + " \033[1;31m 您的验证码： \033[0m" + sss)
            #         else:
            #             print("该手机号为新账号|" + " \033[1;31m 您的验证码： \033[0m" + sss)
            #             remark = input("\033[30m 备注师傅信息: \033[0m")  # 手机号的输入
            #             if remark == "0":
            #                 master = "无"
            #             if remark == "1":
            #                 master = "18817762560"
            #             if remark == "2":
            #                 master = "13401139442"
            #
            #     if sss == '查不到！':  # 如果接口没有返回没有查到则不记录
            #         continue  # 在表内不做写入
            #     else:
            #         with open(realmobile, 'r+', encoding="utf-8") as file_object:  # 打开记录execl文件
            #             pi_string = ''
            #             for lines in file_object:
            #                 pi_string += lines.strip()
            #             if mobile in pi_string:  # 判断手机号是否存在于表内
            #                 continue  # 在表内不做写入
            #             else:
            #                 nowtime = time.strftime('%Y-%m-%d% %H:%M:%S')  # 获取当前时间
            #                 file_object.write(mobile + "\t")  # \t = tab  \n = 换行
            #                 file_object.write(nowtime + "\t")
            #                 file_object.write(master + "\n")
        else:
            print("\033[1;31m！！!手机号码错误，请重新输入！！!\033[0m")
