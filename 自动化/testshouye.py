# coding=utf-8

from selenium import webdriver
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.common.exceptions import NoSuchElementException
import time
import sys

while True:
    capabilities = {}
    capabilities['platformName'] = 'Android'  # Android平台测试
    # 华为8x
    capabilities['platformVersion'] = '10'
    capabilities['deviceName'] = 'JSN-AL00'

    capabilities['appPackage'] = 'com.kamitu.drawsth.standalone.free.android'  # 系统手机中的联系人app的包名
    capabilities['appActivity'] = 'com.qsmy.busniess.welcome.WelcomeActivity'  # 系统手机中的联系人app的主入口activity
    capabilities['noReset'] = 'True'  # 不重置app
    capabilities['autoAcceptAlerts'] = 'true'
    capabilities['autoWebview'] = 'false'
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', capabilities)  # 连接测试所在服务器

    time.sleep(10)  # 等待10秒加载进入首页

    try:
        l2 = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/text_title")
        time.sleep(5)
    except NoSuchElementException:
        nowtime = time.strftime('%Y-%m-%d% %H:%M:%S')
        print("首页无异常" + "     " + nowtime)
        # sys.exit()
    else:
        l2.click()
        driver.get_screenshot_as_file("/Users/aotak/Documents/autotest/首页异常.png")
        print("首页异常")
        sys.exit()
    time.sleep(3)

    TouchAction(driver).tap(x=526, y=1845).perform()  # 进入接龙页面
    time.sleep(3)

    try:
        l2 = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/text_title")
        time.sleep(5)
    except NoSuchElementException:
        nowtime = time.strftime('%Y-%m-%d% %H:%M:%S')
        print("接龙无异常" + "     " + nowtime)
        # sys.exit()
    else:
        l2.click()
        driver.get_screenshot_as_file("/Users/aotak/Documents/autotest/接龙异常.png")
        print("接龙异常")
        sys.exit()
    time.sleep(3)
    # TouchAction(driver).tap(x=90, y=140).perform()# 返回首页
    # time.sleep(3)
    TouchAction(driver).tap(x=934, y=131).perform()  # 进入拼图页面
    time.sleep(3)
    try:
        l2 = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/text_title")
        time.sleep(5)
    except NoSuchElementException:
        nowtime = time.strftime('%Y-%m-%d% %H:%M:%S')
        print("拼图无异常" + "     " + nowtime)
        # sys.exit()
    else:
        l2.click()
        driver.get_screenshot_as_file("/Users/aotak/Documents/autotest/拼图异常.png")
        print("拼图异常")
        sys.exit()
    time.sleep(3)
    TouchAction(driver).tap(x=90, y=140).perform()
    # back = driver.find_element_by_xpath(
    #     "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.widget.Image")
    # back.click()
    time.sleep(3)
    TouchAction(driver).tap(x=90, y=140).perform()  # 返回首页
    time.sleep(3)
    try:
        l2 = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/text_title")
        time.sleep(5)
    except NoSuchElementException:
        nowtime = time.strftime('%Y-%m-%d% %H:%M:%S')
        print("返回首页无异常" + "     " + nowtime)
        # sys.exit()
    else:
        l2.click()
        driver.get_screenshot_as_file("/Users/aotak/Documents/autotest/返回首页异常.png")
        print("返回首页异常")
        sys.exit()
    time.sleep(3)
    TouchAction(driver).tap(x=120, y=2075).perform()  # 进入看图猜成语
    time.sleep(3)
    TouchAction(driver).tap(x=352, y=2080).perform()  # 选择看图第一关
    time.sleep(3)
    try:
        l2 = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/text_title")
        time.sleep(5)
    except NoSuchElementException:
        nowtime = time.strftime('%Y-%m-%d% %H:%M:%S')
        print("看图无异常" + "     " + nowtime)
        # sys.exit()
    else:
        l2.click()
        driver.get_screenshot_as_file("/Users/aotak/Documents/autotest/看图异常.png")
        print("看图异常")
        sys.exit()
    time.sleep(3)

    # TouchAction(driver).tap(x=330, y=1150).perform() # 选择广告
    # time.sleep(40)
    # try:
    #     l2 = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/text_title")
    #     time.sleep(5)
    # except NoSuchElementException:
    #     nowtime = time.strftime('%Y-%m-%d% %H:%M:%S')
    #     print("广告无异常" +"     "+ nowtime)
    #     # sys.exit()
    # else:
    #     l2.click()
    #     driver.get_screenshot_as_file("/Users/aotak/Documents/autotest/异常.png")
    #     print("异常")
    #     sys.exit()
    # time.sleep(1)
# TouchAction(driver).tap(x=500, y=400).perform()
