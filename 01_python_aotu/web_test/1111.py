# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class 1111(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://10.1.0.56/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_1111(self):
        driver = self.driver
        driver.get(self.base_url + "/middleclient/pcManager/LessonPage.do?typeCode=1401&lessonId=49148ad3-064c-4f37-a72e-d67c925753c8&isZhu=1&classroomId=2e01ebe7-e8a0-45e5-b9fa-25af144b856d&interactType=false&created=0")
        driver.find_element_by_id("pc_manager_container").click()
        driver.find_element_by_id("requestDisconn_0052").click()
        driver.find_element_by_id("requestDisconn_0052").click()
        driver.find_element_by_id("requestDisconn_0052").click()
        driver.find_element_by_id("requestDisconn_0052").click()
        driver.find_element_by_id("requestDisconn_0052").click()
        driver.find_element_by_id("requestDisconn_0052").click()
        driver.find_element_by_id("requestDisconn_0052").click()
        driver.find_element_by_id("requestDisconn_0052").click()
        driver.find_element_by_css_selector("#uniqueId_VR2110105029-2839-0_conId0052mcuProductSNsVR2110105029 > div.video-item.connect > div.control-bar > a.video_a > #requestDisconn_0052").click()
        driver.find_element_by_xpath("(//button[@id='requestDisconn_0052'])[2]").click()
        driver.find_element_by_css_selector("#uniqueId_VR2110105029-2839-3_conId0052mcuProductSNsVR2110105029 > div.video-item.connect > div.control-bar > a.video_a > #requestDisconn_0052").click()
        driver.find_element_by_xpath("(//button[@id='requestDisconn_0052'])[3]").click()
        driver.find_element_by_css_selector("#uniqueId_VR2110105029-2839-2_conId0052mcuProductSNsVR2110105029 > div.video-item.connect > div.control-bar > a.video_a > #requestDisconn_0052").click()
        driver.find_element_by_xpath("(//button[@id='requestDisconn_0052'])[4]").click()
        driver.find_element_by_css_selector("#uniqueId_VR2110105029-2839-1_conId0052mcuProductSNsVR2110105029 > div.video-item.connect > div.control-bar > a.video_a > #requestDisconn_0052").click()
        driver.find_element_by_xpath("(//button[@id='requestDisconn_0052'])[5]").click()
        driver.find_element_by_css_selector("#uniqueId_VR2110105029-2839-5_conId0052mcuProductSNsVR2110105029 > div.video-item.connect > div.control-bar > a.video_a > #requestDisconn_0052").click()
        driver.find_element_by_xpath("(//button[@id='requestDisconn_0052'])[6]").click()
        driver.find_element_by_css_selector("#uniqueId_VR2110105029-2839-4_conId0052mcuProductSNsVR2110105029 > div.video-item.connect > div.control-bar > a.video_a > #requestDisconn_0052").click()
        driver.find_element_by_xpath("(//button[@id='requestDisconn_0052'])[7]").click()
        driver.find_element_by_css_selector("#uniqueId_564DDFF0-0B04-9245-12FA-E581275E6A33-1871-1_conId0052mcuProductSNs564DDFF0-0B04-9245-12FA-E581275E6A33 > div.video-item.connect > div.control-bar > a.video_a > #requestDisconn_0052").click()
        driver.find_element_by_xpath("(//button[@id='requestDisconn_0052'])[8]").click()
        driver.find_element_by_css_selector("#uniqueId_564DDFF0-0B04-9245-12FA-E581275E6A33-1871-0_conId0052mcuProductSNs564DDFF0-0B04-9245-12FA-E581275E6A33 > div.video-item.connect > div.control-bar > a.video_a > #requestDisconn_0052").click()
        driver.find_element_by_xpath("(//button[@id='requestDisconn_0052'])[9]").click()
        driver.find_element_by_id("requestConn_0052").click()
        driver.find_element_by_id("requestConn_0052").click()
        driver.find_element_by_xpath("(//button[@id='requestConn_0052'])[2]").click()
        driver.find_element_by_xpath("(//button[@id='requestConn_0052'])[3]").click()
        driver.find_element_by_xpath("(//button[@id='requestConn_0052'])[4]").click()
        driver.find_element_by_xpath("(//button[@id='requestConn_0052'])[5]").click()
        driver.find_element_by_xpath("(//button[@id='requestConn_0052'])[6]").click()
        driver.find_element_by_xpath("(//button[@id='requestConn_0052'])[7]").click()
        driver.find_element_by_css_selector("#uniqueId_564DDFF0-0B04-9245-12FA-E581275E6A33-1871-1_conId0052mcuProductSNs564DDFF0-0B04-9245-12FA-E581275E6A33 > div.video-item.connect > div.control-bar > a.video_a > #requestConn_0052").click()
        driver.find_element_by_xpath("(//button[@id='requestConn_0052'])[8]").click()
        driver.find_element_by_css_selector("#uniqueId_564DDFF0-0B04-9245-12FA-E581275E6A33-1871-0_conId0052mcuProductSNs564DDFF0-0B04-9245-12FA-E581275E6A33 > div.video-item.connect > div.control-bar > a.video_a > #requestConn_0052").click()
        driver.find_element_by_xpath("(//button[@id='requestConn_0052'])[9]").click()
    
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
