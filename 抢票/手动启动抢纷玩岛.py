# coding=utf-8

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.common.exceptions import NoSuchElementException
import time

capabilities = {}
capabilities['platformName'] = 'Android'  # Android平台测试
capabilities['platformVersion'] = '11.0.0'
capabilities['deviceName'] = 'EVA-AL10'
capabilities['noReset'] = 'true'  # 不重置app
capabilities['autoAcceptAlerts'] = 'true'
capabilities['autoWebview'] = 'false'
capabilities['newCommandTimeout'] = '600'
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', capabilities)  # 连接测试所在服务器

# 配置
演唱会开始时间 = 1690426800  # 请设置需要开抢的演唱会时间戳   2023-07-27 11:00:00
"""请手动启动纷玩岛app进入代抢页面并填写预约抢票后启动代码"""

# 等待抢票
def task():
    while True:
        当前时间戳 = time.time()
        当前时间 = int(当前时间戳)
        需要等待时间 = 演唱会开始时间 - 当前时间

        # print(当前时间)
        if 当前时间 >= 演唱会开始时间:
            print('开始抢票')
            # TouchAction(driver).tap(x=698, y=2116).perform()  # 入口立即购买
            driver.tap([(215, 2040), (834, 2119)])  # 入口立即购买
            time.sleep(0.3)
            # TouchAction(driver).tap(x=698, y=2116).perform()  # 确认订单
            driver.tap([(673, 2081), (973, 2151)])  # 确认订单
            time.sleep(0.3)
            # TouchAction(driver).tap(x=698, y=2116).perform()  # 立即支付
            driver.tap([(673, 2081), (973, 2151)])  # 立即支付
            time.sleep(1)
            while True:
                # TouchAction(driver).tap(x=531, y=1558).perform()  # 选择重试
                driver.tap([(227, 1525), (805, 1601)])  # 选择重试
                time.sleep(0.3)
                # TouchAction(driver).tap(x=698, y=2116).perform()  # 确认订单
                driver.tap([(673, 2081), (973, 2151)])  # 确认订单
                time.sleep(0.3)
                # TouchAction(driver).tap(x=698, y=2116).perform()  # 立即支付
                driver.tap([(673, 2081), (973, 2151)])  # 立即支付
                time.sleep(0.3)
            # return
        elif 当前时间 < 演唱会开始时间:
            print("未到抢票时间")
            print("需要等待时间：" + str(需要等待时间))
            time.sleep(需要等待时间)


task()
