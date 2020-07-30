# coding=utf-8

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.common.exceptions import NoSuchElementException
import time
import urllib.request
import ssl

capabilities = {}
capabilities['platformName'] = 'Android'  # Android平台测试
# 三星
capabilities['platformVersion'] = '6.0.1'
capabilities['deviceName'] = 'SM-G9250'
capabilities['appPackage'] = 'com.kamitu.drawsth.standalone.free.android'  # 系统手机中的联系人app的包名
capabilities['appActivity'] = 'com.qsmy.busniess.welcome.WelcomeActivity'  # 系统手机中的联系人app的主入口activity
capabilities['noReset'] = 'true'  # 不重置app
capabilities['autoAcceptAlerts'] = 'true'
capabilities['autoWebview'] = 'false'
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', capabilities)  # 连接测试所在服务器
context = ssl._create_unverified_context()



#######################################################################################################################
mobile = "18017700223"
AA = "\033[1;31mNO.1\033[0m " + mobile + " \033[1;31m开始\033[0m"
print(AA)
nowtime = time.strftime('%Y-%m-%d% %H:%M:%S')
print(nowtime)
time.sleep(5)


def check_login():
    try:
        check_login = driver.find_element_by_id(
            "com.kamitu.drawsth.standalone.free.android:id/iv_mobile_login")  # 选择手机号登录
    except NoSuchElementException:
        print("自动登录成功")
    else:
        TouchAction(driver).tap(x=515, y=2300).perform()
        time.sleep(2)
        el2 = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/edit_phone")  # 选择手机号输入框
        el2.send_keys(mobile)
        time.sleep(2)
        TouchAction(driver).tap(x=1100, y=870).perform()  # 获取验证码
        time.sleep(2)
        # 获取验证码
        logincodeurl = "https://uc.crazyccy.com/login/main_login/testtool?key=sLQq2_jaKLknsqAwZ&type=1&mobile=" + mobile
        # print(logincodeurl)
        request = urllib.request.Request(logincodeurl)  # 构建请求url
        response = urllib.request.urlopen(request, context=context)  # ssl证书免验证加入,context = context# 打开请求url链接
        num = response.read()  # 读取页面返回信息，python3返回数据为bytes类型的对象 (即b为前缀, bytes类型)
        logincode = num.decode()
        if logincode == "查不到！":
            print("获取验证码失败")
            TouchAction(driver).tap(x=1100, y=870).perform()  # 获取验证码
        time.sleep(1)
        el4 = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/edit_identifyCode")  # 选择验证码输入框
        time.sleep(2)
        el4.send_keys(logincode)
        time.sleep(2)
        TouchAction(driver).tap(x=700, y=1200).perform()  # 确定按钮登录
        print("账号登录成功")


check_login()

time.sleep(15)  # 等待10秒加载进入首页


def check_signwindows():  # 检查用户签到弹窗
    try:
        check_signwindows = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/iv_signin_get")
    except NoSuchElementException:
        print("无签到弹窗")
    else:
        TouchAction(driver).tap(x=712, y=1884).perform()
        time.sleep(6)
        TouchAction(driver).tap(x=712, y=852).perform()
        time.sleep(6)
        try:
            GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
        except NoSuchElementException:
            print("toutiaosdk广告")
            time.sleep(40)
            TouchAction(driver).tap(x=1285, y=139).perform()  # 关闭toutiao广告
            print("toutiaosdk广告关闭")
            time.sleep(6)
            TouchAction(driver).tap(x=1254, y=671).perform()  # 关闭加分弹窗
        else:
            print("GDTsdk广告")
            time.sleep(55)
            driver.back()  # GDTsdk广告按钮
            print("GDTsdk广告关闭")
            time.sleep(6)
            TouchAction(driver).tap(x=1254, y=671).perform()  # 关闭加分弹窗


check_signwindows()
time.sleep(3)


def choujiang():
    time.sleep(3)
    TouchAction(driver).tap(x=1285, y=2354).perform()  # 进入抽奖页面
    time.sleep(2)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽10次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽9次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 看广告
    time.sleep(6)
    try:
        GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
    except NoSuchElementException:
        print("toutiaosdk广告")
        time.sleep(40)
        TouchAction(driver).tap(x=1285, y=139).perform()  # 关闭toutiao广告
        print("toutiaosdk广告关闭")
    else:
        print("GDTsdk广告")
        time.sleep(55)
        driver.back()  # GDTsdk广告按钮
        print("GDTsdk广告关闭")
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽8次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽7次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽6次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 看广告
    time.sleep(6)
    try:
        GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
    except NoSuchElementException:
        print("toutiaosdk广告")
        time.sleep(40)
        TouchAction(driver).tap(x=1285, y=139).perform()  # 关闭toutiao广告
        print("toutiaosdk广告关闭")
    else:
        print("GDTsdk广告")
        time.sleep(55)
        driver.back()  # GDTsdk广告按钮
        print("GDTsdk广告关闭")
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽5次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽4次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽3次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽2次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 看广告
    time.sleep(6)
    try:
        GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
    except NoSuchElementException:
        print("toutiaosdk广告")
        time.sleep(40)
        TouchAction(driver).tap(x=1285, y=139).perform()  # 关闭toutiao广告
        print("toutiaosdk广告关闭")
    else:
        print("GDTsdk广告")
        time.sleep(55)
        driver.back()  # GDTsdk广告按钮
        print("GDTsdk广告关闭")
    time.sleep(1)


choujiang()

time.sleep(3)
TouchAction(driver).tap(x=707, y=2070).perform()  # 进入接龙页面
time.sleep(3)
driver.back()
time.sleep(3)


def check_signtoast():  # 检查是否开启签到提示
    try:
        check_signtoast = driver.find_element_by_id(
            "com.kamitu.drawsth.standalone.free.android:id/iv_checkin_reminder_close")
    except NoSuchElementException:
        print("无签到提示")
    else:
        TouchAction(driver).tap(x=1228, y=748).perform()


check_signtoast()
time.sleep(3)


def kantu():
    TouchAction(driver).tap(x=175, y=2385).perform()  # 进入看图猜成语
    time.sleep(3)
    TouchAction(driver).tap(x=475, y=2280).perform()
    time.sleep(1)
    TouchAction(driver).tap(x=1105, y=2188).perform()
    time.sleep(1)
    TouchAction(driver).tap(x=800, y=2280).perform()  # 进入看图使用一次提示
    time.sleep(2)
    TouchAction(driver).tap(x=1000, y=1560).perform()  # 选择右侧提示广告
    driver.back()
    # 广告次数
    a = 6
    while a > 0:
        TouchAction(driver).tap(x=475, y=2280).perform()
        time.sleep(1)
        TouchAction(driver).tap(x=1105, y=2188).perform()
        time.sleep(1)
        TouchAction(driver).tap(x=800, y=2280).perform()  # 选择(位置)
        time.sleep(3)
        TouchAction(driver).tap(x=444, y=1560).perform()  # 选择左侧去除多余选项广告
        print(a)
        time.sleep(6)
        try:
            GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
        except NoSuchElementException:
            print("toutiaosdk广告")
            time.sleep(40)
            TouchAction(driver).tap(x=1285, y=139).perform()  # 关闭toutiao广告
            print("toutiaosdk广告关闭")
        else:
            print("GDTsdk广告")
            time.sleep(55)
            driver.back()  # GDTsdk广告按钮
            print("GDTsdk广告关闭")
        a -= 1
        time.sleep(2)
        TouchAction(driver).tap(x=1000, y=1560).perform()  # 选择右侧提示广告
        print(a)
        time.sleep(6)
        try:
            GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
        except NoSuchElementException:
            print("toutiaosdk广告")
            time.sleep(40)
            TouchAction(driver).tap(x=1285, y=139).perform()  # 关闭toutiao广告
            print("toutiaosdk广告关闭")
        else:
            print("GDTsdk广告")
            time.sleep(55)
            driver.back()  # GDTsdk广告按钮
            print("GDTsdk广告关闭")
        # print(a)
        time.sleep(2)
        driver.back()
        time.sleep(2)
        a -= 1


kantu()
driver.back()  # 返回首页
time.sleep(2)

TouchAction(driver).tap(x=588, y=186).perform()  # 返回进入个人中心
time.sleep(2)
TouchAction(driver).tap(x=1275, y=243).perform()
time.sleep(1)
TouchAction(driver).tap(x=707, y=2467).perform()
time.sleep(1)
TouchAction(driver).tap(x=960, y=1440).perform()
BB = mobile + " \033[1;31m账号退出成功\033[0m"
print(BB)
nowtime = time.strftime('%Y-%m-%d% %H:%M:%S')
print(nowtime)
#######################################################################################################################




mobile = "18017700475"
AA = "\033[1;31mNO.2\033[0m " + mobile + " \033[1;31m开始\033[0m"
print(AA)
nowtime = time.strftime('%Y-%m-%d% %H:%M:%S')
print(nowtime)
time.sleep(5)


def check_login():
    try:
        check_login = driver.find_element_by_id(
            "com.kamitu.drawsth.standalone.free.android:id/iv_mobile_login")  # 选择手机号登录
    except NoSuchElementException:
        print("自动登录成功")
    else:
        TouchAction(driver).tap(x=515, y=2300).perform()
        time.sleep(2)
        el2 = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/edit_phone")  # 选择手机号输入框
        el2.send_keys(mobile)
        time.sleep(2)
        TouchAction(driver).tap(x=1100, y=870).perform()  # 获取验证码
        time.sleep(2)
        # 获取验证码
        logincodeurl = "https://uc.crazyccy.com/login/main_login/testtool?key=sLQq2_jaKLknsqAwZ&type=1&mobile=" + mobile
        # print(logincodeurl)
        request = urllib.request.Request(logincodeurl)  # 构建请求url
        response = urllib.request.urlopen(request, context=context)  # ssl证书免验证加入,context = context# 打开请求url链接
        num = response.read()  # 读取页面返回信息，python3返回数据为bytes类型的对象 (即b为前缀, bytes类型)
        logincode = num.decode()
        if logincode == "查不到！":
            print("获取验证码失败")
            TouchAction(driver).tap(x=1100, y=870).perform()  # 获取验证码
        time.sleep(1)
        el4 = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/edit_identifyCode")  # 选择验证码输入框
        time.sleep(2)
        el4.send_keys(logincode)
        time.sleep(2)
        TouchAction(driver).tap(x=700, y=1200).perform()  # 确定按钮登录
        print("账号登录成功")


check_login()

time.sleep(15)  # 等待10秒加载进入首页


def check_signwindows():  # 检查用户签到弹窗
    try:
        check_signwindows = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/iv_signin_get")
    except NoSuchElementException:
        print("无签到弹窗")
    else:
        TouchAction(driver).tap(x=712, y=1884).perform()
        time.sleep(6)
        TouchAction(driver).tap(x=712, y=852).perform()
        time.sleep(6)
        try:
            GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
        except NoSuchElementException:
            print("toutiaosdk广告")
            time.sleep(40)
            TouchAction(driver).tap(x=1285, y=139).perform()  # 关闭toutiao广告
            print("toutiaosdk广告关闭")
            time.sleep(6)
            TouchAction(driver).tap(x=1254, y=671).perform()  # 关闭加分弹窗
        else:
            print("GDTsdk广告")
            time.sleep(55)
            driver.back()  # GDTsdk广告按钮
            print("GDTsdk广告关闭")
            time.sleep(6)
            TouchAction(driver).tap(x=1254, y=671).perform()  # 关闭加分弹窗


check_signwindows()
time.sleep(3)


def choujiang():
    time.sleep(3)
    TouchAction(driver).tap(x=1285, y=2354).perform()  # 进入抽奖页面
    time.sleep(2)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽10次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽9次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 看广告
    time.sleep(6)
    try:
        GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
    except NoSuchElementException:
        print("toutiaosdk广告")
        time.sleep(40)
        TouchAction(driver).tap(x=1285, y=139).perform()  # 关闭toutiao广告
        print("toutiaosdk广告关闭")
    else:
        print("GDTsdk广告")
        time.sleep(55)
        driver.back()  # GDTsdk广告按钮
        print("GDTsdk广告关闭")
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽8次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽7次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽6次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 看广告
    time.sleep(6)
    try:
        GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
    except NoSuchElementException:
        print("toutiaosdk广告")
        time.sleep(40)
        TouchAction(driver).tap(x=1285, y=139).perform()  # 关闭toutiao广告
        print("toutiaosdk广告关闭")
    else:
        print("GDTsdk广告")
        time.sleep(55)
        driver.back()  # GDTsdk广告按钮
        print("GDTsdk广告关闭")
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽5次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽4次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽3次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽2次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 看广告
    time.sleep(6)
    try:
        GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
    except NoSuchElementException:
        print("toutiaosdk广告")
        time.sleep(40)
        TouchAction(driver).tap(x=1285, y=139).perform()  # 关闭toutiao广告
        print("toutiaosdk广告关闭")
    else:
        print("GDTsdk广告")
        time.sleep(55)
        driver.back()  # GDTsdk广告按钮
        print("GDTsdk广告关闭")
    time.sleep(1)


choujiang()

time.sleep(3)
TouchAction(driver).tap(x=707, y=2070).perform()  # 进入接龙页面
time.sleep(3)
driver.back()
time.sleep(3)


def check_signtoast():  # 检查是否开启签到提示
    try:
        check_signtoast = driver.find_element_by_id(
            "com.kamitu.drawsth.standalone.free.android:id/iv_checkin_reminder_close")
    except NoSuchElementException:
        print("无签到提示")
    else:
        TouchAction(driver).tap(x=1228, y=748).perform()


check_signtoast()
time.sleep(3)


def kantu():
    TouchAction(driver).tap(x=175, y=2385).perform()  # 进入看图猜成语
    time.sleep(3)
    TouchAction(driver).tap(x=475, y=2280).perform()
    time.sleep(1)
    TouchAction(driver).tap(x=1105, y=2188).perform()
    time.sleep(1)
    TouchAction(driver).tap(x=800, y=2280).perform()  # 进入看图使用一次提示
    time.sleep(2)
    TouchAction(driver).tap(x=1000, y=1560).perform()  # 选择右侧提示广告
    driver.back()
    # 广告次数
    a = 6
    while a > 0:
        TouchAction(driver).tap(x=475, y=2280).perform()
        time.sleep(1)
        TouchAction(driver).tap(x=1105, y=2188).perform()
        time.sleep(1)
        TouchAction(driver).tap(x=800, y=2280).perform()  # 选择(位置)
        time.sleep(3)
        TouchAction(driver).tap(x=444, y=1560).perform()  # 选择左侧去除多余选项广告
        print(a)
        time.sleep(6)
        try:
            GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
        except NoSuchElementException:
            print("toutiaosdk广告")
            time.sleep(40)
            TouchAction(driver).tap(x=1285, y=139).perform()  # 关闭toutiao广告
            print("toutiaosdk广告关闭")
        else:
            print("GDTsdk广告")
            time.sleep(55)
            driver.back()  # GDTsdk广告按钮
            print("GDTsdk广告关闭")
        a -= 1
        time.sleep(2)
        TouchAction(driver).tap(x=1000, y=1560).perform()  # 选择右侧提示广告
        print(a)
        time.sleep(6)
        try:
            GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
        except NoSuchElementException:
            print("toutiaosdk广告")
            time.sleep(40)
            TouchAction(driver).tap(x=1285, y=139).perform()  # 关闭toutiao广告
            print("toutiaosdk广告关闭")
        else:
            print("GDTsdk广告")
            time.sleep(55)
            driver.back()  # GDTsdk广告按钮
            print("GDTsdk广告关闭")
        # print(a)
        time.sleep(2)
        driver.back()
        time.sleep(2)
        a -= 1


kantu()
driver.back()  # 返回首页
time.sleep(2)

TouchAction(driver).tap(x=588, y=186).perform()  # 返回进入个人中心
time.sleep(2)
TouchAction(driver).tap(x=1275, y=243).perform()
time.sleep(1)
TouchAction(driver).tap(x=707, y=2467).perform()
time.sleep(1)
TouchAction(driver).tap(x=960, y=1440).perform()
BB = mobile + " \033[1;31m账号退出成功\033[0m"
print(BB)
#######################################################################################################################


mobile = "18017700515"
AA = "\033[1;31mNO.3\033[0m " + mobile + " \033[1;31m开始\033[0m"
print(AA)
nowtime = time.strftime('%Y-%m-%d% %H:%M:%S')
print(nowtime)
time.sleep(5)


def check_login():
    try:
        check_login = driver.find_element_by_id(
            "com.kamitu.drawsth.standalone.free.android:id/iv_mobile_login")  # 选择手机号登录
    except NoSuchElementException:
        print("自动登录成功")
    else:
        TouchAction(driver).tap(x=515, y=2300).perform()
        time.sleep(2)
        el2 = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/edit_phone")  # 选择手机号输入框
        el2.send_keys(mobile)
        time.sleep(2)
        TouchAction(driver).tap(x=1100, y=870).perform()  # 获取验证码
        time.sleep(2)
        # 获取验证码
        logincodeurl = "https://uc.crazyccy.com/login/main_login/testtool?key=sLQq2_jaKLknsqAwZ&type=1&mobile=" + mobile
        # print(logincodeurl)
        request = urllib.request.Request(logincodeurl)  # 构建请求url
        response = urllib.request.urlopen(request, context=context)  # ssl证书免验证加入,context = context# 打开请求url链接
        num = response.read()  # 读取页面返回信息，python3返回数据为bytes类型的对象 (即b为前缀, bytes类型)
        logincode = num.decode()
        if logincode == "查不到！":
            print("获取验证码失败")
            TouchAction(driver).tap(x=1100, y=870).perform()  # 获取验证码
        time.sleep(1)
        el4 = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/edit_identifyCode")  # 选择验证码输入框
        time.sleep(2)
        el4.send_keys(logincode)
        time.sleep(2)
        TouchAction(driver).tap(x=700, y=1200).perform()  # 确定按钮登录
        print("账号登录成功")


check_login()

time.sleep(15)  # 等待10秒加载进入首页


def check_signwindows():  # 检查用户签到弹窗
    try:
        check_signwindows = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/iv_signin_get")
    except NoSuchElementException:
        print("无签到弹窗")
    else:
        TouchAction(driver).tap(x=712, y=1884).perform()
        time.sleep(6)
        TouchAction(driver).tap(x=712, y=852).perform()
        time.sleep(6)
        try:
            GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
        except NoSuchElementException:
            print("toutiaosdk广告")
            time.sleep(40)
            TouchAction(driver).tap(x=1285, y=139).perform()  # 关闭toutiao广告
            print("toutiaosdk广告关闭")
            time.sleep(6)
            TouchAction(driver).tap(x=1254, y=671).perform()  # 关闭加分弹窗
        else:
            print("GDTsdk广告")
            time.sleep(55)
            driver.back()  # GDTsdk广告按钮
            print("GDTsdk广告关闭")
            time.sleep(6)
            TouchAction(driver).tap(x=1254, y=671).perform()  # 关闭加分弹窗


check_signwindows()
time.sleep(3)


def choujiang():
    time.sleep(3)
    TouchAction(driver).tap(x=1285, y=2354).perform()  # 进入抽奖页面
    time.sleep(2)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽10次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽9次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 看广告
    time.sleep(6)
    try:
        GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
    except NoSuchElementException:
        print("toutiaosdk广告")
        time.sleep(40)
        TouchAction(driver).tap(x=1285, y=139).perform()  # 关闭toutiao广告
        print("toutiaosdk广告关闭")
    else:
        print("GDTsdk广告")
        time.sleep(55)
        driver.back()  # GDTsdk广告按钮
        print("GDTsdk广告关闭")
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽8次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽7次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽6次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 看广告
    time.sleep(6)
    try:
        GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
    except NoSuchElementException:
        print("toutiaosdk广告")
        time.sleep(40)
        TouchAction(driver).tap(x=1285, y=139).perform()  # 关闭toutiao广告
        print("toutiaosdk广告关闭")
    else:
        print("GDTsdk广告")
        time.sleep(55)
        driver.back()  # GDTsdk广告按钮
        print("GDTsdk广告关闭")
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽5次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽4次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽3次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽2次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 看广告
    time.sleep(6)
    try:
        GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
    except NoSuchElementException:
        print("toutiaosdk广告")
        time.sleep(40)
        TouchAction(driver).tap(x=1285, y=139).perform()  # 关闭toutiao广告
        print("toutiaosdk广告关闭")
    else:
        print("GDTsdk广告")
        time.sleep(55)
        driver.back()  # GDTsdk广告按钮
        print("GDTsdk广告关闭")
    time.sleep(1)


choujiang()

time.sleep(3)
TouchAction(driver).tap(x=707, y=2070).perform()  # 进入接龙页面
time.sleep(3)
driver.back()
time.sleep(3)


def check_signtoast():  # 检查是否开启签到提示
    try:
        check_signtoast = driver.find_element_by_id(
            "com.kamitu.drawsth.standalone.free.android:id/iv_checkin_reminder_close")
    except NoSuchElementException:
        print("无签到提示")
    else:
        TouchAction(driver).tap(x=1228, y=748).perform()


check_signtoast()
time.sleep(3)


def kantu():
    TouchAction(driver).tap(x=175, y=2385).perform()  # 进入看图猜成语
    time.sleep(3)
    TouchAction(driver).tap(x=475, y=2280).perform()
    time.sleep(1)
    TouchAction(driver).tap(x=1105, y=2188).perform()
    time.sleep(1)
    TouchAction(driver).tap(x=800, y=2280).perform()  # 进入看图使用一次提示
    time.sleep(2)
    TouchAction(driver).tap(x=1000, y=1560).perform()  # 选择右侧提示广告
    driver.back()
    # 广告次数
    a = 6
    while a > 0:
        TouchAction(driver).tap(x=475, y=2280).perform()
        time.sleep(1)
        TouchAction(driver).tap(x=1105, y=2188).perform()
        time.sleep(1)
        TouchAction(driver).tap(x=800, y=2280).perform()  # 选择(位置)
        time.sleep(3)
        TouchAction(driver).tap(x=444, y=1560).perform()  # 选择左侧去除多余选项广告
        print(a)
        time.sleep(6)
        try:
            GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
        except NoSuchElementException:
            print("toutiaosdk广告")
            time.sleep(40)
            TouchAction(driver).tap(x=1285, y=139).perform()  # 关闭toutiao广告
            print("toutiaosdk广告关闭")
        else:
            print("GDTsdk广告")
            time.sleep(55)
            driver.back()  # GDTsdk广告按钮
            print("GDTsdk广告关闭")
        a -= 1
        time.sleep(2)
        TouchAction(driver).tap(x=1000, y=1560).perform()  # 选择右侧提示广告
        print(a)
        time.sleep(6)
        try:
            GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
        except NoSuchElementException:
            print("toutiaosdk广告")
            time.sleep(40)
            TouchAction(driver).tap(x=1285, y=139).perform()  # 关闭toutiao广告
            print("toutiaosdk广告关闭")
        else:
            print("GDTsdk广告")
            time.sleep(55)
            driver.back()  # GDTsdk广告按钮
            print("GDTsdk广告关闭")
        # print(a)
        time.sleep(2)
        driver.back()
        time.sleep(2)
        a -= 1


kantu()
driver.back()  # 返回首页
time.sleep(2)

TouchAction(driver).tap(x=588, y=186).perform()  # 返回进入个人中心
time.sleep(2)
TouchAction(driver).tap(x=1275, y=243).perform()
time.sleep(1)
TouchAction(driver).tap(x=707, y=2467).perform()
time.sleep(1)
TouchAction(driver).tap(x=960, y=1440).perform()
BB = mobile + " \033[1;31m账号退出成功\033[0m"
print(BB)
#######################################################################################################################


mobile = "18017700516"
AA = "\033[1;31mNO.4\033[0m " + mobile + " \033[1;31m开始\033[0m"
print(AA)
nowtime = time.strftime('%Y-%m-%d% %H:%M:%S')
print(nowtime)
time.sleep(5)


def check_login():
    try:
        check_login = driver.find_element_by_id(
            "com.kamitu.drawsth.standalone.free.android:id/iv_mobile_login")  # 选择手机号登录
    except NoSuchElementException:
        print("自动登录成功")
    else:
        TouchAction(driver).tap(x=515, y=2300).perform()
        time.sleep(2)
        el2 = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/edit_phone")  # 选择手机号输入框
        el2.send_keys(mobile)
        time.sleep(2)
        TouchAction(driver).tap(x=1100, y=870).perform()  # 获取验证码
        time.sleep(2)
        # 获取验证码
        logincodeurl = "https://uc.crazyccy.com/login/main_login/testtool?key=sLQq2_jaKLknsqAwZ&type=1&mobile=" + mobile
        # print(logincodeurl)
        request = urllib.request.Request(logincodeurl)  # 构建请求url
        response = urllib.request.urlopen(request, context=context)  # ssl证书免验证加入,context = context# 打开请求url链接
        num = response.read()  # 读取页面返回信息，python3返回数据为bytes类型的对象 (即b为前缀, bytes类型)
        logincode = num.decode()
        if logincode == "查不到！":
            print("获取验证码失败")
            TouchAction(driver).tap(x=1100, y=870).perform()  # 获取验证码
        time.sleep(1)
        el4 = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/edit_identifyCode")  # 选择验证码输入框
        time.sleep(2)
        el4.send_keys(logincode)
        time.sleep(2)
        TouchAction(driver).tap(x=700, y=1200).perform()  # 确定按钮登录
        print("账号登录成功")


check_login()

time.sleep(15)  # 等待10秒加载进入首页


def check_signwindows():  # 检查用户签到弹窗
    try:
        check_signwindows = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/iv_signin_get")
    except NoSuchElementException:
        print("无签到弹窗")
    else:
        TouchAction(driver).tap(x=712, y=1884).perform()
        time.sleep(6)
        TouchAction(driver).tap(x=712, y=852).perform()
        time.sleep(6)
        try:
            GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
        except NoSuchElementException:
            print("toutiaosdk广告")
            time.sleep(40)
            TouchAction(driver).tap(x=1285, y=139).perform()  # 关闭toutiao广告
            print("toutiaosdk广告关闭")
            time.sleep(6)
            TouchAction(driver).tap(x=1254, y=671).perform()  # 关闭加分弹窗
        else:
            print("GDTsdk广告")
            time.sleep(55)
            driver.back()  # GDTsdk广告按钮
            print("GDTsdk广告关闭")
            time.sleep(6)
            TouchAction(driver).tap(x=1254, y=671).perform()  # 关闭加分弹窗


check_signwindows()
time.sleep(3)


def choujiang():
    time.sleep(3)
    TouchAction(driver).tap(x=1285, y=2354).perform()  # 进入抽奖页面
    time.sleep(2)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽10次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽9次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 看广告
    time.sleep(6)
    try:
        GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
    except NoSuchElementException:
        print("toutiaosdk广告")
        time.sleep(40)
        TouchAction(driver).tap(x=1285, y=139).perform()  # 关闭toutiao广告
        print("toutiaosdk广告关闭")
    else:
        print("GDTsdk广告")
        time.sleep(55)
        driver.back()  # GDTsdk广告按钮
        print("GDTsdk广告关闭")
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽8次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽7次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽6次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 看广告
    time.sleep(6)
    try:
        GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
    except NoSuchElementException:
        print("toutiaosdk广告")
        time.sleep(40)
        TouchAction(driver).tap(x=1285, y=139).perform()  # 关闭toutiao广告
        print("toutiaosdk广告关闭")
    else:
        print("GDTsdk广告")
        time.sleep(55)
        driver.back()  # GDTsdk广告按钮
        print("GDTsdk广告关闭")
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽5次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽4次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽3次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽2次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 看广告
    time.sleep(6)
    try:
        GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
    except NoSuchElementException:
        print("toutiaosdk广告")
        time.sleep(40)
        TouchAction(driver).tap(x=1285, y=139).perform()  # 关闭toutiao广告
        print("toutiaosdk广告关闭")
    else:
        print("GDTsdk广告")
        time.sleep(55)
        driver.back()  # GDTsdk广告按钮
        print("GDTsdk广告关闭")
    time.sleep(1)


choujiang()

time.sleep(3)
TouchAction(driver).tap(x=707, y=2070).perform()  # 进入接龙页面
time.sleep(3)
driver.back()
time.sleep(3)


def check_signtoast():  # 检查是否开启签到提示
    try:
        check_signtoast = driver.find_element_by_id(
            "com.kamitu.drawsth.standalone.free.android:id/iv_checkin_reminder_close")
    except NoSuchElementException:
        print("无签到提示")
    else:
        TouchAction(driver).tap(x=1228, y=748).perform()


check_signtoast()
time.sleep(3)


def kantu():
    TouchAction(driver).tap(x=175, y=2385).perform()  # 进入看图猜成语
    time.sleep(3)
    TouchAction(driver).tap(x=475, y=2280).perform()
    time.sleep(1)
    TouchAction(driver).tap(x=1105, y=2188).perform()
    time.sleep(1)
    TouchAction(driver).tap(x=800, y=2280).perform()  # 进入看图使用一次提示
    time.sleep(2)
    TouchAction(driver).tap(x=1000, y=1560).perform()  # 选择右侧提示广告
    driver.back()
    # 广告次数
    a = 6
    while a > 0:
        TouchAction(driver).tap(x=475, y=2280).perform()
        time.sleep(1)
        TouchAction(driver).tap(x=1105, y=2188).perform()
        time.sleep(1)
        TouchAction(driver).tap(x=800, y=2280).perform()  # 选择(位置)
        time.sleep(3)
        TouchAction(driver).tap(x=444, y=1560).perform()  # 选择左侧去除多余选项广告
        print(a)
        time.sleep(6)
        try:
            GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
        except NoSuchElementException:
            print("toutiaosdk广告")
            time.sleep(40)
            TouchAction(driver).tap(x=1285, y=139).perform()  # 关闭toutiao广告
            print("toutiaosdk广告关闭")
        else:
            print("GDTsdk广告")
            time.sleep(55)
            driver.back()  # GDTsdk广告按钮
            print("GDTsdk广告关闭")
        a -= 1
        time.sleep(2)
        TouchAction(driver).tap(x=1000, y=1560).perform()  # 选择右侧提示广告
        print(a)
        time.sleep(6)
        try:
            GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
        except NoSuchElementException:
            print("toutiaosdk广告")
            time.sleep(40)
            TouchAction(driver).tap(x=1285, y=139).perform()  # 关闭toutiao广告
            print("toutiaosdk广告关闭")
        else:
            print("GDTsdk广告")
            time.sleep(55)
            driver.back()  # GDTsdk广告按钮
            print("GDTsdk广告关闭")
        # print(a)
        time.sleep(2)
        driver.back()
        time.sleep(2)
        a -= 1


