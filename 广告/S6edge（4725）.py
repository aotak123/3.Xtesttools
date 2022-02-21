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
    time.sleep(5)
    print("\033[1;31mProject.\033[0m " + str(mobile) + " \033[1;31mSTART\033[0m : " + time.strftime('%H:%M:%S'))
    # 登录模块
    try:
        check_login = driver.find_element_by_id(
            "com.kamitu.drawsth.standalone.free.android:id/iv_mobile_login")  # 选择手机号登录
    except NoSuchElementException:
        print("当前为自动登录模式...正在退出账号重新进行登录")
        time.sleep(10)  # 等待加载进入首页
        TouchAction(driver).tap(x=588, y=186).perform()  # 返回进入个人中心
        time.sleep(2)
        TouchAction(driver).tap(x=1275, y=243).perform()  # 点击设置
        time.sleep(2)
        TouchAction(driver).tap(x=707, y=2467).perform()  # 点击退出
        time.sleep(2)
        TouchAction(driver).tap(x=960, y=1440).perform()  # 弹窗确定退出
        time.sleep(3)
        TouchAction(driver).tap(x=515, y=2300).perform()  # 点击手机号登录
        time.sleep(2)
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
        time.sleep(2)
        edit_code.send_keys(logincode)
        time.sleep(2)
        TouchAction(driver).tap(x=700, y=1200).perform()  # 确定按钮登录
        print("...账号登录成功")
    else:
        TouchAction(driver).tap(x=515, y=2300).perform()  # 点击手机号登录
        time.sleep(2)
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
        time.sleep(2)
        edit_code.send_keys(logincode)
        time.sleep(2)
        TouchAction(driver).tap(x=700, y=1200).perform()  # 确定按钮登录
        print("账号登录成功")
    time.sleep(20)  # 等待加载进入首页
    # 进入判官进行刷广告
    TouchAction(driver).tap(x=439, y=2379).perform()  # 选择进入判官
    time.sleep(3)
    TouchAction(driver).tap(x=712, y=1342).perform()  # 选择开始挑战
    time.sleep(3)
    a = 1
    while a <= 11:
        time.sleep(10)
        TouchAction(driver).tap(x=671, y=1734).perform()  # 点击查看广告
        time.sleep(8)
        BB = "  \033[1;31mNO.\033[0m " + str(a) + " 次广告"
        print(BB)
        # os.popen("adb -s 02157df2c8865716 shell am start -n com.kamitu.drawsth.standalone.free.android/com.qsmy.busniess.welcome.WelcomeActivity")
        time.sleep(42)
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
        # os.popen("adb -s 02157df2c8865716 shell am force-stop com.kamitu.drawsth.standalone.free.android")
        time.sleep(2)
        # os.popen(
        #     "adb -s 02157df2c8865716 shell am start -n com.kamitu.drawsth.standalone.free.android/com.qsmy.busniess.welcome.WelcomeActivity")
        time.sleep(10)  # 等待加载进入首页
        TouchAction(driver).tap(x=588, y=186).perform()  # 返回进入个人中心
        time.sleep(2)
        TouchAction(driver).tap(x=1275, y=243).perform()  # 点击设置
        time.sleep(2)
        TouchAction(driver).tap(x=707, y=2467).perform()  # 点击退出
        time.sleep(2)
        TouchAction(driver).tap(x=960, y=1440).perform()  # 弹窗确定退出
    else:
        TouchAction(driver).tap(x=1275, y=243).perform()  # 点击设置
        time.sleep(2)
        TouchAction(driver).tap(x=707, y=2467).perform()  # 点击退出
        time.sleep(2)
        TouchAction(driver).tap(x=960, y=1440).perform()  # 弹窗确定退出


########################################################################################################################
if __name__ == '__main__':
    c = 1
    while c <= 2:
        # tak
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
        panguan(17939699208)
        panguan(19367241617)
        panguan(17476070492)
        panguan(16833601539)
        panguan(17938136012)
        panguan(19791239757)
        panguan(18017700533)
        panguan(18017700535)
        panguan(18017700477)
        panguan(18017700580)  # 小糖糖2
        panguan(18918024483)
        panguan(18017700596)
        panguan(18017700598)
        panguan(15917449818)
        panguan(13032337111)
        panguan(19823637887)
        panguan(18017700355)
        panguan(13161767110)
        panguan(13161057538)
        panguan(13164767109)
        panguan(14988888053)
        panguan(14988889962)
        panguan(14988887871)
        panguan(14988888780)
        panguan(14988889699)
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
        panguan(18601608165)
        # 臀臀
        panguan(18017700607)
        panguan(14017700111)
        panguan(18100011111)
        panguan(13402063488)
        panguan(15721403717)
        panguan(18321273743)
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
        panguan(19529759329)
        panguan(13529021576)
        panguan(18987872800)
        panguan(18917779999)
        panguan(13761113333)
        panguan(13985622222)
        panguan(13763333333)
        panguan(13698521470)
        panguan(13760000001)

########################################################################################################################
finally2 = "\033[1;31m全部执行完毕：\033[0m " + time.strftime('%H:%M:%S')
print(finally2)
driver.back()
driver.back()
