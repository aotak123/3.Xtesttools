# -*- coding:utf-8 -*-
import os

apk = "/Users/aotak/Desktop/【抖你1.2.0版本基础包】chinaDouni_v1.2.0_2021-12-08-0014_Product_ceshi2.apk"  # 配置需要打包的母包地址，请使用『/』分隔符!!!

# 非加固包
# os.popen("java -jar walle-cli-all.jar batch2 -f config.json " + apk)

# 360加固包
os.popen("java -jar new-walle-cli-all.jar batch2 -f config.json " + apk)

print("打包成功，同母包目录下")
