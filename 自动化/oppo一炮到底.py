# coding=utf-8

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.common.exceptions import NoSuchElementException
import time
import urllib.request
import ssl

capabilities = {}
capabilities['platformName'] = 'Android'  # Android平台测试
capabilities['platformVersion'] = '8.1.0'
capabilities['deviceName'] = 'PBBM30'
capabilities['appPackage'] = 'com.kamitu.drawsth.standalone.free.android'  # 系统手机中的联系人app的包名
capabilities['appActivity'] = 'com.qsmy.busniess.welcome.WelcomeActivity'  # 系统手机中的联系人app的主入口activity
capabilities['noReset'] = 'true'  # 不重置app
capabilities['autoAcceptAlerts'] = 'true'
capabilities['autoWebview'] = 'false'
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', capabilities)  # 连接测试所在服务器
context = ssl._create_unverified_context()



#######################################################################################################################
mobile = "18017700401"
AA = "\033[1;31mNO.1\033[0m " + mobile + " \033[1;31m开始\033[0m"
nowtime = time.strftime('%H:%M:%S')
print(nowtime)
print(AA)
time.sleep(5)


def check_login():
    try:
        check_login = driver.find_element_by_id(
            "com.kamitu.drawsth.standalone.free.android:id/iv_mobile_login")  # 选择手机号登录
    except NoSuchElementException:
        print("自动登录成功")
    else:
        check_login.click()
        # TouchAction(driver).tap(x=255, y=1291).perform() # 点击手机号登录
        time.sleep(1)
        edit_mobile = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/edit_phone")  # 选择手机号输入框
        edit_mobile.send_keys(mobile)
        time.sleep(1)
        getcode = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/tv_get_identifyCode")
        getcode.click()
        # TouchAction(driver).tap(x=543, y=494).perform()  # 获取验证码
        time.sleep(2) # 获取验证码
        logincodeurl = "https://uc.crazyccy.com/login/main_login/testtool?key=sLQq2_jaKLknsqAwZ&type=1&mobile=" + mobile
        # print(logincodeurl)
        request = urllib.request.Request(logincodeurl)  # 构建请求url
        response = urllib.request.urlopen(request, context=context)  # ssl证书免验证加入,context = context# 打开请求url链接
        num = response.read()  # 读取页面返回信息，python3返回数据为bytes类型的对象 (即b为前缀, bytes类型)
        logincode = num.decode()
        edit_Code = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/edit_identifyCode")  # 选择验证码输入框
        time.sleep(1)
        edit_Code.send_keys(logincode)
        time.sleep(1)
        loginsure = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/btn_sure")
        loginsure.click()
        # TouchAction(driver).tap(x=353, y=660).perform()  # 确定按钮登录
        print("账号登录成功")


check_login()
time.sleep(15)  # 等待10秒加载进入首页


def check_signwindows():  # 检查用户签到弹窗

    try:
        check_signwindows = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/v_signin_close")
    except NoSuchElementException:
        print("无签到弹窗")
    else:
        check_signwindows.click()
        # TouchAction(driver).tap(x=630, y=400).perform() # 关闭签到弹窗
        time.sleep(3)


check_signwindows()
time.sleep(3)

TouchAction(driver).tap(x=345, y=1182).perform()  # 进入接龙页面
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
        check_signtoast.click()
        # TouchAction(driver).tap(x=611, y=456).perform() # 关闭签到提示弹窗


check_signtoast()
time.sleep(3)

TouchAction(driver).tap(x=212, y=1342).perform()  # 选择进入判官
time.sleep(1)
TouchAction(driver).tap(x=350, y=744).perform()  # 选择开始挑战
time.sleep(3)

a = 11
while a > 0:
    time.sleep(8)
    TouchAction(driver).tap(x=345, y=948).perform()  # 点击查看广告
    time.sleep(5)
    try:
        GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
    except NoSuchElementException:
        print("toutiaosdk广告")
        time.sleep(35)
        TouchAction(driver).tap(x=641, y=119).perform()  # 关闭toutiao广告
        print(a)
        print("toutiaosdk广告关闭")
    else:
        print("GDTsdk广告")
        time.sleep(50)
        driver.back()  # GDTsdk广告按钮
        print(a)
        print("GDTsdk广告关闭")
    a -= 1

