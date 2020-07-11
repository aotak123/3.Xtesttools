# coding=utf-8

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.common.exceptions import NoSuchElementException
import time
import urllib.request
import ssl


capabilities = {}
# Android平台测试
capabilities['platformName'] = 'Android'
capabilities['platformVersion'] = '7.1.2'
capabilities['deviceName'] = 'vivo X9Plus'
# 系统手机中的联系人app的包名
capabilities['appPackage'] = 'com.kamitu.drawsth.standalone.free.android'
# 系统手机中的联系人app的主入口activity
capabilities['appActivity'] = 'com.qsmy.busniess.welcome.WelcomeActivity'
capabilities['unicodeKeyboard'] = 'true' # 如果指定UI2作为驱动，不需要配置
capabilities['resetKeyboard'] = 'true' # 重置自动化时设置的键盘
capabilities['noReset'] = 'false'
capabilities['autoGrantPermissions'] = 'true' # appium自动设置权限
capabilities['autoWebview'] = 'false'
capabilities['mobile'] = '18017700610'
# 连接测试机所在服务器服务器
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', capabilities)
mobile = capabilities['mobile']
context = ssl._create_unverified_context()


def check_agree():  # 检查用户协议及隐私条款
    try:
        check_agree = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/mh")
    except NoSuchElementException:
        pass
    else:
        check_agree.click()
        print("FKC-4:权限引导:隐私及授权弹窗   PASS")
check_agree()
time.sleep(5)

def mobile_login():
    try:
        check_login = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/ga")  # 选择手机号登录
    except NoSuchElementException:
        pass
    else:
        check_login.click()
        time.sleep(2)
        el2 = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/do")  # 选择手机号输入框
        el2.send_keys(mobile)
        time.sleep(3)
        el3 = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/n2")  # 发送验证码
        el3.click()
        time.sleep(2)

        # 获取验证码
        logincodeurl = "https://uc.crazyccy.com/login/main_login/testtool?key=sLQq2_jaKLknsqAwZ&type=1&mobile=" + mobile
        # print(logincodeurl)
        request = urllib.request.Request(logincodeurl)  # 构建请求url
        response = urllib.request.urlopen(request, context=context)  # ssl证书免验证加入,context = context# 打开请求url链接
        num = response.read()  # 读取页面返回信息，python3返回数据为bytes类型的对象 (即b为前缀, bytes类型)
        logincode = num.decode()
        if logincode == "查不到！":
            print()
        else:
            time.sleep(2)
            el4 = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/dn")  # 选择验证码输入框
            time.sleep(2)
            el4.send_keys(logincode)

        el5 = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/b1")  # 再点击确定登录
        el5.click()

mobile_login()