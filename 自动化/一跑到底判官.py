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
nowtime = time.strftime('%H:%M:%S')
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
        time.sleep(1)
        edit_mobile = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/edit_phone")  # 选择手机号输入框
        edit_mobile.send_keys(mobile)
        time.sleep(1)
        TouchAction(driver).tap(x=1100, y=870).perform()  # 获取验证码
        time.sleep(2)
        # 获取验证码
        logincodeurl = "https://uc.crazyccy.com/login/main_login/testtool?key=sLQq2_jaKLknsqAwZ&type=1&mobile=" + mobile
        # print(logincodeurl)
        request = urllib.request.Request(logincodeurl)  # 构建请求url
        response = urllib.request.urlopen(request, context=context)  # ssl证书免验证加入,context = context# 打开请求url链接
        num = response.read()  # 读取页面返回信息，python3返回数据为bytes类型的对象 (即b为前缀, bytes类型)
        logincode = num.decode()
        edit_code = driver.find_element_by_id(
            "com.kamitu.drawsth.standalone.free.android:id/edit_identifyCode")  # 选择验证码输入框
        time.sleep(1)
        edit_code.send_keys(logincode)
        time.sleep(1)
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
        TouchAction(driver).tap(x=1270, y=655).perform()


check_signwindows()
time.sleep(2)

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
time.sleep(2)

TouchAction(driver).tap(x=439, y=2379).perform()  # 选择进入判官
time.sleep(1)
TouchAction(driver).tap(x=712, y=1342).perform()  # 选择开始挑战
time.sleep(3)

a = 11
while a > 0:
    time.sleep(8)
    TouchAction(driver).tap(x=671, y=1734).perform()  # 点击查看广告
    time.sleep(5)
    try:
        GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
    except NoSuchElementException:
        print("toutiaosdk广告")
        time.sleep(40)
        TouchAction(driver).tap(x=1285, y=139).perform()  # 关闭toutiao广告
        print(a)
        print("toutiaosdk广告关闭")
    else:
        print("GDTsdk广告")
        time.sleep(50)
        driver.back()  # GDTsdk广告按钮
        print(a)
        print("GDTsdk广告关闭")
    a -= 1

time.sleep(8)
driver.back()  # 判官中回到首页
time.sleep(1)
driver.back()
TouchAction(driver).tap(x=588, y=186).perform()  # 返回进入个人中心
time.sleep(2)
TouchAction(driver).tap(x=1275, y=243).perform()
time.sleep(1)
TouchAction(driver).tap(x=707, y=2467).perform()
time.sleep(1)
TouchAction(driver).tap(x=960, y=1440).perform()

#######################################################################################################################
mobile = "15606566329"
AA = "\033[1;31mNO.2\033[0m " + mobile + " \033[1;31m开始\033[0m"
print(AA)
nowtime = time.strftime('%H:%M:%S')
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
        time.sleep(1)
        edit_mobile = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/edit_phone")  # 选择手机号输入框
        edit_mobile.send_keys(mobile)
        time.sleep(1)
        TouchAction(driver).tap(x=1100, y=870).perform()  # 获取验证码
        time.sleep(2)
        # 获取验证码
        logincodeurl = "https://uc.crazyccy.com/login/main_login/testtool?key=sLQq2_jaKLknsqAwZ&type=1&mobile=" + mobile
        # print(logincodeurl)
        request = urllib.request.Request(logincodeurl)  # 构建请求url
        response = urllib.request.urlopen(request, context=context)  # ssl证书免验证加入,context = context# 打开请求url链接
        num = response.read()  # 读取页面返回信息，python3返回数据为bytes类型的对象 (即b为前缀, bytes类型)
        logincode = num.decode()
        edit_code = driver.find_element_by_id(
            "com.kamitu.drawsth.standalone.free.android:id/edit_identifyCode")  # 选择验证码输入框
        time.sleep(1)
        edit_code.send_keys(logincode)
        time.sleep(1)
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
        TouchAction(driver).tap(x=1270, y=655).perform()


check_signwindows()
time.sleep(2)

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
time.sleep(2)

TouchAction(driver).tap(x=439, y=2379).perform()  # 选择进入判官
time.sleep(1)
TouchAction(driver).tap(x=712, y=1342).perform()  # 选择开始挑战
time.sleep(3)

a = 11
while a > 0:
    time.sleep(8)
    TouchAction(driver).tap(x=671, y=1734).perform()  # 点击查看广告
    time.sleep(5)
    try:
        GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
    except NoSuchElementException:
        print("toutiaosdk广告")
        time.sleep(40)
        TouchAction(driver).tap(x=1285, y=139).perform()  # 关闭toutiao广告
        print(a)
        print("toutiaosdk广告关闭")
    else:
        print("GDTsdk广告")
        time.sleep(50)
        driver.back()  # GDTsdk广告按钮
        print(a)
        print("GDTsdk广告关闭")
    a -= 1

time.sleep(8)
driver.back()  # 判官中回到首页
time.sleep(1)
driver.back()
TouchAction(driver).tap(x=588, y=186).perform()  # 返回进入个人中心
time.sleep(2)
TouchAction(driver).tap(x=1275, y=243).perform()
time.sleep(1)
TouchAction(driver).tap(x=707, y=2467).perform()
time.sleep(1)
TouchAction(driver).tap(x=960, y=1440).perform()

#######################################################################################################################
mobile = "17502150079"
AA = "\033[1;31mNO.3\033[0m " + mobile + " \033[1;31m开始\033[0m"
print(AA)
nowtime = time.strftime('%H:%M:%S')
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
        time.sleep(1)
        edit_mobile = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/edit_phone")  # 选择手机号输入框
        edit_mobile.send_keys(mobile)
        time.sleep(1)
        TouchAction(driver).tap(x=1100, y=870).perform()  # 获取验证码
        time.sleep(2)
        # 获取验证码
        logincodeurl = "https://uc.crazyccy.com/login/main_login/testtool?key=sLQq2_jaKLknsqAwZ&type=1&mobile=" + mobile
        # print(logincodeurl)
        request = urllib.request.Request(logincodeurl)  # 构建请求url
        response = urllib.request.urlopen(request, context=context)  # ssl证书免验证加入,context = context# 打开请求url链接
        num = response.read()  # 读取页面返回信息，python3返回数据为bytes类型的对象 (即b为前缀, bytes类型)
        logincode = num.decode()
        edit_code = driver.find_element_by_id(
            "com.kamitu.drawsth.standalone.free.android:id/edit_identifyCode")  # 选择验证码输入框
        time.sleep(1)
        edit_code.send_keys(logincode)
        time.sleep(1)
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
        TouchAction(driver).tap(x=1270, y=655).perform()


check_signwindows()
time.sleep(2)

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
time.sleep(2)

TouchAction(driver).tap(x=439, y=2379).perform()  # 选择进入判官
time.sleep(1)
TouchAction(driver).tap(x=712, y=1342).perform()  # 选择开始挑战
time.sleep(3)

a = 11
while a > 0:
    time.sleep(8)
    TouchAction(driver).tap(x=671, y=1734).perform()  # 点击查看广告
    time.sleep(5)
    try:
        GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
    except NoSuchElementException:
        print("toutiaosdk广告")
        time.sleep(40)
        TouchAction(driver).tap(x=1285, y=139).perform()  # 关闭toutiao广告
        print(a)
        print("toutiaosdk广告关闭")
    else:
        print("GDTsdk广告")
        time.sleep(50)
        driver.back()  # GDTsdk广告按钮
        print(a)
        print("GDTsdk广告关闭")
    a -= 1

time.sleep(8)
driver.back()  # 判官中回到首页
time.sleep(1)
driver.back()
TouchAction(driver).tap(x=588, y=186).perform()  # 返回进入个人中心
time.sleep(2)
TouchAction(driver).tap(x=1275, y=243).perform()
time.sleep(1)
TouchAction(driver).tap(x=707, y=2467).perform()
time.sleep(1)
TouchAction(driver).tap(x=960, y=1440).perform()

#######################################################################################################################
mobile = "18017700411"
AA = "\033[1;31mNO.4\033[0m " + mobile + " \033[1;31m开始\033[0m"
print(AA)
nowtime = time.strftime('%H:%M:%S')
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
        time.sleep(1)
        edit_mobile = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/edit_phone")  # 选择手机号输入框
        edit_mobile.send_keys(mobile)
        time.sleep(1)
        TouchAction(driver).tap(x=1100, y=870).perform()  # 获取验证码
        time.sleep(2)
        # 获取验证码
        logincodeurl = "https://uc.crazyccy.com/login/main_login/testtool?key=sLQq2_jaKLknsqAwZ&type=1&mobile=" + mobile
        # print(logincodeurl)
        request = urllib.request.Request(logincodeurl)  # 构建请求url
        response = urllib.request.urlopen(request, context=context)  # ssl证书免验证加入,context = context# 打开请求url链接
        num = response.read()  # 读取页面返回信息，python3返回数据为bytes类型的对象 (即b为前缀, bytes类型)
        logincode = num.decode()
        edit_code = driver.find_element_by_id(
            "com.kamitu.drawsth.standalone.free.android:id/edit_identifyCode")  # 选择验证码输入框
        time.sleep(1)
        edit_code.send_keys(logincode)
        time.sleep(1)
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
        TouchAction(driver).tap(x=1270, y=655).perform()


check_signwindows()
time.sleep(2)

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
time.sleep(2)

TouchAction(driver).tap(x=439, y=2379).perform()  # 选择进入判官
time.sleep(1)
TouchAction(driver).tap(x=712, y=1342).perform()  # 选择开始挑战
time.sleep(3)

a = 11
while a > 0:
    time.sleep(8)
    TouchAction(driver).tap(x=671, y=1734).perform()  # 点击查看广告
    time.sleep(5)
    try:
        GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
    except NoSuchElementException:
        print("toutiaosdk广告")
        time.sleep(40)
        TouchAction(driver).tap(x=1285, y=139).perform()  # 关闭toutiao广告
        print(a)
        print("toutiaosdk广告关闭")
    else:
        print("GDTsdk广告")
        time.sleep(50)
        driver.back()  # GDTsdk广告按钮
        print(a)
        print("GDTsdk广告关闭")
    a -= 1

time.sleep(8)
driver.back()  # 判官中回到首页
time.sleep(1)
driver.back()
TouchAction(driver).tap(x=588, y=186).perform()  # 返回进入个人中心
time.sleep(2)
TouchAction(driver).tap(x=1275, y=243).perform()
time.sleep(1)
TouchAction(driver).tap(x=707, y=2467).perform()
time.sleep(1)
TouchAction(driver).tap(x=960, y=1440).perform()

#######################################################################################################################
mobile = "18017700610"
AA = "\033[1;31mNO.5\033[0m " + mobile + " \033[1;31m开始\033[0m"
print(AA)
nowtime = time.strftime('%H:%M:%S')
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
        time.sleep(1)
        edit_mobile = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/edit_phone")  # 选择手机号输入框
        edit_mobile.send_keys(mobile)
        time.sleep(1)
        TouchAction(driver).tap(x=1100, y=870).perform()  # 获取验证码
        time.sleep(2)
        # 获取验证码
        logincodeurl = "https://uc.crazyccy.com/login/main_login/testtool?key=sLQq2_jaKLknsqAwZ&type=1&mobile=" + mobile
        # print(logincodeurl)
        request = urllib.request.Request(logincodeurl)  # 构建请求url
        response = urllib.request.urlopen(request, context=context)  # ssl证书免验证加入,context = context# 打开请求url链接
        num = response.read()  # 读取页面返回信息，python3返回数据为bytes类型的对象 (即b为前缀, bytes类型)
        logincode = num.decode()
        edit_code = driver.find_element_by_id(
            "com.kamitu.drawsth.standalone.free.android:id/edit_identifyCode")  # 选择验证码输入框
        time.sleep(1)
        edit_code.send_keys(logincode)
        time.sleep(1)
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
        TouchAction(driver).tap(x=1270, y=655).perform()


check_signwindows()
time.sleep(2)

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
time.sleep(2)

TouchAction(driver).tap(x=439, y=2379).perform()  # 选择进入判官
time.sleep(1)
TouchAction(driver).tap(x=712, y=1342).perform()  # 选择开始挑战
time.sleep(3)

a = 11
while a > 0:
    time.sleep(8)
    TouchAction(driver).tap(x=671, y=1734).perform()  # 点击查看广告
    time.sleep(5)
    try:
        GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
    except NoSuchElementException:
        print("toutiaosdk广告")
        time.sleep(40)
        TouchAction(driver).tap(x=1285, y=139).perform()  # 关闭toutiao广告
        print(a)
        print("toutiaosdk广告关闭")
    else:
        print("GDTsdk广告")
        time.sleep(50)
        driver.back()  # GDTsdk广告按钮
        print(a)
        print("GDTsdk广告关闭")
    a -= 1

time.sleep(8)
driver.back()  # 判官中回到首页
time.sleep(1)
driver.back()
TouchAction(driver).tap(x=588, y=186).perform()  # 返回进入个人中心
time.sleep(2)
TouchAction(driver).tap(x=1275, y=243).perform()
time.sleep(1)
TouchAction(driver).tap(x=707, y=2467).perform()
time.sleep(1)
TouchAction(driver).tap(x=960, y=1440).perform()

#######################################################################################################################
mobile = "18017700716"
AA = "\033[1;31mNO.6\033[0m " + mobile + " \033[1;31m开始\033[0m"
print(AA)
nowtime = time.strftime('%H:%M:%S')
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
        time.sleep(1)
        edit_mobile = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/edit_phone")  # 选择手机号输入框
        edit_mobile.send_keys(mobile)
        time.sleep(1)
        TouchAction(driver).tap(x=1100, y=870).perform()  # 获取验证码
        time.sleep(2)
        # 获取验证码
        logincodeurl = "https://uc.crazyccy.com/login/main_login/testtool?key=sLQq2_jaKLknsqAwZ&type=1&mobile=" + mobile
        # print(logincodeurl)
        request = urllib.request.Request(logincodeurl)  # 构建请求url
        response = urllib.request.urlopen(request, context=context)  # ssl证书免验证加入,context = context# 打开请求url链接
        num = response.read()  # 读取页面返回信息，python3返回数据为bytes类型的对象 (即b为前缀, bytes类型)
        logincode = num.decode()
        edit_code = driver.find_element_by_id(
            "com.kamitu.drawsth.standalone.free.android:id/edit_identifyCode")  # 选择验证码输入框
        time.sleep(1)
        edit_code.send_keys(logincode)
        time.sleep(1)
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
        TouchAction(driver).tap(x=1270, y=655).perform()


check_signwindows()
time.sleep(2)

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
time.sleep(2)

TouchAction(driver).tap(x=439, y=2379).perform()  # 选择进入判官
time.sleep(1)
TouchAction(driver).tap(x=712, y=1342).perform()  # 选择开始挑战
time.sleep(3)

a = 11
while a > 0:
    time.sleep(8)
    TouchAction(driver).tap(x=671, y=1734).perform()  # 点击查看广告
    time.sleep(5)
    try:
        GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
    except NoSuchElementException:
        print("toutiaosdk广告")
        time.sleep(40)
        TouchAction(driver).tap(x=1285, y=139).perform()  # 关闭toutiao广告
        print(a)
        print("toutiaosdk广告关闭")
    else:
        print("GDTsdk广告")
        time.sleep(50)
        driver.back()  # GDTsdk广告按钮
        print(a)
        print("GDTsdk广告关闭")
    a -= 1

