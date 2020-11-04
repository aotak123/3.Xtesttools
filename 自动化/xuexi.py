# coding=utf-8

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.common.exceptions import NoSuchElementException
import time
import ssl

capabilities = {}
capabilities['platformName'] = 'Android'  # Android平台测试
capabilities['platformVersion'] = '10'
capabilities['deviceName'] = 'SEA-AL10'
capabilities['appPackage'] = 'cn.xuexi.android'  # 系统手机中的联系人app的包名
capabilities['appActivity'] = 'com.alibaba.android.rimet.biz.SplashActivity'  # 系统手机中的联系人app的主入口activity
capabilities['noReset'] = 'true'  # 不重置app
capabilities['autoAcceptAlerts'] = 'true'
capabilities['autoWebview'] = 'false'
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', capabilities)  # 连接测试所在服务器
context = ssl._create_unverified_context()


#############################################################################################################################################################
def panguan(mobile,passnumber):
    time.sleep(5)
    print("\033[1;31mProject.\033[0m " + str(mobile) + " \033[1;31mSTART\033[0m : " + time.strftime('%H:%M:%S'))
    # 登录模块
    try:
        edit_mobile = driver.find_element_by_id("cn.xuexi.android:id/et_phone_input")  # 选择手机号登录
    except NoSuchElementException:
        print("自动登录成功")
    else:
        edit_mobile.send_keys(mobile)
        time.sleep(1)
        passnum = driver.find_element_by_id("cn.xuexi.android:id/et_pwd_login")
        passnum.send_keys(passnumber)
        time.sleep(1)
        loginin = driver.find_element_by_id("cn.xuexi.android:id/btn_next")
        loginin.click()
        print("账号登录成功")
    time.sleep(3)  # 等待加载进入首页
    # 检查是否弹出隐私协议
    try:
        check_signwindows = driver.find_element_by_id("cn.xuexi.android:id/ui_common_base_ui_activity_toolbar")
    except NoSuchElementException:
        print("无协议弹窗")
    else:
        TouchAction(driver).tap(x=613, y=1421).perform()
        time.sleep(3)
    # 刷新闻 6条新闻
    TouchAction(driver).tap(x=601, y=197).perform()  # 选择分类
    TouchAction(driver).tap(x=275, y=297).perform()  # 选择进入要闻
    time.sleep(1)
    TouchAction(driver).tap(x=357, y=1321).perform()  # 点击查看新闻
    time.sleep(1)
    TouchAction(driver).press(x=639, y=1214).move_to(x=660, y=336).release().perform()  # 滚动第一次新闻
    time.sleep(2)
    TouchAction(driver).press(x=639, y=1214).move_to(x=660, y=336).release().perform()  # 滚动第一次新闻
    time.sleep(2)
    TouchAction(driver).press(x=639, y=1214).move_to(x=660, y=336).release().perform()  # 滚动第一次新闻
    time.sleep(2)
    driver.back()


    TouchAction(driver).tap(x=601, y=197).perform()  # 选择分类
    TouchAction(driver).tap(x=435, y=297).perform()  # 选择新思想
    time.sleep(1)
    TouchAction(driver).tap(x=357, y=1321).perform()  # 点击查看新闻
    time.sleep(1)
    TouchAction(driver).press(x=639, y=1214).move_to(x=660, y=336).release().perform()  # 滚动第一次新闻
    time.sleep(2)
    TouchAction(driver).press(x=639, y=1214).move_to(x=660, y=336).release().perform()  # 滚动第一次新闻
    time.sleep(2)
    TouchAction(driver).press(x=639, y=1214).move_to(x=660, y=336).release().perform()  # 滚动第一次新闻
    time.sleep(2)
    driver.back()

    TouchAction(driver).tap(x=601, y=197).perform()  # 选择分类
    TouchAction(driver).tap(x=435, y=297).perform()  # 选择上海
    time.sleep(1)
    TouchAction(driver).tap(x=357, y=1321).perform()  # 点击查看新闻
    time.sleep(1)
    TouchAction(driver).press(x=639, y=1214).move_to(x=660, y=336).release().perform()  # 滚动第一次新闻
    time.sleep(2)
    TouchAction(driver).press(x=639, y=1214).move_to(x=660, y=336).release().perform()  # 滚动第一次新闻
    time.sleep(2)
    TouchAction(driver).press(x=639, y=1214).move_to(x=660, y=336).release().perform()  # 滚动第一次新闻
    time.sleep(2)
    driver.back()

    TouchAction(driver).tap(x=601, y=197).perform()  # 选择分类
    TouchAction(driver).tap(x=110, y=401).perform()  # 选择综合
    time.sleep(1)
    TouchAction(driver).tap(x=357, y=1321).perform()  # 点击查看新闻
    time.sleep(1)
    TouchAction(driver).press(x=639, y=1214).move_to(x=660, y=336).release().perform()  # 滚动第一次新闻
    time.sleep(2)
    TouchAction(driver).press(x=639, y=1214).move_to(x=660, y=336).release().perform()  # 滚动第一次新闻
    time.sleep(2)
    TouchAction(driver).press(x=639, y=1214).move_to(x=660, y=336).release().perform()  # 滚动第一次新闻
    time.sleep(2)
    driver.back()

    TouchAction(driver).tap(x=601, y=197).perform()  # 选择分类
    TouchAction(driver).tap(x=122, y=501).perform()  # 选择发布
    time.sleep(1)
    TouchAction(driver).tap(x=357, y=1321).perform()  # 点击查看新闻
    time.sleep(1)
    TouchAction(driver).press(x=639, y=1214).move_to(x=660, y=336).release().perform()  # 滚动第一次新闻
    time.sleep(2)
    TouchAction(driver).press(x=639, y=1214).move_to(x=660, y=336).release().perform()  # 滚动第一次新闻
    time.sleep(2)
    TouchAction(driver).press(x=639, y=1214).move_to(x=660, y=336).release().perform()  # 滚动第一次新闻
    time.sleep(2)
    driver.back()

    TouchAction(driver).tap(x=601, y=197).perform()  # 选择分类
    TouchAction(driver).tap(x=103, y=589).perform()  # 选择经济
    time.sleep(1)
    TouchAction(driver).tap(x=357, y=1321).perform()  # 点击查看新闻
    time.sleep(1)
    TouchAction(driver).press(x=639, y=1214).move_to(x=660, y=336).release().perform()  # 滚动第一次新闻
    time.sleep(2)
    TouchAction(driver).press(x=639, y=1214).move_to(x=660, y=336).release().perform()  # 滚动第一次新闻
    time.sleep(2)
    TouchAction(driver).press(x=639, y=1214).move_to(x=660, y=336).release().perform()  # 滚动第一次新闻
    time.sleep(2)
    driver.back()

    #刷视频
    TouchAction(driver).tap(x=501, y=1412).perform()  # 点击进入底部电视台
    TouchAction(driver).tap(x=357, y=1321).perform()
    time.sleep(55)
    driver.back()
    TouchAction(driver).tap(x=357, y=1321).perform()
    time.sleep(55)
    driver.back()
    TouchAction(driver).tap(x=351, y=341).perform()
    time.sleep(55)
    driver.back()
    TouchAction(driver).tap(x=351, y=341).perform()
    time.sleep(55)
    driver.back()
    TouchAction(driver).press(x=639, y=1214).move_to(x=660, y=336).release().perform() # 滚动
    TouchAction(driver).tap(x=357, y=1321).perform()
    time.sleep(55)
    driver.back()
    TouchAction(driver).tap(x=357, y=1321).perform()
    time.sleep(55)
    driver.back()
    TouchAction(driver).tap(x=351, y=341).perform()
    time.sleep(55)
    driver.back()
    TouchAction(driver).tap(x=351, y=341).perform()
    time.sleep(55)
    driver.back()
    TouchAction(driver).press(x=639, y=1214).move_to(x=660, y=336).release().perform()  # 滚动
    TouchAction(driver).tap(x=357, y=1321).perform()
    time.sleep(55)
    driver.back()
    TouchAction(driver).tap(x=357, y=1321).perform()
    time.sleep(55)
    driver.back()
    TouchAction(driver).tap(x=351, y=341).perform()
    time.sleep(55)
    driver.back()
    TouchAction(driver).tap(x=351, y=341).perform()
    time.sleep(55)
    driver.back()



#############################################################################################################################################################

if __name__ == '__main__':
    panguan(mobile ="15692176153",passnumber= "aotak19931128")  # NO.01

#############################################################################################################################################################
finally2 = "\033[1;31m全部执行完毕：\033[0m " + time.strftime('%H:%M:%S')
print(finally2)
driver.back()
driver.back()
