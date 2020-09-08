# coding=utf-8

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.common.exceptions import NoSuchElementException
import time
import urllib.request
import ssl

capabilities = {}
capabilities['platformName'] = 'Android'  # Android平台测试
capabilities['platformVersion'] = '8.0.0'
capabilities['deviceName'] = 'SM-C5000'
capabilities['appPackage'] = 'com.kamitu.drawsth.standalone.free.android'  # 系统手机中的联系人app的包名
capabilities['appActivity'] = 'com.qsmy.busniess.welcome.WelcomeActivity'  # 系统手机中的联系人app的主入口activity
capabilities['noReset'] = 'true'  # 不重置app
capabilities['autoAcceptAlerts'] = 'true'
capabilities['autoWebview'] = 'false'
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', capabilities)  # 连接测试所在服务器
context = ssl._create_unverified_context()
nowtime1 = "\033[1;31m执行开始\033[0m " + time.strftime('%H:%M:%S')
print(nowtime1)

#############################################################################################################################################################
mobile = "18017700401"
AA = "\033[1;31mNO.1\033[0m " + mobile + " \033[1;31m开始\033[0m"
print(AA)
time.sleep(5)


def check_login():
    try:
        check_login = driver.find_element_by_id(
            "com.kamitu.drawsth.standalone.free.android:id/iv_mobile_login")  # 选择手机号登录
    except NoSuchElementException:
        print("自动登录成功")
    else:
        TouchAction(driver).tap(x=409, y=1729).perform()  # 点击手机号登录
        time.sleep(2)
        edit_mobile = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/edit_phone")  # 选择手机号输入框
        edit_mobile.send_keys(mobile)
        time.sleep(2)
        TouchAction(driver).tap(x=776, y=615).perform()  # 获取验证码
        time.sleep(2)
        logincodeurl = "https://uc.crazyccy.com/login/main_login/testtool?key=sLQq2_jaKLknsqAwZ&type=1&mobile=" + mobile
        request = urllib.request.Request(logincodeurl)  # 构建请求url
        response = urllib.request.urlopen(request, context=context)  # ssl证书免验证加入,context = context# 打开请求url链接
        num = response.read()  # 读取页面返回信息，python3返回数据为bytes类型的对象 (即b为前缀, bytes类型)
        logincode = num.decode()
        if logincode == '查不到！':
            time.sleep(2)
            TouchAction(driver).tap(x=776, y=615).perform()  # 获取验证码
            time.sleep(2)  # 获取验证码
            request = urllib.request.Request(logincodeurl)  # 构建请求url
            response = urllib.request.urlopen(request, context=context)  # ssl证书免验证加入,context = context# 打开请求url链接
            num = response.read()  # 读取页面返回信息，python3返回数据为bytes类型的对象 (即b为前缀, bytes类型)
            logincode = num.decode()
        edit_Code = driver.find_element_by_id(
            "com.kamitu.drawsth.standalone.free.android:id/edit_identifyCode")  # 选择验证码输入框
        time.sleep(2)
        edit_Code.send_keys(logincode)
        time.sleep(2)
        TouchAction(driver).tap(x=529, y=833).perform()  # 确定按钮登录


check_login()
time.sleep(15)  # 等待15秒加载进入首页


def check_signwindows():  # 检查是否有每日签到弹窗

    try:
        check_signwindows = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/iv_signin_get")
    except NoSuchElementException:
        print("无签到弹窗")
    else:
        TouchAction(driver).tap(x=953, y=551).perform()  # 关闭签到弹窗
        time.sleep(3)


check_signwindows()
time.sleep(3)

TouchAction(driver).tap(x=525, y=1556).perform()  # 进入接龙页面
time.sleep(3)
driver.back()
time.sleep(3)


def check_signtoast():  # 检查是否开启签到提醒

    try:
        check_signtoast = driver.find_element_by_id(
            "com.kamitu.drawsth.standalone.free.android:id/btn_open_reminder")
    except NoSuchElementException:
        print("无签到提醒弹窗")
    else:
        TouchAction(driver).tap(x=870, y=611).perform()  # 关闭签到提示弹窗


check_signtoast()
time.sleep(3)

TouchAction(driver).tap(x=323, y=1774).perform()  # 选择进入判官
time.sleep(2)
TouchAction(driver).tap(x=536, y=1009).perform()  # 选择开始挑战
time.sleep(3)

a = 1
while a <= 10:
    time.sleep(8)
    TouchAction(driver).tap(x=503, y=1305).perform()  # 点击查看广告
    time.sleep(10)
    try:
        GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
    except NoSuchElementException:
        BB = "  \033[1;31m第\033[0m " + str(a) + " \033[1;31m次\033[0m " + "toutiaosdk广告"
        print(BB)
        time.sleep(40)
        TouchAction(driver).tap(x=979, y=86).perform()  # 关闭toutiao广告
        print("     toutiaosdk广告关闭")
    else:
        CC = "  \033[1;31m第\033[0m " + str(a) + " \033[1;31m次\033[0m " + "GDTsdk广告"
        print(CC)
        time.sleep(55)  # 保证完整看完GTD广告
        driver.back()  # GDTsdk广告关闭
        print("     GDTsdk广告关闭")
    a += 1

time.sleep(7)
driver.back()  # 判官中回到首页
time.sleep(2)
TouchAction(driver).tap(x=439, y=124).perform()  # 返回进入个人中心
time.sleep(2)
TouchAction(driver).tap(x=971, y=158).perform()  # 点击设置
time.sleep(2)
TouchAction(driver).tap(x=536, y=1770).perform()  # 点击退出
time.sleep(2)
TouchAction(driver).tap(x=690, y=1069).perform()  # 弹窗确定退出

#############################################################################################################################################################
mobile = "18017700403"
AA = "\033[1;31mNO.2\033[0m " + mobile + " \033[1;31m开始\033[0m"
print(AA)
time.sleep(5)


def check_login():
    try:
        check_login = driver.find_element_by_id(
            "com.kamitu.drawsth.standalone.free.android:id/iv_mobile_login")  # 选择手机号登录
    except NoSuchElementException:
        print("自动登录成功")
    else:
        TouchAction(driver).tap(x=409, y=1729).perform()  # 点击手机号登录
        time.sleep(2)
        edit_mobile = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/edit_phone")  # 选择手机号输入框
        edit_mobile.send_keys(mobile)
        time.sleep(2)
        TouchAction(driver).tap(x=776, y=615).perform()  # 获取验证码
        time.sleep(2)
        logincodeurl = "https://uc.crazyccy.com/login/main_login/testtool?key=sLQq2_jaKLknsqAwZ&type=1&mobile=" + mobile
        request = urllib.request.Request(logincodeurl)  # 构建请求url
        response = urllib.request.urlopen(request, context=context)  # ssl证书免验证加入,context = context# 打开请求url链接
        num = response.read()  # 读取页面返回信息，python3返回数据为bytes类型的对象 (即b为前缀, bytes类型)
        logincode = num.decode()
        if logincode == '查不到！':
            time.sleep(2)
            TouchAction(driver).tap(x=776, y=615).perform()  # 获取验证码
            time.sleep(2)  # 获取验证码
            request = urllib.request.Request(logincodeurl)  # 构建请求url
            response = urllib.request.urlopen(request, context=context)  # ssl证书免验证加入,context = context# 打开请求url链接
            num = response.read()  # 读取页面返回信息，python3返回数据为bytes类型的对象 (即b为前缀, bytes类型)
            logincode = num.decode()
        edit_Code = driver.find_element_by_id(
            "com.kamitu.drawsth.standalone.free.android:id/edit_identifyCode")  # 选择验证码输入框
        time.sleep(2)
        edit_Code.send_keys(logincode)
        time.sleep(2)
        TouchAction(driver).tap(x=529, y=833).perform()  # 确定按钮登录


check_login()
time.sleep(15)  # 等待15秒加载进入首页


def check_signwindows():  # 检查是否有每日签到弹窗

    try:
        check_signwindows = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/iv_signin_get")
    except NoSuchElementException:
        print("无签到弹窗")
    else:
        TouchAction(driver).tap(x=953, y=551).perform()  # 关闭签到弹窗
        time.sleep(3)


check_signwindows()
time.sleep(3)

TouchAction(driver).tap(x=525, y=1556).perform()  # 进入接龙页面
time.sleep(3)
driver.back()
time.sleep(3)


def check_signtoast():  # 检查是否开启签到提醒

    try:
        check_signtoast = driver.find_element_by_id(
            "com.kamitu.drawsth.standalone.free.android:id/btn_open_reminder")
    except NoSuchElementException:
        print("无签到提醒弹窗")
    else:
        TouchAction(driver).tap(x=870, y=611).perform()  # 关闭签到提示弹窗


check_signtoast()
time.sleep(3)

TouchAction(driver).tap(x=323, y=1774).perform()  # 选择进入判官
time.sleep(2)
TouchAction(driver).tap(x=536, y=1009).perform()  # 选择开始挑战
time.sleep(3)

a = 1
while a <= 10:
    time.sleep(8)
    TouchAction(driver).tap(x=503, y=1305).perform()  # 点击查看广告
    time.sleep(10)
    try:
        GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
    except NoSuchElementException:
        BB = "  \033[1;31m第\033[0m " + str(a) + " \033[1;31m次\033[0m " + "toutiaosdk广告"
        print(BB)
        time.sleep(40)
        TouchAction(driver).tap(x=979, y=86).perform()  # 关闭toutiao广告
        print("     toutiaosdk广告关闭")
    else:
        CC = "  \033[1;31m第\033[0m " + str(a) + " \033[1;31m次\033[0m " + "GDTsdk广告"
        print(CC)
        time.sleep(55)  # 保证完整看完GTD广告
        driver.back()  # GDTsdk广告关闭
        print("     GDTsdk广告关闭")
    a += 1

time.sleep(7)
driver.back()  # 判官中回到首页
time.sleep(2)
TouchAction(driver).tap(x=439, y=124).perform()  # 返回进入个人中心
time.sleep(2)
TouchAction(driver).tap(x=971, y=158).perform()  # 点击设置
time.sleep(2)
TouchAction(driver).tap(x=536, y=1770).perform()  # 点击退出
time.sleep(2)
TouchAction(driver).tap(x=690, y=1069).perform()  # 弹窗确定退出

#############################################################################################################################################################
mobile = "18017700339"
AA = "\033[1;31mNO.3\033[0m " + mobile + " \033[1;31m开始\033[0m"
print(AA)
time.sleep(5)


def check_login():
    try:
        check_login = driver.find_element_by_id(
            "com.kamitu.drawsth.standalone.free.android:id/iv_mobile_login")  # 选择手机号登录
    except NoSuchElementException:
        print("自动登录成功")
    else:
        TouchAction(driver).tap(x=409, y=1729).perform()  # 点击手机号登录
        time.sleep(2)
        edit_mobile = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/edit_phone")  # 选择手机号输入框
        edit_mobile.send_keys(mobile)
        time.sleep(2)
        TouchAction(driver).tap(x=776, y=615).perform()  # 获取验证码
        time.sleep(2)
        logincodeurl = "https://uc.crazyccy.com/login/main_login/testtool?key=sLQq2_jaKLknsqAwZ&type=1&mobile=" + mobile
        request = urllib.request.Request(logincodeurl)  # 构建请求url
        response = urllib.request.urlopen(request, context=context)  # ssl证书免验证加入,context = context# 打开请求url链接
        num = response.read()  # 读取页面返回信息，python3返回数据为bytes类型的对象 (即b为前缀, bytes类型)
        logincode = num.decode()
        if logincode == '查不到！':
            time.sleep(2)
            TouchAction(driver).tap(x=776, y=615).perform()  # 获取验证码
            time.sleep(2)  # 获取验证码
            request = urllib.request.Request(logincodeurl)  # 构建请求url
            response = urllib.request.urlopen(request, context=context)  # ssl证书免验证加入,context = context# 打开请求url链接
            num = response.read()  # 读取页面返回信息，python3返回数据为bytes类型的对象 (即b为前缀, bytes类型)
            logincode = num.decode()
        edit_Code = driver.find_element_by_id(
            "com.kamitu.drawsth.standalone.free.android:id/edit_identifyCode")  # 选择验证码输入框
        time.sleep(2)
        edit_Code.send_keys(logincode)
        time.sleep(2)
        TouchAction(driver).tap(x=529, y=833).perform()  # 确定按钮登录


check_login()
time.sleep(15)  # 等待15秒加载进入首页


def check_signwindows():  # 检查是否有每日签到弹窗

    try:
        check_signwindows = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/iv_signin_get")
    except NoSuchElementException:
        print("无签到弹窗")
    else:
        TouchAction(driver).tap(x=953, y=551).perform()  # 关闭签到弹窗
        time.sleep(3)


check_signwindows()
time.sleep(3)

TouchAction(driver).tap(x=525, y=1556).perform()  # 进入接龙页面
time.sleep(3)
driver.back()
time.sleep(3)


def check_signtoast():  # 检查是否开启签到提醒

    try:
        check_signtoast = driver.find_element_by_id(
            "com.kamitu.drawsth.standalone.free.android:id/btn_open_reminder")
    except NoSuchElementException:
        print("无签到提醒弹窗")
    else:
        TouchAction(driver).tap(x=870, y=611).perform()  # 关闭签到提示弹窗


check_signtoast()
time.sleep(3)

TouchAction(driver).tap(x=323, y=1774).perform()  # 选择进入判官
time.sleep(2)
TouchAction(driver).tap(x=536, y=1009).perform()  # 选择开始挑战
time.sleep(3)

a = 1
while a <= 10:
    time.sleep(8)
    TouchAction(driver).tap(x=503, y=1305).perform()  # 点击查看广告
    time.sleep(10)
    try:
        GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
    except NoSuchElementException:
        BB = "  \033[1;31m第\033[0m " + str(a) + " \033[1;31m次\033[0m " + "toutiaosdk广告"
        print(BB)
        time.sleep(40)
        TouchAction(driver).tap(x=979, y=86).perform()  # 关闭toutiao广告
        print("     toutiaosdk广告关闭")
    else:
        CC = "  \033[1;31m第\033[0m " + str(a) + " \033[1;31m次\033[0m " + "GDTsdk广告"
        print(CC)
        time.sleep(55)  # 保证完整看完GTD广告
        driver.back()  # GDTsdk广告关闭
        print("     GDTsdk广告关闭")
    a += 1

