"""
============================
Author:柠檬班-木森
Time:2019/10/28
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""

"""
条件循环

while 条件：
    循环体  

"""

# a = 10
#
# while a > 1:
#     print('条件成立，这里是循环体中的代码')
#     print('当前a的值是',a)
#     a -= 1
#
# print('这个不在循环体中，没有缩进')

# 需求：打印100遍hello python,
# 需求：第50遍打印两遍

number = 0
while number < 100:
    print('这是第{}遍打印,hello python'.format(number + 1))
    if number == 49:
        print('这是第{}遍打印,hello python'.format(number + 1))

    number += 1
