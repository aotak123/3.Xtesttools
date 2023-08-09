from selenium import webdriver
from selenium.webdriver.common.by import By
import time
# 在这里先打开一个浏览器的范围地址，设置为自动化打开模式。
# 打开ChromeDriver下载地址：http://chromedriver.storage.googleapis.com/index.html
url = 'https://www.chainflix.net/video?contentId=359931'
# 然后再打开浏览器所在的地址
driver = webdriver.Chrome()
# 最后打开浏览器，并访问设置的网址。
driver.get(url)
time.sleep(5)
first_login = (By.XPATH, '//a[@class="ma-0 v-icon v-icon notranslate v-icon--is-component theme--light my-icon videoNext"]') # 切换
driver.find_element(*first_login).click()