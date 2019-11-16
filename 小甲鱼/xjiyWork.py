#coding:utf-8
"""
============================
作者:seak
时间:
邮件:274882401@qq.com
作用：
题目： 编写一个函数power()模拟内建函数pow()，即power(x, y)为计算并返回x的y次幂的值。
============================
"""
def func(x,y):
  #  x = int(input("输入第一个数："))
   # y = int(input("输入第二个数："))
    res = x ** y
    return res
x = int(input("输入第一个数："))
y = int(input("输入第二个数："))
rest = func(x,y)
print(rest)
