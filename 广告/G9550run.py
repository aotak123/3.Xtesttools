# coding=utf-8

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.common.exceptions import NoSuchElementException
import time
import urllib.request
import ssl

capabilities = {}
capabilities['platformName'] = 'Android'  # Android平台测试
capabilities['platformVersion'] = '9.0'
capabilities['deviceName'] = 'SM-G9550'
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
        TouchAction(driver).tap(x=530, y=2541).perform()  # 点击手机号登录
        time.sleep(2)
        edit_mobile = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/edit_phone")  # 选择手机号输入框
        edit_mobile.send_keys(mobile)
        time.sleep(1)
        TouchAction(driver).tap(x=1035, y=899).perform()  # 获取验证码
        time.sleep(2)
        # 获取验证码
        logincodeurl = "https://uc.crazyccy.com/login/main_login/testtool?key=sLQq2_jaKLknsqAwZ&type=1&mobile=" + str(
            mobile)
        request = urllib.request.Request(logincodeurl)  # 构建请求url
        response = urllib.request.urlopen(request, context=context)  # ssl证书免验证加入,context = context# 打开请求url链接
        num = response.read()  # 读取页面返回信息，python3返回数据为bytes类型的对象 (即b为前缀, bytes类型)
        logincode = num.decode()
        if logincode == '查不到！':
            time.sleep(2)
            TouchAction(driver).tap(x=1035, y=899).perform()  # 获取验证码
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
        TouchAction(driver).tap(x=700, y=1184).perform()  # 确定按钮登录
        print("账号登录成功")
    time.sleep(15)  # 等待加载进入首页
    # 检查是否弹出每日签到弹窗
    try:
        check_signwindows = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/iv_signin_get")
    except NoSuchElementException:
        print("无每日签到弹窗")
    else:
        TouchAction(driver).tap(x=1267, y=839).perform()  # 关闭每日签到弹窗
        time.sleep(2)
    # 进入接龙主游戏页面
    TouchAction(driver).tap(x=702, y=2291).perform()  # 进入接龙页面
    time.sleep(3)
    driver.back()
    time.sleep(2)
    # 检查是否弹出签到提示
    try:
        check_signtoast = driver.find_element_by_id(
            "com.kamitu.drawsth.standalone.free.android:id/btn_open_reminder")
    except NoSuchElementException:
        print("无签到提醒弹窗")
    else:
        TouchAction(driver).tap(x=720, y=1839).perform()  # 关闭签到提示弹窗
        time.sleep(2)
    # 进入判官进行刷广告
    TouchAction(driver).tap(x=446, y=2588).perform()  # 选择进入判官
    time.sleep(2)
    TouchAction(driver).tap(x=720, y=1458).perform()  # 选择开始挑战
    time.sleep(3)
    a = 1
    while a <= 11:
        time.sleep(8)
        TouchAction(driver).tap(x=684, y=1857).perform()  # 点击查看广告
        time.sleep(10)
        try:
            GDT = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
        except NoSuchElementException:
            BB = "  \033[1;31mNO.\033[0m " + str(a) + " toutiaosdk广告"
            print(BB)
            time.sleep(35)
            TouchAction(driver).tap(x=1303, y=113).perform()  # 关闭toutiao广告
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
    time.sleep(2)
    # 退出账号
    TouchAction(driver).tap(x=583, y=208).perform()  # 返回进入个人中心
    time.sleep(2)
    TouchAction(driver).tap(x=1291, y=214).perform()  # 点击设置
    time.sleep(1)
    TouchAction(driver).tap(x=708, y=476).perform()  # 点击清理
    time.sleep(1)
    TouchAction(driver).tap(x=916, y=1535).perform()  # 弹窗确定清理
    time.sleep(1)
    TouchAction(driver).tap(x=708, y=2154).perform()  # 点击退出
    time.sleep(1)
    TouchAction(driver).tap(x=916, y=1535).perform()  # 弹窗确定退出


#############################################################################################################################################################

if __name__ == '__main__':
    panguan(13062803788)  # NO.01
    panguan(13161057550)  # NO.02
    panguan(13161057579)  # NO.03
    panguan(13168867678)  # NO.04
    panguan(13402063488)  # NO.05
    panguan(13666088700)  # NO.06
    panguan(13666088775)  # NO.07
    panguan(13683351952)  # NO.08
    panguan(15173160505)  # NO.09
    panguan(15721403717)  # NO.10
    panguan(15823382766)  # NO.11
    panguan(15850670782)  # NO.12
    panguan(15981831553)  # NO.13
    panguan(17318102888)  # NO.14
    panguan(18017700595)  # NO.15
    panguan(18017700597)  # NO.16
    panguan(18017700602)  # NO.17
    panguan(18017700603)  # NO.18
    panguan(18017700605)  # NO.19
    panguan(18017700610)  # NO.20
    panguan(18017700611)  # NO.21
    panguan(18017700713)  # NO.22
    panguan(18017700715)  # NO.23
    panguan(18017700716)  # NO.24
    panguan(18017700722)  # NO.25
    panguan(18027328833)  # NO.26
    panguan(18116688811)  # NO.27
    panguan(18116688822)  # NO.28
    panguan(18116699805)  # NO.29
    panguan(18519820628)  # NO.30
    panguan(18321273743)  # NO.31
    panguan(18819123459)  # NO.32
    panguan(18901156158)  # NO.33
    panguan(18920308799)  # NO.34
    panguan(18929597700)  # NO.35
    panguan(18145608526)  # NO.36
    panguan(18930223547)  # NO.37
    panguan(13255615265)  # NO.38
    panguan(13032337272)  # NO.39
    panguan(17322190031)  # NO.40
    panguan(13720031029)  # NO.41
    panguan(18116699805)  # NO.42

#############################################################################################################################################################
finally2 = "\033[1;31m全部执行完毕：\033[0m " + time.strftime('%H:%M:%S')
print(finally2)
driver.back()
driver.back()
