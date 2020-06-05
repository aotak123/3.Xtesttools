# coding=utf-8
import urllib.request
import ssl
####################——————tak制作  vol.605——————####################

while True:
    a = input("\n 请输入获取的类型：\n 1：测试环境清除\n ***正式环境 请去Ocelot平台***\n ")

    if a == "1":
        url = "http://106.75.6.212:8020/testcleantools/cleanimei?apptypeid=100022&imei="
    if a == "2":
        # url = "https://invite.crazyccy.com/invite/Iiiii/imei_accid"
        print("\033[1;31m 功能暂时无法使用！！！ \033[0m")
        continue
    elif a > "2":
        print("\033[1;31m 输入有误，请重新选择！！！ \033[0m")
        continue
    elif a < "1":
        print("\033[1;31m 输入有误，请重新选择！！！ \033[0m")
        continue

    while True:  # 无限循环语句
        imei = input("请输入\033[1;31m imei\033[0m 或 \033[1;31moaid\033[0m 进行清除，返回请输入0\n")
        # 添加快捷方式输入
        if imei == "0":
            break
        if imei == "":
            continue
        if imei == "1":
            imei = "9CFBCE03-BAE2-42DE-81CF-C537A1AD1D59"
            deviceid = "F95F0A62-8C6E-40B5-ABE2-D855D49742F1"  # "#iphone 7plus

        if imei == "2":
            # imei = "863056044142477"#huawei 8x
            imei = "7ff3e7df-b96e-e8e1-baf1-f6dcf75f2be3"
            deviceid = "94764aa49bb442e5"
            aaid = "461f14fe628616f42a085259e39cc978"
            oaid = "7ff3e7df-b96e-e8e1-baf1-f6dcf75f2be3"

        if imei == "3":
            # imei = "865973042769010"#黑鲨
            imei = "43e219e4af34ad4e"#黑鲨
            deviceid = "43e219e4af34ad4e"



        fullurl = url + imei
        context = ssl._create_unverified_context()  # ssl证书免验证，python3需要验证https证书
        # print(fullurl)

        request = urllib.request.Request(fullurl)  # 构建请求url
        response = urllib.request.urlopen(request)
        num = response.read()
        sss = num.decode()
        print(imei +"  "+ sss)

####################——————tak制作  vol.605——————####################