# coding=utf-8

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
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
starttime = 1691031600  # 请设置需要开抢的演唱会时间戳   2023-08-03 11:00:00 纷玩岛【上海】杨千嬅 1691031600
"""请手动启动纷玩岛app进入代抢页面并填写预约抢票后启动代码"""


# 等待抢票
def task():
    while True:
        nowtimestamp = time.time()  # 当前时间戳
        nowtime = int(nowtimestamp)  # 时间戳转换int格式
        waitingtime = starttime - nowtime  # 需要等待的时间 = 开始时间 - 现在时间

        # print(当前时间)
        if nowtime >= starttime:  # 如果 现在时间 ≥ 开始时间
            print('开始抢票')
            # TouchAction(driver).tap(x=698, y=2116).perform()  # 入口立即购买
            driver.tap([(215, 2040), (834, 2119)])  # 入口立即购买
            # driver.tap([(215, 2040), (834, 2119)])  # 入口立即购买
            time.sleep(0.1)
            # TouchAction(driver).tap(x=698, y=2116).perform()  # 确认订单
            driver.tap([(673, 2081), (973, 2151)])  # 确认订单
            # driver.tap([(673, 2081), (973, 2151)])  # 确认订单
            time.sleep(0.1)
            # TouchAction(driver).tap(x=698, y=2116).perform()  # 立即支付
            driver.tap([(673, 2081), (973, 2151)])  # 立即支付
            # driver.tap([(673, 2081), (973, 2151)])  # 立即支付
            time.sleep(0.2)
            while True:
                # TouchAction(driver).tap(x=531, y=1558).perform()  # 选择重试
                driver.tap([(227, 1525), (805, 1601)])  # 选择重试
                # driver.tap([(227, 1525), (805, 1601)])  # 选择重试
                time.sleep(0.1)
                # TouchAction(driver).tap(x=698, y=2116).perform()  # 确认订单
                driver.tap([(673, 2081), (973, 2151)])  # 确认订单
                # driver.tap([(673, 2081), (973, 2151)])  # 确认订单
                time.sleep(0.1)
                # TouchAction(driver).tap(x=698, y=2116).perform()  # 立即支付
                driver.tap([(673, 2081), (973, 2151)])  # 立即支付
                # driver.tap([(673, 2081), (973, 2151)])  # 立即支付
                time.sleep(0.1)
            # return
        elif nowtime < starttime:  # 如果现在时间＜开始时间
            if waitingtime > 120:  # 是否等待时间大于2分钟
                print("未到抢票时间,需要等待：" + str(waitingtime))
                print("2分钟后重新判断")
                time.sleep(120)  # 等待2分钟后重新判断防止进程卡死
                # driver.tap([(44, 1977), (161, 1974)])  # 点击屏幕
            elif waitingtime <= 120:  # 是否等待时间小于2分钟
                print("未到抢票时间,需要等待：" + str(waitingtime))
                time.sleep(waitingtime)
                driver.swipe(549, 581, 549, 1140)  # 刷新页面
                # TouchAction(driver).press(x=549, y=581).move_to(x=549, y=1140).release().perform()  # 刷新页面
                print('开始抢票')
                # time.sleep(0.1)
                # TouchAction(driver).tap(x=698, y=2116).perform()  # 入口立即购买
                driver.tap([(215, 2040), (834, 2119)])  # 入口立即购买
                # driver.tap([(215, 2040), (834, 2119)])  # 入口立即购买
                time.sleep(0.1)
                # TouchAction(driver).tap(x=698, y=2116).perform()  # 确认订单
                driver.tap([(673, 2081), (973, 2151)])  # 确认订单
                # driver.tap([(673, 2081), (973, 2151)])  # 确认订单
                time.sleep(0.1)
                # TouchAction(driver).tap(x=698, y=2116).perform()  # 立即支付
                driver.tap([(673, 2081), (973, 2151)])  # 立即支付
                # driver.tap([(673, 2081), (973, 2151)])  # 立即支付
                time.sleep(0.2)
                while True:
                    # TouchAction(driver).tap(x=531, y=1558).perform()  # 选择重试
                    driver.tap([(227, 1525), (805, 1601)])  # 选择重试
                    # driver.tap([(227, 1525), (805, 1601)])  # 选择重试
                    time.sleep(0.1)
                    # TouchAction(driver).tap(x=698, y=2116).perform()  # 确认订单
                    driver.tap([(673, 2081), (973, 2151)])  # 确认订单
                    # driver.tap([(673, 2081), (973, 2151)])  # 确认订单
                    time.sleep(0.1)
                    # TouchAction(driver).tap(x=698, y=2116).perform()  # 立即支付
                    driver.tap([(673, 2081), (973, 2151)])  # 立即支付
                    # driver.tap([(673, 2081), (973, 2151)])  # 立即支付
                    time.sleep(0.1)


task()
