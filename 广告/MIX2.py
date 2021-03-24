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
driver = webdriver.Remote('http://127.0.0.1:4725/wd/hub', capabilities, )  # 连接测试所在服务器
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
        time.sleep(1)
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
        time.sleep(1)
        TouchAction(driver).tap(x=499, y=879).perform()  # 确定按钮登录
        print("账号登录成功")
    time.sleep(8)  # 等待加载进入首页
    # 进入判官进行刷广告
    TouchAction(driver).tap(x=313, y=1924).perform()  # 选择进入判官
    time.sleep(3)
    TouchAction(driver).tap(x=539, y=1078).perform()  # 选择开始挑战
    time.sleep(3)
    a = 1
    while a <= 11:
        time.sleep(8)
        TouchAction(driver).tap(x=515, y=1383).perform()  # 点击查看广告
        time.sleep(5)
        try:
            GDT = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
        except NoSuchElementException:
            BB = "  \033[1;31mNO.\033[0m " + str(a) + " toutiaosdk广告"
            print(BB)
            time.sleep(40)
            TouchAction(driver).tap(x=985, y=89).perform()  # 关闭toutiao广告
        else:
            CC = "  \033[1;31mNO.\033[0m " + str(a) + " GDTsdk广告"
            print(CC)
            time.sleep(55)
            driver.back()  # GDTsdk广告按钮
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
    panguan(18508071757)
    panguan(18600007117)
    panguan(14060019638)
    panguan(14120012351)
    panguan(14010000158)
    panguan(14020000269)
    panguan(14012341472)
    panguan(18234567890)
    panguan(13122027777)
    panguan(19825805208)
    panguan(19825052192)
    panguan(17538253260)
    panguan(14111007144)
    panguan(14112008053)
    panguan(14113009962)
    panguan(14114000871)
    panguan(14115001780)
    panguan(14988882699)
    panguan(14988883508)
    panguan(14988884417)
    panguan(14988885326)
    panguan(14130006143)
    panguan(14030001372)
    panguan(14040002483)
    panguan(14050003594)
    panguan(14060004605)
    panguan(18222851111)
    panguan(14988886235)
    panguan(14987650098)
    panguan(14987651909)
    panguan(14987652810)
    panguan(14987653729)
    panguan(14987654638)
    panguan(14987658274)  # 3/22新增tak
    panguan(14987659183)  # 3/22新增tak
    panguan(14987650092)  # 3/23新增tak
    panguan(14987651901)  # 3/23新增tak
    panguan(14987652819)  # 3/24新增tak
    panguan(14987653728)  # 3/24新增tak

########################################################################################################################
finally2 = "\033[1;31m全部执行完毕：\033[0m " + time.strftime('%H:%M:%S')
print(finally2)
driver.back()
driver.back()
