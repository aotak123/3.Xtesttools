# -*- coding:utf-8 -*-
import os

Tool = "/Users/aotak/PycharmProjects/3.Xtesttools/气泡资源文件点9图转换/dian9zhuanhuan"  # 工具路径地址

png_path = "/Users/aotak/Downloads/聊天气泡.9.png"  # 图片路径地址
png_rename = "run.png"  # 转换后文件命名

cmd = 'ls -a'  # 前置cmd指令
CallCMD = os.popen("cd " + Tool + "&& aapt s -i " + png_path + " -o /Users/aotak/Desktop/" + png_rename)  # cmd指令执行
result = CallCMD.read()  # 读取cmd返回信息
print(result)  # 打印cmd信息
