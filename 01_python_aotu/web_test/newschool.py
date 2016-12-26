# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class Newschool(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://10.1.0.47/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_newschool(self):
        driver = self.driver
        driver.get(self.base_url + "/middleclient/index.do")
        driver.find_element_by_id("addSchool").click()
        Select(driver.find_element_by_css_selector("select.form-control")).select_by_visible_text(u"高中")
        driver.find_element_by_css_selector("#schoolName > div.col-sm-9 > input.form-control").clear()
        driver.find_element_by_css_selector("#schoolName > div.col-sm-9 > input.form-control").send_keys(u"郑州一中")
        driver.find_element_by_id("submit").click()
    
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