kantu()
driver.back()  # 返回首页
time.sleep(2)

TouchAction(driver).tap(x=588, y=186).perform()  # 返回进入个人中心
time.sleep(2)
TouchAction(driver).tap(x=1275, y=243).perform()
time.sleep(1)
TouchAction(driver).tap(x=707, y=2467).perform()
time.sleep(1)
TouchAction(driver).tap(x=960, y=1440).perform()
BB = mobile + " \033[1;31m账号退出成功\033[0m"
print(BB)
#######################################################################################################################


mobile = "18017700526"
AA = "\033[1;31mNO.5\033[0m " + mobile + " \033[1;31m开始\033[0m"
print(AA)
nowtime = time.strftime('%Y-%m-%d% %H:%M:%S')
print(nowtime)
time.sleep(5)


def check_login():
    try:
        check_login = driver.find_element_by_id(
            "com.kamitu.drawsth.standalone.free.android:id/iv_mobile_login")  # 选择手机号登录
    except NoSuchElementException:
        print("自动登录成功")
    else:
        TouchAction(driver).tap(x=515, y=2300).perform()
        time.sleep(2)
        el2 = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/edit_phone")  # 选择手机号输入框
        el2.send_keys(mobile)
        time.sleep(2)
        TouchAction(driver).tap(x=1100, y=870).perform()  # 获取验证码
        time.sleep(2)
        # 获取验证码
        logincodeurl = "https://uc.crazyccy.com/login/main_login/testtool?key=sLQq2_jaKLknsqAwZ&type=1&mobile=" + mobile
        # print(logincodeurl)
        request = urllib.request.Request(logincodeurl)  # 构建请求url
        response = urllib.request.urlopen(request, context=context)  # ssl证书免验证加入,context = context# 打开请求url链接
        num = response.read()  # 读取页面返回信息，python3返回数据为bytes类型的对象 (即b为前缀, bytes类型)
        logincode = num.decode()
        if logincode == "查不到！":
            print("获取验证码失败")
            TouchAction(driver).tap(x=1100, y=870).perform()  # 获取验证码
        time.sleep(1)
        el4 = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/edit_identifyCode")  # 选择验证码输入框
        time.sleep(2)
        el4.send_keys(logincode)
        time.sleep(2)
        TouchAction(driver).tap(x=700, y=1200).perform()  # 确定按钮登录
        print("账号登录成功")


check_login()

time.sleep(15)  # 等待10秒加载进入首页


def check_signwindows():  # 检查用户签到弹窗
    try:
        check_signwindows = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/iv_signin_get")
    except NoSuchElementException:
        print("无签到弹窗")
    else:
        TouchAction(driver).tap(x=712, y=1884).perform()
        time.sleep(6)
        TouchAction(driver).tap(x=712, y=852).perform()
        time.sleep(6)
        try:
            GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
        except NoSuchElementException:
            print("toutiaosdk广告")
            time.sleep(40)
            TouchAction(driver).tap(x=1285, y=139).perform()  # 关闭toutiao广告
            print("toutiaosdk广告关闭")
            time.sleep(6)
            TouchAction(driver).tap(x=1254, y=671).perform()  # 关闭加分弹窗
        else:
            print("GDTsdk广告")
            time.sleep(55)
            driver.back()  # GDTsdk广告按钮
            print("GDTsdk广告关闭")
            time.sleep(6)
            TouchAction(driver).tap(x=1254, y=671).perform()  # 关闭加分弹窗


check_signwindows()
time.sleep(3)


def choujiang():
    time.sleep(3)
    TouchAction(driver).tap(x=1285, y=2354).perform()  # 进入抽奖页面
    time.sleep(2)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽10次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽9次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 看广告
    time.sleep(6)
    try:
        GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
    except NoSuchElementException:
        print("toutiaosdk广告")
        time.sleep(40)
        TouchAction(driver).tap(x=1285, y=139).perform()  # 关闭toutiao广告
        print("toutiaosdk广告关闭")
    else:
        print("GDTsdk广告")
        time.sleep(55)
        driver.back()  # GDTsdk广告按钮
        print("GDTsdk广告关闭")
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽8次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽7次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽6次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 看广告
    time.sleep(6)
    try:
        GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
    except NoSuchElementException:
        print("toutiaosdk广告")
        time.sleep(40)
        TouchAction(driver).tap(x=1285, y=139).perform()  # 关闭toutiao广告
        print("toutiaosdk广告关闭")
    else:
        print("GDTsdk广告")
        time.sleep(55)
        driver.back()  # GDTsdk广告按钮
        print("GDTsdk广告关闭")
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽5次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽4次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽3次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽2次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 看广告
    time.sleep(6)
    try:
        GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
    except NoSuchElementException:
        print("toutiaosdk广告")
        time.sleep(40)
        TouchAction(driver).tap(x=1285, y=139).perform()  # 关闭toutiao广告
        print("toutiaosdk广告关闭")
    else:
        print("GDTsdk广告")
        time.sleep(55)
        driver.back()  # GDTsdk广告按钮
        print("GDTsdk广告关闭")
    time.sleep(1)


choujiang()

time.sleep(3)
TouchAction(driver).tap(x=707, y=2070).perform()  # 进入接龙页面
time.sleep(3)
driver.back()
time.sleep(3)


def check_signtoast():  # 检查是否开启签到提示
    try:
        check_signtoast = driver.find_element_by_id(
            "com.kamitu.drawsth.standalone.free.android:id/iv_checkin_reminder_close")
    except NoSuchElementException:
        print("无签到提示")
    else:
        TouchAction(driver).tap(x=1228, y=748).perform()


check_signtoast()
time.sleep(3)


def kantu():
    TouchAction(driver).tap(x=175, y=2385).perform()  # 进入看图猜成语
    time.sleep(3)
    TouchAction(driver).tap(x=475, y=2280).perform()
    time.sleep(1)
    TouchAction(driver).tap(x=1105, y=2188).perform()
    time.sleep(1)
    TouchAction(driver).tap(x=800, y=2280).perform()  # 进入看图使用一次提示
    time.sleep(2)
    TouchAction(driver).tap(x=1000, y=1560).perform()  # 选择右侧提示广告
    driver.back()
    # 广告次数
    a = 6
    while a > 0:
        TouchAction(driver).tap(x=475, y=2280).perform()
        time.sleep(1)
        TouchAction(driver).tap(x=1105, y=2188).perform()
        time.sleep(1)
        TouchAction(driver).tap(x=800, y=2280).perform()  # 选择(位置)
        time.sleep(3)
        TouchAction(driver).tap(x=444, y=1560).perform()  # 选择左侧去除多余选项广告
        print(a)
        time.sleep(6)
        try:
            GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
        except NoSuchElementException:
            print("toutiaosdk广告")
            time.sleep(40)
            TouchAction(driver).tap(x=1285, y=139).perform()  # 关闭toutiao广告
            print("toutiaosdk广告关闭")
        else:
            print("GDTsdk广告")
            time.sleep(55)
            driver.back()  # GDTsdk广告按钮
            print("GDTsdk广告关闭")
        a -= 1
        time.sleep(2)
        TouchAction(driver).tap(x=1000, y=1560).perform()  # 选择右侧提示广告
        print(a)
        time.sleep(6)
        try:
            GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
        except NoSuchElementException:
            print("toutiaosdk广告")
            time.sleep(40)
            TouchAction(driver).tap(x=1285, y=139).perform()  # 关闭toutiao广告
            print("toutiaosdk广告关闭")
        else:
            print("GDTsdk广告")
            time.sleep(55)
            driver.back()  # GDTsdk广告按钮
            print("GDTsdk广告关闭")
        # print(a)
        time.sleep(2)
        driver.back()
        time.sleep(2)
        a -= 1


kantu()
driver.back()  # 返回首页
time.sleep(2)

TouchAction(driver).tap(x=588, y=186).perform()  # 返回进入个人中心
time.sleep(2)
TouchAction(driver).tap(x=1275, y=243).perform()
time.sleep(1)
TouchAction(driver).tap(x=707, y=2467).perform()
time.sleep(1)
TouchAction(driver).tap(x=960, y=1440).perform()
BB = mobile + " \033[1;31m账号退出成功\033[0m"
print(BB)
#######################################################################################################################


mobile = "18017700533"
AA = "\033[1;31mNO.6\033[0m " + mobile + " \033[1;31m开始\033[0m"
print(AA)
nowtime = time.strftime('%Y-%m-%d% %H:%M:%S')
print(nowtime)
time.sleep(5)


def check_login():
    try:
        check_login = driver.find_element_by_id(
            "com.kamitu.drawsth.standalone.free.android:id/iv_mobile_login")  # 选择手机号登录
    except NoSuchElementException:
        print("自动登录成功")
    else:
        TouchAction(driver).tap(x=515, y=2300).perform()
        time.sleep(2)
        el2 = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/edit_phone")  # 选择手机号输入框
        el2.send_keys(mobile)
        time.sleep(2)
        TouchAction(driver).tap(x=1100, y=870).perform()  # 获取验证码
        time.sleep(2)
        # 获取验证码
        logincodeurl = "https://uc.crazyccy.com/login/main_login/testtool?key=sLQq2_jaKLknsqAwZ&type=1&mobile=" + mobile
        # print(logincodeurl)
        request = urllib.request.Request(logincodeurl)  # 构建请求url
        response = urllib.request.urlopen(request, context=context)  # ssl证书免验证加入,context = context# 打开请求url链接
        num = response.read()  # 读取页面返回信息，python3返回数据为bytes类型的对象 (即b为前缀, bytes类型)
        logincode = num.decode()
        if logincode == "查不到！":
            print("获取验证码失败")
            TouchAction(driver).tap(x=1100, y=870).perform()  # 获取验证码
        time.sleep(1)
        el4 = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/edit_identifyCode")  # 选择验证码输入框
        time.sleep(2)
        el4.send_keys(logincode)
        time.sleep(2)
        TouchAction(driver).tap(x=700, y=1200).perform()  # 确定按钮登录
        print("账号登录成功")


check_login()

time.sleep(15)  # 等待10秒加载进入首页


def check_signwindows():  # 检查用户签到弹窗
    try:
        check_signwindows = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/iv_signin_get")
    except NoSuchElementException:
        print("无签到弹窗")
    else:
        TouchAction(driver).tap(x=712, y=1884).perform()
        time.sleep(6)
        TouchAction(driver).tap(x=712, y=852).perform()
        time.sleep(6)
        try:
            GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
        except NoSuchElementException:
            print("toutiaosdk广告")
            time.sleep(40)
            TouchAction(driver).tap(x=1285, y=139).perform()  # 关闭toutiao广告
            print("toutiaosdk广告关闭")
            time.sleep(6)
            TouchAction(driver).tap(x=1254, y=671).perform()  # 关闭加分弹窗
        else:
            print("GDTsdk广告")
            time.sleep(55)
            driver.back()  # GDTsdk广告按钮
            print("GDTsdk广告关闭")
            time.sleep(6)
            TouchAction(driver).tap(x=1254, y=671).perform()  # 关闭加分弹窗


check_signwindows()
time.sleep(3)


def choujiang():
    time.sleep(3)
    TouchAction(driver).tap(x=1285, y=2354).perform()  # 进入抽奖页面
    time.sleep(2)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽10次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽9次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 看广告
    time.sleep(6)
    try:
        GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
    except NoSuchElementException:
        print("toutiaosdk广告")
        time.sleep(40)
        TouchAction(driver).tap(x=1285, y=139).perform()  # 关闭toutiao广告
        print("toutiaosdk广告关闭")
    else:
        print("GDTsdk广告")
        time.sleep(55)
        driver.back()  # GDTsdk广告按钮
        print("GDTsdk广告关闭")
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽8次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽7次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽6次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 看广告
    time.sleep(6)
    try:
        GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
    except NoSuchElementException:
        print("toutiaosdk广告")
        time.sleep(40)
        TouchAction(driver).tap(x=1285, y=139).perform()  # 关闭toutiao广告
        print("toutiaosdk广告关闭")
    else:
        print("GDTsdk广告")
        time.sleep(55)
        driver.back()  # GDTsdk广告按钮
        print("GDTsdk广告关闭")
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽5次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽4次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽3次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽2次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 看广告
    time.sleep(6)
    try:
        GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
    except NoSuchElementException:
        print("toutiaosdk广告")
        time.sleep(40)
        TouchAction(driver).tap(x=1285, y=139).perform()  # 关闭toutiao广告
        print("toutiaosdk广告关闭")
    else:
        print("GDTsdk广告")
        time.sleep(55)
        driver.back()  # GDTsdk广告按钮
        print("GDTsdk广告关闭")
    time.sleep(1)


choujiang()

time.sleep(3)
TouchAction(driver).tap(x=707, y=2070).perform()  # 进入接龙页面
time.sleep(3)
driver.back()
time.sleep(3)


def check_signtoast():  # 检查是否开启签到提示
    try:
        check_signtoast = driver.find_element_by_id(
            "com.kamitu.drawsth.standalone.free.android:id/iv_checkin_reminder_close")
    except NoSuchElementException:
        print("无签到提示")
    else:
        TouchAction(driver).tap(x=1228, y=748).perform()


check_signtoast()
time.sleep(3)


def kantu():
    TouchAction(driver).tap(x=175, y=2385).perform()  # 进入看图猜成语
    time.sleep(3)
    TouchAction(driver).tap(x=475, y=2280).perform()
    time.sleep(1)
    TouchAction(driver).tap(x=1105, y=2188).perform()
    time.sleep(1)
    TouchAction(driver).tap(x=800, y=2280).perform()  # 进入看图使用一次提示
    time.sleep(2)
    TouchAction(driver).tap(x=1000, y=1560).perform()  # 选择右侧提示广告
    driver.back()
    # 广告次数
    a = 6
    while a > 0:
        TouchAction(driver).tap(x=475, y=2280).perform()
        time.sleep(1)
        TouchAction(driver).tap(x=1105, y=2188).perform()
        time.sleep(1)
        TouchAction(driver).tap(x=800, y=2280).perform()  # 选择(位置)
        time.sleep(3)
        TouchAction(driver).tap(x=444, y=1560).perform()  # 选择左侧去除多余选项广告
        print(a)
        time.sleep(6)
        try:
            GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
        except NoSuchElementException:
            print("toutiaosdk广告")
            time.sleep(40)
            TouchAction(driver).tap(x=1285, y=139).perform()  # 关闭toutiao广告
            print("toutiaosdk广告关闭")
        else:
            print("GDTsdk广告")
            time.sleep(55)
            driver.back()  # GDTsdk广告按钮
            print("GDTsdk广告关闭")
        a -= 1
        time.sleep(2)
        TouchAction(driver).tap(x=1000, y=1560).perform()  # 选择右侧提示广告
        print(a)
        time.sleep(6)
        try:
            GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
        except NoSuchElementException:
            print("toutiaosdk广告")
            time.sleep(40)
            TouchAction(driver).tap(x=1285, y=139).perform()  # 关闭toutiao广告
            print("toutiaosdk广告关闭")
        else:
            print("GDTsdk广告")
            time.sleep(55)
            driver.back()  # GDTsdk广告按钮
            print("GDTsdk广告关闭")
        # print(a)
        time.sleep(2)
        driver.back()
        time.sleep(2)
        a -= 1


kantu()
driver.back()  # 返回首页
time.sleep(2)

TouchAction(driver).tap(x=588, y=186).perform()  # 返回进入个人中心
time.sleep(2)
TouchAction(driver).tap(x=1275, y=243).perform()
time.sleep(1)
TouchAction(driver).tap(x=707, y=2467).perform()
time.sleep(1)
TouchAction(driver).tap(x=960, y=1440).perform()
BB = mobile + " \033[1;31m账号退出成功\033[0m"
print(BB)
#######################################################################################################################


mobile = "18017700535"
AA = "\033[1;31mNO.7\033[0m " + mobile + " \033[1;31m开始\033[0m"
print(AA)
nowtime = time.strftime('%Y-%m-%d% %H:%M:%S')
print(nowtime)
time.sleep(5)


def check_login():
    try:
        check_login = driver.find_element_by_id(
            "com.kamitu.drawsth.standalone.free.android:id/iv_mobile_login")  # 选择手机号登录
    except NoSuchElementException:
        print("自动登录成功")
    else:
        TouchAction(driver).tap(x=515, y=2300).perform()
        time.sleep(2)
        el2 = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/edit_phone")  # 选择手机号输入框
        el2.send_keys(mobile)
        time.sleep(2)
        TouchAction(driver).tap(x=1100, y=870).perform()  # 获取验证码
        time.sleep(2)
        # 获取验证码
        logincodeurl = "https://uc.crazyccy.com/login/main_login/testtool?key=sLQq2_jaKLknsqAwZ&type=1&mobile=" + mobile
        # print(logincodeurl)
        request = urllib.request.Request(logincodeurl)  # 构建请求url
        response = urllib.request.urlopen(request, context=context)  # ssl证书免验证加入,context = context# 打开请求url链接
        num = response.read()  # 读取页面返回信息，python3返回数据为bytes类型的对象 (即b为前缀, bytes类型)
        logincode = num.decode()
        if logincode == "查不到！":
            print("获取验证码失败")
            TouchAction(driver).tap(x=1100, y=870).perform()  # 获取验证码
        time.sleep(1)
        el4 = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/edit_identifyCode")  # 选择验证码输入框
        time.sleep(2)
        el4.send_keys(logincode)
        time.sleep(2)
        TouchAction(driver).tap(x=700, y=1200).perform()  # 确定按钮登录
        print("账号登录成功")


check_login()

time.sleep(15)  # 等待10秒加载进入首页


def check_signwindows():  # 检查用户签到弹窗
    try:
        check_signwindows = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/iv_signin_get")
    except NoSuchElementException:
        print("无签到弹窗")
    else:
        TouchAction(driver).tap(x=712, y=1884).perform()
        time.sleep(6)
        TouchAction(driver).tap(x=712, y=852).perform()
        time.sleep(6)
        try:
            GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
        except NoSuchElementException:
            print("toutiaosdk广告")
            time.sleep(40)
            TouchAction(driver).tap(x=1285, y=139).perform()  # 关闭toutiao广告
            print("toutiaosdk广告关闭")
            time.sleep(6)
            TouchAction(driver).tap(x=1254, y=671).perform()  # 关闭加分弹窗
        else:
            print("GDTsdk广告")
            time.sleep(55)
            driver.back()  # GDTsdk广告按钮
            print("GDTsdk广告关闭")
            time.sleep(6)
            TouchAction(driver).tap(x=1254, y=671).perform()  # 关闭加分弹窗


check_signwindows()
time.sleep(3)


def choujiang():
    time.sleep(3)
    TouchAction(driver).tap(x=1285, y=2354).perform()  # 进入抽奖页面
    time.sleep(2)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽10次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽9次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 看广告
    time.sleep(6)
    try:
        GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
    except NoSuchElementException:
        print("toutiaosdk广告")
        time.sleep(40)
        TouchAction(driver).tap(x=1285, y=139).perform()  # 关闭toutiao广告
        print("toutiaosdk广告关闭")
    else:
        print("GDTsdk广告")
        time.sleep(55)
        driver.back()  # GDTsdk广告按钮
        print("GDTsdk广告关闭")
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽8次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽7次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽6次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 看广告
    time.sleep(6)
    try:
        GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
    except NoSuchElementException:
        print("toutiaosdk广告")
        time.sleep(40)
        TouchAction(driver).tap(x=1285, y=139).perform()  # 关闭toutiao广告
        print("toutiaosdk广告关闭")
    else:
        print("GDTsdk广告")
        time.sleep(55)
        driver.back()  # GDTsdk广告按钮
        print("GDTsdk广告关闭")
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽5次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽4次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽3次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽2次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 看广告
    time.sleep(6)
    try:
        GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
    except NoSuchElementException:
        print("toutiaosdk广告")
        time.sleep(40)
        TouchAction(driver).tap(x=1285, y=139).perform()  # 关闭toutiao广告
        print("toutiaosdk广告关闭")
    else:
        print("GDTsdk广告")
        time.sleep(55)
        driver.back()  # GDTsdk广告按钮
        print("GDTsdk广告关闭")
    time.sleep(1)


choujiang()

time.sleep(3)
TouchAction(driver).tap(x=707, y=2070).perform()  # 进入接龙页面
time.sleep(3)
driver.back()
time.sleep(3)


def check_signtoast():  # 检查是否开启签到提示
    try:
        check_signtoast = driver.find_element_by_id(
            "com.kamitu.drawsth.standalone.free.android:id/iv_checkin_reminder_close")
    except NoSuchElementException:
        print("无签到提示")
    else:
        TouchAction(driver).tap(x=1228, y=748).perform()


check_signtoast()
time.sleep(3)


def kantu():
    TouchAction(driver).tap(x=175, y=2385).perform()  # 进入看图猜成语
    time.sleep(3)
    TouchAction(driver).tap(x=475, y=2280).perform()
    time.sleep(1)
    TouchAction(driver).tap(x=1105, y=2188).perform()
    time.sleep(1)
    TouchAction(driver).tap(x=800, y=2280).perform()  # 进入看图使用一次提示
    time.sleep(2)
    TouchAction(driver).tap(x=1000, y=1560).perform()  # 选择右侧提示广告
    driver.back()
    # 广告次数
    a = 6
    while a > 0:
        TouchAction(driver).tap(x=475, y=2280).perform()
        time.sleep(1)
        TouchAction(driver).tap(x=1105, y=2188).perform()
        time.sleep(1)
        TouchAction(driver).tap(x=800, y=2280).perform()  # 选择(位置)
        time.sleep(3)
        TouchAction(driver).tap(x=444, y=1560).perform()  # 选择左侧去除多余选项广告
        print(a)
        time.sleep(6)
        try:
            GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
        except NoSuchElementException:
            print("toutiaosdk广告")
            time.sleep(40)
            TouchAction(driver).tap(x=1285, y=139).perform()  # 关闭toutiao广告
            print("toutiaosdk广告关闭")
        else:
            print("GDTsdk广告")
            time.sleep(55)
            driver.back()  # GDTsdk广告按钮
            print("GDTsdk广告关闭")
        a -= 1
        time.sleep(2)
        TouchAction(driver).tap(x=1000, y=1560).perform()  # 选择右侧提示广告
        print(a)
        time.sleep(6)
        try:
            GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
        except NoSuchElementException:
            print("toutiaosdk广告")
            time.sleep(40)
            TouchAction(driver).tap(x=1285, y=139).perform()  # 关闭toutiao广告
            print("toutiaosdk广告关闭")
        else:
            print("GDTsdk广告")
            time.sleep(55)
            driver.back()  # GDTsdk广告按钮
            print("GDTsdk广告关闭")
        # print(a)
        time.sleep(2)
        driver.back()
        time.sleep(2)
        a -= 1


kantu()
driver.back()  # 返回首页
time.sleep(2)

TouchAction(driver).tap(x=588, y=186).perform()  # 返回进入个人中心
time.sleep(2)
TouchAction(driver).tap(x=1275, y=243).perform()
time.sleep(1)
TouchAction(driver).tap(x=707, y=2467).perform()
time.sleep(1)
TouchAction(driver).tap(x=960, y=1440).perform()
BB = mobile + " \033[1;31m账号退出成功\033[0m"
print(BB)
#######################################################################################################################


mobile = "18017700536"
AA = "\033[1;31mNO.8\033[0m " + mobile + " \033[1;31m开始\033[0m"
print(AA)
nowtime = time.strftime('%Y-%m-%d% %H:%M:%S')
print(nowtime)
time.sleep(5)


def check_login():
    try:
        check_login = driver.find_element_by_id(
            "com.kamitu.drawsth.standalone.free.android:id/iv_mobile_login")  # 选择手机号登录
    except NoSuchElementException:
        print("自动登录成功")
    else:
        TouchAction(driver).tap(x=515, y=2300).perform()
        time.sleep(2)
        el2 = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/edit_phone")  # 选择手机号输入框
        el2.send_keys(mobile)
        time.sleep(2)
        TouchAction(driver).tap(x=1100, y=870).perform()  # 获取验证码
        time.sleep(2)
        # 获取验证码
        logincodeurl = "https://uc.crazyccy.com/login/main_login/testtool?key=sLQq2_jaKLknsqAwZ&type=1&mobile=" + mobile
        # print(logincodeurl)
        request = urllib.request.Request(logincodeurl)  # 构建请求url
        response = urllib.request.urlopen(request, context=context)  # ssl证书免验证加入,context = context# 打开请求url链接
        num = response.read()  # 读取页面返回信息，python3返回数据为bytes类型的对象 (即b为前缀, bytes类型)
        logincode = num.decode()
        if logincode == "查不到！":
            print("获取验证码失败")
            TouchAction(driver).tap(x=1100, y=870).perform()  # 获取验证码
        time.sleep(1)
        el4 = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/edit_identifyCode")  # 选择验证码输入框
        time.sleep(2)
        el4.send_keys(logincode)
        time.sleep(2)
        TouchAction(driver).tap(x=700, y=1200).perform()  # 确定按钮登录
        print("账号登录成功")


check_login()

time.sleep(15)  # 等待10秒加载进入首页


def check_signwindows():  # 检查用户签到弹窗
    try:
        check_signwindows = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/iv_signin_get")
    except NoSuchElementException:
        print("无签到弹窗")
    else:
        TouchAction(driver).tap(x=712, y=1884).perform()
        time.sleep(6)
        TouchAction(driver).tap(x=712, y=852).perform()
        time.sleep(6)
        try:
            GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
        except NoSuchElementException:
            print("toutiaosdk广告")
            time.sleep(40)
            TouchAction(driver).tap(x=1285, y=139).perform()  # 关闭toutiao广告
            print("toutiaosdk广告关闭")
            time.sleep(6)
            TouchAction(driver).tap(x=1254, y=671).perform()  # 关闭加分弹窗
        else:
            print("GDTsdk广告")
            time.sleep(55)
            driver.back()  # GDTsdk广告按钮
            print("GDTsdk广告关闭")
            time.sleep(6)
            TouchAction(driver).tap(x=1254, y=671).perform()  # 关闭加分弹窗


check_signwindows()
time.sleep(3)


def choujiang():
    time.sleep(3)
    TouchAction(driver).tap(x=1285, y=2354).perform()  # 进入抽奖页面
    time.sleep(2)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽10次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽9次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 看广告
    time.sleep(6)
    try:
        GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
    except NoSuchElementException:
        print("toutiaosdk广告")
        time.sleep(40)
        TouchAction(driver).tap(x=1285, y=139).perform()  # 关闭toutiao广告
        print("toutiaosdk广告关闭")
    else:
        print("GDTsdk广告")
        time.sleep(55)
        driver.back()  # GDTsdk广告按钮
        print("GDTsdk广告关闭")
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽8次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽7次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽6次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 看广告
    time.sleep(6)
    try:
        GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
    except NoSuchElementException:
        print("toutiaosdk广告")
        time.sleep(40)
        TouchAction(driver).tap(x=1285, y=139).perform()  # 关闭toutiao广告
        print("toutiaosdk广告关闭")
    else:
        print("GDTsdk广告")
        time.sleep(55)
        driver.back()  # GDTsdk广告按钮
        print("GDTsdk广告关闭")
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽5次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽4次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽3次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽2次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 看广告
    time.sleep(6)
    try:
        GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
    except NoSuchElementException:
        print("toutiaosdk广告")
        time.sleep(40)
        TouchAction(driver).tap(x=1285, y=139).perform()  # 关闭toutiao广告
        print("toutiaosdk广告关闭")
    else:
        print("GDTsdk广告")
        time.sleep(55)
        driver.back()  # GDTsdk广告按钮
        print("GDTsdk广告关闭")
    time.sleep(1)


choujiang()

time.sleep(3)
TouchAction(driver).tap(x=707, y=2070).perform()  # 进入接龙页面
time.sleep(3)
driver.back()
time.sleep(3)


def check_signtoast():  # 检查是否开启签到提示
    try:
        check_signtoast = driver.find_element_by_id(
            "com.kamitu.drawsth.standalone.free.android:id/iv_checkin_reminder_close")
    except NoSuchElementException:
        print("无签到提示")
    else:
        TouchAction(driver).tap(x=1228, y=748).perform()


check_signtoast()
time.sleep(3)


def kantu():
    TouchAction(driver).tap(x=175, y=2385).perform()  # 进入看图猜成语
    time.sleep(3)
    TouchAction(driver).tap(x=475, y=2280).perform()
    time.sleep(1)
    TouchAction(driver).tap(x=1105, y=2188).perform()
    time.sleep(1)
    TouchAction(driver).tap(x=800, y=2280).perform()  # 进入看图使用一次提示
    time.sleep(2)
    TouchAction(driver).tap(x=1000, y=1560).perform()  # 选择右侧提示广告
    driver.back()
    # 广告次数
    a = 6
    while a > 0:
        TouchAction(driver).tap(x=475, y=2280).perform()
        time.sleep(1)
        TouchAction(driver).tap(x=1105, y=2188).perform()
        time.sleep(1)
        TouchAction(driver).tap(x=800, y=2280).perform()  # 选择(位置)
        time.sleep(3)
        TouchAction(driver).tap(x=444, y=1560).perform()  # 选择左侧去除多余选项广告
        print(a)
        time.sleep(6)
        try:
            GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
        except NoSuchElementException:
            print("toutiaosdk广告")
            time.sleep(40)
            TouchAction(driver).tap(x=1285, y=139).perform()  # 关闭toutiao广告
            print("toutiaosdk广告关闭")
        else:
            print("GDTsdk广告")
            time.sleep(55)
            driver.back()  # GDTsdk广告按钮
            print("GDTsdk广告关闭")
        a -= 1
        time.sleep(2)
        TouchAction(driver).tap(x=1000, y=1560).perform()  # 选择右侧提示广告
        print(a)
        time.sleep(6)
        try:
            GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
        except NoSuchElementException:
            print("toutiaosdk广告")
            time.sleep(40)
            TouchAction(driver).tap(x=1285, y=139).perform()  # 关闭toutiao广告
            print("toutiaosdk广告关闭")
        else:
            print("GDTsdk广告")
            time.sleep(55)
            driver.back()  # GDTsdk广告按钮
            print("GDTsdk广告关闭")
        # print(a)
        time.sleep(2)
        driver.back()
        time.sleep(2)
        a -= 1


