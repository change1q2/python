"""
============================
作者:seak
时间:
邮件:274882401@qq.com
作用：
题目：0. 编写一个函数，判断传入的字符串参数是否为“回文联”
（回文联即用回文形式写成的对联，既可顺读，也可倒读。例如：上海自来水来自海上）VA6
============================
"""


def same_data():
    a = input("请输入一段话：")
    list = ["a"]
    if list[0:3] == list[-8:-5]:
        print("是回文联")
    else:
        print("不是会文联")