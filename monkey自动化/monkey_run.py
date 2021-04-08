# -*- coding:utf-8 -*-
import os
import time

monkeyjar = "Monkey自动化/monkey.jar"
frameworkjar = "Monkey自动化/framework.jar"

# 抖你项目
appPackage = "com.shakeyou.app"

"""
1.首先确保设备已经连上电脑adb
2.push2个文件到手机根目录
3.运行money
"""
os.popen("adb push " + monkeyjar + " /sdcard/")
print("推送monkeyjar到手机根目录 - 完成")
time.sleep(2)
os.popen("adb push " + frameworkjar + " /sdcard/")
print("推送monkeyjar到手机根目录 - 完成")
time.sleep(2)
os.popen(
    "adb shell CLASSPATH=/sdcard/monkey.jar:/sdcard/framework.jar exec app_process /system/bin tv.panda.test.monkey.Monkey -p " + appPackage + " --uiautomatormix --running-minutes 60")
print("服务启动，等待60分钟后自动结束")

"""参数说明：
1.tv.panda.test.monkey.Monkey 主调入口  无需修改
2.-p com.panda.videoliveplatform  待测appid
3.--uiautomatormix 混合模式（70%控件解析随机点击，其余30%按原Monkey事件概率分布） 
4.--pct-uiautomatormix n 可自定义混合模式中控件解析事件概率
5.--uiautomatordfs DFS深度遍历算法（优化版）（注 Android5不支持dfs）
6.--uiautomatortroy Troy模式
7.执行时长 --running-minutes 60        执行60分钟monkey场景细粒度控制
8.--act-whitelist-file  /sdcard/awl.strings    自定义Activity白名单
"""
