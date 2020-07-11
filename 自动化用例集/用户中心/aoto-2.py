# coding=utf-8

"""
登录引导
1.新安装用户打开app
2.非游客用户打开app
"""
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.common.exceptions import NoSuchElementException
import time
import urllib.request
import ssl

capabilities = {}
capabilities['platformName'] = 'Android'  # Android平台测试
# 华为8x
capabilities['platformVersion'] = '10'
capabilities['deviceName'] = 'JSN-AL00'

capabilities['appPackage'] = 'com.kamitu.drawsth.standalone.free.android'  # 系统手机中的联系人app的包名
capabilities['appActivity'] = 'com.qsmy.busniess.welcome.WelcomeActivity'  # 系统手机中的联系人app的主入口activity
capabilities['noReset'] = 'false'  # 不重置app
capabilities['autoGrantPermissions'] = 'true' # appium自动设置权限
capabilities['autoWebview'] = 'false'
capabilities['mobile'] = '18017700610'
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', capabilities)  # 连接测试所在服务器
mobile = capabilities['mobile']
context = ssl._create_unverified_context()

def check_agree():  # 检查用户协议及隐私条款
    try:
        check_agree = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/mh")
    except NoSuchElementException:
        pass
    else:
        check_agree.click()
        print("FKC-4:权限引导：隐私及授权弹窗   PASS")
check_agree()
time.sleep(5)

def wx_login():  # 微信登录
    try:
        wx_login = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/p6")
    except NoSuchElementException:
        pass
    else:
        wx_login.click()
        print("FKC-8:账号登录：微信（三方）登录   PASS")
wx_login()
time.sleep(10)  # 等待10秒加载进入首页
