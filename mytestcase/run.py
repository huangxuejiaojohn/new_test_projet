import unittest
from mytestcase import  trybaidu,tryTestfan
import  HTMLTestRunner


mycase = unittest.TestSuite() #多个测试用例集合到一起
mycase.addTest(unittest.makeSuite(trybaidu.MyFirtUnit))#加载多个测试用例到TestSuiite
mycase.addTest(unittest.makeSuite(tryTestfan.Testfan))
# runcase = unittest.TextTestRunner()

filename = 'result1.html'
fp = open(filename, 'wb')
runner = HTMLTestRunner.HTMLTestRunner(
    stream=fp,
    title='测试报告',
    description='用例执行情况：')
runner.run(mycase)
