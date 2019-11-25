"""
============================
作者:seak
时间:
邮件:274882401@qq.com
作用：
题目：

	注册成功               返回结果：{"code": 1, "msg": "注册成功"}
	有参数为空，            返回结果 {"code": 0, "msg": "所有参数不能为空"}
	两次密码不一致          返回结果：{"code": 0, "msg": "两次密码不一致"}
	账户已存在             返回结果：{"code": 0, "msg": "该账户已存在"}
	密码不在6-18位之间      返回结果：{"code": 0, "msg": "账号和密码必须在6-18位之间"}
	账号不在6-18位之间      返回结果：{"code": 0, "msg": "账号和密码必须在6-18位之间"}

============================
"""
#编辑测试用例
import unittest

#定义一个测试用例类
from homework.py13.register import register


class LoginTestRegister(unittest.TestCase):
    #定义4个必写方法
    def setUp(self):
        # 每条用例执行之前都会执行
        print("用例{}开始执行--".format(self))

    def tearDown(self):
        # 每条用例执行之后都会执行
        print("用例{}执行结束--".format(self))

    @classmethod
    def setUpClass(cls):
        # 当成测试用例类中的用例执行之前，会执行改方法
        print("-----setup---classs-----")

    @classmethod
    def tearDownClass(cls):
        # 当成测试用例类中的用例执行完毕，会执行改方法
        print("-----teardown---classs-----")

#准备各种测试用例
    def test_register(self):
        """正常注册"""
        # 第一步：准备用例数据
        # 1、用例的参数：
        data = ('python1', '123456', '123456')
        # 2、预期结果：
        excepted = {"code": 1, "msg": "注册成功"}
        # 调用被测试的功能函数，传入参数，获取实际结果
        result = register(*data)
        # 比对预期结果，和实际结果是否一致
        self.assertEqual(excepted, result)

    def test_password_dis(self):
        """两次密码不一致"""
        # 第一步：准备用例数据
        # 1、用例的参数：
        data = ('python1', '123456', '1234567')
        excepted = {"code": 0, "msg": "两次密码不一致"}
        # 2、预期结果：
        excepted = {"code": 0, "msg": "两次密码不一致"}
        # 调用被测试的功能函数，传入参数，获取实际结果
        result = register(*data)
        # 比对预期结果，和实际结果是否一致
        self.assertEqual(excepted, result)

    def test_user_register(self):
        """账号已经被注册"""
        # 第一步：准备用例数据
        # 1、用例的参数：
        data = ('python23', '1234567', '1234567')
        # 2、预期结果：
        excepted = {"code": 0, "msg": "该账号已存在"}
        # 调用被测试的功能函数，传入参数，获取实际结果
        result = register(*data)
        # 比对预期结果，和实际结果是否一致
        self.assertEqual(excepted, result)

    def test_password_lt6(self):
        """密码小于6"""
        # 预期结果
        excepted = {"code": 0, "msg": "账号和密码必须在6-18位之间"}
        # 参数：data
        data = ('python3', '12345', '12345')
        # 调用被测试的功能函数，传入参数，获取实际结果
        res = register(*data)
        # 比对预期结果，和实际结果是否一致
        self.assertEqual(excepted, res)

    def test_password_gt18(self):
        """密码大于18"""
        # 预期结果
        excepted = {"code": 0, "msg": "账号和密码必须在6-18位之间"}
        # 参数：data
        data = ('python3', '8888888888888888888', '8888888888888888888')
        # 调用被测试的功能函数，传入参数，获取实际结果
        res = register(*data)
        try:
            # 比对预期结果，和实际结果是否一致
            self.assertEqual(excepted, res)
        except AssertionError as e:
            print('该用例测试未通过')
            raise e
        else:
            print('该用命测试通过')

    def test_user_lt6(self):
        """账号长度小于6"""
        # 预期结果
        excepted = {"code": 0, "msg": "账号和密码必须在6-18位之间"}
        # 参数：data
        data = ('py01', '1234567', '1234567')
        # 调用被测试的功能函数，传入参数，获取实际结果
        res = register(*data)
        # 比对预期结果，和实际结果是否一致
        self.assertEqual(excepted, res)

    def test_user_gt18(self):
        """账号长度大于18"""
        # 预期结果
        excepted = {"code": 0, "msg": "账号和密码必须在6-18位之间"}
        # 参数：data
        data = ('pythonpytheon2342455322q2223', '1234567', '1234567')
        # 调用被测试的功能函数，传入参数，获取实际结果
        res = register(*data)
        try:
            # 比对预期结果，和实际结果是否一致
            self.assertEqual(excepted, res)
        except AssertionError as e:
            print('该用例测试未通过')
            raise e
        else:
            print('该用例测试通过')

    def test_user_is_none(self):
        """账号为空"""
        # 预期结果
        excepted = {"code": 0, "msg": "账号和密码必须在6-18位之间"}
        # 参数：data
        data = (None, '1234567', '1234567')
        # 调用被测试的功能函数，传入参数，获取实际结果
        res = register(*data)
        try:
            # 比对预期结果，和实际结果是否一致
            self.assertEqual(excepted, res)
        except AssertionError as e:
            print('该用例测试未通过')
            raise e
        else:
            print('该用例测试通过')

    def test_password_is_none(self):
        """密码为空"""
        # 预期结果
        excepted = {"code": 0, "msg": "账号和密码必须在6-18位之间"}
        # 参数：data
        data = ('python56', None, None)
        # 调用被测试的功能函数，传入参数，获取实际结果
        res = register(*data)
        try:
            # 比对预期结果，和实际结果是否一致
            self.assertEqual(excepted, res)
        except AssertionError as e:
            print('该用例测试未通过')
            raise e
        else:
            print('该用例测试通过')