kantu()
driver.back()  # 返回首页
time.sleep(2)

TouchAction(driver).tap(x=588, y=186).perform()  # 返回进入个人中心
time.sleep(2)
TouchAction(driver).tap(x=1275, y=243).perform()
time.sleep(1)
TouchAction(driver).tap(x=707, y=2467).perform()
time.sleep(1)
TouchAction(driver).tap(x=960, y=1440).perform()
BB = mobile + " \033[1;31m账号退出成功\033[0m"
print(BB)
#######################################################################################################################


mobile = "18017700537"
AA = "\033[1;31mNO.9\033[0m " + mobile + " \033[1;31m开始\033[0m"
print(AA)
nowtime = time.strftime('%Y-%m-%d% %H:%M:%S')
print(nowtime)
time.sleep(5)


def check_login():
    try:
        check_login = driver.find_element_by_id(
            "com.kamitu.drawsth.standalone.free.android:id/iv_mobile_login")  # 选择手机号登录
    except NoSuchElementException:
        print("自动登录成功")
    else:
        TouchAction(driver).tap(x=515, y=2300).perform()
        time.sleep(2)
        el2 = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/edit_phone")  # 选择手机号输入框
        el2.send_keys(mobile)
        time.sleep(2)
        TouchAction(driver).tap(x=1100, y=870).perform()  # 获取验证码
        time.sleep(2)
        # 获取验证码
        logincodeurl = "https://uc.crazyccy.com/login/main_login/testtool?key=sLQq2_jaKLknsqAwZ&type=1&mobile=" + mobile
        # print(logincodeurl)
        request = urllib.request.Request(logincodeurl)  # 构建请求url
        response = urllib.request.urlopen(request, context=context)  # ssl证书免验证加入,context = context# 打开请求url链接
        num = response.read()  # 读取页面返回信息，python3返回数据为bytes类型的对象 (即b为前缀, bytes类型)
        logincode = num.decode()
        if logincode == "查不到！":
            print("获取验证码失败")
            TouchAction(driver).tap(x=1100, y=870).perform()  # 获取验证码
        time.sleep(1)
        el4 = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/edit_identifyCode")  # 选择验证码输入框
        time.sleep(2)
        el4.send_keys(logincode)
        time.sleep(2)
        TouchAction(driver).tap(x=700, y=1200).perform()  # 确定按钮登录
        print("账号登录成功")


check_login()

time.sleep(15)  # 等待10秒加载进入首页


def check_signwindows():  # 检查用户签到弹窗
    try:
        check_signwindows = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/iv_signin_get")
    except NoSuchElementException:
        print("无签到弹窗")
    else:
        TouchAction(driver).tap(x=712, y=1884).perform()
        time.sleep(6)
        TouchAction(driver).tap(x=712, y=852).perform()
        time.sleep(6)
        try:
            GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
        except NoSuchElementException:
            print("toutiaosdk广告")
            time.sleep(40)
            TouchAction(driver).tap(x=1285, y=139).perform()  # 关闭toutiao广告
            print("toutiaosdk广告关闭")
            time.sleep(6)
            TouchAction(driver).tap(x=1254, y=671).perform()  # 关闭加分弹窗
        else:
            print("GDTsdk广告")
            time.sleep(55)
            driver.back()  # GDTsdk广告按钮
            print("GDTsdk广告关闭")
            time.sleep(6)
            TouchAction(driver).tap(x=1254, y=671).perform()  # 关闭加分弹窗


check_signwindows()
time.sleep(3)


def choujiang():
    time.sleep(3)
    TouchAction(driver).tap(x=1285, y=2354).perform()  # 进入抽奖页面
    time.sleep(2)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽10次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽9次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 看广告
    time.sleep(6)
    try:
        GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
    except NoSuchElementException:
        print("toutiaosdk广告")
        time.sleep(40)
        TouchAction(driver).tap(x=1285, y=139).perform()  # 关闭toutiao广告
        print("toutiaosdk广告关闭")
    else:
        print("GDTsdk广告")
        time.sleep(55)
        driver.back()  # GDTsdk广告按钮
        print("GDTsdk广告关闭")
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽8次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽7次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽6次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 看广告
    time.sleep(6)
    try:
        GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
    except NoSuchElementException:
        print("toutiaosdk广告")
        time.sleep(40)
        TouchAction(driver).tap(x=1285, y=139).perform()  # 关闭toutiao广告
        print("toutiaosdk广告关闭")
    else:
        print("GDTsdk广告")
        time.sleep(55)
        driver.back()  # GDTsdk广告按钮
        print("GDTsdk广告关闭")
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽5次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽4次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽3次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽2次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 看广告
    time.sleep(6)
    try:
        GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
    except NoSuchElementException:
        print("toutiaosdk广告")
        time.sleep(40)
        TouchAction(driver).tap(x=1285, y=139).perform()  # 关闭toutiao广告
        print("toutiaosdk广告关闭")
    else:
        print("GDTsdk广告")
        time.sleep(55)
        driver.back()  # GDTsdk广告按钮
        print("GDTsdk广告关闭")
    time.sleep(1)


choujiang()

time.sleep(3)
TouchAction(driver).tap(x=707, y=2070).perform()  # 进入接龙页面
time.sleep(3)
driver.back()
time.sleep(3)


def check_signtoast():  # 检查是否开启签到提示
    try:
        check_signtoast = driver.find_element_by_id(
            "com.kamitu.drawsth.standalone.free.android:id/iv_checkin_reminder_close")
    except NoSuchElementException:
        print("无签到提示")
    else:
        TouchAction(driver).tap(x=1228, y=748).perform()


check_signtoast()
time.sleep(3)


def kantu():
    TouchAction(driver).tap(x=175, y=2385).perform()  # 进入看图猜成语
    time.sleep(3)
    TouchAction(driver).tap(x=475, y=2280).perform()
    time.sleep(1)
    TouchAction(driver).tap(x=1105, y=2188).perform()
    time.sleep(1)
    TouchAction(driver).tap(x=800, y=2280).perform()  # 进入看图使用一次提示
    time.sleep(2)
    TouchAction(driver).tap(x=1000, y=1560).perform()  # 选择右侧提示广告
    driver.back()
    # 广告次数
    a = 6
    while a > 0:
        TouchAction(driver).tap(x=475, y=2280).perform()
        time.sleep(1)
        TouchAction(driver).tap(x=1105, y=2188).perform()
        time.sleep(1)
        TouchAction(driver).tap(x=800, y=2280).perform()  # 选择(位置)
        time.sleep(3)
        TouchAction(driver).tap(x=444, y=1560).perform()  # 选择左侧去除多余选项广告
        print(a)
        time.sleep(6)
        try:
            GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
        except NoSuchElementException:
            print("toutiaosdk广告")
            time.sleep(40)
            TouchAction(driver).tap(x=1285, y=139).perform()  # 关闭toutiao广告
            print("toutiaosdk广告关闭")
        else:
            print("GDTsdk广告")
            time.sleep(55)
            driver.back()  # GDTsdk广告按钮
            print("GDTsdk广告关闭")
        a -= 1
        time.sleep(2)
        TouchAction(driver).tap(x=1000, y=1560).perform()  # 选择右侧提示广告
        print(a)
        time.sleep(6)
        try:
            GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
        except NoSuchElementException:
            print("toutiaosdk广告")
            time.sleep(40)
            TouchAction(driver).tap(x=1285, y=139).perform()  # 关闭toutiao广告
            print("toutiaosdk广告关闭")
        else:
            print("GDTsdk广告")
            time.sleep(55)
            driver.back()  # GDTsdk广告按钮
            print("GDTsdk广告关闭")
        # print(a)
        time.sleep(2)
        driver.back()
        time.sleep(2)
        a -= 1


kantu()
driver.back()  # 返回首页
time.sleep(2)

TouchAction(driver).tap(x=588, y=186).perform()  # 返回进入个人中心
time.sleep(2)
TouchAction(driver).tap(x=1275, y=243).perform()
time.sleep(1)
TouchAction(driver).tap(x=707, y=2467).perform()
time.sleep(1)
TouchAction(driver).tap(x=960, y=1440).perform()
BB = mobile + " \033[1;31m账号退出成功\033[0m"
print(BB)
#######################################################################################################################


mobile = "18017700550"
AA = "\033[1;31mNO.10\033[0m " + mobile + " \033[1;31m开始\033[0m"
print(AA)
nowtime = time.strftime('%Y-%m-%d% %H:%M:%S')
print(nowtime)
time.sleep(5)


def check_login():
    try:
        check_login = driver.find_element_by_id(
            "com.kamitu.drawsth.standalone.free.android:id/iv_mobile_login")  # 选择手机号登录
    except NoSuchElementException:
        print("自动登录成功")
    else:
        TouchAction(driver).tap(x=515, y=2300).perform()
        time.sleep(2)
        el2 = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/edit_phone")  # 选择手机号输入框
        el2.send_keys(mobile)
        time.sleep(2)
        TouchAction(driver).tap(x=1100, y=870).perform()  # 获取验证码
        time.sleep(2)
        # 获取验证码
        logincodeurl = "https://uc.crazyccy.com/login/main_login/testtool?key=sLQq2_jaKLknsqAwZ&type=1&mobile=" + mobile
        # print(logincodeurl)
        request = urllib.request.Request(logincodeurl)  # 构建请求url
        response = urllib.request.urlopen(request, context=context)  # ssl证书免验证加入,context = context# 打开请求url链接
        num = response.read()  # 读取页面返回信息，python3返回数据为bytes类型的对象 (即b为前缀, bytes类型)
        logincode = num.decode()
        if logincode == "查不到！":
            print("获取验证码失败")
            TouchAction(driver).tap(x=1100, y=870).perform()  # 获取验证码
        time.sleep(1)
        el4 = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/edit_identifyCode")  # 选择验证码输入框
        time.sleep(2)
        el4.send_keys(logincode)
        time.sleep(2)
        TouchAction(driver).tap(x=700, y=1200).perform()  # 确定按钮登录
        print("账号登录成功")


check_login()

time.sleep(15)  # 等待10秒加载进入首页


def check_signwindows():  # 检查用户签到弹窗
    try:
        check_signwindows = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/iv_signin_get")
    except NoSuchElementException:
        print("无签到弹窗")
    else:
        TouchAction(driver).tap(x=712, y=1884).perform()
        time.sleep(6)
        TouchAction(driver).tap(x=712, y=852).perform()
        time.sleep(6)
        try:
            GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
        except NoSuchElementException:
            print("toutiaosdk广告")
            time.sleep(40)
            TouchAction(driver).tap(x=1285, y=139).perform()  # 关闭toutiao广告
            print("toutiaosdk广告关闭")
            time.sleep(6)
            TouchAction(driver).tap(x=1254, y=671).perform()  # 关闭加分弹窗
        else:
            print("GDTsdk广告")
            time.sleep(55)
            driver.back()  # GDTsdk广告按钮
            print("GDTsdk广告关闭")
            time.sleep(6)
            TouchAction(driver).tap(x=1254, y=671).perform()  # 关闭加分弹窗


check_signwindows()
time.sleep(3)


def choujiang():
    time.sleep(3)
    TouchAction(driver).tap(x=1285, y=2354).perform()  # 进入抽奖页面
    time.sleep(2)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽10次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽9次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 看广告
    time.sleep(6)
    try:
        GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
    except NoSuchElementException:
        print("toutiaosdk广告")
        time.sleep(40)
        TouchAction(driver).tap(x=1285, y=139).perform()  # 关闭toutiao广告
        print("toutiaosdk广告关闭")
    else:
        print("GDTsdk广告")
        time.sleep(55)
        driver.back()  # GDTsdk广告按钮
        print("GDTsdk广告关闭")
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽8次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽7次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽6次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 看广告
    time.sleep(6)
    try:
        GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
    except NoSuchElementException:
        print("toutiaosdk广告")
        time.sleep(40)
        TouchAction(driver).tap(x=1285, y=139).perform()  # 关闭toutiao广告
        print("toutiaosdk广告关闭")
    else:
        print("GDTsdk广告")
        time.sleep(55)
        driver.back()  # GDTsdk广告按钮
        print("GDTsdk广告关闭")
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽5次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽4次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽3次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽2次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 看广告
    time.sleep(6)
    try:
        GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
    except NoSuchElementException:
        print("toutiaosdk广告")
        time.sleep(40)
        TouchAction(driver).tap(x=1285, y=139).perform()  # 关闭toutiao广告
        print("toutiaosdk广告关闭")
    else:
        print("GDTsdk广告")
        time.sleep(55)
        driver.back()  # GDTsdk广告按钮
        print("GDTsdk广告关闭")
    time.sleep(1)


choujiang()

time.sleep(3)
TouchAction(driver).tap(x=707, y=2070).perform()  # 进入接龙页面
time.sleep(3)
driver.back()
time.sleep(3)


def check_signtoast():  # 检查是否开启签到提示
    try:
        check_signtoast = driver.find_element_by_id(
            "com.kamitu.drawsth.standalone.free.android:id/iv_checkin_reminder_close")
    except NoSuchElementException:
        print("无签到提示")
    else:
        TouchAction(driver).tap(x=1228, y=748).perform()


check_signtoast()
time.sleep(3)


def kantu():
    TouchAction(driver).tap(x=175, y=2385).perform()  # 进入看图猜成语
    time.sleep(3)
    TouchAction(driver).tap(x=475, y=2280).perform()
    time.sleep(1)
    TouchAction(driver).tap(x=1105, y=2188).perform()
    time.sleep(1)
    TouchAction(driver).tap(x=800, y=2280).perform()  # 进入看图使用一次提示
    time.sleep(2)
    TouchAction(driver).tap(x=1000, y=1560).perform()  # 选择右侧提示广告
    driver.back()
    # 广告次数
    a = 6
    while a > 0:
        TouchAction(driver).tap(x=475, y=2280).perform()
        time.sleep(1)
        TouchAction(driver).tap(x=1105, y=2188).perform()
        time.sleep(1)
        TouchAction(driver).tap(x=800, y=2280).perform()  # 选择(位置)
        time.sleep(3)
        TouchAction(driver).tap(x=444, y=1560).perform()  # 选择左侧去除多余选项广告
        print(a)
        time.sleep(6)
        try:
            GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
        except NoSuchElementException:
            print("toutiaosdk广告")
            time.sleep(40)
            TouchAction(driver).tap(x=1285, y=139).perform()  # 关闭toutiao广告
            print("toutiaosdk广告关闭")
        else:
            print("GDTsdk广告")
            time.sleep(55)
            driver.back()  # GDTsdk广告按钮
            print("GDTsdk广告关闭")
        a -= 1
        time.sleep(2)
        TouchAction(driver).tap(x=1000, y=1560).perform()  # 选择右侧提示广告
        print(a)
        time.sleep(6)
        try:
            GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
        except NoSuchElementException:
            print("toutiaosdk广告")
            time.sleep(40)
            TouchAction(driver).tap(x=1285, y=139).perform()  # 关闭toutiao广告
            print("toutiaosdk广告关闭")
        else:
            print("GDTsdk广告")
            time.sleep(55)
            driver.back()  # GDTsdk广告按钮
            print("GDTsdk广告关闭")
        # print(a)
        time.sleep(2)
        driver.back()
        time.sleep(2)
        a -= 1


kantu()
driver.back()  # 返回首页
time.sleep(2)

TouchAction(driver).tap(x=588, y=186).perform()  # 返回进入个人中心
time.sleep(2)
TouchAction(driver).tap(x=1275, y=243).perform()
time.sleep(1)
TouchAction(driver).tap(x=707, y=2467).perform()
time.sleep(1)
TouchAction(driver).tap(x=960, y=1440).perform()
BB = mobile + " \033[1;31m账号退出成功\033[0m"
print(BB)
#######################################################################################################################


mobile = "18017700596"
AA = "\033[1;31mNO.11\033[0m " + mobile + " \033[1;31m开始\033[0m"
print(AA)
nowtime = time.strftime('%Y-%m-%d% %H:%M:%S')
print(nowtime)
time.sleep(5)


def check_login():
    try:
        check_login = driver.find_element_by_id(
            "com.kamitu.drawsth.standalone.free.android:id/iv_mobile_login")  # 选择手机号登录
    except NoSuchElementException:
        print("自动登录成功")
    else:
        TouchAction(driver).tap(x=515, y=2300).perform()
        time.sleep(2)
        el2 = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/edit_phone")  # 选择手机号输入框
        el2.send_keys(mobile)
        time.sleep(2)
        TouchAction(driver).tap(x=1100, y=870).perform()  # 获取验证码
        time.sleep(2)
        # 获取验证码
        logincodeurl = "https://uc.crazyccy.com/login/main_login/testtool?key=sLQq2_jaKLknsqAwZ&type=1&mobile=" + mobile
        # print(logincodeurl)
        request = urllib.request.Request(logincodeurl)  # 构建请求url
        response = urllib.request.urlopen(request, context=context)  # ssl证书免验证加入,context = context# 打开请求url链接
        num = response.read()  # 读取页面返回信息，python3返回数据为bytes类型的对象 (即b为前缀, bytes类型)
        logincode = num.decode()
        if logincode == "查不到！":
            print("获取验证码失败")
            TouchAction(driver).tap(x=1100, y=870).perform()  # 获取验证码
        time.sleep(1)
        el4 = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/edit_identifyCode")  # 选择验证码输入框
        time.sleep(2)
        el4.send_keys(logincode)
        time.sleep(2)
        TouchAction(driver).tap(x=700, y=1200).perform()  # 确定按钮登录
        print("账号登录成功")


check_login()

time.sleep(15)  # 等待10秒加载进入首页


def check_signwindows():  # 检查用户签到弹窗
    try:
        check_signwindows = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/iv_signin_get")
    except NoSuchElementException:
        print("无签到弹窗")
    else:
        TouchAction(driver).tap(x=712, y=1884).perform()
        time.sleep(6)
        TouchAction(driver).tap(x=712, y=852).perform()
        time.sleep(6)
        try:
            GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
        except NoSuchElementException:
            print("toutiaosdk广告")
            time.sleep(40)
            TouchAction(driver).tap(x=1285, y=139).perform()  # 关闭toutiao广告
            print("toutiaosdk广告关闭")
            time.sleep(6)
            TouchAction(driver).tap(x=1254, y=671).perform()  # 关闭加分弹窗
        else:
            print("GDTsdk广告")
            time.sleep(55)
            driver.back()  # GDTsdk广告按钮
            print("GDTsdk广告关闭")
            time.sleep(6)
            TouchAction(driver).tap(x=1254, y=671).perform()  # 关闭加分弹窗


check_signwindows()
time.sleep(3)


def choujiang():
    time.sleep(3)
    TouchAction(driver).tap(x=1285, y=2354).perform()  # 进入抽奖页面
    time.sleep(2)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽10次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽9次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 看广告
    time.sleep(6)
    try:
        GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
    except NoSuchElementException:
        print("toutiaosdk广告")
        time.sleep(40)
        TouchAction(driver).tap(x=1285, y=139).perform()  # 关闭toutiao广告
        print("toutiaosdk广告关闭")
    else:
        print("GDTsdk广告")
        time.sleep(55)
        driver.back()  # GDTsdk广告按钮
        print("GDTsdk广告关闭")
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽8次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽7次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽6次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 看广告
    time.sleep(6)
    try:
        GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
    except NoSuchElementException:
        print("toutiaosdk广告")
        time.sleep(40)
        TouchAction(driver).tap(x=1285, y=139).perform()  # 关闭toutiao广告
        print("toutiaosdk广告关闭")
    else:
        print("GDTsdk广告")
        time.sleep(55)
        driver.back()  # GDTsdk广告按钮
        print("GDTsdk广告关闭")
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽5次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽4次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽3次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽2次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 看广告
    time.sleep(6)
    try:
        GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
    except NoSuchElementException:
        print("toutiaosdk广告")
        time.sleep(40)
        TouchAction(driver).tap(x=1285, y=139).perform()  # 关闭toutiao广告
        print("toutiaosdk广告关闭")
    else:
        print("GDTsdk广告")
        time.sleep(55)
        driver.back()  # GDTsdk广告按钮
        print("GDTsdk广告关闭")
    time.sleep(1)


choujiang()

time.sleep(3)
TouchAction(driver).tap(x=707, y=2070).perform()  # 进入接龙页面
time.sleep(3)
driver.back()
time.sleep(3)


def check_signtoast():  # 检查是否开启签到提示
    try:
        check_signtoast = driver.find_element_by_id(
            "com.kamitu.drawsth.standalone.free.android:id/iv_checkin_reminder_close")
    except NoSuchElementException:
        print("无签到提示")
    else:
        TouchAction(driver).tap(x=1228, y=748).perform()


check_signtoast()
time.sleep(3)


def kantu():
    TouchAction(driver).tap(x=175, y=2385).perform()  # 进入看图猜成语
    time.sleep(3)
    TouchAction(driver).tap(x=475, y=2280).perform()
    time.sleep(1)
    TouchAction(driver).tap(x=1105, y=2188).perform()
    time.sleep(1)
    TouchAction(driver).tap(x=800, y=2280).perform()  # 进入看图使用一次提示
    time.sleep(2)
    TouchAction(driver).tap(x=1000, y=1560).perform()  # 选择右侧提示广告
    driver.back()
    # 广告次数
    a = 6
    while a > 0:
        TouchAction(driver).tap(x=475, y=2280).perform()
        time.sleep(1)
        TouchAction(driver).tap(x=1105, y=2188).perform()
        time.sleep(1)
        TouchAction(driver).tap(x=800, y=2280).perform()  # 选择(位置)
        time.sleep(3)
        TouchAction(driver).tap(x=444, y=1560).perform()  # 选择左侧去除多余选项广告
        print(a)
        time.sleep(6)
        try:
            GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
        except NoSuchElementException:
            print("toutiaosdk广告")
            time.sleep(40)
            TouchAction(driver).tap(x=1285, y=139).perform()  # 关闭toutiao广告
            print("toutiaosdk广告关闭")
        else:
            print("GDTsdk广告")
            time.sleep(55)
            driver.back()  # GDTsdk广告按钮
            print("GDTsdk广告关闭")
        a -= 1
        time.sleep(2)
        TouchAction(driver).tap(x=1000, y=1560).perform()  # 选择右侧提示广告
        print(a)
        time.sleep(6)
        try:
            GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
        except NoSuchElementException:
            print("toutiaosdk广告")
            time.sleep(40)
            TouchAction(driver).tap(x=1285, y=139).perform()  # 关闭toutiao广告
            print("toutiaosdk广告关闭")
        else:
            print("GDTsdk广告")
            time.sleep(55)
            driver.back()  # GDTsdk广告按钮
            print("GDTsdk广告关闭")
        # print(a)
        time.sleep(2)
        driver.back()
        time.sleep(2)
        a -= 1


kantu()
driver.back()  # 返回首页
time.sleep(2)

TouchAction(driver).tap(x=588, y=186).perform()  # 返回进入个人中心
time.sleep(2)
TouchAction(driver).tap(x=1275, y=243).perform()
time.sleep(1)
TouchAction(driver).tap(x=707, y=2467).perform()
time.sleep(1)
TouchAction(driver).tap(x=960, y=1440).perform()
BB = mobile + " \033[1;31m账号退出成功\033[0m"
print(BB)
#######################################################################################################################


mobile = "18017700597"
AA = "\033[1;31mNO.12\033[0m " + mobile + " \033[1;31m开始\033[0m"
print(AA)
nowtime = time.strftime('%Y-%m-%d% %H:%M:%S')
print(nowtime)
time.sleep(5)


def check_login():
    try:
        check_login = driver.find_element_by_id(
            "com.kamitu.drawsth.standalone.free.android:id/iv_mobile_login")  # 选择手机号登录
    except NoSuchElementException:
        print("自动登录成功")
    else:
        TouchAction(driver).tap(x=515, y=2300).perform()
        time.sleep(2)
        el2 = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/edit_phone")  # 选择手机号输入框
        el2.send_keys(mobile)
        time.sleep(2)
        TouchAction(driver).tap(x=1100, y=870).perform()  # 获取验证码
        time.sleep(2)
        # 获取验证码
        logincodeurl = "https://uc.crazyccy.com/login/main_login/testtool?key=sLQq2_jaKLknsqAwZ&type=1&mobile=" + mobile
        # print(logincodeurl)
        request = urllib.request.Request(logincodeurl)  # 构建请求url
        response = urllib.request.urlopen(request, context=context)  # ssl证书免验证加入,context = context# 打开请求url链接
        num = response.read()  # 读取页面返回信息，python3返回数据为bytes类型的对象 (即b为前缀, bytes类型)
        logincode = num.decode()
        if logincode == "查不到！":
            print("获取验证码失败")
            TouchAction(driver).tap(x=1100, y=870).perform()  # 获取验证码
        time.sleep(1)
        el4 = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/edit_identifyCode")  # 选择验证码输入框
        time.sleep(2)
        el4.send_keys(logincode)
        time.sleep(2)
        TouchAction(driver).tap(x=700, y=1200).perform()  # 确定按钮登录
        print("账号登录成功")


check_login()

time.sleep(15)  # 等待10秒加载进入首页


def check_signwindows():  # 检查用户签到弹窗
    try:
        check_signwindows = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/iv_signin_get")
    except NoSuchElementException:
        print("无签到弹窗")
    else:
        TouchAction(driver).tap(x=712, y=1884).perform()
        time.sleep(6)
        TouchAction(driver).tap(x=712, y=852).perform()
        time.sleep(6)
        try:
            GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
        except NoSuchElementException:
            print("toutiaosdk广告")
            time.sleep(40)
            TouchAction(driver).tap(x=1285, y=139).perform()  # 关闭toutiao广告
            print("toutiaosdk广告关闭")
            time.sleep(6)
            TouchAction(driver).tap(x=1254, y=671).perform()  # 关闭加分弹窗
        else:
            print("GDTsdk广告")
            time.sleep(55)
            driver.back()  # GDTsdk广告按钮
            print("GDTsdk广告关闭")
            time.sleep(6)
            TouchAction(driver).tap(x=1254, y=671).perform()  # 关闭加分弹窗


check_signwindows()
time.sleep(3)


def choujiang():
    time.sleep(3)
    TouchAction(driver).tap(x=1285, y=2354).perform()  # 进入抽奖页面
    time.sleep(2)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽10次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽9次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 看广告
    time.sleep(6)
    try:
        GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
    except NoSuchElementException:
        print("toutiaosdk广告")
        time.sleep(40)
        TouchAction(driver).tap(x=1285, y=139).perform()  # 关闭toutiao广告
        print("toutiaosdk广告关闭")
    else:
        print("GDTsdk广告")
        time.sleep(55)
        driver.back()  # GDTsdk广告按钮
        print("GDTsdk广告关闭")
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽8次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽7次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽6次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 看广告
    time.sleep(6)
    try:
        GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
    except NoSuchElementException:
        print("toutiaosdk广告")
        time.sleep(40)
        TouchAction(driver).tap(x=1285, y=139).perform()  # 关闭toutiao广告
        print("toutiaosdk广告关闭")
    else:
        print("GDTsdk广告")
        time.sleep(55)
        driver.back()  # GDTsdk广告按钮
        print("GDTsdk广告关闭")
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽5次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽4次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽3次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽2次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 看广告
    time.sleep(6)
    try:
        GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
    except NoSuchElementException:
        print("toutiaosdk广告")
        time.sleep(40)
        TouchAction(driver).tap(x=1285, y=139).perform()  # 关闭toutiao广告
        print("toutiaosdk广告关闭")
    else:
        print("GDTsdk广告")
        time.sleep(55)
        driver.back()  # GDTsdk广告按钮
        print("GDTsdk广告关闭")
    time.sleep(1)


choujiang()

time.sleep(3)
TouchAction(driver).tap(x=707, y=2070).perform()  # 进入接龙页面
time.sleep(3)
driver.back()
time.sleep(3)


def check_signtoast():  # 检查是否开启签到提示
    try:
        check_signtoast = driver.find_element_by_id(
            "com.kamitu.drawsth.standalone.free.android:id/iv_checkin_reminder_close")
    except NoSuchElementException:
        print("无签到提示")
    else:
        TouchAction(driver).tap(x=1228, y=748).perform()


check_signtoast()
time.sleep(3)


def kantu():
    TouchAction(driver).tap(x=175, y=2385).perform()  # 进入看图猜成语
    time.sleep(3)
    TouchAction(driver).tap(x=475, y=2280).perform()
    time.sleep(1)
    TouchAction(driver).tap(x=1105, y=2188).perform()
    time.sleep(1)
    TouchAction(driver).tap(x=800, y=2280).perform()  # 进入看图使用一次提示
    time.sleep(2)
    TouchAction(driver).tap(x=1000, y=1560).perform()  # 选择右侧提示广告
    driver.back()
    # 广告次数
    a = 6
    while a > 0:
        TouchAction(driver).tap(x=475, y=2280).perform()
        time.sleep(1)
        TouchAction(driver).tap(x=1105, y=2188).perform()
        time.sleep(1)
        TouchAction(driver).tap(x=800, y=2280).perform()  # 选择(位置)
        time.sleep(3)
        TouchAction(driver).tap(x=444, y=1560).perform()  # 选择左侧去除多余选项广告
        print(a)
        time.sleep(6)
        try:
            GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
        except NoSuchElementException:
            print("toutiaosdk广告")
            time.sleep(40)
            TouchAction(driver).tap(x=1285, y=139).perform()  # 关闭toutiao广告
            print("toutiaosdk广告关闭")
        else:
            print("GDTsdk广告")
            time.sleep(55)
            driver.back()  # GDTsdk广告按钮
            print("GDTsdk广告关闭")
        a -= 1
        time.sleep(2)
        TouchAction(driver).tap(x=1000, y=1560).perform()  # 选择右侧提示广告
        print(a)
        time.sleep(6)
        try:
            GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
        except NoSuchElementException:
            print("toutiaosdk广告")
            time.sleep(40)
            TouchAction(driver).tap(x=1285, y=139).perform()  # 关闭toutiao广告
            print("toutiaosdk广告关闭")
        else:
            print("GDTsdk广告")
            time.sleep(55)
            driver.back()  # GDTsdk广告按钮
            print("GDTsdk广告关闭")
        # print(a)
        time.sleep(2)
        driver.back()
        time.sleep(2)
        a -= 1


kantu()
driver.back()  # 返回首页
time.sleep(2)

