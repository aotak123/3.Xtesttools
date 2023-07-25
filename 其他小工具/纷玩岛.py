# coding=utf-8

from appium import webdriver
from datetime import datetime
from appium.webdriver.common.touch_action import TouchAction
from selenium.common.exceptions import NoSuchElementException
import time
import os


# capabilities = {}
# capabilities['platformName'] = 'Android'  # Android平台测试
# capabilities['platformVersion'] = '11.0.0'
# capabilities['deviceName'] = 'EVA-AL10'
# capabilities['appPackage'] = 'cn.com.livelab'  # 系统手机中的联系人app的包名
# capabilities['appActivity'] = 'cn.com.livelab.WelcomeActivity'  # 系统手机中的联系人app的主入口activity
# capabilities['noReset'] = 'true'  # 不重置app
# capabilities['autoAcceptAlerts'] = 'true'
# capabilities['autoWebview'] = 'false'
# driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', capabilities)  # 连接测试所在服务器
#


def task():
    while True:
        演唱会开始时间 = 1690278576  # 请设置需要开抢的演唱会时间戳
        当前时间戳 = time.time()
        当前时间 = int(当前时间戳)
        需要等待时间 = 演唱会开始时间 - 当前时间

        # print(当前时间)
        if 当前时间 >= 演唱会开始时间:
            print('开始抢票')
            # time.sleep(tc)
            return
        elif 当前时间 < 演唱会开始时间:
            print("未到抢票时间")
            print("需要等待时间：" + str(需要等待时间))
            time.sleep(abs(需要等待时间))


task()
