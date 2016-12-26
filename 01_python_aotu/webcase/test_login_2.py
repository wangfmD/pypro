# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from time import sleep
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

# http://10.1.0.54/middleclient/pcManager/LessonPage.do?typeCode=1401&lessonId=ad53d86d-24d5-40fc-99c7-3a799983aa00&isZhu=1&classroomId=3b56d0d6-bae4-4e42-b0f7-0534fcbd64c9&interactType=false&created=0&mcuIds=ee8e08a4-7113-404d-ab63-e938ce14c631
# http://10.1.0.54/middleclient/pcManager/LessonPage.do?typeCode=1401&lessonId=2ef96704-b305-4991-a1c2-b69111a1834e&isZhu=1&classroomId=7a562357-4a68-40b4-bb30-50c7da90512e&interactType=false&created=0&mcuIds=ee8e08a4-7113-404d-ab63-e938ce14c631
# http://10.1.0.54/middleclient/pcManager/LessonPage.do?typeCode=1401&lessonId=838ff881-e1f3-4515-96c2-7e405c1bbc7c&isZhu=1&classroomId=7a562357-4a68-40b4-bb30-50c7da90512e&interactType=false&created=0&mcuIds=ee8e08a4-7113-404d-ab63-e938ce14c631
# http://10.1.0.54/middleclient/pcManager/LessonPage.do?typeCode=1403&lessonId=3eb83aa7-c2d4-41f7-b3a5-85c3ad4e5fad&isZhu=1&classroomId=7a562357-4a68-40b4-bb30-50c7da90512e&interactType=false&created=0&mcuIds=3fc3ff07-42d7-451f-8deb-03fa86f6eebb
# http://10.1.0.54/middleclient/pcManager/LessonPage.do?typeCode=1401&lessonId=e60a32bd-8fe0-47dd-b30d-f736ec894d87&isZhu=1&classroomId=fd0e7b60-3205-454a-99ba-cc2afb04288f&interactType=false&created=0
# http://10.1.0.56/middleclient/pcManager/LessonPage.do?typeCode=1401&lessonId=9a1545de-9f78-42a3-aa49-deb2a7920446&isZhu=1&classroomId=2e01ebe7-e8a0-45e5-b9fa-25af144b856d&interactType=false&created=0
# http://10.1.0.56
# http://10.1.0.56/middleclient/pcManager/LessonPage.do?typeCode=1401&lessonId=9a1545de-9f78-42a3-aa49-deb2a7920446&isZhu=1&classroomId=2e01ebe7-e8a0-45e5-b9fa-25af144b856d&interactType=false&created=0
# http://10.1.0.56/middleclient/pcManager/LessonPage.do?typeCode=1401&lessonId=49148ad3-064c-4f37-a72e-d67c925753c8&isZhu=1&classroomId=2e01ebe7-e8a0-45e5-b9fa-25af144b856d&interactType=false&created=0
# http://10.1.0.54/middleclient/pcManager/LessonPage.do?typeCode=1401&lessonId=90d2a8e6-d7d3-45dd-9596-6a463cdf006c&isZhu=1&classroomId=aa9ba972-94a0-4853-9b0b-ca1a4c24d305&interactType=false&created=0

# plus_url = '/middleclient/pcManager/LessonPage.do?typeCode=1401&lessonId=9a1545de-9f78-42a3-aa49-deb2a7920446&isZhu=1&classroomId=2e01ebe7-e8a0-45e5-b9fa-25af144b856d&interactType=false&created=0'
# plus_url = '/middleclient/pcManager/LessonPage.do?typeCode=1401&lessonId=49148ad3-064c-4f37-a72e-d67c925753c8&isZhu=1&classroomId=2e01ebe7-e8a0-45e5-b9fa-25af144b856d&interactType=false&created=0'
# 56 0041
plus_url = '/middleclient/pcManager/LessonPage.do?typeCode=1401&lessonId=90d2a8e6-d7d3-45dd-9596-6a463cdf006c&isZhu=1&classroomId=aa9ba972-94a0-4853-9b0b-ca1a4c24d305&interactType=false&created=0'
# 54 0041


def login():
    driver = webdriver.Chrome()
    driver.implicitly_wait(30)
    base_url = "http://10.1.0.54"
    verificationErrors = []
    accept_next_alert = True
    driver.get(base_url + plus_url)
    Select(driver.find_element_by_id("platform")).select_by_visible_text(
        u"河南教育局")
    driver.find_element_by_id("s_username").clear()
    driver.find_element_by_id("s_username").send_keys("hnsadmin")
    driver.find_element_by_id("s_password").clear()
    driver.find_element_by_id("s_password").send_keys("111111")
    # 登录
    driver.find_element_by_name("submit").click()
    driver.maximize_window()
    sleep(10)
    # 开课
    driver.find_element_by_id("pc_startButton").click()
    sleep(59)
    while True:
        # driver.find_element_by_xpath("(//button[@id='requestDisconn_0041'])[2]").click()
        driver.find_element_by_xpath("(//button[@id='requestDisconn_0041'])[2]").click()
        sleep(3)
        driver.find_element_by_xpath("(//button[@id='requestDisconn_0041'])[3]").click()
        sleep(3)
        driver.find_element_by_xpath("(//button[@id='requestDisconn_0041'])[4]").click()
        sleep(3)
        driver.find_element_by_xpath("(//button[@id='requestDisconn_0041'])[5]").click()
        sleep(3)
        driver.find_element_by_xpath("(//button[@id='requestDisconn_0041'])[6]").click()
        sleep(3)
        driver.find_element_by_xpath("(//button[@id='requestDisconn_0041'])[7]").click()
        sleep(3)
        driver.find_element_by_xpath("//button[@id='requestDisconn_0041']").click()
        sleep(10)
        driver.find_element_by_xpath("//button[@id='requestConn_0041']").click()
        sleep(20)
        driver.find_element_by_xpath("(//button[@id='requestConn_0041'])[2]").click()
        sleep(3)
        driver.find_element_by_xpath("(//button[@id='requestConn_0041'])[3]").click()
        sleep(3)
        driver.find_element_by_xpath("(//button[@id='requestConn_0041'])[4]").click()
        sleep(3)
        driver.find_element_by_xpath("(//button[@id='requestConn_0041'])[5]").click()
        # sleep(2)
        driver.find_element_by_xpath("(//button[@id='requestConn_0041'])[6]").click()
        sleep(3)
        driver.find_element_by_xpath("(//button[@id='requestConn_0041'])[7]").click()
        sleep(15)

    # driver.find_element_by_link_text(u"10.1.0.38录播").click()
    # driver.find_element_by_link_text(u"10.1.0.40录播").click()
    # driver.find_element_by_link_text(u"10.1.0.31录播").click()
    # driver.find_element_by_link_text(u"10.1.0.34录播").click()
    # driver.find_element_by_link_text(u"10.1.0.33录播").click()

    sleep(300000)
    # 开课
    driver.find_element_by_id("pc_startButton").click()

    driver.maximize_window()
    sleep(2)
    sleep(10)


if __name__ == '__main__':
    login()