time.sleep(7)
driver.back()  # 判官中回到首页
time.sleep(1)
TouchAction(driver).tap(x=290, y=85).perform()  # 返回进入个人中心
time.sleep(1)
# setbutton = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/iv_setting")
# setbutton.click()
TouchAction(driver).tap(x=638, y=122).perform()  # 点击设置
time.sleep(1)
# loginout = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/btn_login_exit")
# loginout.click()
TouchAction(driver).tap(x=354, y=1355).perform()  # 点击退出
time.sleep(1)
TouchAction(driver).tap(x=479, y=790).perform()  # 弹窗确定退出
# loginout_true = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/text_right")
# loginout_true.click()




#######################################################################################################################
mobile = "18017700403"
AA = "\033[1;31mNO.2\033[0m " + mobile + " \033[1;31m开始\033[0m"
nowtime = time.strftime('%H:%M:%S')
print(nowtime)
print(AA)
time.sleep(5)


def check_login():
    try:
        check_login = driver.find_element_by_id(
            "com.kamitu.drawsth.standalone.free.android:id/iv_mobile_login")  # 选择手机号登录
    except NoSuchElementException:
        print("自动登录成功")
    else:
        check_login.click()
        # TouchAction(driver).tap(x=255, y=1291).perform() # 点击手机号登录
        time.sleep(1)
        edit_mobile = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/edit_phone")  # 选择手机号输入框
        edit_mobile.send_keys(mobile)
        time.sleep(1)
        getcode = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/tv_get_identifyCode")
        getcode.click()
        # TouchAction(driver).tap(x=543, y=494).perform()  # 获取验证码
        time.sleep(2) # 获取验证码
        logincodeurl = "https://uc.crazyccy.com/login/main_login/testtool?key=sLQq2_jaKLknsqAwZ&type=1&mobile=" + mobile
        # print(logincodeurl)
        request = urllib.request.Request(logincodeurl)  # 构建请求url
        response = urllib.request.urlopen(request, context=context)  # ssl证书免验证加入,context = context# 打开请求url链接
        num = response.read()  # 读取页面返回信息，python3返回数据为bytes类型的对象 (即b为前缀, bytes类型)
        logincode = num.decode()
        edit_Code = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/edit_identifyCode")  # 选择验证码输入框
        time.sleep(1)
        edit_Code.send_keys(logincode)
        time.sleep(1)
        loginsure = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/btn_sure")
        loginsure.click()
        # TouchAction(driver).tap(x=353, y=660).perform()  # 确定按钮登录
        print("账号登录成功")


check_login()
time.sleep(15)  # 等待10秒加载进入首页


def check_signwindows():  # 检查用户签到弹窗

    try:
        check_signwindows = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/v_signin_close")
    except NoSuchElementException:
        print("无签到弹窗")
    else:
        check_signwindows.click()
        # TouchAction(driver).tap(x=630, y=400).perform() # 关闭签到弹窗
        time.sleep(3)


check_signwindows()
time.sleep(3)

TouchAction(driver).tap(x=345, y=1182).perform()  # 进入接龙页面
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
        check_signtoast.click()
        # TouchAction(driver).tap(x=611, y=456).perform() # 关闭签到提示弹窗


check_signtoast()
time.sleep(3)

TouchAction(driver).tap(x=212, y=1342).perform()  # 选择进入判官
time.sleep(1)
TouchAction(driver).tap(x=350, y=744).perform()  # 选择开始挑战
time.sleep(3)

a = 11
while a > 0:
    time.sleep(8)
    TouchAction(driver).tap(x=345, y=948).perform()  # 点击查看广告
    time.sleep(5)
    try:
        GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
    except NoSuchElementException:
        print("toutiaosdk广告")
        time.sleep(35)
        TouchAction(driver).tap(x=641, y=119).perform()  # 关闭toutiao广告
        print(a)
        print("toutiaosdk广告关闭")
    else:
        print("GDTsdk广告")
        time.sleep(50)
        driver.back()  # GDTsdk广告按钮
        print(a)
        print("GDTsdk广告关闭")
    a -= 1

