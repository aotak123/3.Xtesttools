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
capabilities['platformVersion'] = '9.0'
capabilities['deviceName'] = 'SM-G9550'
capabilities['udid'] = '98899a463539333854'
capabilities['appPackage'] = 'com.kamitu.drawsth.standalone.free.android'  # 系统手机中的联系人app的包名
capabilities['appActivity'] = 'com.qsmy.busniess.welcome.WelcomeActivity'  # 系统手机中的联系人app的主入口activity
capabilities['noReset'] = 'true'  # 不重置app
capabilities['autoAcceptAlerts'] = 'true'
capabilities['autoWebview'] = 'false'
driver = webdriver.Remote('http://127.0.0.1:4725/wd/hub', capabilities)  # 连接测试所在服务器
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
        TouchAction(driver).tap(x=583, y=208).perform()  # 返回进入个人中心
        time.sleep(2)
        TouchAction(driver).tap(x=1291, y=214).perform()  # 点击设置
        time.sleep(2)
        TouchAction(driver).tap(x=708, y=2154).perform()  # 点击退出
        time.sleep(1)
        TouchAction(driver).tap(x=916, y=1535).perform()  # 弹窗确定退出
        time.sleep(3)
        TouchAction(driver).tap(x=530, y=2541).perform()  # 点击手机号登录
        time.sleep(1)
        # 选择手机号输入框
        edit_mobile = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/edit_phone")
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
        edit_Code = driver.find_element_by_id(
            "com.kamitu.drawsth.standalone.free.android:id/edit_identifyCode")  # 选择验证码输入框
        time.sleep(1)
        edit_Code.send_keys(logincode)
        time.sleep(2)
        TouchAction(driver).tap(x=700, y=1184).perform()  # 确定按钮登录
        print("...账号登录成功")
    else:
        TouchAction(driver).tap(x=530, y=2541).perform()  # 点击手机号登录
        time.sleep(1)
        # 选择手机号输入框
        edit_mobile = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/edit_phone")
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
        edit_Code = driver.find_element_by_id(
            "com.kamitu.drawsth.standalone.free.android:id/edit_identifyCode")  # 选择验证码输入框
        time.sleep(1)
        edit_Code.send_keys(logincode)
        time.sleep(2)
        TouchAction(driver).tap(x=700, y=1184).perform()  # 确定按钮登录
        print("账号登录成功")
    time.sleep(13)  # 等待加载进入首页
    # 进入判官进行刷广告
    TouchAction(driver).tap(x=446, y=2588).perform()  # 选择进入判官
    time.sleep(3)
    TouchAction(driver).tap(x=720, y=1458).perform()  # 选择开始挑战
    time.sleep(3)
    a = 1
    while a <= 11:
        time.sleep(8)
        TouchAction(driver).tap(x=684, y=1857).perform()  # 点击查看广告
        time.sleep(5)
        BB = "  \033[1;31mNO.\033[0m " + str(a) + " 次广告"
        print(BB)
        # os.popen(
        #     "adb -s 98899a463539333854 shell am start -n com.kamitu.drawsth.standalone.free.android/com.qsmy.busniess.welcome.WelcomeActivity")
        time.sleep(35)
        TouchAction(driver).tap(x=1303, y=113).perform()  # 关闭toutiao广告
        # time.sleep(5)
        # try:
        #     GDT = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
        # except NoSuchElementException:
        #     BB = "  \033[1;31mNO.\033[0m " + str(a) + " toutiaosdk广告"
        #     print(BB)
        #     time.sleep(40)
        #     TouchAction(driver).tap(x=1303, y=113).perform()  # 关闭toutiao广告
        # else:
        #     CC = "  \033[1;31mNO.\033[0m " + str(a) + " GDTsdk广告"
        #     print(CC)
        #     time.sleep(55)
        #     driver.back()  # GDTsdk广告按钮
        a += 1
    # 退出广告循环
    time.sleep(10)
    driver.back()  # 判官回到首页
    time.sleep(3)
    # 退出账号
    TouchAction(driver).tap(x=583, y=208).perform()  # 返回进入个人中心
    time.sleep(2)
    try:
        set = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/iv_setting")
    except NoSuchElementException:
        os.popen("adb -s 98899a463539333854 shell am force-stop com.kamitu.drawsth.standalone.free.android")
        time.sleep(2)
        os.popen(
            "adb -s 98899a463539333854 shell am start -n com.kamitu.drawsth.standalone.free.android/com.qsmy.busniess.welcome.WelcomeActivity")
        time.sleep(10)  # 等待加载进入首页
        TouchAction(driver).tap(x=583, y=208).perform()  # 返回进入个人中心
        time.sleep(2)
        TouchAction(driver).tap(x=1291, y=214).perform()  # 点击设置
        time.sleep(2)
        TouchAction(driver).tap(x=708, y=2154).perform()  # 点击退出
        time.sleep(1)
        TouchAction(driver).tap(x=916, y=1535).perform()  # 弹窗确定退出
    else:
        TouchAction(driver).tap(x=1291, y=214).perform()  # 点击设置
        time.sleep(2)
        TouchAction(driver).tap(x=708, y=2154).perform()  # 点击退出
        time.sleep(1)
        TouchAction(driver).tap(x=916, y=1535).perform()  # 弹窗确定退出


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
    panguan(14012398702)
    panguan(18017700536)
    panguan(18222222222)
    panguan(18600007007)
    panguan(17857577938)
    panguan(19876543210)
    panguan(18622077306)
    panguan(18933207305)
    panguan(16015012345)
    panguan(14012398701)
    panguan(18007610419)
    panguan(18127209865)
    panguan(17538253260)
    panguan(14111007144)
    panguan(14112008053)
    panguan(14113009962)
    panguan(14114000871)
    panguan(14115001780)
    panguan(14988882699)
    panguan(13560736789)
    panguan(15611828881)
    panguan(18134508526)
    panguan(15927257999)
    panguan(18017700540)
    panguan(18930224047)
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
    panguan(14987658274)
    panguan(14987659183)
    panguan(14987650092)
    panguan(14987651901)
    panguan(14987652819)
    panguan(14987653728)
    panguan(14987654637)
    panguan(14987655546)
    panguan(14987656455)
    panguan(14987657364)
    panguan(14987658273)
    panguan(14987659182)
    panguan(14987651991)
    panguan(14987652002)
    panguan(16994779810)
    panguan(19367984833)
    panguan(17455039213)
    panguan(19458371424)
    panguan(14498412062)
    panguan(17993769525)
    panguan(17946568789)  # 4/26新增tak
    panguan(19412085993)  # 4/26新增tak

########################################################################################################################
finally2 = "\033[1;31m全部执行完毕：\033[0m " + time.strftime('%H:%M:%S')
print(finally2)
driver.back()
driver.back()
