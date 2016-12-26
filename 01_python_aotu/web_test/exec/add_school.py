# coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from time import sleep


def adomin_login():
    driver = webdriver.Chrome()
    driver.implicitly_wait(30)
    base_url = 'http://10.1.0.47'
    driver.get(base_url + "/middleclient/index.do")
    # Select(driver.find_element_by_id("platform")).select_by_visible_text(
    #     u"河南省教育局")
    Select(driver.find_element_by_id("platform")).select_by_visible_text(
        u"河南教育局")
    driver.find_element_by_id('s_username').clear()
    driver.find_element_by_id('s_username').send_keys('hnsadmin')
    driver.find_element_by_id('s_password').clear()
    driver.find_element_by_id('s_password').send_keys('111111')
    driver.find_element_by_name('submit').click()
    driver.maximize_window()

    # driver.find_element_by_css_selector("#div_menu > ul.nav.nav-list > li > a.dropdown-toggle > span.menu-text").click()
    driver.find_element_by_xpath("//ul/div/ul/li/a/span").click()
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
    sleep(50)

if __name__ == '__main__':
    adomin_login()
