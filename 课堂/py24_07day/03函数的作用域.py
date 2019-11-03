"""
============================
Author:柠檬班-木森
Time:2019/11/1
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""

"""
全局变量：直接定义在py文件中的变量，叫全局变量，在该文件中任何地方都可以使用
局部变量：在函数内部定义的变量，叫做局部变量，只能在该函数内部使用，函数外部无法使用


"""
# 定义一个全局变量
# name = "musen"
#
#
# def func():
#     # 定义一个局部变量
#     a = 100
#     print(a)
#     print(name)
#
#
#
# func()
# print(name)


"""
变量的查找过程：由内到外（先找自身的，没有再去外面找）

"""
# aa = 10
#
#
# def func():
#     # aa = 100
#     print(aa)
#
# func()


"""

如何在函数内部去修改全局变量？
global:在函数内部声明全局变量

"""

aa = 10


def func():
    global aa, cc
    aa = aa + 1
    print(aa)
    cc = 99
    # print(aa)
    # aa = 100


func()

print(aa)
print(cc)
