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
capabilities['noReset'] = 'true'  # 不重置app
capabilities['autoGrantPermissions'] = 'true' # appium自动设置权限
capabilities['autoWebview'] = 'false'
capabilities['mobile'] = '18017700610'
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', capabilities)  # 连接测试所在服务器
mobile = capabilities['mobile']
context = ssl._create_unverified_context()


time.sleep(10)  # 等待10秒加载进入首页

def check_sign():  # 检查用户签到弹窗
    try:
        el1 = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/gu")
    except NoSuchElementException:
        pass
    else:
        el1.click()
        time.sleep(3)
        el2 = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/bo")
        el2.click()
check_sign()
time.sleep(3)

def check_signonoff():  # 检查是否开启签到提示
    try:
        el3 = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/fn")
    except NoSuchElementException:
        pass
    else:
        el3.click()
check_signonoff()
time.sleep(3)
print("FKC-9:自动登录   PASS")