# coding=utf-8

from selenium import webdriver
# from appium import webdriver
import urllib.request
import unittest
import ssl
from selenium.common.exceptions import NoSuchElementException
import time
import HTMLTestRunner

capabilities = {}
# ios虚拟机测试
capabilities['platformName'] = 'ios'
capabilities['deviceName'] = 'aotak的iPhone'
capabilities['bundleId'] = 'com.chengyu.new.one'
# capabilities['deviceName'] = 'iPhone' # 虚拟机
# capabilities['platformVersion'] = '13.5'# 虚拟机
# capabilities['udid'] = '498F9D3E-C9F5-4188-B0DE-0CBCA9C79609' # 虚拟机
capabilities['platformVersion'] = "13.4.1" # 7p
capabilities['udid'] = '1bf56fd27e946673faf8e787e07e6c632b21425e' # 7p
capabilities['automationName'] = 'XCUITest'
# capabilities['mobile'] = '18017700111'
# capabilities['app'] = '/Users/aotak/Desktop/CrazyIdiomSimulator.app'
capabilities['xcodeSigningId'] = 'iPhone Developer'
# capabilities['xcodeOrgId'] = 'Jun yi Hu'
capabilities['updatedWDABundleId'] = 'com.facebeek.WebDriverAgentRunner'
capabilities['useNewWDA'] = 'true'
capabilities['autoLaunch'] = 'false'
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', capabilities)
mobile = "18017700111"  # capabilities['mobile']
context = ssl._create_unverified_context()


class CaseTest(unittest.TestCase):
    # @classmethod
    # def setUpClass(cls):
    #     print('开始测试')

    # def setUp(self):
    #     print('')

    def check_login(self):
        try:
            check_login = driver.find_element_by_accessibility_id("手机登录")
        except NoSuchElementException:
            print("无需登录")
        else:
            check_login.click()
            el2 = driver.find_element_by_xpath(
                "//XCUIElementTypeApplication[@name=\"CrazyIdiomSimulator\"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTextField[1]")
            el2.send_keys(mobile)
            el3 = driver.find_element_by_xpath("//XCUIElementTypeStaticText[@name=\"获取验证码\"]")
            el3.click()
            time.sleep(2)
            logincodeurl = "https://uc.crazyccy.com/login/main_login/testtool?key=sLQq2_jaKLknsqAwZ&type=1&mobile=" + mobile
            print(logincodeurl)
            request = urllib.request.Request(logincodeurl)  # 构建请求url
            response = urllib.request.urlopen(request, context=context)  # ssl证书免验证加入,context = context# 打开请求url链接
            num = response.read()  # 读取页面返回信息，python3返回数据为bytes类型的对象 (即b为前缀, bytes类型)
            logincode = num.decode()
            if logincode == "查不到！":
                print("未获取到验证码!")
            el4 = driver.find_element_by_xpath(
                "//XCUIElementTypeApplication[@name=\"CrazyIdiomSimulator\"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTextField[2]")
            time.sleep(2)
            el4.send_keys(logincode)
            driver.get_screenshot_as_file("/Users/aotak/Documents/autotest/登录.png")
            el5 = driver.find_element_by_xpath("//XCUIElementTypeButton[@name=\"确定\"]")
            el5.click()
            print("登录成功")
        time.sleep(2)

    def check_newred(self):
        try:
            check_newred = driver.find_element_by_accessibility_id("恭喜获得新人奖励红包")
        except NoSuchElementException:
            print("无新人红包")
        else:
            check_newred = driver.find_element_by_accessibility_id("NewUserRedPacket close")
            driver.get_screenshot_as_file("/Users/aotak/Documents/autotest/新人红包.png")
            check_newred.click()
            print("新人红包关闭")
        time.sleep(2)

    def check_Sign_reminder(self):
        try:
            check_Sign_reminder = driver.find_element_by_accessibility_id("开启签到提醒")
        except NoSuchElementException:
            print("无签到提示")
        else:
            check_Sign_reminder = driver.find_element_by_accessibility_id("SignRemind close")
            driver.get_screenshot_as_file("/Users/aotak/Documents/autotest/签到提醒.png")
            check_Sign_reminder.click()
            print("签到提示关闭")
        time.sleep(2)

    def check_Sign(self):
        try:
            check_Sign = driver.find_element_by_xpath("//XCUIElementTypeStaticText[@name=\"每日签到领奖励\"]")
        except NoSuchElementException:
            print("无签到弹窗")
        else:
            check_Sign = driver.find_element_by_xpath(
                "//XCUIElementTypeApplication[@name=\"CrazyIdiomSimulator\"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeButton[2]")
            driver.get_screenshot_as_file("/Users/aotak/Documents/autotest/每日签到弹窗.png")
            check_Sign.click()
            print("每日签到关闭")
        time.sleep(2)
        now = time.strftime('%Y-%m-%d%-%H:%M:%S')  # 获取当前时间
        driver.get_screenshot_as_file("/Users/aotak/Documents/autotest/"+now+"首页.png")

    # def tearDown(self):
    #     print('')

    # @classmethod
    # def tearDownClass(cls):
    #     print('\n测试结束')


if __name__ == '__main__':
    # print('hello 123')
    # unittest.main()
    suite = unittest.TestSuite()
    suite.addTest(CaseTest('check_login'))
    suite.addTest(CaseTest('check_newred'))
    suite.addTest(CaseTest('check_Sign_reminder'))
    suite.addTest(CaseTest('check_Sign'))
    # unittest.TextTestRunner().run(suite)
    nowtime = time.strftime('%Y-%m-%d')  # 获取当前时间
    html_file = "/Users/aotak/Documents/autotest/" + nowtime + "报告.html"
    fp = open(html_file, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        title=u'疯狂猜成语自动化登录检测',
        description=u'用例执行情况:')
    runner.run(suite)
    fp.close()

# check_login()
# time.sleep(3)
# check_newred()
# time.sleep(3)
# check_Sign_reminder()
# time.sleep(3)
# check_Sign()
# time.sleep(3)


# TouchAction(driver).tap(x=296, y=102).perform()  # 点击空白区域,关闭不必要的H5弹窗
# time.sleep(2)
# TouchAction(driver).tap(x=112, y=620).perform()  # 打开小判官
# time.sleep(2)
# TouchAction(driver).tap(x=191, y=352).perform()  # 点击开始游戏,等待15秒
# time.sleep(15)
# a = 10
# while a > 0:
#     TouchAction(driver).tap(x=177, y=458).perform()  # 点击查看广告,等待30秒
#     time.sleep(30)
#     TouchAction(driver).tap(x=44, y=50).perform()  # 点击关闭按钮,等待10秒再出弹窗
#     time.sleep(10)
#     a -= 1

# now = time.strftime('%Y-%m-%d% %H:%M:%S')  # 获取当前时间
# fp = open("./report"+ now +"result.html", 'wb')
# runner = HTMLTestRunner(stream=fp, title=check_login, description=check_Sign)
# runner.run(check_login)
# fp.close()