time.sleep(7)
driver.back()  # 判官中回到首页
time.sleep(1)
TouchAction(driver).tap(x=290, y=85).perform()  # 返回进入个人中心
time.sleep(1)
# setbutton = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/iv_setting")
# setbutton.click()
TouchAction(driver).tap(x=638, y=122).perform() # 点击设置
time.sleep(1)
# loginout = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/btn_login_exit")
# loginout.click()
TouchAction(driver).tap(x=354, y=1355).perform() # 点击退出
time.sleep(1)
TouchAction(driver).tap(x=479, y=790).perform() # 弹窗确定退出
# loginout_true = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/text_right")
# loginout_true.click()





#######################################################################################################################
mobile = "18017700339"
AA = "\033[1;31mNO.3\033[0m " + mobile + " \033[1;31m开始\033[0m"
nowtime = time.strftime('%H:%M:%S')
print(nowtime)
print(AA)
time.sleep(5)


def check_login():
    try:
        check_login = driver.find_element_by_id(
            "com.kamitu.drawsth.standalone.free.android:id/iv_mobile_login")  # 选择手机号登录
    except NoSuchElementException:
        print("自动登录成功")
    else:
        check_login.click()
        # TouchAction(driver).tap(x=255, y=1291).perform() # 点击手机号登录
        time.sleep(1)
        edit_mobile = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/edit_phone")  # 选择手机号输入框
        edit_mobile.send_keys(mobile)
        time.sleep(1)
        getcode = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/tv_get_identifyCode")
        getcode.click()
        # TouchAction(driver).tap(x=543, y=494).perform()  # 获取验证码
        time.sleep(2) # 获取验证码
        logincodeurl = "https://uc.crazyccy.com/login/main_login/testtool?key=sLQq2_jaKLknsqAwZ&type=1&mobile=" + mobile
        # print(logincodeurl)
        request = urllib.request.Request(logincodeurl)  # 构建请求url
        response = urllib.request.urlopen(request, context=context)  # ssl证书免验证加入,context = context# 打开请求url链接
        num = response.read()  # 读取页面返回信息，python3返回数据为bytes类型的对象 (即b为前缀, bytes类型)
        logincode = num.decode()
        edit_Code = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/edit_identifyCode")  # 选择验证码输入框
        time.sleep(1)
        edit_Code.send_keys(logincode)
        time.sleep(1)
        loginsure = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/btn_sure")
        loginsure.click()
        # TouchAction(driver).tap(x=353, y=660).perform()  # 确定按钮登录
        print("账号登录成功")


check_login()
time.sleep(15)  # 等待10秒加载进入首页


def check_signwindows():  # 检查用户签到弹窗

    try:
        check_signwindows = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/v_signin_close")
    except NoSuchElementException:
        print("无签到弹窗")
    else:
        check_signwindows.click()
        # TouchAction(driver).tap(x=630, y=400).perform() # 关闭签到弹窗
        time.sleep(3)


check_signwindows()
time.sleep(3)

TouchAction(driver).tap(x=345, y=1182).perform()  # 进入接龙页面
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
        check_signtoast.click()
        # TouchAction(driver).tap(x=611, y=456).perform() # 关闭签到提示弹窗


check_signtoast()
time.sleep(3)

TouchAction(driver).tap(x=212, y=1342).perform()  # 选择进入判官
time.sleep(1)
TouchAction(driver).tap(x=350, y=744).perform()  # 选择开始挑战
time.sleep(3)

a = 11
while a > 0:
    time.sleep(8)
    TouchAction(driver).tap(x=345, y=948).perform()  # 点击查看广告
    time.sleep(5)
    try:
        GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
    except NoSuchElementException:
        print("toutiaosdk广告")
        time.sleep(35)
        TouchAction(driver).tap(x=641, y=119).perform()  # 关闭toutiao广告
        print(a)
        print("toutiaosdk广告关闭")
    else:
        print("GDTsdk广告")
        time.sleep(50)
        driver.back()  # GDTsdk广告按钮
        print(a)
        print("GDTsdk广告关闭")
    a -= 1

