# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest
import re
import sys
from init import base_url, classroom_para
from time import sleep
reload(sys)
sys.setdefaultencoding("utf-8")


def conf_local_interact(interactaddr):
    driver = webdriver.Chrome()
    driver.implicitly_wait(40)
    driver.get("http://" + interactaddr + "/interact/login.do")
    driver.maximize_window()
    driver.find_element_by_id("username").clear()
    driver.find_element_by_id("username").send_keys("administrator")
    driver.find_element_by_id("password").clear()
    driver.find_element_by_id("password").send_keys("xungejiaoyu")
    sleep(1)
    driver.find_element_by_id("buttlogin").click()
    sleep(1)
    driver.find_element_by_id("sysconfig").click()
    sleep(1)
    driver.find_element_by_xpath("//table[@id='table']/tbody/tr[2]/td[3]/a/i").click()
    sleep(1)
    driver.find_element_by_id("value").clear()
    driver.find_element_by_id("value").send_keys(interactaddr)
    driver.find_element_by_xpath("(//button[@type='button'])[4]").click()
    sleep(1)
    driver.find_element_by_id("sysmiddlewarelocal").click()
    sleep(1)
    driver.find_element_by_id("addLocal").click()  # 获取消息中间件
    sleep(1)
    driver.find_element_by_xpath("(//input[@name='text'])").click()
    sleep(1)
    driver.find_element_by_id("determines").click()
    sleep(1)
    driver.switch_to_alert().accept()
    sleep(1)
    driver.find_element_by_css_selector(u"button[title=\"设为本地连接中间件\"]").click()
    sleep(1)
    driver.switch_to_alert().accept()
    sleep(1)
    driver.find_element_by_css_selector(u"button[title=\"手动连接中间件\"]").click()
    sleep(1)
    driver.switch_to_alert().accept()
    sleep(1)
    driver.quit()


def conf_interact(interactaddr, serveraddr):
    driver = webdriver.Chrome()
    driver.implicitly_wait(40)
    driver.get("http://" + interactaddr + "/interact/login.do")
    driver.maximize_window()
    driver.find_element_by_id("username").clear()
    driver.find_element_by_id("username").send_keys("administrator")
    driver.find_element_by_id("password").clear()
    driver.find_element_by_id("password").send_keys("xungejiaoyu")
    sleep(1)
    driver.find_element_by_id("buttlogin").click()
    sleep(1)
    driver.find_element_by_id("sysconfig").click()
    sleep(1)
    driver.find_element_by_xpath("//table[@id='table']/tbody/tr[2]/td[3]/a/i").click()
    sleep(1)
    driver.find_element_by_id("value").clear()
    driver.find_element_by_id("value").send_keys(serveraddr)
    driver.find_element_by_xpath("(//button[@type='button'])[4]").click()
    sleep(1)
    driver.find_element_by_id("sysmiddlewarelocal").click()
    sleep(1)
    driver.find_element_by_id("addLocal").click()
    sleep(1)
    driver.find_element_by_xpath("//input[@name='text']").click()
    sleep(1)
    driver.find_element_by_xpath("(//input[@name='text'])[2]").click()
    sleep(1)
    driver.find_element_by_id("determines").click()
    sleep(1)
    driver.switch_to_alert().accept()
    sleep(1)
    driver.find_element_by_xpath("//tbody[@id='localQuery']/tr[2]/th[8]/button").click()
    sleep(1)
    driver.switch_to_alert().accept()
    sleep(1)
    driver.find_element_by_xpath("//button[4]").click()
    sleep(1)
    driver.switch_to_alert().accept()
    sleep(1)
    driver.find_element_by_xpath("//tr[2]/th[8]/button[4]").click()
    sleep(1)
    driver.switch_to_alert().accept()
    sleep(1)
    driver.find_element_by_css_selector(u"button[title=\"设为自动连接\"]").click()
    sleep(1)
    driver.switch_to_alert().accept()
    sleep(1)
    driver.quit()


if __name__ == '__main__':
    conf_local_interact("10.1.0.56")
    conf_interact("10.1.0.58", "10.1.0.56")
