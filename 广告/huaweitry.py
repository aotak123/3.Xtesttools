# coding=utf-8

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.common.exceptions import NoSuchElementException
import time
import urllib.request
import ssl
import os

capabilities = {}
capabilities['platformName'] = 'Android'  # Android平台测试
capabilities['platformVersion'] = '8.0.0'
capabilities['deviceName'] = 'EVA-AL10'
capabilities['appPackage'] = 'com.kamitu.drawsth.standalone.free.android'  # 系统手机中的联系人app的包名
capabilities['appActivity'] = 'com.qsmy.busniess.welcome.WelcomeActivity'  # 系统手机中的联系人app的主入口activity
capabilities['noReset'] = 'true'  # 不重置app
capabilities['autoAcceptAlerts'] = 'true'
capabilities['autoWebview'] = 'false'
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', capabilities)  # 连接测试所在服务器
context = ssl._create_unverified_context()

'''
block list添加 https://sign.crazyccy.com:443/index/index
'''


########################################################################################################################
def panguan(mobile):
    time.sleep(3)
    print("\033[1;31mProject.\033[0m " + str(mobile) + " \033[1;31mSTART\033[0m : " + time.strftime('%H:%M:%S'))
    # 登录模块
    try:
        check_login = driver.find_element_by_id(
            "com.kamitu.drawsth.standalone.free.android:id/iv_mobile_login")  # 选择手机号登录
    except NoSuchElementException:
        print("当前为自动登录...退出账号")
        time.sleep(8)  # 等待加载进入首页
        TouchAction(driver).tap(x=422, y=120).perform()  # 返回进入个人中心
        time.sleep(2)
        TouchAction(driver).tap(x=960, y=186).perform()  # 点击设置
        time.sleep(2)
        TouchAction(driver).tap(x=492, y=1777).perform()  # 点击退出
        time.sleep(2)
        TouchAction(driver).tap(x=712, y=1014).perform()  # 弹窗确定退出
        time.sleep(3)
        print("退出账号成功...重新进入登录")
        TouchAction(driver).tap(x=391, y=1591).perform()  # 点击手机号登录
        time.sleep(1)
        # 选择手机号输入框
        edit_mobile = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/edit_phone")
        edit_mobile.send_keys(mobile)
        time.sleep(1)
        TouchAction(driver).tap(x=825, y=588).perform()  # 获取验证码
        time.sleep(2)
        # 获取验证码
        logincodeurl = "https://uc.crazyccy.com/login/main_login/testtool?key=sLQq2_jaKLknsqAwZ&type=1&mobile=" + str(
            mobile)
        request = urllib.request.Request(logincodeurl)  # 构建请求url
        response = urllib.request.urlopen(request, context=context)  # ssl证书免验证加入,context = context# 打开请求url链接
        num = response.read()  # 读取页面返回信息，python3返回数据为bytes类型的对象 (即b为前缀, bytes类型)
        logincode = num.decode()
        edit_code = driver.find_element_by_id(
            "com.kamitu.drawsth.standalone.free.android:id/edit_identifyCode")  # 选择验证码输入框
        time.sleep(1)
        edit_code.send_keys(logincode)
        time.sleep(1)
        TouchAction(driver).tap(x=530, y=844).perform()  # 确定按钮登录
        print("账号登录成功")
    else:
        TouchAction(driver).tap(x=391, y=1591).perform()  # 点击手机号登录
        time.sleep(1)
        # 选择手机号输入框
        edit_mobile = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/edit_phone")
        edit_mobile.send_keys(mobile)
        time.sleep(1)
        TouchAction(driver).tap(x=825, y=588).perform()  # 获取验证码
        time.sleep(2)
        # 获取验证码
        logincodeurl = "https://uc.crazyccy.com/login/main_login/testtool?key=sLQq2_jaKLknsqAwZ&type=1&mobile=" + str(
            mobile)
        request = urllib.request.Request(logincodeurl)  # 构建请求url
        response = urllib.request.urlopen(request, context=context)  # ssl证书免验证加入,context = context# 打开请求url链接
        num = response.read()  # 读取页面返回信息，python3返回数据为bytes类型的对象 (即b为前缀, bytes类型)
        logincode = num.decode()
        edit_code = driver.find_element_by_id(
            "com.kamitu.drawsth.standalone.free.android:id/edit_identifyCode")  # 选择验证码输入框
        time.sleep(1)
        edit_code.send_keys(logincode)
        time.sleep(1)
        TouchAction(driver).tap(x=530, y=844).perform()  # 确定按钮登录
        print("账号登录成功")
    time.sleep(10)  # 等待加载进入首页
    # 进入判官进行刷广告
    TouchAction(driver).tap(x=321, y=1665).perform()  # 选择进入判官
    time.sleep(3)
    TouchAction(driver).tap(x=546, y=941).perform()  # 选择开始挑战
    time.sleep(3)
    a = 1
    while a <= 11:
        time.sleep(8)
        TouchAction(driver).tap(x=503, y=1254).perform()  # 点击查看广告
        time.sleep(5)
        try:
            GDT = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
        except NoSuchElementException:
            BB = "  \033[1;31mNO.\033[0m " + str(a) + " toutiaosdk广告"
            print(BB)
            time.sleep(40)
            TouchAction(driver).tap(x=964, y=101).perform()  # 关闭toutiao广告
            # print("     toutiaosdk广告关闭")
        else:
            CC = "  \033[1;31mNO.\033[0m " + str(a) + " GDTsdk广告"
            print(CC)
            time.sleep(55)
            driver.back()  # GDTsdk广告按钮
            # print("     GDTsdk广告关闭")
        a += 1
    # 退出广告循环
    time.sleep(10)
    driver.back()  # 判官回到首页
    time.sleep(2)
    # 退出账号
    TouchAction(driver).tap(x=422, y=120).perform()  # 返回进入个人中心
    time.sleep(2)
    try:
        set = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/iv_setting")
    except NoSuchElementException:
        os.popen("adb shell am force-stop com.kamitu.drawsth.standalone.free.android")
        time.sleep(2)
        os.popen(
            "adb shell am start -n com.kamitu.drawsth.standalone.free.android/com.qsmy.busniess.welcome.WelcomeActivity")
        time.sleep(10)  # 等待加载进入首页
        TouchAction(driver).tap(x=422, y=120).perform()  # 返回进入个人中心
        time.sleep(2)
        TouchAction(driver).tap(x=960, y=186).perform()  # 点击设置
        time.sleep(2)
        TouchAction(driver).tap(x=492, y=1777).perform()  # 点击退出
        time.sleep(2)
        TouchAction(driver).tap(x=712, y=1014).perform()  # 弹窗确定退出
    else:
        TouchAction(driver).tap(x=960, y=186).perform()  # 点击设置
        time.sleep(2)
        TouchAction(driver).tap(x=492, y=1777).perform()  # 点击退出
        time.sleep(2)
        TouchAction(driver).tap(x=712, y=1014).perform()  # 弹窗确定退出


########################################################################################################################
if __name__ == '__main__':
    panguan(18321273743)
    panguan(18519820628)
    panguan(18575823673)
    panguan(18681025732)
    panguan(18819123459)
    panguan(18901156158)
    panguan(18920308799)
    panguan(18929597700)
    panguan(18930223547)  # 末凉
    panguan(19882152576)
    panguan(15895663333)
    panguan(13918122777)
    panguan(13223986738)
    panguan(17767380753)
    panguan(13200500500)
    panguan(13200500001)
    panguan(13079188626)
    panguan(17260878175)
    panguan(19813758251)
    panguan(17261803056)
    panguan(19529759329)
    panguan(17538519737)
    panguan(13529021576)
    panguan(18987872800)
    panguan(18917779999)
    panguan(13761113333)
    panguan(13985622222)
    panguan(13763333333)
    panguan(13698521470)
    panguan(13760000001)
    panguan(17729152205)
    panguan(14017700111)
    panguan(16016000001)

########################################################################################################################
finally2 = "\033[1;31m全部执行完毕：\033[0m " + time.strftime('%H:%M:%S')
print(finally2)
driver.back()
driver.back()