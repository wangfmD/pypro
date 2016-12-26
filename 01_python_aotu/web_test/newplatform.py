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


class Newplatform(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://10.1.0.47/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_newplatform(self):
        driver = self.driver
        driver.get(self.base_url + "/middleclient/index.do")
        driver.find_element_by_link_text(u"系统管理").click()
        driver.find_element_by_link_text(u"租户管理").click()
        driver.find_element_by_css_selector("i.fa.fa-plus").click()
        driver.find_element_by_css_selector("#areaId > div.col-sm-9 > input.form-control").click()
        driver.find_element_by_xpath("//div[@id='treeview']/ul/li[17]").click()
        driver.find_element_by_css_selector("div.modal-content > div.text-center > button.btn.btn-success").click()
        driver.find_element_by_css_selector("#platmarkName > div.col-sm-9 > input.form-control").clear()
        driver.find_element_by_css_selector("#platmarkName > div.col-sm-9 > input.form-control").send_keys(u"河南教育局")
        driver.find_element_by_css_selector("#platmarkCode > div.col-sm-9 > input.form-control").clear()
        driver.find_element_by_css_selector("#platmarkCode > div.col-sm-9 > input.form-control").send_keys("001")
        driver.find_element_by_id("submit").click()
        driver.find_element_by_id("insertten").click()

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException as e:
            return False
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
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