time.sleep(7)
driver.back()  # 判官中回到首页
time.sleep(2)
TouchAction(driver).tap(x=439, y=124).perform()  # 返回进入个人中心
time.sleep(2)
TouchAction(driver).tap(x=971, y=158).perform()  # 点击设置
time.sleep(2)
TouchAction(driver).tap(x=536, y=1770).perform()  # 点击退出
time.sleep(2)
TouchAction(driver).tap(x=690, y=1069).perform()  # 弹窗确定退出

#############################################################################################################################################################
mobile = "18017700413"
AA = "\033[1;31mNO.4\033[0m " + mobile + " \033[1;31m开始\033[0m"
print(AA)
time.sleep(5)


def check_login():
    try:
        check_login = driver.find_element_by_id(
            "com.kamitu.drawsth.standalone.free.android:id/iv_mobile_login")  # 选择手机号登录
    except NoSuchElementException:
        print("自动登录成功")
    else:
        TouchAction(driver).tap(x=409, y=1729).perform()  # 点击手机号登录
        time.sleep(2)
        edit_mobile = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/edit_phone")  # 选择手机号输入框
        edit_mobile.send_keys(mobile)
        time.sleep(2)
        TouchAction(driver).tap(x=776, y=615).perform()  # 获取验证码
        time.sleep(2)
        logincodeurl = "https://uc.crazyccy.com/login/main_login/testtool?key=sLQq2_jaKLknsqAwZ&type=1&mobile=" + mobile
        request = urllib.request.Request(logincodeurl)  # 构建请求url
        response = urllib.request.urlopen(request, context=context)  # ssl证书免验证加入,context = context# 打开请求url链接
        num = response.read()  # 读取页面返回信息，python3返回数据为bytes类型的对象 (即b为前缀, bytes类型)
        logincode = num.decode()
        if logincode == '查不到！':
            time.sleep(2)
            TouchAction(driver).tap(x=776, y=615).perform()  # 获取验证码
            time.sleep(2)  # 获取验证码
            request = urllib.request.Request(logincodeurl)  # 构建请求url
            response = urllib.request.urlopen(request, context=context)  # ssl证书免验证加入,context = context# 打开请求url链接
            num = response.read()  # 读取页面返回信息，python3返回数据为bytes类型的对象 (即b为前缀, bytes类型)
            logincode = num.decode()
        edit_Code = driver.find_element_by_id(
            "com.kamitu.drawsth.standalone.free.android:id/edit_identifyCode")  # 选择验证码输入框
        time.sleep(2)
        edit_Code.send_keys(logincode)
        time.sleep(2)
        TouchAction(driver).tap(x=529, y=833).perform()  # 确定按钮登录


check_login()
time.sleep(15)  # 等待15秒加载进入首页


def check_signwindows():  # 检查是否有每日签到弹窗

    try:
        check_signwindows = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/iv_signin_get")
    except NoSuchElementException:
        print("无签到弹窗")
    else:
        TouchAction(driver).tap(x=953, y=551).perform()  # 关闭签到弹窗
        time.sleep(3)


check_signwindows()
time.sleep(3)

TouchAction(driver).tap(x=525, y=1556).perform()  # 进入接龙页面
time.sleep(3)
driver.back()
time.sleep(3)


def check_signtoast():  # 检查是否开启签到提醒

    try:
        check_signtoast = driver.find_element_by_id(
            "com.kamitu.drawsth.standalone.free.android:id/btn_open_reminder")
    except NoSuchElementException:
        print("无签到提醒弹窗")
    else:
        TouchAction(driver).tap(x=870, y=611).perform()  # 关闭签到提示弹窗


check_signtoast()
time.sleep(3)

TouchAction(driver).tap(x=323, y=1774).perform()  # 选择进入判官
time.sleep(2)
TouchAction(driver).tap(x=536, y=1009).perform()  # 选择开始挑战
time.sleep(3)

a = 1
while a <= 10:
    time.sleep(8)
    TouchAction(driver).tap(x=503, y=1305).perform()  # 点击查看广告
    time.sleep(10)
    try:
        GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
    except NoSuchElementException:
        BB = "  \033[1;31m第\033[0m " + str(a) + " \033[1;31m次\033[0m " + "toutiaosdk广告"
        print(BB)
        time.sleep(40)
        TouchAction(driver).tap(x=979, y=86).perform()  # 关闭toutiao广告
        print("     toutiaosdk广告关闭")
    else:
        CC = "  \033[1;31m第\033[0m " + str(a) + " \033[1;31m次\033[0m " + "GDTsdk广告"
        print(CC)
        time.sleep(55)  # 保证完整看完GTD广告
        driver.back()  # GDTsdk广告关闭
        print("     GDTsdk广告关闭")
    a += 1

time.sleep(7)
driver.back()  # 判官中回到首页
time.sleep(2)
TouchAction(driver).tap(x=439, y=124).perform()  # 返回进入个人中心
time.sleep(2)
TouchAction(driver).tap(x=971, y=158).perform()  # 点击设置
time.sleep(2)
TouchAction(driver).tap(x=536, y=1770).perform()  # 点击退出
time.sleep(2)
TouchAction(driver).tap(x=690, y=1069).perform()  # 弹窗确定退出

#############################################################################################################################################################
mobile = "18017700414"
AA = "\033[1;31mNO.5\033[0m " + mobile + " \033[1;31m开始\033[0m"
print(AA)
time.sleep(5)


def check_login():
    try:
        check_login = driver.find_element_by_id(
            "com.kamitu.drawsth.standalone.free.android:id/iv_mobile_login")  # 选择手机号登录
    except NoSuchElementException:
        print("自动登录成功")
    else:
        TouchAction(driver).tap(x=409, y=1729).perform()  # 点击手机号登录
        time.sleep(2)
        edit_mobile = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/edit_phone")  # 选择手机号输入框
        edit_mobile.send_keys(mobile)
        time.sleep(2)
        TouchAction(driver).tap(x=776, y=615).perform()  # 获取验证码
        time.sleep(2)
        logincodeurl = "https://uc.crazyccy.com/login/main_login/testtool?key=sLQq2_jaKLknsqAwZ&type=1&mobile=" + mobile
        request = urllib.request.Request(logincodeurl)  # 构建请求url
        response = urllib.request.urlopen(request, context=context)  # ssl证书免验证加入,context = context# 打开请求url链接
        num = response.read()  # 读取页面返回信息，python3返回数据为bytes类型的对象 (即b为前缀, bytes类型)
        logincode = num.decode()
        if logincode == '查不到！':
            time.sleep(2)
            TouchAction(driver).tap(x=776, y=615).perform()  # 获取验证码
            time.sleep(2)  # 获取验证码
            request = urllib.request.Request(logincodeurl)  # 构建请求url
            response = urllib.request.urlopen(request, context=context)  # ssl证书免验证加入,context = context# 打开请求url链接
            num = response.read()  # 读取页面返回信息，python3返回数据为bytes类型的对象 (即b为前缀, bytes类型)
            logincode = num.decode()
        edit_Code = driver.find_element_by_id(
            "com.kamitu.drawsth.standalone.free.android:id/edit_identifyCode")  # 选择验证码输入框
        time.sleep(2)
        edit_Code.send_keys(logincode)
        time.sleep(2)
        TouchAction(driver).tap(x=529, y=833).perform()  # 确定按钮登录


check_login()
time.sleep(15)  # 等待15秒加载进入首页


def check_signwindows():  # 检查是否有每日签到弹窗

    try:
        check_signwindows = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/iv_signin_get")
    except NoSuchElementException:
        print("无签到弹窗")
    else:
        TouchAction(driver).tap(x=953, y=551).perform()  # 关闭签到弹窗
        time.sleep(3)


check_signwindows()
time.sleep(3)

TouchAction(driver).tap(x=525, y=1556).perform()  # 进入接龙页面
time.sleep(3)
driver.back()
time.sleep(3)


def check_signtoast():  # 检查是否开启签到提醒

    try:
        check_signtoast = driver.find_element_by_id(
            "com.kamitu.drawsth.standalone.free.android:id/btn_open_reminder")
    except NoSuchElementException:
        print("无签到提醒弹窗")
    else:
        TouchAction(driver).tap(x=870, y=611).perform()  # 关闭签到提示弹窗


check_signtoast()
time.sleep(3)

TouchAction(driver).tap(x=323, y=1774).perform()  # 选择进入判官
time.sleep(2)
TouchAction(driver).tap(x=536, y=1009).perform()  # 选择开始挑战
time.sleep(3)

a = 1
while a <= 10:
    time.sleep(8)
    TouchAction(driver).tap(x=503, y=1305).perform()  # 点击查看广告
    time.sleep(10)
    try:
        GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
    except NoSuchElementException:
        BB = "  \033[1;31m第\033[0m " + str(a) + " \033[1;31m次\033[0m " + "toutiaosdk广告"
        print(BB)
        time.sleep(40)
        TouchAction(driver).tap(x=979, y=86).perform()  # 关闭toutiao广告
        print("     toutiaosdk广告关闭")
    else:
        CC = "  \033[1;31m第\033[0m " + str(a) + " \033[1;31m次\033[0m " + "GDTsdk广告"
        print(CC)
        time.sleep(55)  # 保证完整看完GTD广告
        driver.back()  # GDTsdk广告关闭
        print("     GDTsdk广告关闭")
    a += 1

time.sleep(7)
driver.back()  # 判官中回到首页
time.sleep(2)
TouchAction(driver).tap(x=439, y=124).perform()  # 返回进入个人中心
time.sleep(2)
TouchAction(driver).tap(x=971, y=158).perform()  # 点击设置
time.sleep(2)
TouchAction(driver).tap(x=536, y=1770).perform()  # 点击退出
time.sleep(2)
TouchAction(driver).tap(x=690, y=1069).perform()  # 弹窗确定退出

#############################################################################################################################################################
mobile = "18017700521"
AA = "\033[1;31mNO.6\033[0m " + mobile + " \033[1;31m开始\033[0m"
print(AA)
time.sleep(5)


def check_login():
    try:
        check_login = driver.find_element_by_id(
            "com.kamitu.drawsth.standalone.free.android:id/iv_mobile_login")  # 选择手机号登录
    except NoSuchElementException:
        print("自动登录成功")
    else:
        TouchAction(driver).tap(x=409, y=1729).perform()  # 点击手机号登录
        time.sleep(2)
        edit_mobile = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/edit_phone")  # 选择手机号输入框
        edit_mobile.send_keys(mobile)
        time.sleep(2)
        TouchAction(driver).tap(x=776, y=615).perform()  # 获取验证码
        time.sleep(2)
        logincodeurl = "https://uc.crazyccy.com/login/main_login/testtool?key=sLQq2_jaKLknsqAwZ&type=1&mobile=" + mobile
        request = urllib.request.Request(logincodeurl)  # 构建请求url
        response = urllib.request.urlopen(request, context=context)  # ssl证书免验证加入,context = context# 打开请求url链接
        num = response.read()  # 读取页面返回信息，python3返回数据为bytes类型的对象 (即b为前缀, bytes类型)
        logincode = num.decode()
        if logincode == '查不到！':
            time.sleep(2)
            TouchAction(driver).tap(x=776, y=615).perform()  # 获取验证码
            time.sleep(2)  # 获取验证码
            request = urllib.request.Request(logincodeurl)  # 构建请求url
            response = urllib.request.urlopen(request, context=context)  # ssl证书免验证加入,context = context# 打开请求url链接
            num = response.read()  # 读取页面返回信息，python3返回数据为bytes类型的对象 (即b为前缀, bytes类型)
            logincode = num.decode()
        edit_Code = driver.find_element_by_id(
            "com.kamitu.drawsth.standalone.free.android:id/edit_identifyCode")  # 选择验证码输入框
        time.sleep(2)
        edit_Code.send_keys(logincode)
        time.sleep(2)
        TouchAction(driver).tap(x=529, y=833).perform()  # 确定按钮登录


check_login()
time.sleep(15)  # 等待15秒加载进入首页


def check_signwindows():  # 检查是否有每日签到弹窗

    try:
        check_signwindows = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/iv_signin_get")
    except NoSuchElementException:
        print("无签到弹窗")
    else:
        TouchAction(driver).tap(x=953, y=551).perform()  # 关闭签到弹窗
        time.sleep(3)


check_signwindows()
time.sleep(3)

TouchAction(driver).tap(x=525, y=1556).perform()  # 进入接龙页面
time.sleep(3)
driver.back()
time.sleep(3)


def check_signtoast():  # 检查是否开启签到提醒

    try:
        check_signtoast = driver.find_element_by_id(
            "com.kamitu.drawsth.standalone.free.android:id/btn_open_reminder")
    except NoSuchElementException:
        print("无签到提醒弹窗")
    else:
        TouchAction(driver).tap(x=870, y=611).perform()  # 关闭签到提示弹窗


check_signtoast()
time.sleep(3)

TouchAction(driver).tap(x=323, y=1774).perform()  # 选择进入判官
time.sleep(2)
TouchAction(driver).tap(x=536, y=1009).perform()  # 选择开始挑战
time.sleep(3)

a = 1
while a <= 10:
    time.sleep(8)
    TouchAction(driver).tap(x=503, y=1305).perform()  # 点击查看广告
    time.sleep(10)
    try:
        GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
    except NoSuchElementException:
        BB = "  \033[1;31m第\033[0m " + str(a) + " \033[1;31m次\033[0m " + "toutiaosdk广告"
        print(BB)
        time.sleep(40)
        TouchAction(driver).tap(x=979, y=86).perform()  # 关闭toutiao广告
        print("     toutiaosdk广告关闭")
    else:
        CC = "  \033[1;31m第\033[0m " + str(a) + " \033[1;31m次\033[0m " + "GDTsdk广告"
        print(CC)
        time.sleep(55)  # 保证完整看完GTD广告
        driver.back()  # GDTsdk广告关闭
        print("     GDTsdk广告关闭")
    a += 1

