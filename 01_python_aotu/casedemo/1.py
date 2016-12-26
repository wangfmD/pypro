# coding=utf-8
from pyse import Pyse, TestRunner
from time import sleep

def test_baidu():
    ''' baidu search key : pyse '''
    driver = Pyse("chrome")
    # driver.open("https://www.baidu.com")
    base_url = "http://10.1.0.50/middlecas/login"
    url = "?service=http://10.1.0.50/middleresource/index.do"
    driver.open(base_url + url)
    driver.type("id=>s_username", "jssadmin")
    driver.type("id=>s_password", "111111")
    # driver.click()

    sleep(10)
    assert "pyse" in driver.get_title()
    driver.quit()

if __name__ == '__main__':
    TestRunner().run()