time.sleep(7)
driver.back()  # 判官中回到首页
time.sleep(1)
TouchAction(driver).tap(x=290, y=85).perform()  # 返回进入个人中心
time.sleep(1)
# setbutton = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/iv_setting")
# setbutton.click()
TouchAction(driver).tap(x=638, y=122).perform() # 点击设置
time.sleep(1)
# loginout = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/btn_login_exit")
# loginout.click()
TouchAction(driver).tap(x=354, y=1355).perform() # 点击退出
time.sleep(1)
TouchAction(driver).tap(x=479, y=790).perform() # 弹窗确定退出
# loginout_true = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/text_right")
# loginout_true.click()





#######################################################################################################################
mobile = "18017700413"
AA = "\033[1;31mNO.4\033[0m " + mobile + " \033[1;31m开始\033[0m"
nowtime = time.strftime('%H:%M:%S')
print(nowtime)
print(AA)
time.sleep(5)


def check_login():
    try:
        check_login = driver.find_element_by_id(
            "com.kamitu.drawsth.standalone.free.android:id/iv_mobile_login")  # 选择手机号登录
    except NoSuchElementException:
        print("自动登录成功")
    else:
        check_login.click()
        # TouchAction(driver).tap(x=255, y=1291).perform() # 点击手机号登录
        time.sleep(1)
        edit_mobile = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/edit_phone")  # 选择手机号输入框
        edit_mobile.send_keys(mobile)
        time.sleep(1)
        getcode = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/tv_get_identifyCode")
        getcode.click()
        # TouchAction(driver).tap(x=543, y=494).perform()  # 获取验证码
        time.sleep(2) # 获取验证码
        logincodeurl = "https://uc.crazyccy.com/login/main_login/testtool?key=sLQq2_jaKLknsqAwZ&type=1&mobile=" + mobile
        # print(logincodeurl)
        request = urllib.request.Request(logincodeurl)  # 构建请求url
        response = urllib.request.urlopen(request, context=context)  # ssl证书免验证加入,context = context# 打开请求url链接
        num = response.read()  # 读取页面返回信息，python3返回数据为bytes类型的对象 (即b为前缀, bytes类型)
        logincode = num.decode()
        edit_Code = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/edit_identifyCode")  # 选择验证码输入框
        time.sleep(1)
        edit_Code.send_keys(logincode)
        time.sleep(1)
        loginsure = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/btn_sure")
        loginsure.click()
        # TouchAction(driver).tap(x=353, y=660).perform()  # 确定按钮登录
        print("账号登录成功")


check_login()
time.sleep(15)  # 等待10秒加载进入首页


def check_signwindows():  # 检查用户签到弹窗

    try:
        check_signwindows = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/v_signin_close")
    except NoSuchElementException:
        print("无签到弹窗")
    else:
        check_signwindows.click()
        # TouchAction(driver).tap(x=630, y=400).perform() # 关闭签到弹窗
        time.sleep(3)


check_signwindows()
time.sleep(3)

TouchAction(driver).tap(x=345, y=1182).perform()  # 进入接龙页面
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
        check_signtoast.click()
        # TouchAction(driver).tap(x=611, y=456).perform() # 关闭签到提示弹窗


check_signtoast()
time.sleep(3)

TouchAction(driver).tap(x=212, y=1342).perform()  # 选择进入判官
time.sleep(1)
TouchAction(driver).tap(x=350, y=744).perform()  # 选择开始挑战
time.sleep(3)

a = 11
while a > 0:
    time.sleep(8)
    TouchAction(driver).tap(x=345, y=948).perform()  # 点击查看广告
    time.sleep(5)
    try:
        GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
    except NoSuchElementException:
        print("toutiaosdk广告")
        time.sleep(35)
        TouchAction(driver).tap(x=641, y=119).perform()  # 关闭toutiao广告
        print(a)
        print("toutiaosdk广告关闭")
    else:
        print("GDTsdk广告")
        time.sleep(50)
        driver.back()  # GDTsdk广告按钮
        print(a)
        print("GDTsdk广告关闭")
    a -= 1

