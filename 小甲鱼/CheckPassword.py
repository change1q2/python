"""
============================
作者:seak
时间:
邮件:274882401@qq.com
作用：
题目： 请写一个密码安全性检查的代码代码：check.py

# 密码安全性检查代码
#
# 低级密码要求：
#   1. 密码由单纯的数字或字母组成
#   2. 密码长度小于等于8位
#
# 中级密码要求：
#   1. 密码必须由数字、字母或特殊字符（仅限：~!@#$%^&*()_=-/,.?<>;:[]{}|\）任意两种组合
#   2. 密码长度不能低于8位
#
# 高级密码要求：
#   1. 密码必须由数字、字母及特殊字符（仅限：~!@#$%^&*()_=-/,.?<>;:[]{}|\）三种组合
#   2. 密码只能由字母开头
#   3. 密码长度不能低于16位
============================
"""
def check():
    nums = '0123456789'
    char =r'''`!@#$%^&*()_+-=/*{}[]\|'";:/?,.<>''' #特殊符号要用""" """, r表示特殊符号不会被转换
    str = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    passwad =input("请输入需要检查的密码组合：")
    while (passwad.isspace() and len == 0): #isspace检查是不是空格  len==0 检查是不是为空
        passwad =input("你输入的密码有空格或者为空，请重新输入：")
        lenght = len(passwad)
        if lenght <= 8:
            flag_con = 0
            for each in nums:
                if each in nums:
                    flag_con +=1
                    break