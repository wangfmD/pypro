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


def adomin_login():
    driver = webdriver.Chrome()
    driver.implicitly_wait(40)
    base_url = 'http://10.1.0.47'
    driver.get(base_url + "/middleclient/index.do")
    driver.find_element_by_id('s_username').clear()
    driver.find_element_by_id('s_username').send_keys('administrator')
    driver.find_element_by_id('s_password').clear()
    driver.find_element_by_id('s_password').send_keys('xungejiaoyu')
    driver.find_element_by_name('submit').click()


def user_login():
    driver = webdriver.Chrome()
    driver.implicitly_wait(40)
    base_url = 'http://10.1.0.47'
    driver.get(base_url + "/middleclient/index.do")
    Select(driver.find_element_by_id("platform")).select_by_visible_text(
        u"河南省教育局")
    # Select(driver.find_element_by_id("platform")).select_by_visible_text(
    #     u"河南教育局哦")
    driver.find_element_by_id('s_username').clear()
    driver.find_element_by_id('s_username').send_keys('hnsadmin')
    driver.find_element_by_id('s_password').clear()
    driver.find_element_by_id('s_password').send_keys('111111')
    driver.find_element_by_name('submit').click()
    driver.maximize_window()


def addUserPlatform():
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

if __name__ == '__main__':
    adomin_login()
    addUserPlatform()