time.sleep(7)
driver.back()  # 判官中回到首页
time.sleep(2)
TouchAction(driver).tap(x=439, y=124).perform()  # 返回进入个人中心
time.sleep(2)
TouchAction(driver).tap(x=971, y=158).perform()  # 点击设置
time.sleep(2)
TouchAction(driver).tap(x=536, y=1770).perform()  # 点击退出
time.sleep(2)
TouchAction(driver).tap(x=690, y=1069).perform()  # 弹窗确定退出

#############################################################################################################################################################
mobile = "18017700715"
AA = "\033[1;31mNO.7\033[0m " + mobile + " \033[1;31m开始\033[0m"
print(AA)
time.sleep(5)


def check_login():
    try:
        check_login = driver.find_element_by_id(
            "com.kamitu.drawsth.standalone.free.android:id/iv_mobile_login")  # 选择手机号登录
    except NoSuchElementException:
        print("自动登录成功")
    else:
        TouchAction(driver).tap(x=409, y=1729).perform()  # 点击手机号登录
        time.sleep(2)
        edit_mobile = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/edit_phone")  # 选择手机号输入框
        edit_mobile.send_keys(mobile)
        time.sleep(2)
        TouchAction(driver).tap(x=776, y=615).perform()  # 获取验证码
        time.sleep(2)
        logincodeurl = "https://uc.crazyccy.com/login/main_login/testtool?key=sLQq2_jaKLknsqAwZ&type=1&mobile=" + mobile
        request = urllib.request.Request(logincodeurl)  # 构建请求url
        response = urllib.request.urlopen(request, context=context)  # ssl证书免验证加入,context = context# 打开请求url链接
        num = response.read()  # 读取页面返回信息，python3返回数据为bytes类型的对象 (即b为前缀, bytes类型)
        logincode = num.decode()
        if logincode == '查不到！':
            time.sleep(2)
            TouchAction(driver).tap(x=776, y=615).perform()  # 获取验证码
            time.sleep(2)  # 获取验证码
            request = urllib.request.Request(logincodeurl)  # 构建请求url
            response = urllib.request.urlopen(request, context=context)  # ssl证书免验证加入,context = context# 打开请求url链接
            num = response.read()  # 读取页面返回信息，python3返回数据为bytes类型的对象 (即b为前缀, bytes类型)
            logincode = num.decode()
        edit_Code = driver.find_element_by_id(
            "com.kamitu.drawsth.standalone.free.android:id/edit_identifyCode")  # 选择验证码输入框
        time.sleep(2)
        edit_Code.send_keys(logincode)
        time.sleep(2)
        TouchAction(driver).tap(x=529, y=833).perform()  # 确定按钮登录


check_login()
time.sleep(15)  # 等待15秒加载进入首页


def check_signwindows():  # 检查是否有每日签到弹窗

    try:
        check_signwindows = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/iv_signin_get")
    except NoSuchElementException:
        print("无签到弹窗")
    else:
        TouchAction(driver).tap(x=953, y=551).perform()  # 关闭签到弹窗
        time.sleep(3)


check_signwindows()
time.sleep(3)

TouchAction(driver).tap(x=525, y=1556).perform()  # 进入接龙页面
time.sleep(3)
driver.back()
time.sleep(3)


def check_signtoast():  # 检查是否开启签到提醒

    try:
        check_signtoast = driver.find_element_by_id(
            "com.kamitu.drawsth.standalone.free.android:id/btn_open_reminder")
    except NoSuchElementException:
        print("无签到提醒弹窗")
    else:
        TouchAction(driver).tap(x=870, y=611).perform()  # 关闭签到提示弹窗


check_signtoast()
time.sleep(3)

TouchAction(driver).tap(x=323, y=1774).perform()  # 选择进入判官
time.sleep(2)
TouchAction(driver).tap(x=536, y=1009).perform()  # 选择开始挑战
time.sleep(3)

a = 1
while a <= 10:
    time.sleep(8)
    TouchAction(driver).tap(x=503, y=1305).perform()  # 点击查看广告
    time.sleep(10)
    try:
        GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
    except NoSuchElementException:
        BB = "  \033[1;31m第\033[0m " + str(a) + " \033[1;31m次\033[0m " + "toutiaosdk广告"
        print(BB)
        time.sleep(40)
        TouchAction(driver).tap(x=979, y=86).perform()  # 关闭toutiao广告
        print("     toutiaosdk广告关闭")
    else:
        CC = "  \033[1;31m第\033[0m " + str(a) + " \033[1;31m次\033[0m " + "GDTsdk广告"
        print(CC)
        time.sleep(55)  # 保证完整看完GTD广告
        driver.back()  # GDTsdk广告关闭
        print("     GDTsdk广告关闭")
    a += 1

time.sleep(7)
driver.back()  # 判官中回到首页
time.sleep(2)
TouchAction(driver).tap(x=439, y=124).perform()  # 返回进入个人中心
time.sleep(2)
TouchAction(driver).tap(x=971, y=158).perform()  # 点击设置
time.sleep(2)
TouchAction(driver).tap(x=536, y=1770).perform()  # 点击退出
time.sleep(2)
TouchAction(driver).tap(x=690, y=1069).perform()  # 弹窗确定退出

#############################################################################################################################################################
mobile = "18220860324"
AA = "\033[1;31mNO.8\033[0m " + mobile + " \033[1;31m开始\033[0m"
print(AA)
time.sleep(5)


def check_login():
    try:
        check_login = driver.find_element_by_id(
            "com.kamitu.drawsth.standalone.free.android:id/iv_mobile_login")  # 选择手机号登录
    except NoSuchElementException:
        print("自动登录成功")
    else:
        TouchAction(driver).tap(x=409, y=1729).perform()  # 点击手机号登录
        time.sleep(2)
        edit_mobile = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/edit_phone")  # 选择手机号输入框
        edit_mobile.send_keys(mobile)
        time.sleep(2)
        TouchAction(driver).tap(x=776, y=615).perform()  # 获取验证码
        time.sleep(2)
        logincodeurl = "https://uc.crazyccy.com/login/main_login/testtool?key=sLQq2_jaKLknsqAwZ&type=1&mobile=" + mobile
        request = urllib.request.Request(logincodeurl)  # 构建请求url
        response = urllib.request.urlopen(request, context=context)  # ssl证书免验证加入,context = context# 打开请求url链接
        num = response.read()  # 读取页面返回信息，python3返回数据为bytes类型的对象 (即b为前缀, bytes类型)
        logincode = num.decode()
        if logincode == '查不到！':
            time.sleep(2)
            TouchAction(driver).tap(x=776, y=615).perform()  # 获取验证码
            time.sleep(2)  # 获取验证码
            request = urllib.request.Request(logincodeurl)  # 构建请求url
            response = urllib.request.urlopen(request, context=context)  # ssl证书免验证加入,context = context# 打开请求url链接
            num = response.read()  # 读取页面返回信息，python3返回数据为bytes类型的对象 (即b为前缀, bytes类型)
            logincode = num.decode()
        edit_Code = driver.find_element_by_id(
            "com.kamitu.drawsth.standalone.free.android:id/edit_identifyCode")  # 选择验证码输入框
        time.sleep(2)
        edit_Code.send_keys(logincode)
        time.sleep(2)
        TouchAction(driver).tap(x=529, y=833).perform()  # 确定按钮登录


check_login()
time.sleep(15)  # 等待15秒加载进入首页


def check_signwindows():  # 检查是否有每日签到弹窗

    try:
        check_signwindows = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/iv_signin_get")
    except NoSuchElementException:
        print("无签到弹窗")
    else:
        TouchAction(driver).tap(x=953, y=551).perform()  # 关闭签到弹窗
        time.sleep(3)


check_signwindows()
time.sleep(3)

TouchAction(driver).tap(x=525, y=1556).perform()  # 进入接龙页面
time.sleep(3)
driver.back()
time.sleep(3)


def check_signtoast():  # 检查是否开启签到提醒

    try:
        check_signtoast = driver.find_element_by_id(
            "com.kamitu.drawsth.standalone.free.android:id/btn_open_reminder")
    except NoSuchElementException:
        print("无签到提醒弹窗")
    else:
        TouchAction(driver).tap(x=870, y=611).perform()  # 关闭签到提示弹窗


check_signtoast()
time.sleep(3)

TouchAction(driver).tap(x=323, y=1774).perform()  # 选择进入判官
time.sleep(2)
TouchAction(driver).tap(x=536, y=1009).perform()  # 选择开始挑战
time.sleep(3)

a = 1
while a <= 10:
    time.sleep(8)
    TouchAction(driver).tap(x=503, y=1305).perform()  # 点击查看广告
    time.sleep(10)
    try:
        GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
    except NoSuchElementException:
        BB = "  \033[1;31m第\033[0m " + str(a) + " \033[1;31m次\033[0m " + "toutiaosdk广告"
        print(BB)
        time.sleep(40)
        TouchAction(driver).tap(x=979, y=86).perform()  # 关闭toutiao广告
        print("     toutiaosdk广告关闭")
    else:
        CC = "  \033[1;31m第\033[0m " + str(a) + " \033[1;31m次\033[0m " + "GDTsdk广告"
        print(CC)
        time.sleep(55)  # 保证完整看完GTD广告
        driver.back()  # GDTsdk广告关闭
        print("     GDTsdk广告关闭")
    a += 1

time.sleep(7)
driver.back()  # 判官中回到首页
time.sleep(2)
TouchAction(driver).tap(x=439, y=124).perform()  # 返回进入个人中心
time.sleep(2)
TouchAction(driver).tap(x=971, y=158).perform()  # 点击设置
time.sleep(2)
TouchAction(driver).tap(x=536, y=1770).perform()  # 点击退出
time.sleep(2)
TouchAction(driver).tap(x=690, y=1069).perform()  # 弹窗确定退出

#############################################################################################################################################################
mobile = "18116699805"
AA = "\033[1;31mNO.9\033[0m " + mobile + " \033[1;31m开始\033[0m"
print(AA)
time.sleep(5)


def check_login():
    try:
        check_login = driver.find_element_by_id(
            "com.kamitu.drawsth.standalone.free.android:id/iv_mobile_login")  # 选择手机号登录
    except NoSuchElementException:
        print("自动登录成功")
    else:
        TouchAction(driver).tap(x=409, y=1729).perform()  # 点击手机号登录
        time.sleep(2)
        edit_mobile = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/edit_phone")  # 选择手机号输入框
        edit_mobile.send_keys(mobile)
        time.sleep(2)
        TouchAction(driver).tap(x=776, y=615).perform()  # 获取验证码
        time.sleep(2)
        logincodeurl = "https://uc.crazyccy.com/login/main_login/testtool?key=sLQq2_jaKLknsqAwZ&type=1&mobile=" + mobile
        request = urllib.request.Request(logincodeurl)  # 构建请求url
        response = urllib.request.urlopen(request, context=context)  # ssl证书免验证加入,context = context# 打开请求url链接
        num = response.read()  # 读取页面返回信息，python3返回数据为bytes类型的对象 (即b为前缀, bytes类型)
        logincode = num.decode()
        if logincode == '查不到！':
            time.sleep(2)
            TouchAction(driver).tap(x=776, y=615).perform()  # 获取验证码
            time.sleep(2)  # 获取验证码
            request = urllib.request.Request(logincodeurl)  # 构建请求url
            response = urllib.request.urlopen(request, context=context)  # ssl证书免验证加入,context = context# 打开请求url链接
            num = response.read()  # 读取页面返回信息，python3返回数据为bytes类型的对象 (即b为前缀, bytes类型)
            logincode = num.decode()
        edit_Code = driver.find_element_by_id(
            "com.kamitu.drawsth.standalone.free.android:id/edit_identifyCode")  # 选择验证码输入框
        time.sleep(2)
        edit_Code.send_keys(logincode)
        time.sleep(2)
        TouchAction(driver).tap(x=529, y=833).perform()  # 确定按钮登录


check_login()
time.sleep(15)  # 等待15秒加载进入首页


def check_signwindows():  # 检查是否有每日签到弹窗

    try:
        check_signwindows = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/iv_signin_get")
    except NoSuchElementException:
        print("无签到弹窗")
    else:
        TouchAction(driver).tap(x=953, y=551).perform()  # 关闭签到弹窗
        time.sleep(3)


check_signwindows()
time.sleep(3)

TouchAction(driver).tap(x=525, y=1556).perform()  # 进入接龙页面
time.sleep(3)
driver.back()
time.sleep(3)


def check_signtoast():  # 检查是否开启签到提醒

    try:
        check_signtoast = driver.find_element_by_id(
            "com.kamitu.drawsth.standalone.free.android:id/btn_open_reminder")
    except NoSuchElementException:
        print("无签到提醒弹窗")
    else:
        TouchAction(driver).tap(x=870, y=611).perform()  # 关闭签到提示弹窗


check_signtoast()
time.sleep(3)

TouchAction(driver).tap(x=323, y=1774).perform()  # 选择进入判官
time.sleep(2)
TouchAction(driver).tap(x=536, y=1009).perform()  # 选择开始挑战
time.sleep(3)

a = 1
while a <= 10:
    time.sleep(8)
    TouchAction(driver).tap(x=503, y=1305).perform()  # 点击查看广告
    time.sleep(10)
    try:
        GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
    except NoSuchElementException:
        BB = "  \033[1;31m第\033[0m " + str(a) + " \033[1;31m次\033[0m " + "toutiaosdk广告"
        print(BB)
        time.sleep(40)
        TouchAction(driver).tap(x=979, y=86).perform()  # 关闭toutiao广告
        print("     toutiaosdk广告关闭")
    else:
        CC = "  \033[1;31m第\033[0m " + str(a) + " \033[1;31m次\033[0m " + "GDTsdk广告"
        print(CC)
        time.sleep(55)  # 保证完整看完GTD广告
        driver.back()  # GDTsdk广告关闭
        print("     GDTsdk广告关闭")
    a += 1