TouchAction(driver).tap(x=588, y=186).perform()  # 返回进入个人中心
time.sleep(2)
TouchAction(driver).tap(x=1275, y=243).perform()
time.sleep(1)
TouchAction(driver).tap(x=707, y=2467).perform()
time.sleep(1)
TouchAction(driver).tap(x=960, y=1440).perform()
BB = mobile + " \033[1;31m账号退出成功\033[0m"
print(BB)
#######################################################################################################################


mobile = "18017700598"
AA = "\033[1;31mNO.13\033[0m " + mobile + " \033[1;31m开始\033[0m"
print(AA)
nowtime = time.strftime('%Y-%m-%d% %H:%M:%S')
print(nowtime)
time.sleep(5)


def check_login():
    try:
        check_login = driver.find_element_by_id(
            "com.kamitu.drawsth.standalone.free.android:id/iv_mobile_login")  # 选择手机号登录
    except NoSuchElementException:
        print("自动登录成功")
    else:
        TouchAction(driver).tap(x=515, y=2300).perform()
        time.sleep(2)
        el2 = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/edit_phone")  # 选择手机号输入框
        el2.send_keys(mobile)
        time.sleep(2)
        TouchAction(driver).tap(x=1100, y=870).perform()  # 获取验证码
        time.sleep(2)
        # 获取验证码
        logincodeurl = "https://uc.crazyccy.com/login/main_login/testtool?key=sLQq2_jaKLknsqAwZ&type=1&mobile=" + mobile
        # print(logincodeurl)
        request = urllib.request.Request(logincodeurl)  # 构建请求url
        response = urllib.request.urlopen(request, context=context)  # ssl证书免验证加入,context = context# 打开请求url链接
        num = response.read()  # 读取页面返回信息，python3返回数据为bytes类型的对象 (即b为前缀, bytes类型)
        logincode = num.decode()
        if logincode == "查不到！":
            print("获取验证码失败")
            TouchAction(driver).tap(x=1100, y=870).perform()  # 获取验证码
        time.sleep(1)
        el4 = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/edit_identifyCode")  # 选择验证码输入框
        time.sleep(2)
        el4.send_keys(logincode)
        time.sleep(2)
        TouchAction(driver).tap(x=700, y=1200).perform()  # 确定按钮登录
        print("账号登录成功")


check_login()

time.sleep(15)  # 等待10秒加载进入首页


def check_signwindows():  # 检查用户签到弹窗
    try:
        check_signwindows = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/iv_signin_get")
    except NoSuchElementException:
        print("无签到弹窗")
    else:
        TouchAction(driver).tap(x=712, y=1884).perform()
        time.sleep(6)
        TouchAction(driver).tap(x=712, y=852).perform()
        time.sleep(6)
        try:
            GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
        except NoSuchElementException:
            print("toutiaosdk广告")
            time.sleep(40)
            TouchAction(driver).tap(x=1285, y=139).perform()  # 关闭toutiao广告
            print("toutiaosdk广告关闭")
            time.sleep(6)
            TouchAction(driver).tap(x=1254, y=671).perform()  # 关闭加分弹窗
        else:
            print("GDTsdk广告")
            time.sleep(55)
            driver.back()  # GDTsdk广告按钮
            print("GDTsdk广告关闭")
            time.sleep(6)
            TouchAction(driver).tap(x=1254, y=671).perform()  # 关闭加分弹窗


check_signwindows()
time.sleep(3)


def choujiang():
    time.sleep(3)
    TouchAction(driver).tap(x=1285, y=2354).perform()  # 进入抽奖页面
    time.sleep(2)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽10次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽9次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 看广告
    time.sleep(6)
    try:
        GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
    except NoSuchElementException:
        print("toutiaosdk广告")
        time.sleep(40)
        TouchAction(driver).tap(x=1285, y=139).perform()  # 关闭toutiao广告
        print("toutiaosdk广告关闭")
    else:
        print("GDTsdk广告")
        time.sleep(55)
        driver.back()  # GDTsdk广告按钮
        print("GDTsdk广告关闭")
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽8次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽7次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽6次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 看广告
    time.sleep(6)
    try:
        GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
    except NoSuchElementException:
        print("toutiaosdk广告")
        time.sleep(40)
        TouchAction(driver).tap(x=1285, y=139).perform()  # 关闭toutiao广告
        print("toutiaosdk广告关闭")
    else:
        print("GDTsdk广告")
        time.sleep(55)
        driver.back()  # GDTsdk广告按钮
        print("GDTsdk广告关闭")
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽5次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽4次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽3次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽2次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 看广告
    time.sleep(6)
    try:
        GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
    except NoSuchElementException:
        print("toutiaosdk广告")
        time.sleep(40)
        TouchAction(driver).tap(x=1285, y=139).perform()  # 关闭toutiao广告
        print("toutiaosdk广告关闭")
    else:
        print("GDTsdk广告")
        time.sleep(55)
        driver.back()  # GDTsdk广告按钮
        print("GDTsdk广告关闭")
    time.sleep(1)


choujiang()

time.sleep(3)
TouchAction(driver).tap(x=707, y=2070).perform()  # 进入接龙页面
time.sleep(3)
driver.back()
time.sleep(3)


def check_signtoast():  # 检查是否开启签到提示
    try:
        check_signtoast = driver.find_element_by_id(
            "com.kamitu.drawsth.standalone.free.android:id/iv_checkin_reminder_close")
    except NoSuchElementException:
        print("无签到提示")
    else:
        TouchAction(driver).tap(x=1228, y=748).perform()


check_signtoast()
time.sleep(3)


def kantu():
    TouchAction(driver).tap(x=175, y=2385).perform()  # 进入看图猜成语
    time.sleep(3)
    TouchAction(driver).tap(x=475, y=2280).perform()
    time.sleep(1)
    TouchAction(driver).tap(x=1105, y=2188).perform()
    time.sleep(1)
    TouchAction(driver).tap(x=800, y=2280).perform()  # 进入看图使用一次提示
    time.sleep(2)
    TouchAction(driver).tap(x=1000, y=1560).perform()  # 选择右侧提示广告
    driver.back()
    # 广告次数
    a = 6
    while a > 0:
        TouchAction(driver).tap(x=475, y=2280).perform()
        time.sleep(1)
        TouchAction(driver).tap(x=1105, y=2188).perform()
        time.sleep(1)
        TouchAction(driver).tap(x=800, y=2280).perform()  # 选择(位置)
        time.sleep(3)
        TouchAction(driver).tap(x=444, y=1560).perform()  # 选择左侧去除多余选项广告
        print(a)
        time.sleep(6)
        try:
            GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
        except NoSuchElementException:
            print("toutiaosdk广告")
            time.sleep(40)
            TouchAction(driver).tap(x=1285, y=139).perform()  # 关闭toutiao广告
            print("toutiaosdk广告关闭")
        else:
            print("GDTsdk广告")
            time.sleep(55)
            driver.back()  # GDTsdk广告按钮
            print("GDTsdk广告关闭")
        a -= 1
        time.sleep(2)
        TouchAction(driver).tap(x=1000, y=1560).perform()  # 选择右侧提示广告
        print(a)
        time.sleep(6)
        try:
            GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
        except NoSuchElementException:
            print("toutiaosdk广告")
            time.sleep(40)
            TouchAction(driver).tap(x=1285, y=139).perform()  # 关闭toutiao广告
            print("toutiaosdk广告关闭")
        else:
            print("GDTsdk广告")
            time.sleep(55)
            driver.back()  # GDTsdk广告按钮
            print("GDTsdk广告关闭")
        # print(a)
        time.sleep(2)
        driver.back()
        time.sleep(2)
        a -= 1


kantu()
driver.back()  # 返回首页
time.sleep(2)

TouchAction(driver).tap(x=588, y=186).perform()  # 返回进入个人中心
time.sleep(2)
TouchAction(driver).tap(x=1275, y=243).perform()
time.sleep(1)
TouchAction(driver).tap(x=707, y=2467).perform()
time.sleep(1)
TouchAction(driver).tap(x=960, y=1440).perform()
BB = mobile + " \033[1;31m账号退出成功\033[0m"
print(BB)
#######################################################################################################################


mobile = "18017700599"
AA = "\033[1;31mNO.14\033[0m " + mobile + " \033[1;31m开始\033[0m"
print(AA)
nowtime = time.strftime('%Y-%m-%d% %H:%M:%S')
print(nowtime)
time.sleep(5)


def check_login():
    try:
        check_login = driver.find_element_by_id(
            "com.kamitu.drawsth.standalone.free.android:id/iv_mobile_login")  # 选择手机号登录
    except NoSuchElementException:
        print("自动登录成功")
    else:
        TouchAction(driver).tap(x=515, y=2300).perform()
        time.sleep(2)
        el2 = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/edit_phone")  # 选择手机号输入框
        el2.send_keys(mobile)
        time.sleep(2)
        TouchAction(driver).tap(x=1100, y=870).perform()  # 获取验证码
        time.sleep(2)
        # 获取验证码
        logincodeurl = "https://uc.crazyccy.com/login/main_login/testtool?key=sLQq2_jaKLknsqAwZ&type=1&mobile=" + mobile
        # print(logincodeurl)
        request = urllib.request.Request(logincodeurl)  # 构建请求url
        response = urllib.request.urlopen(request, context=context)  # ssl证书免验证加入,context = context# 打开请求url链接
        num = response.read()  # 读取页面返回信息，python3返回数据为bytes类型的对象 (即b为前缀, bytes类型)
        logincode = num.decode()
        if logincode == "查不到！":
            print("获取验证码失败")
            TouchAction(driver).tap(x=1100, y=870).perform()  # 获取验证码
        time.sleep(1)
        el4 = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/edit_identifyCode")  # 选择验证码输入框
        time.sleep(2)
        el4.send_keys(logincode)
        time.sleep(2)
        TouchAction(driver).tap(x=700, y=1200).perform()  # 确定按钮登录
        print("账号登录成功")


check_login()

time.sleep(15)  # 等待10秒加载进入首页


def check_signwindows():  # 检查用户签到弹窗
    try:
        check_signwindows = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/iv_signin_get")
    except NoSuchElementException:
        print("无签到弹窗")
    else:
        TouchAction(driver).tap(x=712, y=1884).perform()
        time.sleep(6)
        TouchAction(driver).tap(x=712, y=852).perform()
        time.sleep(6)
        try:
            GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
        except NoSuchElementException:
            print("toutiaosdk广告")
            time.sleep(40)
            TouchAction(driver).tap(x=1285, y=139).perform()  # 关闭toutiao广告
            print("toutiaosdk广告关闭")
            time.sleep(6)
            TouchAction(driver).tap(x=1254, y=671).perform()  # 关闭加分弹窗
        else:
            print("GDTsdk广告")
            time.sleep(55)
            driver.back()  # GDTsdk广告按钮
            print("GDTsdk广告关闭")
            time.sleep(6)
            TouchAction(driver).tap(x=1254, y=671).perform()  # 关闭加分弹窗


check_signwindows()
time.sleep(3)


def choujiang():
    time.sleep(3)
    TouchAction(driver).tap(x=1285, y=2354).perform()  # 进入抽奖页面
    time.sleep(2)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽10次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽9次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 看广告
    time.sleep(6)
    try:
        GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
    except NoSuchElementException:
        print("toutiaosdk广告")
        time.sleep(40)
        TouchAction(driver).tap(x=1285, y=139).perform()  # 关闭toutiao广告
        print("toutiaosdk广告关闭")
    else:
        print("GDTsdk广告")
        time.sleep(55)
        driver.back()  # GDTsdk广告按钮
        print("GDTsdk广告关闭")
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽8次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽7次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽6次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 看广告
    time.sleep(6)
    try:
        GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
    except NoSuchElementException:
        print("toutiaosdk广告")
        time.sleep(40)
        TouchAction(driver).tap(x=1285, y=139).perform()  # 关闭toutiao广告
        print("toutiaosdk广告关闭")
    else:
        print("GDTsdk广告")
        time.sleep(55)
        driver.back()  # GDTsdk广告按钮
        print("GDTsdk广告关闭")
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽5次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽4次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽3次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽2次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 看广告
    time.sleep(6)
    try:
        GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
    except NoSuchElementException:
        print("toutiaosdk广告")
        time.sleep(40)
        TouchAction(driver).tap(x=1285, y=139).perform()  # 关闭toutiao广告
        print("toutiaosdk广告关闭")
    else:
        print("GDTsdk广告")
        time.sleep(55)
        driver.back()  # GDTsdk广告按钮
        print("GDTsdk广告关闭")
    time.sleep(1)


choujiang()

time.sleep(3)
TouchAction(driver).tap(x=707, y=2070).perform()  # 进入接龙页面
time.sleep(3)
driver.back()
time.sleep(3)


def check_signtoast():  # 检查是否开启签到提示
    try:
        check_signtoast = driver.find_element_by_id(
            "com.kamitu.drawsth.standalone.free.android:id/iv_checkin_reminder_close")
    except NoSuchElementException:
        print("无签到提示")
    else:
        TouchAction(driver).tap(x=1228, y=748).perform()


check_signtoast()
time.sleep(3)


def kantu():
    TouchAction(driver).tap(x=175, y=2385).perform()  # 进入看图猜成语
    time.sleep(3)
    TouchAction(driver).tap(x=475, y=2280).perform()
    time.sleep(1)
    TouchAction(driver).tap(x=1105, y=2188).perform()
    time.sleep(1)
    TouchAction(driver).tap(x=800, y=2280).perform()  # 进入看图使用一次提示
    time.sleep(2)
    TouchAction(driver).tap(x=1000, y=1560).perform()  # 选择右侧提示广告
    driver.back()
    # 广告次数
    a = 6
    while a > 0:
        TouchAction(driver).tap(x=475, y=2280).perform()
        time.sleep(1)
        TouchAction(driver).tap(x=1105, y=2188).perform()
        time.sleep(1)
        TouchAction(driver).tap(x=800, y=2280).perform()  # 选择(位置)
        time.sleep(3)
        TouchAction(driver).tap(x=444, y=1560).perform()  # 选择左侧去除多余选项广告
        print(a)
        time.sleep(6)
        try:
            GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
        except NoSuchElementException:
            print("toutiaosdk广告")
            time.sleep(40)
            TouchAction(driver).tap(x=1285, y=139).perform()  # 关闭toutiao广告
            print("toutiaosdk广告关闭")
        else:
            print("GDTsdk广告")
            time.sleep(55)
            driver.back()  # GDTsdk广告按钮
            print("GDTsdk广告关闭")
        a -= 1
        time.sleep(2)
        TouchAction(driver).tap(x=1000, y=1560).perform()  # 选择右侧提示广告
        print(a)
        time.sleep(6)
        try:
            GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
        except NoSuchElementException:
            print("toutiaosdk广告")
            time.sleep(40)
            TouchAction(driver).tap(x=1285, y=139).perform()  # 关闭toutiao广告
            print("toutiaosdk广告关闭")
        else:
            print("GDTsdk广告")
            time.sleep(55)
            driver.back()  # GDTsdk广告按钮
            print("GDTsdk广告关闭")
        # print(a)
        time.sleep(2)
        driver.back()
        time.sleep(2)
        a -= 1


kantu()
driver.back()  # 返回首页
time.sleep(2)

TouchAction(driver).tap(x=588, y=186).perform()  # 返回进入个人中心
time.sleep(2)
TouchAction(driver).tap(x=1275, y=243).perform()
time.sleep(1)
TouchAction(driver).tap(x=707, y=2467).perform()
time.sleep(1)
TouchAction(driver).tap(x=960, y=1440).perform()
BB = mobile + " \033[1;31m账号退出成功\033[0m"
print(BB)
#######################################################################################################################


mobile = "18017700601"
AA = "\033[1;31mNO.15\033[0m " + mobile + " \033[1;31m开始\033[0m"
print(AA)
nowtime = time.strftime('%Y-%m-%d% %H:%M:%S')
print(nowtime)
time.sleep(5)


def check_login():
    try:
        check_login = driver.find_element_by_id(
            "com.kamitu.drawsth.standalone.free.android:id/iv_mobile_login")  # 选择手机号登录
    except NoSuchElementException:
        print("自动登录成功")
    else:
        TouchAction(driver).tap(x=515, y=2300).perform()
        time.sleep(2)
        el2 = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/edit_phone")  # 选择手机号输入框
        el2.send_keys(mobile)
        time.sleep(2)
        TouchAction(driver).tap(x=1100, y=870).perform()  # 获取验证码
        time.sleep(2)
        # 获取验证码
        logincodeurl = "https://uc.crazyccy.com/login/main_login/testtool?key=sLQq2_jaKLknsqAwZ&type=1&mobile=" + mobile
        # print(logincodeurl)
        request = urllib.request.Request(logincodeurl)  # 构建请求url
        response = urllib.request.urlopen(request, context=context)  # ssl证书免验证加入,context = context# 打开请求url链接
        num = response.read()  # 读取页面返回信息，python3返回数据为bytes类型的对象 (即b为前缀, bytes类型)
        logincode = num.decode()
        if logincode == "查不到！":
            print("获取验证码失败")
            TouchAction(driver).tap(x=1100, y=870).perform()  # 获取验证码
        time.sleep(1)
        el4 = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/edit_identifyCode")  # 选择验证码输入框
        time.sleep(2)
        el4.send_keys(logincode)
        time.sleep(2)
        TouchAction(driver).tap(x=700, y=1200).perform()  # 确定按钮登录
        print("账号登录成功")


check_login()

time.sleep(15)  # 等待10秒加载进入首页


def check_signwindows():  # 检查用户签到弹窗
    try:
        check_signwindows = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/iv_signin_get")
    except NoSuchElementException:
        print("无签到弹窗")
    else:
        TouchAction(driver).tap(x=712, y=1884).perform()
        time.sleep(6)
        TouchAction(driver).tap(x=712, y=852).perform()
        time.sleep(6)
        try:
            GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
        except NoSuchElementException:
            print("toutiaosdk广告")
            time.sleep(40)
            TouchAction(driver).tap(x=1285, y=139).perform()  # 关闭toutiao广告
            print("toutiaosdk广告关闭")
            time.sleep(6)
            TouchAction(driver).tap(x=1254, y=671).perform()  # 关闭加分弹窗
        else:
            print("GDTsdk广告")
            time.sleep(55)
            driver.back()  # GDTsdk广告按钮
            print("GDTsdk广告关闭")
            time.sleep(6)
            TouchAction(driver).tap(x=1254, y=671).perform()  # 关闭加分弹窗


check_signwindows()
time.sleep(3)


def choujiang():
    time.sleep(3)
    TouchAction(driver).tap(x=1285, y=2354).perform()  # 进入抽奖页面
    time.sleep(2)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽10次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽9次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 看广告
    time.sleep(6)
    try:
        GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
    except NoSuchElementException:
        print("toutiaosdk广告")
        time.sleep(40)
        TouchAction(driver).tap(x=1285, y=139).perform()  # 关闭toutiao广告
        print("toutiaosdk广告关闭")
    else:
        print("GDTsdk广告")
        time.sleep(55)
        driver.back()  # GDTsdk广告按钮
        print("GDTsdk广告关闭")
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽8次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽7次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽6次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 看广告
    time.sleep(6)
    try:
        GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
    except NoSuchElementException:
        print("toutiaosdk广告")
        time.sleep(40)
        TouchAction(driver).tap(x=1285, y=139).perform()  # 关闭toutiao广告
        print("toutiaosdk广告关闭")
    else:
        print("GDTsdk广告")
        time.sleep(55)
        driver.back()  # GDTsdk广告按钮
        print("GDTsdk广告关闭")
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽5次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽4次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽3次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽2次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 看广告
    time.sleep(6)
    try:
        GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
    except NoSuchElementException:
        print("toutiaosdk广告")
        time.sleep(40)
        TouchAction(driver).tap(x=1285, y=139).perform()  # 关闭toutiao广告
        print("toutiaosdk广告关闭")
    else:
        print("GDTsdk广告")
        time.sleep(55)
        driver.back()  # GDTsdk广告按钮
        print("GDTsdk广告关闭")
    time.sleep(1)


choujiang()

time.sleep(3)
TouchAction(driver).tap(x=707, y=2070).perform()  # 进入接龙页面
time.sleep(3)
driver.back()
time.sleep(3)


def check_signtoast():  # 检查是否开启签到提示
    try:
        check_signtoast = driver.find_element_by_id(
            "com.kamitu.drawsth.standalone.free.android:id/iv_checkin_reminder_close")
    except NoSuchElementException:
        print("无签到提示")
    else:
        TouchAction(driver).tap(x=1228, y=748).perform()


check_signtoast()
time.sleep(3)


def kantu():
    TouchAction(driver).tap(x=175, y=2385).perform()  # 进入看图猜成语
    time.sleep(3)
    TouchAction(driver).tap(x=475, y=2280).perform()
    time.sleep(1)
    TouchAction(driver).tap(x=1105, y=2188).perform()
    time.sleep(1)
    TouchAction(driver).tap(x=800, y=2280).perform()  # 进入看图使用一次提示
    time.sleep(2)
    TouchAction(driver).tap(x=1000, y=1560).perform()  # 选择右侧提示广告
    driver.back()
    # 广告次数
    a = 6
    while a > 0:
        TouchAction(driver).tap(x=475, y=2280).perform()
        time.sleep(1)
        TouchAction(driver).tap(x=1105, y=2188).perform()
        time.sleep(1)
        TouchAction(driver).tap(x=800, y=2280).perform()  # 选择(位置)
        time.sleep(3)
        TouchAction(driver).tap(x=444, y=1560).perform()  # 选择左侧去除多余选项广告
        print(a)
        time.sleep(6)
        try:
            GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
        except NoSuchElementException:
            print("toutiaosdk广告")
            time.sleep(40)
            TouchAction(driver).tap(x=1285, y=139).perform()  # 关闭toutiao广告
            print("toutiaosdk广告关闭")
        else:
            print("GDTsdk广告")
            time.sleep(55)
            driver.back()  # GDTsdk广告按钮
            print("GDTsdk广告关闭")
        a -= 1
        time.sleep(2)
        TouchAction(driver).tap(x=1000, y=1560).perform()  # 选择右侧提示广告
        print(a)
        time.sleep(6)
        try:
            GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
        except NoSuchElementException:
            print("toutiaosdk广告")
            time.sleep(40)
            TouchAction(driver).tap(x=1285, y=139).perform()  # 关闭toutiao广告
            print("toutiaosdk广告关闭")
        else:
            print("GDTsdk广告")
            time.sleep(55)
            driver.back()  # GDTsdk广告按钮
            print("GDTsdk广告关闭")
        # print(a)
        time.sleep(2)
        driver.back()
        time.sleep(2)
        a -= 1


kantu()
driver.back()  # 返回首页
time.sleep(2)

TouchAction(driver).tap(x=588, y=186).perform()  # 返回进入个人中心
time.sleep(2)
TouchAction(driver).tap(x=1275, y=243).perform()
time.sleep(1)
TouchAction(driver).tap(x=707, y=2467).perform()
time.sleep(1)
TouchAction(driver).tap(x=960, y=1440).perform()
BB = mobile + " \033[1;31m账号退出成功\033[0m"
print(BB)
#######################################################################################################################


mobile = "18017700602"
AA = "\033[1;31mNO.16\033[0m " + mobile + " \033[1;31m开始\033[0m"
print(AA)
nowtime = time.strftime('%Y-%m-%d% %H:%M:%S')
print(nowtime)
time.sleep(5)


def check_login():
    try:
        check_login = driver.find_element_by_id(
            "com.kamitu.drawsth.standalone.free.android:id/iv_mobile_login")  # 选择手机号登录
    except NoSuchElementException:
        print("自动登录成功")
    else:
        TouchAction(driver).tap(x=515, y=2300).perform()
        time.sleep(2)
        el2 = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/edit_phone")  # 选择手机号输入框
        el2.send_keys(mobile)
        time.sleep(2)
        TouchAction(driver).tap(x=1100, y=870).perform()  # 获取验证码
        time.sleep(2)
        # 获取验证码
        logincodeurl = "https://uc.crazyccy.com/login/main_login/testtool?key=sLQq2_jaKLknsqAwZ&type=1&mobile=" + mobile
        # print(logincodeurl)
        request = urllib.request.Request(logincodeurl)  # 构建请求url
        response = urllib.request.urlopen(request, context=context)  # ssl证书免验证加入,context = context# 打开请求url链接
        num = response.read()  # 读取页面返回信息，python3返回数据为bytes类型的对象 (即b为前缀, bytes类型)
        logincode = num.decode()
        if logincode == "查不到！":
            print("获取验证码失败")
            TouchAction(driver).tap(x=1100, y=870).perform()  # 获取验证码
        time.sleep(1)
        el4 = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/edit_identifyCode")  # 选择验证码输入框
        time.sleep(2)
        el4.send_keys(logincode)
        time.sleep(2)
        TouchAction(driver).tap(x=700, y=1200).perform()  # 确定按钮登录
        print("账号登录成功")


check_login()

time.sleep(15)  # 等待10秒加载进入首页


def check_signwindows():  # 检查用户签到弹窗
    try:
        check_signwindows = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/iv_signin_get")
    except NoSuchElementException:
        print("无签到弹窗")
    else:
        TouchAction(driver).tap(x=712, y=1884).perform()
        time.sleep(6)
        TouchAction(driver).tap(x=712, y=852).perform()
        time.sleep(6)
        try:
            GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
        except NoSuchElementException:
            print("toutiaosdk广告")
            time.sleep(40)
            TouchAction(driver).tap(x=1285, y=139).perform()  # 关闭toutiao广告
            print("toutiaosdk广告关闭")
            time.sleep(6)
            TouchAction(driver).tap(x=1254, y=671).perform()  # 关闭加分弹窗
        else:
            print("GDTsdk广告")
            time.sleep(55)
            driver.back()  # GDTsdk广告按钮
            print("GDTsdk广告关闭")
            time.sleep(6)
            TouchAction(driver).tap(x=1254, y=671).perform()  # 关闭加分弹窗


check_signwindows()
time.sleep(3)


def choujiang():
    time.sleep(3)
    TouchAction(driver).tap(x=1285, y=2354).perform()  # 进入抽奖页面
    time.sleep(2)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽10次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽9次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 看广告
    time.sleep(6)
    try:
        GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
    except NoSuchElementException:
        print("toutiaosdk广告")
        time.sleep(40)
        TouchAction(driver).tap(x=1285, y=139).perform()  # 关闭toutiao广告
        print("toutiaosdk广告关闭")
    else:
        print("GDTsdk广告")
        time.sleep(55)
        driver.back()  # GDTsdk广告按钮
        print("GDTsdk广告关闭")
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽8次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽7次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽6次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 看广告
    time.sleep(6)
    try:
        GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
    except NoSuchElementException:
        print("toutiaosdk广告")
        time.sleep(40)
        TouchAction(driver).tap(x=1285, y=139).perform()  # 关闭toutiao广告
        print("toutiaosdk广告关闭")
    else:
        print("GDTsdk广告")
        time.sleep(55)
        driver.back()  # GDTsdk广告按钮
        print("GDTsdk广告关闭")
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽5次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽4次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽3次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽2次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 看广告
    time.sleep(6)
    try:
        GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
    except NoSuchElementException:
        print("toutiaosdk广告")
        time.sleep(40)
        TouchAction(driver).tap(x=1285, y=139).perform()  # 关闭toutiao广告
        print("toutiaosdk广告关闭")
    else:
        print("GDTsdk广告")
        time.sleep(55)
        driver.back()  # GDTsdk广告按钮
        print("GDTsdk广告关闭")
    time.sleep(1)


choujiang()

time.sleep(3)
TouchAction(driver).tap(x=707, y=2070).perform()  # 进入接龙页面
time.sleep(3)
driver.back()
time.sleep(3)


def check_signtoast():  # 检查是否开启签到提示
    try:
        check_signtoast = driver.find_element_by_id(
            "com.kamitu.drawsth.standalone.free.android:id/iv_checkin_reminder_close")
    except NoSuchElementException:
        print("无签到提示")
    else:
        TouchAction(driver).tap(x=1228, y=748).perform()


check_signtoast()
time.sleep(3)


def kantu():
    TouchAction(driver).tap(x=175, y=2385).perform()  # 进入看图猜成语
    time.sleep(3)
    TouchAction(driver).tap(x=475, y=2280).perform()
    time.sleep(1)
    TouchAction(driver).tap(x=1105, y=2188).perform()
    time.sleep(1)
    TouchAction(driver).tap(x=800, y=2280).perform()  # 进入看图使用一次提示
    time.sleep(2)
    TouchAction(driver).tap(x=1000, y=1560).perform()  # 选择右侧提示广告
    driver.back()
    # 广告次数
    a = 6
    while a > 0:
        TouchAction(driver).tap(x=475, y=2280).perform()
        time.sleep(1)
        TouchAction(driver).tap(x=1105, y=2188).perform()
        time.sleep(1)
        TouchAction(driver).tap(x=800, y=2280).perform()  # 选择(位置)
        time.sleep(3)
        TouchAction(driver).tap(x=444, y=1560).perform()  # 选择左侧去除多余选项广告
        print(a)
        time.sleep(6)
        try:
            GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
        except NoSuchElementException:
            print("toutiaosdk广告")
            time.sleep(40)
            TouchAction(driver).tap(x=1285, y=139).perform()  # 关闭toutiao广告
            print("toutiaosdk广告关闭")
        else:
            print("GDTsdk广告")
            time.sleep(55)
            driver.back()  # GDTsdk广告按钮
            print("GDTsdk广告关闭")
        a -= 1
        time.sleep(2)
        TouchAction(driver).tap(x=1000, y=1560).perform()  # 选择右侧提示广告
        print(a)
        time.sleep(6)
        try:
            GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
        except NoSuchElementException:
            print("toutiaosdk广告")
            time.sleep(40)
            TouchAction(driver).tap(x=1285, y=139).perform()  # 关闭toutiao广告
            print("toutiaosdk广告关闭")
        else:
            print("GDTsdk广告")
            time.sleep(55)
            driver.back()  # GDTsdk广告按钮
            print("GDTsdk广告关闭")
        # print(a)
        time.sleep(2)
        driver.back()
        time.sleep(2)
        a -= 1


kantu()
driver.back()  # 返回首页
time.sleep(2)

