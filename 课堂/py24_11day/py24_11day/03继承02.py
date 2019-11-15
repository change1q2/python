"""
============================
Author:柠檬班-木森
Time:2019/11/11
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""


class BaseClass(object):
    money = 100000000

    def func(self):
        print("赚钱的方法，一次赚100万")


class ClassV1(BaseClass):
    # 通过继承可以获得父类的方法和属性
    pass


class ClassV2(ClassV1):
    pass


# c = ClassV1()
# print(c.money)
# c.func()


c2 = ClassV2()

print(c2.money)
c2.func()
