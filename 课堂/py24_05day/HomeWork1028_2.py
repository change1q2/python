"""
============================
作者:seak
时间:
邮件:274882401@qq.com
作用：
题目： 2、输入一个 5 位数，判断它个位与万位相同，十位与千位相 同。 根据判断打印出相关信息，
          相同打印结果：该数据符合规范，
          不相同打印：该数据不符合规范
============================
"""

'''
#没要求一次输入可以分为5此输入
num1 = input("输入一个5位数的第万位：")
num2= input("输入一个5位数的第千位：")
num3 = input("输入一个5位数的第百位：")
num4 = input("输入一个5位数的第十位：")
num5 = input("输入一个5位数的第个位：")
num = num1 + num2 + num3 + num4 + num5  #这是进行的拼接不是加法运算
#print(num)
if num4 == num2:
    print("该数据符合规范")
else:
    print("该数据不符合规范")
'''

12345
#如果要求一次输入,
#疑问如何获取一个数的每个下标索引值
num = input("输入一个5位数：")
str = num
str[4]
if (str[4] == str[0]) and (str[3] == str[1]):
    print("该数据符合规范")
else:
    print("该数据不符合规范")
