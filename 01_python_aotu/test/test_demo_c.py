# coding:utf-8
import demo_c


class TestCount:
	'''doc'''
    def test_case_add(self):
        try:
            j = demo_c.Count(1, 4)
            add = j.add()
            assert (add == 5), 'addition result error!'
        except AssertionError as msg:
            print(msg)
        else:
            print('Test pass')

mytest = TestCount()
mytest.test_case_add()