time.sleep(7)
driver.back()  # 判官中回到首页
time.sleep(2)
TouchAction(driver).tap(x=439, y=124).perform()  # 返回进入个人中心
time.sleep(2)
TouchAction(driver).tap(x=971, y=158).perform()  # 点击设置
time.sleep(2)
TouchAction(driver).tap(x=536, y=1770).perform()  # 点击退出
time.sleep(2)
TouchAction(driver).tap(x=690, y=1069).perform()  # 弹窗确定退出

#############################################################################################################################################################
mobile = "13161057550"
AA = "\033[1;31mNO.10\033[0m " + mobile + " \033[1;31m开始\033[0m"
print(AA)
time.sleep(5)


def check_login():
    try:
        check_login = driver.find_element_by_id(
            "com.kamitu.drawsth.standalone.free.android:id/iv_mobile_login")  # 选择手机号登录
    except NoSuchElementException:
        print("自动登录成功")
    else:
        TouchAction(driver).tap(x=409, y=1729).perform()  # 点击手机号登录
        time.sleep(2)
        edit_mobile = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/edit_phone")  # 选择手机号输入框
        edit_mobile.send_keys(mobile)
        time.sleep(2)
        TouchAction(driver).tap(x=776, y=615).perform()  # 获取验证码
        time.sleep(2)
        logincodeurl = "https://uc.crazyccy.com/login/main_login/testtool?key=sLQq2_jaKLknsqAwZ&type=1&mobile=" + mobile
        request = urllib.request.Request(logincodeurl)  # 构建请求url
        response = urllib.request.urlopen(request, context=context)  # ssl证书免验证加入,context = context# 打开请求url链接
        num = response.read()  # 读取页面返回信息，python3返回数据为bytes类型的对象 (即b为前缀, bytes类型)
        logincode = num.decode()
        if logincode == '查不到！':
            time.sleep(2)
            TouchAction(driver).tap(x=776, y=615).perform()  # 获取验证码
            time.sleep(2)  # 获取验证码
            request = urllib.request.Request(logincodeurl)  # 构建请求url
            response = urllib.request.urlopen(request, context=context)  # ssl证书免验证加入,context = context# 打开请求url链接
            num = response.read()  # 读取页面返回信息，python3返回数据为bytes类型的对象 (即b为前缀, bytes类型)
            logincode = num.decode()
        edit_Code = driver.find_element_by_id(
            "com.kamitu.drawsth.standalone.free.android:id/edit_identifyCode")  # 选择验证码输入框
        time.sleep(2)
        edit_Code.send_keys(logincode)
        time.sleep(2)
        TouchAction(driver).tap(x=529, y=833).perform()  # 确定按钮登录


check_login()
time.sleep(15)  # 等待15秒加载进入首页


def check_signwindows():  # 检查是否有每日签到弹窗

    try:
        check_signwindows = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/iv_signin_get")
    except NoSuchElementException:
        print("无签到弹窗")
    else:
        TouchAction(driver).tap(x=953, y=551).perform()  # 关闭签到弹窗
        time.sleep(3)


check_signwindows()
time.sleep(3)

TouchAction(driver).tap(x=525, y=1556).perform()  # 进入接龙页面
time.sleep(3)
driver.back()
time.sleep(3)


def check_signtoast():  # 检查是否开启签到提醒

    try:
        check_signtoast = driver.find_element_by_id(
            "com.kamitu.drawsth.standalone.free.android:id/btn_open_reminder")
    except NoSuchElementException:
        print("无签到提醒弹窗")
    else:
        TouchAction(driver).tap(x=870, y=611).perform()  # 关闭签到提示弹窗


check_signtoast()
time.sleep(3)

TouchAction(driver).tap(x=323, y=1774).perform()  # 选择进入判官
time.sleep(2)
TouchAction(driver).tap(x=536, y=1009).perform()  # 选择开始挑战
time.sleep(3)

a = 1
while a <= 10:
    time.sleep(8)
    TouchAction(driver).tap(x=503, y=1305).perform()  # 点击查看广告
    time.sleep(10)
    try:
        GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
    except NoSuchElementException:
        BB = "  \033[1;31m第\033[0m " + str(a) + " \033[1;31m次\033[0m " + "toutiaosdk广告"
        print(BB)
        time.sleep(40)
        TouchAction(driver).tap(x=979, y=86).perform()  # 关闭toutiao广告
        print("     toutiaosdk广告关闭")
    else:
        CC = "  \033[1;31m第\033[0m " + str(a) + " \033[1;31m次\033[0m " + "GDTsdk广告"
        print(CC)
        time.sleep(55)  # 保证完整看完GTD广告
        driver.back()  # GDTsdk广告关闭
        print("     GDTsdk广告关闭")
    a += 1

time.sleep(7)
driver.back()  # 判官中回到首页
time.sleep(2)
TouchAction(driver).tap(x=439, y=124).perform()  # 返回进入个人中心
time.sleep(2)
TouchAction(driver).tap(x=971, y=158).perform()  # 点击设置
time.sleep(2)
TouchAction(driver).tap(x=536, y=1770).perform()  # 点击退出
time.sleep(2)
TouchAction(driver).tap(x=690, y=1069).perform()  # 弹窗确定退出

#############################################################################################################################################################
mobile = "18014400369"
AA = "\033[1;31mNO.11\033[0m " + mobile + " \033[1;31m开始\033[0m"
print(AA)
time.sleep(5)


def check_login():
    try:
        check_login = driver.find_element_by_id(
            "com.kamitu.drawsth.standalone.free.android:id/iv_mobile_login")  # 选择手机号登录
    except NoSuchElementException:
        print("自动登录成功")
    else:
        TouchAction(driver).tap(x=409, y=1729).perform()  # 点击手机号登录
        time.sleep(2)
        edit_mobile = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/edit_phone")  # 选择手机号输入框
        edit_mobile.send_keys(mobile)
        time.sleep(2)
        TouchAction(driver).tap(x=776, y=615).perform()  # 获取验证码
        time.sleep(2)
        logincodeurl = "https://uc.crazyccy.com/login/main_login/testtool?key=sLQq2_jaKLknsqAwZ&type=1&mobile=" + mobile
        request = urllib.request.Request(logincodeurl)  # 构建请求url
        response = urllib.request.urlopen(request, context=context)  # ssl证书免验证加入,context = context# 打开请求url链接
        num = response.read()  # 读取页面返回信息，python3返回数据为bytes类型的对象 (即b为前缀, bytes类型)
        logincode = num.decode()
        if logincode == '查不到！':
            time.sleep(2)
            TouchAction(driver).tap(x=776, y=615).perform()  # 获取验证码
            time.sleep(2)  # 获取验证码
            request = urllib.request.Request(logincodeurl)  # 构建请求url
            response = urllib.request.urlopen(request, context=context)  # ssl证书免验证加入,context = context# 打开请求url链接
            num = response.read()  # 读取页面返回信息，python3返回数据为bytes类型的对象 (即b为前缀, bytes类型)
            logincode = num.decode()
        edit_Code = driver.find_element_by_id(
            "com.kamitu.drawsth.standalone.free.android:id/edit_identifyCode")  # 选择验证码输入框
        time.sleep(2)
        edit_Code.send_keys(logincode)
        time.sleep(2)
        TouchAction(driver).tap(x=529, y=833).perform()  # 确定按钮登录


check_login()
time.sleep(15)  # 等待15秒加载进入首页


def check_signwindows():  # 检查是否有每日签到弹窗

    try:
        check_signwindows = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/iv_signin_get")
    except NoSuchElementException:
        print("无签到弹窗")
    else:
        TouchAction(driver).tap(x=953, y=551).perform()  # 关闭签到弹窗
        time.sleep(3)


check_signwindows()
time.sleep(3)

TouchAction(driver).tap(x=525, y=1556).perform()  # 进入接龙页面
time.sleep(3)
driver.back()
time.sleep(3)


def check_signtoast():  # 检查是否开启签到提醒

    try:
        check_signtoast = driver.find_element_by_id(
            "com.kamitu.drawsth.standalone.free.android:id/btn_open_reminder")
    except NoSuchElementException:
        print("无签到提醒弹窗")
    else:
        TouchAction(driver).tap(x=870, y=611).perform()  # 关闭签到提示弹窗


check_signtoast()
time.sleep(3)

TouchAction(driver).tap(x=323, y=1774).perform()  # 选择进入判官
time.sleep(2)
TouchAction(driver).tap(x=536, y=1009).perform()  # 选择开始挑战
time.sleep(3)

a = 1
while a <= 10:
    time.sleep(8)
    TouchAction(driver).tap(x=503, y=1305).perform()  # 点击查看广告
    time.sleep(10)
    try:
        GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
    except NoSuchElementException:
        BB = "  \033[1;31m第\033[0m " + str(a) + " \033[1;31m次\033[0m " + "toutiaosdk广告"
        print(BB)
        time.sleep(40)
        TouchAction(driver).tap(x=979, y=86).perform()  # 关闭toutiao广告
        print("     toutiaosdk广告关闭")
    else:
        CC = "  \033[1;31m第\033[0m " + str(a) + " \033[1;31m次\033[0m " + "GDTsdk广告"
        print(CC)
        time.sleep(55)  # 保证完整看完GTD广告
        driver.back()  # GDTsdk广告关闭
        print("     GDTsdk广告关闭")
    a += 1

time.sleep(7)
driver.back()  # 判官中回到首页
time.sleep(2)
TouchAction(driver).tap(x=439, y=124).perform()  # 返回进入个人中心
time.sleep(2)
TouchAction(driver).tap(x=971, y=158).perform()  # 点击设置
time.sleep(2)
TouchAction(driver).tap(x=536, y=1770).perform()  # 点击退出
time.sleep(2)
TouchAction(driver).tap(x=690, y=1069).perform()  # 弹窗确定退出

#############################################################################################################################################################
mobile = "15721403717"
AA = "\033[1;31mNO.12\033[0m " + mobile + " \033[1;31m开始\033[0m"
print(AA)
time.sleep(5)


def check_login():
    try:
        check_login = driver.find_element_by_id(
            "com.kamitu.drawsth.standalone.free.android:id/iv_mobile_login")  # 选择手机号登录
    except NoSuchElementException:
        print("自动登录成功")
    else:
        TouchAction(driver).tap(x=409, y=1729).perform()  # 点击手机号登录
        time.sleep(2)
        edit_mobile = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/edit_phone")  # 选择手机号输入框
        edit_mobile.send_keys(mobile)
        time.sleep(2)
        TouchAction(driver).tap(x=776, y=615).perform()  # 获取验证码
        time.sleep(2)
        logincodeurl = "https://uc.crazyccy.com/login/main_login/testtool?key=sLQq2_jaKLknsqAwZ&type=1&mobile=" + mobile
        request = urllib.request.Request(logincodeurl)  # 构建请求url
        response = urllib.request.urlopen(request, context=context)  # ssl证书免验证加入,context = context# 打开请求url链接
        num = response.read()  # 读取页面返回信息，python3返回数据为bytes类型的对象 (即b为前缀, bytes类型)
        logincode = num.decode()
        if logincode == '查不到！':
            time.sleep(2)
            TouchAction(driver).tap(x=776, y=615).perform()  # 获取验证码
            time.sleep(2)  # 获取验证码
            request = urllib.request.Request(logincodeurl)  # 构建请求url
            response = urllib.request.urlopen(request, context=context)  # ssl证书免验证加入,context = context# 打开请求url链接
            num = response.read()  # 读取页面返回信息，python3返回数据为bytes类型的对象 (即b为前缀, bytes类型)
            logincode = num.decode()
        edit_Code = driver.find_element_by_id(
            "com.kamitu.drawsth.standalone.free.android:id/edit_identifyCode")  # 选择验证码输入框
        time.sleep(2)
        edit_Code.send_keys(logincode)
        time.sleep(2)
        TouchAction(driver).tap(x=529, y=833).perform()  # 确定按钮登录


check_login()
time.sleep(15)  # 等待15秒加载进入首页


def check_signwindows():  # 检查是否有每日签到弹窗

    try:
        check_signwindows = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/iv_signin_get")
    except NoSuchElementException:
        print("无签到弹窗")
    else:
        TouchAction(driver).tap(x=953, y=551).perform()  # 关闭签到弹窗
        time.sleep(3)


check_signwindows()
time.sleep(3)

TouchAction(driver).tap(x=525, y=1556).perform()  # 进入接龙页面
time.sleep(3)
driver.back()
time.sleep(3)


def check_signtoast():  # 检查是否开启签到提醒

    try:
        check_signtoast = driver.find_element_by_id(
            "com.kamitu.drawsth.standalone.free.android:id/btn_open_reminder")
    except NoSuchElementException:
        print("无签到提醒弹窗")
    else:
        TouchAction(driver).tap(x=870, y=611).perform()  # 关闭签到提示弹窗


check_signtoast()
time.sleep(3)

TouchAction(driver).tap(x=323, y=1774).perform()  # 选择进入判官
time.sleep(2)
TouchAction(driver).tap(x=536, y=1009).perform()  # 选择开始挑战
time.sleep(3)

a = 1
while a <= 10:
    time.sleep(8)
    TouchAction(driver).tap(x=503, y=1305).perform()  # 点击查看广告
    time.sleep(10)
    try:
        GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
    except NoSuchElementException:
        BB = "  \033[1;31m第\033[0m " + str(a) + " \033[1;31m次\033[0m " + "toutiaosdk广告"
        print(BB)
        time.sleep(40)
        TouchAction(driver).tap(x=979, y=86).perform()  # 关闭toutiao广告
        print("     toutiaosdk广告关闭")
    else:
        CC = "  \033[1;31m第\033[0m " + str(a) + " \033[1;31m次\033[0m " + "GDTsdk广告"
        print(CC)
        time.sleep(55)  # 保证完整看完GTD广告
        driver.back()  # GDTsdk广告关闭
        print("     GDTsdk广告关闭")
    a += 1

