"""
============================
作者:seak
时间:
邮件:274882401@qq.com
作用：
题目：
5、封装一个测试用例类(自行分辨定义为类属性还是实例属性)，
-  属性：用例编号  url地址   请求参数   请求方法    预期结果   实际结果
============================
"""
class TestCase:


    def __init__(self,case,url,data,method,excepted,actual):#初始化函数self后面所有写满
        self.case = case
        self.url = url
        self.data = data
        self.method = method
        self.excepted = excepted
        self.actual = actual
    def cases_info(self):#定义一个实列
        return ("测试用例格式：测试编号为:{}\nurl地址为:{}\n请求参数为:{}\n请求方法为:{}\n实际结果为:{}\n预期结果为:{}\n".
              format(self.case,self.url,self.data,self.method,self.excepted,self.actual))

test = TestCase('01','https://aml.mytaiwanbusiness.com','1','get','测试通过','测试通过')
print(test.cases_info())

