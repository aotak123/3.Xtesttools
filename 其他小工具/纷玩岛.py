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
capabilities['appActivity'] = 'cn.com.livelab.WelcomeActivity'  # 系统手机中的联系人app的主入口activity
capabilities['noReset'] = 'true'  # 不重置app
capabilities['autoAcceptAlerts'] = 'true'
capabilities['autoWebview'] = 'false'
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', capabilities)  # 连接测试所在服务器

演唱会开始时间 = 1690278576  # 请设置需要开抢的演唱会时间戳
演唱会名称 = "【南京】2023MAYDAY五月天「好好好想见到你」巡回演唱会-南京站"

time.sleep(15)  # 等待app启动
TouchAction(driver).tap(x=429, y=152).perform()  # 进入搜索页面
time.sleep(1)
TouchAction(driver).tap(x=429, y=152).perform()  # 光标定位搜索
time.sleep(1)
el2 = driver.find_element_by_xpath(
    "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.widget.EditText")
el2.send_keys(演唱会名称)
el3 = driver.find_element_by_xpath("(//android.view.View[@content-desc=\"" + 演唱会名称 + "\"])[2]")
time.sleep(1)
TouchAction(driver).tap(x=500, y=458).perform()  # 光标定位搜索


def task():
    while True:
        当前时间戳 = time.time()
        当前时间 = int(当前时间戳)
        需要等待时间 = 演唱会开始时间 - 当前时间

        # print(当前时间)
        if 当前时间 >= 演唱会开始时间:
            print('开始抢票')
            try:
                立即购买 = driver.find_element_by_accessibility_id("立即购买")
            except NoSuchElementException:
                driver.back()
            else:
                立即购买.click()
            time.sleep(1)
            try:
                确认下单 = driver.find_element_by_accessibility_id("确认下单")
            except NoSuchElementException:
                driver.back()
            else:
                确认下单.click()
            time.sleep(1)
            try:
                立即支付 = driver.find_element_by_accessibility_id("立即支付")
            except NoSuchElementException:
                driver.back()
            else:
                立即支付.click()
            # return
        elif 当前时间 < 演唱会开始时间:
            print("未到抢票时间")
            print("需要等待时间：" + str(需要等待时间))
            time.sleep(需要等待时间)


task()
