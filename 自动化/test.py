# # coding=utf-8
import requests
import json
import time
import response

# for i in range(5):
#     print(i)
# else:
#     print("第", i, "次")
#######################################################################################

# Python 函数允许同时全部或部分使用固定参数、默认参数、单值（一颗星）可变参数、键值对（两颗星）可变参数，使用时必须按照前述顺序书写
# def do_something(name, age, gender='男', *args, **kwds):
#     print('姓名：%s，年龄：%d，性别：%s'%(name, age, gender))
#     print(args)
#     print(kwds)
#
# do_something('xufive', 50, '男', 175, 75, math=99, english=90)
#######################################################################################

# 求列表各元素的平方
# a = [1, 2, 3, 4, 5]
# result = [i*i for i in a]
# print(result)

###########
# a = [1,2,3]
# for item in map(lambda x:x*x, a):
#     print(item, end=' ') # 间隔符号更改为空格

#######################################################################################

# 索引
# a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# b = ['a', 'b']
# a[1:9] = b    # 索引从0计算   索引4到索引8（不包括8）
# print(a)
#######################################################################################

# 断言
# def i_want_to_sleep(delay):
#     assert(isinstance(delay, (int,float))), '函数参数必须为整数或浮点数'
#     print('开始睡觉')
#     time.sleep(delay)
#     print('睡醒了')
# i_want_to_sleep(2)

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
mobile = "18017700112"
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
        time.sleep(2)
        edit_mobile = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/edit_phone")  # 选择手机号输入框
        edit_mobile.send_keys(mobile)
        time.sleep(2)
        getcode = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/tv_get_identifyCode")
        getcode.click()
        # TouchAction(driver).tap(x=543, y=494).perform()  # 获取验证码
        time.sleep(2)  # 获取验证码
        logincodeurl = "http://test-uc.crazyccy.com/login/main_login/testtool?key=sLQq2_jaKLknsqAwZ&type=1&mobile=" + mobile
        # print(logincodeurl)
        request = urllib.request.Request(logincodeurl)  # 构建请求url
        response = urllib.request.urlopen(request, context=context)  # ssl证书免验证加入,context = context# 打开请求url链接
        num = response.read()  # 读取页面返回信息，python3返回数据为bytes类型的对象 (即b为前缀, bytes类型)
        logincode = num.decode()
        if logincode == '查不到！':
            TouchAction(driver).tap(x=543, y=494).perform()  # 获取验证码
            time.sleep(2)  # 获取验证码
            logincodeurl = "https://uc.crazyccy.com/login/main_login/testtool?key=sLQq2_jaKLknsqAwZ&type=1&mobile=" + mobile
            request = urllib.request.Request(logincodeurl)  # 构建请求url
            response = urllib.request.urlopen(request, context=context)  # ssl证书免验证加入,context = context# 打开请求url链接
            num = response.read()  # 读取页面返回信息，python3返回数据为bytes类型的对象 (即b为前缀, bytes类型)
            logincode = num.decode()
            # print(logincodeurl)
        edit_Code = driver.find_element_by_id(
            "com.kamitu.drawsth.standalone.free.android:id/edit_identifyCode")  # 选择验证码输入框
        time.sleep(2)
        edit_Code.send_keys(logincode)
        time.sleep(2)
        loginsure = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/btn_sure")
        loginsure.click()
        # TouchAction(driver).tap(x=353, y=660).perform()  # 确定按钮登录
        print("账号登录成功")


check_login()
time.sleep(15)  # 等待10秒加载进入首页
