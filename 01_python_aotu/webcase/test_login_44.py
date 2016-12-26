# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re


class TestLogin44(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "http://10.1.0.44"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_login44(self):
        driver = self.driver
        driver.get(self.base_url + "/middleclient/index.do")
        Select(driver.find_element_by_id("platform")).select_by_visible_text(
            u"江苏教育局")
        driver.find_element_by_id("s_username").clear()
        driver.find_element_by_id("s_username").send_keys("jssadmin")
        driver.find_element_by_id("s_password").clear()
        driver.find_element_by_id("s_password").send_keys("111111")
        driver.find_element_by_name("submit").click()


if __name__ == "__main__":
    unittest.main()
