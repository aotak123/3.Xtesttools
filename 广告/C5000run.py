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

first1 = "\033[1;31m执行开始\033[0m " + time.strftime('%H:%M:%S')
print(first1)


#############################################################################################################################################################
def panguan(mobile):
    time.sleep(5)
    AA = "\033[1;31mProject.\033[0m " + str(mobile) + " \033[1;31mSTART\033[0m"
    print(AA)
    # 登录模块
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
        logincodeurl = "https://uc.crazyccy.com/login/main_login/testtool?key=sLQq2_jaKLknsqAwZ&type=1&mobile=" + str(
            mobile)
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
    time.sleep(15)  # 等待加载进入首页
    # 检查是否弹出每日签到弹窗
    try:
        check_signwindows = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/iv_signin_get")
    except NoSuchElementException:
        print("无签到弹窗")
    else:
        TouchAction(driver).tap(x=953, y=551).perform()  # 关闭签到弹窗
        time.sleep(3)
    # 进入接龙主游戏页面
    TouchAction(driver).tap(x=525, y=1556).perform()  # 进入接龙页面
    time.sleep(3)
    driver.back()
    time.sleep(3)
    # 检查是否弹出签到提示
    try:
        check_signtoast = driver.find_element_by_id(
            "com.kamitu.drawsth.standalone.free.android:id/btn_open_reminder")
    except NoSuchElementException:
        print("无签到提醒弹窗")
    else:
        TouchAction(driver).tap(x=870, y=611).perform()  # 关闭签到提示弹窗
    time.sleep(2)
    # 进入判官进行刷广告
    TouchAction(driver).tap(x=323, y=1774).perform()  # 选择进入判官
    time.sleep(2)
    TouchAction(driver).tap(x=536, y=1009).perform()  # 选择开始挑战
    time.sleep(3)
    a = 1
    while a <= 11:
        time.sleep(8)
        TouchAction(driver).tap(x=503, y=1305).perform()  # 点击查看广告
        time.sleep(10)

        try:
            GDT = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
        except NoSuchElementException:
            BB = "  \033[1;31mNO.\033[0m " + str(a) + " toutiaosdk广告"
            print(BB)
            time.sleep(40)
            TouchAction(driver).tap(x=979, y=86).perform()  # 关闭toutiao广告
            print("     toutiaosdk广告关闭")
        else:
            CC = "  \033[1;31mNO.\033[0m " + str(a) + " GDTsdk广告"
            print(CC)
            time.sleep(55)
            driver.back()  # GDTsdk广告按钮
            print("     GDTsdk广告关闭")
        a += 1
    # 退出广告循环
    time.sleep(8)
    driver.back()  # 判官中回到首页
    time.sleep(1)
    driver.back()
    time.sleep(2)
    # 退出账号
    TouchAction(driver).tap(x=439, y=124).perform()  # 返回进入个人中心
    time.sleep(2)
    TouchAction(driver).tap(x=971, y=158).perform()  # 点击设置
    time.sleep(2)
    TouchAction(driver).tap(x=534, y=1614).perform()  # 点击退出
    time.sleep(2)
    TouchAction(driver).tap(x=690, y=1069).perform()  # 弹窗确定退出


#############################################################################################################################################################

if __name__ == '__main__':
    panguan(13032337111)  # NO.1
    panguan(13062803788)  # NO.2
    panguan(13161057550)  # NO.3
    panguan(13161057579)  # NO.4
    panguan(13168867678)  # NO.5
    panguan(13560736789)  # NO.6
    panguan(13666088700)  # NO.7
    panguan(15611828881)  # NO.8
    panguan(15721403717)  # NO.9
    panguan(15917449818)  # NO.10
    panguan(15981831553)  # NO.11
    panguan(18014400369)  # NO.12
    panguan(18017700339)  # NO.13
    panguan(18017700401)  # NO.14
    panguan(18017700403)  # NO.15
    panguan(18017700413)  # NO.16
    panguan(18017700414)  # NO.17
    panguan(18017700521)  # NO.18
    panguan(18017700715)  # NO.19
    panguan(18116699805)  # NO.20
    panguan(18220860324)  # NO.21
    panguan(18317269850)  # NO.22
    panguan(18321273743)  # NO.23
    panguan(18819123459)  # NO.24
    panguan(18918024483)  # NO.25
    panguan(19823637887)  # NO.26
    panguan(15173160505)  # NO.27
    panguan(15927257999)  # NO.28
    panguan(13161767110)  # NO.29
    panguan(18180868581)  # NO.30
    panguan(18920308799)  # NO.31
    panguan(18027328833)  # NO.32
    panguan(18901156158)  # NO.33
    panguan(17318102888)  # NO.34
    panguan(18929597700)  # NO.35
    panguan(15850670782)  # NO.36
    panguan(15823382766)  # NO.37
    panguan(13666088775)  # NO.38
    panguan(13683351952)  # NO.39



#############################################################################################################################################################
finally2 = "\033[1;31m全部执行完毕：\033[0m " + time.strftime('%H:%M:%S')
print(finally2)
driver.back()
driver.back()
