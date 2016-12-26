# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class Shangke2(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://10.1.0.56/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_shangke2(self):
        driver = self.driver
        driver.get(self.base_url + "/middleclient/pcManager/LessonPage.do?typeCode=1401&lessonId=9a1545de-9f78-42a3-aa49-deb2a7920446&isZhu=1&classroomId=2e01ebe7-e8a0-45e5-b9fa-25af144b856d&interactType=false&created=0")
        driver.find_element_by_xpath("(//button[@id='requestConn_0001'])[2]").click()
        driver.find_element_by_xpath("(//button[@id='requestConn_0001'])[3]").click()
        driver.find_element_by_css_selector("#uniqueId_VR2110105029-2744-2_conId0001mcuProductSNsVR2110105029 > div.video-item.connect > div.control-bar > a.video_a > #requestConn_0001").click()
        driver.find_element_by_xpath("(//button[@id='requestConn_0001'])[4]").click()
        driver.find_element_by_css_selector("#uniqueId_VR2110105029-2744-3_conId0001mcuProductSNsVR2110105029 > div.video-item.connect > div.control-bar > a.video_a > #requestConn_0001").click()
        driver.find_element_by_xpath("(//button[@id='requestConn_0001'])[5]").click()
        driver.find_element_by_css_selector("#uniqueId_VR2110105029-2744-4_conId0001mcuProductSNsVR2110105029 > div.video-item.connect > div.control-bar > a.video_a > #requestConn_0001").click()
        driver.find_element_by_xpath("(//button[@id='requestConn_0001'])[6]").click()
    
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
