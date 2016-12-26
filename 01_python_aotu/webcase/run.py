# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import StaleElementReferenceException
from time import sleep
# http://10.1.0.56/middleclient/pcManager/LessonPage.do?typeCode=1401&lessonId=c0524ec5-ffa8-4d69-ab28-fa302935a9af&isZhu=1&classroomId=6cded52c-d5cc-469a-958d-6c6f9718384f&interactType=false&created=0
plus_url = '/middleclient/pcManager/LessonPage.do?typeCode=1401&lessonId=c0524ec5-ffa8-4d69-ab28-fa302935a9af&isZhu=1&classroomId=6cded52c-d5cc-469a-958d-6c6f9718384f&interactType=false&created=0'


def login():
    driver = webdriver.Chrome()
    driver.implicitly_wait(30)
    base_url = "http://10.1.0.56"
    verificationErrors = []
    accept_next_alert = True
    # driver.get(base_url + plus_url)
    driver.get(base_url + "/middleclient/index.do")
    Select(driver.find_element_by_id("platform")).select_by_visible_text(
        u"河南教育局")
    driver.find_element_by_id("s_username").clear()
    driver.find_element_by_id("s_username").send_keys("hnsadmin")
    driver.find_element_by_id("s_password").clear()
    driver.find_element_by_id("s_password").send_keys("111111")
    # 登录
    driver.find_element_by_name("submit").click()
    driver.maximize_window()
    sleep(2)
    driver.get(base_url + plus_url)
    sleep(8)
    # 开课
    driver.find_element_by_id("pc_startButton").click()
    sleep(25)
    while True:
        try:
            driver.find_element_by_xpath("(//button[@id='requestDisconn_0000'])[2]").click()
        except StaleElementReferenceException as e:
            print e
        sleep(2)
        try:
            driver.find_element_by_xpath("(//button[@id='requestDisconn_0000'])[3]").click()
        except StaleElementReferenceException as e:
            print e
        sleep(2)
        try:
            driver.find_element_by_xpath("(//button[@id='requestDisconn_0000'])[4]").click()
        except StaleElementReferenceException as e:
            print e
        sleep(3)
        try:
            driver.find_element_by_xpath("(//button[@id='requestDisconn_0000'])[5]").click()
        except StaleElementReferenceException as e:
            print e
        sleep(2)
        try:
            driver.find_element_by_xpath("(//button[@id='requestDisconn_0000'])[6]").click()
        except StaleElementReferenceException as e:
            print e
        sleep(2)
        try:
            driver.find_element_by_xpath("(//button[@id='requestDisconn_0000'])[7]").click()
        except StaleElementReferenceException as e:
            print e
        sleep(2)
        try:
            driver.find_element_by_xpath("//button[@id='requestDisconn_0000']").click()
        except StaleElementReferenceException as e:
            print e
        sleep(10)
        try:
            driver.find_element_by_xpath("//button[@id='requestConn_0000']").click()
        except StaleElementReferenceException as e:
            print e
        sleep(20)
        try:
            driver.find_element_by_xpath("(//button[@id='requestConn_0000'])[2]").click()
        except StaleElementReferenceException as e:
            print e
        sleep(2)
        try:
            driver.find_element_by_xpath("(//button[@id='requestConn_0000'])[3]").click()
        except StaleElementReferenceException as e:
            print e
        sleep(2)
        try:
            driver.find_element_by_xpath("(//button[@id='requestConn_0000'])[4]").click()
        except StaleElementReferenceException as e:
            print e
        sleep(2)
        try:
            driver.find_element_by_xpath("(//button[@id='requestConn_0000'])[5]").click()
        except StaleElementReferenceException as e:
            print e
        sleep(2)
        try:
            driver.find_element_by_xpath("(//button[@id='requestConn_0000'])[6]").click()
        except StaleElementReferenceException as e:
            print e
        sleep(2)
        try:
            driver.find_element_by_xpath("(//button[@id='requestConn_0000'])[7]").click()
        except StaleElementReferenceException as e:
            print e
        sleep(15)

    sleep(300000)
    # 开课
    driver.find_element_by_id("pc_startButton").click()
    sleep(10)


if __name__ == '__main__':
    login()
