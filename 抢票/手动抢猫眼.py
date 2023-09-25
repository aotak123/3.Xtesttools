# coding=utf-8

from appium import webdriver
# from appium.webdriver.common.touch_action import TouchAction
import time
from dateutil import parser

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
date_str = "2023-09-25 14:07:00"  # 请设置需要开抢的演唱会时间
dt = parser.parse(date_str)
timestamp = dt.timestamp()
fixtime = str(timestamp).split('.')[0]
starttime = int(fixtime)  # 将str格式转成int格式
print("场次开抢时间：", date_str)
# print("转换时间戳：", starttime)
# starttime = 1691563020  # 请设置需要开抢的演唱会时间戳  2023-08-09 14:37:00

"""请手动启动大麦app进入演唱会待抢页面并填写预约抢票"""
"""请在抢票倒计时前5分钟左右开启,保证屏幕亮着"""


# 等待抢票
def task():
    while True:
        nowtimestamp = time.time()  # 当前时间戳
        nowtime = int(nowtimestamp)  # 时间戳转换int格式
        waitingtime = starttime - nowtime  # 需要等待的时间 = 开始时间 - 现在时间

        # print(当前时间)
        if nowtime >= starttime:  # 如果 现在时间 ≥ 开始时间
            print('开始抢票')
            driver.tap([(780, 2084), (982, 2151)])  # 入口立即购买
            time.sleep(0.1)
            driver.tap([(780, 2084), (982, 2151)])  # 确认订单
            time.sleep(0.1)
            driver.tap([(780, 2084), (982, 2151)])  # 立即支付
            time.sleep(0.1)
            while True:
                driver.tap([(297, 1456), (774, 1519)])  # 选择重试
                time.sleep(0.1)
                driver.tap([(79, 951), (477, 1355)])  # 选择档位
                time.sleep(0.02)
                driver.tap([(780, 2084), (982, 2151)])  # 确认订单
                time.sleep(0.1)
                driver.tap([(780, 2084), (982, 2151)])  # 立即支付
                time.sleep(0.1)
            # return
        elif nowtime < starttime:  # 如果现在时间＜开始时间
            if waitingtime > 120:  # 是否等待时间大于2分钟
                print("未到抢票时间,需要等待：" + str(waitingtime))
                print("120秒后重新判断")
                time.sleep(120)  # 等待2分钟后重新判断防止进程卡死
            elif waitingtime <= 120:  # 是否等待时间小于2分钟
                print("未到抢票时间,需要等待：" + str(waitingtime))
                time.sleep(waitingtime)
                print('开始抢票')
                driver.tap([(780, 2084), (982, 2151)])  # 入口立即购买
                time.sleep(0.1)
                driver.tap([(780, 2084), (982, 2151)])  # 确认订单
                time.sleep(0.1)
                driver.tap([(780, 2084), (982, 2151)])  # 立即支付
                time.sleep(0.1)
                while True:
                    driver.tap([(297, 1456), (774, 1519)])  # 选择重试
                    time.sleep(0.1)
                    driver.tap([(79, 951), (477, 1355)])  # 选择档位
                    time.sleep(0.02)
                    driver.tap([(780, 2084), (982, 2151)])  # 确认订单
                    time.sleep(0.1)
                    driver.tap([(780, 2084), (982, 2151)])  # 立即支付
                    time.sleep(0.1)


task()
