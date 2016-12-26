# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class AddInteract(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://10.1.0.56/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_add_interact(self):
        driver = self.driver
        driver.get(self.base_url + "/middleclient/;JSESSIONID=4398f2ff-aa1b-4b03-9d5e-e83d9c5fd49b")
        driver.find_element_by_xpath("//div[@id='div_menu']/ul/li[3]/a/span").click()
        driver.find_element_by_link_text(u"中心设备").click()
        driver.find_element_by_id("xiaoximiddleware").click()
        driver.find_element_by_css_selector("#addmiddleware > i.fa.fa-plus").click()
        driver.find_element_by_id("host").clear()
        driver.find_element_by_id("host").send_keys("10.1.0.56")
        driver.find_element_by_id("port").clear()
        driver.find_element_by_id("port").send_keys("80")
        driver.find_element_by_id("username").clear()
        driver.find_element_by_id("username").send_keys("administrator")
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys("xungejiaoyu")
        driver.find_element_by_id("insertmiddleware").click()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
