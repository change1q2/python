"""
============================
作者:seak
时间:
邮件:274882401@qq.com
作用：
题目：
============================
建立一个启动器
"""

#第一步，创建一个测试套件
import unittest

import testcase as testcase

from homework.py13 import testcases
from homework.py13.HTMLTestRunnerNew import HTMLTestRunner

suite = unittest.TestSuite()


#第二步，将测试用例，加载到测试套件中
loader = unittest.TestLoader()
suite.addTest(loader.loadTestsFromTestCase(testcases.LoginTestRegister))


#第三步，创建一个测试运行程序启动器
runner = HTMLTestRunner(stream=open("report.html", "wb"),  # 打开一个报告文件，将句柄传给stream
                        tester="seak",                    # 报告种显示的测试人员
                        description="python24第一份测试报告",        # 报告种显示描述信息
                        title="24期作业测试报告")                 # 报告的标题


#第四步，使用启动器
runner.run(suite)