"""
============================
作者:seak
时间:
邮件:274882401@qq.com
作用：
题目： 3、利用random函数生成随机整数，从1-9取出来。然后输入一个数字，
      来猜，如果大于，则 印大于随机数。小了，则打印小于随机数。如果相等，则打印等于随机数
============================
"""
import random

num = int(random.randint(1,9))
print("随机数为："+str(num))
num2 = int(input("输入一个数："))
if num > num2:
    print("小于随机数")
elif num == num2:
    print("等于随机数")
else :
    print("大于随机数")