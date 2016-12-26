# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest
from time import sleep
import re
import sys
reload(sys)
sys.setdefaultencoding("utf-8")


base_url = 'http://10.1.0.54'
cn = [{"classroomname": u"30教室", "classaccnumber": "10"},
      {"classroomname": u"31教室", "classaccnumber": "10"},
      {"classroomname": u"33教室", "classaccnumber": "10"},
      {"classroomname": u"34教室", "classaccnumber": "10"},
      {"classroomname": u"38教室", "classaccnumber": "10"},
      {"classroomname": u"40教室", "classaccnumber": "10"},
      {"classroomname": u"81教室", "classaccnumber": "10"},
      {"classroomname": u"164教室", "classaccnumber": "10"}]


def adomin_login(driver):
    driver.implicitly_wait(40)
    driver.get(base_url + "/middleclient/index.do")
    driver.maximize_window()
    driver.find_element_by_id('s_username').clear()
    driver.find_element_by_id('s_username').send_keys('administrator')
    driver.find_element_by_id('s_password').clear()
    driver.find_element_by_id('s_password').send_keys('xungejiaoyu')
    driver.find_element_by_name('submit').click()


def user_login(driver, username, platformname):
    driver.implicitly_wait(30)
    driver.get(base_url + "/middleclient/index.do")
    driver.maximize_window()
    driver.refresh()
    Select(driver.find_element_by_id("platform")).select_by_visible_text(platformname)
    # Select(driver.find_element_by_id("platform")).select_by_visible_text(
    #     u"河南教育局哦")
    driver.find_element_by_id('s_username').clear()
    driver.find_element_by_id('s_username').send_keys(username)
    driver.find_element_by_id('s_password').clear()
    driver.find_element_by_id('s_password').send_keys('111111')
    driver.find_element_by_name('submit').click()


def addUserPlatform():
    driver = webdriver.Chrome()
    adomin_login(driver)

    driver.find_element_by_link_text(u"系统管理").click()
    driver.find_element_by_link_text(u"租户管理").click()
    sleep(1)
    driver.find_element_by_css_selector("i.fa.fa-plus").click()
    sleep(1)
    driver.find_element_by_css_selector("#areaId > div.col-sm-9 > input.form-control").click()
    sleep(1)
    driver.find_element_by_xpath("//div[@id='treeview']/ul/li[17]").click()
    sleep(1)
    driver.find_element_by_css_selector("div.modal-content > div.text-center > button.btn.btn-success").click()
    sleep(1)
    driver.find_element_by_css_selector("#platmarkName > div.col-sm-9 > input.form-control").clear()
    driver.find_element_by_css_selector("#platmarkName > div.col-sm-9 > input.form-control").send_keys(u"河南教育局")
    driver.find_element_by_css_selector("#platmarkCode > div.col-sm-9 > input.form-control").clear()
    driver.find_element_by_css_selector("#platmarkCode > div.col-sm-9 > input.form-control").send_keys("0011")
    sleep(1)
    driver.find_element_by_id("submit").click()
    sleep(5)
    driver.quit()


def addSchool():
    driver = webdriver.Chrome()
    user_login(driver, 'hnsadmin', u"河南省教育局")

    sleep(1)
    driver.find_element_by_link_text(u"系统管理").click()
    driver.find_element_by_link_text(u"学校管理").click()
    driver.find_element_by_id("choosearea").click()
    sleep(1)
    driver.find_element_by_xpath("//div[@id='treeview']/ul/li[2]").click()
    driver.find_element_by_css_selector("div.col-sm-9.text-center > #submit").click()
    sleep(1)
    driver.find_element_by_id("addSchool").click()
    sleep(1)
    Select(driver.find_element_by_css_selector("select.form-control")).select_by_visible_text(u"高中")
    driver.find_element_by_css_selector("#schoolName > div.col-sm-9 > input.form-control").clear()
    driver.find_element_by_css_selector("#schoolName > div.col-sm-9 > input.form-control").send_keys(u"郑州一中")
    driver.find_element_by_id("submit").click()
    sleep(3)
    driver.get_screenshot_as_file('D:/11111.png')
    dir(driver)
    sleep(2)
    driver.quit()


def addclassromm(classroomname, classaccnumber):
    driver = webdriver.Chrome()
    user_login(driver, 'hnsadmin', u"河南省教育局")

    sleep(1)
    driver.find_element_by_css_selector("#div_menu > ul.nav.nav-list > li > a.dropdown-toggle > span.menu-text").click()
    driver.find_element_by_link_text(u"学校管理").click()
    driver.find_element_by_css_selector(u"a[title=\"添加教室\"] > span").click()
    sleep(1)
    driver.find_element_by_css_selector("#className > div.col-sm-9 > input.form-control").clear()
    driver.find_element_by_css_selector("#className > div.col-sm-9 > input.form-control").send_keys(classroomname)
    driver.find_element_by_css_selector("#classAccNumber > div.col-sm-9 > input.form-control").clear()
    driver.find_element_by_css_selector("#classAccNumber > div.col-sm-9 > input.form-control").send_keys(classaccnumber)
    sleep(1)
    driver.find_element_by_css_selector(
        "#classroommodal > div.modal-dialog > div.modal-content > form.form-horizontal > div.modal-body.row > div.form-group > div.col-sm-9 > #submit").click()

    sleep(3)
    driver.quit()


if __name__ == '__main__':
    # addUserPlatform()
    # sleep(4)
    addSchool()

    for flag in range(len(cn)):
        # print cn[flag]['classaccnumber'], cn[flag]['classroomname']
        addclassromm(cn[flag]['classroomname'], cn[flag]['classaccnumber'])