time.sleep(8)
driver.back()  # 判官中回到首页
time.sleep(1)
driver.back()
TouchAction(driver).tap(x=588, y=186).perform()  # 返回进入个人中心
time.sleep(2)
TouchAction(driver).tap(x=1275, y=243).perform()
time.sleep(1)
TouchAction(driver).tap(x=707, y=2467).perform()
time.sleep(1)
TouchAction(driver).tap(x=960, y=1440).perform()

#######################################################################################################################
mobile = "18930224047"
AA = "\033[1;31mNO.7\033[0m " + mobile + " \033[1;31m开始\033[0m"
print(AA)
nowtime = time.strftime('%H:%M:%S')
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
        time.sleep(1)
        edit_mobile = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/edit_phone")  # 选择手机号输入框
        edit_mobile.send_keys(mobile)
        time.sleep(1)
        TouchAction(driver).tap(x=1100, y=870).perform()  # 获取验证码
        time.sleep(2)
        # 获取验证码
        logincodeurl = "https://uc.crazyccy.com/login/main_login/testtool?key=sLQq2_jaKLknsqAwZ&type=1&mobile=" + mobile
        # print(logincodeurl)
        request = urllib.request.Request(logincodeurl)  # 构建请求url
        response = urllib.request.urlopen(request, context=context)  # ssl证书免验证加入,context = context# 打开请求url链接
        num = response.read()  # 读取页面返回信息，python3返回数据为bytes类型的对象 (即b为前缀, bytes类型)
        logincode = num.decode()
        edit_code = driver.find_element_by_id(
            "com.kamitu.drawsth.standalone.free.android:id/edit_identifyCode")  # 选择验证码输入框
        time.sleep(1)
        edit_code.send_keys(logincode)
        time.sleep(1)
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
        TouchAction(driver).tap(x=1270, y=655).perform()


check_signwindows()
time.sleep(2)

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
time.sleep(2)

TouchAction(driver).tap(x=439, y=2379).perform()  # 选择进入判官
time.sleep(1)
TouchAction(driver).tap(x=712, y=1342).perform()  # 选择开始挑战
time.sleep(3)

a = 11
while a > 0:
    time.sleep(8)
    TouchAction(driver).tap(x=671, y=1734).perform()  # 点击查看广告
    time.sleep(5)
    try:
        GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
    except NoSuchElementException:
        print("toutiaosdk广告")
        time.sleep(40)
        TouchAction(driver).tap(x=1285, y=139).perform()  # 关闭toutiao广告
        print(a)
        print("toutiaosdk广告关闭")
    else:
        print("GDTsdk广告")
        time.sleep(50)
        driver.back()  # GDTsdk广告按钮
        print(a)
        print("GDTsdk广告关闭")
    a -= 1

time.sleep(8)
driver.back()  # 判官中回到首页
time.sleep(1)
driver.back()
TouchAction(driver).tap(x=588, y=186).perform()  # 返回进入个人中心
time.sleep(2)
TouchAction(driver).tap(x=1275, y=243).perform()
time.sleep(1)
TouchAction(driver).tap(x=707, y=2467).perform()
time.sleep(1)
TouchAction(driver).tap(x=960, y=1440).perform()

#######################################################################################################################
mobile = "18017700410"
AA = "\033[1;31mNO.8\033[0m " + mobile + " \033[1;31m开始\033[0m"
print(AA)
nowtime = time.strftime('%H:%M:%S')
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
        time.sleep(1)
        edit_mobile = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/edit_phone")  # 选择手机号输入框
        edit_mobile.send_keys(mobile)
        time.sleep(1)
        TouchAction(driver).tap(x=1100, y=870).perform()  # 获取验证码
        time.sleep(2)
        # 获取验证码
        logincodeurl = "https://uc.crazyccy.com/login/main_login/testtool?key=sLQq2_jaKLknsqAwZ&type=1&mobile=" + mobile
        # print(logincodeurl)
        request = urllib.request.Request(logincodeurl)  # 构建请求url
        response = urllib.request.urlopen(request, context=context)  # ssl证书免验证加入,context = context# 打开请求url链接
        num = response.read()  # 读取页面返回信息，python3返回数据为bytes类型的对象 (即b为前缀, bytes类型)
        logincode = num.decode()
        edit_code = driver.find_element_by_id(
            "com.kamitu.drawsth.standalone.free.android:id/edit_identifyCode")  # 选择验证码输入框
        time.sleep(1)
        edit_code.send_keys(logincode)
        time.sleep(1)
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
        TouchAction(driver).tap(x=1270, y=655).perform()


check_signwindows()
time.sleep(2)

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
time.sleep(2)

TouchAction(driver).tap(x=439, y=2379).perform()  # 选择进入判官
time.sleep(1)
TouchAction(driver).tap(x=712, y=1342).perform()  # 选择开始挑战
time.sleep(3)

a = 11
while a > 0:
    time.sleep(8)
    TouchAction(driver).tap(x=671, y=1734).perform()  # 点击查看广告
    time.sleep(5)
    try:
        GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
    except NoSuchElementException:
        print("toutiaosdk广告")
        time.sleep(40)
        TouchAction(driver).tap(x=1285, y=139).perform()  # 关闭toutiao广告
        print(a)
        print("toutiaosdk广告关闭")
    else:
        print("GDTsdk广告")
        time.sleep(50)
        driver.back()  # GDTsdk广告按钮
        print(a)
        print("GDTsdk广告关闭")
    a -= 1

time.sleep(8)
driver.back()  # 判官中回到首页
time.sleep(1)
driver.back()
TouchAction(driver).tap(x=588, y=186).perform()  # 返回进入个人中心
time.sleep(2)
TouchAction(driver).tap(x=1275, y=243).perform()
time.sleep(1)
TouchAction(driver).tap(x=707, y=2467).perform()
time.sleep(1)
TouchAction(driver).tap(x=960, y=1440).perform()

#######################################################################################################################
mobile = "18017700717"
AA = "\033[1;31mNO.9\033[0m " + mobile + " \033[1;31m开始\033[0m"
print(AA)
nowtime = time.strftime('%H:%M:%S')
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
        time.sleep(1)
        edit_mobile = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/edit_phone")  # 选择手机号输入框
        edit_mobile.send_keys(mobile)
        time.sleep(1)
        TouchAction(driver).tap(x=1100, y=870).perform()  # 获取验证码
        time.sleep(2)
        # 获取验证码
        logincodeurl = "https://uc.crazyccy.com/login/main_login/testtool?key=sLQq2_jaKLknsqAwZ&type=1&mobile=" + mobile
        # print(logincodeurl)
        request = urllib.request.Request(logincodeurl)  # 构建请求url
        response = urllib.request.urlopen(request, context=context)  # ssl证书免验证加入,context = context# 打开请求url链接
        num = response.read()  # 读取页面返回信息，python3返回数据为bytes类型的对象 (即b为前缀, bytes类型)
        logincode = num.decode()
        edit_code = driver.find_element_by_id(
            "com.kamitu.drawsth.standalone.free.android:id/edit_identifyCode")  # 选择验证码输入框
        time.sleep(1)
        edit_code.send_keys(logincode)
        time.sleep(1)
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
        TouchAction(driver).tap(x=1270, y=655).perform()


check_signwindows()
time.sleep(2)

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
time.sleep(2)

TouchAction(driver).tap(x=439, y=2379).perform()  # 选择进入判官
time.sleep(1)
TouchAction(driver).tap(x=712, y=1342).perform()  # 选择开始挑战
time.sleep(3)

a = 11
while a > 0:
    time.sleep(8)
    TouchAction(driver).tap(x=671, y=1734).perform()  # 点击查看广告
    time.sleep(5)
    try:
        GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
    except NoSuchElementException:
        print("toutiaosdk广告")
        time.sleep(40)
        TouchAction(driver).tap(x=1285, y=139).perform()  # 关闭toutiao广告
        print(a)
        print("toutiaosdk广告关闭")
    else:
        print("GDTsdk广告")
        time.sleep(50)
        driver.back()  # GDTsdk广告按钮
        print(a)
        print("GDTsdk广告关闭")
    a -= 1

time.sleep(8)
driver.back()  # 判官中回到首页
time.sleep(1)
driver.back()
TouchAction(driver).tap(x=588, y=186).perform()  # 返回进入个人中心
time.sleep(2)
TouchAction(driver).tap(x=1275, y=243).perform()
time.sleep(1)
TouchAction(driver).tap(x=707, y=2467).perform()
time.sleep(1)
TouchAction(driver).tap(x=960, y=1440).perform()

#######################################################################################################################
mobile = "18017700400"
AA = "\033[1;31mNO.10\033[0m " + mobile + " \033[1;31m开始\033[0m"
print(AA)
nowtime = time.strftime('%H:%M:%S')
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
        time.sleep(1)
        edit_mobile = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/edit_phone")  # 选择手机号输入框
        edit_mobile.send_keys(mobile)
        time.sleep(1)
        TouchAction(driver).tap(x=1100, y=870).perform()  # 获取验证码
        time.sleep(2)
        # 获取验证码
        logincodeurl = "https://uc.crazyccy.com/login/main_login/testtool?key=sLQq2_jaKLknsqAwZ&type=1&mobile=" + mobile
        # print(logincodeurl)
        request = urllib.request.Request(logincodeurl)  # 构建请求url
        response = urllib.request.urlopen(request, context=context)  # ssl证书免验证加入,context = context# 打开请求url链接
        num = response.read()  # 读取页面返回信息，python3返回数据为bytes类型的对象 (即b为前缀, bytes类型)
        logincode = num.decode()
        edit_code = driver.find_element_by_id(
            "com.kamitu.drawsth.standalone.free.android:id/edit_identifyCode")  # 选择验证码输入框
        time.sleep(1)
        edit_code.send_keys(logincode)
        time.sleep(1)
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
        TouchAction(driver).tap(x=1270, y=655).perform()


check_signwindows()
time.sleep(2)

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
time.sleep(2)

TouchAction(driver).tap(x=439, y=2379).perform()  # 选择进入判官
time.sleep(1)
TouchAction(driver).tap(x=712, y=1342).perform()  # 选择开始挑战
time.sleep(3)

a = 11
while a > 0:
    time.sleep(8)
    TouchAction(driver).tap(x=671, y=1734).perform()  # 点击查看广告
    time.sleep(5)
    try:
        GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
    except NoSuchElementException:
        print("toutiaosdk广告")
        time.sleep(40)
        TouchAction(driver).tap(x=1285, y=139).perform()  # 关闭toutiao广告
        print(a)
        print("toutiaosdk广告关闭")
    else:
        print("GDTsdk广告")
        time.sleep(50)
        driver.back()  # GDTsdk广告按钮
        print(a)
        print("GDTsdk广告关闭")
    a -= 1

time.sleep(8)
driver.back()  # 判官中回到首页
time.sleep(1)
driver.back()
TouchAction(driver).tap(x=588, y=186).perform()  # 返回进入个人中心
time.sleep(2)
TouchAction(driver).tap(x=1275, y=243).perform()
time.sleep(1)
TouchAction(driver).tap(x=707, y=2467).perform()
time.sleep(1)
TouchAction(driver).tap(x=960, y=1440).perform()

#######################################################################################################################
mobile = "18017700602"
AA = "\033[1;31mNO.11\033[0m " + mobile + " \033[1;31m开始\033[0m"
print(AA)
nowtime = time.strftime('%H:%M:%S')
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
        time.sleep(1)
        edit_mobile = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/edit_phone")  # 选择手机号输入框
        edit_mobile.send_keys(mobile)
        time.sleep(1)
        TouchAction(driver).tap(x=1100, y=870).perform()  # 获取验证码
        time.sleep(2)
        # 获取验证码
        logincodeurl = "https://uc.crazyccy.com/login/main_login/testtool?key=sLQq2_jaKLknsqAwZ&type=1&mobile=" + mobile
        # print(logincodeurl)
        request = urllib.request.Request(logincodeurl)  # 构建请求url
        response = urllib.request.urlopen(request, context=context)  # ssl证书免验证加入,context = context# 打开请求url链接
        num = response.read()  # 读取页面返回信息，python3返回数据为bytes类型的对象 (即b为前缀, bytes类型)
        logincode = num.decode()
        edit_code = driver.find_element_by_id(
            "com.kamitu.drawsth.standalone.free.android:id/edit_identifyCode")  # 选择验证码输入框
        time.sleep(1)
        edit_code.send_keys(logincode)
        time.sleep(1)
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
        TouchAction(driver).tap(x=1270, y=655).perform()


check_signwindows()
time.sleep(2)

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
time.sleep(2)

TouchAction(driver).tap(x=439, y=2379).perform()  # 选择进入判官
time.sleep(1)
TouchAction(driver).tap(x=712, y=1342).perform()  # 选择开始挑战
time.sleep(3)

a = 11
while a > 0:
    time.sleep(8)
    TouchAction(driver).tap(x=671, y=1734).perform()  # 点击查看广告
    time.sleep(5)
    try:
        GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
    except NoSuchElementException:
        print("toutiaosdk广告")
        time.sleep(40)
        TouchAction(driver).tap(x=1285, y=139).perform()  # 关闭toutiao广告
        print(a)
        print("toutiaosdk广告关闭")
    else:
        print("GDTsdk广告")
        time.sleep(50)
        driver.back()  # GDTsdk广告按钮
        print(a)
        print("GDTsdk广告关闭")
    a -= 1

time.sleep(8)
driver.back()  # 判官中回到首页
time.sleep(1)
driver.back()
TouchAction(driver).tap(x=588, y=186).perform()  # 返回进入个人中心
time.sleep(2)
TouchAction(driver).tap(x=1275, y=243).perform()
time.sleep(1)
TouchAction(driver).tap(x=707, y=2467).perform()
time.sleep(1)
TouchAction(driver).tap(x=960, y=1440).perform()

#######################################################################################################################
mobile = "18017700601"
AA = "\033[1;31mNO.12\033[0m " + mobile + " \033[1;31m开始\033[0m"
print(AA)
nowtime = time.strftime('%H:%M:%S')
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
        time.sleep(1)
        edit_mobile = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/edit_phone")  # 选择手机号输入框
        edit_mobile.send_keys(mobile)
        time.sleep(1)
        TouchAction(driver).tap(x=1100, y=870).perform()  # 获取验证码
        time.sleep(2)
        # 获取验证码
        logincodeurl = "https://uc.crazyccy.com/login/main_login/testtool?key=sLQq2_jaKLknsqAwZ&type=1&mobile=" + mobile
        # print(logincodeurl)
        request = urllib.request.Request(logincodeurl)  # 构建请求url
        response = urllib.request.urlopen(request, context=context)  # ssl证书免验证加入,context = context# 打开请求url链接
        num = response.read()  # 读取页面返回信息，python3返回数据为bytes类型的对象 (即b为前缀, bytes类型)
        logincode = num.decode()
        edit_code = driver.find_element_by_id(
            "com.kamitu.drawsth.standalone.free.android:id/edit_identifyCode")  # 选择验证码输入框
        time.sleep(1)
        edit_code.send_keys(logincode)
        time.sleep(1)
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
        TouchAction(driver).tap(x=1270, y=655).perform()


check_signwindows()
time.sleep(2)

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
time.sleep(2)

TouchAction(driver).tap(x=439, y=2379).perform()  # 选择进入判官
time.sleep(1)
TouchAction(driver).tap(x=712, y=1342).perform()  # 选择开始挑战
time.sleep(3)

a = 11
while a > 0:
    time.sleep(8)
    TouchAction(driver).tap(x=671, y=1734).perform()  # 点击查看广告
    time.sleep(5)
    try:
        GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
    except NoSuchElementException:
        print("toutiaosdk广告")
        time.sleep(40)
        TouchAction(driver).tap(x=1285, y=139).perform()  # 关闭toutiao广告
        print(a)
        print("toutiaosdk广告关闭")
    else:
        print("GDTsdk广告")
        time.sleep(50)
        driver.back()  # GDTsdk广告按钮
        print(a)
        print("GDTsdk广告关闭")
    a -= 1

