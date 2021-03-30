# -*- coding:utf-8 -*-
import os

apk = "/Users/aotak/Desktop/shakeu_chinadouni_v1.0.0_2021-03-30-2241_Product.apk"  # 配置需要打包的母包地址，请使用『/』分隔符!!!

os.popen("java -jar walle-cli-all.jar batch2 -f config.json " + apk)
print("打包成功，同母包目录下")