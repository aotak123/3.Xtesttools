import urllib.request
import ssl
context = ssl._create_unverified_context()

url = "https://acs.m.taobao.com/gw/mtop.alibaba.detail.subpage.getdetail/2.0?t=1699898684&rnd=2A0CF4FB8F0F17BD80FD48DC95F8A6A3&data=%7B%22scenario%22%3A%22itemsku%22%2C%22itemId%22%3A%22745919556420%22%2C%22dataType%22%3A%222%22%2C%22dataId%22%3A%22212223275%22%2C%22exParams%22%3A%22%7B%5C%22dataType%5C%22%3A%5C%222%5C%22%2C%5C%22scenario%5C%22%3A%5C%22itemsku%5C%22%2C%5C%22bizCode%5C%22%3A%5C%22ali.china.damai%5C%22%2C%5C%22itemId%5C%22%3A%5C%22745919556420%5C%22%2C%5C%22dataId%5C%22%3A%5C%22212223275%5C%22%7D%22%2C%22bizCode%22%3A%22ali.china.damai%22%2C%22comboChannel%22%3A%221%22%7D"
request = urllib.request.Request(url)  # 构建请求url
response = urllib.request.urlopen(request, context=context)  # ssl证书免验证加入,context = context# 打开请求url链接
num = response.read()
print(num)
