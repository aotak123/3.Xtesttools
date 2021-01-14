# coding=utf-8

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.common.exceptions import NoSuchElementException
import time
import urllib.request
import ssl

capabilities = {}
capabilities['platformName'] = 'Android'  # Android平台测试
capabilities['platformVersion'] = '8.0.0'
capabilities['deviceName'] = 'EVA-AL10'
capabilities['appPackage'] = 'com.kamitu.drawsth.standalone.free.android'  # 系统手机中的联系人app的包名
capabilities['appActivity'] = 'com.qsmy.busniess.welcome.WelcomeActivity'  # 系统手机中的联系人app的主入口activity
capabilities['noReset'] = 'true'  # 不重置app
capabilities['autoAcceptAlerts'] = 'true'
capabilities['autoWebview'] = 'false'
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', capabilities)  # 连接测试所在服务器
context = ssl._create_unverified_context()

'''
block list添加 https://sign.crazyccy.com:443/index/index
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
        print("自动登录成功")
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
        time.sleep(1)
        TouchAction(driver).tap(x=530, y=844).perform()  # 确定按钮登录
        print("账号登录成功")
    time.sleep(10)  # 等待加载进入首页
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
        try:
            GDT = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:xml/gdt_file_path")
        except NoSuchElementException:
            BB = "  \033[1;31mNO.\033[0m " + str(a) + " toutiaosdk广告"
            print(BB)
            time.sleep(45)
            TouchAction(driver).tap(x=964, y=101).perform()  # 关闭toutiao广告
            # print("     toutiaosdk广告关闭")
        else:
            CC = "  \033[1;31mNO.\033[0m " + str(a) + " GDTsdk广告"
            print(CC)
            time.sleep(55)
            driver.back()  # GDTsdk广告按钮
            # print("     GDTsdk广告关闭")
        a += 1
    # 退出广告循环
    time.sleep(10)
    driver.back()  # 判官回到首页
    time.sleep(2)
    # 退出账号
    TouchAction(driver).tap(x=422, y=120).perform()  # 返回进入个人中心
    time.sleep(2)
    TouchAction(driver).tap(x=960, y=186).perform()  # 点击设置
    time.sleep(2)
    # 退出前清理缓存
    # TouchAction(driver).tap(x=723, y=547).perform()  # 点击清理
    # time.sleep(1)
    # TouchAction(driver).tap(x=960, y=1440).perform()  # 弹窗确定清理
    # time.sleep(1)
    TouchAction(driver).tap(x=492, y=1777).perform()  # 点击退出
    time.sleep(2)
    TouchAction(driver).tap(x=712, y=1014).perform()  # 弹窗确定退出


########################################################################################################################
if __name__ == '__main__':
    panguan(18600007117)  # NO.01
    panguan(18780000008)  # NO.02
    panguan(18637605801)  # NO.03
    panguan(17752939592)  # NO.04
    panguan(18131526059)  # NO.05
    panguan(15660925537)  # NO.06
    panguan(17538253260)  # NO.07
    panguan(19825052192)  # NO.08
    panguan(19825805208)  # NO.09
    panguan(13122027777)  # NO.10
    panguan(18222851111)  # NO.11
    panguan(18222222222)  # NO.12
    panguan(19876543210)  # NO.13
    panguan(18234567890)  # NO.14
    panguan(17857577938)  # NO.15
    panguan(18321273743)  # NO.16
    panguan(18519820628)  # NO.17
    panguan(18575823673)  # NO.18
    panguan(18681025732)  # NO.19
    panguan(18819123459)  # NO.20
    panguan(18901156158)  # NO.21
    panguan(18920308799)  # NO.22
    panguan(18929597700)  # NO.23
    panguan(18930223547)  # NO.24 末凉
    panguan(19882152576)  # NO.25
    panguan(15895663333)  # NO.26
    panguan(13918122777)  # NO.27
    panguan(13223986738)  # NO.28
    panguan(17767380753)  # NO.29
    panguan(13200500500)  # NO.30
    panguan(13200500001)  # NO.31
    panguan(13079188626)  # NO.32
    panguan(17260878175)  # NO.33
    panguan(19813758251)  # NO.34
    panguan(17261803056)  # NO.35
    panguan(19529759329)  # NO.36
    panguan(17538519737)  # NO.37
    panguan(13529021576)  # NO.38
    panguan(18987872800)  # NO.39
    panguan(18917779999)  # NO.40
    panguan(13761113333)  # NO.41
    panguan(13985622222)  # NO.42
    panguan(13763333333)  # NO.43
    panguan(13698521470)  # NO.44
    panguan(13760000001)  # NO.45
    panguan(17729152205)  # NO.46
    panguan(19850838555)  # NO.47
    panguan(19850000111)  # NO.48
    panguan(15237371035)  # NO.49
    panguan(18508071757)  # NO.50

########################################################################################################################
finally2 = "\033[1;31m全部执行完毕：\033[0m " + time.strftime('%H:%M:%S')
print(finally2)
driver.back()
driver.back()