time.sleep(7)
driver.back()  # 判官中回到首页
time.sleep(1)
TouchAction(driver).tap(x=290, y=85).perform()  # 返回进入个人中心
time.sleep(1)
# setbutton = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/iv_setting")
# setbutton.click()
TouchAction(driver).tap(x=638, y=122).perform() # 点击设置
time.sleep(1)
# loginout = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/btn_login_exit")
# loginout.click()
TouchAction(driver).tap(x=354, y=1355).perform() # 点击退出
time.sleep(1)
TouchAction(driver).tap(x=479, y=790).perform() # 弹窗确定退出
# loginout_true = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/text_right")
# loginout_true.click()





#######################################################################################################################
mobile = "18017700414"
AA = "\033[1;31mNO.5\033[0m " + mobile + " \033[1;31m开始\033[0m"
nowtime = time.strftime('%H:%M:%S')
print(nowtime)
print(AA)
time.sleep(5)


def check_login():
    try:
        check_login = driver.find_element_by_id(
            "com.kamitu.drawsth.standalone.free.android:id/iv_mobile_login")  # 选择手机号登录
    except NoSuchElementException:
        print("自动登录成功")
    else:
        check_login.click()
        # TouchAction(driver).tap(x=255, y=1291).perform() # 点击手机号登录
        time.sleep(1)
        edit_mobile = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/edit_phone")  # 选择手机号输入框
        edit_mobile.send_keys(mobile)
        time.sleep(1)
        getcode = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/tv_get_identifyCode")
        getcode.click()
        # TouchAction(driver).tap(x=543, y=494).perform()  # 获取验证码
        time.sleep(2) # 获取验证码
        logincodeurl = "https://uc.crazyccy.com/login/main_login/testtool?key=sLQq2_jaKLknsqAwZ&type=1&mobile=" + mobile
        # print(logincodeurl)
        request = urllib.request.Request(logincodeurl)  # 构建请求url
        response = urllib.request.urlopen(request, context=context)  # ssl证书免验证加入,context = context# 打开请求url链接
        num = response.read()  # 读取页面返回信息，python3返回数据为bytes类型的对象 (即b为前缀, bytes类型)
        logincode = num.decode()
        edit_Code = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/edit_identifyCode")  # 选择验证码输入框
        time.sleep(1)
        edit_Code.send_keys(logincode)
        time.sleep(1)
        loginsure = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/btn_sure")
        loginsure.click()
        # TouchAction(driver).tap(x=353, y=660).perform()  # 确定按钮登录
        print("账号登录成功")


check_login()
time.sleep(15)  # 等待10秒加载进入首页


def check_signwindows():  # 检查用户签到弹窗

    try:
        check_signwindows = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/v_signin_close")
    except NoSuchElementException:
        print("无签到弹窗")
    else:
        check_signwindows.click()
        # TouchAction(driver).tap(x=630, y=400).perform() # 关闭签到弹窗
        time.sleep(3)


check_signwindows()
time.sleep(3)

TouchAction(driver).tap(x=345, y=1182).perform()  # 进入接龙页面
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
        check_signtoast.click()
        # TouchAction(driver).tap(x=611, y=456).perform() # 关闭签到提示弹窗


check_signtoast()
time.sleep(3)

TouchAction(driver).tap(x=212, y=1342).perform()  # 选择进入判官
time.sleep(1)
TouchAction(driver).tap(x=350, y=744).perform()  # 选择开始挑战
time.sleep(3)

a = 11
while a > 0:
    time.sleep(8)
    TouchAction(driver).tap(x=345, y=948).perform()  # 点击查看广告
    time.sleep(5)
    try:
        GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
    except NoSuchElementException:
        print("toutiaosdk广告")
        time.sleep(35)
        TouchAction(driver).tap(x=641, y=119).perform()  # 关闭toutiao广告
        print(a)
        print("toutiaosdk广告关闭")
    else:
        print("GDTsdk广告")
        time.sleep(50)
        driver.back()  # GDTsdk广告按钮
        print(a)
        print("GDTsdk广告关闭")
    a -= 1

time.sleep(7)
driver.back()  # 判官中回到首页
time.sleep(1)
TouchAction(driver).tap(x=290, y=85).perform()  # 返回进入个人中心
time.sleep(1)
# setbutton = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/iv_setting")
# setbutton.click()
TouchAction(driver).tap(x=638, y=122).perform() # 点击设置
time.sleep(1)
# loginout = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/btn_login_exit")
# loginout.click()
TouchAction(driver).tap(x=354, y=1355).perform() # 点击退出
time.sleep(1)
TouchAction(driver).tap(x=479, y=790).perform() # 弹窗确定退出
# loginout_true = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/text_right")
# loginout_true.click()








