# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from time import sleep


def login():
    driver = webdriver.Chrome()
    driver.implicitly_wait(30)
    base_url = "http://10.1.0.54"
    verificationErrors = []
    accept_next_alert = True
    driver.get(base_url + "/middleclient/index.do")
    Select(driver.find_element_by_id("platform")).select_by_visible_text(
        u"河南教育局")
    driver.find_element_by_id("s_username").clear()
    driver.find_element_by_id("s_username").send_keys("hnsadmin")
    driver.find_element_by_id("s_password").clear()
    driver.find_element_by_id("s_password").send_keys("111111")
    driver.find_element_by_name("submit").click()
    driver.maximize_window()
    driver.find_element_by_link_text(u"内容管理").click()
    driver.find_element_by_link_text(u"视频管理").click()
    driver.find_element_by_id("upload").click()
    filePath = "G:\\2.mp4"
    driver.find_element_by_id("upload").sendKeys(filePath)
    # String filePath = "G:\\2.mp4"
    # adFileUpload..sendKeys(filePath)
    sleep(20)
    driver.find_element_by_id("modeeditsure").click()
    sleep(2)
    sleep(10)


if __name__ == '__main__':
    login()