TouchAction(driver).tap(x=588, y=186).perform()  # 返回进入个人中心
time.sleep(2)
TouchAction(driver).tap(x=1275, y=243).perform()
time.sleep(1)
TouchAction(driver).tap(x=707, y=2467).perform()
time.sleep(1)
TouchAction(driver).tap(x=960, y=1440).perform()
BB = mobile + " \033[1;31m账号退出成功\033[0m"
print(BB)
#######################################################################################################################


mobile = "18017700715"
AA = "\033[1;31mNO.17\033[0m " + mobile + " \033[1;31m开始\033[0m"
print(AA)
nowtime = time.strftime('%Y-%m-%d% %H:%M:%S')
print(nowtime)
time.sleep(5)


def check_login():
    try:
        check_login = driver.find_element_by_id(
            "com.kamitu.drawsth.standalone.free.android:id/iv_mobile_login")  # 选择手机号登录
    except NoSuchElementException:
        print("自动登录成功")
    else:
        TouchAction(driver).tap(x=515, y=2300).perform()
        time.sleep(2)
        el2 = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/edit_phone")  # 选择手机号输入框
        el2.send_keys(mobile)
        time.sleep(2)
        TouchAction(driver).tap(x=1100, y=870).perform()  # 获取验证码
        time.sleep(2)
        # 获取验证码
        logincodeurl = "https://uc.crazyccy.com/login/main_login/testtool?key=sLQq2_jaKLknsqAwZ&type=1&mobile=" + mobile
        # print(logincodeurl)
        request = urllib.request.Request(logincodeurl)  # 构建请求url
        response = urllib.request.urlopen(request, context=context)  # ssl证书免验证加入,context = context# 打开请求url链接
        num = response.read()  # 读取页面返回信息，python3返回数据为bytes类型的对象 (即b为前缀, bytes类型)
        logincode = num.decode()
        if logincode == "查不到！":
            print("获取验证码失败")
            TouchAction(driver).tap(x=1100, y=870).perform()  # 获取验证码
        time.sleep(1)
        el4 = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/edit_identifyCode")  # 选择验证码输入框
        time.sleep(2)
        el4.send_keys(logincode)
        time.sleep(2)
        TouchAction(driver).tap(x=700, y=1200).perform()  # 确定按钮登录
        print("账号登录成功")


check_login()

time.sleep(15)  # 等待10秒加载进入首页


def check_signwindows():  # 检查用户签到弹窗
    try:
        check_signwindows = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/iv_signin_get")
    except NoSuchElementException:
        print("无签到弹窗")
    else:
        TouchAction(driver).tap(x=712, y=1884).perform()
        time.sleep(6)
        TouchAction(driver).tap(x=712, y=852).perform()
        time.sleep(6)
        try:
            GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
        except NoSuchElementException:
            print("toutiaosdk广告")
            time.sleep(40)
            TouchAction(driver).tap(x=1285, y=139).perform()  # 关闭toutiao广告
            print("toutiaosdk广告关闭")
            time.sleep(6)
            TouchAction(driver).tap(x=1254, y=671).perform()  # 关闭加分弹窗
        else:
            print("GDTsdk广告")
            time.sleep(55)
            driver.back()  # GDTsdk广告按钮
            print("GDTsdk广告关闭")
            time.sleep(6)
            TouchAction(driver).tap(x=1254, y=671).perform()  # 关闭加分弹窗


check_signwindows()
time.sleep(3)


def choujiang():
    time.sleep(3)
    TouchAction(driver).tap(x=1285, y=2354).perform()  # 进入抽奖页面
    time.sleep(2)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽10次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽9次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 看广告
    time.sleep(6)
    try:
        GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
    except NoSuchElementException:
        print("toutiaosdk广告")
        time.sleep(40)
        TouchAction(driver).tap(x=1285, y=139).perform()  # 关闭toutiao广告
        print("toutiaosdk广告关闭")
    else:
        print("GDTsdk广告")
        time.sleep(55)
        driver.back()  # GDTsdk广告按钮
        print("GDTsdk广告关闭")
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽8次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽7次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽6次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 看广告
    time.sleep(6)
    try:
        GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
    except NoSuchElementException:
        print("toutiaosdk广告")
        time.sleep(40)
        TouchAction(driver).tap(x=1285, y=139).perform()  # 关闭toutiao广告
        print("toutiaosdk广告关闭")
    else:
        print("GDTsdk广告")
        time.sleep(55)
        driver.back()  # GDTsdk广告按钮
        print("GDTsdk广告关闭")
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽5次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽4次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽3次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽2次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 看广告
    time.sleep(6)
    try:
        GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
    except NoSuchElementException:
        print("toutiaosdk广告")
        time.sleep(40)
        TouchAction(driver).tap(x=1285, y=139).perform()  # 关闭toutiao广告
        print("toutiaosdk广告关闭")
    else:
        print("GDTsdk广告")
        time.sleep(55)
        driver.back()  # GDTsdk广告按钮
        print("GDTsdk广告关闭")
    time.sleep(1)


choujiang()

time.sleep(3)
TouchAction(driver).tap(x=707, y=2070).perform()  # 进入接龙页面
time.sleep(3)
driver.back()
time.sleep(3)


def check_signtoast():  # 检查是否开启签到提示
    try:
        check_signtoast = driver.find_element_by_id(
            "com.kamitu.drawsth.standalone.free.android:id/iv_checkin_reminder_close")
    except NoSuchElementException:
        print("无签到提示")
    else:
        TouchAction(driver).tap(x=1228, y=748).perform()


check_signtoast()
time.sleep(3)


def kantu():
    TouchAction(driver).tap(x=175, y=2385).perform()  # 进入看图猜成语
    time.sleep(3)
    TouchAction(driver).tap(x=475, y=2280).perform()
    time.sleep(1)
    TouchAction(driver).tap(x=1105, y=2188).perform()
    time.sleep(1)
    TouchAction(driver).tap(x=800, y=2280).perform()  # 进入看图使用一次提示
    time.sleep(2)
    TouchAction(driver).tap(x=1000, y=1560).perform()  # 选择右侧提示广告
    driver.back()
    # 广告次数
    a = 6
    while a > 0:
        TouchAction(driver).tap(x=475, y=2280).perform()
        time.sleep(1)
        TouchAction(driver).tap(x=1105, y=2188).perform()
        time.sleep(1)
        TouchAction(driver).tap(x=800, y=2280).perform()  # 选择(位置)
        time.sleep(3)
        TouchAction(driver).tap(x=444, y=1560).perform()  # 选择左侧去除多余选项广告
        print(a)
        time.sleep(6)
        try:
            GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
        except NoSuchElementException:
            print("toutiaosdk广告")
            time.sleep(40)
            TouchAction(driver).tap(x=1285, y=139).perform()  # 关闭toutiao广告
            print("toutiaosdk广告关闭")
        else:
            print("GDTsdk广告")
            time.sleep(55)
            driver.back()  # GDTsdk广告按钮
            print("GDTsdk广告关闭")
        a -= 1
        time.sleep(2)
        TouchAction(driver).tap(x=1000, y=1560).perform()  # 选择右侧提示广告
        print(a)
        time.sleep(6)
        try:
            GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
        except NoSuchElementException:
            print("toutiaosdk广告")
            time.sleep(40)
            TouchAction(driver).tap(x=1285, y=139).perform()  # 关闭toutiao广告
            print("toutiaosdk广告关闭")
        else:
            print("GDTsdk广告")
            time.sleep(55)
            driver.back()  # GDTsdk广告按钮
            print("GDTsdk广告关闭")
        # print(a)
        time.sleep(2)
        driver.back()
        time.sleep(2)
        a -= 1


kantu()
driver.back()  # 返回首页
time.sleep(2)

TouchAction(driver).tap(x=588, y=186).perform()  # 返回进入个人中心
time.sleep(2)
TouchAction(driver).tap(x=1275, y=243).perform()
time.sleep(1)
TouchAction(driver).tap(x=707, y=2467).perform()
time.sleep(1)
TouchAction(driver).tap(x=960, y=1440).perform()
BB = mobile + " \033[1;31m账号退出成功\033[0m"
print(BB)
#######################################################################################################################


mobile = "18017700717"  # 卢俊
AA = "\033[1;31mNO.18\033[0m " + mobile + " \033[1;31m开始\033[0m"
print(AA)
nowtime = time.strftime('%Y-%m-%d% %H:%M:%S')
print(nowtime)
time.sleep(5)


def check_login():
    try:
        check_login = driver.find_element_by_id(
            "com.kamitu.drawsth.standalone.free.android:id/iv_mobile_login")  # 选择手机号登录
    except NoSuchElementException:
        print("自动登录成功")
    else:
        TouchAction(driver).tap(x=515, y=2300).perform()
        time.sleep(2)
        el2 = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/edit_phone")  # 选择手机号输入框
        el2.send_keys(mobile)
        time.sleep(2)
        TouchAction(driver).tap(x=1100, y=870).perform()  # 获取验证码
        time.sleep(2)
        # 获取验证码
        logincodeurl = "https://uc.crazyccy.com/login/main_login/testtool?key=sLQq2_jaKLknsqAwZ&type=1&mobile=" + mobile
        # print(logincodeurl)
        request = urllib.request.Request(logincodeurl)  # 构建请求url
        response = urllib.request.urlopen(request, context=context)  # ssl证书免验证加入,context = context# 打开请求url链接
        num = response.read()  # 读取页面返回信息，python3返回数据为bytes类型的对象 (即b为前缀, bytes类型)
        logincode = num.decode()
        if logincode == "查不到！":
            print("获取验证码失败")
            TouchAction(driver).tap(x=1100, y=870).perform()  # 获取验证码
        time.sleep(1)
        el4 = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/edit_identifyCode")  # 选择验证码输入框
        time.sleep(2)
        el4.send_keys(logincode)
        time.sleep(2)
        TouchAction(driver).tap(x=700, y=1200).perform()  # 确定按钮登录
        print("账号登录成功")


check_login()

time.sleep(15)  # 等待10秒加载进入首页


def check_signwindows():  # 检查用户签到弹窗
    try:
        check_signwindows = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/iv_signin_get")
    except NoSuchElementException:
        print("无签到弹窗")
    else:
        TouchAction(driver).tap(x=712, y=1884).perform()
        time.sleep(6)
        TouchAction(driver).tap(x=712, y=852).perform()
        time.sleep(6)
        try:
            GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
        except NoSuchElementException:
            print("toutiaosdk广告")
            time.sleep(40)
            TouchAction(driver).tap(x=1285, y=139).perform()  # 关闭toutiao广告
            print("toutiaosdk广告关闭")
            time.sleep(6)
            TouchAction(driver).tap(x=1254, y=671).perform()  # 关闭加分弹窗
        else:
            print("GDTsdk广告")
            time.sleep(55)
            driver.back()  # GDTsdk广告按钮
            print("GDTsdk广告关闭")
            time.sleep(6)
            TouchAction(driver).tap(x=1254, y=671).perform()  # 关闭加分弹窗


check_signwindows()
time.sleep(3)


def choujiang():
    time.sleep(3)
    TouchAction(driver).tap(x=1285, y=2354).perform()  # 进入抽奖页面
    time.sleep(2)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽10次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽9次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 看广告
    time.sleep(6)
    try:
        GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
    except NoSuchElementException:
        print("toutiaosdk广告")
        time.sleep(40)
        TouchAction(driver).tap(x=1285, y=139).perform()  # 关闭toutiao广告
        print("toutiaosdk广告关闭")
    else:
        print("GDTsdk广告")
        time.sleep(55)
        driver.back()  # GDTsdk广告按钮
        print("GDTsdk广告关闭")
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽8次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽7次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽6次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 看广告
    time.sleep(6)
    try:
        GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
    except NoSuchElementException:
        print("toutiaosdk广告")
        time.sleep(40)
        TouchAction(driver).tap(x=1285, y=139).perform()  # 关闭toutiao广告
        print("toutiaosdk广告关闭")
    else:
        print("GDTsdk广告")
        time.sleep(55)
        driver.back()  # GDTsdk广告按钮
        print("GDTsdk广告关闭")
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽5次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽4次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽3次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽2次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 看广告
    time.sleep(6)
    try:
        GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
    except NoSuchElementException:
        print("toutiaosdk广告")
        time.sleep(40)
        TouchAction(driver).tap(x=1285, y=139).perform()  # 关闭toutiao广告
        print("toutiaosdk广告关闭")
    else:
        print("GDTsdk广告")
        time.sleep(55)
        driver.back()  # GDTsdk广告按钮
        print("GDTsdk广告关闭")
    time.sleep(1)


choujiang()

time.sleep(3)
TouchAction(driver).tap(x=707, y=2070).perform()  # 进入接龙页面
time.sleep(3)
driver.back()
time.sleep(3)


def check_signtoast():  # 检查是否开启签到提示
    try:
        check_signtoast = driver.find_element_by_id(
            "com.kamitu.drawsth.standalone.free.android:id/iv_checkin_reminder_close")
    except NoSuchElementException:
        print("无签到提示")
    else:
        TouchAction(driver).tap(x=1228, y=748).perform()


check_signtoast()
time.sleep(3)


def kantu():
    TouchAction(driver).tap(x=175, y=2385).perform()  # 进入看图猜成语
    time.sleep(3)
    TouchAction(driver).tap(x=475, y=2280).perform()
    time.sleep(1)
    TouchAction(driver).tap(x=1105, y=2188).perform()
    time.sleep(1)
    TouchAction(driver).tap(x=800, y=2280).perform()  # 进入看图使用一次提示
    time.sleep(2)
    TouchAction(driver).tap(x=1000, y=1560).perform()  # 选择右侧提示广告
    driver.back()
    # 广告次数
    a = 6
    while a > 0:
        TouchAction(driver).tap(x=475, y=2280).perform()
        time.sleep(1)
        TouchAction(driver).tap(x=1105, y=2188).perform()
        time.sleep(1)
        TouchAction(driver).tap(x=800, y=2280).perform()  # 选择(位置)
        time.sleep(3)
        TouchAction(driver).tap(x=444, y=1560).perform()  # 选择左侧去除多余选项广告
        print(a)
        time.sleep(6)
        try:
            GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
        except NoSuchElementException:
            print("toutiaosdk广告")
            time.sleep(40)
            TouchAction(driver).tap(x=1285, y=139).perform()  # 关闭toutiao广告
            print("toutiaosdk广告关闭")
        else:
            print("GDTsdk广告")
            time.sleep(55)
            driver.back()  # GDTsdk广告按钮
            print("GDTsdk广告关闭")
        a -= 1
        time.sleep(2)
        TouchAction(driver).tap(x=1000, y=1560).perform()  # 选择右侧提示广告
        print(a)
        time.sleep(6)
        try:
            GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
        except NoSuchElementException:
            print("toutiaosdk广告")
            time.sleep(40)
            TouchAction(driver).tap(x=1285, y=139).perform()  # 关闭toutiao广告
            print("toutiaosdk广告关闭")
        else:
            print("GDTsdk广告")
            time.sleep(55)
            driver.back()  # GDTsdk广告按钮
            print("GDTsdk广告关闭")
        # print(a)
        time.sleep(2)
        driver.back()
        time.sleep(2)
        a -= 1


kantu()
driver.back()  # 返回首页
time.sleep(2)

TouchAction(driver).tap(x=588, y=186).perform()  # 返回进入个人中心
time.sleep(2)
TouchAction(driver).tap(x=1275, y=243).perform()
time.sleep(1)
TouchAction(driver).tap(x=707, y=2467).perform()
time.sleep(1)
TouchAction(driver).tap(x=960, y=1440).perform()
BB = mobile + " \033[1;31m账号退出成功\033[0m"
print(BB)
#######################################################################################################################


mobile = "18017700530"
AA = "\033[1;31mNO.19\033[0m " + mobile + " \033[1;31m开始\033[0m"
print(AA)
nowtime = time.strftime('%Y-%m-%d% %H:%M:%S')
print(nowtime)
time.sleep(5)


def check_login():
    try:
        check_login = driver.find_element_by_id(
            "com.kamitu.drawsth.standalone.free.android:id/iv_mobile_login")  # 选择手机号登录
    except NoSuchElementException:
        print("自动登录成功")
    else:
        TouchAction(driver).tap(x=515, y=2300).perform()
        time.sleep(2)
        el2 = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/edit_phone")  # 选择手机号输入框
        el2.send_keys(mobile)
        time.sleep(2)
        TouchAction(driver).tap(x=1100, y=870).perform()  # 获取验证码
        time.sleep(2)
        # 获取验证码
        logincodeurl = "https://uc.crazyccy.com/login/main_login/testtool?key=sLQq2_jaKLknsqAwZ&type=1&mobile=" + mobile
        # print(logincodeurl)
        request = urllib.request.Request(logincodeurl)  # 构建请求url
        response = urllib.request.urlopen(request, context=context)  # ssl证书免验证加入,context = context# 打开请求url链接
        num = response.read()  # 读取页面返回信息，python3返回数据为bytes类型的对象 (即b为前缀, bytes类型)
        logincode = num.decode()
        if logincode == "查不到！":
            print("获取验证码失败")
            TouchAction(driver).tap(x=1100, y=870).perform()  # 获取验证码
        time.sleep(1)
        el4 = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/edit_identifyCode")  # 选择验证码输入框
        time.sleep(2)
        el4.send_keys(logincode)
        time.sleep(2)
        TouchAction(driver).tap(x=700, y=1200).perform()  # 确定按钮登录
        print("账号登录成功")


check_login()

time.sleep(15)  # 等待10秒加载进入首页


def check_signwindows():  # 检查用户签到弹窗
    try:
        check_signwindows = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/iv_signin_get")
    except NoSuchElementException:
        print("无签到弹窗")
    else:
        TouchAction(driver).tap(x=712, y=1884).perform()
        time.sleep(6)
        TouchAction(driver).tap(x=712, y=852).perform()
        time.sleep(6)
        try:
            GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
        except NoSuchElementException:
            print("toutiaosdk广告")
            time.sleep(40)
            TouchAction(driver).tap(x=1285, y=139).perform()  # 关闭toutiao广告
            print("toutiaosdk广告关闭")
            time.sleep(6)
            TouchAction(driver).tap(x=1254, y=671).perform()  # 关闭加分弹窗
        else:
            print("GDTsdk广告")
            time.sleep(55)
            driver.back()  # GDTsdk广告按钮
            print("GDTsdk广告关闭")
            time.sleep(6)
            TouchAction(driver).tap(x=1254, y=671).perform()  # 关闭加分弹窗


check_signwindows()
time.sleep(3)


def choujiang():
    time.sleep(3)
    TouchAction(driver).tap(x=1285, y=2354).perform()  # 进入抽奖页面
    time.sleep(2)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽10次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽9次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 看广告
    time.sleep(6)
    try:
        GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
    except NoSuchElementException:
        print("toutiaosdk广告")
        time.sleep(40)
        TouchAction(driver).tap(x=1285, y=139).perform()  # 关闭toutiao广告
        print("toutiaosdk广告关闭")
    else:
        print("GDTsdk广告")
        time.sleep(55)
        driver.back()  # GDTsdk广告按钮
        print("GDTsdk广告关闭")
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽8次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽7次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽6次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 看广告
    time.sleep(6)
    try:
        GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
    except NoSuchElementException:
        print("toutiaosdk广告")
        time.sleep(40)
        TouchAction(driver).tap(x=1285, y=139).perform()  # 关闭toutiao广告
        print("toutiaosdk广告关闭")
    else:
        print("GDTsdk广告")
        time.sleep(55)
        driver.back()  # GDTsdk广告按钮
        print("GDTsdk广告关闭")
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽5次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽4次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽3次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽2次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 看广告
    time.sleep(6)
    try:
        GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
    except NoSuchElementException:
        print("toutiaosdk广告")
        time.sleep(40)
        TouchAction(driver).tap(x=1285, y=139).perform()  # 关闭toutiao广告
        print("toutiaosdk广告关闭")
    else:
        print("GDTsdk广告")
        time.sleep(55)
        driver.back()  # GDTsdk广告按钮
        print("GDTsdk广告关闭")
    time.sleep(1)


choujiang()

time.sleep(3)
TouchAction(driver).tap(x=707, y=2070).perform()  # 进入接龙页面
time.sleep(3)
driver.back()
time.sleep(3)


def check_signtoast():  # 检查是否开启签到提示
    try:
        check_signtoast = driver.find_element_by_id(
            "com.kamitu.drawsth.standalone.free.android:id/iv_checkin_reminder_close")
    except NoSuchElementException:
        print("无签到提示")
    else:
        TouchAction(driver).tap(x=1228, y=748).perform()


check_signtoast()
time.sleep(3)


def kantu():
    TouchAction(driver).tap(x=175, y=2385).perform()  # 进入看图猜成语
    time.sleep(3)
    TouchAction(driver).tap(x=475, y=2280).perform()
    time.sleep(1)
    TouchAction(driver).tap(x=1105, y=2188).perform()
    time.sleep(1)
    TouchAction(driver).tap(x=800, y=2280).perform()  # 进入看图使用一次提示
    time.sleep(2)
    TouchAction(driver).tap(x=1000, y=1560).perform()  # 选择右侧提示广告
    driver.back()
    # 广告次数
    a = 6
    while a > 0:
        TouchAction(driver).tap(x=475, y=2280).perform()
        time.sleep(1)
        TouchAction(driver).tap(x=1105, y=2188).perform()
        time.sleep(1)
        TouchAction(driver).tap(x=800, y=2280).perform()  # 选择(位置)
        time.sleep(3)
        TouchAction(driver).tap(x=444, y=1560).perform()  # 选择左侧去除多余选项广告
        print(a)
        time.sleep(6)
        try:
            GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
        except NoSuchElementException:
            print("toutiaosdk广告")
            time.sleep(40)
            TouchAction(driver).tap(x=1285, y=139).perform()  # 关闭toutiao广告
            print("toutiaosdk广告关闭")
        else:
            print("GDTsdk广告")
            time.sleep(55)
            driver.back()  # GDTsdk广告按钮
            print("GDTsdk广告关闭")
        a -= 1
        time.sleep(2)
        TouchAction(driver).tap(x=1000, y=1560).perform()  # 选择右侧提示广告
        print(a)
        time.sleep(6)
        try:
            GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
        except NoSuchElementException:
            print("toutiaosdk广告")
            time.sleep(40)
            TouchAction(driver).tap(x=1285, y=139).perform()  # 关闭toutiao广告
            print("toutiaosdk广告关闭")
        else:
            print("GDTsdk广告")
            time.sleep(55)
            driver.back()  # GDTsdk广告按钮
            print("GDTsdk广告关闭")
        # print(a)
        time.sleep(2)
        driver.back()
        time.sleep(2)
        a -= 1


kantu()
driver.back()  # 返回首页
time.sleep(2)

TouchAction(driver).tap(x=588, y=186).perform()  # 返回进入个人中心
time.sleep(2)
TouchAction(driver).tap(x=1275, y=243).perform()
time.sleep(1)
TouchAction(driver).tap(x=707, y=2467).perform()
time.sleep(1)
TouchAction(driver).tap(x=960, y=1440).perform()
BB = mobile + " \033[1;31m账号退出成功\033[0m"
print(BB)
#######################################################################################################################


mobile = "18017700580"
AA = "\033[1;31mNO.20\033[0m " + mobile + " \033[1;31m开始\033[0m"
print(AA)
nowtime = time.strftime('%Y-%m-%d% %H:%M:%S')
print(nowtime)
time.sleep(5)


def check_login():
    try:
        check_login = driver.find_element_by_id(
            "com.kamitu.drawsth.standalone.free.android:id/iv_mobile_login")  # 选择手机号登录
    except NoSuchElementException:
        print("自动登录成功")
    else:
        TouchAction(driver).tap(x=515, y=2300).perform()
        time.sleep(2)
        el2 = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/edit_phone")  # 选择手机号输入框
        el2.send_keys(mobile)
        time.sleep(2)
        TouchAction(driver).tap(x=1100, y=870).perform()  # 获取验证码
        time.sleep(2)
        # 获取验证码
        logincodeurl = "https://uc.crazyccy.com/login/main_login/testtool?key=sLQq2_jaKLknsqAwZ&type=1&mobile=" + mobile
        # print(logincodeurl)
        request = urllib.request.Request(logincodeurl)  # 构建请求url
        response = urllib.request.urlopen(request, context=context)  # ssl证书免验证加入,context = context# 打开请求url链接
        num = response.read()  # 读取页面返回信息，python3返回数据为bytes类型的对象 (即b为前缀, bytes类型)
        logincode = num.decode()
        if logincode == "查不到！":
            print("获取验证码失败")
            TouchAction(driver).tap(x=1100, y=870).perform()  # 获取验证码
        time.sleep(1)
        el4 = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/edit_identifyCode")  # 选择验证码输入框
        time.sleep(2)
        el4.send_keys(logincode)
        time.sleep(2)
        TouchAction(driver).tap(x=700, y=1200).perform()  # 确定按钮登录
        print("账号登录成功")


check_login()

time.sleep(15)  # 等待10秒加载进入首页


def check_signwindows():  # 检查用户签到弹窗
    try:
        check_signwindows = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/iv_signin_get")
    except NoSuchElementException:
        print("无签到弹窗")
    else:
        TouchAction(driver).tap(x=712, y=1884).perform()
        time.sleep(6)
        TouchAction(driver).tap(x=712, y=852).perform()
        time.sleep(6)
        try:
            GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
        except NoSuchElementException:
            print("toutiaosdk广告")
            time.sleep(40)
            TouchAction(driver).tap(x=1285, y=139).perform()  # 关闭toutiao广告
            print("toutiaosdk广告关闭")
            time.sleep(6)
            TouchAction(driver).tap(x=1254, y=671).perform()  # 关闭加分弹窗
        else:
            print("GDTsdk广告")
            time.sleep(55)
            driver.back()  # GDTsdk广告按钮
            print("GDTsdk广告关闭")
            time.sleep(6)
            TouchAction(driver).tap(x=1254, y=671).perform()  # 关闭加分弹窗


check_signwindows()
time.sleep(3)


def choujiang():
    time.sleep(3)
    TouchAction(driver).tap(x=1285, y=2354).perform()  # 进入抽奖页面
    time.sleep(2)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽10次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽9次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 看广告
    time.sleep(6)
    try:
        GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
    except NoSuchElementException:
        print("toutiaosdk广告")
        time.sleep(40)
        TouchAction(driver).tap(x=1285, y=139).perform()  # 关闭toutiao广告
        print("toutiaosdk广告关闭")
    else:
        print("GDTsdk广告")
        time.sleep(55)
        driver.back()  # GDTsdk广告按钮
        print("GDTsdk广告关闭")
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽8次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽7次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽6次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 看广告
    time.sleep(6)
    try:
        GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
    except NoSuchElementException:
        print("toutiaosdk广告")
        time.sleep(40)
        TouchAction(driver).tap(x=1285, y=139).perform()  # 关闭toutiao广告
        print("toutiaosdk广告关闭")
    else:
        print("GDTsdk广告")
        time.sleep(55)
        driver.back()  # GDTsdk广告按钮
        print("GDTsdk广告关闭")
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽5次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽4次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽3次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽2次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 看广告
    time.sleep(6)
    try:
        GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
    except NoSuchElementException:
        print("toutiaosdk广告")
        time.sleep(40)
        TouchAction(driver).tap(x=1285, y=139).perform()  # 关闭toutiao广告
        print("toutiaosdk广告关闭")
    else:
        print("GDTsdk广告")
        time.sleep(55)
        driver.back()  # GDTsdk广告按钮
        print("GDTsdk广告关闭")
    time.sleep(1)


choujiang()

time.sleep(3)
TouchAction(driver).tap(x=707, y=2070).perform()  # 进入接龙页面
time.sleep(3)
driver.back()
time.sleep(3)


def check_signtoast():  # 检查是否开启签到提示
    try:
        check_signtoast = driver.find_element_by_id(
            "com.kamitu.drawsth.standalone.free.android:id/iv_checkin_reminder_close")
    except NoSuchElementException:
        print("无签到提示")
    else:
        TouchAction(driver).tap(x=1228, y=748).perform()


check_signtoast()
time.sleep(3)


def kantu():
    TouchAction(driver).tap(x=175, y=2385).perform()  # 进入看图猜成语
    time.sleep(3)
    TouchAction(driver).tap(x=475, y=2280).perform()
    time.sleep(1)
    TouchAction(driver).tap(x=1105, y=2188).perform()
    time.sleep(1)
    TouchAction(driver).tap(x=800, y=2280).perform()  # 进入看图使用一次提示
    time.sleep(2)
    TouchAction(driver).tap(x=1000, y=1560).perform()  # 选择右侧提示广告
    driver.back()
    # 广告次数
    a = 6
    while a > 0:
        TouchAction(driver).tap(x=475, y=2280).perform()
        time.sleep(1)
        TouchAction(driver).tap(x=1105, y=2188).perform()
        time.sleep(1)
        TouchAction(driver).tap(x=800, y=2280).perform()  # 选择(位置)
        time.sleep(3)
        TouchAction(driver).tap(x=444, y=1560).perform()  # 选择左侧去除多余选项广告
        print(a)
        time.sleep(6)
        try:
            GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
        except NoSuchElementException:
            print("toutiaosdk广告")
            time.sleep(40)
            TouchAction(driver).tap(x=1285, y=139).perform()  # 关闭toutiao广告
            print("toutiaosdk广告关闭")
        else:
            print("GDTsdk广告")
            time.sleep(55)
            driver.back()  # GDTsdk广告按钮
            print("GDTsdk广告关闭")
        a -= 1
        time.sleep(2)
        TouchAction(driver).tap(x=1000, y=1560).perform()  # 选择右侧提示广告
        print(a)
        time.sleep(6)
        try:
            GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
        except NoSuchElementException:
            print("toutiaosdk广告")
            time.sleep(40)
            TouchAction(driver).tap(x=1285, y=139).perform()  # 关闭toutiao广告
            print("toutiaosdk广告关闭")
        else:
            print("GDTsdk广告")
            time.sleep(55)
            driver.back()  # GDTsdk广告按钮
            print("GDTsdk广告关闭")
        # print(a)
        time.sleep(2)
        driver.back()
        time.sleep(2)
        a -= 1


kantu()
driver.back()  # 返回首页
time.sleep(2)

TouchAction(driver).tap(x=588, y=186).perform()  # 返回进入个人中心
time.sleep(2)
TouchAction(driver).tap(x=1275, y=243).perform()
time.sleep(1)
TouchAction(driver).tap(x=707, y=2467).perform()
time.sleep(1)
TouchAction(driver).tap(x=960, y=1440).perform()
BB = mobile + " \033[1;31m账号退出成功\033[0m"
print(BB)
#######################################################################################################################


