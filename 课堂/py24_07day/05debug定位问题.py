"""
============================
Author:柠檬班-木森
Time:2019/11/1
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""
"""
print调试：
断点打在报错的哪一行代码上，或者之前都是可以的

"""


a = 100
c = "10"


def func(a, b):
    # print(type(a), type(b))
    c = a + b

    print(c)


func(a, c)
