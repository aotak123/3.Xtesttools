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
capabilities['deviceName'] = 'Mi MIX 2'
capabilities['udid'] = '26385389'
capabilities['appPackage'] = 'com.kamitu.drawsth.standalone.free.android'  # 系统手机中的联系人app的包名
capabilities['appActivity'] = 'com.qsmy.busniess.welcome.WelcomeActivity'  # 系统手机中的联系人app的主入口activity
capabilities['noReset'] = 'true'  # 不重置app
capabilities['autoAcceptAlerts'] = 'true'
capabilities['autoWebview'] = 'false'
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', capabilities, )  # 连接测试所在服务器
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
    time.sleep(3)
    print("\033[1;31mProject.\033[0m " + str(mobile) + " \033[1;31mSTART\033[0m : " + time.strftime('%H:%M:%S'))
    # 登录模块
    try:
        check_login = driver.find_element_by_id(
            "com.kamitu.drawsth.standalone.free.android:id/iv_mobile_login")  # 选择手机号登录
    except NoSuchElementException:
        print("当前为自动登录模式...正在退出账号重新进行登录")
        time.sleep(8)  # 等待加载进入首页
        TouchAction(driver).tap(x=454, y=142).perform()  # 返回进入个人中心
        time.sleep(2)
        TouchAction(driver).tap(x=950, y=150).perform()  # 点击设置
        time.sleep(2)
        TouchAction(driver).tap(x=536, y=1734).perform()  # 点击退出
        time.sleep(1)
        TouchAction(driver).tap(x=687, y=1132).perform()  # 弹窗确定退出
        time.sleep(3)
        TouchAction(driver).tap(x=384, y=1847).perform()  # 点击手机号登录
        time.sleep(1)
        # 选择手机号输入框
        edit_mobile = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/edit_phone")
        edit_mobile.send_keys(mobile)
        time.sleep(2)
        TouchAction(driver).tap(x=803, y=642).perform()  # 获取验证码
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
        time.sleep(1)
        edit_code.send_keys(logincode)
        time.sleep(2)
        TouchAction(driver).tap(x=499, y=879).perform()  # 确定按钮登录
        print("...账号登录成功")
    else:
        TouchAction(driver).tap(x=384, y=1847).perform()  # 点击手机号登录
        time.sleep(1)
        # 选择手机号输入框
        edit_mobile = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/edit_phone")
        edit_mobile.send_keys(mobile)
        time.sleep(2)
        TouchAction(driver).tap(x=803, y=642).perform()  # 获取验证码
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
        time.sleep(1)
        edit_code.send_keys(logincode)
        time.sleep(2)
        TouchAction(driver).tap(x=499, y=879).perform()  # 确定按钮登录
        print("账号登录成功")
    time.sleep(13)  # 等待加载进入首页
    # 进入判官进行刷广告
    TouchAction(driver).tap(x=313, y=1924).perform()  # 选择进入判官
    time.sleep(3)
    TouchAction(driver).tap(x=529, y=1073).perform()  # 选择开始挑战
    time.sleep(3)
    a = 1
    while a <= 11:
        time.sleep(8)
        TouchAction(driver).tap(x=515, y=1383).perform()  # 点击查看广告
        time.sleep(5)
        BB = "  \033[1;31mNO.\033[0m " + str(a) + " 次广告"
        print(BB)
        # os.popen(
        #     "adb -s 26385389 shell am start -n com.kamitu.drawsth.standalone.free.android/com.qsmy.busniess.welcome.WelcomeActivity")
        time.sleep(35)
        TouchAction(driver).tap(x=985, y=89).perform()  # 关闭toutiao广告
        # time.sleep(5)
        # try:
        #     GDT = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
        # except NoSuchElementException:
        #     BB = "  \033[1;31mNO.\033[0m " + str(a) + " toutiaosdk广告"
        #     print(BB)
        #     time.sleep(40)
        #     TouchAction(driver).tap(x=985, y=89).perform()  # 关闭toutiao广告
        # else:
        #     CC = "  \033[1;31mNO.\033[0m " + str(a) + " GDTsdk广告"
        #     print(CC)
        #     time.sleep(55)
        #     driver.back()  # GDTsdk广告按钮
        a += 1
    # 退出广告循环
    time.sleep(8)
    driver.back()  # 判官回到首页
    time.sleep(2)
    # 退出账号
    TouchAction(driver).tap(x=454, y=142).perform()  # 返回进入个人中心
    time.sleep(2)
    try:
        set = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/iv_setting")
    except NoSuchElementException:
        os.popen("adb -s 26385389 shell am  force-stop com.kamitu.drawsth.standalone.free.android")
        time.sleep(2)
        os.popen(
            "adb -s 26385389 shell am start -n com.kamitu.drawsth.standalone.free.android/com.qsmy.busniess.welcome.WelcomeActivity")
        time.sleep(10)  # 等待加载进入首页
        TouchAction(driver).tap(x=454, y=142).perform()  # 返回进入个人中心
        time.sleep(2)
        TouchAction(driver).tap(x=950, y=150).perform()  # 点击设置
        time.sleep(2)
        TouchAction(driver).tap(x=536, y=1734).perform()  # 点击退出
        time.sleep(1)
        TouchAction(driver).tap(x=687, y=1132).perform()  # 弹窗确定退出
    else:
        TouchAction(driver).tap(x=950, y=150).perform()  # 点击设置
        time.sleep(2)
        TouchAction(driver).tap(x=536, y=1734).perform()  # 点击退出
        time.sleep(1)
        TouchAction(driver).tap(x=687, y=1132).perform()  # 弹窗确定退出


