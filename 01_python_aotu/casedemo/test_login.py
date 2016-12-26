# coding = utf-8
import time
import os
from selenium import webdriver


def test_login_case():
    browser = webdriver.Chrome()
    base_url = "http://10.1.0.50/middlecas/login"
    url = "?service=http://10.1.0.50:8080/middleresource/shiro-cas"
    print "now access %s" % (base_url + url)
    browser.get(base_url + url)
    time.sleep(2)
    select = browser.find_element_by_tag_name("select")
    allOptions = select.find_elements_by_tag_name("option")
    # for option in allOptions:
    #    print "Value is: " + option.get_attribute("value")
    for option in allOptions:
        print "Value is: " + option.get_attribute("value")
        if option.get_attribute(
                'value') == 'f326c482-5c3f-4660-ab1b-434b09ee3a26':
            option.click()
    time.sleep(1)
    browser.find_element_by_id('s_username').send_keys('jssadmin')
    browser.find_element_by_id('s_password').send_keys('111111')
    time.sleep(1)
    browser.find_element_by_name('submit').click()
    time.sleep(5)
    browser.quit()


class TestRunner(object):
    def __init__(self, cases="./"):
        self.cases = cases

    def run(self):

        for filename in os.listdir(self.cases):
            if filename == "report":
                break
        else:
            os.mkdir(self.cases + '/report')

        # base_dir = os.path.dirname(os.path.dirname(__file__))
        now = time.strftime("%Y-%m-%d_%H_%M_%S")
        test_report = "nosetests " + self.cases + " --with-html --html-report=" + \
            self.cases + "report/" + now + "report.html"
        # print test_report
        os.system(test_report)


if __name__ == '__main__':
    test = TestRunner()
    test.run()
