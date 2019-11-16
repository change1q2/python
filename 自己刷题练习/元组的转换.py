"""
============================
作者:seak
时间:
邮件:274882401@qq.com
作用：
题目：元祖的转换
============================
"""
#元祖的转换

#元祖转换为列表tuple——->list
# tuple1 = (1,2,3,4,5,'2','a')
# print(list(tuple1))
#
# #元祖转换成字符串tuple——–>str
# tuple1 = ('1','2','3','4','5','2','a')
# print(''.join(tuple1))

#元祖转换为字典tuple——>dict
#也是通过zip实现map映射的
# tuple1 = ('1','2','3','4')
# tuple2= ('a','b','c','d')
# dict1 = dict(zip(tuple1,tuple2))
# print(dict1)

#元祖转换为集合tuple——>set
tuple1 = ('1','2','3','4','1','2')
print(set(tuple1))