mobile = "17502150079"
AA = "\033[1;31mNO.21\033[0m " + mobile + " \033[1;31m开始\033[0m"
print(AA)
nowtime = time.strftime('%Y-%m-%d% %H:%M:%S')
print(nowtime)
time.sleep(5)


def check_login():
    try:
        check_login = driver.find_element_by_id(
            "com.kamitu.drawsth.standalone.free.android:id/iv_mobile_login")  # 选择手机号登录
    except NoSuchElementException:
        print("自动登录成功")
    else:
        TouchAction(driver).tap(x=515, y=2300).perform()
        time.sleep(2)
        el2 = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/edit_phone")  # 选择手机号输入框
        el2.send_keys(mobile)
        time.sleep(2)
        TouchAction(driver).tap(x=1100, y=870).perform()  # 获取验证码
        time.sleep(2)
        # 获取验证码
        logincodeurl = "https://uc.crazyccy.com/login/main_login/testtool?key=sLQq2_jaKLknsqAwZ&type=1&mobile=" + mobile
        # print(logincodeurl)
        request = urllib.request.Request(logincodeurl)  # 构建请求url
        response = urllib.request.urlopen(request, context=context)  # ssl证书免验证加入,context = context# 打开请求url链接
        num = response.read()  # 读取页面返回信息，python3返回数据为bytes类型的对象 (即b为前缀, bytes类型)
        logincode = num.decode()
        if logincode == "查不到！":
            print("获取验证码失败")
            TouchAction(driver).tap(x=1100, y=870).perform()  # 获取验证码
        time.sleep(1)
        el4 = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/edit_identifyCode")  # 选择验证码输入框
        time.sleep(2)
        el4.send_keys(logincode)
        time.sleep(2)
        TouchAction(driver).tap(x=700, y=1200).perform()  # 确定按钮登录
        print("账号登录成功")


check_login()

time.sleep(15)  # 等待10秒加载进入首页


def check_signwindows():  # 检查用户签到弹窗
    try:
        check_signwindows = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/iv_signin_get")
    except NoSuchElementException:
        print("无签到弹窗")
    else:
        TouchAction(driver).tap(x=712, y=1884).perform()
        time.sleep(6)
        TouchAction(driver).tap(x=712, y=852).perform()
        time.sleep(6)
        try:
            GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
        except NoSuchElementException:
            print("toutiaosdk广告")
            time.sleep(40)
            TouchAction(driver).tap(x=1285, y=139).perform()  # 关闭toutiao广告
            print("toutiaosdk广告关闭")
            time.sleep(6)
            TouchAction(driver).tap(x=1254, y=671).perform()  # 关闭加分弹窗
        else:
            print("GDTsdk广告")
            time.sleep(55)
            driver.back()  # GDTsdk广告按钮
            print("GDTsdk广告关闭")
            time.sleep(6)
            TouchAction(driver).tap(x=1254, y=671).perform()  # 关闭加分弹窗


check_signwindows()
time.sleep(3)


def choujiang():
    time.sleep(3)
    TouchAction(driver).tap(x=1285, y=2354).perform()  # 进入抽奖页面
    time.sleep(2)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽10次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽9次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 看广告
    time.sleep(6)
    try:
        GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
    except NoSuchElementException:
        print("toutiaosdk广告")
        time.sleep(40)
        TouchAction(driver).tap(x=1285, y=139).perform()  # 关闭toutiao广告
        print("toutiaosdk广告关闭")
    else:
        print("GDTsdk广告")
        time.sleep(55)
        driver.back()  # GDTsdk广告按钮
        print("GDTsdk广告关闭")
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽8次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽7次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽6次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 看广告
    time.sleep(6)
    try:
        GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
    except NoSuchElementException:
        print("toutiaosdk广告")
        time.sleep(40)
        TouchAction(driver).tap(x=1285, y=139).perform()  # 关闭toutiao广告
        print("toutiaosdk广告关闭")
    else:
        print("GDTsdk广告")
        time.sleep(55)
        driver.back()  # GDTsdk广告按钮
        print("GDTsdk广告关闭")
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽5次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽4次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽3次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽2次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 看广告
    time.sleep(6)
    try:
        GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
    except NoSuchElementException:
        print("toutiaosdk广告")
        time.sleep(40)
        TouchAction(driver).tap(x=1285, y=139).perform()  # 关闭toutiao广告
        print("toutiaosdk广告关闭")
    else:
        print("GDTsdk广告")
        time.sleep(55)
        driver.back()  # GDTsdk广告按钮
        print("GDTsdk广告关闭")
    time.sleep(1)


choujiang()

time.sleep(3)
TouchAction(driver).tap(x=707, y=2070).perform()  # 进入接龙页面
time.sleep(3)
driver.back()
time.sleep(3)


def check_signtoast():  # 检查是否开启签到提示
    try:
        check_signtoast = driver.find_element_by_id(
            "com.kamitu.drawsth.standalone.free.android:id/iv_checkin_reminder_close")
    except NoSuchElementException:
        print("无签到提示")
    else:
        TouchAction(driver).tap(x=1228, y=748).perform()


check_signtoast()
time.sleep(3)


def kantu():
    TouchAction(driver).tap(x=175, y=2385).perform()  # 进入看图猜成语
    time.sleep(3)
    TouchAction(driver).tap(x=475, y=2280).perform()
    time.sleep(1)
    TouchAction(driver).tap(x=1105, y=2188).perform()
    time.sleep(1)
    TouchAction(driver).tap(x=800, y=2280).perform()  # 进入看图使用一次提示
    time.sleep(2)
    TouchAction(driver).tap(x=1000, y=1560).perform()  # 选择右侧提示广告
    driver.back()
    # 广告次数
    a = 6
    while a > 0:
        TouchAction(driver).tap(x=475, y=2280).perform()
        time.sleep(1)
        TouchAction(driver).tap(x=1105, y=2188).perform()
        time.sleep(1)
        TouchAction(driver).tap(x=800, y=2280).perform()  # 选择(位置)
        time.sleep(3)
        TouchAction(driver).tap(x=444, y=1560).perform()  # 选择左侧去除多余选项广告
        print(a)
        time.sleep(6)
        try:
            GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
        except NoSuchElementException:
            print("toutiaosdk广告")
            time.sleep(40)
            TouchAction(driver).tap(x=1285, y=139).perform()  # 关闭toutiao广告
            print("toutiaosdk广告关闭")
        else:
            print("GDTsdk广告")
            time.sleep(55)
            driver.back()  # GDTsdk广告按钮
            print("GDTsdk广告关闭")
        a -= 1
        time.sleep(2)
        TouchAction(driver).tap(x=1000, y=1560).perform()  # 选择右侧提示广告
        print(a)
        time.sleep(6)
        try:
            GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
        except NoSuchElementException:
            print("toutiaosdk广告")
            time.sleep(40)
            TouchAction(driver).tap(x=1285, y=139).perform()  # 关闭toutiao广告
            print("toutiaosdk广告关闭")
        else:
            print("GDTsdk广告")
            time.sleep(55)
            driver.back()  # GDTsdk广告按钮
            print("GDTsdk广告关闭")
        # print(a)
        time.sleep(2)
        driver.back()
        time.sleep(2)
        a -= 1


kantu()
driver.back()  # 返回首页
time.sleep(2)

TouchAction(driver).tap(x=588, y=186).perform()  # 返回进入个人中心
time.sleep(2)
TouchAction(driver).tap(x=1275, y=243).perform()
time.sleep(1)
TouchAction(driver).tap(x=707, y=2467).perform()
time.sleep(1)
TouchAction(driver).tap(x=960, y=1440).perform()
BB = mobile + " \033[1;31m账号退出成功\033[0m"
print(BB)
#######################################################################################################################


mobile = "18930223547"
AA = "\033[1;31mNO.22\033[0m " + mobile + " \033[1;31m开始\033[0m"
print(AA)
nowtime = time.strftime('%Y-%m-%d% %H:%M:%S')
print(nowtime)
time.sleep(5)


def check_login():
    try:
        check_login = driver.find_element_by_id(
            "com.kamitu.drawsth.standalone.free.android:id/iv_mobile_login")  # 选择手机号登录
    except NoSuchElementException:
        print("自动登录成功")
    else:
        TouchAction(driver).tap(x=515, y=2300).perform()
        time.sleep(2)
        el2 = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/edit_phone")  # 选择手机号输入框
        el2.send_keys(mobile)
        time.sleep(2)
        TouchAction(driver).tap(x=1100, y=870).perform()  # 获取验证码
        time.sleep(2)
        # 获取验证码
        logincodeurl = "https://uc.crazyccy.com/login/main_login/testtool?key=sLQq2_jaKLknsqAwZ&type=1&mobile=" + mobile
        # print(logincodeurl)
        request = urllib.request.Request(logincodeurl)  # 构建请求url
        response = urllib.request.urlopen(request, context=context)  # ssl证书免验证加入,context = context# 打开请求url链接
        num = response.read()  # 读取页面返回信息，python3返回数据为bytes类型的对象 (即b为前缀, bytes类型)
        logincode = num.decode()
        if logincode == "查不到！":
            print("获取验证码失败")
            TouchAction(driver).tap(x=1100, y=870).perform()  # 获取验证码
        time.sleep(1)
        el4 = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/edit_identifyCode")  # 选择验证码输入框
        time.sleep(2)
        el4.send_keys(logincode)
        time.sleep(2)
        TouchAction(driver).tap(x=700, y=1200).perform()  # 确定按钮登录
        print("账号登录成功")


check_login()

time.sleep(15)  # 等待10秒加载进入首页


def check_signwindows():  # 检查用户签到弹窗
    try:
        check_signwindows = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/iv_signin_get")
    except NoSuchElementException:
        print("无签到弹窗")
    else:
        TouchAction(driver).tap(x=712, y=1884).perform()
        time.sleep(6)
        TouchAction(driver).tap(x=712, y=852).perform()
        time.sleep(6)
        try:
            GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
        except NoSuchElementException:
            print("toutiaosdk广告")
            time.sleep(40)
            TouchAction(driver).tap(x=1285, y=139).perform()  # 关闭toutiao广告
            print("toutiaosdk广告关闭")
            time.sleep(6)
            TouchAction(driver).tap(x=1254, y=671).perform()  # 关闭加分弹窗
        else:
            print("GDTsdk广告")
            time.sleep(55)
            driver.back()  # GDTsdk广告按钮
            print("GDTsdk广告关闭")
            time.sleep(6)
            TouchAction(driver).tap(x=1254, y=671).perform()  # 关闭加分弹窗


check_signwindows()
time.sleep(3)


def choujiang():
    time.sleep(3)
    TouchAction(driver).tap(x=1285, y=2354).perform()  # 进入抽奖页面
    time.sleep(2)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽10次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽9次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 看广告
    time.sleep(6)
    try:
        GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
    except NoSuchElementException:
        print("toutiaosdk广告")
        time.sleep(40)
        TouchAction(driver).tap(x=1285, y=139).perform()  # 关闭toutiao广告
        print("toutiaosdk广告关闭")
    else:
        print("GDTsdk广告")
        time.sleep(55)
        driver.back()  # GDTsdk广告按钮
        print("GDTsdk广告关闭")
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽8次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽7次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽6次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 看广告
    time.sleep(6)
    try:
        GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
    except NoSuchElementException:
        print("toutiaosdk广告")
        time.sleep(40)
        TouchAction(driver).tap(x=1285, y=139).perform()  # 关闭toutiao广告
        print("toutiaosdk广告关闭")
    else:
        print("GDTsdk广告")
        time.sleep(55)
        driver.back()  # GDTsdk广告按钮
        print("GDTsdk广告关闭")
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽5次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽4次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽3次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽2次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 看广告
    time.sleep(6)
    try:
        GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
    except NoSuchElementException:
        print("toutiaosdk广告")
        time.sleep(40)
        TouchAction(driver).tap(x=1285, y=139).perform()  # 关闭toutiao广告
        print("toutiaosdk广告关闭")
    else:
        print("GDTsdk广告")
        time.sleep(55)
        driver.back()  # GDTsdk广告按钮
        print("GDTsdk广告关闭")
    time.sleep(1)


choujiang()

time.sleep(3)
TouchAction(driver).tap(x=707, y=2070).perform()  # 进入接龙页面
time.sleep(3)
driver.back()
time.sleep(3)


def check_signtoast():  # 检查是否开启签到提示
    try:
        check_signtoast = driver.find_element_by_id(
            "com.kamitu.drawsth.standalone.free.android:id/iv_checkin_reminder_close")
    except NoSuchElementException:
        print("无签到提示")
    else:
        TouchAction(driver).tap(x=1228, y=748).perform()


check_signtoast()
time.sleep(3)


def kantu():
    TouchAction(driver).tap(x=175, y=2385).perform()  # 进入看图猜成语
    time.sleep(3)
    TouchAction(driver).tap(x=475, y=2280).perform()
    time.sleep(1)
    TouchAction(driver).tap(x=1105, y=2188).perform()
    time.sleep(1)
    TouchAction(driver).tap(x=800, y=2280).perform()  # 进入看图使用一次提示
    time.sleep(2)
    TouchAction(driver).tap(x=1000, y=1560).perform()  # 选择右侧提示广告
    driver.back()
    # 广告次数
    a = 6
    while a > 0:
        TouchAction(driver).tap(x=475, y=2280).perform()
        time.sleep(1)
        TouchAction(driver).tap(x=1105, y=2188).perform()
        time.sleep(1)
        TouchAction(driver).tap(x=800, y=2280).perform()  # 选择(位置)
        time.sleep(3)
        TouchAction(driver).tap(x=444, y=1560).perform()  # 选择左侧去除多余选项广告
        print(a)
        time.sleep(6)
        try:
            GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
        except NoSuchElementException:
            print("toutiaosdk广告")
            time.sleep(40)
            TouchAction(driver).tap(x=1285, y=139).perform()  # 关闭toutiao广告
            print("toutiaosdk广告关闭")
        else:
            print("GDTsdk广告")
            time.sleep(55)
            driver.back()  # GDTsdk广告按钮
            print("GDTsdk广告关闭")
        a -= 1
        time.sleep(2)
        TouchAction(driver).tap(x=1000, y=1560).perform()  # 选择右侧提示广告
        print(a)
        time.sleep(6)
        try:
            GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
        except NoSuchElementException:
            print("toutiaosdk广告")
            time.sleep(40)
            TouchAction(driver).tap(x=1285, y=139).perform()  # 关闭toutiao广告
            print("toutiaosdk广告关闭")
        else:
            print("GDTsdk广告")
            time.sleep(55)
            driver.back()  # GDTsdk广告按钮
            print("GDTsdk广告关闭")
        # print(a)
        time.sleep(2)
        driver.back()
        time.sleep(2)
        a -= 1


kantu()
driver.back()  # 返回首页
time.sleep(2)

TouchAction(driver).tap(x=588, y=186).perform()  # 返回进入个人中心
time.sleep(2)
TouchAction(driver).tap(x=1275, y=243).perform()
time.sleep(1)
TouchAction(driver).tap(x=707, y=2467).perform()
time.sleep(1)
TouchAction(driver).tap(x=960, y=1440).perform()
BB = mobile + " \033[1;31m账号退出成功\033[0m"
print(BB)
#######################################################################################################################


mobile = "15606566329"
AA = "\033[1;31mNO.23\033[0m " + mobile + " \033[1;31m开始\033[0m"
print(AA)
nowtime = time.strftime('%Y-%m-%d% %H:%M:%S')
print(nowtime)
time.sleep(5)


def check_login():
    try:
        check_login = driver.find_element_by_id(
            "com.kamitu.drawsth.standalone.free.android:id/iv_mobile_login")  # 选择手机号登录
    except NoSuchElementException:
        print("自动登录成功")
    else:
        TouchAction(driver).tap(x=515, y=2300).perform()
        time.sleep(2)
        el2 = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/edit_phone")  # 选择手机号输入框
        el2.send_keys(mobile)
        time.sleep(2)
        TouchAction(driver).tap(x=1100, y=870).perform()  # 获取验证码
        time.sleep(2)
        # 获取验证码
        logincodeurl = "https://uc.crazyccy.com/login/main_login/testtool?key=sLQq2_jaKLknsqAwZ&type=1&mobile=" + mobile
        # print(logincodeurl)
        request = urllib.request.Request(logincodeurl)  # 构建请求url
        response = urllib.request.urlopen(request, context=context)  # ssl证书免验证加入,context = context# 打开请求url链接
        num = response.read()  # 读取页面返回信息，python3返回数据为bytes类型的对象 (即b为前缀, bytes类型)
        logincode = num.decode()
        if logincode == "查不到！":
            print("获取验证码失败")
            TouchAction(driver).tap(x=1100, y=870).perform()  # 获取验证码
        time.sleep(1)
        el4 = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/edit_identifyCode")  # 选择验证码输入框
        time.sleep(2)
        el4.send_keys(logincode)
        time.sleep(2)
        TouchAction(driver).tap(x=700, y=1200).perform()  # 确定按钮登录
        print("账号登录成功")


check_login()

time.sleep(15)  # 等待10秒加载进入首页


def check_signwindows():  # 检查用户签到弹窗
    try:
        check_signwindows = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/iv_signin_get")
    except NoSuchElementException:
        print("无签到弹窗")
    else:
        TouchAction(driver).tap(x=712, y=1884).perform()
        time.sleep(6)
        TouchAction(driver).tap(x=712, y=852).perform()
        time.sleep(6)
        try:
            GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
        except NoSuchElementException:
            print("toutiaosdk广告")
            time.sleep(40)
            TouchAction(driver).tap(x=1285, y=139).perform()  # 关闭toutiao广告
            print("toutiaosdk广告关闭")
            time.sleep(6)
            TouchAction(driver).tap(x=1254, y=671).perform()  # 关闭加分弹窗
        else:
            print("GDTsdk广告")
            time.sleep(55)
            driver.back()  # GDTsdk广告按钮
            print("GDTsdk广告关闭")
            time.sleep(6)
            TouchAction(driver).tap(x=1254, y=671).perform()  # 关闭加分弹窗


check_signwindows()
time.sleep(3)


def choujiang():
    time.sleep(3)
    TouchAction(driver).tap(x=1285, y=2354).perform()  # 进入抽奖页面
    time.sleep(2)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽10次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽9次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 看广告
    time.sleep(6)
    try:
        GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
    except NoSuchElementException:
        print("toutiaosdk广告")
        time.sleep(40)
        TouchAction(driver).tap(x=1285, y=139).perform()  # 关闭toutiao广告
        print("toutiaosdk广告关闭")
    else:
        print("GDTsdk广告")
        time.sleep(55)
        driver.back()  # GDTsdk广告按钮
        print("GDTsdk广告关闭")
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽8次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽7次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽6次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 看广告
    time.sleep(6)
    try:
        GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
    except NoSuchElementException:
        print("toutiaosdk广告")
        time.sleep(40)
        TouchAction(driver).tap(x=1285, y=139).perform()  # 关闭toutiao广告
        print("toutiaosdk广告关闭")
    else:
        print("GDTsdk广告")
        time.sleep(55)
        driver.back()  # GDTsdk广告按钮
        print("GDTsdk广告关闭")
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽5次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽4次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽3次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽2次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 看广告
    time.sleep(6)
    try:
        GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
    except NoSuchElementException:
        print("toutiaosdk广告")
        time.sleep(40)
        TouchAction(driver).tap(x=1285, y=139).perform()  # 关闭toutiao广告
        print("toutiaosdk广告关闭")
    else:
        print("GDTsdk广告")
        time.sleep(55)
        driver.back()  # GDTsdk广告按钮
        print("GDTsdk广告关闭")
    time.sleep(1)


choujiang()

time.sleep(3)
TouchAction(driver).tap(x=707, y=2070).perform()  # 进入接龙页面
time.sleep(3)
driver.back()
time.sleep(3)


def check_signtoast():  # 检查是否开启签到提示
    try:
        check_signtoast = driver.find_element_by_id(
            "com.kamitu.drawsth.standalone.free.android:id/iv_checkin_reminder_close")
    except NoSuchElementException:
        print("无签到提示")
    else:
        TouchAction(driver).tap(x=1228, y=748).perform()


check_signtoast()
time.sleep(3)


def kantu():
    TouchAction(driver).tap(x=175, y=2385).perform()  # 进入看图猜成语
    time.sleep(3)
    TouchAction(driver).tap(x=475, y=2280).perform()
    time.sleep(1)
    TouchAction(driver).tap(x=1105, y=2188).perform()
    time.sleep(1)
    TouchAction(driver).tap(x=800, y=2280).perform()  # 进入看图使用一次提示
    time.sleep(2)
    TouchAction(driver).tap(x=1000, y=1560).perform()  # 选择右侧提示广告
    driver.back()
    # 广告次数
    a = 6
    while a > 0:
        TouchAction(driver).tap(x=475, y=2280).perform()
        time.sleep(1)
        TouchAction(driver).tap(x=1105, y=2188).perform()
        time.sleep(1)
        TouchAction(driver).tap(x=800, y=2280).perform()  # 选择(位置)
        time.sleep(3)
        TouchAction(driver).tap(x=444, y=1560).perform()  # 选择左侧去除多余选项广告
        print(a)
        time.sleep(6)
        try:
            GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
        except NoSuchElementException:
            print("toutiaosdk广告")
            time.sleep(40)
            TouchAction(driver).tap(x=1285, y=139).perform()  # 关闭toutiao广告
            print("toutiaosdk广告关闭")
        else:
            print("GDTsdk广告")
            time.sleep(55)
            driver.back()  # GDTsdk广告按钮
            print("GDTsdk广告关闭")
        a -= 1
        time.sleep(2)
        TouchAction(driver).tap(x=1000, y=1560).perform()  # 选择右侧提示广告
        print(a)
        time.sleep(6)
        try:
            GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
        except NoSuchElementException:
            print("toutiaosdk广告")
            time.sleep(40)
            TouchAction(driver).tap(x=1285, y=139).perform()  # 关闭toutiao广告
            print("toutiaosdk广告关闭")
        else:
            print("GDTsdk广告")
            time.sleep(55)
            driver.back()  # GDTsdk广告按钮
            print("GDTsdk广告关闭")
        # print(a)
        time.sleep(2)
        driver.back()
        time.sleep(2)
        a -= 1


kantu()
driver.back()  # 返回首页
time.sleep(2)

TouchAction(driver).tap(x=588, y=186).perform()  # 返回进入个人中心
time.sleep(2)
TouchAction(driver).tap(x=1275, y=243).perform()
time.sleep(1)
TouchAction(driver).tap(x=707, y=2467).perform()
time.sleep(1)
TouchAction(driver).tap(x=960, y=1440).perform()
BB = mobile + " \033[1;31m账号退出成功\033[0m"
print(BB)
#######################################################################################################################


mobile = "18017700710"
AA = "\033[1;31mNO.24\033[0m " + mobile + " \033[1;31m开始\033[0m"
print(AA)
nowtime = time.strftime('%Y-%m-%d% %H:%M:%S')
print(nowtime)
time.sleep(5)


def check_login():
    try:
        check_login = driver.find_element_by_id(
            "com.kamitu.drawsth.standalone.free.android:id/iv_mobile_login")  # 选择手机号登录
    except NoSuchElementException:
        print("自动登录成功")
    else:
        TouchAction(driver).tap(x=515, y=2300).perform()
        time.sleep(2)
        el2 = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/edit_phone")  # 选择手机号输入框
        el2.send_keys(mobile)
        time.sleep(2)
        TouchAction(driver).tap(x=1100, y=870).perform()  # 获取验证码
        time.sleep(2)
        # 获取验证码
        logincodeurl = "https://uc.crazyccy.com/login/main_login/testtool?key=sLQq2_jaKLknsqAwZ&type=1&mobile=" + mobile
        # print(logincodeurl)
        request = urllib.request.Request(logincodeurl)  # 构建请求url
        response = urllib.request.urlopen(request, context=context)  # ssl证书免验证加入,context = context# 打开请求url链接
        num = response.read()  # 读取页面返回信息，python3返回数据为bytes类型的对象 (即b为前缀, bytes类型)
        logincode = num.decode()
        if logincode == "查不到！":
            print("获取验证码失败")
            TouchAction(driver).tap(x=1100, y=870).perform()  # 获取验证码
        time.sleep(1)
        el4 = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/edit_identifyCode")  # 选择验证码输入框
        time.sleep(2)
        el4.send_keys(logincode)
        time.sleep(2)
        TouchAction(driver).tap(x=700, y=1200).perform()  # 确定按钮登录
        print("账号登录成功")


check_login()

time.sleep(15)  # 等待10秒加载进入首页


def check_signwindows():  # 检查用户签到弹窗
    try:
        check_signwindows = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/iv_signin_get")
    except NoSuchElementException:
        print("无签到弹窗")
    else:
        TouchAction(driver).tap(x=712, y=1884).perform()
        time.sleep(6)
        TouchAction(driver).tap(x=712, y=852).perform()
        time.sleep(6)
        try:
            GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
        except NoSuchElementException:
            print("toutiaosdk广告")
            time.sleep(40)
            TouchAction(driver).tap(x=1285, y=139).perform()  # 关闭toutiao广告
            print("toutiaosdk广告关闭")
            time.sleep(6)
            TouchAction(driver).tap(x=1254, y=671).perform()  # 关闭加分弹窗
        else:
            print("GDTsdk广告")
            time.sleep(55)
            driver.back()  # GDTsdk广告按钮
            print("GDTsdk广告关闭")
            time.sleep(6)
            TouchAction(driver).tap(x=1254, y=671).perform()  # 关闭加分弹窗


check_signwindows()
time.sleep(3)


def choujiang():
    time.sleep(3)
    TouchAction(driver).tap(x=1285, y=2354).perform()  # 进入抽奖页面
    time.sleep(2)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽10次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽9次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 看广告
    time.sleep(6)
    try:
        GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
    except NoSuchElementException:
        print("toutiaosdk广告")
        time.sleep(40)
        TouchAction(driver).tap(x=1285, y=139).perform()  # 关闭toutiao广告
        print("toutiaosdk广告关闭")
    else:
        print("GDTsdk广告")
        time.sleep(55)
        driver.back()  # GDTsdk广告按钮
        print("GDTsdk广告关闭")
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽8次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽7次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽6次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 看广告
    time.sleep(6)
    try:
        GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
    except NoSuchElementException:
        print("toutiaosdk广告")
        time.sleep(40)
        TouchAction(driver).tap(x=1285, y=139).perform()  # 关闭toutiao广告
        print("toutiaosdk广告关闭")
    else:
        print("GDTsdk广告")
        time.sleep(55)
        driver.back()  # GDTsdk广告按钮
        print("GDTsdk广告关闭")
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽5次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽4次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽3次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽2次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 看广告
    time.sleep(6)
    try:
        GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
    except NoSuchElementException:
        print("toutiaosdk广告")
        time.sleep(40)
        TouchAction(driver).tap(x=1285, y=139).perform()  # 关闭toutiao广告
        print("toutiaosdk广告关闭")
    else:
        print("GDTsdk广告")
        time.sleep(55)
        driver.back()  # GDTsdk广告按钮
        print("GDTsdk广告关闭")
    time.sleep(1)


choujiang()

time.sleep(3)
TouchAction(driver).tap(x=707, y=2070).perform()  # 进入接龙页面
time.sleep(3)
driver.back()
time.sleep(3)


def check_signtoast():  # 检查是否开启签到提示
    try:
        check_signtoast = driver.find_element_by_id(
            "com.kamitu.drawsth.standalone.free.android:id/iv_checkin_reminder_close")
    except NoSuchElementException:
        print("无签到提示")
    else:
        TouchAction(driver).tap(x=1228, y=748).perform()


check_signtoast()
time.sleep(3)


def kantu():
    TouchAction(driver).tap(x=175, y=2385).perform()  # 进入看图猜成语
    time.sleep(3)
    TouchAction(driver).tap(x=475, y=2280).perform()
    time.sleep(1)
    TouchAction(driver).tap(x=1105, y=2188).perform()
    time.sleep(1)
    TouchAction(driver).tap(x=800, y=2280).perform()  # 进入看图使用一次提示
    time.sleep(2)
    TouchAction(driver).tap(x=1000, y=1560).perform()  # 选择右侧提示广告
    driver.back()
    # 广告次数
    a = 6
    while a > 0:
        TouchAction(driver).tap(x=475, y=2280).perform()
        time.sleep(1)
        TouchAction(driver).tap(x=1105, y=2188).perform()
        time.sleep(1)
        TouchAction(driver).tap(x=800, y=2280).perform()  # 选择(位置)
        time.sleep(3)
        TouchAction(driver).tap(x=444, y=1560).perform()  # 选择左侧去除多余选项广告
        print(a)
        time.sleep(6)
        try:
            GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
        except NoSuchElementException:
            print("toutiaosdk广告")
            time.sleep(40)
            TouchAction(driver).tap(x=1285, y=139).perform()  # 关闭toutiao广告
            print("toutiaosdk广告关闭")
        else:
            print("GDTsdk广告")
            time.sleep(55)
            driver.back()  # GDTsdk广告按钮
            print("GDTsdk广告关闭")
        a -= 1
        time.sleep(2)
        TouchAction(driver).tap(x=1000, y=1560).perform()  # 选择右侧提示广告
        print(a)
        time.sleep(6)
        try:
            GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
        except NoSuchElementException:
            print("toutiaosdk广告")
            time.sleep(40)
            TouchAction(driver).tap(x=1285, y=139).perform()  # 关闭toutiao广告
            print("toutiaosdk广告关闭")
        else:
            print("GDTsdk广告")
            time.sleep(55)
            driver.back()  # GDTsdk广告按钮
            print("GDTsdk广告关闭")
        # print(a)
        time.sleep(2)
        driver.back()
        time.sleep(2)
        a -= 1


kantu()
driver.back()  # 返回首页
time.sleep(2)

TouchAction(driver).tap(x=588, y=186).perform()  # 返回进入个人中心
time.sleep(2)
TouchAction(driver).tap(x=1275, y=243).perform()
time.sleep(1)
TouchAction(driver).tap(x=707, y=2467).perform()
time.sleep(1)
TouchAction(driver).tap(x=960, y=1440).perform()
BB = mobile + " \033[1;31m账号退出成功\033[0m"
print(BB)
#######################################################################################################################