########################################################################################################################
if __name__ == '__main__':
    panguan(18782323016)
    panguan(19850838555)
    panguan(19850000111)
    panguan(14987655547)
    panguan(18500071700)
    panguan(14376463070)
    panguan(16728141023)
    panguan(16092840624)
    panguan(17998344668)
    panguan(17490659514)
    panguan(16015383512)
    panguan(19293946812)
    panguan(16944094417)
    panguan(16048177072)
    panguan(17980467459)
    panguan(16021343601)
    panguan(17412349761)
    panguan(14024038791)
    panguan(19425524436)
    panguan(16974415657)
    panguan(19724282179)
    panguan(17929260172)
    panguan(17939699208)
    panguan(19367241617)  # 4/27新增tak
    panguan(17476070492)  # 4/27新增tak
    panguan(16833601539)  # 4/28新增tak
    panguan(17938136012)  # 4/28新增tak
    panguan(14017700111)
    panguan(18100011111)
    panguan(14100099991)
    panguan(18017700603)
    panguan(18017700605)
    panguan(18017700610)
    panguan(18920308799)
    panguan(18901156158)
    panguan(18929597700)
    panguan(18575823673)
    panguan(15353993082)
    panguan(13223986738)
    panguan(17767380753)
    panguan(13200500500)
    panguan(13200500001)
    panguan(19813758251)
    panguan(17261803056)
    panguan(19529759329)
    panguan(13529021576)
    panguan(18987872800)
    panguan(18917779999)
    panguan(13761113333)
    panguan(13985622222)
    panguan(13763333333)
    panguan(13698521470)
    panguan(13760000001)
    panguan(17729152205)
    panguan(16016000001)
    panguan(17538519737)
    panguan(18681025732)
    panguan(18930223547)  # 末凉
    panguan(18017700602)
    panguan(18017700595)
    panguan(18017700597)
    panguan(18017700715)
    panguan(18017700722)

########################################################################################################################
finally2 = "\033[1;31m全部执行完毕：\033[0m " + time.strftime('%H:%M:%S')
print(finally2)
driver.back()
driver.back()
