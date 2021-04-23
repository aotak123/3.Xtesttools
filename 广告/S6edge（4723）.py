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
capabilities['platformVersion'] = '6.0.1'
capabilities['deviceName'] = 'SM-G9250'
capabilities['udid'] = '02157df2c8865716'
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
    time.sleep(3)
    print("\033[1;31mProject.\033[0m " + str(mobile) + " \033[1;31mSTART\033[0m : " + time.strftime('%H:%M:%S'))
    # 登录模块
    try:
        check_login = driver.find_element_by_id(
            "com.kamitu.drawsth.standalone.free.android:id/iv_mobile_login")  # 选择手机号登录
    except NoSuchElementException:
        print("当前为自动登录模式...正在退出账号重新进行登录")
        time.sleep(8)  # 等待加载进入首页
        TouchAction(driver).tap(x=588, y=186).perform()  # 返回进入个人中心
        time.sleep(2)
        TouchAction(driver).tap(x=1275, y=243).perform()  # 点击设置
        time.sleep(2)
        TouchAction(driver).tap(x=707, y=2467).perform()  # 点击退出
        time.sleep(1)
        TouchAction(driver).tap(x=960, y=1440).perform()  # 弹窗确定退出
        time.sleep(3)
        TouchAction(driver).tap(x=515, y=2300).perform()  # 点击手机号登录
        time.sleep(1)
        # 选择手机号输入框
        edit_mobile = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/edit_phone")
        edit_mobile.send_keys(mobile)
        time.sleep(2)
        TouchAction(driver).tap(x=1100, y=870).perform()  # 获取验证码
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
        TouchAction(driver).tap(x=700, y=1200).perform()  # 确定按钮登录
        print("...账号登录成功")
    else:
        TouchAction(driver).tap(x=515, y=2300).perform()  # 点击手机号登录
        time.sleep(1)
        # 选择手机号输入框
        edit_mobile = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/edit_phone")
        edit_mobile.send_keys(mobile)
        time.sleep(2)
        TouchAction(driver).tap(x=1100, y=870).perform()  # 获取验证码
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
        TouchAction(driver).tap(x=700, y=1200).perform()  # 确定按钮登录
        print("账号登录成功")
    time.sleep(13)  # 等待加载进入首页
    # 进入判官进行刷广告
    TouchAction(driver).tap(x=439, y=2379).perform()  # 选择进入判官
    time.sleep(3)
    TouchAction(driver).tap(x=712, y=1342).perform()  # 选择开始挑战
    time.sleep(3)
    a = 1
    while a <= 11:
        time.sleep(8)
        TouchAction(driver).tap(x=671, y=1734).perform()  # 点击查看广告
        time.sleep(5)
        BB = "  \033[1;31mNO.\033[0m " + str(a) + " 次广告"
        print(BB)
        # os.popen("adb -s 02157df2c8865716 shell am start -n com.kamitu.drawsth.standalone.free.android/com.qsmy.busniess.welcome.WelcomeActivity")
        time.sleep(35)
        TouchAction(driver).tap(x=1285, y=139).perform()  # 关闭toutiao广告
        # time.sleep(5)
        # try:
        #     GDT = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
        # except NoSuchElementException:
        #     BB = "  \033[1;31mNO.\033[0m " + str(a) + " toutiaosdk广告"
        #     print(BB)
        #     time.sleep(40)
        #     TouchAction(driver).tap(x=1285, y=139).perform()  # 关闭toutiao广告
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
    TouchAction(driver).tap(x=588, y=186).perform()  # 返回进入个人中心
    time.sleep(2)
    try:
        set = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/iv_setting")
    except NoSuchElementException:
        os.popen("adb -s 02157df2c8865716 shell am force-stop com.kamitu.drawsth.standalone.free.android")
        time.sleep(2)
        os.popen(
            "adb -s 02157df2c8865716 shell am start -n com.kamitu.drawsth.standalone.free.android/com.qsmy.busniess.welcome.WelcomeActivity")
        time.sleep(10)  # 等待加载进入首页
        TouchAction(driver).tap(x=588, y=186).perform()  # 返回进入个人中心
        time.sleep(2)
        TouchAction(driver).tap(x=1275, y=243).perform()  # 点击设置
        time.sleep(2)
        TouchAction(driver).tap(x=707, y=2467).perform()  # 点击退出
        time.sleep(1)
        TouchAction(driver).tap(x=960, y=1440).perform()  # 弹窗确定退出
    else:
        TouchAction(driver).tap(x=1275, y=243).perform()  # 点击设置
        time.sleep(2)
        TouchAction(driver).tap(x=707, y=2467).perform()  # 点击退出
        time.sleep(1)
        TouchAction(driver).tap(x=960, y=1440).perform()  # 弹窗确定退出


########################################################################################################################
if __name__ == '__main__':
    panguan(18017700571)
    panguan(18017700475)
    panguan(18017700533)
    panguan(18017700535)
    panguan(18017700477)
    panguan(18017700580)  # 小糖糖2
    panguan(18918024483)
    panguan(18017700596)
    panguan(18017700598)
    panguan(18017700600)
    panguan(18017700601)
    panguan(18017700604)
    panguan(18017700606)
    panguan(18017700710)  # 治疗失眠陶老师
    panguan(18017700223)
    panguan(17502150079)  # 小糖糖
    panguan(18017700339)  # 阿拉斯加加加加
    panguan(18017700400)
    panguan(18017700410)
    panguan(18017700411)
    panguan(18017700207)
    panguan(18017700478)
    panguan(18014400369)
    panguan(13651711999)
    panguan(15917449818)
    panguan(13032337111)
    panguan(19823637887)
    panguan(18017700355)
    panguan(15611828882)
    panguan(18085112222)
    panguan(13666088773)
    panguan(17939309036)
    panguan(16967271006)
    panguan(18616905709)
    panguan(18503807583)
    panguan(18601608371)
    panguan(18780000008)
    panguan(18637605801)
    panguan(17752939592)
    panguan(18131526059)
    panguan(15660925537)
    panguan(18050071007)
    panguan(13161767110)
    panguan(13161057538)
    panguan(13164767109)
    panguan(13311936568)
    panguan(18601608165)
    panguan(13520010705)
    panguan(15237371035)
    panguan(17710032752)
    panguan(18519880503)
    panguan(13920051605)
    panguan(14988887144)
    panguan(14988888053)
    panguan(14988889962)
    panguan(14988887871)
    panguan(14988888780)
    panguan(14988889699)
    panguan(14987654444)
    panguan(14987655533)
    panguan(14987656424)
    panguan(14987657315)
    panguan(14987658206)
    panguan(14987659197)
    panguan(14987656456)
    panguan(14987657365)
    panguan(14629177373)
    panguan(14261015450)
    panguan(17429725866)
    panguan(19555949829)

########################################################################################################################
finally2 = "\033[1;31m全部执行完毕：\033[0m " + time.strftime('%H:%M:%S')
print(finally2)
driver.back()
driver.back()