time.sleep(8)
driver.back()  # 判官中回到首页
time.sleep(1)
driver.back()
TouchAction(driver).tap(x=588, y=186).perform()  # 返回进入个人中心
time.sleep(2)
TouchAction(driver).tap(x=1275, y=243).perform()
time.sleep(1)
TouchAction(driver).tap(x=707, y=2467).perform()
time.sleep(1)
TouchAction(driver).tap(x=960, y=1440).perform()

#######################################################################################################################
mobile = "18017700599"
AA = "\033[1;31mNO.13\033[0m " + mobile + " \033[1;31m开始\033[0m"
print(AA)
nowtime = time.strftime('%H:%M:%S')
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
        time.sleep(1)
        edit_mobile = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/edit_phone")  # 选择手机号输入框
        edit_mobile.send_keys(mobile)
        time.sleep(1)
        TouchAction(driver).tap(x=1100, y=870).perform()  # 获取验证码
        time.sleep(2)
        # 获取验证码
        logincodeurl = "https://uc.crazyccy.com/login/main_login/testtool?key=sLQq2_jaKLknsqAwZ&type=1&mobile=" + mobile
        # print(logincodeurl)
        request = urllib.request.Request(logincodeurl)  # 构建请求url
        response = urllib.request.urlopen(request, context=context)  # ssl证书免验证加入,context = context# 打开请求url链接
        num = response.read()  # 读取页面返回信息，python3返回数据为bytes类型的对象 (即b为前缀, bytes类型)
        logincode = num.decode()
        edit_code = driver.find_element_by_id(
            "com.kamitu.drawsth.standalone.free.android:id/edit_identifyCode")  # 选择验证码输入框
        time.sleep(1)
        edit_code.send_keys(logincode)
        time.sleep(1)
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
        TouchAction(driver).tap(x=1270, y=655).perform()


check_signwindows()
time.sleep(2)

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
time.sleep(2)

TouchAction(driver).tap(x=439, y=2379).perform()  # 选择进入判官
time.sleep(1)
TouchAction(driver).tap(x=712, y=1342).perform()  # 选择开始挑战
time.sleep(3)

a = 11
while a > 0:
    time.sleep(8)
    TouchAction(driver).tap(x=671, y=1734).perform()  # 点击查看广告
    time.sleep(5)
    try:
        GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
    except NoSuchElementException:
        print("toutiaosdk广告")
        time.sleep(40)
        TouchAction(driver).tap(x=1285, y=139).perform()  # 关闭toutiao广告
        print(a)
        print("toutiaosdk广告关闭")
    else:
        print("GDTsdk广告")
        time.sleep(50)
        driver.back()  # GDTsdk广告按钮
        print(a)
        print("GDTsdk广告关闭")
    a -= 1

time.sleep(8)
driver.back()  # 判官中回到首页
time.sleep(1)
driver.back()
TouchAction(driver).tap(x=588, y=186).perform()  # 返回进入个人中心
time.sleep(2)
TouchAction(driver).tap(x=1275, y=243).perform()
time.sleep(1)
TouchAction(driver).tap(x=707, y=2467).perform()
time.sleep(1)
TouchAction(driver).tap(x=960, y=1440).perform()

#######################################################################################################################
mobile = "18017700598"
AA = "\033[1;31mNO.14\033[0m " + mobile + " \033[1;31m开始\033[0m"
print(AA)
nowtime = time.strftime('%H:%M:%S')
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
        time.sleep(1)
        edit_mobile = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/edit_phone")  # 选择手机号输入框
        edit_mobile.send_keys(mobile)
        time.sleep(1)
        TouchAction(driver).tap(x=1100, y=870).perform()  # 获取验证码
        time.sleep(2)
        # 获取验证码
        logincodeurl = "https://uc.crazyccy.com/login/main_login/testtool?key=sLQq2_jaKLknsqAwZ&type=1&mobile=" + mobile
        # print(logincodeurl)
        request = urllib.request.Request(logincodeurl)  # 构建请求url
        response = urllib.request.urlopen(request, context=context)  # ssl证书免验证加入,context = context# 打开请求url链接
        num = response.read()  # 读取页面返回信息，python3返回数据为bytes类型的对象 (即b为前缀, bytes类型)
        logincode = num.decode()
        edit_code = driver.find_element_by_id(
            "com.kamitu.drawsth.standalone.free.android:id/edit_identifyCode")  # 选择验证码输入框
        time.sleep(1)
        edit_code.send_keys(logincode)
        time.sleep(1)
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
        TouchAction(driver).tap(x=1270, y=655).perform()


check_signwindows()
time.sleep(2)

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
time.sleep(2)

TouchAction(driver).tap(x=439, y=2379).perform()  # 选择进入判官
time.sleep(1)
TouchAction(driver).tap(x=712, y=1342).perform()  # 选择开始挑战
time.sleep(3)

a = 11
while a > 0:
    time.sleep(8)
    TouchAction(driver).tap(x=671, y=1734).perform()  # 点击查看广告
    time.sleep(5)
    try:
        GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
    except NoSuchElementException:
        print("toutiaosdk广告")
        time.sleep(40)
        TouchAction(driver).tap(x=1285, y=139).perform()  # 关闭toutiao广告
        print(a)
        print("toutiaosdk广告关闭")
    else:
        print("GDTsdk广告")
        time.sleep(50)
        driver.back()  # GDTsdk广告按钮
        print(a)
        print("GDTsdk广告关闭")
    a -= 1

time.sleep(8)
driver.back()  # 判官中回到首页
time.sleep(1)
driver.back()
TouchAction(driver).tap(x=588, y=186).perform()  # 返回进入个人中心
time.sleep(2)
TouchAction(driver).tap(x=1275, y=243).perform()
time.sleep(1)
TouchAction(driver).tap(x=707, y=2467).perform()
time.sleep(1)
TouchAction(driver).tap(x=960, y=1440).perform()

#######################################################################################################################
mobile = "18017700597"
AA = "\033[1;31mNO.15\033[0m " + mobile + " \033[1;31m开始\033[0m"
print(AA)
nowtime = time.strftime('%H:%M:%S')
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
        time.sleep(1)
        edit_mobile = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/edit_phone")  # 选择手机号输入框
        edit_mobile.send_keys(mobile)
        time.sleep(1)
        TouchAction(driver).tap(x=1100, y=870).perform()  # 获取验证码
        time.sleep(2)
        # 获取验证码
        logincodeurl = "https://uc.crazyccy.com/login/main_login/testtool?key=sLQq2_jaKLknsqAwZ&type=1&mobile=" + mobile
        # print(logincodeurl)
        request = urllib.request.Request(logincodeurl)  # 构建请求url
        response = urllib.request.urlopen(request, context=context)  # ssl证书免验证加入,context = context# 打开请求url链接
        num = response.read()  # 读取页面返回信息，python3返回数据为bytes类型的对象 (即b为前缀, bytes类型)
        logincode = num.decode()
        edit_code = driver.find_element_by_id(
            "com.kamitu.drawsth.standalone.free.android:id/edit_identifyCode")  # 选择验证码输入框
        time.sleep(1)
        edit_code.send_keys(logincode)
        time.sleep(1)
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
        TouchAction(driver).tap(x=1270, y=655).perform()


check_signwindows()
time.sleep(2)

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
time.sleep(2)

TouchAction(driver).tap(x=439, y=2379).perform()  # 选择进入判官
time.sleep(1)
TouchAction(driver).tap(x=712, y=1342).perform()  # 选择开始挑战
time.sleep(3)

a = 11
while a > 0:
    time.sleep(8)
    TouchAction(driver).tap(x=671, y=1734).perform()  # 点击查看广告
    time.sleep(5)
    try:
        GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
    except NoSuchElementException:
        print("toutiaosdk广告")
        time.sleep(40)
        TouchAction(driver).tap(x=1285, y=139).perform()  # 关闭toutiao广告
        print(a)
        print("toutiaosdk广告关闭")
    else:
        print("GDTsdk广告")
        time.sleep(50)
        driver.back()  # GDTsdk广告按钮
        print(a)
        print("GDTsdk广告关闭")
    a -= 1

time.sleep(8)
driver.back()  # 判官中回到首页
time.sleep(1)
driver.back()
TouchAction(driver).tap(x=588, y=186).perform()  # 返回进入个人中心
time.sleep(2)
TouchAction(driver).tap(x=1275, y=243).perform()
time.sleep(1)
TouchAction(driver).tap(x=707, y=2467).perform()
time.sleep(1)
TouchAction(driver).tap(x=960, y=1440).perform()

#######################################################################################################################
mobile = "18017700596"
AA = "\033[1;31mNO.16\033[0m " + mobile + " \033[1;31m开始\033[0m"
print(AA)
nowtime = time.strftime('%H:%M:%S')
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
        time.sleep(1)
        edit_mobile = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/edit_phone")  # 选择手机号输入框
        edit_mobile.send_keys(mobile)
        time.sleep(1)
        TouchAction(driver).tap(x=1100, y=870).perform()  # 获取验证码
        time.sleep(2)
        # 获取验证码
        logincodeurl = "https://uc.crazyccy.com/login/main_login/testtool?key=sLQq2_jaKLknsqAwZ&type=1&mobile=" + mobile
        # print(logincodeurl)
        request = urllib.request.Request(logincodeurl)  # 构建请求url
        response = urllib.request.urlopen(request, context=context)  # ssl证书免验证加入,context = context# 打开请求url链接
        num = response.read()  # 读取页面返回信息，python3返回数据为bytes类型的对象 (即b为前缀, bytes类型)
        logincode = num.decode()
        edit_code = driver.find_element_by_id(
            "com.kamitu.drawsth.standalone.free.android:id/edit_identifyCode")  # 选择验证码输入框
        time.sleep(1)
        edit_code.send_keys(logincode)
        time.sleep(1)
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
        TouchAction(driver).tap(x=1270, y=655).perform()


check_signwindows()
time.sleep(2)

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
time.sleep(2)

TouchAction(driver).tap(x=439, y=2379).perform()  # 选择进入判官
time.sleep(1)
TouchAction(driver).tap(x=712, y=1342).perform()  # 选择开始挑战
time.sleep(3)

a = 11
while a > 0:
    time.sleep(8)
    TouchAction(driver).tap(x=671, y=1734).perform()  # 点击查看广告
    time.sleep(5)
    try:
        GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
    except NoSuchElementException:
        print("toutiaosdk广告")
        time.sleep(40)
        TouchAction(driver).tap(x=1285, y=139).perform()  # 关闭toutiao广告
        print(a)
        print("toutiaosdk广告关闭")
    else:
        print("GDTsdk广告")
        time.sleep(50)
        driver.back()  # GDTsdk广告按钮
        print(a)
        print("GDTsdk广告关闭")
    a -= 1

time.sleep(8)
driver.back()  # 判官中回到首页
time.sleep(1)
driver.back()
TouchAction(driver).tap(x=588, y=186).perform()  # 返回进入个人中心
time.sleep(2)
TouchAction(driver).tap(x=1275, y=243).perform()
time.sleep(1)
TouchAction(driver).tap(x=707, y=2467).perform()
time.sleep(1)
TouchAction(driver).tap(x=960, y=1440).perform()

#######################################################################################################################
mobile = "18017700550"
AA = "\033[1;31mNO.17\033[0m " + mobile + " \033[1;31m开始\033[0m"
print(AA)
nowtime = time.strftime('%H:%M:%S')
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
        time.sleep(1)
        edit_mobile = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/edit_phone")  # 选择手机号输入框
        edit_mobile.send_keys(mobile)
        time.sleep(1)
        TouchAction(driver).tap(x=1100, y=870).perform()  # 获取验证码
        time.sleep(2)
        # 获取验证码
        logincodeurl = "https://uc.crazyccy.com/login/main_login/testtool?key=sLQq2_jaKLknsqAwZ&type=1&mobile=" + mobile
        # print(logincodeurl)
        request = urllib.request.Request(logincodeurl)  # 构建请求url
        response = urllib.request.urlopen(request, context=context)  # ssl证书免验证加入,context = context# 打开请求url链接
        num = response.read()  # 读取页面返回信息，python3返回数据为bytes类型的对象 (即b为前缀, bytes类型)
        logincode = num.decode()
        edit_code = driver.find_element_by_id(
            "com.kamitu.drawsth.standalone.free.android:id/edit_identifyCode")  # 选择验证码输入框
        time.sleep(1)
        edit_code.send_keys(logincode)
        time.sleep(1)
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
        TouchAction(driver).tap(x=1270, y=655).perform()


check_signwindows()
time.sleep(2)

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
time.sleep(2)

TouchAction(driver).tap(x=439, y=2379).perform()  # 选择进入判官
time.sleep(1)
TouchAction(driver).tap(x=712, y=1342).perform()  # 选择开始挑战
time.sleep(3)

a = 11
while a > 0:
    time.sleep(8)
    TouchAction(driver).tap(x=671, y=1734).perform()  # 点击查看广告
    time.sleep(5)
    try:
        GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
    except NoSuchElementException:
        print("toutiaosdk广告")
        time.sleep(40)
        TouchAction(driver).tap(x=1285, y=139).perform()  # 关闭toutiao广告
        print(a)
        print("toutiaosdk广告关闭")
    else:
        print("GDTsdk广告")
        time.sleep(50)
        driver.back()  # GDTsdk广告按钮
        print(a)
        print("GDTsdk广告关闭")
    a -= 1

time.sleep(8)
driver.back()  # 判官中回到首页
time.sleep(1)
driver.back()
TouchAction(driver).tap(x=588, y=186).perform()  # 返回进入个人中心
time.sleep(2)
TouchAction(driver).tap(x=1275, y=243).perform()
time.sleep(1)
TouchAction(driver).tap(x=707, y=2467).perform()
time.sleep(1)
TouchAction(driver).tap(x=960, y=1440).perform()

#######################################################################################################################
mobile = "18017700537"
AA = "\033[1;31mNO.18\033[0m " + mobile + " \033[1;31m开始\033[0m"
print(AA)
nowtime = time.strftime('%H:%M:%S')
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
        time.sleep(1)
        edit_mobile = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/edit_phone")  # 选择手机号输入框
        edit_mobile.send_keys(mobile)
        time.sleep(1)
        TouchAction(driver).tap(x=1100, y=870).perform()  # 获取验证码
        time.sleep(2)
        # 获取验证码
        logincodeurl = "https://uc.crazyccy.com/login/main_login/testtool?key=sLQq2_jaKLknsqAwZ&type=1&mobile=" + mobile
        # print(logincodeurl)
        request = urllib.request.Request(logincodeurl)  # 构建请求url
        response = urllib.request.urlopen(request, context=context)  # ssl证书免验证加入,context = context# 打开请求url链接
        num = response.read()  # 读取页面返回信息，python3返回数据为bytes类型的对象 (即b为前缀, bytes类型)
        logincode = num.decode()
        edit_code = driver.find_element_by_id(
            "com.kamitu.drawsth.standalone.free.android:id/edit_identifyCode")  # 选择验证码输入框
        time.sleep(1)
        edit_code.send_keys(logincode)
        time.sleep(1)
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
        TouchAction(driver).tap(x=1270, y=655).perform()


check_signwindows()
time.sleep(2)

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
time.sleep(2)

TouchAction(driver).tap(x=439, y=2379).perform()  # 选择进入判官
time.sleep(1)
TouchAction(driver).tap(x=712, y=1342).perform()  # 选择开始挑战
time.sleep(3)

