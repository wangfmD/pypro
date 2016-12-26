# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class Addterminal(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://10.1.0.47/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_addterminal(self):
        driver = self.driver
        driver.get(self.base_url + "/middleclient/index.do")
        driver.find_element_by_css_selector("#div_menu > ul.nav.nav-list > li > a.dropdown-toggle > span.menu-text").click()
        driver.find_element_by_link_text(u"学校管理").click()
        driver.find_element_by_link_text(u"30教室").click()
        driver.find_element_by_xpath(u"//a[contains(text(),'设备管理')]").click()
        driver.find_element_by_id("addterminal").click()
        driver.find_element_by_css_selector("div.modal-body > div > #name > div.col-sm-9 > input.form-control").clear()
        driver.find_element_by_css_selector("div.modal-body > div > #name > div.col-sm-9 > input.form-control").send_keys("10.1.0.30")
        Select(driver.find_element_by_css_selector("div.modal-body > div > #equipmentModel > div.col-sm-9 > select")).select_by_visible_text(u"Group系列")
        driver.find_element_by_css_selector("div.modal-body > div > #ipAddr > div.col-sm-9 > input.form-control").clear()
        driver.find_element_by_css_selector("div.modal-body > div > #ipAddr > div.col-sm-9 > input.form-control").send_keys("10.1.0.30")
        driver.find_element_by_css_selector("div.modal-body > div > #locAddr > div.col-sm-9 > input.form-control").clear()
        driver.find_element_by_css_selector("div.modal-body > div > #locAddr > div.col-sm-9 > input.form-control").send_keys("10.1.0.30")
        driver.find_element_by_css_selector("div.modal-body > div > #equipmentLogName > div.col-sm-9 > input.form-control").clear()
        driver.find_element_by_css_selector("div.modal-body > div > #equipmentLogName > div.col-sm-9 > input.form-control").send_keys("admin")
        driver.find_element_by_css_selector("div.modal-body > div > #equipmentLogPwd > div.col-sm-9 > input.form-control").clear()
        driver.find_element_by_css_selector("div.modal-body > div > #equipmentLogPwd > div.col-sm-9 > input.form-control").send_keys("admin")
        driver.find_element_by_css_selector("#terminal > div.modal-dialog > div.modal-content > #formrole > div.modal-body > div.text-center > #submit").click()
        driver.find_element_by_xpath("(//input[@name='isgk'])[2]").click()
    
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
