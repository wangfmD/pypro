# coding=utf-8
from selenium import webdriver
from time import sleep


def adomin_login():
    driver = webdriver.Chrome()
    driver.implicitly_wait(30)
    base_url = 'http://10.1.0.47'
    driver.get(base_url + "/middlecas/login?service=http://10.1.0.47:8080/middleclient/shiro-cas")
    driver.find_element_by_id('s_username').clear()
    driver.find_element_by_id('s_username').send_keys('administrator')
    driver.find_element_by_id('s_password').clear()
    driver.find_element_by_id('s_password').send_keys('xungejiaoyu')
    driver.find_element_by_name('submit').click()

    sleep(50)

if __name__ == '__main__':
    adomin_login()