a = 11
while a > 0:
    time.sleep(8)
    TouchAction(driver).tap(x=671, y=1734).perform()  # 点击查看广告
    time.sleep(5)
    try:
        GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
    except NoSuchElementException:
        print("toutiaosdk广告")
        time.sleep(40)
        TouchAction(driver).tap(x=1285, y=139).perform()  # 关闭toutiao广告
        print(a)
        print("toutiaosdk广告关闭")
    else:
        print("GDTsdk广告")
        time.sleep(50)
        driver.back()  # GDTsdk广告按钮
        print(a)
        print("GDTsdk广告关闭")
    a -= 1

time.sleep(8)
driver.back()  # 判官中回到首页
time.sleep(1)
driver.back()
TouchAction(driver).tap(x=588, y=186).perform()  # 返回进入个人中心
time.sleep(2)
TouchAction(driver).tap(x=1275, y=243).perform()
time.sleep(1)
TouchAction(driver).tap(x=707, y=2467).perform()
time.sleep(1)
TouchAction(driver).tap(x=960, y=1440).perform()

#######################################################################################################################
mobile = "18017700536"
AA = "\033[1;31mNO.19\033[0m " + mobile + " \033[1;31m开始\033[0m"
print(AA)
nowtime = time.strftime('%H:%M:%S')
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
        time.sleep(1)
        edit_mobile = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/edit_phone")  # 选择手机号输入框
        edit_mobile.send_keys(mobile)
        time.sleep(1)
        TouchAction(driver).tap(x=1100, y=870).perform()  # 获取验证码
        time.sleep(2)
        # 获取验证码
        logincodeurl = "https://uc.crazyccy.com/login/main_login/testtool?key=sLQq2_jaKLknsqAwZ&type=1&mobile=" + mobile
        # print(logincodeurl)
        request = urllib.request.Request(logincodeurl)  # 构建请求url
        response = urllib.request.urlopen(request, context=context)  # ssl证书免验证加入,context = context# 打开请求url链接
        num = response.read()  # 读取页面返回信息，python3返回数据为bytes类型的对象 (即b为前缀, bytes类型)
        logincode = num.decode()
        edit_code = driver.find_element_by_id(
            "com.kamitu.drawsth.standalone.free.android:id/edit_identifyCode")  # 选择验证码输入框
        time.sleep(1)
        edit_code.send_keys(logincode)
        time.sleep(1)
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
        TouchAction(driver).tap(x=1270, y=655).perform()


check_signwindows()
time.sleep(2)

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
time.sleep(2)

TouchAction(driver).tap(x=439, y=2379).perform()  # 选择进入判官
time.sleep(1)
TouchAction(driver).tap(x=712, y=1342).perform()  # 选择开始挑战
time.sleep(3)

a = 11
while a > 0:
    time.sleep(8)
    TouchAction(driver).tap(x=671, y=1734).perform()  # 点击查看广告
    time.sleep(5)
    try:
        GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
    except NoSuchElementException:
        print("toutiaosdk广告")
        time.sleep(40)
        TouchAction(driver).tap(x=1285, y=139).perform()  # 关闭toutiao广告
        print(a)
        print("toutiaosdk广告关闭")
    else:
        print("GDTsdk广告")
        time.sleep(50)
        driver.back()  # GDTsdk广告按钮
        print(a)
        print("GDTsdk广告关闭")
    a -= 1

time.sleep(8)
driver.back()  # 判官中回到首页
time.sleep(1)
driver.back()
TouchAction(driver).tap(x=588, y=186).perform()  # 返回进入个人中心
time.sleep(2)
TouchAction(driver).tap(x=1275, y=243).perform()
time.sleep(1)
TouchAction(driver).tap(x=707, y=2467).perform()
time.sleep(1)
TouchAction(driver).tap(x=960, y=1440).perform()

#######################################################################################################################
mobile = "18017700540"
AA = "\033[1;31mNO.20\033[0m " + mobile + " \033[1;31m开始\033[0m"
print(AA)
nowtime = time.strftime('%H:%M:%S')
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
        time.sleep(1)
        edit_mobile = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/edit_phone")  # 选择手机号输入框
        edit_mobile.send_keys(mobile)
        time.sleep(1)
        TouchAction(driver).tap(x=1100, y=870).perform()  # 获取验证码
        time.sleep(2)
        # 获取验证码
        logincodeurl = "https://uc.crazyccy.com/login/main_login/testtool?key=sLQq2_jaKLknsqAwZ&type=1&mobile=" + mobile
        # print(logincodeurl)
        request = urllib.request.Request(logincodeurl)  # 构建请求url
        response = urllib.request.urlopen(request, context=context)  # ssl证书免验证加入,context = context# 打开请求url链接
        num = response.read()  # 读取页面返回信息，python3返回数据为bytes类型的对象 (即b为前缀, bytes类型)
        logincode = num.decode()
        edit_code = driver.find_element_by_id(
            "com.kamitu.drawsth.standalone.free.android:id/edit_identifyCode")  # 选择验证码输入框
        time.sleep(1)
        edit_code.send_keys(logincode)
        time.sleep(1)
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
        TouchAction(driver).tap(x=1270, y=655).perform()


check_signwindows()
time.sleep(2)

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
time.sleep(2)

TouchAction(driver).tap(x=439, y=2379).perform()  # 选择进入判官
time.sleep(1)
TouchAction(driver).tap(x=712, y=1342).perform()  # 选择开始挑战
time.sleep(3)

a = 11
while a > 0:
    time.sleep(8)
    TouchAction(driver).tap(x=671, y=1734).perform()  # 点击查看广告
    time.sleep(5)
    try:
        GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
    except NoSuchElementException:
        print("toutiaosdk广告")
        time.sleep(40)
        TouchAction(driver).tap(x=1285, y=139).perform()  # 关闭toutiao广告
        print(a)
        print("toutiaosdk广告关闭")
    else:
        print("GDTsdk广告")
        time.sleep(50)
        driver.back()  # GDTsdk广告按钮
        print(a)
        print("GDTsdk广告关闭")
    a -= 1

time.sleep(8)
driver.back()  # 判官中回到首页
time.sleep(1)
driver.back()
TouchAction(driver).tap(x=588, y=186).perform()  # 返回进入个人中心
time.sleep(2)
TouchAction(driver).tap(x=1275, y=243).perform()
time.sleep(1)
TouchAction(driver).tap(x=707, y=2467).perform()
time.sleep(1)
TouchAction(driver).tap(x=960, y=1440).perform()

#######################################################################################################################
mobile = "18017700533"
AA = "\033[1;31mNO.21\033[0m " + mobile + " \033[1;31m开始\033[0m"
print(AA)
nowtime = time.strftime('%H:%M:%S')
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
        time.sleep(1)
        edit_mobile = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/edit_phone")  # 选择手机号输入框
        edit_mobile.send_keys(mobile)
        time.sleep(1)
        TouchAction(driver).tap(x=1100, y=870).perform()  # 获取验证码
        time.sleep(2)
        # 获取验证码
        logincodeurl = "https://uc.crazyccy.com/login/main_login/testtool?key=sLQq2_jaKLknsqAwZ&type=1&mobile=" + mobile
        # print(logincodeurl)
        request = urllib.request.Request(logincodeurl)  # 构建请求url
        response = urllib.request.urlopen(request, context=context)  # ssl证书免验证加入,context = context# 打开请求url链接
        num = response.read()  # 读取页面返回信息，python3返回数据为bytes类型的对象 (即b为前缀, bytes类型)
        logincode = num.decode()
        edit_code = driver.find_element_by_id(
            "com.kamitu.drawsth.standalone.free.android:id/edit_identifyCode")  # 选择验证码输入框
        time.sleep(1)
        edit_code.send_keys(logincode)
        time.sleep(1)
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
        TouchAction(driver).tap(x=1270, y=655).perform()


check_signwindows()
time.sleep(2)

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
time.sleep(2)

TouchAction(driver).tap(x=439, y=2379).perform()  # 选择进入判官
time.sleep(1)
TouchAction(driver).tap(x=712, y=1342).perform()  # 选择开始挑战
time.sleep(3)

a = 11
while a > 0:
    time.sleep(8)
    TouchAction(driver).tap(x=671, y=1734).perform()  # 点击查看广告
    time.sleep(5)
    try:
        GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
    except NoSuchElementException:
        print("toutiaosdk广告")
        time.sleep(40)
        TouchAction(driver).tap(x=1285, y=139).perform()  # 关闭toutiao广告
        print(a)
        print("toutiaosdk广告关闭")
    else:
        print("GDTsdk广告")
        time.sleep(50)
        driver.back()  # GDTsdk广告按钮
        print(a)
        print("GDTsdk广告关闭")
    a -= 1

time.sleep(8)
driver.back()  # 判官中回到首页
time.sleep(1)
driver.back()
TouchAction(driver).tap(x=588, y=186).perform()  # 返回进入个人中心
time.sleep(2)
TouchAction(driver).tap(x=1275, y=243).perform()
time.sleep(1)
TouchAction(driver).tap(x=707, y=2467).perform()
time.sleep(1)
TouchAction(driver).tap(x=960, y=1440).perform()

#######################################################################################################################
mobile = "18017700526"
AA = "\033[1;31mNO.22\033[0m " + mobile + " \033[1;31m开始\033[0m"
print(AA)
nowtime = time.strftime('%H:%M:%S')
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
        time.sleep(1)
        edit_mobile = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/edit_phone")  # 选择手机号输入框
        edit_mobile.send_keys(mobile)
        time.sleep(1)
        TouchAction(driver).tap(x=1100, y=870).perform()  # 获取验证码
        time.sleep(2)
        # 获取验证码
        logincodeurl = "https://uc.crazyccy.com/login/main_login/testtool?key=sLQq2_jaKLknsqAwZ&type=1&mobile=" + mobile
        # print(logincodeurl)
        request = urllib.request.Request(logincodeurl)  # 构建请求url
        response = urllib.request.urlopen(request, context=context)  # ssl证书免验证加入,context = context# 打开请求url链接
        num = response.read()  # 读取页面返回信息，python3返回数据为bytes类型的对象 (即b为前缀, bytes类型)
        logincode = num.decode()
        edit_code = driver.find_element_by_id(
            "com.kamitu.drawsth.standalone.free.android:id/edit_identifyCode")  # 选择验证码输入框
        time.sleep(1)
        edit_code.send_keys(logincode)
        time.sleep(1)
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
        TouchAction(driver).tap(x=1270, y=655).perform()


check_signwindows()
time.sleep(2)

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
time.sleep(2)

TouchAction(driver).tap(x=439, y=2379).perform()  # 选择进入判官
time.sleep(1)
TouchAction(driver).tap(x=712, y=1342).perform()  # 选择开始挑战
time.sleep(3)

a = 11
while a > 0:
    time.sleep(8)
    TouchAction(driver).tap(x=671, y=1734).perform()  # 点击查看广告
    time.sleep(5)
    try:
        GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
    except NoSuchElementException:
        print("toutiaosdk广告")
        time.sleep(40)
        TouchAction(driver).tap(x=1285, y=139).perform()  # 关闭toutiao广告
        print(a)
        print("toutiaosdk广告关闭")
    else:
        print("GDTsdk广告")
        time.sleep(50)
        driver.back()  # GDTsdk广告按钮
        print(a)
        print("GDTsdk广告关闭")
    a -= 1

time.sleep(8)
driver.back()  # 判官中回到首页
time.sleep(1)
driver.back()
TouchAction(driver).tap(x=588, y=186).perform()  # 返回进入个人中心
time.sleep(2)
TouchAction(driver).tap(x=1275, y=243).perform()
time.sleep(1)
TouchAction(driver).tap(x=707, y=2467).perform()
time.sleep(1)
TouchAction(driver).tap(x=960, y=1440).perform()

#######################################################################################################################
mobile = "18017700516"
AA = "\033[1;31mNO.23\033[0m " + mobile + " \033[1;31m开始\033[0m"
print(AA)
nowtime = time.strftime('%H:%M:%S')
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
        time.sleep(1)
        edit_mobile = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/edit_phone")  # 选择手机号输入框
        edit_mobile.send_keys(mobile)
        time.sleep(1)
        TouchAction(driver).tap(x=1100, y=870).perform()  # 获取验证码
        time.sleep(2)
        # 获取验证码
        logincodeurl = "https://uc.crazyccy.com/login/main_login/testtool?key=sLQq2_jaKLknsqAwZ&type=1&mobile=" + mobile
        # print(logincodeurl)
        request = urllib.request.Request(logincodeurl)  # 构建请求url
        response = urllib.request.urlopen(request, context=context)  # ssl证书免验证加入,context = context# 打开请求url链接
        num = response.read()  # 读取页面返回信息，python3返回数据为bytes类型的对象 (即b为前缀, bytes类型)
        logincode = num.decode()
        edit_code = driver.find_element_by_id(
            "com.kamitu.drawsth.standalone.free.android:id/edit_identifyCode")  # 选择验证码输入框
        time.sleep(1)
        edit_code.send_keys(logincode)
        time.sleep(1)
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
        TouchAction(driver).tap(x=1270, y=655).perform()


check_signwindows()
time.sleep(2)

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
time.sleep(2)

TouchAction(driver).tap(x=439, y=2379).perform()  # 选择进入判官
time.sleep(1)
TouchAction(driver).tap(x=712, y=1342).perform()  # 选择开始挑战
time.sleep(3)

a = 11
while a > 0:
    time.sleep(8)
    TouchAction(driver).tap(x=671, y=1734).perform()  # 点击查看广告
    time.sleep(5)
    try:
        GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
    except NoSuchElementException:
        print("toutiaosdk广告")
        time.sleep(40)
        TouchAction(driver).tap(x=1285, y=139).perform()  # 关闭toutiao广告
        print(a)
        print("toutiaosdk广告关闭")
    else:
        print("GDTsdk广告")
        time.sleep(50)
        driver.back()  # GDTsdk广告按钮
        print(a)
        print("GDTsdk广告关闭")
    a -= 1

time.sleep(8)
driver.back()  # 判官中回到首页
time.sleep(1)
driver.back()
TouchAction(driver).tap(x=588, y=186).perform()  # 返回进入个人中心
time.sleep(2)
TouchAction(driver).tap(x=1275, y=243).perform()
time.sleep(1)
TouchAction(driver).tap(x=707, y=2467).perform()
time.sleep(1)
TouchAction(driver).tap(x=960, y=1440).perform()

#######################################################################################################################
mobile = "18017700515"
AA = "\033[1;31mNO.24\033[0m " + mobile + " \033[1;31m开始\033[0m"
print(AA)
nowtime = time.strftime('%H:%M:%S')
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
        time.sleep(1)
        edit_mobile = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/edit_phone")  # 选择手机号输入框
        edit_mobile.send_keys(mobile)
        time.sleep(1)
        TouchAction(driver).tap(x=1100, y=870).perform()  # 获取验证码
        time.sleep(2)
        # 获取验证码
        logincodeurl = "https://uc.crazyccy.com/login/main_login/testtool?key=sLQq2_jaKLknsqAwZ&type=1&mobile=" + mobile
        # print(logincodeurl)
        request = urllib.request.Request(logincodeurl)  # 构建请求url
        response = urllib.request.urlopen(request, context=context)  # ssl证书免验证加入,context = context# 打开请求url链接
        num = response.read()  # 读取页面返回信息，python3返回数据为bytes类型的对象 (即b为前缀, bytes类型)
        logincode = num.decode()
        edit_code = driver.find_element_by_id(
            "com.kamitu.drawsth.standalone.free.android:id/edit_identifyCode")  # 选择验证码输入框
        time.sleep(1)
        edit_code.send_keys(logincode)
        time.sleep(1)
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
        TouchAction(driver).tap(x=1270, y=655).perform()


check_signwindows()
time.sleep(2)

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
time.sleep(2)

