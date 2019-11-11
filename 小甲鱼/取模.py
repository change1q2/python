#coding:utf-8

"""
============================
作者:seak
时间:
邮件:274882401@qq.com
作用：
题目：
============================
"""
#欧几里得算法
def gcd(a,b):
    while a != 0:
        a,b = b%a,a
    return b

a = int(input("请输入第一个数："))
b = int(input("请输入第二个数："))
res = gcd(a,b)
print("最大公约数为：",res)