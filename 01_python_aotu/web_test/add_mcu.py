# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class AddMcu(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://10.1.0.56/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_add_mcu(self):
        driver = self.driver
        driver.get(self.base_url + "/middleclient/index.do")
        driver.find_element_by_link_text(u"设备管理").click()
        driver.find_element_by_link_text(u"中心设备").click()
        driver.find_element_by_css_selector("i.fa.fa-plus").click()
        driver.find_element_by_id("mcuAreaName").click()
        driver.find_element_by_css_selector("li.list-group-item.node-treeview").click()
        driver.find_element_by_id("equipmentName").clear()
        driver.find_element_by_id("equipmentName").send_keys("10.1.0.85")
        driver.find_element_by_id("equipIpAddr").clear()
        driver.find_element_by_id("equipIpAddr").send_keys("10.1.0.85")
        driver.find_element_by_id("mcu_port").clear()
        driver.find_element_by_id("mcu_port").send_keys("80")
        driver.find_element_by_id("mcuLoginName").clear()
        driver.find_element_by_id("mcuLoginName").send_keys("POLYCOM")
        driver.find_element_by_id("mcuPasswd").clear()
        driver.find_element_by_id("mcuPasswd").send_keys("POLYCOM")
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