#######################################################################################################################
mobile = "18017700521"
AA = "\033[1;31mNO.6\033[0m " + mobile + " \033[1;31m开始\033[0m"
nowtime = time.strftime('%H:%M:%S')
print(nowtime)
print(AA)
time.sleep(5)


def check_login():
    try:
        check_login = driver.find_element_by_id(
            "com.kamitu.drawsth.standalone.free.android:id/iv_mobile_login")  # 选择手机号登录
    except NoSuchElementException:
        print("自动登录成功")
    else:
        check_login.click()
        # TouchAction(driver).tap(x=255, y=1291).perform() # 点击手机号登录
        time.sleep(1)
        edit_mobile = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/edit_phone")  # 选择手机号输入框
        edit_mobile.send_keys(mobile)
        time.sleep(1)
        getcode = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/tv_get_identifyCode")
        getcode.click()
        # TouchAction(driver).tap(x=543, y=494).perform()  # 获取验证码
        time.sleep(2) # 获取验证码
        logincodeurl = "https://uc.crazyccy.com/login/main_login/testtool?key=sLQq2_jaKLknsqAwZ&type=1&mobile=" + mobile
        # print(logincodeurl)
        request = urllib.request.Request(logincodeurl)  # 构建请求url
        response = urllib.request.urlopen(request, context=context)  # ssl证书免验证加入,context = context# 打开请求url链接
        num = response.read()  # 读取页面返回信息，python3返回数据为bytes类型的对象 (即b为前缀, bytes类型)
        logincode = num.decode()
        edit_Code = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/edit_identifyCode")  # 选择验证码输入框
        time.sleep(1)
        edit_Code.send_keys(logincode)
        time.sleep(1)
        loginsure = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/btn_sure")
        loginsure.click()
        # TouchAction(driver).tap(x=353, y=660).perform()  # 确定按钮登录
        print("账号登录成功")


check_login()
time.sleep(15)  # 等待10秒加载进入首页


def check_signwindows():  # 检查用户签到弹窗

    try:
        check_signwindows = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/v_signin_close")
    except NoSuchElementException:
        print("无签到弹窗")
    else:
        check_signwindows.click()
        # TouchAction(driver).tap(x=630, y=400).perform() # 关闭签到弹窗
        time.sleep(3)


check_signwindows()
time.sleep(3)

TouchAction(driver).tap(x=345, y=1182).perform()  # 进入接龙页面
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
        check_signtoast.click()
        # TouchAction(driver).tap(x=611, y=456).perform() # 关闭签到提示弹窗


check_signtoast()
time.sleep(3)

TouchAction(driver).tap(x=212, y=1342).perform()  # 选择进入判官
time.sleep(1)
TouchAction(driver).tap(x=350, y=744).perform()  # 选择开始挑战
time.sleep(3)

a = 11
while a > 0:
    time.sleep(8)
    TouchAction(driver).tap(x=345, y=948).perform()  # 点击查看广告
    time.sleep(5)
    try:
        GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
    except NoSuchElementException:
        print("toutiaosdk广告")
        time.sleep(35)
        TouchAction(driver).tap(x=641, y=119).perform()  # 关闭toutiao广告
        print(a)
        print("toutiaosdk广告关闭")
    else:
        print("GDTsdk广告")
        time.sleep(50)
        driver.back()  # GDTsdk广告按钮
        print(a)
        print("GDTsdk广告关闭")
    a -= 1

time.sleep(7)
driver.back()  # 判官中回到首页
time.sleep(1)
TouchAction(driver).tap(x=290, y=85).perform()  # 返回进入个人中心
time.sleep(1)
# setbutton = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/iv_setting")
# setbutton.click()
TouchAction(driver).tap(x=638, y=122).perform() # 点击设置
time.sleep(1)
# loginout = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/btn_login_exit")
# loginout.click()
TouchAction(driver).tap(x=354, y=1355).perform() # 点击退出
time.sleep(1)
TouchAction(driver).tap(x=479, y=790).perform() # 弹窗确定退出
# loginout_true = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/text_right")
# loginout_true.click()










