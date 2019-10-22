"""
============================
Author:柠檬班-木森
Time:2019/10/21
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""
#  导入随机数模块
# import random

# 指定范围生成一个随机整数数(包含边界值的)
# num = random.randint(1, 3)
# print(num)

# 随机生成一个0-1之间的小数（边界值包含0,不包含1）
# num1 = random.random()
# print(num1)

# 如何生成10-20之间的小数


# 源码查看的方式：ctrl + 鼠标左键点击


# 解决浮点数运算的精度问题
import decimal

a = 2.89
b = 0.3
print(a-b)


aa = decimal.Decimal('2.89')
bb = decimal.Decimal('0.3')

print(aa-bb)
