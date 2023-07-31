# coding=utf-8

from appium import webdriver
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
starttime = 1690794000  # 请设置需要开抢的演唱会时间戳  2023-07-31 17:00:00

"""请手动启动大麦app进入演唱会待抢页面并填写预约抢票后启动代码"""


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
            driver.tap([(357, 2091), (951, 2154)])  # 入口立即购买
            driver.tap([(357, 2091), (951, 2154)])  # 入口立即购买
            time.sleep(0.1)
            # TouchAction(driver).tap(x=698, y=2116).perform()  # 确认订单
            driver.tap([(591, 2087), (960, 2154)])  # 确认订单
            driver.tap([(591, 2087), (960, 2154)])  # 确认订单
            time.sleep(0.1)
            # TouchAction(driver).tap(x=698, y=2116).perform()  # 立即支付
            driver.tap([(780, 2084), (982, 2151)])  # 立即支付
            driver.tap([(780, 2084), (982, 2151)])  # 立即支付
            time.sleep(0.2)
            while True:
                # TouchAction(driver).tap(x=531, y=1558).perform()  # 选择重试
                driver.tap([(297, 1456), (774, 1519)])  # 选择重试
                driver.tap([(297, 1456), (774, 1519)])  # 选择重试
                time.sleep(0.1)
                driver.tap([(79, 951), (477, 1355)])  # 选择档位
                driver.tap([(79, 951), (477, 1355)])  # 选择档位
                time.sleep(0.05)
                # TouchAction(driver).tap(x=698, y=2116).perform()  # 确认订单
                driver.tap([(591, 2087), (960, 2154)])  # 确认订单
                driver.tap([(591, 2087), (960, 2154)])  # 确认订单
                time.sleep(0.1)
                # TouchAction(driver).tap(x=698, y=2116).perform()  # 立即支付
                driver.tap([(780, 2084), (982, 2151)])  # 立即支付
                driver.tap([(780, 2084), (982, 2151)])  # 立即支付
                time.sleep(0.1)
            # return
        elif nowtime < starttime:  # 如果现在时间＜开始时间
            if waitingtime > 180:  # 是否等待时间大于3分钟
                print("未到抢票时间,需要等待：" + str(waitingtime))
                print("60秒后重新判断")
                time.sleep(60)  # 等待1分钟后重新判断防止进程卡死
                driver.tap([(79, 2277), (101, 2264)])  # 点击屏幕
            elif waitingtime <= 60:  # 是否等待时间小于1分钟
                print("未到抢票时间,需要等待：" + str(waitingtime))
                time.sleep(waitingtime - 0.5)
                print('开始抢票')
                # TouchAction(driver).tap(x=698, y=2116).perform()  # 入口立即购买
                driver.tap([(357, 2091), (951, 2154)])  # 入口立即购买
                driver.tap([(357, 2091), (951, 2154)])  # 入口立即购买
                time.sleep(0.1)
                # TouchAction(driver).tap(x=698, y=2116).perform()  # 确认订单
                driver.tap([(591, 2087), (960, 2154)])  # 确认订单
                driver.tap([(591, 2087), (960, 2154)])  # 确认订单
                time.sleep(0.1)
                # TouchAction(driver).tap(x=698, y=2116).perform()  # 立即支付
                driver.tap([(780, 2084), (982, 2151)])  # 立即支付
                driver.tap([(780, 2084), (982, 2151)])  # 立即支付
                time.sleep(0.2)
                while True:
                    # TouchAction(driver).tap(x=531, y=1558).perform()  # 选择重试
                    driver.tap([(297, 1456), (774, 1519)])  # 选择重试
                    driver.tap([(297, 1456), (774, 1519)])  # 选择重试
                    time.sleep(0.1)
                    driver.tap([(79, 951), (477, 1355)])  # 选择档位
                    driver.tap([(79, 951), (477, 1355)])  # 选择档位
                    time.sleep(0.05)
                    # TouchAction(driver).tap(x=698, y=2116).perform()  # 确认订单
                    driver.tap([(591, 2087), (960, 2154)])  # 确认订单
                    driver.tap([(591, 2087), (960, 2154)])  # 确认订单
                    time.sleep(0.1)
                    # TouchAction(driver).tap(x=698, y=2116).perform()  # 立即支付
                    driver.tap([(780, 2084), (982, 2151)])  # 立即支付
                    driver.tap([(780, 2084), (982, 2151)])  # 立即支付
                    time.sleep(0.1)


task()
