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
capabilities['udid'] = 'KWG5T16928033201'
capabilities['appPackage'] = 'com.kamitu.drawsth.standalone.free.android'  # 系统手机中的联系人app的包名
capabilities['appActivity'] = 'com.qsmy.busniess.welcome.WelcomeActivity'  # 系统手机中的联系人app的主入口activity
capabilities['noReset'] = 'true'  # 不重置app
capabilities['autoAcceptAlerts'] = 'true'
capabilities['autoWebview'] = 'false'
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', capabilities)  # 连接测试所在服务器
context = ssl._create_unverified_context()

'''
###一台主机多台设备###
1.请配置不同的服务端号
2.参数配置需要添加udid
3.python配置同意并行运行
4.启动多个appiumsever端

###block list###
https://sign.crazyccy.com:443/index/index
https://update.crazyccy.com/androidupdate/android
'''


########################################################################################################################
def panguan(mobile):
    time.sleep(5)
    print("\033[1;31mProject.\033[0m " + str(mobile) + " \033[1;31mSTART\033[0m : " + time.strftime('%H:%M:%S'))
    # 登录模块
    try:
        check_login = driver.find_element_by_id(
            "com.kamitu.drawsth.standalone.free.android:id/iv_mobile_login")  # 选择手机号登录
    except NoSuchElementException:
        print("当前为自动登录模式...正在退出账号重新进行登录")
        time.sleep(8)  # 等待加载进入首页
        TouchAction(driver).tap(x=422, y=120).perform()  # 返回进入个人中心
        time.sleep(2)
        TouchAction(driver).tap(x=960, y=186).perform()  # 点击设置
        time.sleep(2)
        TouchAction(driver).tap(x=492, y=1777).perform()  # 点击退出
        time.sleep(2)
        TouchAction(driver).tap(x=712, y=1014).perform()  # 弹窗确定退出
        time.sleep(3)
        TouchAction(driver).tap(x=391, y=1591).perform()  # 点击手机号登录
        time.sleep(2)
        # 选择手机号输入框
        edit_mobile = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/edit_phone")
        edit_mobile.send_keys(mobile)
        time.sleep(2)
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
        time.sleep(2)
        edit_code.send_keys(logincode)
        time.sleep(2)
        TouchAction(driver).tap(x=530, y=844).perform()  # 确定按钮登录
        print("...账号登录成功")
    else:
        TouchAction(driver).tap(x=391, y=1591).perform()  # 点击手机号登录
        time.sleep(2)
        # 选择手机号输入框
        edit_mobile = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/edit_phone")
        edit_mobile.send_keys(mobile)
        time.sleep(2)
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
        time.sleep(2)
        edit_code.send_keys(logincode)
        time.sleep(2)
        TouchAction(driver).tap(x=530, y=844).perform()  # 确定按钮登录
        print("账号登录成功")
    time.sleep(15)  # 等待加载进入首页
    # 进入判官进行刷广告
    TouchAction(driver).tap(x=321, y=1665).perform()  # 选择进入判官
    time.sleep(3)
    TouchAction(driver).tap(x=546, y=941).perform()  # 选择开始挑战
    time.sleep(3)
    a = 1
    while a <= 11:
        time.sleep(8)
        TouchAction(driver).tap(x=503, y=1254).perform()  # 点击查看广告
        time.sleep(8)
        BB = "  \033[1;31mNO.\033[0m " + str(a) + " toutiaosdk广告"
        print(BB)
        os.popen(
            "adb -s KWG5T16928033201 shell am start -n com.kamitu.drawsth.standalone.free.android/com.qsmy.busniess.welcome.WelcomeActivity")
        time.sleep(42)
        TouchAction(driver).tap(x=964, y=101).perform()  # 关闭toutiao广告
        # time.sleep(5)
        # try:
        #     GDT = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
        # except NoSuchElementException:
        #     BB = "  \033[1;31mNO.\033[0m " + str(a) + " toutiaosdk广告"
        #     print(BB)
        #     time.sleep(40)
        #     TouchAction(driver).tap(x=964, y=101).perform()  # 关闭toutiao广告
        # else:
        #     CC = "  \033[1;31mNO.\033[0m " + str(a) + " GDTsdk广告"
        #     print(CC)
        #     time.sleep(55)
        #     driver.back()  # GDTsdk广告按钮
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
        os.popen("adb -s KWG5T16928033201 shell am force-stop com.kamitu.drawsth.standalone.free.android")
        time.sleep(2)
        os.popen(
            "adb -s KWG5T16928033201 shell am start -n com.kamitu.drawsth.standalone.free.android/com.qsmy.busniess.welcome.WelcomeActivity")
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
    b = 1
    while b <= 2:
        panguan(17729152205)
        panguan(16016000001)
        panguan(18681025732)
        panguan(18930223547)  # 末凉
        panguan(18017700602)
        panguan(18017700722)
        panguan(18819123459)
        panguan(13168867678)
        panguan(15981831553)
        panguan(18017700401)
        panguan(18017700403)
        panguan(18017700515)
        panguan(18017700516)
        panguan(18017700521)
        panguan(18017700530)
        panguan(18017700595)
        panguan(18017700597)
        panguan(18017700715)
        panguan(18017700537)
        panguan(18017700550)
        panguan(14987654444)
        panguan(14987655533)
        panguan(14987656424)
        panguan(18017700571)
        panguan(18017700475)
        panguan(16021343601)
        panguan(17412349761)
        panguan(14024038791)
        panguan(19425524436)
        panguan(16974415657)
        panguan(19724282179)
        panguan(17929260172)

########################################################################################################################
finally2 = "\033[1;31m全部执行完毕：\033[0m " + time.strftime('%H:%M:%S')
print(finally2)
driver.back()
driver.back()
