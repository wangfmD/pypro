# coding = utf-8
from selenium import webdriver
import time

browser = webdriver.Chrome()
# base_url = "http://10.1.0.44/middlecas/login"
# url = "?service=http://10.1.0.44:8080/middleresource/shiro-cas"
base_url = 'http://10.1.0.44'
url = '/middleclient/index.do'
print "now access %s" % (base_url + url)
browser.get(base_url + url)
time.sleep(2)
select = browser.find_element_by_tag_name("select")
allOptions = select.find_elements_by_tag_name("option")
# for option in allOptions:
#    print "Value is: " + option.get_attribute("value")
for option in allOptions:
    if option.get_attribute('value') == '94004b13-6d67-4339-9816-5b728066e35a':
        option.click()
browser.find_element_by_id('s_username').send_keys('jssadmin')
browser.find_element_by_id('s_password').send_keys('111111')

browser.find_element_by_name('submit').click()

time.sleep(5)
# browser.quit()
