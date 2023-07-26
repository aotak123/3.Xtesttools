# coding=utf-8

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.common.exceptions import NoSuchElementException
import time

capabilities = {}
capabilities['platformName'] = 'Android'  # Android平台测试
capabilities['platformVersion'] = '11.0.0'
capabilities['deviceName'] = 'EVA-AL10'
capabilities['appPackage'] = 'cn.com.livelab'  # 系统手机中的联系人app的包名
capabilities['appActivity'] = 'cn.com.livelab.MainActivity'  # 系统手机中的联系人app的主入口activity
capabilities['noReset'] = 'true'  # 不重置app
capabilities['autoAcceptAlerts'] = 'true'
capabilities['autoWebview'] = 'false'
capabilities['newCommandTimeout'] = '600'
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', capabilities)  # 连接测试所在服务器

# 配置
演唱会开始时间 = 1690426800  # 请设置需要开抢的演唱会时间戳1690340100
演唱会名称 = "【上海】Amber刘逸云2023“No More Sad Songs”巡演-上海站"  # 输入演唱会全名

# 执行代码
time.sleep(15)  # 等待app启动
# TouchAction(driver).tap(x=429, y=152).perform()  # 进入搜索页面
driver.tap([(176, 133), (925, 177)])  # 进入搜索页面
time.sleep(2)
# TouchAction(driver).tap(x=429, y=152).perform()  # 光标定位搜索
driver.tap([(158, 109), (858, 189)])  # 进入搜索页面
time.sleep(2)
选择输入 = driver.find_element_by_xpath(
    "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.widget.EditText")
选择输入.send_keys(演唱会名称)
time.sleep(2)
# 选择演唱会 = driver.find_element_by_xpath("(//android.view.View[@content-desc=\"" + 演唱会名称 + "\"])[2]")
# 选择演唱会.click()
driver.tap([(58, 227), (1022, 371)])  # 选择演唱会
time.sleep(2)
# TouchAction(driver).tap(x=500, y=458).perform()  # 选择演唱会
driver.tap([(58, 218), (1022, 636)])  # 选择演唱会
time.sleep(4)


# 等待抢票
def task():
    while True:
        当前时间戳 = time.time()
        当前时间 = int(当前时间戳)
        需要等待时间 = 演唱会开始时间 - 当前时间

        # print(当前时间)
        if 当前时间 >= 演唱会开始时间:
            print('开始抢票')
            # TouchAction(driver).tap(x=698, y=2116).perform()  # 进入抢票
            driver.tap([(86, 2020), (994, 2152)])  # 进入抢票
            time.sleep(0.3)
            # TouchAction(driver).tap(x=698, y=2116).perform()  # 确认订单
            driver.tap([(636, 2066), (1022, 2181)])  # 确认订单
            time.sleep(0.3)
            # TouchAction(driver).tap(x=698, y=2116).perform()  # 立即支付
            driver.tap([(636, 2066), (1022, 2181)])  # 立即支付
            time.sleep(1)
            while True:
                # TouchAction(driver).tap(x=531, y=1558).perform()  # 选择重试
                driver.tap([(227, 1525), (805, 1601)])  # 选择重试
                time.sleep(0.3)
                # TouchAction(driver).tap(x=698, y=2116).perform()  # 确认订单
                driver.tap([(636, 2066), (1022, 2181)])  # 确认订单
                time.sleep(0.3)
                # TouchAction(driver).tap(x=698, y=2116).perform()  # 立即支付
                driver.tap([(636, 2066), (1022, 2181)])  # 立即支付
                time.sleep(0.3)
            # return
        elif 当前时间 < 演唱会开始时间:
            print("未到抢票时间")
            print("需要等待时间：" + str(需要等待时间))
            time.sleep(需要等待时间)


task()
