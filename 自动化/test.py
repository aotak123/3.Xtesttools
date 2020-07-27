# coding=utf-8

import ssl
import time
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.common.exceptions import NoSuchElementException

capabilities = {}
capabilities['platformName'] = 'Android'  # Android平台测试
# 三星
capabilities['platformVersion'] = '6.0.1'
capabilities['deviceName'] = 'SM-G9250'
capabilities['appPackage'] = 'com.kamitu.drawsth.standalone.free.android'  # 系统手机中的联系人app的包名
capabilities['appActivity'] = 'com.qsmy.busniess.welcome.WelcomeActivity'  # 系统手机中的联系人app的主入口activity
capabilities['noReset'] = 'true'  # 不重置app
capabilities['autoAcceptAlerts'] = 'true'
capabilities['autoWebview'] = 'false'
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', capabilities)  # 连接测试所在服务器
context = ssl._create_unverified_context()

#######################################################################################################################
mobile = "18017700223"
AA = "\033[1;31mNO.1\033[0m " + mobile + " \033[1;31m开始\033[0m"
print(AA)
nowtime = time.strftime('%Y-%m-%d% %H:%M:%S')
print(nowtime)
time.sleep(5)


time.sleep(15)  # 等待10秒加载进入首页


def check_signwindows():  # 检查用户签到弹窗
    try:
        check_signwindows = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/iv_signin_get")
    except NoSuchElementException:
        print("无签到弹窗")
    else:
        TouchAction(driver).tap(x=1270, y=655).perform()
        time.sleep(3)


check_signwindows()
time.sleep(3)
TouchAction(driver).tap(x=707, y=2070).perform()  # 进入接龙页面
time.sleep(3)
driver.back()
time.sleep(3)


def check_signtoast():  # 检查是否开启签到提示
    try:
        check_signtoast = driver.find_element_by_id(
            "com.kamitu.drawsth.standalone.free.android:id/iv_checkin_reminder_close")
    except NoSuchElementException:
        print("无签到提示")
    else:
        TouchAction(driver).tap(x=1228, y=748).perform()


check_signtoast()
time.sleep(3)
TouchAction(driver).tap(x=175, y=2385).perform()  # 进入看图猜成语
time.sleep(3)
# 广告次数
a = 12
while a > 0:
    TouchAction(driver).tap(x=475, y=2280).perform()
    time.sleep(1)
    TouchAction(driver).tap(x=1105, y=2188).perform()
    time.sleep(1)
    TouchAction(driver).tap(x=800, y=2280).perform()  # 选择(位置)
    time.sleep(3)
    TouchAction(driver).tap(x=444, y=1560).perform()  # 选择左侧去除多余选项广告
    print(a)
    time.sleep(6)
    try:
        GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
    except NoSuchElementException:
        print("toutiaosdk广告")
        time.sleep(40)
        TouchAction(driver).tap(x=1285, y=139).perform()  # 关闭toutiao广告
        print("toutiaosdk广告关闭")
    else:
        print("GDTsdk广告")
        time.sleep(55)
        driver.back()  # GDTsdk广告按钮
        print("GDTsdk广告关闭")
    a -= 1
    time.sleep(2)
    TouchAction(driver).tap(x=1000, y=1560).perform()  # 选择右侧提示广告
    print(a)
    time.sleep(6)
    try:
        GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
    except NoSuchElementException:
        print("toutiaosdk广告")
        time.sleep(40)
        TouchAction(driver).tap(x=1285, y=139).perform()  # 关闭toutiao广告
        print("toutiaosdk广告关闭")
    else:
        print("GDTsdk广告")
        time.sleep(55)
        driver.back()  # GDTsdk广告按钮
        print("GDTsdk广告关闭")
    # print(a)
    time.sleep(2)
    driver.back()
    time.sleep(2)
    a -= 1
driver.back()  # 返回首页
time.sleep(2)
TouchAction(driver).tap(x=588, y=186).perform()  # 返回进入个人中心
time.sleep(2)
TouchAction(driver).tap(x=1275, y=243).perform()
time.sleep(1)
TouchAction(driver).tap(x=707, y=2467).perform()
time.sleep(1)
TouchAction(driver).tap(x=960, y=1440).perform()
BB = mobile + " \033[1;31m账号退出成功\033[0m"
print(BB)
nowtime = time.strftime('%Y-%m-%d% %H:%M:%S')
print(nowtime)
#######################################################################################################################