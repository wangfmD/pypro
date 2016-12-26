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


class AddLive1(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "http://10.1.0.44"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_add_live1(self):
        driver = self.driver
        driver.get(
            self.base_url + "/middlecas/login?service=http://10.1.0.44:8080/middleclient/shiro-cas")
        Select(driver.find_element_by_id("platform")
               ).select_by_visible_text(u"江苏教育局")
        driver.find_element_by_id("s_username").clear()
        driver.find_element_by_id("s_username").send_keys("jssadmin")
        driver.find_element_by_id("s_password").clear()
        driver.find_element_by_id("s_password").send_keys("111111")
        driver.find_element_by_name("submit").click()
        driver.find_element_by_link_text(u"内容管理").click()
        driver.find_element_by_link_text(u"直播管理").click()
        driver.find_element_by_xpath(
            "//div[@id='main-container']/div/div[2]/div/div[2]/div/button[3]").click()
        driver.find_element_by_id("addList").click()
        driver.find_element_by_css_selector(
            "span.glyphicon.glyphicon-time").click()
        driver.find_element_by_xpath(
            "//div[@id='sizzle1468213061064']/div[3]/table/tbody/tr[6]/td").click()
        driver.find_element_by_css_selector("span.hour.active").click()
        driver.find_element_by_css_selector("span.minute").click()
        driver.find_element_by_xpath(
            "//div[@id='formrole']/div/div/div[2]/div/div/span[2]/span").click()
        driver.find_element_by_xpath(
            "//div[@id='sizzle1468213061064']/div[3]/table/tbody/tr[6]/td").click()
        driver.find_element_by_css_selector(
            "#sizzle1468213061064 > div.datetimepicker-hours > table..table-condensed > tbody > tr > td > span.hour.active").click()
        driver.find_element_by_xpath(
            "//div[@id='sizzle1468213061064']/div/table/tbody/tr/td/span[12]").click()
        driver.find_element_by_id("sd_url").clear()
        driver.find_element_by_id("sd_url").send_keys("http://")
        driver.find_element_by_id("sureAdd").click()
        driver.find_element_by_id("pdLession_id").clear()
        driver.find_element_by_id("pdLession_id").send_keys("liveplay1")
        driver.find_element_by_id("sureAdd").click()

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

    # def close_alert_and_get_its_text(self):
    #     try:
    #         alert = self.driver.switch_to_alert()
    #         alert_text = alert.text
    #         if self.accept_next_alert:
    #             alert.accept()
    #         else:
    #             alert.dismiss()
    #         return alert_text
    #     finally:
    #         self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
