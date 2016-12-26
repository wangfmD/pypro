# coding = utf-8
from selenium import webdriver
import time
from selenium.webdriver.support.select import Select

browser = webdriver.Firefox()
url = 'http://10.1.0.52/middlecas/login?service=http://10.1.0.52:8080/middleresource/shiro-cas'
print "now access %s" % (url)
browser.get(url)
time.sleep(2)
sel = browser.find_element_by_xpath("//select[@id='platform']")
Select(sel).select_by_value('1b5dd0fd-df88-4241-ade7-47283e63ef75')
