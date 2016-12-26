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


class ConfInteract(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "http://10.1.0.56"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_conf_interact(self):
        driver = self.driver
        driver.get(self.base_url + "/interact/login.do")
        driver.find_element_by_id("username").clear()
        driver.find_element_by_id("username").send_keys("adminstrator")
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys("xungejiaoyu")
        driver.find_element_by_id("buttlogin").click()
        driver.find_element_by_id("username").clear()
        driver.find_element_by_id("username").send_keys("administrator")
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys("xungejiaoyu")
        driver.find_element_by_id("buttlogin").click()
        driver.find_element_by_id("sysconfig").click()
        driver.find_element_by_xpath("//table[@id='table']/tbody/tr[2]/td[3]/a/i").click()
        driver.find_element_by_id("value").clear()
        driver.find_element_by_id("value").send_keys("10.1.0.56")
        driver.find_element_by_xpath("(//button[@type='button'])[4]").click()
        driver.find_element_by_id("sysmiddlewarelocal").click()
        driver.find_element_by_id("addLocal").click()
        driver.find_element_by_xpath("(//input[@name='text'])[2]").click()
        driver.find_element_by_id("determines").click()
        driver.switch_to_alert().accept()
        # self.assertEqual(u"添加成功！", self.close_alert_and_get_its_text())
        driver.find_element_by_css_selector(u"button[title=\"设为本地连接中间件\"]").click()
        driver.switch_to_alert().accept()
        # self.assertEqual(u"修改成功！", self.close_alert_and_get_its_text())
        driver.find_element_by_css_selector(u"button[title=\"手动连接中间件\"]").click()
        # self.assertEqual(u"操作成功！", self.close_alert_and_get_its_text())
        driver.switch_to_alert().accept()

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
