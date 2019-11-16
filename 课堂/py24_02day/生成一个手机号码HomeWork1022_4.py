"""
============================
作者:seak
时间:2019
邮件:274882401@qq.com
作用：
题目;4、使用random模块和字符串拼接的方法，随机生成一个130开头的手机号码。
============================
"""
import random
num0 = "130"
res1 = random.randint(0,9)
num1 = str(res1)
res2 = random.randint(0,9)
num2 = str(res2)
res3 = random.randint(0,9)
num3 = str(res3)
res4 = random.randint(0,9)
num4 = str(res4)
res5 = random.randint(0,9)
num5 = str(res5)
res6 = random.randint(0,9)
num6 = str(res6)
res7 = random.randint(0,9)
num7 = str(res7)
res8 = random.randint(0,9)
num8 = str(res8)
PhoneNum = ''.join((num0,num1,num2,num3,num4,num5,num6,num7,num8))
print(PhoneNum)

