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
    driver.implicitly_wait(40)
    base_url = 'http://10.1.0.54'
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

    driver.find_element_by_css_selector(
        "#div_menu > ul.nav.nav-list > li > a.dropdown-toggle > span.menu-text").click()
    driver.find_element_by_link_text(u"学校管理").click()
    driver.find_element_by_link_text(u"教室列表").click()
    driver.find_element_by_link_text(u"40教室").click()
    driver.find_element_by_xpath(u"//a[contains(text(),'设备管理')]").click()
    sleep(1)
    driver.find_element_by_id("addterminal").click()
    sleep(1)
    driver.find_element_by_css_selector(
        "div.modal-body > div > #name > div.col-sm-9 > input.form-control").clear()
    driver.find_element_by_css_selector(
        "div.modal-body > div > #name > div.col-sm-9 > input.form-control").send_keys("10.1.0.40")
    Select(driver.find_element_by_css_selector(
        "div.modal-body > div > #equipmentModel > div.col-sm-9 > select")).select_by_visible_text(u"Group系列")
    driver.find_element_by_css_selector(
        "div.modal-body > div > #ipAddr > div.col-sm-9 > input.form-control").clear()
    driver.find_element_by_css_selector(
        "div.modal-body > div > #ipAddr > div.col-sm-9 > input.form-control").send_keys("10.1.0.40")
    driver.find_element_by_css_selector(
        "div.modal-body > div > #locAddr > div.col-sm-9 > input.form-control").clear()
    driver.find_element_by_css_selector(
        "div.modal-body > div > #locAddr > div.col-sm-9 > input.form-control").send_keys("10.1.0.40")
    driver.find_element_by_css_selector(
        "div.modal-body > div > #equipmentLogName > div.col-sm-9 > input.form-control").clear()
    driver.find_element_by_css_selector(
        "div.modal-body > div > #equipmentLogName > div.col-sm-9 > input.form-control").send_keys("admin")
    driver.find_element_by_css_selector(
        "div.modal-body > div > #equipmentLogPwd > div.col-sm-9 > input.form-control").clear()
    driver.find_element_by_css_selector(
        "div.modal-body > div > #equipmentLogPwd > div.col-sm-9 > input.form-control").send_keys("admin")
    driver.find_element_by_css_selector(
        "#terminal > div.modal-dialog > div.modal-content > #formrole > div.modal-body > div.text-center > #submit").click()
    driver.find_element_by_xpath("(//input[@name='isgk'])[2]").click()

    sleep(50)

if __name__ == '__main__':
    adomin_login()

    # driver = self.driver
    # driver.get(self.base_url + "/middleclient/index.do")
    # driver.find_element_by_css_selector(u"a[title=\"添加教室\"] > span").click()
    # driver.find_element_by_css_selector("#className > div.col-sm-9 > input.form-control").clear()
    # driver.find_element_by_css_selector("#className > div.col-sm-9 > input.form-control").send_keys(u"40教室")
    # driver.find_element_by_css_selector("#classAccNumber > div.col-sm-9 > input.form-control").clear()
    # driver.find_element_by_css_selector("#classAccNumber > div.col-sm-9 > input.form-control").send_keys("10")
    # driver.find_element_by_css_selector("#classroommodal > div.modal-dialog > div.modal-content > form.form-horizontal > div.modal-body.row > div.form-group > div.col-sm-9 > #submit").click()
