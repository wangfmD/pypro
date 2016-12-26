# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest
import time
import re

# http://10.1.0.44/middlecas/login?service=http://10.1.0.44/middleresource/index.do
driver = webdriver.Chrome()
driver.implicitly_wait(30)
base_url = "http://10.1.0.44"
verificationErrors = []
accept_next_alert = True
driver = driver
driver.get(
    base_url + "/middlecas/login?service=http://10.1.0.44/middleresource/index.do")
Select(driver.find_element_by_id("platform")
       ).select_by_visible_text(u"江苏教育局")
driver.find_element_by_id("s_username").clear()
driver.find_element_by_id("s_username").send_keys("jssadmin")
driver.find_element_by_id("s_password").clear()
driver.find_element_by_id("s_password").send_keys("111111")
driver.find_element_by_name("submit").click()
time.sleep(10)
