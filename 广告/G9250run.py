# coding=utf-8

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.common.exceptions import NoSuchElementException
import time
import urllib.request
import ssl

capabilities = {}
capabilities['platformName'] = 'Android'  # Android平台测试
# 三星
capabilities['platformVersion'] = '6.0.1'
capabilities['deviceName'] = 'SM-G9250'
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
        TouchAction(driver).tap(x=515, y=2300).perform()  # 点击手机号登录
        time.sleep(1)
        edit_mobile = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/edit_phone")  # 选择手机号输入框
        edit_mobile.send_keys(mobile)
        time.sleep(1)
        TouchAction(driver).tap(x=1100, y=870).perform()  # 获取验证码
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
            TouchAction(driver).tap(x=1100, y=870).perform()  # 获取验证码
            time.sleep(2)  # 获取验证码
            request = urllib.request.Request(logincodeurl)  # 构建请求url
            response = urllib.request.urlopen(request, context=context)  # ssl证书免验证加入,context = context# 打开请求url链接
            num = response.read()  # 读取页面返回信息，python3返回数据为bytes类型的对象 (即b为前缀, bytes类型)
            logincode = num.decode()
        edit_code = driver.find_element_by_id(
            "com.kamitu.drawsth.standalone.free.android:id/edit_identifyCode")  # 选择验证码输入框
        time.sleep(1)
        edit_code.send_keys(logincode)
        time.sleep(1)
        TouchAction(driver).tap(x=700, y=1200).perform()  # 确定按钮登录
        print("账号登录成功")
    time.sleep(15)  # 等待加载进入首页
    # 检查是否弹出每日签到弹窗
    try:
        check_signwindows = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/iv_signin_get")
    except NoSuchElementException:
        print("无每日签到弹窗")
    else:
        TouchAction(driver).tap(x=1270, y=655).perform()  # 关闭每日签到弹窗
        time.sleep(2)
    # 进入接龙主游戏页面
    TouchAction(driver).tap(x=707, y=2070).perform()  # 进入接龙页面
    time.sleep(2)
    driver.back()
    time.sleep(2)
    # 检查是否弹出签到提示
    try:
        check_signtoast = driver.find_element_by_id(
            "com.kamitu.drawsth.standalone.free.android:id/iv_checkin_reminder_close")
    except NoSuchElementException:
        print("无签到提示弹窗")
    else:
        TouchAction(driver).tap(x=1228, y=748).perform()  # 关闭签到提示弹窗
        time.sleep(2)
    # 进入判官进行刷广告
    TouchAction(driver).tap(x=439, y=2379).perform()  # 选择进入判官
    time.sleep(1)
    TouchAction(driver).tap(x=712, y=1342).perform()  # 选择开始挑战
    time.sleep(3)
    a = 1
    while a <= 11:
        time.sleep(7)
        TouchAction(driver).tap(x=671, y=1734).perform()  # 点击查看广告
        time.sleep(5)
        try:
            GDT = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
        except NoSuchElementException:
            BB = "  \033[1;31mNO.\033[0m " + str(a) + " toutiaosdk广告"
            print(BB)
            time.sleep(35)
            TouchAction(driver).tap(x=1285, y=139).perform()  # 关闭toutiao广告
            print("     toutiaosdk广告关闭")
        else:
            CC = "  \033[1;31mNO.\033[0m " + str(a) + " GDTsdk广告"
            print(CC)
            time.sleep(55)
            driver.back()  # GDTsdk广告按钮
            print("     GDTsdk广告关闭")
        a += 1
    # 退出广告循环
    time.sleep(7)
    driver.back()  # 判官中回到首页
    time.sleep(2)
    # 退出账号
    TouchAction(driver).tap(x=588, y=186).perform()  # 返回进入个人中心
    time.sleep(2)
    TouchAction(driver).tap(x=1275, y=243).perform()  # 点击设置
    time.sleep(1)
    # TouchAction(driver).tap(x=723, y=547).perform()  # 点击清理
    # time.sleep(1)
    # TouchAction(driver).tap(x=960, y=1440).perform()  # 弹窗确定清理
    # time.sleep(1)
    TouchAction(driver).tap(x=707, y=2467).perform()  # 点击退出
    time.sleep(1)
    TouchAction(driver).tap(x=960, y=1440).perform()  # 弹窗确定退出


#############################################################################################################################################################

if __name__ == '__main__':
    panguan(13032337111)  # NO.01
    panguan(13161767110)  # NO.02
    panguan(13560736789)  # NO.03
    panguan(13651711999)  # NO.04
    panguan(15611828881)  # NO.05
    panguan(15917449818)  # NO.06
    panguan(15927257999)  # NO.07
    panguan(17502150079)  # NO.08
    panguan(18014400369)  # NO.09
    panguan(18017700207)  # NO.10
    panguan(18017700223)  # NO.11
    panguan(18017700339)  # NO.12   阿拉斯加加加加
    panguan(18017700400)  # NO.13
    panguan(18017700410)  # NO.14
    panguan(18017700411)  # NO.15
    panguan(18017700475)  # NO.16
    panguan(18017700477)  # NO.17
    panguan(18017700478)  # NO.18
    panguan(18017700533)  # NO.19
    panguan(18017700535)  # NO.20
    panguan(18017700536)  # NO.21
    panguan(18017700540)  # NO.22
    panguan(18017700571)  # NO.23
    panguan(18017700580)  # NO.24   小糖糖2
    panguan(18017700596)  # NO.25
    panguan(18017700598)  # NO.26
    panguan(18017700600)  # NO.27
    panguan(18017700601)  # NO.28
    panguan(18017700604)  # NO.29
    panguan(18017700606)  # NO.30
    panguan(18017700710)  # NO.31   治疗失眠陶老师
    panguan(18503807583)  # NO.32
    panguan(18918024483)  # NO.33
    panguan(18930224047)  # NO.34
    panguan(19823637887)  # NO.35
    panguan(18017700355)  # NO.36
    panguan(18134508526)  # NO.37
    panguan(15611828882)  # NO.38
    panguan(13161057538)  # NO.39
    panguan(18085112222)  # NO.40
    panguan(15300900920)  # NO.41
    panguan(13164767109)  # NO.42
    panguan(13666088773)  # NO.43
    panguan(18616905709)  # NO.44
    panguan(13311936568)  # NO.45
    panguan(18601608165)  # NO.46
    panguan(18601608371)  # NO.47
    panguan(17710032752)  # NO.48
    panguan(18519880503)  # NO.49
    panguan(13520010705)  # NO.50
    panguan(13920051605)  # NO.51
    panguan(18622077306)  # NO.52

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
    panguan(18180868581)  # NO.29
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
    panguan(18575823673)  # NO.43
    panguan(18022503751)  # NO.44

#############################################################################################################################################################
finally2 = "\033[1;31m全部执行完毕：\033[0m " + time.strftime('%H:%M:%S')
print(finally2)
driver.back()
driver.back()
