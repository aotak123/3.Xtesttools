# -*- coding:utf-8 -*-

import unittest
import HTMLTestRunner

class CaseTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('this is setUpClass')

    def setUp(self):
        print('this is setUp')

    def test_01(self):
        print('this is case01')

    # @unittest.skip('CaseTest')#跳过这个case
    def test_02(self):
        print('this is case02')

    def tearDown(self):
        print('this is tearDown')

    @classmethod
    def tearDownClass(cls):
        print('this is tearDownClass')

if __name__ == '__main__':
    print('hello 123')
    # unittest.main()
    suite = unittest.TestSuite()
    suite.addTest(CaseTest('test_02'))
    suite.addTest(CaseTest('test_01'))
    # unittest.TextTestRunner().run(suite)
    html_file = "./report" +"result.html"
    fp = open(html_file,'wb')
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        title=u'test',
        description=u'用例执行情况:')
    runner.run(suite)
    fp.close()