TouchAction(driver).tap(x=439, y=2379).perform()  # 选择进入判官
time.sleep(1)
TouchAction(driver).tap(x=712, y=1342).perform()  # 选择开始挑战
time.sleep(3)

a = 11
while a > 0:
    time.sleep(8)
    TouchAction(driver).tap(x=671, y=1734).perform()  # 点击查看广告
    time.sleep(5)
    try:
        GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
    except NoSuchElementException:
        print("toutiaosdk广告")
        time.sleep(40)
        TouchAction(driver).tap(x=1285, y=139).perform()  # 关闭toutiao广告
        print(a)
        print("toutiaosdk广告关闭")
    else:
        print("GDTsdk广告")
        time.sleep(50)
        driver.back()  # GDTsdk广告按钮
        print(a)
        print("GDTsdk广告关闭")
    a -= 1

time.sleep(8)
driver.back()  # 判官中回到首页
time.sleep(1)
driver.back()
TouchAction(driver).tap(x=588, y=186).perform()  # 返回进入个人中心
time.sleep(2)
TouchAction(driver).tap(x=1275, y=243).perform()
time.sleep(1)
TouchAction(driver).tap(x=707, y=2467).perform()
time.sleep(1)
TouchAction(driver).tap(x=960, y=1440).perform()

#######################################################################################################################
mobile = "18017700475"
AA = "\033[1;31mNO.25\033[0m " + mobile + " \033[1;31m开始\033[0m"
print(AA)
nowtime = time.strftime('%H:%M:%S')
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
        time.sleep(1)
        edit_mobile = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/edit_phone")  # 选择手机号输入框
        edit_mobile.send_keys(mobile)
        time.sleep(1)
        TouchAction(driver).tap(x=1100, y=870).perform()  # 获取验证码
        time.sleep(2)
        # 获取验证码
        logincodeurl = "https://uc.crazyccy.com/login/main_login/testtool?key=sLQq2_jaKLknsqAwZ&type=1&mobile=" + mobile
        # print(logincodeurl)
        request = urllib.request.Request(logincodeurl)  # 构建请求url
        response = urllib.request.urlopen(request, context=context)  # ssl证书免验证加入,context = context# 打开请求url链接
        num = response.read()  # 读取页面返回信息，python3返回数据为bytes类型的对象 (即b为前缀, bytes类型)
        logincode = num.decode()
        edit_code = driver.find_element_by_id(
            "com.kamitu.drawsth.standalone.free.android:id/edit_identifyCode")  # 选择验证码输入框
        time.sleep(1)
        edit_code.send_keys(logincode)
        time.sleep(1)
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
        TouchAction(driver).tap(x=1270, y=655).perform()


check_signwindows()
time.sleep(2)

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
time.sleep(2)

TouchAction(driver).tap(x=439, y=2379).perform()  # 选择进入判官
time.sleep(1)
TouchAction(driver).tap(x=712, y=1342).perform()  # 选择开始挑战
time.sleep(3)

a = 11
while a > 0:
    time.sleep(8)
    TouchAction(driver).tap(x=671, y=1734).perform()  # 点击查看广告
    time.sleep(5)
    try:
        GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
    except NoSuchElementException:
        print("toutiaosdk广告")
        time.sleep(40)
        TouchAction(driver).tap(x=1285, y=139).perform()  # 关闭toutiao广告
        print(a)
        print("toutiaosdk广告关闭")
    else:
        print("GDTsdk广告")
        time.sleep(50)
        driver.back()  # GDTsdk广告按钮
        print(a)
        print("GDTsdk广告关闭")
    a -= 1

time.sleep(8)
driver.back()  # 判官中回到首页
time.sleep(1)
driver.back()
TouchAction(driver).tap(x=588, y=186).perform()  # 返回进入个人中心
time.sleep(2)
TouchAction(driver).tap(x=1275, y=243).perform()
time.sleep(1)
TouchAction(driver).tap(x=707, y=2467).perform()
time.sleep(1)
TouchAction(driver).tap(x=960, y=1440).perform()

#######################################################################################################################
mobile = "18017700710"
AA = "\033[1;31mNO.26\033[0m " + mobile + " \033[1;31m开始\033[0m"
print(AA)
nowtime = time.strftime('%H:%M:%S')
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
        time.sleep(1)
        edit_mobile = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/edit_phone")  # 选择手机号输入框
        edit_mobile.send_keys(mobile)
        time.sleep(1)
        TouchAction(driver).tap(x=1100, y=870).perform()  # 获取验证码
        time.sleep(2)
        # 获取验证码
        logincodeurl = "https://uc.crazyccy.com/login/main_login/testtool?key=sLQq2_jaKLknsqAwZ&type=1&mobile=" + mobile
        # print(logincodeurl)
        request = urllib.request.Request(logincodeurl)  # 构建请求url
        response = urllib.request.urlopen(request, context=context)  # ssl证书免验证加入,context = context# 打开请求url链接
        num = response.read()  # 读取页面返回信息，python3返回数据为bytes类型的对象 (即b为前缀, bytes类型)
        logincode = num.decode()
        edit_code = driver.find_element_by_id(
            "com.kamitu.drawsth.standalone.free.android:id/edit_identifyCode")  # 选择验证码输入框
        time.sleep(1)
        edit_code.send_keys(logincode)
        time.sleep(1)
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
        TouchAction(driver).tap(x=1270, y=655).perform()


check_signwindows()
time.sleep(2)

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
time.sleep(2)

TouchAction(driver).tap(x=439, y=2379).perform()  # 选择进入判官
time.sleep(1)
TouchAction(driver).tap(x=712, y=1342).perform()  # 选择开始挑战
time.sleep(3)

a = 11
while a > 0:
    time.sleep(8)
    TouchAction(driver).tap(x=671, y=1734).perform()  # 点击查看广告
    time.sleep(5)
    try:
        GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
    except NoSuchElementException:
        print("toutiaosdk广告")
        time.sleep(40)
        TouchAction(driver).tap(x=1285, y=139).perform()  # 关闭toutiao广告
        print(a)
        print("toutiaosdk广告关闭")
    else:
        print("GDTsdk广告")
        time.sleep(50)
        driver.back()  # GDTsdk广告按钮
        print(a)
        print("GDTsdk广告关闭")
    a -= 1

time.sleep(8)
driver.back()  # 判官中回到首页
time.sleep(1)
driver.back()
TouchAction(driver).tap(x=588, y=186).perform()  # 返回进入个人中心
time.sleep(2)
TouchAction(driver).tap(x=1275, y=243).perform()
time.sleep(1)
TouchAction(driver).tap(x=707, y=2467).perform()
time.sleep(1)
TouchAction(driver).tap(x=960, y=1440).perform()

#######################################################################################################################
mobile = "18017700580"
AA = "\033[1;31mNO.27\033[0m " + mobile + " \033[1;31m开始\033[0m"
print(AA)
nowtime = time.strftime('%H:%M:%S')
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
        time.sleep(1)
        edit_mobile = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/edit_phone")  # 选择手机号输入框
        edit_mobile.send_keys(mobile)
        time.sleep(1)
        TouchAction(driver).tap(x=1100, y=870).perform()  # 获取验证码
        time.sleep(2)
        # 获取验证码
        logincodeurl = "https://uc.crazyccy.com/login/main_login/testtool?key=sLQq2_jaKLknsqAwZ&type=1&mobile=" + mobile
        # print(logincodeurl)
        request = urllib.request.Request(logincodeurl)  # 构建请求url
        response = urllib.request.urlopen(request, context=context)  # ssl证书免验证加入,context = context# 打开请求url链接
        num = response.read()  # 读取页面返回信息，python3返回数据为bytes类型的对象 (即b为前缀, bytes类型)
        logincode = num.decode()
        edit_code = driver.find_element_by_id(
            "com.kamitu.drawsth.standalone.free.android:id/edit_identifyCode")  # 选择验证码输入框
        time.sleep(1)
        edit_code.send_keys(logincode)
        time.sleep(1)
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
        TouchAction(driver).tap(x=1270, y=655).perform()


check_signwindows()
time.sleep(2)

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
time.sleep(2)

TouchAction(driver).tap(x=439, y=2379).perform()  # 选择进入判官
time.sleep(1)
TouchAction(driver).tap(x=712, y=1342).perform()  # 选择开始挑战
time.sleep(3)

a = 11
while a > 0:
    time.sleep(8)
    TouchAction(driver).tap(x=671, y=1734).perform()  # 点击查看广告
    time.sleep(5)
    try:
        GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
    except NoSuchElementException:
        print("toutiaosdk广告")
        time.sleep(40)
        TouchAction(driver).tap(x=1285, y=139).perform()  # 关闭toutiao广告
        print(a)
        print("toutiaosdk广告关闭")
    else:
        print("GDTsdk广告")
        time.sleep(50)
        driver.back()  # GDTsdk广告按钮
        print(a)
        print("GDTsdk广告关闭")
    a -= 1

time.sleep(8)
driver.back()  # 判官中回到首页
time.sleep(1)
driver.back()
TouchAction(driver).tap(x=588, y=186).perform()  # 返回进入个人中心
time.sleep(2)
TouchAction(driver).tap(x=1275, y=243).perform()
time.sleep(1)
TouchAction(driver).tap(x=707, y=2467).perform()
time.sleep(1)
TouchAction(driver).tap(x=960, y=1440).perform()

#######################################################################################################################
mobile = "18017700530"
AA = "\033[1;31mNO.28\033[0m " + mobile + " \033[1;31m开始\033[0m"
print(AA)
nowtime = time.strftime('%H:%M:%S')
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
        time.sleep(1)
        edit_mobile = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/edit_phone")  # 选择手机号输入框
        edit_mobile.send_keys(mobile)
        time.sleep(1)
        TouchAction(driver).tap(x=1100, y=870).perform()  # 获取验证码
        time.sleep(2)
        # 获取验证码
        logincodeurl = "https://uc.crazyccy.com/login/main_login/testtool?key=sLQq2_jaKLknsqAwZ&type=1&mobile=" + mobile
        # print(logincodeurl)
        request = urllib.request.Request(logincodeurl)  # 构建请求url
        response = urllib.request.urlopen(request, context=context)  # ssl证书免验证加入,context = context# 打开请求url链接
        num = response.read()  # 读取页面返回信息，python3返回数据为bytes类型的对象 (即b为前缀, bytes类型)
        logincode = num.decode()
        edit_code = driver.find_element_by_id(
            "com.kamitu.drawsth.standalone.free.android:id/edit_identifyCode")  # 选择验证码输入框
        time.sleep(1)
        edit_code.send_keys(logincode)
        time.sleep(1)
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
        TouchAction(driver).tap(x=1270, y=655).perform()


check_signwindows()
time.sleep(2)

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
time.sleep(2)

TouchAction(driver).tap(x=439, y=2379).perform()  # 选择进入判官
time.sleep(1)
TouchAction(driver).tap(x=712, y=1342).perform()  # 选择开始挑战
time.sleep(3)

a = 11
while a > 0:
    time.sleep(8)
    TouchAction(driver).tap(x=671, y=1734).perform()  # 点击查看广告
    time.sleep(5)
    try:
        GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
    except NoSuchElementException:
        print("toutiaosdk广告")
        time.sleep(40)
        TouchAction(driver).tap(x=1285, y=139).perform()  # 关闭toutiao广告
        print(a)
        print("toutiaosdk广告关闭")
    else:
        print("GDTsdk广告")
        time.sleep(50)
        driver.back()  # GDTsdk广告按钮
        print(a)
        print("GDTsdk广告关闭")
    a -= 1

time.sleep(8)
driver.back()  # 判官中回到首页
time.sleep(1)
driver.back()
TouchAction(driver).tap(x=588, y=186).perform()  # 返回进入个人中心
time.sleep(2)
TouchAction(driver).tap(x=1275, y=243).perform()
time.sleep(1)
TouchAction(driver).tap(x=707, y=2467).perform()
time.sleep(1)
TouchAction(driver).tap(x=960, y=1440).perform()

#######################################################################################################################
mobile = "18017700722"
AA = "\033[1;31mNO.29\033[0m " + mobile + " \033[1;31m开始\033[0m"
print(AA)
nowtime = time.strftime('%H:%M:%S')
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
        time.sleep(1)
        edit_mobile = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/edit_phone")  # 选择手机号输入框
        edit_mobile.send_keys(mobile)
        time.sleep(1)
        TouchAction(driver).tap(x=1100, y=870).perform()  # 获取验证码
        time.sleep(2)
        # 获取验证码
        logincodeurl = "https://uc.crazyccy.com/login/main_login/testtool?key=sLQq2_jaKLknsqAwZ&type=1&mobile=" + mobile
        # print(logincodeurl)
        request = urllib.request.Request(logincodeurl)  # 构建请求url
        response = urllib.request.urlopen(request, context=context)  # ssl证书免验证加入,context = context# 打开请求url链接
        num = response.read()  # 读取页面返回信息，python3返回数据为bytes类型的对象 (即b为前缀, bytes类型)
        logincode = num.decode()
        edit_code = driver.find_element_by_id(
            "com.kamitu.drawsth.standalone.free.android:id/edit_identifyCode")  # 选择验证码输入框
        time.sleep(1)
        edit_code.send_keys(logincode)
        time.sleep(1)
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
        TouchAction(driver).tap(x=1270, y=655).perform()


check_signwindows()
time.sleep(2)

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
time.sleep(2)

TouchAction(driver).tap(x=439, y=2379).perform()  # 选择进入判官
time.sleep(1)
TouchAction(driver).tap(x=712, y=1342).perform()  # 选择开始挑战
time.sleep(3)

a = 11
while a > 0:
    time.sleep(8)
    TouchAction(driver).tap(x=671, y=1734).perform()  # 点击查看广告
    time.sleep(5)
    try:
        GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
    except NoSuchElementException:
        print("toutiaosdk广告")
        time.sleep(40)
        TouchAction(driver).tap(x=1285, y=139).perform()  # 关闭toutiao广告
        print(a)
        print("toutiaosdk广告关闭")
    else:
        print("GDTsdk广告")
        time.sleep(50)
        driver.back()  # GDTsdk广告按钮
        print(a)
        print("GDTsdk广告关闭")
    a -= 1

time.sleep(8)
driver.back()  # 判官中回到首页
time.sleep(1)
driver.back()
TouchAction(driver).tap(x=588, y=186).perform()  # 返回进入个人中心
time.sleep(2)
TouchAction(driver).tap(x=1275, y=243).perform()
time.sleep(1)
TouchAction(driver).tap(x=707, y=2467).perform()
time.sleep(1)
TouchAction(driver).tap(x=960, y=1440).perform()

#######################################################################################################################
mobile = "18017700713"
AA = "\033[1;31mNO.30\033[0m " + mobile + " \033[1;31m开始\033[0m"
print(AA)
nowtime = time.strftime('%H:%M:%S')
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
        time.sleep(1)
        edit_mobile = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/edit_phone")  # 选择手机号输入框
        edit_mobile.send_keys(mobile)
        time.sleep(1)
        TouchAction(driver).tap(x=1100, y=870).perform()  # 获取验证码
        time.sleep(2)
        # 获取验证码
        logincodeurl = "https://uc.crazyccy.com/login/main_login/testtool?key=sLQq2_jaKLknsqAwZ&type=1&mobile=" + mobile
        # print(logincodeurl)
        request = urllib.request.Request(logincodeurl)  # 构建请求url
        response = urllib.request.urlopen(request, context=context)  # ssl证书免验证加入,context = context# 打开请求url链接
        num = response.read()  # 读取页面返回信息，python3返回数据为bytes类型的对象 (即b为前缀, bytes类型)
        logincode = num.decode()
        edit_code = driver.find_element_by_id(
            "com.kamitu.drawsth.standalone.free.android:id/edit_identifyCode")  # 选择验证码输入框
        time.sleep(1)
        edit_code.send_keys(logincode)
        time.sleep(1)
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
        TouchAction(driver).tap(x=1270, y=655).perform()


