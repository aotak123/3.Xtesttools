# coding=utf-8
import urllib.request
import time

####################——————tak制作  vol.606——————####################

url = "http://test-servertime.yiqibuduoduo.com/update_time/update?f=update"  # url请求地址

while True:
    type = input("\n 请输入数字：\n 1：查询时间\n 2：恢复时间\n 3：修改时间\n")

    if type == "1":
        urls = "http://test-servertime.yiqibuduoduo.com/update_time/update?f=get"  # 疯狂猜成语获取服务器时间
        request = urllib.request.Request(urls)  # 创建请求地址
        response = urllib.request.urlopen(request)  # 请求打开地址
        openurl = response.read()  # 读取页面内容
        timenow = openurl.decode()  # decode解密
        print("\033[1;31m 当前服务时间： \033[0m")  # 打印时间
        print(timenow)
        # break

    if type == "2":
        nowtime = time.strftime('%Y-%m-%d%%20%H:%M:%S')  # 获取本地当前时间
        fullurl2 = url + "&datetime=" + nowtime  # 拼接地址
        # print(fullurl) #打印地址
        request = urllib.request.Request(fullurl2)  # 创建请求地址
        response = urllib.request.urlopen(request)  # 请求打开地址
        fullurl2bytes = response.read()  # 读取页面内容
        defullurl2 = fullurl2bytes.decode()  # decode解密
        print("\033[1;31m 恢复成功 \033[0m")  # 打印结果
        print(defullurl2)
        # break

    if type == "3":
        while True:  # 无限循环语句
            nowtime = time.strftime('%Y-%m-%d%%20%H:%M:%S')  # 获取当前本地时间
            print("例子：" + nowtime)  # 打印时间
            yeartime = input("请输入你想修改的时间：            \033[1;31m！！！请复制例子进行修改时间！！！\033[0m\n恢复时间请输入：0\n")
            # 请使用例子中的格式，不得有误
            if yeartime == "0":
                nowtime = time.strftime('%Y-%m-%d%%20%H:%M:%S')  # 获取当前本地时间
                nowtimeurl = url + "&datetime=" + nowtime  # 拼接地址
                # print(nowtimeurl)#打印拼接地址
                request = urllib.request.Request(nowtimeurl)  # 创建请求地址
                response = urllib.request.urlopen(request)  # 请求打开地址
                nowtimeurlbytes = response.read()  # 读取页面内容
                denowtimeurl = nowtimeurlbytes.decode()  # decode解密
                print(denowtimeurl)
                break

            else:
                fullurl3 = url + "&datetime=" + yeartime  # 拼接请求地址
                # print(fullurl3)#打印拼接地址
                request = urllib.request.Request(fullurl3)  # 创建请求地址
                response = urllib.request.urlopen(request)  # 请求打开地址
                fullurl3bytes = response.read()  # 读取页面内容
                defullurl3 = fullurl3bytes.decode()  # decode解密
                print(defullurl3)

####################——————tak制作  vol.606——————####################
####################——————tak制作移植 2.X版——————####################
