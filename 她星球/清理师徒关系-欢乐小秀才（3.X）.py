# coding=utf-8
import urllib.request
import ssl

####################——————tak制作  vol.606——————####################

url = "http://106.75.6.212:8020/testcleantools/cleanimei?apptypeid=100008&imei="
while True:  # 无限循环语句
    imei = input("请输入\033[1;31m imei\033[0m 或 \033[1;31moaid\033[0m 进行清除\n")
    # if imei == "0":
    #     break #
    if imei == "":
        continue
        """可在此添加设备信息以便快捷操作"""
    if imei == "1":  # iphone 7plus#
        imei = "9CFBCE03-BAE2-42DE-81CF-C537A1AD1D59"
        deviceid = "F95F0A62-8C6E-40B5-ABE2-D855D49742F1"
    if imei == "2":
        # imei = "863056044142477"#huawei 8x#
        imei = "7ff3e7df-b96e-e8e1-baf1-f6dcf75f2be3"
        deviceid = "94764aa49bb442e5"
        aaid = "461f14fe628616f42a085259e39cc978"
        oaid = "7ff3e7df-b96e-e8e1-baf1-f6dcf75f2be3"
    if imei == "3":  # 黑鲨#
        # imei = "865973042769010"
        imei = "43e219e4af34ad4e"
        deviceid = "43e219e4af34ad4e"

    # 拼接地址
    fullurl = url + imei
    context = ssl._create_unverified_context()  # ssl证书免验证，python3需要验证https证书
    # print(fullurl)

    request = urllib.request.Request(fullurl)  # 构建请求url
    response = urllib.request.urlopen(request)  # 请求打开地址
    num = response.read()  # 读取页面内容
    sss = num.decode()  # 内容decode解密
    print(imei + "  " + sss)  ##打印地址

####################——————tak制作  vol.605——————####################
"""
Code producer：aotak
Mobile：+86 18817762560
E-Mail：hujunyi@021.com 
"""