check_signwindows()
time.sleep(2)

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
time.sleep(2)

TouchAction(driver).tap(x=439, y=2379).perform()  # 选择进入判官
time.sleep(1)
TouchAction(driver).tap(x=712, y=1342).perform()  # 选择开始挑战
time.sleep(3)

a = 11
while a > 0:
    time.sleep(8)
    TouchAction(driver).tap(x=671, y=1734).perform()  # 点击查看广告
    time.sleep(5)
    try:
        GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
    except NoSuchElementException:
        print("toutiaosdk广告")
        time.sleep(40)
        TouchAction(driver).tap(x=1285, y=139).perform()  # 关闭toutiao广告
        print(a)
        print("toutiaosdk广告关闭")
    else:
        print("GDTsdk广告")
        time.sleep(50)
        driver.back()  # GDTsdk广告按钮
        print(a)
        print("GDTsdk广告关闭")
    a -= 1

time.sleep(8)
driver.back()  # 判官中回到首页
time.sleep(1)
driver.back()
TouchAction(driver).tap(x=588, y=186).perform()  # 返回进入个人中心
time.sleep(2)
TouchAction(driver).tap(x=1275, y=243).perform()
time.sleep(1)
TouchAction(driver).tap(x=707, y=2467).perform()
time.sleep(1)
TouchAction(driver).tap(x=960, y=1440).perform()

#######################################################################################################################
mobile = "18017700595"
AA = "\033[1;31mNO.31\033[0m " + mobile + " \033[1;31m开始\033[0m"
print(AA)
nowtime = time.strftime('%H:%M:%S')
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
        time.sleep(1)
        edit_mobile = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/edit_phone")  # 选择手机号输入框
        edit_mobile.send_keys(mobile)
        time.sleep(1)
        TouchAction(driver).tap(x=1100, y=870).perform()  # 获取验证码
        time.sleep(2)
        # 获取验证码
        logincodeurl = "https://uc.crazyccy.com/login/main_login/testtool?key=sLQq2_jaKLknsqAwZ&type=1&mobile=" + mobile
        # print(logincodeurl)
        request = urllib.request.Request(logincodeurl)  # 构建请求url
        response = urllib.request.urlopen(request, context=context)  # ssl证书免验证加入,context = context# 打开请求url链接
        num = response.read()  # 读取页面返回信息，python3返回数据为bytes类型的对象 (即b为前缀, bytes类型)
        logincode = num.decode()
        edit_code = driver.find_element_by_id(
            "com.kamitu.drawsth.standalone.free.android:id/edit_identifyCode")  # 选择验证码输入框
        time.sleep(1)
        edit_code.send_keys(logincode)
        time.sleep(1)
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
        TouchAction(driver).tap(x=1270, y=655).perform()


check_signwindows()
time.sleep(2)

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
time.sleep(2)

TouchAction(driver).tap(x=439, y=2379).perform()  # 选择进入判官
time.sleep(1)
TouchAction(driver).tap(x=712, y=1342).perform()  # 选择开始挑战
time.sleep(3)

a = 11
while a > 0:
    time.sleep(8)
    TouchAction(driver).tap(x=671, y=1734).perform()  # 点击查看广告
    time.sleep(5)
    try:
        GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
    except NoSuchElementException:
        print("toutiaosdk广告")
        time.sleep(40)
        TouchAction(driver).tap(x=1285, y=139).perform()  # 关闭toutiao广告
        print(a)
        print("toutiaosdk广告关闭")
    else:
        print("GDTsdk广告")
        time.sleep(50)
        driver.back()  # GDTsdk广告按钮
        print(a)
        print("GDTsdk广告关闭")
    a -= 1

time.sleep(8)
driver.back()  # 判官中回到首页
time.sleep(1)
driver.back()
TouchAction(driver).tap(x=588, y=186).perform()  # 返回进入个人中心
time.sleep(2)
TouchAction(driver).tap(x=1275, y=243).perform()
time.sleep(1)
TouchAction(driver).tap(x=707, y=2467).perform()
time.sleep(1)
TouchAction(driver).tap(x=960, y=1440).perform()

#######################################################################################################################
mobile = "18017700571"
AA = "\033[1;31mNO.32\033[0m " + mobile + " \033[1;31m开始\033[0m"
print(AA)
nowtime = time.strftime('%H:%M:%S')
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
        time.sleep(1)
        edit_mobile = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/edit_phone")  # 选择手机号输入框
        edit_mobile.send_keys(mobile)
        time.sleep(1)
        TouchAction(driver).tap(x=1100, y=870).perform()  # 获取验证码
        time.sleep(2)
        # 获取验证码
        logincodeurl = "https://uc.crazyccy.com/login/main_login/testtool?key=sLQq2_jaKLknsqAwZ&type=1&mobile=" + mobile
        # print(logincodeurl)
        request = urllib.request.Request(logincodeurl)  # 构建请求url
        response = urllib.request.urlopen(request, context=context)  # ssl证书免验证加入,context = context# 打开请求url链接
        num = response.read()  # 读取页面返回信息，python3返回数据为bytes类型的对象 (即b为前缀, bytes类型)
        logincode = num.decode()
        edit_code = driver.find_element_by_id(
            "com.kamitu.drawsth.standalone.free.android:id/edit_identifyCode")  # 选择验证码输入框
        time.sleep(1)
        edit_code.send_keys(logincode)
        time.sleep(1)
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
        TouchAction(driver).tap(x=1270, y=655).perform()


check_signwindows()
time.sleep(2)

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
time.sleep(2)

TouchAction(driver).tap(x=439, y=2379).perform()  # 选择进入判官
time.sleep(1)
TouchAction(driver).tap(x=712, y=1342).perform()  # 选择开始挑战
time.sleep(3)

a = 11
while a > 0:
    time.sleep(8)
    TouchAction(driver).tap(x=671, y=1734).perform()  # 点击查看广告
    time.sleep(5)
    try:
        GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
    except NoSuchElementException:
        print("toutiaosdk广告")
        time.sleep(40)
        TouchAction(driver).tap(x=1285, y=139).perform()  # 关闭toutiao广告
        print(a)
        print("toutiaosdk广告关闭")
    else:
        print("GDTsdk广告")
        time.sleep(50)
        driver.back()  # GDTsdk广告按钮
        print(a)
        print("GDTsdk广告关闭")
    a -= 1

time.sleep(8)
driver.back()  # 判官中回到首页
time.sleep(1)
driver.back()
TouchAction(driver).tap(x=588, y=186).perform()  # 返回进入个人中心
time.sleep(2)
TouchAction(driver).tap(x=1275, y=243).perform()
time.sleep(1)
TouchAction(driver).tap(x=707, y=2467).perform()
time.sleep(1)
TouchAction(driver).tap(x=960, y=1440).perform()

#######################################################################################################################
mobile = "18017700477"
AA = "\033[1;31mNO.33\033[0m " + mobile + " \033[1;31m开始\033[0m"
print(AA)
nowtime = time.strftime('%H:%M:%S')
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
        time.sleep(1)
        edit_mobile = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/edit_phone")  # 选择手机号输入框
        edit_mobile.send_keys(mobile)
        time.sleep(1)
        TouchAction(driver).tap(x=1100, y=870).perform()  # 获取验证码
        time.sleep(2)
        # 获取验证码
        logincodeurl = "https://uc.crazyccy.com/login/main_login/testtool?key=sLQq2_jaKLknsqAwZ&type=1&mobile=" + mobile
        # print(logincodeurl)
        request = urllib.request.Request(logincodeurl)  # 构建请求url
        response = urllib.request.urlopen(request, context=context)  # ssl证书免验证加入,context = context# 打开请求url链接
        num = response.read()  # 读取页面返回信息，python3返回数据为bytes类型的对象 (即b为前缀, bytes类型)
        logincode = num.decode()
        edit_code = driver.find_element_by_id(
            "com.kamitu.drawsth.standalone.free.android:id/edit_identifyCode")  # 选择验证码输入框
        time.sleep(1)
        edit_code.send_keys(logincode)
        time.sleep(1)
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
        TouchAction(driver).tap(x=1270, y=655).perform()


check_signwindows()
time.sleep(2)

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
time.sleep(2)

TouchAction(driver).tap(x=439, y=2379).perform()  # 选择进入判官
time.sleep(1)
TouchAction(driver).tap(x=712, y=1342).perform()  # 选择开始挑战
time.sleep(3)

a = 11
while a > 0:
    time.sleep(8)
    TouchAction(driver).tap(x=671, y=1734).perform()  # 点击查看广告
    time.sleep(5)
    try:
        GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
    except NoSuchElementException:
        print("toutiaosdk广告")
        time.sleep(40)
        TouchAction(driver).tap(x=1285, y=139).perform()  # 关闭toutiao广告
        print(a)
        print("toutiaosdk广告关闭")
    else:
        print("GDTsdk广告")
        time.sleep(50)
        driver.back()  # GDTsdk广告按钮
        print(a)
        print("GDTsdk广告关闭")
    a -= 1

time.sleep(8)
driver.back()  # 判官中回到首页
time.sleep(1)
driver.back()
TouchAction(driver).tap(x=588, y=186).perform()  # 返回进入个人中心
time.sleep(2)
TouchAction(driver).tap(x=1275, y=243).perform()
time.sleep(1)
TouchAction(driver).tap(x=707, y=2467).perform()
time.sleep(1)
TouchAction(driver).tap(x=960, y=1440).perform()

#######################################################################################################################
mobile = "18017700608"
AA = "\033[1;31mNO.34\033[0m " + mobile + " \033[1;31m开始\033[0m"
print(AA)
nowtime = time.strftime('%H:%M:%S')
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
        time.sleep(1)
        edit_mobile = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/edit_phone")  # 选择手机号输入框
        edit_mobile.send_keys(mobile)
        time.sleep(1)
        TouchAction(driver).tap(x=1100, y=870).perform()  # 获取验证码
        time.sleep(2)
        # 获取验证码
        logincodeurl = "https://uc.crazyccy.com/login/main_login/testtool?key=sLQq2_jaKLknsqAwZ&type=1&mobile=" + mobile
        # print(logincodeurl)
        request = urllib.request.Request(logincodeurl)  # 构建请求url
        response = urllib.request.urlopen(request, context=context)  # ssl证书免验证加入,context = context# 打开请求url链接
        num = response.read()  # 读取页面返回信息，python3返回数据为bytes类型的对象 (即b为前缀, bytes类型)
        logincode = num.decode()
        edit_code = driver.find_element_by_id(
            "com.kamitu.drawsth.standalone.free.android:id/edit_identifyCode")  # 选择验证码输入框
        time.sleep(1)
        edit_code.send_keys(logincode)
        time.sleep(1)
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
        TouchAction(driver).tap(x=1270, y=655).perform()


check_signwindows()
time.sleep(2)

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
time.sleep(2)

TouchAction(driver).tap(x=439, y=2379).perform()  # 选择进入判官
time.sleep(1)
TouchAction(driver).tap(x=712, y=1342).perform()  # 选择开始挑战
time.sleep(3)

a = 11
while a > 0:
    time.sleep(8)
    TouchAction(driver).tap(x=671, y=1734).perform()  # 点击查看广告
    time.sleep(5)
    try:
        GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
    except NoSuchElementException:
        print("toutiaosdk广告")
        time.sleep(40)
        TouchAction(driver).tap(x=1285, y=139).perform()  # 关闭toutiao广告
        print(a)
        print("toutiaosdk广告关闭")
    else:
        print("GDTsdk广告")
        time.sleep(50)
        driver.back()  # GDTsdk广告按钮
        print(a)
        print("GDTsdk广告关闭")
    a -= 1

time.sleep(8)
driver.back()  # 判官中回到首页
time.sleep(1)
driver.back()
TouchAction(driver).tap(x=588, y=186).perform()  # 返回进入个人中心
time.sleep(2)
TouchAction(driver).tap(x=1275, y=243).perform()
time.sleep(1)
TouchAction(driver).tap(x=707, y=2467).perform()
time.sleep(1)
TouchAction(driver).tap(x=960, y=1440).perform()

#######################################################################################################################
mobile = "18017700607"
AA = "\033[1;31mNO.35\033[0m " + mobile + " \033[1;31m开始\033[0m"
print(AA)
nowtime = time.strftime('%H:%M:%S')
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
        time.sleep(1)
        edit_mobile = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/edit_phone")  # 选择手机号输入框
        edit_mobile.send_keys(mobile)
        time.sleep(1)
        TouchAction(driver).tap(x=1100, y=870).perform()  # 获取验证码
        time.sleep(2)
        # 获取验证码
        logincodeurl = "https://uc.crazyccy.com/login/main_login/testtool?key=sLQq2_jaKLknsqAwZ&type=1&mobile=" + mobile
        # print(logincodeurl)
        request = urllib.request.Request(logincodeurl)  # 构建请求url
        response = urllib.request.urlopen(request, context=context)  # ssl证书免验证加入,context = context# 打开请求url链接
        num = response.read()  # 读取页面返回信息，python3返回数据为bytes类型的对象 (即b为前缀, bytes类型)
        logincode = num.decode()
        edit_code = driver.find_element_by_id(
            "com.kamitu.drawsth.standalone.free.android:id/edit_identifyCode")  # 选择验证码输入框
        time.sleep(1)
        edit_code.send_keys(logincode)
        time.sleep(1)
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
        TouchAction(driver).tap(x=1270, y=655).perform()


check_signwindows()
time.sleep(2)

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
time.sleep(2)

TouchAction(driver).tap(x=439, y=2379).perform()  # 选择进入判官
time.sleep(1)
TouchAction(driver).tap(x=712, y=1342).perform()  # 选择开始挑战
time.sleep(3)

a = 11
while a > 0:
    time.sleep(8)
    TouchAction(driver).tap(x=671, y=1734).perform()  # 点击查看广告
    time.sleep(5)
    try:
        GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
    except NoSuchElementException:
        print("toutiaosdk广告")
        time.sleep(40)
        TouchAction(driver).tap(x=1285, y=139).perform()  # 关闭toutiao广告
        print(a)
        print("toutiaosdk广告关闭")
    else:
        print("GDTsdk广告")
        time.sleep(50)
        driver.back()  # GDTsdk广告按钮
        print(a)
        print("GDTsdk广告关闭")
    a -= 1

time.sleep(8)
driver.back()  # 判官中回到首页
time.sleep(1)
driver.back()
TouchAction(driver).tap(x=588, y=186).perform()  # 返回进入个人中心
time.sleep(2)
TouchAction(driver).tap(x=1275, y=243).perform()
time.sleep(1)
TouchAction(driver).tap(x=707, y=2467).perform()
time.sleep(1)
TouchAction(driver).tap(x=960, y=1440).perform()

#######################################################################################################################
mobile = "18017700606"
AA = "\033[1;31mNO.36\033[0m " + mobile + " \033[1;31m开始\033[0m"
print(AA)
nowtime = time.strftime('%H:%M:%S')
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
        time.sleep(1)
        edit_mobile = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/edit_phone")  # 选择手机号输入框
        edit_mobile.send_keys(mobile)
        time.sleep(1)
        TouchAction(driver).tap(x=1100, y=870).perform()  # 获取验证码
        time.sleep(2)
        # 获取验证码
        logincodeurl = "https://uc.crazyccy.com/login/main_login/testtool?key=sLQq2_jaKLknsqAwZ&type=1&mobile=" + mobile
        # print(logincodeurl)
        request = urllib.request.Request(logincodeurl)  # 构建请求url
        response = urllib.request.urlopen(request, context=context)  # ssl证书免验证加入,context = context# 打开请求url链接
        num = response.read()  # 读取页面返回信息，python3返回数据为bytes类型的对象 (即b为前缀, bytes类型)
        logincode = num.decode()
        edit_code = driver.find_element_by_id(
            "com.kamitu.drawsth.standalone.free.android:id/edit_identifyCode")  # 选择验证码输入框
        time.sleep(1)
        edit_code.send_keys(logincode)
        time.sleep(1)
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
        TouchAction(driver).tap(x=1270, y=655).perform()


