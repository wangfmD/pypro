# coding:utf-8
import unittest


# cmd进入当然runtest.py所在的目录执行以下：
# python runtest.py >> report/log.txt 2>&1
test_dir = './'
discover = unittest.defaultTestLoader.discover(test_dir, pattern='test*.py')

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(discover)
