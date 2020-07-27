# coding=utf-8

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
import time

capabilities = {}
capabilities['platformName'] = 'Android'  # Android平台测试
capabilities['platformVersion'] = '9'
capabilities['deviceName'] = 'MI CC 9e'

capabilities['appPackage'] = 'com.kamitu.drawsth.standalone.free.android'  # 系统手机中的联系人app的包名
capabilities['appActivity'] = 'com.qsmy.busniess.welcome.WelcomeActivity'  # 系统手机中的联系人app的主入口activity
capabilities['noReset'] = 'True'  # 不重置app
capabilities['autoAcceptAlerts'] = 'true'
capabilities['autoWebview'] = 'false'
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', capabilities)  # 连接测试所在服务器

time.sleep(10)  # 等待10秒加载进入首页
time.sleep(5)
TouchAction(driver).tap(x=650, y=1220).perform()
time.sleep(2)

a = 1
while a >= 0:
    print(a)
    time.sleep(5)
    TouchAction(driver).tap(x=650, y=1220).perform()
    time.sleep(2)
    driver.back()
    time.sleep(2)
    TouchAction(driver).tap(x=350, y=1200).perform()  # 进入接龙页面
    time.sleep(2)
    driver.back()
    time.sleep(2)
    a += 1