#######################################################################################################################
mobile = "18017700715"
AA = "\033[1;31mNO.7\033[0m " + mobile + " \033[1;31m开始\033[0m"
nowtime = time.strftime('%H:%M:%S')
print(nowtime)
print(AA)
time.sleep(5)


def check_login():
    try:
        check_login = driver.find_element_by_id(
            "com.kamitu.drawsth.standalone.free.android:id/iv_mobile_login")  # 选择手机号登录
    except NoSuchElementException:
        print("自动登录成功")
    else:
        check_login.click()
        # TouchAction(driver).tap(x=255, y=1291).perform() # 点击手机号登录
        time.sleep(1)
        edit_mobile = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/edit_phone")  # 选择手机号输入框
        edit_mobile.send_keys(mobile)
        time.sleep(1)
        getcode = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/tv_get_identifyCode")
        getcode.click()
        # TouchAction(driver).tap(x=543, y=494).perform()  # 获取验证码
        time.sleep(2) # 获取验证码
        logincodeurl = "https://uc.crazyccy.com/login/main_login/testtool?key=sLQq2_jaKLknsqAwZ&type=1&mobile=" + mobile
        # print(logincodeurl)
        request = urllib.request.Request(logincodeurl)  # 构建请求url
        response = urllib.request.urlopen(request, context=context)  # ssl证书免验证加入,context = context# 打开请求url链接
        num = response.read()  # 读取页面返回信息，python3返回数据为bytes类型的对象 (即b为前缀, bytes类型)
        logincode = num.decode()
        edit_Code = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/edit_identifyCode")  # 选择验证码输入框
        time.sleep(1)
        edit_Code.send_keys(logincode)
        time.sleep(1)
        loginsure = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/btn_sure")
        loginsure.click()
        # TouchAction(driver).tap(x=353, y=660).perform()  # 确定按钮登录
        print("账号登录成功")


check_login()
time.sleep(15)  # 等待10秒加载进入首页


def check_signwindows():  # 检查用户签到弹窗

    try:
        check_signwindows = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/v_signin_close")
    except NoSuchElementException:
        print("无签到弹窗")
    else:
        check_signwindows.click()
        # TouchAction(driver).tap(x=630, y=400).perform() # 关闭签到弹窗
        time.sleep(3)


check_signwindows()
time.sleep(3)

TouchAction(driver).tap(x=345, y=1182).perform()  # 进入接龙页面
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
        check_signtoast.click()
        # TouchAction(driver).tap(x=611, y=456).perform() # 关闭签到提示弹窗


check_signtoast()
time.sleep(3)

TouchAction(driver).tap(x=212, y=1342).perform()  # 选择进入判官
time.sleep(1)
TouchAction(driver).tap(x=350, y=744).perform()  # 选择开始挑战
time.sleep(3)

a = 11
while a > 0:
    time.sleep(8)
    TouchAction(driver).tap(x=345, y=948).perform()  # 点击查看广告
    time.sleep(5)
    try:
        GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
    except NoSuchElementException:
        print("toutiaosdk广告")
        time.sleep(35)
        TouchAction(driver).tap(x=641, y=119).perform()  # 关闭toutiao广告
        print(a)
        print("toutiaosdk广告关闭")
    else:
        print("GDTsdk广告")
        time.sleep(50)
        driver.back()  # GDTsdk广告按钮
        print(a)
        print("GDTsdk广告关闭")
    a -= 1

time.sleep(7)
driver.back()  # 判官中回到首页
time.sleep(1)
TouchAction(driver).tap(x=290, y=85).perform()  # 返回进入个人中心
time.sleep(1)
# setbutton = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/iv_setting")
# setbutton.click()
TouchAction(driver).tap(x=638, y=122).perform() # 点击设置
time.sleep(1)
# loginout = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/btn_login_exit")
# loginout.click()
TouchAction(driver).tap(x=354, y=1355).perform() # 点击退出
time.sleep(1)
TouchAction(driver).tap(x=479, y=790).perform() # 弹窗确定退出
# loginout_true = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/text_right")
# loginout_true.click()










