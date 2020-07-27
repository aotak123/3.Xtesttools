# coding=utf-8

from appium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time

while True:
    capabilities = {}
# Android平台测试
    capabilities['platformName'] = 'Android'
    capabilities['platformVersion'] = '10'
    capabilities['deviceName'] = 'SEA-AL10'
# 系统手机中的联系人app的包名
# # 疯狂猜成语
#     capabilities['appPackage'] = 'com.kamitu.drawsth.standalone.free.android'
#     capabilities['appActivity'] = 'com.qsmy.busniess.welcome.WelcomeActivity'
# # 多多守护
#     capabilities['appPackage'] = 'com.xiaoxian.guardian.everyday'
#     capabilities['appActivity'] = 'com.qsmy.busniess.welcome.WelcomeActivity'
# # 看图猜成语
#     capabilities['appPackage'] = 'com.xiaoxian.cy.kantu.android'
#     capabilities['appActivity'] = 'com.qsmy.busniess.welcome.WelcomeActivity'
# 天天守护
    capabilities['appPackage'] = 'com.xiaoxian.guardian.everyday'
    capabilities['appActivity'] = 'com.qsmy.busniess.welcome.WelcomeActivity'
    capabilities['unicodeKeyboard'] = 'true'  # 如果指定UI2作为驱动，不需要配置
    capabilities['resetKeyboard'] = 'true'  # 重置自动化时设置的键盘
    capabilities['noReset'] = 'false'
    capabilities['autoGrantPermissions'] = 'true'  # appium自动设置权限
    capabilities['autoWebview'] = 'false'

# 连接测试机所在服务器服务器
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', capabilities)
    time.sleep(5)