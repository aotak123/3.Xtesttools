# -*- coding:utf-8 -*-
import os

apk = "/Users/aotak/Desktop/crazyldinoms_v6.3.9_2021-05-29-2041_Product_639_jiagu_sign.apk"  # 配置需要打包的母包地址，请使用『/』分隔符!!!

# os.popen("java -jar walle-cli-all.jar batch2 -f config.json " + apk)  # 非加固包

os.popen("java -jar new-walle-cli-all.jar batch2 -f config.json " + apk)  # 360加固包

print("打包成功，同母包目录下")
