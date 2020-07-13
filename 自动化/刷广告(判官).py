# coding=utf-8

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.common.exceptions import NoSuchElementException
import time
import urllib.request
import ssl
import sys

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

# capabilities['mobile'] = '18017700601'
# capabilities['mobile'] = '18017700596'
# capabilities['mobile'] = '18930223547'
# capabilities['mobile'] = '18017700475'
# capabilities['mobile'] = '18017700535'
# capabilities['mobile'] = '18017700533'
# capabilities['mobile'] = '18017700598'
# capabilities['mobile'] = '17502150079'
# capabilities['mobile'] = '18017700536'
# capabilities['mobile'] = '18017700602'
# capabilities['mobile'] = '18017700550'
# capabilities['mobile'] = '18017700223'
# capabilities['mobile'] = '18017700597'


driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', capabilities)  # 连接测试所在服务器
mobile = capabilities['mobile']
context = ssl._create_unverified_context()


#看图刷toutiao广告
print("服务启动")
time.sleep(5)
# 检查用户协议及隐私条款
def check_agree():

    try:
        time.sleep(3)
        check_agree = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/tv_agree")  # 三星
    except NoSuchElementException:
        print("无隐私条款")
    else:
        TouchAction(driver).tap(x=1000, y=2050).perform() #点击确定

check_agree()
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
        check_signwindows = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/v_signin_close")
    except NoSuchElementException:
        print("无签到弹窗")
    else:
        TouchAction(driver).tap(x=1270, y=655).perform()
        time.sleep(3)

check_signwindows()
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

TouchAction(driver).tap(x=439, y=2379).perform()#选择进入判官
time.sleep(1)
TouchAction(driver).tap(x=712, y=1342).perform()#选择开始挑战
time.sleep(3)

a = 13
while a > 0:
    time.sleep(6)
    TouchAction(driver).tap(x=671, y=1734).perform()#点击查看广告
    time.sleep(5)
    try:
        GDT_G = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
    except NoSuchElementException:
        print("头条广告")
        time.sleep(35)
        TouchAction(driver).tap(x=1285, y=139).perform()#关闭toutiao广告
        print(a)
        print("toutiaosdk广告关闭")
    else:
        print("广点通广告")
        time.sleep(50)
        driver.back()  # GDTsdk广告按钮
        print(a)
        print("GDTsdk广告关闭")
    a -= 1

driver.back()#判官中回到首页
driver.back()
TouchAction(driver).tap(x=588, y=186).perform()  # 返回进入个人中心
time.sleep(2)
# set1 = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/iv_setting")  # 进入设置
TouchAction(driver).tap(x=1275, y=243).perform()
time.sleep(1)
# logout = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/btn_login_exit")  # 选择退出
TouchAction(driver).tap(x=707, y=2467).perform()
time.sleep(1)
# checklogout = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/text_right")  # 确定退出
TouchAction(driver).tap(x=960, y=1440).perform()
sys.exit()
