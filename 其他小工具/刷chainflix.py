from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

# 在这里先打开一个浏览器的范围地址，设置为自动化打开模式。
# 打开ChromeDriver下载地址：http://chromedriver.storage.googleapis.com/index.html
url = 'https://www.chainflix.net/'
# 然后再打开浏览器所在的地址
browser = webdriver.Chrome()
# 最后打开浏览器，并访问设置的网址。
browser.get(url)
browser.set_window_size(1320, 1000)
time.sleep(5)
print("等待加载完成")
ActionChains(browser).move_by_offset(1038, 516).click().perform()  # 鼠标左键点击
ActionChains(browser).move_by_offset(-1038, -516).perform()  # 将鼠标位置恢复到移动前
time.sleep(5)
print("可进行登录操作进入播放页")
"""手动登录"""
a = 1
while a > 0:
    print("  \033[1;31mNO.\033[0m " + str(a) + " 个视频")
    time.sleep(300)
    ActionChains(browser).move_by_offset(939, 734).click().perform()  # 鼠标左键点击
    ActionChains(browser).move_by_offset(-939, -734).perform()  # 将鼠标位置恢复到移动前
    a += 1

# driver.find_element(By.XPATH, '//a[@class="ma-0 v-icon v-icon notranslate v-icon--is-component theme--light my-icon videoNext"]').click()
