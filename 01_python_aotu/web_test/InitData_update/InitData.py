# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException, ElementNotVisibleException
import unittest
import re
import sys
from init import base_url, classroom_para, db_conf, interact_1
from mysql_kit import sqlOperating, sqlpara
from time import sleep
reload(sys)
sys.setdefaultencoding("utf-8")

middle_interact_ip = db_conf['hostadd']
node_interact_ip = interact_1


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
    driver.find_element_by_css_selector("#platmarkCode > div.col-sm-9 > input.form-control").send_keys("001")
    sleep(1)
    driver.find_element_by_id("submit").click()
    sleep(5)
    driver.quit()


def addSchool():
    driver = webdriver.Chrome()
    user_login(driver, 'hnsadmin', u"河南教育局")
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
    sleep(2)
    driver.get_screenshot_as_file('D:/11111.png')
    dir(driver)
    sleep(2)
    driver.quit()


def addclassromm(classroomname, classaccnumber):
    driver = webdriver.Chrome()
    user_login(driver, 'hnsadmin', u"河南教育局")

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
    sleep(2)
    driver.quit()


def addterminal(
        click_classroom, equipment_name, equipmentModel, ipAddr, locAddr, equipmentLogName, equipmentLogPwd, equimenttype):
    driver = webdriver.Chrome()
    user_login(driver, 'hnsadmin', u"河南教育局")

    driver.find_element_by_css_selector(
        "#div_menu > ul.nav.nav-list > li > a.dropdown-toggle > span.menu-text").click()
    driver.find_element_by_link_text(u"学校管理").click()
    sleep(1)
    driver.find_element_by_link_text(u"教室列表").click()
    sleep(1)
    driver.find_element_by_link_text(click_classroom).click()
    sleep(1)
    driver.find_element_by_xpath(u"//a[contains(text(),'设备管理')]").click()
    sleep(1)
    if equimenttype == '1':
        driver.find_element_by_id("addIntegrated").click()
        sleep(1)
        driver.find_element_by_css_selector(
            "div.modal-body.row > div > #name > div.col-sm-9 > input.form-control").clear()
        driver.find_element_by_css_selector(
            "div.modal-body.row > div > #name > div.col-sm-9 > input.form-control").send_keys("81lubo")
        driver.find_element_by_css_selector(
            "div.modal-body.row > div > #ipAddr > div.col-sm-9 > input.form-control").clear()
        driver.find_element_by_css_selector(
            "div.modal-body.row > div > #ipAddr > div.col-sm-9 > input.form-control").send_keys("10.1.0.81")
        driver.find_element_by_css_selector(
            "div.modal-body.row > div > #locAddr > div.col-sm-9 > input.form-control").clear()
        driver.find_element_by_css_selector(
            "div.modal-body.row > div > #locAddr > div.col-sm-9 > input.form-control").send_keys("10.1.0.81")
        driver.find_element_by_css_selector(
            "div.modal-body.row > div > #equipmentLogName > div.col-sm-9 > input.form-control").clear()
        driver.find_element_by_css_selector(
            "div.modal-body.row > div > #equipmentLogName > div.col-sm-9 > input.form-control").send_keys("admin")
        driver.find_element_by_css_selector(
            "div.modal-body.row > div > #equipmentLogPwd > div.col-sm-9 > input.form-control").clear()
        driver.find_element_by_css_selector(
            "div.modal-body.row > div > #equipmentLogPwd > div.col-sm-9 > input.form-control").send_keys("admin")
        driver.find_element_by_css_selector(
            "#Integrated > div.modal-dialog > div.modal-content > #formrole > div.modal-body.row > div.text-center > #submit").click()
        # driver.find_element_by_xpath("(//input[@name='isIngk'])[2]").click()
        sleep(2)
        driver.quit()
    else:
        driver.find_element_by_id("addterminal").click()
        sleep(1)
        driver.find_element_by_css_selector(
            "div.modal-body > div > #name > div.col-sm-9 > input.form-control").clear()
        driver.find_element_by_css_selector(
            "div.modal-body > div > #name > div.col-sm-9 > input.form-control").send_keys(equipment_name)
        Select(driver.find_element_by_css_selector(
            "div.modal-body > div > #equipmentModel > div.col-sm-9 > select")).select_by_visible_text(equipmentModel)
        driver.find_element_by_css_selector(
            "div.modal-body > div > #ipAddr > div.col-sm-9 > input.form-control").clear()
        driver.find_element_by_css_selector(
            "div.modal-body > div > #ipAddr > div.col-sm-9 > input.form-control").send_keys(ipAddr)
        driver.find_element_by_css_selector(
            "div.modal-body > div > #locAddr > div.col-sm-9 > input.form-control").clear()
        driver.find_element_by_css_selector(
            "div.modal-body > div > #locAddr > div.col-sm-9 > input.form-control").send_keys(locAddr)
        driver.find_element_by_css_selector(
            "div.modal-body > div > #equipmentLogName > div.col-sm-9 > input.form-control").clear()
        driver.find_element_by_css_selector(
            "div.modal-body > div > #equipmentLogName > div.col-sm-9 > input.form-control").send_keys(equipmentLogName)
        driver.find_element_by_css_selector(
            "div.modal-body > div > #equipmentLogPwd > div.col-sm-9 > input.form-control").clear()
        driver.find_element_by_css_selector(
            "div.modal-body > div > #equipmentLogPwd > div.col-sm-9 > input.form-control").send_keys(equipmentLogPwd)
        driver.find_element_by_css_selector(
            "#terminal > div.modal-dialog > div.modal-content > #formrole > div.modal-body > div.text-center > #submit").click()
        # driver.find_element_by_xpath("(//input[@name='isgk'])[2]").click()
        sleep(2)
        driver.quit()


