import demo_c
import unittest

# j = demo_c.Count(2, 3)
# print j.add()


class Testcount(unittest.TestCase):
    def setUp(self):
        print "test start"

    def test_add(self):
        j = demo_c.Count(1, 4)
        self.assertEqual(j.add(), 5)

    def test_add1(self):
        j = demo_c.Count(112, 4)
        self.assertEqual(j.add(), 116, msg="The test result is not Ture")

    def tearDown(self):
        print "test end"
if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(Testcount("test_add"))
    suite.addTest(Testcount("test_add1"))
    runner = unittest.TextTestRunner()
    runner.run(suite)