time.sleep(7)
driver.back()  # 判官中回到首页
time.sleep(2)
TouchAction(driver).tap(x=439, y=124).perform()  # 返回进入个人中心
time.sleep(2)
TouchAction(driver).tap(x=971, y=158).perform()  # 点击设置
time.sleep(2)
TouchAction(driver).tap(x=536, y=1770).perform()  # 点击退出
time.sleep(2)
TouchAction(driver).tap(x=690, y=1069).perform()  # 弹窗确定退出

#############################################################################################################################################################
mobile = "15721403717"
AA = "\033[1;31mNO.13\033[0m " + mobile + " \033[1;31m开始\033[0m"
print(AA)
time.sleep(5)


def check_login():
    try:
        check_login = driver.find_element_by_id(
            "com.kamitu.drawsth.standalone.free.android:id/iv_mobile_login")  # 选择手机号登录
    except NoSuchElementException:
        print("自动登录成功")
    else:
        TouchAction(driver).tap(x=409, y=1729).perform()  # 点击手机号登录
        time.sleep(2)
        edit_mobile = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/edit_phone")  # 选择手机号输入框
        edit_mobile.send_keys(mobile)
        time.sleep(2)
        TouchAction(driver).tap(x=776, y=615).perform()  # 获取验证码
        time.sleep(2)
        logincodeurl = "https://uc.crazyccy.com/login/main_login/testtool?key=sLQq2_jaKLknsqAwZ&type=1&mobile=" + mobile
        request = urllib.request.Request(logincodeurl)  # 构建请求url
        response = urllib.request.urlopen(request, context=context)  # ssl证书免验证加入,context = context# 打开请求url链接
        num = response.read()  # 读取页面返回信息，python3返回数据为bytes类型的对象 (即b为前缀, bytes类型)
        logincode = num.decode()
        if logincode == '查不到！':
            time.sleep(2)
            TouchAction(driver).tap(x=776, y=615).perform()  # 获取验证码
            time.sleep(2)  # 获取验证码
            request = urllib.request.Request(logincodeurl)  # 构建请求url
            response = urllib.request.urlopen(request, context=context)  # ssl证书免验证加入,context = context# 打开请求url链接
            num = response.read()  # 读取页面返回信息，python3返回数据为bytes类型的对象 (即b为前缀, bytes类型)
            logincode = num.decode()
        edit_Code = driver.find_element_by_id(
            "com.kamitu.drawsth.standalone.free.android:id/edit_identifyCode")  # 选择验证码输入框
        time.sleep(2)
        edit_Code.send_keys(logincode)
        time.sleep(2)
        TouchAction(driver).tap(x=529, y=833).perform()  # 确定按钮登录


check_login()
time.sleep(15)  # 等待15秒加载进入首页


def check_signwindows():  # 检查是否有每日签到弹窗

    try:
        check_signwindows = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/iv_signin_get")
    except NoSuchElementException:
        print("无签到弹窗")
    else:
        TouchAction(driver).tap(x=953, y=551).perform()  # 关闭签到弹窗
        time.sleep(3)


check_signwindows()
time.sleep(3)

TouchAction(driver).tap(x=525, y=1556).perform()  # 进入接龙页面
time.sleep(3)
driver.back()
time.sleep(3)


def check_signtoast():  # 检查是否开启签到提醒

    try:
        check_signtoast = driver.find_element_by_id(
            "com.kamitu.drawsth.standalone.free.android:id/btn_open_reminder")
    except NoSuchElementException:
        print("无签到提醒弹窗")
    else:
        TouchAction(driver).tap(x=870, y=611).perform()  # 关闭签到提示弹窗


check_signtoast()
time.sleep(3)

TouchAction(driver).tap(x=323, y=1774).perform()  # 选择进入判官
time.sleep(2)
TouchAction(driver).tap(x=536, y=1009).perform()  # 选择开始挑战
time.sleep(3)

a = 1
while a <= 10:
    time.sleep(8)
    TouchAction(driver).tap(x=503, y=1305).perform()  # 点击查看广告
    time.sleep(10)
    try:
        GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
    except NoSuchElementException:
        BB = "  \033[1;31m第\033[0m " + str(a) + " \033[1;31m次\033[0m " + "toutiaosdk广告"
        print(BB)
        time.sleep(40)
        TouchAction(driver).tap(x=979, y=86).perform()  # 关闭toutiao广告
        print("     toutiaosdk广告关闭")
    else:
        CC = "  \033[1;31m第\033[0m " + str(a) + " \033[1;31m次\033[0m " + "GDTsdk广告"
        print(CC)
        time.sleep(55)  # 保证完整看完GTD广告
        driver.back()  # GDTsdk广告关闭
        print("     GDTsdk广告关闭")
    a += 1

time.sleep(7)
driver.back()  # 判官中回到首页
time.sleep(2)
TouchAction(driver).tap(x=439, y=124).perform()  # 返回进入个人中心
time.sleep(2)
TouchAction(driver).tap(x=971, y=158).perform()  # 点击设置
time.sleep(2)
TouchAction(driver).tap(x=536, y=1770).perform()  # 点击退出
time.sleep(2)
TouchAction(driver).tap(x=690, y=1069).perform()  # 弹窗确定退出

#############################################################################################################################################################
mobile = "18321273743"
AA = "\033[1;31mNO.14\033[0m " + mobile + " \033[1;31m开始\033[0m"
print(AA)
time.sleep(5)


def check_login():
    try:
        check_login = driver.find_element_by_id(
            "com.kamitu.drawsth.standalone.free.android:id/iv_mobile_login")  # 选择手机号登录
    except NoSuchElementException:
        print("自动登录成功")
    else:
        TouchAction(driver).tap(x=409, y=1729).perform()  # 点击手机号登录
        time.sleep(2)
        edit_mobile = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/edit_phone")  # 选择手机号输入框
        edit_mobile.send_keys(mobile)
        time.sleep(2)
        TouchAction(driver).tap(x=776, y=615).perform()  # 获取验证码
        time.sleep(2)
        logincodeurl = "https://uc.crazyccy.com/login/main_login/testtool?key=sLQq2_jaKLknsqAwZ&type=1&mobile=" + mobile
        request = urllib.request.Request(logincodeurl)  # 构建请求url
        response = urllib.request.urlopen(request, context=context)  # ssl证书免验证加入,context = context# 打开请求url链接
        num = response.read()  # 读取页面返回信息，python3返回数据为bytes类型的对象 (即b为前缀, bytes类型)
        logincode = num.decode()
        if logincode == '查不到！':
            time.sleep(2)
            TouchAction(driver).tap(x=776, y=615).perform()  # 获取验证码
            time.sleep(2)  # 获取验证码
            request = urllib.request.Request(logincodeurl)  # 构建请求url
            response = urllib.request.urlopen(request, context=context)  # ssl证书免验证加入,context = context# 打开请求url链接
            num = response.read()  # 读取页面返回信息，python3返回数据为bytes类型的对象 (即b为前缀, bytes类型)
            logincode = num.decode()
        edit_Code = driver.find_element_by_id(
            "com.kamitu.drawsth.standalone.free.android:id/edit_identifyCode")  # 选择验证码输入框
        time.sleep(2)
        edit_Code.send_keys(logincode)
        time.sleep(2)
        TouchAction(driver).tap(x=529, y=833).perform()  # 确定按钮登录


check_login()
time.sleep(15)  # 等待15秒加载进入首页


def check_signwindows():  # 检查是否有每日签到弹窗

    try:
        check_signwindows = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/iv_signin_get")
    except NoSuchElementException:
        print("无签到弹窗")
    else:
        TouchAction(driver).tap(x=953, y=551).perform()  # 关闭签到弹窗
        time.sleep(3)


check_signwindows()
time.sleep(3)

TouchAction(driver).tap(x=525, y=1556).perform()  # 进入接龙页面
time.sleep(3)
driver.back()
time.sleep(3)


def check_signtoast():  # 检查是否开启签到提醒

    try:
        check_signtoast = driver.find_element_by_id(
            "com.kamitu.drawsth.standalone.free.android:id/btn_open_reminder")
    except NoSuchElementException:
        print("无签到提醒弹窗")
    else:
        TouchAction(driver).tap(x=870, y=611).perform()  # 关闭签到提示弹窗


check_signtoast()
time.sleep(3)

TouchAction(driver).tap(x=323, y=1774).perform()  # 选择进入判官
time.sleep(2)
TouchAction(driver).tap(x=536, y=1009).perform()  # 选择开始挑战
time.sleep(3)

a = 1
while a <= 10:
    time.sleep(8)
    TouchAction(driver).tap(x=503, y=1305).perform()  # 点击查看广告
    time.sleep(10)
    try:
        GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
    except NoSuchElementException:
        BB = "  \033[1;31m第\033[0m " + str(a) + " \033[1;31m次\033[0m " + "toutiaosdk广告"
        print(BB)
        time.sleep(40)
        TouchAction(driver).tap(x=979, y=86).perform()  # 关闭toutiao广告
        print("     toutiaosdk广告关闭")
    else:
        CC = "  \033[1;31m第\033[0m " + str(a) + " \033[1;31m次\033[0m " + "GDTsdk广告"
        print(CC)
        time.sleep(55)  # 保证完整看完GTD广告
        driver.back()  # GDTsdk广告关闭
        print("     GDTsdk广告关闭")
    a += 1

time.sleep(7)
driver.back()  # 判官中回到首页
time.sleep(2)
TouchAction(driver).tap(x=439, y=124).perform()  # 返回进入个人中心
time.sleep(2)
TouchAction(driver).tap(x=971, y=158).perform()  # 点击设置
time.sleep(2)
TouchAction(driver).tap(x=536, y=1770).perform()  # 点击退出
time.sleep(2)
TouchAction(driver).tap(x=690, y=1069).perform()  # 弹窗确定退出

#############################################################################################################################################################
mobile = "18819123459"
AA = "\033[1;31mNO.15\033[0m " + mobile + " \033[1;31m开始\033[0m"
print(AA)
time.sleep(5)


def check_login():
    try:
        check_login = driver.find_element_by_id(
            "com.kamitu.drawsth.standalone.free.android:id/iv_mobile_login")  # 选择手机号登录
    except NoSuchElementException:
        print("自动登录成功")
    else:
        TouchAction(driver).tap(x=409, y=1729).perform()  # 点击手机号登录
        time.sleep(2)
        edit_mobile = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/edit_phone")  # 选择手机号输入框
        edit_mobile.send_keys(mobile)
        time.sleep(2)
        TouchAction(driver).tap(x=776, y=615).perform()  # 获取验证码
        time.sleep(2)
        logincodeurl = "https://uc.crazyccy.com/login/main_login/testtool?key=sLQq2_jaKLknsqAwZ&type=1&mobile=" + mobile
        request = urllib.request.Request(logincodeurl)  # 构建请求url
        response = urllib.request.urlopen(request, context=context)  # ssl证书免验证加入,context = context# 打开请求url链接
        num = response.read()  # 读取页面返回信息，python3返回数据为bytes类型的对象 (即b为前缀, bytes类型)
        logincode = num.decode()
        if logincode == '查不到！':
            time.sleep(2)
            TouchAction(driver).tap(x=776, y=615).perform()  # 获取验证码
            time.sleep(2)  # 获取验证码
            request = urllib.request.Request(logincodeurl)  # 构建请求url
            response = urllib.request.urlopen(request, context=context)  # ssl证书免验证加入,context = context# 打开请求url链接
            num = response.read()  # 读取页面返回信息，python3返回数据为bytes类型的对象 (即b为前缀, bytes类型)
            logincode = num.decode()
        edit_Code = driver.find_element_by_id(
            "com.kamitu.drawsth.standalone.free.android:id/edit_identifyCode")  # 选择验证码输入框
        time.sleep(2)
        edit_Code.send_keys(logincode)
        time.sleep(2)
        TouchAction(driver).tap(x=529, y=833).perform()  # 确定按钮登录


check_login()
time.sleep(15)  # 等待15秒加载进入首页


def check_signwindows():  # 检查是否有每日签到弹窗

    try:
        check_signwindows = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/iv_signin_get")
    except NoSuchElementException:
        print("无签到弹窗")
    else:
        TouchAction(driver).tap(x=953, y=551).perform()  # 关闭签到弹窗
        time.sleep(3)


check_signwindows()
time.sleep(3)

TouchAction(driver).tap(x=525, y=1556).perform()  # 进入接龙页面
time.sleep(3)
driver.back()
time.sleep(3)


def check_signtoast():  # 检查是否开启签到提醒

    try:
        check_signtoast = driver.find_element_by_id(
            "com.kamitu.drawsth.standalone.free.android:id/btn_open_reminder")
    except NoSuchElementException:
        print("无签到提醒弹窗")
    else:
        TouchAction(driver).tap(x=870, y=611).perform()  # 关闭签到提示弹窗


check_signtoast()
time.sleep(3)

TouchAction(driver).tap(x=323, y=1774).perform()  # 选择进入判官
time.sleep(2)
TouchAction(driver).tap(x=536, y=1009).perform()  # 选择开始挑战
time.sleep(3)

a = 1
while a <= 10:
    time.sleep(8)
    TouchAction(driver).tap(x=503, y=1305).perform()  # 点击查看广告
    time.sleep(10)
    try:
        GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
    except NoSuchElementException:
        BB = "  \033[1;31m第\033[0m " + str(a) + " \033[1;31m次\033[0m " + "toutiaosdk广告"
        print(BB)
        time.sleep(40)
        TouchAction(driver).tap(x=979, y=86).perform()  # 关闭toutiao广告
        print("     toutiaosdk广告关闭")
    else:
        CC = "  \033[1;31m第\033[0m " + str(a) + " \033[1;31m次\033[0m " + "GDTsdk广告"
        print(CC)
        time.sleep(55)  # 保证完整看完GTD广告
        driver.back()  # GDTsdk广告关闭
        print("     GDTsdk广告关闭")
    a += 1

time.sleep(7)
driver.back()  # 判官中回到首页
time.sleep(2)
TouchAction(driver).tap(x=439, y=124).perform()  # 返回进入个人中心
time.sleep(2)
TouchAction(driver).tap(x=971, y=158).perform()  # 点击设置
time.sleep(2)
TouchAction(driver).tap(x=536, y=1770).perform()  # 点击退出
time.sleep(2)
TouchAction(driver).tap(x=690, y=1069).perform()  # 弹窗确定退出