check_signwindows()
time.sleep(2)

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
time.sleep(2)

TouchAction(driver).tap(x=439, y=2379).perform()  # 选择进入判官
time.sleep(1)
TouchAction(driver).tap(x=712, y=1342).perform()  # 选择开始挑战
time.sleep(3)

a = 11
while a > 0:
    time.sleep(8)
    TouchAction(driver).tap(x=671, y=1734).perform()  # 点击查看广告
    time.sleep(5)
    try:
        GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
    except NoSuchElementException:
        print("toutiaosdk广告")
        time.sleep(40)
        TouchAction(driver).tap(x=1285, y=139).perform()  # 关闭toutiao广告
        print(a)
        print("toutiaosdk广告关闭")
    else:
        print("GDTsdk广告")
        time.sleep(50)
        driver.back()  # GDTsdk广告按钮
        print(a)
        print("GDTsdk广告关闭")
    a -= 1

time.sleep(8)
driver.back()  # 判官中回到首页
time.sleep(1)
driver.back()
TouchAction(driver).tap(x=588, y=186).perform()  # 返回进入个人中心
time.sleep(2)
TouchAction(driver).tap(x=1275, y=243).perform()
time.sleep(1)
TouchAction(driver).tap(x=707, y=2467).perform()
time.sleep(1)
TouchAction(driver).tap(x=960, y=1440).perform()

#######################################################################################################################
mobile = "18017700605"
AA = "\033[1;31mNO.37\033[0m " + mobile + " \033[1;31m开始\033[0m"
print(AA)
nowtime = time.strftime('%H:%M:%S')
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
        time.sleep(1)
        edit_mobile = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/edit_phone")  # 选择手机号输入框
        edit_mobile.send_keys(mobile)
        time.sleep(1)
        TouchAction(driver).tap(x=1100, y=870).perform()  # 获取验证码
        time.sleep(2)
        # 获取验证码
        logincodeurl = "https://uc.crazyccy.com/login/main_login/testtool?key=sLQq2_jaKLknsqAwZ&type=1&mobile=" + mobile
        # print(logincodeurl)
        request = urllib.request.Request(logincodeurl)  # 构建请求url
        response = urllib.request.urlopen(request, context=context)  # ssl证书免验证加入,context = context# 打开请求url链接
        num = response.read()  # 读取页面返回信息，python3返回数据为bytes类型的对象 (即b为前缀, bytes类型)
        logincode = num.decode()
        edit_code = driver.find_element_by_id(
            "com.kamitu.drawsth.standalone.free.android:id/edit_identifyCode")  # 选择验证码输入框
        time.sleep(1)
        edit_code.send_keys(logincode)
        time.sleep(1)
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
        TouchAction(driver).tap(x=1270, y=655).perform()


check_signwindows()
time.sleep(2)

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
time.sleep(2)

TouchAction(driver).tap(x=439, y=2379).perform()  # 选择进入判官
time.sleep(1)
TouchAction(driver).tap(x=712, y=1342).perform()  # 选择开始挑战
time.sleep(3)

a = 11
while a > 0:
    time.sleep(8)
    TouchAction(driver).tap(x=671, y=1734).perform()  # 点击查看广告
    time.sleep(5)
    try:
        GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
    except NoSuchElementException:
        print("toutiaosdk广告")
        time.sleep(40)
        TouchAction(driver).tap(x=1285, y=139).perform()  # 关闭toutiao广告
        print(a)
        print("toutiaosdk广告关闭")
    else:
        print("GDTsdk广告")
        time.sleep(50)
        driver.back()  # GDTsdk广告按钮
        print(a)
        print("GDTsdk广告关闭")
    a -= 1

time.sleep(8)
driver.back()  # 判官中回到首页
time.sleep(1)
driver.back()
TouchAction(driver).tap(x=588, y=186).perform()  # 返回进入个人中心
time.sleep(2)
TouchAction(driver).tap(x=1275, y=243).perform()
time.sleep(1)
TouchAction(driver).tap(x=707, y=2467).perform()
time.sleep(1)
TouchAction(driver).tap(x=960, y=1440).perform()

#######################################################################################################################
mobile = "18017700604"
AA = "\033[1;31mNO.38\033[0m " + mobile + " \033[1;31m开始\033[0m"
print(AA)
nowtime = time.strftime('%H:%M:%S')
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
        time.sleep(1)
        edit_mobile = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/edit_phone")  # 选择手机号输入框
        edit_mobile.send_keys(mobile)
        time.sleep(1)
        TouchAction(driver).tap(x=1100, y=870).perform()  # 获取验证码
        time.sleep(2)
        # 获取验证码
        logincodeurl = "https://uc.crazyccy.com/login/main_login/testtool?key=sLQq2_jaKLknsqAwZ&type=1&mobile=" + mobile
        # print(logincodeurl)
        request = urllib.request.Request(logincodeurl)  # 构建请求url
        response = urllib.request.urlopen(request, context=context)  # ssl证书免验证加入,context = context# 打开请求url链接
        num = response.read()  # 读取页面返回信息，python3返回数据为bytes类型的对象 (即b为前缀, bytes类型)
        logincode = num.decode()
        edit_code = driver.find_element_by_id(
            "com.kamitu.drawsth.standalone.free.android:id/edit_identifyCode")  # 选择验证码输入框
        time.sleep(1)
        edit_code.send_keys(logincode)
        time.sleep(1)
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
        TouchAction(driver).tap(x=1270, y=655).perform()


check_signwindows()
time.sleep(2)

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
time.sleep(2)

TouchAction(driver).tap(x=439, y=2379).perform()  # 选择进入判官
time.sleep(1)
TouchAction(driver).tap(x=712, y=1342).perform()  # 选择开始挑战
time.sleep(3)

a = 11
while a > 0:
    time.sleep(8)
    TouchAction(driver).tap(x=671, y=1734).perform()  # 点击查看广告
    time.sleep(5)
    try:
        GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
    except NoSuchElementException:
        print("toutiaosdk广告")
        time.sleep(40)
        TouchAction(driver).tap(x=1285, y=139).perform()  # 关闭toutiao广告
        print(a)
        print("toutiaosdk广告关闭")
    else:
        print("GDTsdk广告")
        time.sleep(50)
        driver.back()  # GDTsdk广告按钮
        print(a)
        print("GDTsdk广告关闭")
    a -= 1

time.sleep(8)
driver.back()  # 判官中回到首页
time.sleep(1)
driver.back()
TouchAction(driver).tap(x=588, y=186).perform()  # 返回进入个人中心
time.sleep(2)
TouchAction(driver).tap(x=1275, y=243).perform()
time.sleep(1)
TouchAction(driver).tap(x=707, y=2467).perform()
time.sleep(1)
TouchAction(driver).tap(x=960, y=1440).perform()

#######################################################################################################################
mobile = "18017700603"
AA = "\033[1;31mNO.39\033[0m " + mobile + " \033[1;31m开始\033[0m"
print(AA)
nowtime = time.strftime('%H:%M:%S')
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
        time.sleep(1)
        edit_mobile = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/edit_phone")  # 选择手机号输入框
        edit_mobile.send_keys(mobile)
        time.sleep(1)
        TouchAction(driver).tap(x=1100, y=870).perform()  # 获取验证码
        time.sleep(2)
        # 获取验证码
        logincodeurl = "https://uc.crazyccy.com/login/main_login/testtool?key=sLQq2_jaKLknsqAwZ&type=1&mobile=" + mobile
        # print(logincodeurl)
        request = urllib.request.Request(logincodeurl)  # 构建请求url
        response = urllib.request.urlopen(request, context=context)  # ssl证书免验证加入,context = context# 打开请求url链接
        num = response.read()  # 读取页面返回信息，python3返回数据为bytes类型的对象 (即b为前缀, bytes类型)
        logincode = num.decode()
        edit_code = driver.find_element_by_id(
            "com.kamitu.drawsth.standalone.free.android:id/edit_identifyCode")  # 选择验证码输入框
        time.sleep(1)
        edit_code.send_keys(logincode)
        time.sleep(1)
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
        TouchAction(driver).tap(x=1270, y=655).perform()


check_signwindows()
time.sleep(2)

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
time.sleep(2)

TouchAction(driver).tap(x=439, y=2379).perform()  # 选择进入判官
time.sleep(1)
TouchAction(driver).tap(x=712, y=1342).perform()  # 选择开始挑战
time.sleep(3)

a = 11
while a > 0:
    time.sleep(8)
    TouchAction(driver).tap(x=671, y=1734).perform()  # 点击查看广告
    time.sleep(5)
    try:
        GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
    except NoSuchElementException:
        print("toutiaosdk广告")
        time.sleep(40)
        TouchAction(driver).tap(x=1285, y=139).perform()  # 关闭toutiao广告
        print(a)
        print("toutiaosdk广告关闭")
    else:
        print("GDTsdk广告")
        time.sleep(50)
        driver.back()  # GDTsdk广告按钮
        print(a)
        print("GDTsdk广告关闭")
    a -= 1

time.sleep(8)
driver.back()  # 判官中回到首页
time.sleep(1)
driver.back()
TouchAction(driver).tap(x=588, y=186).perform()  # 返回进入个人中心
time.sleep(2)
TouchAction(driver).tap(x=1275, y=243).perform()
time.sleep(1)
TouchAction(driver).tap(x=707, y=2467).perform()
time.sleep(1)
TouchAction(driver).tap(x=960, y=1440).perform()

#######################################################################################################################
mobile = "18017700600"
AA = "\033[1;31mNO.40\033[0m " + mobile + " \033[1;31m开始\033[0m"
print(AA)
nowtime = time.strftime('%H:%M:%S')
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
        time.sleep(1)
        edit_mobile = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/edit_phone")  # 选择手机号输入框
        edit_mobile.send_keys(mobile)
        time.sleep(1)
        TouchAction(driver).tap(x=1100, y=870).perform()  # 获取验证码
        time.sleep(2)
        # 获取验证码
        logincodeurl = "https://uc.crazyccy.com/login/main_login/testtool?key=sLQq2_jaKLknsqAwZ&type=1&mobile=" + mobile
        # print(logincodeurl)
        request = urllib.request.Request(logincodeurl)  # 构建请求url
        response = urllib.request.urlopen(request, context=context)  # ssl证书免验证加入,context = context# 打开请求url链接
        num = response.read()  # 读取页面返回信息，python3返回数据为bytes类型的对象 (即b为前缀, bytes类型)
        logincode = num.decode()
        edit_code = driver.find_element_by_id(
            "com.kamitu.drawsth.standalone.free.android:id/edit_identifyCode")  # 选择验证码输入框
        time.sleep(1)
        edit_code.send_keys(logincode)
        time.sleep(1)
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
        TouchAction(driver).tap(x=1270, y=655).perform()


check_signwindows()
time.sleep(2)

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
time.sleep(2)

TouchAction(driver).tap(x=439, y=2379).perform()  # 选择进入判官
time.sleep(1)
TouchAction(driver).tap(x=712, y=1342).perform()  # 选择开始挑战
time.sleep(3)

a = 11
while a > 0:
    time.sleep(8)
    TouchAction(driver).tap(x=671, y=1734).perform()  # 点击查看广告
    time.sleep(5)
    try:
        GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
    except NoSuchElementException:
        print("toutiaosdk广告")
        time.sleep(40)
        TouchAction(driver).tap(x=1285, y=139).perform()  # 关闭toutiao广告
        print(a)
        print("toutiaosdk广告关闭")
    else:
        print("GDTsdk广告")
        time.sleep(50)
        driver.back()  # GDTsdk广告按钮
        print(a)
        print("GDTsdk广告关闭")
    a -= 1

time.sleep(8)
driver.back()  # 判官中回到首页
time.sleep(1)
driver.back()
TouchAction(driver).tap(x=588, y=186).perform()  # 返回进入个人中心
time.sleep(2)
TouchAction(driver).tap(x=1275, y=243).perform()
time.sleep(1)
TouchAction(driver).tap(x=707, y=2467).perform()
time.sleep(1)
TouchAction(driver).tap(x=960, y=1440).perform()

#######################################################################################################################
mobile = "18017700611"
AA = "\033[1;31m   \033[0m " + mobile + " \033[1;31m开始\033[0m"
print(AA)
nowtime = time.strftime('%H:%M:%S')
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
        time.sleep(1)
        edit_mobile = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/edit_phone")  # 选择手机号输入框
        edit_mobile.send_keys(mobile)
        time.sleep(1)
        TouchAction(driver).tap(x=1100, y=870).perform()  # 获取验证码
        time.sleep(2)
        # 获取验证码
        logincodeurl = "https://uc.crazyccy.com/login/main_login/testtool?key=sLQq2_jaKLknsqAwZ&type=1&mobile=" + mobile
        # print(logincodeurl)
        request = urllib.request.Request(logincodeurl)  # 构建请求url
        response = urllib.request.urlopen(request, context=context)  # ssl证书免验证加入,context = context# 打开请求url链接
        num = response.read()  # 读取页面返回信息，python3返回数据为bytes类型的对象 (即b为前缀, bytes类型)
        logincode = num.decode()
        edit_code = driver.find_element_by_id(
            "com.kamitu.drawsth.standalone.free.android:id/edit_identifyCode")  # 选择验证码输入框
        time.sleep(1)
        edit_code.send_keys(logincode)
        time.sleep(1)
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
        TouchAction(driver).tap(x=1270, y=655).perform()


check_signwindows()
time.sleep(2)

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
time.sleep(2)

TouchAction(driver).tap(x=439, y=2379).perform()  # 选择进入判官
time.sleep(1)
TouchAction(driver).tap(x=712, y=1342).perform()  # 选择开始挑战
time.sleep(3)

a = 11
while a > 0:
    time.sleep(8)
    TouchAction(driver).tap(x=671, y=1734).perform()  # 点击查看广告
    time.sleep(5)
    try:
        GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
    except NoSuchElementException:
        print("toutiaosdk广告")
        time.sleep(40)
        TouchAction(driver).tap(x=1285, y=139).perform()  # 关闭toutiao广告
        print(a)
        print("toutiaosdk广告关闭")
    else:
        print("GDTsdk广告")
        time.sleep(50)
        driver.back()  # GDTsdk广告按钮
        print(a)
        print("GDTsdk广告关闭")
    a -= 1

time.sleep(8)
driver.back()  # 判官中回到首页
time.sleep(1)
TouchAction(driver).tap(x=588, y=186).perform()  # 返回进入个人中心
time.sleep(1)
TouchAction(driver).tap(x=1275, y=243).perform()
time.sleep(1)
TouchAction(driver).tap(x=707, y=2467).perform()
time.sleep(1)
TouchAction(driver).tap(x=960, y=1440).perform()

