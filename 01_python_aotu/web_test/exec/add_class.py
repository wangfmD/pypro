# coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from time import sleep
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

cn = [{"classroomname": u"30教室", "classaccnumber": "10"},
      {"classroomname": u"31教室", "classaccnumber": "10"},
      {"classroomname": u"33教室", "classaccnumber": "10"},
      {"classroomname": u"34教室", "classaccnumber": "10"},
      {"classroomname": u"38教室", "classaccnumber": "10"},
      {"classroomname": u"40教室", "classaccnumber": "10"}]


def addclassromm(classroomname, classaccnumber):
    driver = webdriver.Chrome()
    driver.implicitly_wait(30)
    base_url = 'http://10.1.0.47'
    driver.get(base_url + "/middleclient/index.do")
    Select(driver.find_element_by_id("platform")).select_by_visible_text(
        u"河南教育局")
    driver.find_element_by_id('s_username').clear()
    driver.find_element_by_id('s_username').send_keys('hnsadmin')
    driver.find_element_by_id('s_password').clear()
    driver.find_element_by_id('s_password').send_keys('111111')
    driver.find_element_by_name('submit').click()
    driver.maximize_window()

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
    for flag in range(len(cn)):
        # print cn[flag]['classaccnumber'], cn[flag]['classroomname']
        addclassromm(cn[flag]['classroomname'], cn[flag]['classaccnumber'])
