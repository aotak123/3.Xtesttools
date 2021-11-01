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
    time.sleep(3)
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
        time.sleep(1)
        # 选择手机号输入框
        edit_mobile = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/edit_phone")
        edit_mobile.send_keys(mobile)
        time.sleep(1)
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
        time.sleep(1)
        edit_code.send_keys(logincode)
        time.sleep(2)
        TouchAction(driver).tap(x=530, y=844).perform()  # 确定按钮登录
        print("...账号登录成功")
    else:
        TouchAction(driver).tap(x=391, y=1591).perform()  # 点击手机号登录
        time.sleep(1)
        # 选择手机号输入框
        edit_mobile = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/edit_phone")
        edit_mobile.send_keys(mobile)
        time.sleep(1)
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
        time.sleep(1)
        edit_code.send_keys(logincode)
        time.sleep(2)
        TouchAction(driver).tap(x=530, y=844).perform()  # 确定按钮登录
        print("账号登录成功")
    time.sleep(13)  # 等待加载进入首页
    # 进入判官进行刷广告
    TouchAction(driver).tap(x=321, y=1665).perform()  # 选择进入判官
    time.sleep(3)
    TouchAction(driver).tap(x=546, y=941).perform()  # 选择开始挑战
    time.sleep(3)
    a = 1
    while a <= 11:
        time.sleep(8)
        TouchAction(driver).tap(x=503, y=1254).perform()  # 点击查看广告
        time.sleep(5)
        BB = "  \033[1;31mNO.\033[0m " + str(a) + " toutiaosdk广告"
        print(BB)
        os.popen(
            "adb -s KWG5T16928033201 shell am start -n com.kamitu.drawsth.standalone.free.android/com.qsmy.busniess.welcome.WelcomeActivity")
        time.sleep(35)
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
        panguan(14987657315)
        panguan(14987658206)
        panguan(16188856230)
        panguan(17927666394)
        panguan(16873572639)
        panguan(14987659197)
        panguan(14987656456)
        panguan(14987657365)
        panguan(14629177373)
        panguan(14261015450)
        panguan(17429725866)
        panguan(19555949829)
        panguan(14044236804)
        panguan(17447230115)
        panguan(16870465904)
        panguan(17426240088)
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
        # tak
        # 臀臀
        panguan(18017700607)
        panguan(18017700608)
        panguan(19882152576)
        panguan(17260878175)
        panguan(13161057579)
        panguan(15173160505)
        panguan(18180868581)
        panguan(18027328833)
        panguan(17318102888)
        panguan(15823382766)
        panguan(15850670782)
        panguan(13666088775)
        panguan(13683351952)
        panguan(13255615265)
        panguan(13032337272)
        panguan(17322190031)
        panguan(13720031029)
        panguan(18519820628)
        panguan(18022503751)
        panguan(15528939076)
        panguan(15895663333)
        panguan(13918122777)
        panguan(18116699000)
        panguan(14221102560)
        panguan(14110000038)
        panguan(14110003238)
        panguan(18920308799)
        panguan(14120006233)
        panguan(14140001001)
        panguan(14150002649)
        panguan(14160003558)
        panguan(14170004437)
        panguan(14180005326)
        panguan(14190006235)
        panguan(13666088700)
        panguan(13161057550)
        panguan(13062803788)
        panguan(19099990000)
        panguan(19088881111)
        panguan(19088882020)
        panguan(19088885672)
        panguan(18017700716)
        panguan(18017700713)
        panguan(16016000001)
        panguan(17538519737)
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
        panguan(13200500001)
        panguan(19813758251)
        panguan(17261803056)
        panguan(14017700111)
        panguan(18100011111)
        panguan(13402063488)
        panguan(15721403717)
        panguan(18321273743)
        # 臀臀


########################################################################################################################
finally2 = "\033[1;31m全部执行完毕：\033[0m " + time.strftime('%H:%M:%S')
print(finally2)
driver.back()
driver.back()
