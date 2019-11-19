"""
============================
Author:柠檬班-木森
Time:2019/10/28
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""

"""
for 循环：遍历循环


range():
range(n):默认生成一个 0到n-1的整数序列，对于这个整数序列，
我们可以通过list()函数转化为列表类型的数据。

range（n,m)：默认生成一个n到m-1的整数序列，对于这个整数序列，
我们可以通过list()函数转化为列表类型的数据。

range(n,m,k)：相当于其他函数里面的for循环。n 初始值  m 结束值 
 k 步长，会生成初始值为n,结束值为m-1,递减或者是递增的整数序列。
    

"""

# li = ["小明", "小张", "小李"]
#
# for name in li:
#     print(name)
#     print("循环体：hello python")

# 打印一百遍：hello python
# li2 = list(range(100))
# print(li2)
# 遍历列表
# for i in li2:
#     print('第{}遍，hello python'.format(i+1))

# 遍历range
# for i in range(100):
#     print(i)
#     print('第{}遍，hello python'.format(i + 1))


# 遍历字符串
# s = "abchgd"

#  i   n   item  v  k  j
# for i in s:
#     print(i)
'''
#  遍历字典
dic = {"aa": 11, "bb": 22, "cc": 33}

# 1、直接遍历字典：得到的是字典的键
for i in dic:
     print(i)

#1-2遍历字典的键
print("*"*10)
for k in dic.keys():
     print(k)
'''


#2、遍历字典的值
dic = {"aa": 11, "bb": 22, "cc": 33}
for v in dic.values():
     print(v)



# 3、遍历字典的键值对
print("*"*10)
for k, v in dic.items():
     print(k)
     print(v)



'''
#元祖拆包
t = (111, 222)
a, b = t
print(a)
print(b)
# 同时定义2个变量
aa, bb = 888, 999
print(aa, bb)
'''