def add_interact(addr):
    driver = webdriver.Chrome()
    user_login(driver, 'hnsadmin', u"河南教育局")

    driver.find_element_by_xpath("//div[@id='div_menu']/ul/li[3]/a/span").click()
    sleep(1)
    driver.find_element_by_link_text(u"中心设备").click()
    sleep(1)
    driver.find_element_by_id("xiaoximiddleware").click()
    sleep(1)
    driver.find_element_by_css_selector("#addmiddleware > i.fa.fa-plus").click()
    sleep(1)
    driver.find_element_by_id("host").clear()
    driver.find_element_by_id("host").send_keys(addr)
    driver.find_element_by_id("port").clear()
    driver.find_element_by_id("port").send_keys("80")
    driver.find_element_by_id("username").clear()
    driver.find_element_by_id("username").send_keys("administrator")
    driver.find_element_by_id("password").clear()
    driver.find_element_by_id("password").send_keys("xungejiaoyu")
    sleep(1)
    driver.find_element_by_id("insertmiddleware").click()
    sleep(1)
    driver.quit()


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
    sleep(2)
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
    sleep(2)
    driver.switch_to_alert().accept()
    sleep(1)
    driver.find_element_by_css_selector(u"button[title=\"设为本地连接中间件\"]").click()
    sleep(2.5)
    driver.switch_to_alert().accept()
    sleep(1)
    driver.find_element_by_css_selector(u"button[title=\"手动连接中间件\"]").click()
    sleep(5)
    try:
        driver.switch_to_alert().accept()
    except NoAlertPresentException as e:
        print e
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
    sleep(2)
    driver.switch_to_alert().accept()
    sleep(1)
    driver.find_element_by_xpath("//button[4]").click()
    sleep(2)
    driver.switch_to_alert().accept()
    sleep(1)
    driver.find_element_by_xpath("//tr[2]/th[8]/button[4]").click()
    sleep(2)
    driver.switch_to_alert().accept()
    sleep(1)
    driver.find_element_by_css_selector(u"button[title=\"设为自动连接\"]").click()
    sleep(2)
    driver.switch_to_alert().accept()
    sleep(1)
    driver.quit()


