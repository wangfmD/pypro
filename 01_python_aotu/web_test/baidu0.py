from selenium import webdriver
from time import sleep

driver = webdriver.Firefox()
driver.get('http://mail.126.com/')

# driver.find_element_by_xpath("//input[@id='auto-id-1472138193845']").send_keys('haoseanvv')
# j-inputtext dlemail
driver.find_element_by_name("email").click()
driver.find_element_by_name("email").clear()
driver.find_element_by_name("email").send_keys("haoseanvv")
driver.find_element_by_name("password").clear()
driver.find_element_by_name("password").send_keys("1111")
driver.find_element_by_id("dologin").click()
# driver.find_element_by_xpath("//input[@class='j-inputtext dlemail']").send_keys('haoseanvv')

sleep(40)
