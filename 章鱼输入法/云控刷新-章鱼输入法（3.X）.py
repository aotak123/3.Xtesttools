# coding=utf-8
import urllib.request
import ssl
                    ####################——————tak制作  vol.605——————####################

# 定义基础url
context = ssl._create_unverified_context()  # ssl证书免验证，python3需要验证https证书
url = "https://test-zhangyu3.zhihuizhangyu.cn/zycloudcontrol/cloud.basis?pwd=147147"
request = urllib.request.Request(url)
response = urllib.request.urlopen(request,context = context)
# print (response.read())
print("刷新成功")

                    ####################——————tak制作  vol.605——————####################