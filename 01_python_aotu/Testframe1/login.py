# -*- coding: utf-8 -*-
from selenium import selenium
import unittest, time, re

class login(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium("localhost", 4444, "*chrome", "http://10.1.0.44")
        self.selenium.start()
    
    def test_login(self):
        sel = self.selenium
    
    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
