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
    time.sleep(8)
    print("\033[1;31mProject.\033[0m " + str(mobile) + " \033[1;31mSTART\033[0m : " + time.strftime('%H:%M:%S'))
    # 登录模块
    try:
        check_login = driver.find_element_by_id(
            "com.kamitu.drawsth.standalone.free.android:id/iv_mobile_login")  # 选择手机号登录
    except NoSuchElementException:
        print("当前为自动登录模式...正在退出账号重新进行登录")
        time.sleep(10)  # 等待加载进入首页
        TouchAction(driver).tap(x=454, y=142).perform()  # 返回进入个人中心
        time.sleep(2)
        TouchAction(driver).tap(x=950, y=150).perform()  # 点击设置
        time.sleep(2)
        TouchAction(driver).tap(x=536, y=1734).perform()  # 点击退出
        time.sleep(2)
        TouchAction(driver).tap(x=687, y=1132).perform()  # 弹窗确定退出
        time.sleep(3)
        TouchAction(driver).tap(x=384, y=1847).perform()  # 点击手机号登录
        time.sleep(2)
        # 选择手机号输入框
        edit_mobile = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/edit_phone")
        edit_mobile.send_keys(mobile)
        time.sleep(2)
        TouchAction(driver).tap(x=799, y=807).perform()  # 获取验证码
        time.sleep(3)
        # 获取验证码
        logincodeurl = "https://uc.crazyccy.com/login/main_login/testtool?key=sLQq2_jaKLknsqAwZ&type=1&mobile=" + str(
            mobile)
        request = urllib.request.Request(logincodeurl)  # 构建请求url
        response = urllib.request.urlopen(request, context=context)  # ssl证书免验证加入,context = context# 打开请求url链接
        num = response.read()  # 读取页面返回信息，python3返回数据为bytes类型的对象 (即b为前缀, bytes类型)
        logincode = num.decode()
        edit_code = driver.find_element_by_id(
            "com.kamitu.drawsth.standalone.free.android:id/edit_identifyCode")  # 选择验证码输入框
        time.sleep(3)
        edit_code.send_keys(logincode)
        time.sleep(2)
        TouchAction(driver).tap(x=519, y=1032).perform()  # 确定按钮登录
        print("...账号登录成功")
    else:
        TouchAction(driver).tap(x=384, y=1847).perform()  # 点击手机号登录
        time.sleep(2)
        # 选择手机号输入框
        edit_mobile = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/edit_phone")
        edit_mobile.send_keys(mobile)
        time.sleep(2)
        TouchAction(driver).tap(x=799, y=807).perform()  # 获取验证码
        time.sleep(3)
        # 获取验证码
        logincodeurl = "https://uc.crazyccy.com/login/main_login/testtool?key=sLQq2_jaKLknsqAwZ&type=1&mobile=" + str(
            mobile)
        request = urllib.request.Request(logincodeurl)  # 构建请求url
        response = urllib.request.urlopen(request, context=context)  # ssl证书免验证加入,context = context# 打开请求url链接
        num = response.read()  # 读取页面返回信息，python3返回数据为bytes类型的对象 (即b为前缀, bytes类型)
        logincode = num.decode()
        edit_code = driver.find_element_by_id(
            "com.kamitu.drawsth.standalone.free.android:id/edit_identifyCode")  # 选择验证码输入框
        time.sleep(3)
        edit_code.send_keys(logincode)
        time.sleep(2)
        TouchAction(driver).tap(x=519, y=1032).perform()  # 确定按钮登录
        print("账号登录成功")
    time.sleep(20)  # 等待加载进入首页
    # 进入判官进行刷广告
    TouchAction(driver).tap(x=313, y=1924).perform()  # 选择进入判官
    time.sleep(3)
    TouchAction(driver).tap(x=529, y=1073).perform()  # 选择开始挑战
    time.sleep(3)
    a = 1
    while a <= 11:
        time.sleep(10)
        TouchAction(driver).tap(x=515, y=1383).perform()  # 点击查看广告
        time.sleep(8)
        BB = "  \033[1;31mNO.\033[0m " + str(a) + " 次广告"
        print(BB)
        os.popen(
            "adb -s 26385389 shell am start -n com.kamitu.drawsth.standalone.free.android/com.qsmy.busniess.welcome.WelcomeActivity")
        time.sleep(42)
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
        time.sleep(2)
        TouchAction(driver).tap(x=687, y=1132).perform()  # 弹窗确定退出
    else:
        TouchAction(driver).tap(x=950, y=150).perform()  # 点击设置
        time.sleep(2)
        TouchAction(driver).tap(x=536, y=1734).perform()  # 点击退出
        time.sleep(2)
        TouchAction(driver).tap(x=687, y=1132).perform()  # 弹窗确定退出

########################################################################################################################
if __name__ == '__main__':
    b = 1
    while b <= 2:
        # tun
        panguan(14190006235)
        panguan(13666088700)
        panguan(13161057550)
        panguan(13062803788)
        panguan(19099990000)
        panguan(19088881111)
        panguan(19088882020)
        panguan(19088885672)
        panguan(17729152205)
        panguan(18017700722)
        panguan(18017700716)
        panguan(18017700713)
        panguan(16016000001)
        panguan(18017700521)
        panguan(18681025732)
        panguan(17538519737)
        panguan(18819123459)
        panguan(13168867678)
        panguan(15981831553)
        panguan(18017700401)
        panguan(18017700403)
        panguan(18017700611)
        panguan(18116699805)
        panguan(18116688811)
        panguan(18116688822)
        panguan(18145608526)
        panguan(19436266629)
        panguan(14100099991)
        panguan(18017700603)
        panguan(18017700605)
        panguan(18017700610)
        panguan(18901156158)
        panguan(18929597700)
        panguan(18575823673)
        panguan(15353993082)
        panguan(13223986738)
        panguan(17767380753)
        panguan(13200500500)
        panguan(18017700715)
        panguan(18017700515)
        panguan(18017700516)
        panguan(18017700530)
        panguan(18017700597)
        panguan(18017700595)
        panguan(18017700550)
        panguan(18017700602)
        panguan(18930223547)  # 末凉
        panguan(18017700537)
        # tak
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
        panguan(17946568789)
        panguan(19412085993)
        panguan(18782323016)
        panguan(19850838555)
        panguan(19850000111)
        panguan(14987655547)
        panguan(18500071700)
        panguan(17445218012)
        panguan(16934710574)
        panguan(19492460960)

########################################################################################################################
finally2 = "\033[1;31m全部执行完毕：\033[0m " + time.strftime('%H:%M:%S')
print(finally2)
driver.back()
driver.back()
