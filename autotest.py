# coding=utf-8
# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python


from appium import webdriver

caps = {}
caps["platformName"] = "Android"
caps["platformVersion"] = "10"
caps["deviceName"] = "JSN-AL00"
caps["appPackage"] = "com.kamitu.drawsth.standalone.free.android"
caps["appActivity"] = "com.qsmy.busniess.welcome.WelcomeActivity"
caps["noReset"] = "false"
caps["autoAcceptAlerts"] = "ture"
caps["autoWebview"] = "false"

driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)

el1 = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/my")
el1.click()
el2 = driver.find_element_by_id("com.android.permissioncontroller:id/permission_allow_button")
el2.click()
el2.click()
el3 = driver.find_element_by_id("com.android.permissioncontroller:id/permission_allow_foreground_only_button")
el3.click()
el4 = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/pi")
el4.click()
el5 = driver.find_element_by_id("com.kamitu.drawsth.standalone.free.android:id/q8")
el5.click()

driver.quit()