def adduser():
    driver = webdriver.Chrome()
    user_login(driver, 'hnsadmin', u"河南教育局")
    driver.find_element_by_css_selector("#div_menu > ul.nav.nav-list > li > a.dropdown-toggle > span.menu-text").click()
    driver.find_element_by_link_text(u"用户列表").click()
    driver.find_element_by_id("adduserlist").click()
    sleep(1)
    driver.find_element_by_name("loginName").clear()
    driver.find_element_by_name("loginName").send_keys("user")
    driver.find_element_by_name("pwd").clear()
    driver.find_element_by_name("pwd").send_keys("111111")
    driver.find_element_by_name("passwords").clear()
    driver.find_element_by_name("passwords").send_keys("111111")
    driver.find_element_by_name("mobile").clear()
    driver.find_element_by_name("mobile").send_keys("13700010001")
    driver.find_element_by_name("email").clear()
    driver.find_element_by_name("email").send_keys("user@3bu.cn")
    driver.find_element_by_name("trueName").clear()
    driver.find_element_by_name("trueName").send_keys("teacher_1")
    driver.find_element_by_id("determine").click()
    sleep(1)
    driver.quit()


def cfg_interact(interactaddr, serveraddr):
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
    driver.maximize_window()
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
    driver.find_element_by_xpath("(//input[@name='text'])[2]").click()

    sleep(1)
    driver.find_element_by_id("determines").click()
    sleep(2)
    driver.switch_to_alert().accept()  # alert提示框
    sleep(1)
    driver.find_element_by_css_selector(u"button[title=\"设为本地连接中间件\"]").click()
    sleep(2)
    driver.switch_to_alert().accept()  # alert提示框
    sleep(1)
    driver.find_element_by_css_selector(u"button[title=\"手动连接中间件\"]").click()
    sleep(4)
    driver.switch_to_alert().accept()  # alert提示框
    sleep(1)
    driver.find_element_by_id("addLocal").click()
    sleep(1)
    driver.find_element_by_name("text").click()
    sleep(1)
    driver.find_element_by_id("determines").click()
    sleep(2)
    driver.switch_to_alert().accept()  # alert提示框
    sleep(1)
    driver.find_element_by_css_selector(u"button[title=\"手动连接中间件\"]").click()
    sleep(2)
    driver.switch_to_alert().accept()  # alert提示框
    sleep(1)
    try:
        driver.find_element_by_xpath("//tbody[@id='localQuery']/tr[2]/th[8]/button[2]").click()  # 设为自动连接
    except ElementNotVisibleException as e:
        print e
    sleep(2)
    driver.switch_to_alert().accept()  # alert提示框
    # sleep(1)
    # driver.find_element_by_css_selector(u"button[title=\"取消自动连接\"]").click()
    # sleep(2)
    # driver.switch_to_alert().accept()  # alert提示框
    # sleep(1)
    # driver.find_element_by_xpath("//tr[2]/th[8]/button[2]").click()  # 设为自动连接
    driver.quit()


def add_mcu(mcuaddr, mcuport, mcuname, mcupasswd):
    driver = webdriver.Chrome()
    user_login(driver, 'hnsadmin', u"河南教育局")
    driver.find_element_by_link_text(u"设备管理").click()
    driver.find_element_by_link_text(u"中心设备").click()
    sleep(1)
    driver.find_element_by_css_selector("i.fa.fa-plus").click()
    sleep(1)
    driver.find_element_by_id("mcuAreaName").click()
    sleep(1)
    driver.find_element_by_css_selector("li.list-group-item.node-treeview").click()
    sleep(1)
    driver.find_element_by_id("equipmentName").clear()
    driver.find_element_by_id("equipmentName").send_keys(mcuaddr)
    driver.find_element_by_id("equipIpAddr").clear()
    driver.find_element_by_id("equipIpAddr").send_keys(mcuaddr)
    driver.find_element_by_id("mcu_port").clear()
    driver.find_element_by_id("mcu_port").send_keys(mcuport)
    driver.find_element_by_id("mcuLoginName").clear()
    driver.find_element_by_id("mcuLoginName").send_keys(mcuname)
    driver.find_element_by_id("mcuPasswd").clear()
    driver.find_element_by_id("mcuPasswd").send_keys(mcupasswd)
    driver.find_element_by_id("submit").click()
    sleep(1)
    driver.quit()