mobile = "18017700722"
AA = "\033[1;31mNO.25\033[0m " + mobile + " \033[1;31m开始\033[0m"

print(AA)
nowtime = time.strftime('%Y-%m-%d% %H:%M:%S')
print(nowtime)
time.sleep(5)


def check_login():
    try:
        check_login = driver.find_element_by_id(
            "com.kamitu.drawsth.standalone.free.android:id/iv_mobile_login")  # 选择手机号登录
    except NoSuchElementException:
        print("自动登录成功")
    else:
        TouchAction(driver).tap(x=515, y=2300).perform()
        time.sleep(2)
        el2 = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/edit_phone")  # 选择手机号输入框
        el2.send_keys(mobile)
        time.sleep(2)
        TouchAction(driver).tap(x=1100, y=870).perform()  # 获取验证码
        time.sleep(2)
        # 获取验证码
        logincodeurl = "https://uc.crazyccy.com/login/main_login/testtool?key=sLQq2_jaKLknsqAwZ&type=1&mobile=" + mobile
        # print(logincodeurl)
        request = urllib.request.Request(logincodeurl)  # 构建请求url
        response = urllib.request.urlopen(request, context=context)  # ssl证书免验证加入,context = context# 打开请求url链接
        num = response.read()  # 读取页面返回信息，python3返回数据为bytes类型的对象 (即b为前缀, bytes类型)
        logincode = num.decode()
        if logincode == "查不到！":
            print("获取验证码失败")
            TouchAction(driver).tap(x=1100, y=870).perform()  # 获取验证码
        time.sleep(1)
        el4 = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/edit_identifyCode")  # 选择验证码输入框
        time.sleep(2)
        el4.send_keys(logincode)
        time.sleep(2)
        TouchAction(driver).tap(x=700, y=1200).perform()  # 确定按钮登录
        print("账号登录成功")


check_login()

time.sleep(15)  # 等待10秒加载进入首页


def check_signwindows():  # 检查用户签到弹窗
    try:
        check_signwindows = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/iv_signin_get")
    except NoSuchElementException:
        print("无签到弹窗")
    else:
        TouchAction(driver).tap(x=712, y=1884).perform()
        time.sleep(6)
        TouchAction(driver).tap(x=712, y=852).perform()
        time.sleep(6)
        try:
            GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
        except NoSuchElementException:
            print("toutiaosdk广告")
            time.sleep(40)
            TouchAction(driver).tap(x=1285, y=139).perform()  # 关闭toutiao广告
            print("toutiaosdk广告关闭")
            time.sleep(6)
            TouchAction(driver).tap(x=1254, y=671).perform()  # 关闭加分弹窗
        else:
            print("GDTsdk广告")
            time.sleep(55)
            driver.back()  # GDTsdk广告按钮
            print("GDTsdk广告关闭")
            time.sleep(6)
            TouchAction(driver).tap(x=1254, y=671).perform()  # 关闭加分弹窗


check_signwindows()
time.sleep(3)


def choujiang():
    time.sleep(3)
    TouchAction(driver).tap(x=1285, y=2354).perform()  # 进入抽奖页面
    time.sleep(2)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽10次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽9次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 看广告
    time.sleep(6)
    try:
        GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
    except NoSuchElementException:
        print("toutiaosdk广告")
        time.sleep(40)
        TouchAction(driver).tap(x=1285, y=139).perform()  # 关闭toutiao广告
        print("toutiaosdk广告关闭")
    else:
        print("GDTsdk广告")
        time.sleep(55)
        driver.back()  # GDTsdk广告按钮
        print("GDTsdk广告关闭")
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽8次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽7次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽6次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 看广告
    time.sleep(6)
    try:
        GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
    except NoSuchElementException:
        print("toutiaosdk广告")
        time.sleep(40)
        TouchAction(driver).tap(x=1285, y=139).perform()  # 关闭toutiao广告
        print("toutiaosdk广告关闭")
    else:
        print("GDTsdk广告")
        time.sleep(55)
        driver.back()  # GDTsdk广告按钮
        print("GDTsdk广告关闭")
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽5次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽4次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽3次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽2次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 看广告
    time.sleep(6)
    try:
        GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
    except NoSuchElementException:
        print("toutiaosdk广告")
        time.sleep(40)
        TouchAction(driver).tap(x=1285, y=139).perform()  # 关闭toutiao广告
        print("toutiaosdk广告关闭")
    else:
        print("GDTsdk广告")
        time.sleep(55)
        driver.back()  # GDTsdk广告按钮
        print("GDTsdk广告关闭")
    time.sleep(1)


choujiang()

time.sleep(3)
TouchAction(driver).tap(x=707, y=2070).perform()  # 进入接龙页面
time.sleep(3)
driver.back()
time.sleep(3)


def check_signtoast():  # 检查是否开启签到提示
    try:
        check_signtoast = driver.find_element_by_id(
            "com.kamitu.drawsth.standalone.free.android:id/iv_checkin_reminder_close")
    except NoSuchElementException:
        print("无签到提示")
    else:
        TouchAction(driver).tap(x=1228, y=748).perform()


check_signtoast()
time.sleep(3)


def kantu():
    TouchAction(driver).tap(x=175, y=2385).perform()  # 进入看图猜成语
    time.sleep(3)
    TouchAction(driver).tap(x=475, y=2280).perform()
    time.sleep(1)
    TouchAction(driver).tap(x=1105, y=2188).perform()
    time.sleep(1)
    TouchAction(driver).tap(x=800, y=2280).perform()  # 进入看图使用一次提示
    time.sleep(2)
    TouchAction(driver).tap(x=1000, y=1560).perform()  # 选择右侧提示广告
    driver.back()
    # 广告次数
    a = 6
    while a > 0:
        TouchAction(driver).tap(x=475, y=2280).perform()
        time.sleep(1)
        TouchAction(driver).tap(x=1105, y=2188).perform()
        time.sleep(1)
        TouchAction(driver).tap(x=800, y=2280).perform()  # 选择(位置)
        time.sleep(3)
        TouchAction(driver).tap(x=444, y=1560).perform()  # 选择左侧去除多余选项广告
        print(a)
        time.sleep(6)
        try:
            GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
        except NoSuchElementException:
            print("toutiaosdk广告")
            time.sleep(40)
            TouchAction(driver).tap(x=1285, y=139).perform()  # 关闭toutiao广告
            print("toutiaosdk广告关闭")
        else:
            print("GDTsdk广告")
            time.sleep(55)
            driver.back()  # GDTsdk广告按钮
            print("GDTsdk广告关闭")
        a -= 1
        time.sleep(2)
        TouchAction(driver).tap(x=1000, y=1560).perform()  # 选择右侧提示广告
        print(a)
        time.sleep(6)
        try:
            GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
        except NoSuchElementException:
            print("toutiaosdk广告")
            time.sleep(40)
            TouchAction(driver).tap(x=1285, y=139).perform()  # 关闭toutiao广告
            print("toutiaosdk广告关闭")
        else:
            print("GDTsdk广告")
            time.sleep(55)
            driver.back()  # GDTsdk广告按钮
            print("GDTsdk广告关闭")
        # print(a)
        time.sleep(2)
        driver.back()
        time.sleep(2)
        a -= 1


kantu()
driver.back()  # 返回首页
time.sleep(2)

TouchAction(driver).tap(x=588, y=186).perform()  # 返回进入个人中心
time.sleep(2)
TouchAction(driver).tap(x=1275, y=243).perform()
time.sleep(1)
TouchAction(driver).tap(x=707, y=2467).perform()
time.sleep(1)
TouchAction(driver).tap(x=960, y=1440).perform()
BB = mobile + " \033[1;31m账号退出成功\033[0m"
print(BB)
#######################################################################################################################


mobile = "18017700339"
AA = "\033[1;31mNO.26\033[0m " + mobile + " \033[1;31m开始\033[0m"
print(AA)
nowtime = time.strftime('%Y-%m-%d% %H:%M:%S')
print(nowtime)
time.sleep(5)


def check_login():
    try:
        check_login = driver.find_element_by_id(
            "com.kamitu.drawsth.standalone.free.android:id/iv_mobile_login")  # 选择手机号登录
    except NoSuchElementException:
        print("自动登录成功")
    else:
        TouchAction(driver).tap(x=515, y=2300).perform()
        time.sleep(2)
        el2 = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/edit_phone")  # 选择手机号输入框
        el2.send_keys(mobile)
        time.sleep(2)
        TouchAction(driver).tap(x=1100, y=870).perform()  # 获取验证码
        time.sleep(2)
        # 获取验证码
        logincodeurl = "https://uc.crazyccy.com/login/main_login/testtool?key=sLQq2_jaKLknsqAwZ&type=1&mobile=" + mobile
        # print(logincodeurl)
        request = urllib.request.Request(logincodeurl)  # 构建请求url
        response = urllib.request.urlopen(request, context=context)  # ssl证书免验证加入,context = context# 打开请求url链接
        num = response.read()  # 读取页面返回信息，python3返回数据为bytes类型的对象 (即b为前缀, bytes类型)
        logincode = num.decode()
        if logincode == "查不到！":
            print("获取验证码失败")
            TouchAction(driver).tap(x=1100, y=870).perform()  # 获取验证码
        time.sleep(1)
        el4 = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/edit_identifyCode")  # 选择验证码输入框
        time.sleep(2)
        el4.send_keys(logincode)
        time.sleep(2)
        TouchAction(driver).tap(x=700, y=1200).perform()  # 确定按钮登录
        print("账号登录成功")


check_login()

time.sleep(15)  # 等待10秒加载进入首页


def check_signwindows():  # 检查用户签到弹窗
    try:
        check_signwindows = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/iv_signin_get")
    except NoSuchElementException:
        print("无签到弹窗")
    else:
        TouchAction(driver).tap(x=712, y=1884).perform()
        time.sleep(6)
        TouchAction(driver).tap(x=712, y=852).perform()
        time.sleep(6)
        try:
            GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
        except NoSuchElementException:
            print("toutiaosdk广告")
            time.sleep(40)
            TouchAction(driver).tap(x=1285, y=139).perform()  # 关闭toutiao广告
            print("toutiaosdk广告关闭")
            time.sleep(6)
            TouchAction(driver).tap(x=1254, y=671).perform()  # 关闭加分弹窗
        else:
            print("GDTsdk广告")
            time.sleep(55)
            driver.back()  # GDTsdk广告按钮
            print("GDTsdk广告关闭")
            time.sleep(6)
            TouchAction(driver).tap(x=1254, y=671).perform()  # 关闭加分弹窗


check_signwindows()
time.sleep(3)


def choujiang():
    time.sleep(3)
    TouchAction(driver).tap(x=1285, y=2354).perform()  # 进入抽奖页面
    time.sleep(2)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽10次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽9次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 看广告
    time.sleep(6)
    try:
        GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
    except NoSuchElementException:
        print("toutiaosdk广告")
        time.sleep(40)
        TouchAction(driver).tap(x=1285, y=139).perform()  # 关闭toutiao广告
        print("toutiaosdk广告关闭")
    else:
        print("GDTsdk广告")
        time.sleep(55)
        driver.back()  # GDTsdk广告按钮
        print("GDTsdk广告关闭")
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽8次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽7次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽6次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 看广告
    time.sleep(6)
    try:
        GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
    except NoSuchElementException:
        print("toutiaosdk广告")
        time.sleep(40)
        TouchAction(driver).tap(x=1285, y=139).perform()  # 关闭toutiao广告
        print("toutiaosdk广告关闭")
    else:
        print("GDTsdk广告")
        time.sleep(55)
        driver.back()  # GDTsdk广告按钮
        print("GDTsdk广告关闭")
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽5次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽4次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽3次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽2次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 看广告
    time.sleep(6)
    try:
        GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
    except NoSuchElementException:
        print("toutiaosdk广告")
        time.sleep(40)
        TouchAction(driver).tap(x=1285, y=139).perform()  # 关闭toutiao广告
        print("toutiaosdk广告关闭")
    else:
        print("GDTsdk广告")
        time.sleep(55)
        driver.back()  # GDTsdk广告按钮
        print("GDTsdk广告关闭")
    time.sleep(1)


choujiang()

time.sleep(3)
TouchAction(driver).tap(x=707, y=2070).perform()  # 进入接龙页面
time.sleep(3)
driver.back()
time.sleep(3)


def check_signtoast():  # 检查是否开启签到提示
    try:
        check_signtoast = driver.find_element_by_id(
            "com.kamitu.drawsth.standalone.free.android:id/iv_checkin_reminder_close")
    except NoSuchElementException:
        print("无签到提示")
    else:
        TouchAction(driver).tap(x=1228, y=748).perform()


check_signtoast()
time.sleep(3)


def kantu():
    TouchAction(driver).tap(x=175, y=2385).perform()  # 进入看图猜成语
    time.sleep(3)
    TouchAction(driver).tap(x=475, y=2280).perform()
    time.sleep(1)
    TouchAction(driver).tap(x=1105, y=2188).perform()
    time.sleep(1)
    TouchAction(driver).tap(x=800, y=2280).perform()  # 进入看图使用一次提示
    time.sleep(2)
    TouchAction(driver).tap(x=1000, y=1560).perform()  # 选择右侧提示广告
    driver.back()
    # 广告次数
    a = 6
    while a > 0:
        TouchAction(driver).tap(x=475, y=2280).perform()
        time.sleep(1)
        TouchAction(driver).tap(x=1105, y=2188).perform()
        time.sleep(1)
        TouchAction(driver).tap(x=800, y=2280).perform()  # 选择(位置)
        time.sleep(3)
        TouchAction(driver).tap(x=444, y=1560).perform()  # 选择左侧去除多余选项广告
        print(a)
        time.sleep(6)
        try:
            GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
        except NoSuchElementException:
            print("toutiaosdk广告")
            time.sleep(40)
            TouchAction(driver).tap(x=1285, y=139).perform()  # 关闭toutiao广告
            print("toutiaosdk广告关闭")
        else:
            print("GDTsdk广告")
            time.sleep(55)
            driver.back()  # GDTsdk广告按钮
            print("GDTsdk广告关闭")
        a -= 1
        time.sleep(2)
        TouchAction(driver).tap(x=1000, y=1560).perform()  # 选择右侧提示广告
        print(a)
        time.sleep(6)
        try:
            GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
        except NoSuchElementException:
            print("toutiaosdk广告")
            time.sleep(40)
            TouchAction(driver).tap(x=1285, y=139).perform()  # 关闭toutiao广告
            print("toutiaosdk广告关闭")
        else:
            print("GDTsdk广告")
            time.sleep(55)
            driver.back()  # GDTsdk广告按钮
            print("GDTsdk广告关闭")
        # print(a)
        time.sleep(2)
        driver.back()
        time.sleep(2)
        a -= 1


kantu()
driver.back()  # 返回首页
time.sleep(2)

TouchAction(driver).tap(x=588, y=186).perform()  # 返回进入个人中心
time.sleep(2)
TouchAction(driver).tap(x=1275, y=243).perform()
time.sleep(1)
TouchAction(driver).tap(x=707, y=2467).perform()
time.sleep(1)
TouchAction(driver).tap(x=960, y=1440).perform()
BB = mobile + " \033[1;31m账号退出成功\033[0m"
print(BB)
#######################################################################################################################


mobile = "18017700521"
AA = "\033[1;31mNO.27\033[0m " + mobile + " \033[1;31m开始\033[0m"
print(AA)
nowtime = time.strftime('%Y-%m-%d% %H:%M:%S')
print(nowtime)
time.sleep(5)


def check_login():
    try:
        check_login = driver.find_element_by_id(
            "com.kamitu.drawsth.standalone.free.android:id/iv_mobile_login")  # 选择手机号登录
    except NoSuchElementException:
        print("自动登录成功")
    else:
        TouchAction(driver).tap(x=515, y=2300).perform()
        time.sleep(2)
        el2 = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/edit_phone")  # 选择手机号输入框
        el2.send_keys(mobile)
        time.sleep(2)
        TouchAction(driver).tap(x=1100, y=870).perform()  # 获取验证码
        time.sleep(2)
        # 获取验证码
        logincodeurl = "https://uc.crazyccy.com/login/main_login/testtool?key=sLQq2_jaKLknsqAwZ&type=1&mobile=" + mobile
        # print(logincodeurl)
        request = urllib.request.Request(logincodeurl)  # 构建请求url
        response = urllib.request.urlopen(request, context=context)  # ssl证书免验证加入,context = context# 打开请求url链接
        num = response.read()  # 读取页面返回信息，python3返回数据为bytes类型的对象 (即b为前缀, bytes类型)
        logincode = num.decode()
        if logincode == "查不到！":
            print("获取验证码失败")
            TouchAction(driver).tap(x=1100, y=870).perform()  # 获取验证码
        time.sleep(1)
        el4 = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/edit_identifyCode")  # 选择验证码输入框
        time.sleep(2)
        el4.send_keys(logincode)
        time.sleep(2)
        TouchAction(driver).tap(x=700, y=1200).perform()  # 确定按钮登录
        print("账号登录成功")


check_login()

time.sleep(15)  # 等待10秒加载进入首页


def check_signwindows():  # 检查用户签到弹窗
    try:
        check_signwindows = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/iv_signin_get")
    except NoSuchElementException:
        print("无签到弹窗")
    else:
        TouchAction(driver).tap(x=712, y=1884).perform()
        time.sleep(6)
        TouchAction(driver).tap(x=712, y=852).perform()
        time.sleep(6)
        try:
            GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
        except NoSuchElementException:
            print("toutiaosdk广告")
            time.sleep(40)
            TouchAction(driver).tap(x=1285, y=139).perform()  # 关闭toutiao广告
            print("toutiaosdk广告关闭")
            time.sleep(6)
            TouchAction(driver).tap(x=1254, y=671).perform()  # 关闭加分弹窗
        else:
            print("GDTsdk广告")
            time.sleep(55)
            driver.back()  # GDTsdk广告按钮
            print("GDTsdk广告关闭")
            time.sleep(6)
            TouchAction(driver).tap(x=1254, y=671).perform()  # 关闭加分弹窗


check_signwindows()
time.sleep(3)


def choujiang():
    time.sleep(3)
    TouchAction(driver).tap(x=1285, y=2354).perform()  # 进入抽奖页面
    time.sleep(2)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽10次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽9次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 看广告
    time.sleep(6)
    try:
        GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
    except NoSuchElementException:
        print("toutiaosdk广告")
        time.sleep(40)
        TouchAction(driver).tap(x=1285, y=139).perform()  # 关闭toutiao广告
        print("toutiaosdk广告关闭")
    else:
        print("GDTsdk广告")
        time.sleep(55)
        driver.back()  # GDTsdk广告按钮
        print("GDTsdk广告关闭")
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽8次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽7次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽6次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 看广告
    time.sleep(6)
    try:
        GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
    except NoSuchElementException:
        print("toutiaosdk广告")
        time.sleep(40)
        TouchAction(driver).tap(x=1285, y=139).perform()  # 关闭toutiao广告
        print("toutiaosdk广告关闭")
    else:
        print("GDTsdk广告")
        time.sleep(55)
        driver.back()  # GDTsdk广告按钮
        print("GDTsdk广告关闭")
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽5次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽4次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽3次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽2次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 看广告
    time.sleep(6)
    try:
        GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
    except NoSuchElementException:
        print("toutiaosdk广告")
        time.sleep(40)
        TouchAction(driver).tap(x=1285, y=139).perform()  # 关闭toutiao广告
        print("toutiaosdk广告关闭")
    else:
        print("GDTsdk广告")
        time.sleep(55)
        driver.back()  # GDTsdk广告按钮
        print("GDTsdk广告关闭")
    time.sleep(1)


choujiang()

time.sleep(3)
TouchAction(driver).tap(x=707, y=2070).perform()  # 进入接龙页面
time.sleep(3)
driver.back()
time.sleep(3)


def check_signtoast():  # 检查是否开启签到提示
    try:
        check_signtoast = driver.find_element_by_id(
            "com.kamitu.drawsth.standalone.free.android:id/iv_checkin_reminder_close")
    except NoSuchElementException:
        print("无签到提示")
    else:
        TouchAction(driver).tap(x=1228, y=748).perform()


check_signtoast()
time.sleep(3)


def kantu():
    TouchAction(driver).tap(x=175, y=2385).perform()  # 进入看图猜成语
    time.sleep(3)
    TouchAction(driver).tap(x=475, y=2280).perform()
    time.sleep(1)
    TouchAction(driver).tap(x=1105, y=2188).perform()
    time.sleep(1)
    TouchAction(driver).tap(x=800, y=2280).perform()  # 进入看图使用一次提示
    time.sleep(2)
    TouchAction(driver).tap(x=1000, y=1560).perform()  # 选择右侧提示广告
    driver.back()
    # 广告次数
    a = 6
    while a > 0:
        TouchAction(driver).tap(x=475, y=2280).perform()
        time.sleep(1)
        TouchAction(driver).tap(x=1105, y=2188).perform()
        time.sleep(1)
        TouchAction(driver).tap(x=800, y=2280).perform()  # 选择(位置)
        time.sleep(3)
        TouchAction(driver).tap(x=444, y=1560).perform()  # 选择左侧去除多余选项广告
        print(a)
        time.sleep(6)
        try:
            GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
        except NoSuchElementException:
            print("toutiaosdk广告")
            time.sleep(40)
            TouchAction(driver).tap(x=1285, y=139).perform()  # 关闭toutiao广告
            print("toutiaosdk广告关闭")
        else:
            print("GDTsdk广告")
            time.sleep(55)
            driver.back()  # GDTsdk广告按钮
            print("GDTsdk广告关闭")
        a -= 1
        time.sleep(2)
        TouchAction(driver).tap(x=1000, y=1560).perform()  # 选择右侧提示广告
        print(a)
        time.sleep(6)
        try:
            GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
        except NoSuchElementException:
            print("toutiaosdk广告")
            time.sleep(40)
            TouchAction(driver).tap(x=1285, y=139).perform()  # 关闭toutiao广告
            print("toutiaosdk广告关闭")
        else:
            print("GDTsdk广告")
            time.sleep(55)
            driver.back()  # GDTsdk广告按钮
            print("GDTsdk广告关闭")
        # print(a)
        time.sleep(2)
        driver.back()
        time.sleep(2)
        a -= 1


kantu()
driver.back()  # 返回首页
time.sleep(2)

TouchAction(driver).tap(x=588, y=186).perform()  # 返回进入个人中心
time.sleep(2)
TouchAction(driver).tap(x=1275, y=243).perform()
time.sleep(1)
TouchAction(driver).tap(x=707, y=2467).perform()
time.sleep(1)
TouchAction(driver).tap(x=960, y=1440).perform()
BB = mobile + " \033[1;31m账号退出成功\033[0m"
print(BB)
#######################################################################################################################


mobile = "18017700400"
AA = "\033[1;31mNO.28\033[0m " + mobile + " \033[1;31m开始\033[0m"
print(AA)
nowtime = time.strftime('%Y-%m-%d% %H:%M:%S')
print(nowtime)
time.sleep(5)


def check_login():
    try:
        check_login = driver.find_element_by_id(
            "com.kamitu.drawsth.standalone.free.android:id/iv_mobile_login")  # 选择手机号登录
    except NoSuchElementException:
        print("自动登录成功")
    else:
        TouchAction(driver).tap(x=515, y=2300).perform()
        time.sleep(2)
        el2 = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/edit_phone")  # 选择手机号输入框
        el2.send_keys(mobile)
        time.sleep(2)
        TouchAction(driver).tap(x=1100, y=870).perform()  # 获取验证码
        time.sleep(2)
        # 获取验证码
        logincodeurl = "https://uc.crazyccy.com/login/main_login/testtool?key=sLQq2_jaKLknsqAwZ&type=1&mobile=" + mobile
        # print(logincodeurl)
        request = urllib.request.Request(logincodeurl)  # 构建请求url
        response = urllib.request.urlopen(request, context=context)  # ssl证书免验证加入,context = context# 打开请求url链接
        num = response.read()  # 读取页面返回信息，python3返回数据为bytes类型的对象 (即b为前缀, bytes类型)
        logincode = num.decode()
        if logincode == "查不到！":
            print("获取验证码失败")
            TouchAction(driver).tap(x=1100, y=870).perform()  # 获取验证码
        time.sleep(1)
        el4 = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/edit_identifyCode")  # 选择验证码输入框
        time.sleep(2)
        el4.send_keys(logincode)
        time.sleep(2)
        TouchAction(driver).tap(x=700, y=1200).perform()  # 确定按钮登录
        print("账号登录成功")


check_login()

time.sleep(15)  # 等待10秒加载进入首页


def check_signwindows():  # 检查用户签到弹窗
    try:
        check_signwindows = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/iv_signin_get")
    except NoSuchElementException:
        print("无签到弹窗")
    else:
        TouchAction(driver).tap(x=712, y=1884).perform()
        time.sleep(6)
        TouchAction(driver).tap(x=712, y=852).perform()
        time.sleep(6)
        try:
            GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
        except NoSuchElementException:
            print("toutiaosdk广告")
            time.sleep(40)
            TouchAction(driver).tap(x=1285, y=139).perform()  # 关闭toutiao广告
            print("toutiaosdk广告关闭")
            time.sleep(6)
            TouchAction(driver).tap(x=1254, y=671).perform()  # 关闭加分弹窗
        else:
            print("GDTsdk广告")
            time.sleep(55)
            driver.back()  # GDTsdk广告按钮
            print("GDTsdk广告关闭")
            time.sleep(6)
            TouchAction(driver).tap(x=1254, y=671).perform()  # 关闭加分弹窗


check_signwindows()
time.sleep(3)


def choujiang():
    time.sleep(3)
    TouchAction(driver).tap(x=1285, y=2354).perform()  # 进入抽奖页面
    time.sleep(2)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽10次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽9次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 看广告
    time.sleep(6)
    try:
        GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
    except NoSuchElementException:
        print("toutiaosdk广告")
        time.sleep(40)
        TouchAction(driver).tap(x=1285, y=139).perform()  # 关闭toutiao广告
        print("toutiaosdk广告关闭")
    else:
        print("GDTsdk广告")
        time.sleep(55)
        driver.back()  # GDTsdk广告按钮
        print("GDTsdk广告关闭")
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽8次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽7次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽6次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 看广告
    time.sleep(6)
    try:
        GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
    except NoSuchElementException:
        print("toutiaosdk广告")
        time.sleep(40)
        TouchAction(driver).tap(x=1285, y=139).perform()  # 关闭toutiao广告
        print("toutiaosdk广告关闭")
    else:
        print("GDTsdk广告")
        time.sleep(55)
        driver.back()  # GDTsdk广告按钮
        print("GDTsdk广告关闭")
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽5次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽4次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽3次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽2次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 看广告
    time.sleep(6)
    try:
        GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
    except NoSuchElementException:
        print("toutiaosdk广告")
        time.sleep(40)
        TouchAction(driver).tap(x=1285, y=139).perform()  # 关闭toutiao广告
        print("toutiaosdk广告关闭")
    else:
        print("GDTsdk广告")
        time.sleep(55)
        driver.back()  # GDTsdk广告按钮
        print("GDTsdk广告关闭")
    time.sleep(1)


choujiang()

time.sleep(3)
TouchAction(driver).tap(x=707, y=2070).perform()  # 进入接龙页面
time.sleep(3)
driver.back()
time.sleep(3)


def check_signtoast():  # 检查是否开启签到提示
    try:
        check_signtoast = driver.find_element_by_id(
            "com.kamitu.drawsth.standalone.free.android:id/iv_checkin_reminder_close")
    except NoSuchElementException:
        print("无签到提示")
    else:
        TouchAction(driver).tap(x=1228, y=748).perform()


check_signtoast()
time.sleep(3)


def kantu():
    TouchAction(driver).tap(x=175, y=2385).perform()  # 进入看图猜成语
    time.sleep(3)
    TouchAction(driver).tap(x=475, y=2280).perform()
    time.sleep(1)
    TouchAction(driver).tap(x=1105, y=2188).perform()
    time.sleep(1)
    TouchAction(driver).tap(x=800, y=2280).perform()  # 进入看图使用一次提示
    time.sleep(2)
    TouchAction(driver).tap(x=1000, y=1560).perform()  # 选择右侧提示广告
    driver.back()
    # 广告次数
    a = 6
    while a > 0:
        TouchAction(driver).tap(x=475, y=2280).perform()
        time.sleep(1)
        TouchAction(driver).tap(x=1105, y=2188).perform()
        time.sleep(1)
        TouchAction(driver).tap(x=800, y=2280).perform()  # 选择(位置)
        time.sleep(3)
        TouchAction(driver).tap(x=444, y=1560).perform()  # 选择左侧去除多余选项广告
        print(a)
        time.sleep(6)
        try:
            GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
        except NoSuchElementException:
            print("toutiaosdk广告")
            time.sleep(40)
            TouchAction(driver).tap(x=1285, y=139).perform()  # 关闭toutiao广告
            print("toutiaosdk广告关闭")
        else:
            print("GDTsdk广告")
            time.sleep(55)
            driver.back()  # GDTsdk广告按钮
            print("GDTsdk广告关闭")
        a -= 1
        time.sleep(2)
        TouchAction(driver).tap(x=1000, y=1560).perform()  # 选择右侧提示广告
        print(a)
        time.sleep(6)
        try:
            GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
        except NoSuchElementException:
            print("toutiaosdk广告")
            time.sleep(40)
            TouchAction(driver).tap(x=1285, y=139).perform()  # 关闭toutiao广告
            print("toutiaosdk广告关闭")
        else:
            print("GDTsdk广告")
            time.sleep(55)
            driver.back()  # GDTsdk广告按钮
            print("GDTsdk广告关闭")
        # print(a)
        time.sleep(2)
        driver.back()
        time.sleep(2)
        a -= 1


kantu()
driver.back()  # 返回首页
time.sleep(2)

TouchAction(driver).tap(x=588, y=186).perform()  # 返回进入个人中心
time.sleep(2)
TouchAction(driver).tap(x=1275, y=243).perform()
time.sleep(1)
TouchAction(driver).tap(x=707, y=2467).perform()
time.sleep(1)
TouchAction(driver).tap(x=960, y=1440).perform()
BB = mobile + " \033[1;31m账号退出成功\033[0m"
print(BB)
#######################################################################################################################


mobile = "18017700410"
AA = "\033[1;31mNO.29\033[0m " + mobile + " \033[1;31m开始\033[0m"
print(AA)
nowtime = time.strftime('%Y-%m-%d% %H:%M:%S')
print(nowtime)
time.sleep(5)