#######################################################################################################################
mobile = "18017700207"
AA = "\033[1;31mNO.42\033[0m " + mobile + " \033[1;31m开始\033[0m"
print(AA)
nowtime = time.strftime('%H:%M:%S')
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
        time.sleep(1)
        edit_mobile = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/edit_phone")  # 选择手机号输入框
        edit_mobile.send_keys(mobile)
        time.sleep(1)
        TouchAction(driver).tap(x=1100, y=870).perform()  # 获取验证码
        time.sleep(2)
        # 获取验证码
        logincodeurl = "https://uc.crazyccy.com/login/main_login/testtool?key=sLQq2_jaKLknsqAwZ&type=1&mobile=" + mobile
        # print(logincodeurl)
        request = urllib.request.Request(logincodeurl)  # 构建请求url
        response = urllib.request.urlopen(request, context=context)  # ssl证书免验证加入,context = context# 打开请求url链接
        num = response.read()  # 读取页面返回信息，python3返回数据为bytes类型的对象 (即b为前缀, bytes类型)
        logincode = num.decode()
        edit_code = driver.find_element_by_id(
            "com.kamitu.drawsth.standalone.free.android:id/edit_identifyCode")  # 选择验证码输入框
        time.sleep(1)
        edit_code.send_keys(logincode)
        time.sleep(1)
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
        TouchAction(driver).tap(x=1270, y=655).perform()


check_signwindows()
time.sleep(2)

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
time.sleep(2)

TouchAction(driver).tap(x=439, y=2379).perform()  # 选择进入判官
time.sleep(1)
TouchAction(driver).tap(x=712, y=1342).perform()  # 选择开始挑战
time.sleep(3)

a = 11
while a > 0:
    time.sleep(8)
    TouchAction(driver).tap(x=671, y=1734).perform()  # 点击查看广告
    time.sleep(5)
    try:
        GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
    except NoSuchElementException:
        print("toutiaosdk广告")
        time.sleep(40)
        TouchAction(driver).tap(x=1285, y=139).perform()  # 关闭toutiao广告
        print(a)
        print("toutiaosdk广告关闭")
    else:
        print("GDTsdk广告")
        time.sleep(50)
        driver.back()  # GDTsdk广告按钮
        print(a)
        print("GDTsdk广告关闭")
    a -= 1

time.sleep(8)
driver.back()  # 判官中回到首页
time.sleep(1)
driver.back()
TouchAction(driver).tap(x=588, y=186).perform()  # 返回进入个人中心
time.sleep(2)
TouchAction(driver).tap(x=1275, y=243).perform()
time.sleep(1)
TouchAction(driver).tap(x=707, y=2467).perform()
time.sleep(1)
TouchAction(driver).tap(x=960, y=1440).perform()

#######################################################################################################################
mobile = "18017700478"
AA = "\033[1;31mNO.43\033[0m " + mobile + " \033[1;31m开始\033[0m"
print(AA)
nowtime = time.strftime('%H:%M:%S')
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
        time.sleep(1)
        edit_mobile = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/edit_phone")  # 选择手机号输入框
        edit_mobile.send_keys(mobile)
        time.sleep(1)
        TouchAction(driver).tap(x=1100, y=870).perform()  # 获取验证码
        time.sleep(2)
        # 获取验证码
        logincodeurl = "https://uc.crazyccy.com/login/main_login/testtool?key=sLQq2_jaKLknsqAwZ&type=1&mobile=" + mobile
        # print(logincodeurl)
        request = urllib.request.Request(logincodeurl)  # 构建请求url
        response = urllib.request.urlopen(request, context=context)  # ssl证书免验证加入,context = context# 打开请求url链接
        num = response.read()  # 读取页面返回信息，python3返回数据为bytes类型的对象 (即b为前缀, bytes类型)
        logincode = num.decode()
        edit_code = driver.find_element_by_id(
            "com.kamitu.drawsth.standalone.free.android:id/edit_identifyCode")  # 选择验证码输入框
        time.sleep(1)
        edit_code.send_keys(logincode)
        time.sleep(1)
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
        TouchAction(driver).tap(x=1270, y=655).perform()


check_signwindows()
time.sleep(2)

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
time.sleep(2)

TouchAction(driver).tap(x=439, y=2379).perform()  # 选择进入判官
time.sleep(1)
TouchAction(driver).tap(x=712, y=1342).perform()  # 选择开始挑战
time.sleep(3)

a = 11
while a > 0:
    time.sleep(8)
    TouchAction(driver).tap(x=671, y=1734).perform()  # 点击查看广告
    time.sleep(5)
    try:
        GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
    except NoSuchElementException:
        print("toutiaosdk广告")
        time.sleep(40)
        TouchAction(driver).tap(x=1285, y=139).perform()  # 关闭toutiao广告
        print(a)
        print("toutiaosdk广告关闭")
    else:
        print("GDTsdk广告")
        time.sleep(50)
        driver.back()  # GDTsdk广告按钮
        print(a)
        print("GDTsdk广告关闭")
    a -= 1

time.sleep(8)
driver.back()  # 判官中回到首页
time.sleep(1)
driver.back()
TouchAction(driver).tap(x=588, y=186).perform()  # 返回进入个人中心
time.sleep(2)
TouchAction(driver).tap(x=1275, y=243).perform()
time.sleep(1)
TouchAction(driver).tap(x=707, y=2467).perform()
time.sleep(1)
TouchAction(driver).tap(x=960, y=1440).perform()

#######################################################################################################################
mobile = "18116688811"
AA = "\033[1;31mNO.44\033[0m " + mobile + " \033[1;31m开始\033[0m"
print(AA)
nowtime = time.strftime('%H:%M:%S')
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
        time.sleep(1)
        edit_mobile = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/edit_phone")  # 选择手机号输入框
        edit_mobile.send_keys(mobile)
        time.sleep(1)
        TouchAction(driver).tap(x=1100, y=870).perform()  # 获取验证码
        time.sleep(2)
        # 获取验证码
        logincodeurl = "https://uc.crazyccy.com/login/main_login/testtool?key=sLQq2_jaKLknsqAwZ&type=1&mobile=" + mobile
        # print(logincodeurl)
        request = urllib.request.Request(logincodeurl)  # 构建请求url
        response = urllib.request.urlopen(request, context=context)  # ssl证书免验证加入,context = context# 打开请求url链接
        num = response.read()  # 读取页面返回信息，python3返回数据为bytes类型的对象 (即b为前缀, bytes类型)
        logincode = num.decode()
        edit_code = driver.find_element_by_id(
            "com.kamitu.drawsth.standalone.free.android:id/edit_identifyCode")  # 选择验证码输入框
        time.sleep(1)
        edit_code.send_keys(logincode)
        time.sleep(1)
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
        TouchAction(driver).tap(x=1270, y=655).perform()


check_signwindows()
time.sleep(2)

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
time.sleep(2)

TouchAction(driver).tap(x=439, y=2379).perform()  # 选择进入判官
time.sleep(1)
TouchAction(driver).tap(x=712, y=1342).perform()  # 选择开始挑战
time.sleep(3)

a = 11
while a > 0:
    time.sleep(8)
    TouchAction(driver).tap(x=671, y=1734).perform()  # 点击查看广告
    time.sleep(5)
    try:
        GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
    except NoSuchElementException:
        print("toutiaosdk广告")
        time.sleep(40)
        TouchAction(driver).tap(x=1285, y=139).perform()  # 关闭toutiao广告
        print(a)
        print("toutiaosdk广告关闭")
    else:
        print("GDTsdk广告")
        time.sleep(50)
        driver.back()  # GDTsdk广告按钮
        print(a)
        print("GDTsdk广告关闭")
    a -= 1

time.sleep(8)
driver.back()  # 判官中回到首页
time.sleep(1)
driver.back()
TouchAction(driver).tap(x=588, y=186).perform()  # 返回进入个人中心
time.sleep(2)
TouchAction(driver).tap(x=1275, y=243).perform()
time.sleep(1)
TouchAction(driver).tap(x=707, y=2467).perform()
time.sleep(1)
TouchAction(driver).tap(x=960, y=1440).perform()

#######################################################################################################################
mobile = "18220860324"
AA = "\033[1;31mNO.45\033[0m " + mobile + " \033[1;31m开始\033[0m"
print(AA)
nowtime = time.strftime('%H:%M:%S')
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
        time.sleep(1)
        edit_mobile = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/edit_phone")  # 选择手机号输入框
        edit_mobile.send_keys(mobile)
        time.sleep(1)
        TouchAction(driver).tap(x=1100, y=870).perform()  # 获取验证码
        time.sleep(2)
        # 获取验证码
        logincodeurl = "https://uc.crazyccy.com/login/main_login/testtool?key=sLQq2_jaKLknsqAwZ&type=1&mobile=" + mobile
        # print(logincodeurl)
        request = urllib.request.Request(logincodeurl)  # 构建请求url
        response = urllib.request.urlopen(request, context=context)  # ssl证书免验证加入,context = context# 打开请求url链接
        num = response.read()  # 读取页面返回信息，python3返回数据为bytes类型的对象 (即b为前缀, bytes类型)
        logincode = num.decode()
        edit_code = driver.find_element_by_id(
            "com.kamitu.drawsth.standalone.free.android:id/edit_identifyCode")  # 选择验证码输入框
        time.sleep(1)
        edit_code.send_keys(logincode)
        time.sleep(1)
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
        TouchAction(driver).tap(x=1270, y=655).perform()


check_signwindows()
time.sleep(2)

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
time.sleep(2)

TouchAction(driver).tap(x=439, y=2379).perform()  # 选择进入判官
time.sleep(1)
TouchAction(driver).tap(x=712, y=1342).perform()  # 选择开始挑战
time.sleep(3)

a = 11
while a > 0:
    time.sleep(8)
    TouchAction(driver).tap(x=671, y=1734).perform()  # 点击查看广告
    time.sleep(5)
    try:
        GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
    except NoSuchElementException:
        print("toutiaosdk广告")
        time.sleep(40)
        TouchAction(driver).tap(x=1285, y=139).perform()  # 关闭toutiao广告
        print(a)
        print("toutiaosdk广告关闭")
    else:
        print("GDTsdk广告")
        time.sleep(50)
        driver.back()  # GDTsdk广告按钮
        print(a)
        print("GDTsdk广告关闭")
    a -= 1

time.sleep(8)
driver.back()  # 判官中回到首页
time.sleep(1)
driver.back()
TouchAction(driver).tap(x=588, y=186).perform()  # 返回进入个人中心
time.sleep(2)
TouchAction(driver).tap(x=1275, y=243).perform()
time.sleep(1)
TouchAction(driver).tap(x=707, y=2467).perform()
time.sleep(1)
TouchAction(driver).tap(x=960, y=1440).perform()

#######################################################################################################################
mobile = "18116699805"
AA = "\033[1;31mNO.46\033[0m " + mobile + " \033[1;31m开始\033[0m"
print(AA)
nowtime = time.strftime('%H:%M:%S')
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
        time.sleep(1)
        edit_mobile = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/edit_phone")  # 选择手机号输入框
        edit_mobile.send_keys(mobile)
        time.sleep(1)
        TouchAction(driver).tap(x=1100, y=870).perform()  # 获取验证码
        time.sleep(2)
        # 获取验证码
        logincodeurl = "https://uc.crazyccy.com/login/main_login/testtool?key=sLQq2_jaKLknsqAwZ&type=1&mobile=" + mobile
        # print(logincodeurl)
        request = urllib.request.Request(logincodeurl)  # 构建请求url
        response = urllib.request.urlopen(request, context=context)  # ssl证书免验证加入,context = context# 打开请求url链接
        num = response.read()  # 读取页面返回信息，python3返回数据为bytes类型的对象 (即b为前缀, bytes类型)
        logincode = num.decode()
        edit_code = driver.find_element_by_id(
            "com.kamitu.drawsth.standalone.free.android:id/edit_identifyCode")  # 选择验证码输入框
        time.sleep(1)
        edit_code.send_keys(logincode)
        time.sleep(1)
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
        TouchAction(driver).tap(x=1270, y=655).perform()


check_signwindows()
time.sleep(2)

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
time.sleep(2)

TouchAction(driver).tap(x=439, y=2379).perform()  # 选择进入判官
time.sleep(1)
TouchAction(driver).tap(x=712, y=1342).perform()  # 选择开始挑战
time.sleep(3)

a = 11
while a > 0:
    time.sleep(8)
    TouchAction(driver).tap(x=671, y=1734).perform()  # 点击查看广告
    time.sleep(5)
    try:
        GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
    except NoSuchElementException:
        print("toutiaosdk广告")
        time.sleep(40)
        TouchAction(driver).tap(x=1285, y=139).perform()  # 关闭toutiao广告
        print(a)
        print("toutiaosdk广告关闭")
    else:
        print("GDTsdk广告")
        time.sleep(50)
        driver.back()  # GDTsdk广告按钮
        print(a)
        print("GDTsdk广告关闭")
    a -= 1

time.sleep(8)
driver.back()  # 判官中回到首页
time.sleep(1)
driver.back()
TouchAction(driver).tap(x=588, y=186).perform()  # 返回进入个人中心
time.sleep(2)
TouchAction(driver).tap(x=1275, y=243).perform()
time.sleep(1)
TouchAction(driver).tap(x=707, y=2467).perform()
time.sleep(1)
TouchAction(driver).tap(x=960, y=1440).perform()

#######################################################################################################################
mobile = "18116688822"
AA = "\033[1;31mNO.47\033[0m " + mobile + " \033[1;31m开始\033[0m"
print(AA)
nowtime = time.strftime('%H:%M:%S')
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
        time.sleep(1)
        edit_mobile = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/edit_phone")  # 选择手机号输入框
        edit_mobile.send_keys(mobile)
        time.sleep(1)
        TouchAction(driver).tap(x=1100, y=870).perform()  # 获取验证码
        time.sleep(2)
        # 获取验证码
        logincodeurl = "https://uc.crazyccy.com/login/main_login/testtool?key=sLQq2_jaKLknsqAwZ&type=1&mobile=" + mobile
        # print(logincodeurl)
        request = urllib.request.Request(logincodeurl)  # 构建请求url
        response = urllib.request.urlopen(request, context=context)  # ssl证书免验证加入,context = context# 打开请求url链接
        num = response.read()  # 读取页面返回信息，python3返回数据为bytes类型的对象 (即b为前缀, bytes类型)
        logincode = num.decode()
        edit_code = driver.find_element_by_id(
            "com.kamitu.drawsth.standalone.free.android:id/edit_identifyCode")  # 选择验证码输入框
        time.sleep(1)
        edit_code.send_keys(logincode)
        time.sleep(1)
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
        TouchAction(driver).tap(x=1270, y=655).perform()


check_signwindows()
time.sleep(2)

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
time.sleep(2)

TouchAction(driver).tap(x=439, y=2379).perform()  # 选择进入判官
time.sleep(1)
TouchAction(driver).tap(x=712, y=1342).perform()  # 选择开始挑战
time.sleep(3)

a = 11
while a > 0:
    time.sleep(8)
    TouchAction(driver).tap(x=671, y=1734).perform()  # 点击查看广告
    time.sleep(5)
    try:
        GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
    except NoSuchElementException:
        print("toutiaosdk广告")
        time.sleep(40)
        TouchAction(driver).tap(x=1285, y=139).perform()  # 关闭toutiao广告
        print(a)
        print("toutiaosdk广告关闭")
    else:
        print("GDTsdk广告")
        time.sleep(50)
        driver.back()  # GDTsdk广告按钮
        print(a)
        print("GDTsdk广告关闭")
    a -= 1

time.sleep(8)
driver.back()  # 判官中回到首页
time.sleep(1)
driver.back()
TouchAction(driver).tap(x=588, y=186).perform()  # 返回进入个人中心
time.sleep(2)
TouchAction(driver).tap(x=1275, y=243).perform()
time.sleep(1)
TouchAction(driver).tap(x=707, y=2467).perform()
time.sleep(1)
TouchAction(driver).tap(x=960, y=1440).perform()

#######################################################################################################################
nowtime = time.strftime('%H:%M:%S')
print(nowtime)
