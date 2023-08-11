from selenium import webdriver
from selenium.webdriver.common.by import By
import time
# 在这里先打开一个浏览器的范围地址，设置为自动化打开模式。
# 打开ChromeDriver下载地址：http://chromedriver.storage.googleapis.com/index.html
url = 'https://www.chainflix.net/'
# url = 'https://www.baidu.com/'
# 然后再打开浏览器所在的地址
driver = webdriver.Chrome()
# 最后打开浏览器，并访问设置的网址。
driver.get(url)
time.sleep(5)
print("等待加载完成")
# element = driver.find_element_by_id('kw')
# element.send_keys('白月黑羽')
# driver.find_element_by_id('su').click()
first_login = driver.find_element_by_xpath("/html/body/div[3]/div[1]/div[4]/span")
first_login.click()


# driver.find_element(By.XPATH, '//a[@class="ma-0 v-icon v-icon notranslate v-icon--is-component theme--light my-icon videoNext"]').click()