def check_login():
    try:
        check_login = driver.find_element_by_id(
            "com.kamitu.drawsth.standalone.free.android:id/iv_mobile_login")  # 选择手机号登录
    except NoSuchElementException:
        print("自动登录成功")
    else:
        TouchAction(driver).tap(x=515, y=2300).perform()
        time.sleep(2)
        el2 = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/edit_phone")  # 选择手机号输入框
        el2.send_keys(mobile)
        time.sleep(2)
        TouchAction(driver).tap(x=1100, y=870).perform()  # 获取验证码
        time.sleep(2)
        # 获取验证码
        logincodeurl = "https://uc.crazyccy.com/login/main_login/testtool?key=sLQq2_jaKLknsqAwZ&type=1&mobile=" + mobile
        # print(logincodeurl)
        request = urllib.request.Request(logincodeurl)  # 构建请求url
        response = urllib.request.urlopen(request, context=context)  # ssl证书免验证加入,context = context# 打开请求url链接
        num = response.read()  # 读取页面返回信息，python3返回数据为bytes类型的对象 (即b为前缀, bytes类型)
        logincode = num.decode()
        if logincode == "查不到！":
            print("获取验证码失败")
            TouchAction(driver).tap(x=1100, y=870).perform()  # 获取验证码
        time.sleep(1)
        el4 = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/edit_identifyCode")  # 选择验证码输入框
        time.sleep(2)
        el4.send_keys(logincode)
        time.sleep(2)
        TouchAction(driver).tap(x=700, y=1200).perform()  # 确定按钮登录
        print("账号登录成功")


check_login()

time.sleep(15)  # 等待10秒加载进入首页


def check_signwindows():  # 检查用户签到弹窗
    try:
        check_signwindows = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/iv_signin_get")
    except NoSuchElementException:
        print("无签到弹窗")
    else:
        TouchAction(driver).tap(x=712, y=1884).perform()
        time.sleep(6)
        TouchAction(driver).tap(x=712, y=852).perform()
        time.sleep(6)
        try:
            GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
        except NoSuchElementException:
            print("toutiaosdk广告")
            time.sleep(40)
            TouchAction(driver).tap(x=1285, y=139).perform()  # 关闭toutiao广告
            print("toutiaosdk广告关闭")
            time.sleep(6)
            TouchAction(driver).tap(x=1254, y=671).perform()  # 关闭加分弹窗
        else:
            print("GDTsdk广告")
            time.sleep(55)
            driver.back()  # GDTsdk广告按钮
            print("GDTsdk广告关闭")
            time.sleep(6)
            TouchAction(driver).tap(x=1254, y=671).perform()  # 关闭加分弹窗


check_signwindows()
time.sleep(3)


def choujiang():
    time.sleep(3)
    TouchAction(driver).tap(x=1285, y=2354).perform()  # 进入抽奖页面
    time.sleep(2)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽10次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽9次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 看广告
    time.sleep(6)
    try:
        GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
    except NoSuchElementException:
        print("toutiaosdk广告")
        time.sleep(40)
        TouchAction(driver).tap(x=1285, y=139).perform()  # 关闭toutiao广告
        print("toutiaosdk广告关闭")
    else:
        print("GDTsdk广告")
        time.sleep(55)
        driver.back()  # GDTsdk广告按钮
        print("GDTsdk广告关闭")
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽8次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽7次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽6次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 看广告
    time.sleep(6)
    try:
        GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
    except NoSuchElementException:
        print("toutiaosdk广告")
        time.sleep(40)
        TouchAction(driver).tap(x=1285, y=139).perform()  # 关闭toutiao广告
        print("toutiaosdk广告关闭")
    else:
        print("GDTsdk广告")
        time.sleep(55)
        driver.back()  # GDTsdk广告按钮
        print("GDTsdk广告关闭")
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽5次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽4次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽3次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽2次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 看广告
    time.sleep(6)
    try:
        GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
    except NoSuchElementException:
        print("toutiaosdk广告")
        time.sleep(40)
        TouchAction(driver).tap(x=1285, y=139).perform()  # 关闭toutiao广告
        print("toutiaosdk广告关闭")
    else:
        print("GDTsdk广告")
        time.sleep(55)
        driver.back()  # GDTsdk广告按钮
        print("GDTsdk广告关闭")
    time.sleep(1)


choujiang()

time.sleep(3)
TouchAction(driver).tap(x=707, y=2070).perform()  # 进入接龙页面
time.sleep(3)
driver.back()
time.sleep(3)


def check_signtoast():  # 检查是否开启签到提示
    try:
        check_signtoast = driver.find_element_by_id(
            "com.kamitu.drawsth.standalone.free.android:id/iv_checkin_reminder_close")
    except NoSuchElementException:
        print("无签到提示")
    else:
        TouchAction(driver).tap(x=1228, y=748).perform()


check_signtoast()
time.sleep(3)


def kantu():
    TouchAction(driver).tap(x=175, y=2385).perform()  # 进入看图猜成语
    time.sleep(3)
    TouchAction(driver).tap(x=475, y=2280).perform()
    time.sleep(1)
    TouchAction(driver).tap(x=1105, y=2188).perform()
    time.sleep(1)
    TouchAction(driver).tap(x=800, y=2280).perform()  # 进入看图使用一次提示
    time.sleep(2)
    TouchAction(driver).tap(x=1000, y=1560).perform()  # 选择右侧提示广告
    driver.back()
    # 广告次数
    a = 6
    while a > 0:
        TouchAction(driver).tap(x=475, y=2280).perform()
        time.sleep(1)
        TouchAction(driver).tap(x=1105, y=2188).perform()
        time.sleep(1)
        TouchAction(driver).tap(x=800, y=2280).perform()  # 选择(位置)
        time.sleep(3)
        TouchAction(driver).tap(x=444, y=1560).perform()  # 选择左侧去除多余选项广告
        print(a)
        time.sleep(6)
        try:
            GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
        except NoSuchElementException:
            print("toutiaosdk广告")
            time.sleep(40)
            TouchAction(driver).tap(x=1285, y=139).perform()  # 关闭toutiao广告
            print("toutiaosdk广告关闭")
        else:
            print("GDTsdk广告")
            time.sleep(55)
            driver.back()  # GDTsdk广告按钮
            print("GDTsdk广告关闭")
        a -= 1
        time.sleep(2)
        TouchAction(driver).tap(x=1000, y=1560).perform()  # 选择右侧提示广告
        print(a)
        time.sleep(6)
        try:
            GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
        except NoSuchElementException:
            print("toutiaosdk广告")
            time.sleep(40)
            TouchAction(driver).tap(x=1285, y=139).perform()  # 关闭toutiao广告
            print("toutiaosdk广告关闭")
        else:
            print("GDTsdk广告")
            time.sleep(55)
            driver.back()  # GDTsdk广告按钮
            print("GDTsdk广告关闭")
        # print(a)
        time.sleep(2)
        driver.back()
        time.sleep(2)
        a -= 1


kantu()
driver.back()  # 返回首页
time.sleep(2)

TouchAction(driver).tap(x=588, y=186).perform()  # 返回进入个人中心
time.sleep(2)
TouchAction(driver).tap(x=1275, y=243).perform()
time.sleep(1)
TouchAction(driver).tap(x=707, y=2467).perform()
time.sleep(1)
TouchAction(driver).tap(x=960, y=1440).perform()
BB = mobile + " \033[1;31m账号退出成功\033[0m"
print(BB)
#######################################################################################################################


mobile = "18017700716"
AA = "\033[1;31mNO.30\033[0m " + mobile + " \033[1;31m开始\033[0m"
print(AA)
nowtime = time.strftime('%Y-%m-%d% %H:%M:%S')
print(nowtime)
time.sleep(5)


def check_login():
    try:
        check_login = driver.find_element_by_id(
            "com.kamitu.drawsth.standalone.free.android:id/iv_mobile_login")  # 选择手机号登录
    except NoSuchElementException:
        print("自动登录成功")
    else:
        TouchAction(driver).tap(x=515, y=2300).perform()
        time.sleep(2)
        el2 = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/edit_phone")  # 选择手机号输入框
        el2.send_keys(mobile)
        time.sleep(2)
        TouchAction(driver).tap(x=1100, y=870).perform()  # 获取验证码
        time.sleep(2)
        # 获取验证码
        logincodeurl = "https://uc.crazyccy.com/login/main_login/testtool?key=sLQq2_jaKLknsqAwZ&type=1&mobile=" + mobile
        # print(logincodeurl)
        request = urllib.request.Request(logincodeurl)  # 构建请求url
        response = urllib.request.urlopen(request, context=context)  # ssl证书免验证加入,context = context# 打开请求url链接
        num = response.read()  # 读取页面返回信息，python3返回数据为bytes类型的对象 (即b为前缀, bytes类型)
        logincode = num.decode()
        if logincode == "查不到！":
            print("获取验证码失败")
            TouchAction(driver).tap(x=1100, y=870).perform()  # 获取验证码
        time.sleep(1)
        el4 = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/edit_identifyCode")  # 选择验证码输入框
        time.sleep(2)
        el4.send_keys(logincode)
        time.sleep(2)
        TouchAction(driver).tap(x=700, y=1200).perform()  # 确定按钮登录
        print("账号登录成功")


check_login()

time.sleep(15)  # 等待10秒加载进入首页


def check_signwindows():  # 检查用户签到弹窗
    try:
        check_signwindows = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/iv_signin_get")
    except NoSuchElementException:
        print("无签到弹窗")
    else:
        TouchAction(driver).tap(x=712, y=1884).perform()
        time.sleep(6)
        TouchAction(driver).tap(x=712, y=852).perform()
        time.sleep(6)
        try:
            GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
        except NoSuchElementException:
            print("toutiaosdk广告")
            time.sleep(40)
            TouchAction(driver).tap(x=1285, y=139).perform()  # 关闭toutiao广告
            print("toutiaosdk广告关闭")
            time.sleep(6)
            TouchAction(driver).tap(x=1254, y=671).perform()  # 关闭加分弹窗
        else:
            print("GDTsdk广告")
            time.sleep(55)
            driver.back()  # GDTsdk广告按钮
            print("GDTsdk广告关闭")
            time.sleep(6)
            TouchAction(driver).tap(x=1254, y=671).perform()  # 关闭加分弹窗


check_signwindows()
time.sleep(3)


def choujiang():
    time.sleep(3)
    TouchAction(driver).tap(x=1285, y=2354).perform()  # 进入抽奖页面
    time.sleep(2)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽10次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽9次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 看广告
    time.sleep(6)
    try:
        GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
    except NoSuchElementException:
        print("toutiaosdk广告")
        time.sleep(40)
        TouchAction(driver).tap(x=1285, y=139).perform()  # 关闭toutiao广告
        print("toutiaosdk广告关闭")
    else:
        print("GDTsdk广告")
        time.sleep(55)
        driver.back()  # GDTsdk广告按钮
        print("GDTsdk广告关闭")
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽8次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽7次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽6次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 看广告
    time.sleep(6)
    try:
        GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
    except NoSuchElementException:
        print("toutiaosdk广告")
        time.sleep(40)
        TouchAction(driver).tap(x=1285, y=139).perform()  # 关闭toutiao广告
        print("toutiaosdk广告关闭")
    else:
        print("GDTsdk广告")
        time.sleep(55)
        driver.back()  # GDTsdk广告按钮
        print("GDTsdk广告关闭")
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽5次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽4次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽3次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽2次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 看广告
    time.sleep(6)
    try:
        GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
    except NoSuchElementException:
        print("toutiaosdk广告")
        time.sleep(40)
        TouchAction(driver).tap(x=1285, y=139).perform()  # 关闭toutiao广告
        print("toutiaosdk广告关闭")
    else:
        print("GDTsdk广告")
        time.sleep(55)
        driver.back()  # GDTsdk广告按钮
        print("GDTsdk广告关闭")
    time.sleep(1)


choujiang()

time.sleep(3)
TouchAction(driver).tap(x=707, y=2070).perform()  # 进入接龙页面
time.sleep(3)
driver.back()
time.sleep(3)


def check_signtoast():  # 检查是否开启签到提示
    try:
        check_signtoast = driver.find_element_by_id(
            "com.kamitu.drawsth.standalone.free.android:id/iv_checkin_reminder_close")
    except NoSuchElementException:
        print("无签到提示")
    else:
        TouchAction(driver).tap(x=1228, y=748).perform()


check_signtoast()
time.sleep(3)


def kantu():
    TouchAction(driver).tap(x=175, y=2385).perform()  # 进入看图猜成语
    time.sleep(3)
    TouchAction(driver).tap(x=475, y=2280).perform()
    time.sleep(1)
    TouchAction(driver).tap(x=1105, y=2188).perform()
    time.sleep(1)
    TouchAction(driver).tap(x=800, y=2280).perform()  # 进入看图使用一次提示
    time.sleep(2)
    TouchAction(driver).tap(x=1000, y=1560).perform()  # 选择右侧提示广告
    driver.back()
    # 广告次数
    a = 6
    while a > 0:
        TouchAction(driver).tap(x=475, y=2280).perform()
        time.sleep(1)
        TouchAction(driver).tap(x=1105, y=2188).perform()
        time.sleep(1)
        TouchAction(driver).tap(x=800, y=2280).perform()  # 选择(位置)
        time.sleep(3)
        TouchAction(driver).tap(x=444, y=1560).perform()  # 选择左侧去除多余选项广告
        print(a)
        time.sleep(6)
        try:
            GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
        except NoSuchElementException:
            print("toutiaosdk广告")
            time.sleep(40)
            TouchAction(driver).tap(x=1285, y=139).perform()  # 关闭toutiao广告
            print("toutiaosdk广告关闭")
        else:
            print("GDTsdk广告")
            time.sleep(55)
            driver.back()  # GDTsdk广告按钮
            print("GDTsdk广告关闭")
        a -= 1
        time.sleep(2)
        TouchAction(driver).tap(x=1000, y=1560).perform()  # 选择右侧提示广告
        print(a)
        time.sleep(6)
        try:
            GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
        except NoSuchElementException:
            print("toutiaosdk广告")
            time.sleep(40)
            TouchAction(driver).tap(x=1285, y=139).perform()  # 关闭toutiao广告
            print("toutiaosdk广告关闭")
        else:
            print("GDTsdk广告")
            time.sleep(55)
            driver.back()  # GDTsdk广告按钮
            print("GDTsdk广告关闭")
        # print(a)
        time.sleep(2)
        driver.back()
        time.sleep(2)
        a -= 1


kantu()
driver.back()  # 返回首页
time.sleep(2)

TouchAction(driver).tap(x=588, y=186).perform()  # 返回进入个人中心
time.sleep(2)
TouchAction(driver).tap(x=1275, y=243).perform()
time.sleep(1)
TouchAction(driver).tap(x=707, y=2467).perform()
time.sleep(1)
TouchAction(driver).tap(x=960, y=1440).perform()
BB = mobile + " \033[1;31m账号退出成功\033[0m"
print(BB)
#######################################################################################################################


mobile = "18017700411"
AA = "\033[1;31mNO.31\033[0m " + mobile + " \033[1;31m开始\033[0m"
print(AA)
nowtime = time.strftime('%Y-%m-%d% %H:%M:%S')
print(nowtime)
time.sleep(5)


def check_login():
    try:
        check_login = driver.find_element_by_id(
            "com.kamitu.drawsth.standalone.free.android:id/iv_mobile_login")  # 选择手机号登录
    except NoSuchElementException:
        print("自动登录成功")
    else:
        TouchAction(driver).tap(x=515, y=2300).perform()
        time.sleep(2)
        el2 = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/edit_phone")  # 选择手机号输入框
        el2.send_keys(mobile)
        time.sleep(2)
        TouchAction(driver).tap(x=1100, y=870).perform()  # 获取验证码
        time.sleep(2)
        # 获取验证码
        logincodeurl = "https://uc.crazyccy.com/login/main_login/testtool?key=sLQq2_jaKLknsqAwZ&type=1&mobile=" + mobile
        # print(logincodeurl)
        request = urllib.request.Request(logincodeurl)  # 构建请求url
        response = urllib.request.urlopen(request, context=context)  # ssl证书免验证加入,context = context# 打开请求url链接
        num = response.read()  # 读取页面返回信息，python3返回数据为bytes类型的对象 (即b为前缀, bytes类型)
        logincode = num.decode()
        if logincode == "查不到！":
            print("获取验证码失败")
            TouchAction(driver).tap(x=1100, y=870).perform()  # 获取验证码
        time.sleep(1)
        el4 = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/edit_identifyCode")  # 选择验证码输入框
        time.sleep(2)
        el4.send_keys(logincode)
        time.sleep(2)
        TouchAction(driver).tap(x=700, y=1200).perform()  # 确定按钮登录
        print("账号登录成功")


check_login()

time.sleep(15)  # 等待10秒加载进入首页


def check_signwindows():  # 检查用户签到弹窗
    try:
        check_signwindows = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/iv_signin_get")
    except NoSuchElementException:
        print("无签到弹窗")
    else:
        TouchAction(driver).tap(x=712, y=1884).perform()
        time.sleep(6)
        TouchAction(driver).tap(x=712, y=852).perform()
        time.sleep(6)
        try:
            GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
        except NoSuchElementException:
            print("toutiaosdk广告")
            time.sleep(40)
            TouchAction(driver).tap(x=1285, y=139).perform()  # 关闭toutiao广告
            print("toutiaosdk广告关闭")
            time.sleep(6)
            TouchAction(driver).tap(x=1254, y=671).perform()  # 关闭加分弹窗
        else:
            print("GDTsdk广告")
            time.sleep(55)
            driver.back()  # GDTsdk广告按钮
            print("GDTsdk广告关闭")
            time.sleep(6)
            TouchAction(driver).tap(x=1254, y=671).perform()  # 关闭加分弹窗


check_signwindows()
time.sleep(3)


def choujiang():
    time.sleep(3)
    TouchAction(driver).tap(x=1285, y=2354).perform()  # 进入抽奖页面
    time.sleep(2)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽10次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽9次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 看广告
    time.sleep(6)
    try:
        GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
    except NoSuchElementException:
        print("toutiaosdk广告")
        time.sleep(40)
        TouchAction(driver).tap(x=1285, y=139).perform()  # 关闭toutiao广告
        print("toutiaosdk广告关闭")
    else:
        print("GDTsdk广告")
        time.sleep(55)
        driver.back()  # GDTsdk广告按钮
        print("GDTsdk广告关闭")
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽8次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽7次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽6次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 看广告
    time.sleep(6)
    try:
        GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
    except NoSuchElementException:
        print("toutiaosdk广告")
        time.sleep(40)
        TouchAction(driver).tap(x=1285, y=139).perform()  # 关闭toutiao广告
        print("toutiaosdk广告关闭")
    else:
        print("GDTsdk广告")
        time.sleep(55)
        driver.back()  # GDTsdk广告按钮
        print("GDTsdk广告关闭")
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽5次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽4次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽3次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽2次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 看广告
    time.sleep(6)
    try:
        GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
    except NoSuchElementException:
        print("toutiaosdk广告")
        time.sleep(40)
        TouchAction(driver).tap(x=1285, y=139).perform()  # 关闭toutiao广告
        print("toutiaosdk广告关闭")
    else:
        print("GDTsdk广告")
        time.sleep(55)
        driver.back()  # GDTsdk广告按钮
        print("GDTsdk广告关闭")
    time.sleep(1)


choujiang()

time.sleep(3)
TouchAction(driver).tap(x=707, y=2070).perform()  # 进入接龙页面
time.sleep(3)
driver.back()
time.sleep(3)


def check_signtoast():  # 检查是否开启签到提示
    try:
        check_signtoast = driver.find_element_by_id(
            "com.kamitu.drawsth.standalone.free.android:id/iv_checkin_reminder_close")
    except NoSuchElementException:
        print("无签到提示")
    else:
        TouchAction(driver).tap(x=1228, y=748).perform()


check_signtoast()
time.sleep(3)


def kantu():
    TouchAction(driver).tap(x=175, y=2385).perform()  # 进入看图猜成语
    time.sleep(3)
    TouchAction(driver).tap(x=475, y=2280).perform()
    time.sleep(1)
    TouchAction(driver).tap(x=1105, y=2188).perform()
    time.sleep(1)
    TouchAction(driver).tap(x=800, y=2280).perform()  # 进入看图使用一次提示
    time.sleep(2)
    TouchAction(driver).tap(x=1000, y=1560).perform()  # 选择右侧提示广告
    driver.back()
    # 广告次数
    a = 6
    while a > 0:
        TouchAction(driver).tap(x=475, y=2280).perform()
        time.sleep(1)
        TouchAction(driver).tap(x=1105, y=2188).perform()
        time.sleep(1)
        TouchAction(driver).tap(x=800, y=2280).perform()  # 选择(位置)
        time.sleep(3)
        TouchAction(driver).tap(x=444, y=1560).perform()  # 选择左侧去除多余选项广告
        print(a)
        time.sleep(6)
        try:
            GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
        except NoSuchElementException:
            print("toutiaosdk广告")
            time.sleep(40)
            TouchAction(driver).tap(x=1285, y=139).perform()  # 关闭toutiao广告
            print("toutiaosdk广告关闭")
        else:
            print("GDTsdk广告")
            time.sleep(55)
            driver.back()  # GDTsdk广告按钮
            print("GDTsdk广告关闭")
        a -= 1
        time.sleep(2)
        TouchAction(driver).tap(x=1000, y=1560).perform()  # 选择右侧提示广告
        print(a)
        time.sleep(6)
        try:
            GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
        except NoSuchElementException:
            print("toutiaosdk广告")
            time.sleep(40)
            TouchAction(driver).tap(x=1285, y=139).perform()  # 关闭toutiao广告
            print("toutiaosdk广告关闭")
        else:
            print("GDTsdk广告")
            time.sleep(55)
            driver.back()  # GDTsdk广告按钮
            print("GDTsdk广告关闭")
        # print(a)
        time.sleep(2)
        driver.back()
        time.sleep(2)
        a -= 1


kantu()
driver.back()  # 返回首页
time.sleep(2)

TouchAction(driver).tap(x=588, y=186).perform()  # 返回进入个人中心
time.sleep(2)
TouchAction(driver).tap(x=1275, y=243).perform()
time.sleep(1)
TouchAction(driver).tap(x=707, y=2467).perform()
time.sleep(1)
TouchAction(driver).tap(x=960, y=1440).perform()
BB = mobile + " \033[1;31m账号退出成功\033[0m"
print(BB)
#######################################################################################################################


mobile = "18017700610"
AA = "\033[1;31mNO.32\033[0m " + mobile + " \033[1;31m开始\033[0m"
print(AA)
nowtime = time.strftime('%Y-%m-%d% %H:%M:%S')
print(nowtime)
time.sleep(5)


def check_login():
    try:
        check_login = driver.find_element_by_id(
            "com.kamitu.drawsth.standalone.free.android:id/iv_mobile_login")  # 选择手机号登录
    except NoSuchElementException:
        print("自动登录成功")
    else:
        TouchAction(driver).tap(x=515, y=2300).perform()
        time.sleep(2)
        el2 = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/edit_phone")  # 选择手机号输入框
        el2.send_keys(mobile)
        time.sleep(2)
        TouchAction(driver).tap(x=1100, y=870).perform()  # 获取验证码
        time.sleep(2)
        # 获取验证码
        logincodeurl = "https://uc.crazyccy.com/login/main_login/testtool?key=sLQq2_jaKLknsqAwZ&type=1&mobile=" + mobile
        # print(logincodeurl)
        request = urllib.request.Request(logincodeurl)  # 构建请求url
        response = urllib.request.urlopen(request, context=context)  # ssl证书免验证加入,context = context# 打开请求url链接
        num = response.read()  # 读取页面返回信息，python3返回数据为bytes类型的对象 (即b为前缀, bytes类型)
        logincode = num.decode()
        if logincode == "查不到！":
            print("获取验证码失败")
            TouchAction(driver).tap(x=1100, y=870).perform()  # 获取验证码
        time.sleep(1)
        el4 = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/edit_identifyCode")  # 选择验证码输入框
        time.sleep(2)
        el4.send_keys(logincode)
        time.sleep(2)
        TouchAction(driver).tap(x=700, y=1200).perform()  # 确定按钮登录
        print("账号登录成功")


check_login()

time.sleep(15)  # 等待10秒加载进入首页


def check_signwindows():  # 检查用户签到弹窗
    try:
        check_signwindows = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/iv_signin_get")
    except NoSuchElementException:
        print("无签到弹窗")
    else:
        TouchAction(driver).tap(x=712, y=1884).perform()
        time.sleep(6)
        TouchAction(driver).tap(x=712, y=852).perform()
        time.sleep(6)
        try:
            GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
        except NoSuchElementException:
            print("toutiaosdk广告")
            time.sleep(40)
            TouchAction(driver).tap(x=1285, y=139).perform()  # 关闭toutiao广告
            print("toutiaosdk广告关闭")
            time.sleep(6)
            TouchAction(driver).tap(x=1254, y=671).perform()  # 关闭加分弹窗
        else:
            print("GDTsdk广告")
            time.sleep(55)
            driver.back()  # GDTsdk广告按钮
            print("GDTsdk广告关闭")
            time.sleep(6)
            TouchAction(driver).tap(x=1254, y=671).perform()  # 关闭加分弹窗


check_signwindows()
time.sleep(3)


def choujiang():
    time.sleep(3)
    TouchAction(driver).tap(x=1285, y=2354).perform()  # 进入抽奖页面
    time.sleep(2)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽10次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽9次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 看广告
    time.sleep(6)
    try:
        GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
    except NoSuchElementException:
        print("toutiaosdk广告")
        time.sleep(40)
        TouchAction(driver).tap(x=1285, y=139).perform()  # 关闭toutiao广告
        print("toutiaosdk广告关闭")
    else:
        print("GDTsdk广告")
        time.sleep(55)
        driver.back()  # GDTsdk广告按钮
        print("GDTsdk广告关闭")
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽8次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽7次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽6次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 看广告
    time.sleep(6)
    try:
        GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
    except NoSuchElementException:
        print("toutiaosdk广告")
        time.sleep(40)
        TouchAction(driver).tap(x=1285, y=139).perform()  # 关闭toutiao广告
        print("toutiaosdk广告关闭")
    else:
        print("GDTsdk广告")
        time.sleep(55)
        driver.back()  # GDTsdk广告按钮
        print("GDTsdk广告关闭")
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽5次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽4次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽3次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 抽2次
    time.sleep(6)
    TouchAction(driver).tap(x=717, y=1620).perform()  # 关闭奖励弹窗
    TouchAction(driver).tap(x=717, y=1486).perform()  # 关闭奖励弹窗
    time.sleep(1)
    TouchAction(driver).tap(x=1037, y=1977).perform()  # 看广告
    time.sleep(6)
    try:
        GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
    except NoSuchElementException:
        print("toutiaosdk广告")
        time.sleep(40)
        TouchAction(driver).tap(x=1285, y=139).perform()  # 关闭toutiao广告
        print("toutiaosdk广告关闭")
    else:
        print("GDTsdk广告")
        time.sleep(55)
        driver.back()  # GDTsdk广告按钮
        print("GDTsdk广告关闭")
    time.sleep(1)


choujiang()

time.sleep(3)
TouchAction(driver).tap(x=707, y=2070).perform()  # 进入接龙页面
time.sleep(3)
driver.back()
time.sleep(3)


def check_signtoast():  # 检查是否开启签到提示
    try:
        check_signtoast = driver.find_element_by_id(
            "com.kamitu.drawsth.standalone.free.android:id/iv_checkin_reminder_close")
    except NoSuchElementException:
        print("无签到提示")
    else:
        TouchAction(driver).tap(x=1228, y=748).perform()


check_signtoast()
time.sleep(3)


def kantu():
    TouchAction(driver).tap(x=175, y=2385).perform()  # 进入看图猜成语
    time.sleep(3)
    TouchAction(driver).tap(x=475, y=2280).perform()
    time.sleep(1)
    TouchAction(driver).tap(x=1105, y=2188).perform()
    time.sleep(1)
    TouchAction(driver).tap(x=800, y=2280).perform()  # 进入看图使用一次提示
    time.sleep(2)
    TouchAction(driver).tap(x=1000, y=1560).perform()  # 选择右侧提示广告
    driver.back()
    # 广告次数
    a = 6
    while a > 0:
        TouchAction(driver).tap(x=475, y=2280).perform()
        time.sleep(1)
        TouchAction(driver).tap(x=1105, y=2188).perform()
        time.sleep(1)
        TouchAction(driver).tap(x=800, y=2280).perform()  # 选择(位置)
        time.sleep(3)
        TouchAction(driver).tap(x=444, y=1560).perform()  # 选择左侧去除多余选项广告
        print(a)
        time.sleep(6)
        try:
            GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
        except NoSuchElementException:
            print("toutiaosdk广告")
            time.sleep(40)
            TouchAction(driver).tap(x=1285, y=139).perform()  # 关闭toutiao广告
            print("toutiaosdk广告关闭")
        else:
            print("GDTsdk广告")
            time.sleep(55)
            driver.back()  # GDTsdk广告按钮
            print("GDTsdk广告关闭")
        a -= 1
        time.sleep(2)
        TouchAction(driver).tap(x=1000, y=1560).perform()  # 选择右侧提示广告
        print(a)
        time.sleep(6)
        try:
            GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
        except NoSuchElementException:
            print("toutiaosdk广告")
            time.sleep(40)
            TouchAction(driver).tap(x=1285, y=139).perform()  # 关闭toutiao广告
            print("toutiaosdk广告关闭")
        else:
            print("GDTsdk广告")
            time.sleep(55)
            driver.back()  # GDTsdk广告按钮
            print("GDTsdk广告关闭")
        # print(a)
        time.sleep(2)
        driver.back()
        time.sleep(2)
        a -= 1


kantu()
driver.back()  # 返回首页
time.sleep(2)

TouchAction(driver).tap(x=588, y=186).perform()  # 返回进入个人中心
time.sleep(2)
TouchAction(driver).tap(x=1275, y=243).perform()
time.sleep(1)
TouchAction(driver).tap(x=707, y=2467).perform()
time.sleep(1)
TouchAction(driver).tap(x=960, y=1440).perform()
BB = mobile + " \033[1;31m账号退出成功\033[0m"
print(BB)
#######################################################################################################################


nowtime = time.strftime('%Y-%m-%d% %H:%M:%S')
print(nowtime)
