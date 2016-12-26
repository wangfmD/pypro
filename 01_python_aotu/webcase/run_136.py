# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import StaleElementReferenceException
from time import sleep

# http://10.1.0.56/middleclient/pcManager/LessonPage.do?typeCode=1401&lessonId=be6e4154-fe0e-4780-a839-bc9e62d53024&isZhu=1&classroomId=7c3511f7-8b79-4408-ab61-8d36b75ef5aa&interactType=false&created=0
plus_url = '/middleclient/pcManager/LessonPage.do?typeCode=1401&lessonId=40706bfa-a57b-4521-9660-82edfca2b781&isZhu=1&classroomId=7c3511f7-8b79-4408-ab61-8d36b75ef5aa&interactType=false&created=0'
# http://10.1.0.56/middleclient/pcManager/LessonPage.do?typeCode=1401&lessonId=40706bfa-a57b-4521-9660-82edfca2b781&isZhu=1&classroomId=7c3511f7-8b79-4408-ab61-8d36b75ef5aa&interactType=false&created=0


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
    sleep(3)
    driver.get(base_url + plus_url)
    sleep(10)
    # 开课
    driver.find_element_by_id("pc_startButton").click()
    sleep(25)
    while True:
        try:
            driver.find_element_by_xpath("(//button[@id='requestDisconn_0087'])[2]").click()
        except StaleElementReferenceException as e:
            print e
        sleep(2)
        try:
            driver.find_element_by_xpath("(//button[@id='requestDisconn_0087'])[3]").click()
        except StaleElementReferenceException as e:
            print e
        sleep(2)
        try:
            driver.find_element_by_xpath("(//button[@id='requestDisconn_0087'])[4]").click()
        except StaleElementReferenceException as e:
            print e
        sleep(2)
        try:
            driver.find_element_by_xpath("//button[@id='requestDisconn_0087']").click()
        except StaleElementReferenceException as e:
            print e
        sleep(10)
        try:
            driver.find_element_by_xpath("//button[@id='requestConn_0087']").click()
        except StaleElementReferenceException as e:
            print e
        sleep(20)
        try:
            driver.find_element_by_xpath("(//button[@id='requestConn_0087'])[2]").click()
        except StaleElementReferenceException as e:
            print e
        sleep(2)
        try:
            driver.find_element_by_xpath("(//button[@id='requestConn_0087'])[3]").click()
        except StaleElementReferenceException as e:
            print e
        sleep(2)
        try:
            driver.find_element_by_xpath("(//button[@id='requestConn_0087'])[4]").click()
        except StaleElementReferenceException as e:
            print e
        sleep(15)

    sleep(300000)
    # 开课
    driver.find_element_by_id("pc_startButton").click()
    sleep(10)


if __name__ == '__main__':
    login()