#############################################################################################################################################################
mobile = "15917449818"
AA = "\033[1;31mNO.16\033[0m " + mobile + " \033[1;31m开始\033[0m"
print(AA)
time.sleep(5)


def check_login():
    try:
        check_login = driver.find_element_by_id(
            "com.kamitu.drawsth.standalone.free.android:id/iv_mobile_login")  # 选择手机号登录
    except NoSuchElementException:
        print("自动登录成功")
    else:
        TouchAction(driver).tap(x=409, y=1729).perform()  # 点击手机号登录
        time.sleep(2)
        edit_mobile = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/edit_phone")  # 选择手机号输入框
        edit_mobile.send_keys(mobile)
        time.sleep(2)
        TouchAction(driver).tap(x=776, y=615).perform()  # 获取验证码
        time.sleep(2)
        logincodeurl = "https://uc.crazyccy.com/login/main_login/testtool?key=sLQq2_jaKLknsqAwZ&type=1&mobile=" + mobile
        request = urllib.request.Request(logincodeurl)  # 构建请求url
        response = urllib.request.urlopen(request, context=context)  # ssl证书免验证加入,context = context# 打开请求url链接
        num = response.read()  # 读取页面返回信息，python3返回数据为bytes类型的对象 (即b为前缀, bytes类型)
        logincode = num.decode()
        if logincode == '查不到！':
            time.sleep(2)
            TouchAction(driver).tap(x=776, y=615).perform()  # 获取验证码
            time.sleep(2)  # 获取验证码
            request = urllib.request.Request(logincodeurl)  # 构建请求url
            response = urllib.request.urlopen(request, context=context)  # ssl证书免验证加入,context = context# 打开请求url链接
            num = response.read()  # 读取页面返回信息，python3返回数据为bytes类型的对象 (即b为前缀, bytes类型)
            logincode = num.decode()
        edit_Code = driver.find_element_by_id(
            "com.kamitu.drawsth.standalone.free.android:id/edit_identifyCode")  # 选择验证码输入框
        time.sleep(2)
        edit_Code.send_keys(logincode)
        time.sleep(2)
        TouchAction(driver).tap(x=529, y=833).perform()  # 确定按钮登录


check_login()
time.sleep(15)  # 等待15秒加载进入首页


def check_signwindows():  # 检查是否有每日签到弹窗

    try:
        check_signwindows = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/iv_signin_get")
    except NoSuchElementException:
        print("无签到弹窗")
    else:
        TouchAction(driver).tap(x=953, y=551).perform()  # 关闭签到弹窗
        time.sleep(3)


check_signwindows()
time.sleep(3)

TouchAction(driver).tap(x=525, y=1556).perform()  # 进入接龙页面
time.sleep(3)
driver.back()
time.sleep(3)


def check_signtoast():  # 检查是否开启签到提醒

    try:
        check_signtoast = driver.find_element_by_id(
            "com.kamitu.drawsth.standalone.free.android:id/btn_open_reminder")
    except NoSuchElementException:
        print("无签到提醒弹窗")
    else:
        TouchAction(driver).tap(x=870, y=611).perform()  # 关闭签到提示弹窗


check_signtoast()
time.sleep(3)

TouchAction(driver).tap(x=323, y=1774).perform()  # 选择进入判官
time.sleep(2)
TouchAction(driver).tap(x=536, y=1009).perform()  # 选择开始挑战
time.sleep(3)

a = 1
while a <= 10:
    time.sleep(8)
    TouchAction(driver).tap(x=503, y=1305).perform()  # 点击查看广告
    time.sleep(10)
    try:
        GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
    except NoSuchElementException:
        BB = "  \033[1;31m第\033[0m " + str(a) + " \033[1;31m次\033[0m " + "toutiaosdk广告"
        print(BB)
        time.sleep(40)
        TouchAction(driver).tap(x=979, y=86).perform()  # 关闭toutiao广告
        print("     toutiaosdk广告关闭")
    else:
        CC = "  \033[1;31m第\033[0m " + str(a) + " \033[1;31m次\033[0m " + "GDTsdk广告"
        print(CC)
        time.sleep(55)  # 保证完整看完GTD广告
        driver.back()  # GDTsdk广告关闭
        print("     GDTsdk广告关闭")
    a += 1

time.sleep(7)
driver.back()  # 判官中回到首页
time.sleep(2)
TouchAction(driver).tap(x=439, y=124).perform()  # 返回进入个人中心
time.sleep(2)
TouchAction(driver).tap(x=971, y=158).perform()  # 点击设置
time.sleep(2)
TouchAction(driver).tap(x=536, y=1770).perform()  # 点击退出
time.sleep(2)
TouchAction(driver).tap(x=690, y=1069).perform()  # 弹窗确定退出

#############################################################################################################################################################
mobile = "13032337111"
AA = "\033[1;31mNO.7\033[0m " + mobile + " \033[1;31m开始\033[0m"
print(AA)
time.sleep(5)


def check_login():
    try:
        check_login = driver.find_element_by_id(
            "com.kamitu.drawsth.standalone.free.android:id/iv_mobile_login")  # 选择手机号登录
    except NoSuchElementException:
        print("自动登录成功")
    else:
        TouchAction(driver).tap(x=409, y=1729).perform()  # 点击手机号登录
        time.sleep(2)
        edit_mobile = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/edit_phone")  # 选择手机号输入框
        edit_mobile.send_keys(mobile)
        time.sleep(2)
        TouchAction(driver).tap(x=776, y=615).perform()  # 获取验证码
        time.sleep(2)
        logincodeurl = "https://uc.crazyccy.com/login/main_login/testtool?key=sLQq2_jaKLknsqAwZ&type=1&mobile=" + mobile
        request = urllib.request.Request(logincodeurl)  # 构建请求url
        response = urllib.request.urlopen(request, context=context)  # ssl证书免验证加入,context = context# 打开请求url链接
        num = response.read()  # 读取页面返回信息，python3返回数据为bytes类型的对象 (即b为前缀, bytes类型)
        logincode = num.decode()
        if logincode == '查不到！':
            time.sleep(2)
            TouchAction(driver).tap(x=776, y=615).perform()  # 获取验证码
            time.sleep(2)  # 获取验证码
            request = urllib.request.Request(logincodeurl)  # 构建请求url
            response = urllib.request.urlopen(request, context=context)  # ssl证书免验证加入,context = context# 打开请求url链接
            num = response.read()  # 读取页面返回信息，python3返回数据为bytes类型的对象 (即b为前缀, bytes类型)
            logincode = num.decode()
        edit_Code = driver.find_element_by_id(
            "com.kamitu.drawsth.standalone.free.android:id/edit_identifyCode")  # 选择验证码输入框
        time.sleep(2)
        edit_Code.send_keys(logincode)
        time.sleep(2)
        TouchAction(driver).tap(x=529, y=833).perform()  # 确定按钮登录


check_login()
time.sleep(15)  # 等待15秒加载进入首页


def check_signwindows():  # 检查是否有每日签到弹窗

    try:
        check_signwindows = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/iv_signin_get")
    except NoSuchElementException:
        print("无签到弹窗")
    else:
        TouchAction(driver).tap(x=953, y=551).perform()  # 关闭签到弹窗
        time.sleep(3)


check_signwindows()
time.sleep(3)

TouchAction(driver).tap(x=525, y=1556).perform()  # 进入接龙页面
time.sleep(3)
driver.back()
time.sleep(3)


def check_signtoast():  # 检查是否开启签到提醒

    try:
        check_signtoast = driver.find_element_by_id(
            "com.kamitu.drawsth.standalone.free.android:id/btn_open_reminder")
    except NoSuchElementException:
        print("无签到提醒弹窗")
    else:
        TouchAction(driver).tap(x=870, y=611).perform()  # 关闭签到提示弹窗


check_signtoast()
time.sleep(3)

TouchAction(driver).tap(x=323, y=1774).perform()  # 选择进入判官
time.sleep(2)
TouchAction(driver).tap(x=536, y=1009).perform()  # 选择开始挑战
time.sleep(3)

a = 1
while a <= 10:
    time.sleep(8)
    TouchAction(driver).tap(x=503, y=1305).perform()  # 点击查看广告
    time.sleep(10)
    try:
        GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
    except NoSuchElementException:
        BB = "  \033[1;31m第\033[0m " + str(a) + " \033[1;31m次\033[0m " + "toutiaosdk广告"
        print(BB)
        time.sleep(40)
        TouchAction(driver).tap(x=979, y=86).perform()  # 关闭toutiao广告
        print("     toutiaosdk广告关闭")
    else:
        CC = "  \033[1;31m第\033[0m " + str(a) + " \033[1;31m次\033[0m " + "GDTsdk广告"
        print(CC)
        time.sleep(55)  # 保证完整看完GTD广告
        driver.back()  # GDTsdk广告关闭
        print("     GDTsdk广告关闭")
    a += 1

time.sleep(7)
driver.back()  # 判官中回到首页
time.sleep(2)
TouchAction(driver).tap(x=439, y=124).perform()  # 返回进入个人中心
time.sleep(2)
TouchAction(driver).tap(x=971, y=158).perform()  # 点击设置
time.sleep(2)
TouchAction(driver).tap(x=536, y=1770).perform()  # 点击退出
time.sleep(2)
TouchAction(driver).tap(x=690, y=1069).perform()  # 弹窗确定退出

#############################################################################################################################################################
mobile = "13168867678"
AA = "\033[1;31mNO.18\033[0m " + mobile + " \033[1;31m开始\033[0m"
print(AA)
time.sleep(5)


def check_login():
    try:
        check_login = driver.find_element_by_id(
            "com.kamitu.drawsth.standalone.free.android:id/iv_mobile_login")  # 选择手机号登录
    except NoSuchElementException:
        print("自动登录成功")
    else:
        TouchAction(driver).tap(x=409, y=1729).perform()  # 点击手机号登录
        time.sleep(2)
        edit_mobile = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/edit_phone")  # 选择手机号输入框
        edit_mobile.send_keys(mobile)
        time.sleep(2)
        TouchAction(driver).tap(x=776, y=615).perform()  # 获取验证码
        time.sleep(2)
        logincodeurl = "https://uc.crazyccy.com/login/main_login/testtool?key=sLQq2_jaKLknsqAwZ&type=1&mobile=" + mobile
        request = urllib.request.Request(logincodeurl)  # 构建请求url
        response = urllib.request.urlopen(request, context=context)  # ssl证书免验证加入,context = context# 打开请求url链接
        num = response.read()  # 读取页面返回信息，python3返回数据为bytes类型的对象 (即b为前缀, bytes类型)
        logincode = num.decode()
        if logincode == '查不到！':
            time.sleep(2)
            TouchAction(driver).tap(x=776, y=615).perform()  # 获取验证码
            time.sleep(2)  # 获取验证码
            request = urllib.request.Request(logincodeurl)  # 构建请求url
            response = urllib.request.urlopen(request, context=context)  # ssl证书免验证加入,context = context# 打开请求url链接
            num = response.read()  # 读取页面返回信息，python3返回数据为bytes类型的对象 (即b为前缀, bytes类型)
            logincode = num.decode()
        edit_Code = driver.find_element_by_id(
            "com.kamitu.drawsth.standalone.free.android:id/edit_identifyCode")  # 选择验证码输入框
        time.sleep(2)
        edit_Code.send_keys(logincode)
        time.sleep(2)
        TouchAction(driver).tap(x=529, y=833).perform()  # 确定按钮登录


check_login()
time.sleep(15)  # 等待15秒加载进入首页


def check_signwindows():  # 检查是否有每日签到弹窗

    try:
        check_signwindows = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/iv_signin_get")
    except NoSuchElementException:
        print("无签到弹窗")
    else:
        TouchAction(driver).tap(x=953, y=551).perform()  # 关闭签到弹窗
        time.sleep(3)


check_signwindows()
time.sleep(3)

TouchAction(driver).tap(x=525, y=1556).perform()  # 进入接龙页面
time.sleep(3)
driver.back()
time.sleep(3)


def check_signtoast():  # 检查是否开启签到提醒

    try:
        check_signtoast = driver.find_element_by_id(
            "com.kamitu.drawsth.standalone.free.android:id/btn_open_reminder")
    except NoSuchElementException:
        print("无签到提醒弹窗")
    else:
        TouchAction(driver).tap(x=870, y=611).perform()  # 关闭签到提示弹窗


check_signtoast()
time.sleep(3)

TouchAction(driver).tap(x=323, y=1774).perform()  # 选择进入判官
time.sleep(2)
TouchAction(driver).tap(x=536, y=1009).perform()  # 选择开始挑战
time.sleep(3)

a = 1
while a <= 10:
    time.sleep(8)
    TouchAction(driver).tap(x=503, y=1305).perform()  # 点击查看广告
    time.sleep(10)
    try:
        GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
    except NoSuchElementException:
        BB = "  \033[1;31m第\033[0m " + str(a) + " \033[1;31m次\033[0m " + "toutiaosdk广告"
        print(BB)
        time.sleep(40)
        TouchAction(driver).tap(x=979, y=86).perform()  # 关闭toutiao广告
        print("     toutiaosdk广告关闭")
    else:
        CC = "  \033[1;31m第\033[0m " + str(a) + " \033[1;31m次\033[0m " + "GDTsdk广告"
        print(CC)
        time.sleep(55)  # 保证完整看完GTD广告
        driver.back()  # GDTsdk广告关闭
        print("     GDTsdk广告关闭")
    a += 1

time.sleep(7)
driver.back()  # 判官中回到首页
time.sleep(2)
TouchAction(driver).tap(x=439, y=124).perform()  # 返回进入个人中心
time.sleep(2)
TouchAction(driver).tap(x=971, y=158).perform()  # 点击设置
time.sleep(2)
TouchAction(driver).tap(x=536, y=1770).perform()  # 点击退出
time.sleep(2)
TouchAction(driver).tap(x=690, y=1069).perform()  # 弹窗确定退出

