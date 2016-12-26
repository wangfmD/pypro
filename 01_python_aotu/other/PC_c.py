# coding = utf-8
from selenium import webdriver
import time

browser = webdriver.Chrome()
url = 'http://10.1.0.52/middlecas/login?service=http://10.1.0.52:8080/middleresource/shiro-cas'
print "now access %s" % (url)
browser.get(url)
time.sleep(2)
select = browser.find_element_by_tag_name("select")
allOptions = select.find_elements_by_tag_name("option")
# for option in allOptions:
#    print "Value is: " + option.get_attribute("value")
for option in allOptions:
    if option.get_attribute('value') == '1b5dd0fd-df88-4241-ade7-47283e63ef75':
        option.click()
time.sleep(1)

browser.find_element_by_id('s_username').send_keys('jssadmin')
browser.find_element_by_id('s_password').send_keys('111111')
time.sleep(1)
browser.find_element_by_name('submit').click()

time.sleep(5)
browser.get('http://10.1.0.52/middleclient/pcManager/schoolPage.do')
# claz = browser.find_element_by_class_name('btn.btn-list')
button = browser.find_element_by_tag_name("button")
for btn in button:
    if btn.get_attribute('schoolname') == '大学A':
        option.click()
time.sleep(5)