def cfg_mcu():
    driver = webdriver.Chrome()
    user_login(driver, 'hnsadmin', u"河南教育局")
    driver.find_element_by_link_text(u"设备管理").click()
    driver.find_element_by_link_text(u"中心设备").click()
    sleep(1)
    driver.find_element_by_xpath("(//button[@id='current'])[2]").click()
    sleep(1)
    driver.find_element_by_xpath("//div[@id='AreaMcutreeview']/ul/li/span[3]").click()
    sleep(1)
    driver.find_element_by_id("saveAreaMcu").click()
    sleep(1)
    driver.find_element_by_id("xiaoximiddleware").click()
    sleep(1)
    driver.find_element_by_xpath("//table[@id='middlewaretable']/tbody/tr[2]/td[2]").click()  # 选择interact
    sleep(1)
    driver.find_element_by_css_selector("i.fa.fa-server").click()
    sleep(1)
    driver.find_element_by_name("ckrelevmcuid").click()
    sleep(1)
    driver.find_element_by_id("saverelevmcumiddleware").click()
    sleep(1)
    driver.find_element_by_xpath("//table[@id='middlewaretable']/tbody/tr[2]/td[2]").click()  # 选择interact
    sleep(1)
    # driver.find_element_by_xpath("//table[@id='middlewaretable']/tbody/tr[2]/td[2]").click()
    driver.find_element_by_css_selector("i.fa.fa-bars").click()
    sleep(1)
    driver.find_element_by_css_selector("#listofschooltable > tr > td > input[type=\"checkbox\"]").click()
    sleep(1)
    driver.find_element_by_id("insertmiddlewareschool").click()
    sleep(1)
    # driver.find_element_by_xpath("//table[@id='middlewaretable']/tbody/tr[2]/td[2]").click()
    # sleep(1)
    # driver.find_element_by_id("theschoollist").click()
    driver.quit()

if __name__ == '__main__':
    # init data
    for s in sqlpara:
        c = sqlOperating(db_conf['host'],
                         db_conf['user'],
                         db_conf['passwd'],
                         db_conf['db'])
        # c = sqlOperating()
        # print s['col_name'], s['col_value']
        c.updaeDb("UPDATE base_sys_config set CONFIG_VALUE = '%s' where CONFIG_KEY = '%s'" % (s['col_value'], s['col_name']))

    # 添加租户
    addUserPlatform()
    sleep(4)
    # 添加学校
    addSchool()
    # 添加教室
    for flag in range(len(classroom_para)):
        print classroom_para[flag]['classroomname'], classroom_para[flag]['classaccnumber']
        addclassromm(classroom_para[flag]['classroomname'].decode('utf-8'), classroom_para[flag]['classaccnumber'].decode('utf-8'))
    # 添加设备
    for each_terminal in classroom_para:
        addterminal(each_terminal['classroomname'].decode('utf-8'),
                    each_terminal['equipment_name'].decode('utf-8'),
                    each_terminal['equipmentmodel'].decode('utf-8'),
                    each_terminal['ipaddr'].decode('utf-8'),
                    each_terminal['locaddr'].decode('utf-8'),
                    each_terminal['equipmentlogname'].decode('utf-8'),
                    each_terminal['equipmentlogpwd'].decode('utf-8'),
                    each_terminal['equimenttype'].decode('utf-8'))

        # print "add >>", each_terminal['classroomname'], "<< OK!"
    # 添加老师用户
    adduser()
    # 配置平台消息中间件
    add_interact(middle_interact_ip)
    conf_local_interact(middle_interact_ip)
    # 配置节点消息中间件
    add_interact(node_interact_ip)
    cfg_interact(node_interact_ip, middle_interact_ip)
    添加MCU
    add_mcu('10.1.0.85', '80', 'POLYCOM', 'POLYCOM')
    # interact管理配置
    cfg_mcu()