#############################################################################################################################################################
mobile = "19823637887"
AA = "\033[1;31mNO.19\033[0m " + mobile + " \033[1;31m开始\033[0m"
print(AA)
time.sleep(5)


def check_login():
    try:
        check_login = driver.find_element_by_id(
            "com.kamitu.drawsth.standalone.free.android:id/iv_mobile_login")  # 选择手机号登录
    except NoSuchElementException:
        print("自动登录成功")
    else:
        TouchAction(driver).tap(x=409, y=1729).perform()  # 点击手机号登录
        time.sleep(2)
        edit_mobile = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/edit_phone")  # 选择手机号输入框
        edit_mobile.send_keys(mobile)
        time.sleep(2)
        TouchAction(driver).tap(x=776, y=615).perform()  # 获取验证码
        time.sleep(2)
        logincodeurl = "https://uc.crazyccy.com/login/main_login/testtool?key=sLQq2_jaKLknsqAwZ&type=1&mobile=" + mobile
        request = urllib.request.Request(logincodeurl)  # 构建请求url
        response = urllib.request.urlopen(request, context=context)  # ssl证书免验证加入,context = context# 打开请求url链接
        num = response.read()  # 读取页面返回信息，python3返回数据为bytes类型的对象 (即b为前缀, bytes类型)
        logincode = num.decode()
        if logincode == '查不到！':
            time.sleep(2)
            TouchAction(driver).tap(x=776, y=615).perform()  # 获取验证码
            time.sleep(2)  # 获取验证码
            request = urllib.request.Request(logincodeurl)  # 构建请求url
            response = urllib.request.urlopen(request, context=context)  # ssl证书免验证加入,context = context# 打开请求url链接
            num = response.read()  # 读取页面返回信息，python3返回数据为bytes类型的对象 (即b为前缀, bytes类型)
            logincode = num.decode()
        edit_Code = driver.find_element_by_id(
            "com.kamitu.drawsth.standalone.free.android:id/edit_identifyCode")  # 选择验证码输入框
        time.sleep(2)
        edit_Code.send_keys(logincode)
        time.sleep(2)
        TouchAction(driver).tap(x=529, y=833).perform()  # 确定按钮登录


check_login()
time.sleep(15)  # 等待15秒加载进入首页


def check_signwindows():  # 检查是否有每日签到弹窗

    try:
        check_signwindows = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/iv_signin_get")
    except NoSuchElementException:
        print("无签到弹窗")
    else:
        TouchAction(driver).tap(x=953, y=551).perform()  # 关闭签到弹窗
        time.sleep(3)


check_signwindows()
time.sleep(3)

TouchAction(driver).tap(x=525, y=1556).perform()  # 进入接龙页面
time.sleep(3)
driver.back()
time.sleep(3)


def check_signtoast():  # 检查是否开启签到提醒

    try:
        check_signtoast = driver.find_element_by_id(
            "com.kamitu.drawsth.standalone.free.android:id/btn_open_reminder")
    except NoSuchElementException:
        print("无签到提醒弹窗")
    else:
        TouchAction(driver).tap(x=870, y=611).perform()  # 关闭签到提示弹窗


check_signtoast()
time.sleep(3)

TouchAction(driver).tap(x=323, y=1774).perform()  # 选择进入判官
time.sleep(2)
TouchAction(driver).tap(x=536, y=1009).perform()  # 选择开始挑战
time.sleep(3)

a = 1
while a <= 10:
    time.sleep(8)
    TouchAction(driver).tap(x=503, y=1305).perform()  # 点击查看广告
    time.sleep(10)
    try:
        GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
    except NoSuchElementException:
        BB = "  \033[1;31m第\033[0m " + str(a) + " \033[1;31m次\033[0m " + "toutiaosdk广告"
        print(BB)
        time.sleep(40)
        TouchAction(driver).tap(x=979, y=86).perform()  # 关闭toutiao广告
        print("     toutiaosdk广告关闭")
    else:
        CC = "  \033[1;31m第\033[0m " + str(a) + " \033[1;31m次\033[0m " + "GDTsdk广告"
        print(CC)
        time.sleep(55)  # 保证完整看完GTD广告
        driver.back()  # GDTsdk广告关闭
        print("     GDTsdk广告关闭")
    a += 1

time.sleep(7)
driver.back()  # 判官中回到首页
time.sleep(2)
TouchAction(driver).tap(x=439, y=124).perform()  # 返回进入个人中心
time.sleep(2)
TouchAction(driver).tap(x=971, y=158).perform()  # 点击设置
time.sleep(2)
TouchAction(driver).tap(x=536, y=1770).perform()  # 点击退出
time.sleep(2)
TouchAction(driver).tap(x=690, y=1069).perform()  # 弹窗确定退出

#############################################################################################################################################################
mobile = "15981831553"
AA = "\033[1;31mNO.20\033[0m " + mobile + " \033[1;31m开始\033[0m"
print(AA)
time.sleep(5)


def check_login():
    try:
        check_login = driver.find_element_by_id(
            "com.kamitu.drawsth.standalone.free.android:id/iv_mobile_login")  # 选择手机号登录
    except NoSuchElementException:
        print("自动登录成功")
    else:
        TouchAction(driver).tap(x=409, y=1729).perform()  # 点击手机号登录
        time.sleep(2)
        edit_mobile = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/edit_phone")  # 选择手机号输入框
        edit_mobile.send_keys(mobile)
        time.sleep(2)
        TouchAction(driver).tap(x=776, y=615).perform()  # 获取验证码
        time.sleep(2)
        logincodeurl = "https://uc.crazyccy.com/login/main_login/testtool?key=sLQq2_jaKLknsqAwZ&type=1&mobile=" + mobile
        request = urllib.request.Request(logincodeurl)  # 构建请求url
        response = urllib.request.urlopen(request, context=context)  # ssl证书免验证加入,context = context# 打开请求url链接
        num = response.read()  # 读取页面返回信息，python3返回数据为bytes类型的对象 (即b为前缀, bytes类型)
        logincode = num.decode()
        if logincode == '查不到！':
            time.sleep(2)
            TouchAction(driver).tap(x=776, y=615).perform()  # 获取验证码
            time.sleep(2)  # 获取验证码
            request = urllib.request.Request(logincodeurl)  # 构建请求url
            response = urllib.request.urlopen(request, context=context)  # ssl证书免验证加入,context = context# 打开请求url链接
            num = response.read()  # 读取页面返回信息，python3返回数据为bytes类型的对象 (即b为前缀, bytes类型)
            logincode = num.decode()
        edit_Code = driver.find_element_by_id(
            "com.kamitu.drawsth.standalone.free.android:id/edit_identifyCode")  # 选择验证码输入框
        time.sleep(2)
        edit_Code.send_keys(logincode)
        time.sleep(2)
        TouchAction(driver).tap(x=529, y=833).perform()  # 确定按钮登录


check_login()
time.sleep(15)  # 等待15秒加载进入首页


def check_signwindows():  # 检查是否有每日签到弹窗

    try:
        check_signwindows = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/iv_signin_get")
    except NoSuchElementException:
        print("无签到弹窗")
    else:
        TouchAction(driver).tap(x=953, y=551).perform()  # 关闭签到弹窗
        time.sleep(3)


check_signwindows()
time.sleep(3)

TouchAction(driver).tap(x=525, y=1556).perform()  # 进入接龙页面
time.sleep(3)
driver.back()
time.sleep(3)


def check_signtoast():  # 检查是否开启签到提醒

    try:
        check_signtoast = driver.find_element_by_id(
            "com.kamitu.drawsth.standalone.free.android:id/btn_open_reminder")
    except NoSuchElementException:
        print("无签到提醒弹窗")
    else:
        TouchAction(driver).tap(x=870, y=611).perform()  # 关闭签到提示弹窗


check_signtoast()
time.sleep(3)

TouchAction(driver).tap(x=323, y=1774).perform()  # 选择进入判官
time.sleep(2)
TouchAction(driver).tap(x=536, y=1009).perform()  # 选择开始挑战
time.sleep(3)

a = 1
while a <= 10:
    time.sleep(8)
    TouchAction(driver).tap(x=503, y=1305).perform()  # 点击查看广告
    time.sleep(10)
    try:
        GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
    except NoSuchElementException:
        BB = "  \033[1;31m第\033[0m " + str(a) + " \033[1;31m次\033[0m " + "toutiaosdk广告"
        print(BB)
        time.sleep(40)
        TouchAction(driver).tap(x=979, y=86).perform()  # 关闭toutiao广告
        print("     toutiaosdk广告关闭")
    else:
        CC = "  \033[1;31m第\033[0m " + str(a) + " \033[1;31m次\033[0m " + "GDTsdk广告"
        print(CC)
        time.sleep(55)  # 保证完整看完GTD广告
        driver.back()  # GDTsdk广告关闭
        print("     GDTsdk广告关闭")
    a += 1

time.sleep(7)
driver.back()  # 判官中回到首页
time.sleep(2)
TouchAction(driver).tap(x=439, y=124).perform()  # 返回进入个人中心
time.sleep(2)
TouchAction(driver).tap(x=971, y=158).perform()  # 点击设置
time.sleep(2)
TouchAction(driver).tap(x=536, y=1770).perform()  # 点击退出
time.sleep(2)
TouchAction(driver).tap(x=690, y=1069).perform()  # 弹窗确定退出

#############################################################################################################################################################
mobile = "13666088700"
AA = "\033[1;31mNO.21\033[0m " + mobile + " \033[1;31m开始\033[0m"
print(AA)
time.sleep(5)


def check_login():
    try:
        check_login = driver.find_element_by_id(
            "com.kamitu.drawsth.standalone.free.android:id/iv_mobile_login")  # 选择手机号登录
    except NoSuchElementException:
        print("自动登录成功")
    else:
        TouchAction(driver).tap(x=409, y=1729).perform()  # 点击手机号登录
        time.sleep(2)
        edit_mobile = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/edit_phone")  # 选择手机号输入框
        edit_mobile.send_keys(mobile)
        time.sleep(2)
        TouchAction(driver).tap(x=776, y=615).perform()  # 获取验证码
        time.sleep(2)
        logincodeurl = "https://uc.crazyccy.com/login/main_login/testtool?key=sLQq2_jaKLknsqAwZ&type=1&mobile=" + mobile
        request = urllib.request.Request(logincodeurl)  # 构建请求url
        response = urllib.request.urlopen(request, context=context)  # ssl证书免验证加入,context = context# 打开请求url链接
        num = response.read()  # 读取页面返回信息，python3返回数据为bytes类型的对象 (即b为前缀, bytes类型)
        logincode = num.decode()
        if logincode == '查不到！':
            time.sleep(2)
            TouchAction(driver).tap(x=776, y=615).perform()  # 获取验证码
            time.sleep(2)  # 获取验证码
            request = urllib.request.Request(logincodeurl)  # 构建请求url
            response = urllib.request.urlopen(request, context=context)  # ssl证书免验证加入,context = context# 打开请求url链接
            num = response.read()  # 读取页面返回信息，python3返回数据为bytes类型的对象 (即b为前缀, bytes类型)
            logincode = num.decode()
        edit_Code = driver.find_element_by_id(
            "com.kamitu.drawsth.standalone.free.android:id/edit_identifyCode")  # 选择验证码输入框
        time.sleep(2)
        edit_Code.send_keys(logincode)
        time.sleep(2)
        TouchAction(driver).tap(x=529, y=833).perform()  # 确定按钮登录


check_login()
time.sleep(15)  # 等待15秒加载进入首页


def check_signwindows():  # 检查是否有每日签到弹窗

    try:
        check_signwindows = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/iv_signin_get")
    except NoSuchElementException:
        print("无签到弹窗")
    else:
        TouchAction(driver).tap(x=953, y=551).perform()  # 关闭签到弹窗
        time.sleep(3)


check_signwindows()
time.sleep(3)

TouchAction(driver).tap(x=525, y=1556).perform()  # 进入接龙页面
time.sleep(3)
driver.back()
time.sleep(3)


def check_signtoast():  # 检查是否开启签到提醒

    try:
        check_signtoast = driver.find_element_by_id(
            "com.kamitu.drawsth.standalone.free.android:id/btn_open_reminder")
    except NoSuchElementException:
        print("无签到提醒弹窗")
    else:
        TouchAction(driver).tap(x=870, y=611).perform()  # 关闭签到提示弹窗


check_signtoast()
time.sleep(3)

TouchAction(driver).tap(x=323, y=1774).perform()  # 选择进入判官
time.sleep(2)
TouchAction(driver).tap(x=536, y=1009).perform()  # 选择开始挑战
time.sleep(3)

a = 1
while a <= 10:
    time.sleep(8)
    TouchAction(driver).tap(x=503, y=1305).perform()  # 点击查看广告
    time.sleep(10)
    try:
        GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
    except NoSuchElementException:
        BB = "  \033[1;31m第\033[0m " + str(a) + " \033[1;31m次\033[0m " + "toutiaosdk广告"
        print(BB)
        time.sleep(40)
        TouchAction(driver).tap(x=979, y=86).perform()  # 关闭toutiao广告
        print("     toutiaosdk广告关闭")
    else:
        CC = "  \033[1;31m第\033[0m " + str(a) + " \033[1;31m次\033[0m " + "GDTsdk广告"
        print(CC)
        time.sleep(55)  # 保证完整看完GTD广告
        driver.back()  # GDTsdk广告关闭
        print("     GDTsdk广告关闭")
    a += 1

time.sleep(7)
driver.back()  # 判官中回到首页
time.sleep(2)
TouchAction(driver).tap(x=439, y=124).perform()  # 返回进入个人中心
time.sleep(2)
TouchAction(driver).tap(x=971, y=158).perform()  # 点击设置
time.sleep(2)
TouchAction(driver).tap(x=536, y=1770).perform()  # 点击退出
time.sleep(2)
TouchAction(driver).tap(x=690, y=1069).perform()  # 弹窗确定退出

