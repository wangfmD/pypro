# coding = utf-8
from selenium import webdriver
import time
browser = webdriver.Firefox()

url = 'http://10.1.0.52/middlecas/login?service=http://10.1.0.52:8080/middleresource/shiro-cas'
print "now access %s" % (url)
browser.get(url)
time.sleep(2)

browser.find_element_by_id('s_username').send_keys('administrator')
browser.find_element_by_id('s_password').send_keys('xungejiaoyu')
browser.find_element_by_name('submit').click();

time.sleep(20)

browser.quit()
