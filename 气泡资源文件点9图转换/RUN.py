# -*- coding:utf-8 -*-
import os
Tool = "/Users/aotak/PycharmProjects/3.Xtesttools/气泡资源文件点9图转换/dian9zhuanhuan"

#替换图片地址后运行
png = "/Users/aotak/Desktop/1/1.9.png"

cmd = 'ls -a'
Call = os.popen("cd " + Tool + "&& aapt s -i " + png + " -o /Users/aotak/Desktop/run.png")

OutError = Call.read()

print(OutError)