#######################################################################################################################
mobile = "18220860324"
AA = "\033[1;31mNO.8\033[0m " + mobile + " \033[1;31m开始\033[0m"
nowtime = time.strftime('%H:%M:%S')
print(nowtime)
print(AA)
time.sleep(5)


def check_login():
    try:
        check_login = driver.find_element_by_id(
            "com.kamitu.drawsth.standalone.free.android:id/iv_mobile_login")  # 选择手机号登录
    except NoSuchElementException:
        print("自动登录成功")
    else:
        check_login.click()
        # TouchAction(driver).tap(x=255, y=1291).perform() # 点击手机号登录
        time.sleep(1)
        edit_mobile = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/edit_phone")  # 选择手机号输入框
        edit_mobile.send_keys(mobile)
        time.sleep(1)
        getcode = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/tv_get_identifyCode")
        getcode.click()
        # TouchAction(driver).tap(x=543, y=494).perform()  # 获取验证码
        time.sleep(2) # 获取验证码
        logincodeurl = "https://uc.crazyccy.com/login/main_login/testtool?key=sLQq2_jaKLknsqAwZ&type=1&mobile=" + mobile
        # print(logincodeurl)
        request = urllib.request.Request(logincodeurl)  # 构建请求url
        response = urllib.request.urlopen(request, context=context)  # ssl证书免验证加入,context = context# 打开请求url链接
        num = response.read()  # 读取页面返回信息，python3返回数据为bytes类型的对象 (即b为前缀, bytes类型)
        logincode = num.decode()
        edit_Code = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/edit_identifyCode")  # 选择验证码输入框
        time.sleep(1)
        edit_Code.send_keys(logincode)
        time.sleep(1)
        loginsure = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/btn_sure")
        loginsure.click()
        # TouchAction(driver).tap(x=353, y=660).perform()  # 确定按钮登录
        print("账号登录成功")


check_login()
time.sleep(15)  # 等待10秒加载进入首页


def check_signwindows():  # 检查用户签到弹窗

    try:
        check_signwindows = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/v_signin_close")
    except NoSuchElementException:
        print("无签到弹窗")
    else:
        check_signwindows.click()
        # TouchAction(driver).tap(x=630, y=400).perform() # 关闭签到弹窗
        time.sleep(3)


check_signwindows()
time.sleep(3)

TouchAction(driver).tap(x=345, y=1182).perform()  # 进入接龙页面
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
        check_signtoast.click()
        # TouchAction(driver).tap(x=611, y=456).perform() # 关闭签到提示弹窗


check_signtoast()
time.sleep(3)

TouchAction(driver).tap(x=212, y=1342).perform()  # 选择进入判官
time.sleep(1)
TouchAction(driver).tap(x=350, y=744).perform()  # 选择开始挑战
time.sleep(3)

a = 11
while a > 0:
    time.sleep(8)
    TouchAction(driver).tap(x=345, y=948).perform()  # 点击查看广告
    time.sleep(5)
    try:
        GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
    except NoSuchElementException:
        print("toutiaosdk广告")
        time.sleep(35)
        TouchAction(driver).tap(x=641, y=119).perform()  # 关闭toutiao广告
        print(a)
        print("toutiaosdk广告关闭")
    else:
        print("GDTsdk广告")
        time.sleep(50)
        driver.back()  # GDTsdk广告按钮
        print(a)
        print("GDTsdk广告关闭")
    a -= 1

time.sleep(7)
driver.back()  # 判官中回到首页
time.sleep(1)
TouchAction(driver).tap(x=290, y=85).perform()  # 返回进入个人中心
time.sleep(1)
# setbutton = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/iv_setting")
# setbutton.click()
TouchAction(driver).tap(x=638, y=122).perform() # 点击设置
time.sleep(1)
# loginout = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/btn_login_exit")
# loginout.click()
TouchAction(driver).tap(x=354, y=1355).perform() # 点击退出
time.sleep(1)
TouchAction(driver).tap(x=479, y=790).perform() # 弹窗确定退出
# loginout_true = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/text_right")
# loginout_true.click()





#######################################################################################################################
nowtime = time.strftime('%H:%M:%S')
print(nowtime)