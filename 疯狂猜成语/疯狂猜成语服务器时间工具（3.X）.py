# coding=utf-8
import urllib.request
import time
####################——————tak制作  vol.605——————####################

url = "http://test-task-fkccy.tiantianshuibaobao.com/Update_time/update?f=update"

while True:
    type = input("\n 请输入数字：\n 1：查询时间\n 2：恢复时间\n 3：修改时间\n")

    if type == "1":
        urls = "http://test-task-fkccy.tiantianshuibaobao.com/Update_time//update?f=get"  # 疯狂猜成语获取服务器时间
        request = urllib.request.Request(urls)
        response = urllib.request.urlopen(request)
        openurl = response.read()
        # timenow =openurl.decode()
        print("当前服务时间：")
        print (openurl)
        # break

    if type == "2":
        nowtime = time.strftime('%Y-%m-%d%%20%H:%M:%S')
        fullurl2 = url + "&datetime=" + nowtime
        # print fullurl
        request = urllib.request.Request(fullurl2)
        response = urllib.request.Request(request)
        print("已恢复当前服务时间：")
        print (response.read())
        # break

    if type == "3":
        while True:  # 无限循环语句
            nowtime = time.strftime('%Y-%m-%d%%20%H:%M:%S')
            print ("例如：" + nowtime)
            yeartime = input("请输入你想修改的时间：            ！！！请复制例子进行修改时间！！！\n恢复当前时间请输入：0\n")
            #请使用例子中的格式，不得有误
            if yeartime == "0":
                nowtime = time.strftime('%Y-%m-%d%%20%H:%M:%S')
                nowtimeurl = url + "&datetime=" + nowtime
                # print nowtimeurl
                request = urllib.request.Request(nowtimeurl)
                response = urllib.request.urlopen(request)
                print (response.read())
                break

            else:
                fullurl3 = url + "&datetime=" + yeartime
                # print fullurl3
                request = urllib.request.Request(fullurl3)
                response = urllib.request.urlopen(request)
                print (response.read())