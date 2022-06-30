# -*- coding:utf-8 -*-
import os
import re
import time

# 测试日志接口如下：
# ***/apppubliclogs/applisttiming      X1
# ***/shareinstall_log/openapplist      X1
# ***/apppubliclogs/applist     X1
# ***/apppubliclogs/install     x2
# ***/apppubliclogs/open        X2
# ***/apppubliclogs/activity    X3
# ***/apppubliclogs/ontime      X1

"""
注意事项：
1、！！！请再开发者选项中开启ADB调试并关闭监控ADB安装应用需要用户确认的选项。！！！
2、！！！请优先配置apk安装包以及appPackage、appActivity。！！！
3、由于applist收集上报需要在首次安装后上报，所以需要重复卸载安装。
4、不要使用vivo、oppo等需要安装密码的设备（需要填写账号密码进行安装应用的设备无法完成自动安装）。
5、请根据设备的性能更改安装后的等待时长。各机型运行速度不同。
"""

# window获取安装包的地址:文件右键属性 - 安全 一栏对象名称即为包地址路径。需要自行将路径的分隔号修改为『/』!!!
apk = "/Users/aotak/Desktop/haveSeen_v1.0.0_2020-09-14-1355_Test.apk"  # 配置安装包地址，请使用『/』分隔符!!!

# douni
appPackage = "com.shakeyou.app"
appActivity = "com.shakeyou.app.welcome.WelcomeActivity"


def check_devices():  # 检查adb设备链接
    # connectdeviceid = []   # 多台设备链接时使用，单线程可不使用
    A = os.popen("adb devices")
    outstr = A.read()
    print(outstr)
    # connectdeviceid = re.findall(r'(\w+)\s+device\s', outstr)  # 多台设备链接时使用，单线程可不使用
    # return connectdeviceid  # 多台设备链接时使用，单线程可不使用


check_devices()

# a = 1  # 需要运行设置次数，请使用下面for方案
# while a > 0:
for a in range(200):  # 运行从0开始计算，故此处上限为200次
    print("第", a, "次")  # 打印当前次数


    # a += 1  # while语句使用

    def autolog():

        os.popen("adb install " + apk)  # adb命令安装apk应用包
        time.sleep(5)  # 等待传输、安装的时间 （不同设备需要的时间不同，请根据实际情况定义时间）

        os.popen("adb shell am start -n " + appPackage + "/" + appActivity)  # 启动app (需要先配置包名和activity)
        time.sleep(5)  # 等待打开app（不同设备需要的时间不同，请根据实际情况定义时间）
        # 此处上报install、open、activity、applist、openapplist 日志

        os.popen("adb shell input keyevent 3")  # 模拟点击HOME键，回到手机系统首页，app进入后台
        time.sleep(3)  # 挂起app
        # 此处上报 ontime 日志上报

        os.popen("adb shell am start -n " + appPackage + "/" + appActivity)  # 启动app (需要先配置包名和activity)
        time.sleep(5)  # 等待打开app（不同设备需要的时间不同，请根据实际情况定义时间）
        # 此处上报install、open、activity 日志

        os.popen("adb uninstall " + appPackage)  # 卸载app （配置先包名）
        time.sleep(5)  # 等待卸载app（卸载相对比较快速，为了性能和系统的稳定，这里统一设置为5s）


    autolog()

else:  # else跟随for使用
    print('日志结束')
# Warning: Activity not started, its current task has been brought to the front 该问题并非报错，是安卓将软件放入后台导致的。忽略即可