#############################################################################################################################################################
mobile = "13560736789"
AA = "\033[1;31mNO.22\033[0m " + mobile + " \033[1;31m开始\033[0m"
print(AA)
time.sleep(5)


def check_login():
    try:
        check_login = driver.find_element_by_id(
            "com.kamitu.drawsth.standalone.free.android:id/iv_mobile_login")  # 选择手机号登录
    except NoSuchElementException:
        print("自动登录成功")
    else:
        TouchAction(driver).tap(x=409, y=1729).perform()  # 点击手机号登录
        time.sleep(2)
        edit_mobile = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/edit_phone")  # 选择手机号输入框
        edit_mobile.send_keys(mobile)
        time.sleep(2)
        TouchAction(driver).tap(x=776, y=615).perform()  # 获取验证码
        time.sleep(2)
        logincodeurl = "https://uc.crazyccy.com/login/main_login/testtool?key=sLQq2_jaKLknsqAwZ&type=1&mobile=" + mobile
        request = urllib.request.Request(logincodeurl)  # 构建请求url
        response = urllib.request.urlopen(request, context=context)  # ssl证书免验证加入,context = context# 打开请求url链接
        num = response.read()  # 读取页面返回信息，python3返回数据为bytes类型的对象 (即b为前缀, bytes类型)
        logincode = num.decode()
        if logincode == '查不到！':
            time.sleep(2)
            TouchAction(driver).tap(x=776, y=615).perform()  # 获取验证码
            time.sleep(2)  # 获取验证码
            request = urllib.request.Request(logincodeurl)  # 构建请求url
            response = urllib.request.urlopen(request, context=context)  # ssl证书免验证加入,context = context# 打开请求url链接
            num = response.read()  # 读取页面返回信息，python3返回数据为bytes类型的对象 (即b为前缀, bytes类型)
            logincode = num.decode()
        edit_Code = driver.find_element_by_id(
            "com.kamitu.drawsth.standalone.free.android:id/edit_identifyCode")  # 选择验证码输入框
        time.sleep(2)
        edit_Code.send_keys(logincode)
        time.sleep(2)
        TouchAction(driver).tap(x=529, y=833).perform()  # 确定按钮登录


check_login()
time.sleep(15)  # 等待15秒加载进入首页


def check_signwindows():  # 检查是否有每日签到弹窗

    try:
        check_signwindows = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/iv_signin_get")
    except NoSuchElementException:
        print("无签到弹窗")
    else:
        TouchAction(driver).tap(x=953, y=551).perform()  # 关闭签到弹窗
        time.sleep(3)


check_signwindows()
time.sleep(3)

TouchAction(driver).tap(x=525, y=1556).perform()  # 进入接龙页面
time.sleep(3)
driver.back()
time.sleep(3)


def check_signtoast():  # 检查是否开启签到提醒

    try:
        check_signtoast = driver.find_element_by_id(
            "com.kamitu.drawsth.standalone.free.android:id/btn_open_reminder")
    except NoSuchElementException:
        print("无签到提醒弹窗")
    else:
        TouchAction(driver).tap(x=870, y=611).perform()  # 关闭签到提示弹窗


check_signtoast()
time.sleep(3)

TouchAction(driver).tap(x=323, y=1774).perform()  # 选择进入判官
time.sleep(2)
TouchAction(driver).tap(x=536, y=1009).perform()  # 选择开始挑战
time.sleep(3)

a = 1
while a <= 10:
    time.sleep(8)
    TouchAction(driver).tap(x=503, y=1305).perform()  # 点击查看广告
    time.sleep(10)
    try:
        GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
    except NoSuchElementException:
        BB = "  \033[1;31m第\033[0m " + str(a) + " \033[1;31m次\033[0m " + "toutiaosdk广告"
        print(BB)
        time.sleep(40)
        TouchAction(driver).tap(x=979, y=86).perform()  # 关闭toutiao广告
        print("     toutiaosdk广告关闭")
    else:
        CC = "  \033[1;31m第\033[0m " + str(a) + " \033[1;31m次\033[0m " + "GDTsdk广告"
        print(CC)
        time.sleep(55)  # 保证完整看完GTD广告
        driver.back()  # GDTsdk广告关闭
        print("     GDTsdk广告关闭")
    a += 1

time.sleep(7)
driver.back()  # 判官中回到首页
time.sleep(2)
TouchAction(driver).tap(x=439, y=124).perform()  # 返回进入个人中心
time.sleep(2)
TouchAction(driver).tap(x=971, y=158).perform()  # 点击设置
time.sleep(2)
TouchAction(driver).tap(x=536, y=1770).perform()  # 点击退出
time.sleep(2)
TouchAction(driver).tap(x=690, y=1069).perform()  # 弹窗确定退出

#############################################################################################################################################################
mobile = "15611828881"
AA = "\033[1;31mNO.23\033[0m " + mobile + " \033[1;31m开始\033[0m"
print(AA)
time.sleep(5)


def check_login():
    try:
        check_login = driver.find_element_by_id(
            "com.kamitu.drawsth.standalone.free.android:id/iv_mobile_login")  # 选择手机号登录
    except NoSuchElementException:
        print("自动登录成功")
    else:
        TouchAction(driver).tap(x=409, y=1729).perform()  # 点击手机号登录
        time.sleep(2)
        edit_mobile = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/edit_phone")  # 选择手机号输入框
        edit_mobile.send_keys(mobile)
        time.sleep(2)
        TouchAction(driver).tap(x=776, y=615).perform()  # 获取验证码
        time.sleep(2)
        logincodeurl = "https://uc.crazyccy.com/login/main_login/testtool?key=sLQq2_jaKLknsqAwZ&type=1&mobile=" + mobile
        request = urllib.request.Request(logincodeurl)  # 构建请求url
        response = urllib.request.urlopen(request, context=context)  # ssl证书免验证加入,context = context# 打开请求url链接
        num = response.read()  # 读取页面返回信息，python3返回数据为bytes类型的对象 (即b为前缀, bytes类型)
        logincode = num.decode()
        if logincode == '查不到！':
            time.sleep(2)
            TouchAction(driver).tap(x=776, y=615).perform()  # 获取验证码
            time.sleep(2)  # 获取验证码
            request = urllib.request.Request(logincodeurl)  # 构建请求url
            response = urllib.request.urlopen(request, context=context)  # ssl证书免验证加入,context = context# 打开请求url链接
            num = response.read()  # 读取页面返回信息，python3返回数据为bytes类型的对象 (即b为前缀, bytes类型)
            logincode = num.decode()
        edit_Code = driver.find_element_by_id(
            "com.kamitu.drawsth.standalone.free.android:id/edit_identifyCode")  # 选择验证码输入框
        time.sleep(2)
        edit_Code.send_keys(logincode)
        time.sleep(2)
        TouchAction(driver).tap(x=529, y=833).perform()  # 确定按钮登录


check_login()
time.sleep(15)  # 等待15秒加载进入首页


def check_signwindows():  # 检查是否有每日签到弹窗

    try:
        check_signwindows = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/iv_signin_get")
    except NoSuchElementException:
        print("无签到弹窗")
    else:
        TouchAction(driver).tap(x=953, y=551).perform()  # 关闭签到弹窗
        time.sleep(3)


check_signwindows()
time.sleep(3)

TouchAction(driver).tap(x=525, y=1556).perform()  # 进入接龙页面
time.sleep(3)
driver.back()
time.sleep(3)


def check_signtoast():  # 检查是否开启签到提醒

    try:
        check_signtoast = driver.find_element_by_id(
            "com.kamitu.drawsth.standalone.free.android:id/btn_open_reminder")
    except NoSuchElementException:
        print("无签到提醒弹窗")
    else:
        TouchAction(driver).tap(x=870, y=611).perform()  # 关闭签到提示弹窗


check_signtoast()
time.sleep(3)

TouchAction(driver).tap(x=323, y=1774).perform()  # 选择进入判官
time.sleep(2)
TouchAction(driver).tap(x=536, y=1009).perform()  # 选择开始挑战
time.sleep(3)

a = 1
while a <= 10:
    time.sleep(8)
    TouchAction(driver).tap(x=503, y=1305).perform()  # 点击查看广告
    time.sleep(10)
    try:
        GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
    except NoSuchElementException:
        BB = "  \033[1;31m第\033[0m " + str(a) + " \033[1;31m次\033[0m " + "toutiaosdk广告"
        print(BB)
        time.sleep(40)
        TouchAction(driver).tap(x=979, y=86).perform()  # 关闭toutiao广告
        print("     toutiaosdk广告关闭")
    else:
        CC = "  \033[1;31m第\033[0m " + str(a) + " \033[1;31m次\033[0m " + "GDTsdk广告"
        print(CC)
        time.sleep(55)  # 保证完整看完GTD广告
        driver.back()  # GDTsdk广告关闭
        print("     GDTsdk广告关闭")
    a += 1

time.sleep(7)
driver.back()  # 判官中回到首页
time.sleep(2)
TouchAction(driver).tap(x=439, y=124).perform()  # 返回进入个人中心
time.sleep(2)
TouchAction(driver).tap(x=971, y=158).perform()  # 点击设置
time.sleep(2)
TouchAction(driver).tap(x=536, y=1770).perform()  # 点击退出
time.sleep(2)
TouchAction(driver).tap(x=690, y=1069).perform()  # 弹窗确定退出

#############################################################################################################################################################
mobile = "18918024483"
AA = "\033[1;31mNO.24\033[0m " + mobile + " \033[1;31m开始\033[0m"
print(AA)
time.sleep(5)


def check_login():
    try:
        check_login = driver.find_element_by_id(
            "com.kamitu.drawsth.standalone.free.android:id/iv_mobile_login")  # 选择手机号登录
    except NoSuchElementException:
        print("自动登录成功")
    else:
        TouchAction(driver).tap(x=409, y=1729).perform()  # 点击手机号登录
        time.sleep(2)
        edit_mobile = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/edit_phone")  # 选择手机号输入框
        edit_mobile.send_keys(mobile)
        time.sleep(2)
        TouchAction(driver).tap(x=776, y=615).perform()  # 获取验证码
        time.sleep(2)
        logincodeurl = "https://uc.crazyccy.com/login/main_login/testtool?key=sLQq2_jaKLknsqAwZ&type=1&mobile=" + mobile
        request = urllib.request.Request(logincodeurl)  # 构建请求url
        response = urllib.request.urlopen(request, context=context)  # ssl证书免验证加入,context = context# 打开请求url链接
        num = response.read()  # 读取页面返回信息，python3返回数据为bytes类型的对象 (即b为前缀, bytes类型)
        logincode = num.decode()
        if logincode == '查不到！':
            time.sleep(2)
            TouchAction(driver).tap(x=776, y=615).perform()  # 获取验证码
            time.sleep(2)  # 获取验证码
            request = urllib.request.Request(logincodeurl)  # 构建请求url
            response = urllib.request.urlopen(request, context=context)  # ssl证书免验证加入,context = context# 打开请求url链接
            num = response.read()  # 读取页面返回信息，python3返回数据为bytes类型的对象 (即b为前缀, bytes类型)
            logincode = num.decode()
        edit_Code = driver.find_element_by_id(
            "com.kamitu.drawsth.standalone.free.android:id/edit_identifyCode")  # 选择验证码输入框
        time.sleep(2)
        edit_Code.send_keys(logincode)
        time.sleep(2)
        TouchAction(driver).tap(x=529, y=833).perform()  # 确定按钮登录


check_login()
time.sleep(15)  # 等待15秒加载进入首页


def check_signwindows():  # 检查是否有每日签到弹窗

    try:
        check_signwindows = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/iv_signin_get")
    except NoSuchElementException:
        print("无签到弹窗")
    else:
        TouchAction(driver).tap(x=953, y=551).perform()  # 关闭签到弹窗
        time.sleep(3)


check_signwindows()
time.sleep(3)

TouchAction(driver).tap(x=525, y=1556).perform()  # 进入接龙页面
time.sleep(3)
driver.back()
time.sleep(3)


def check_signtoast():  # 检查是否开启签到提醒

    try:
        check_signtoast = driver.find_element_by_id(
            "com.kamitu.drawsth.standalone.free.android:id/btn_open_reminder")
    except NoSuchElementException:
        print("无签到提醒弹窗")
    else:
        TouchAction(driver).tap(x=870, y=611).perform()  # 关闭签到提示弹窗


check_signtoast()
time.sleep(3)

TouchAction(driver).tap(x=323, y=1774).perform()  # 选择进入判官
time.sleep(2)
TouchAction(driver).tap(x=536, y=1009).perform()  # 选择开始挑战
time.sleep(3)

a = 1
while a <= 10:
    time.sleep(8)
    TouchAction(driver).tap(x=503, y=1305).perform()  # 点击查看广告
    time.sleep(10)
    try:
        GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
    except NoSuchElementException:
        BB = "  \033[1;31m第\033[0m " + str(a) + " \033[1;31m次\033[0m " + "toutiaosdk广告"
        print(BB)
        time.sleep(40)
        TouchAction(driver).tap(x=979, y=86).perform()  # 关闭toutiao广告
        print("     toutiaosdk广告关闭")
    else:
        CC = "  \033[1;31m第\033[0m " + str(a) + " \033[1;31m次\033[0m " + "GDTsdk广告"
        print(CC)
        time.sleep(55)  # 保证完整看完GTD广告
        driver.back()  # GDTsdk广告关闭
        print("     GDTsdk广告关闭")
    a += 1

time.sleep(7)
driver.back()  # 判官中回到首页
time.sleep(2)
TouchAction(driver).tap(x=439, y=124).perform()  # 返回进入个人中心
time.sleep(2)
TouchAction(driver).tap(x=971, y=158).perform()  # 点击设置
time.sleep(2)
TouchAction(driver).tap(x=536, y=1770).perform()  # 点击退出
time.sleep(2)
TouchAction(driver).tap(x=690, y=1069).perform()  # 弹窗确定退出

#############################################################################################################################################################
nowtime2 = "\033[1;31m全部执行完毕：\033[0m " + time.strftime('%H:%M:%S')
print(nowtime2)
driver.back()
driver.back()

