# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class CfgMcu(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://10.1.0.56/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_cfg_mcu(self):
        driver = self.driver
        driver.get(self.base_url + "/middleclient/index.do#")
        driver.find_element_by_link_text(u"设备管理").click()
        driver.find_element_by_xpath("(//button[@id='current'])[2]").click()
        driver.find_element_by_xpath("//div[@id='AreaMcutreeview']/ul/li/span[3]").click()
        driver.find_element_by_id("saveAreaMcu").click()
        driver.find_element_by_id("xiaoximiddleware").click()
        driver.find_element_by_css_selector("i.fa.fa-server").click()
        driver.find_element_by_name("ckrelevmcuid").click()
        driver.find_element_by_id("saverelevmcumiddleware").click()
        driver.find_element_by_xpath("//table[@id='middlewaretable']/tbody/tr[2]/td[2]").click()
        driver.find_element_by_xpath("//table[@id='middlewaretable']/tbody/tr[2]/td[2]").click()
        driver.find_element_by_css_selector("i.fa.fa-bars").click()
        driver.find_element_by_css_selector("#listofschooltable > tr > td > input[type=\"checkbox\"]").click()
        driver.find_element_by_id("insertmiddlewareschool").click()
        driver.find_element_by_xpath("//table[@id='middlewaretable']/tbody/tr[2]/td[2]").click()
        driver.find_element_by_id("theschoollist").click()
    
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
