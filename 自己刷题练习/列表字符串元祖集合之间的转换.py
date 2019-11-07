#coding:utf-8
"""
============================
作者:seak
时间:
邮件:274882401@qq.com
作用：
题目：列表，字符串，元祖，字典，集合的转换
============================
"""
#list-----set  列表转集合 （去重）
list1 = [6, 7, 7, 8, 8, 9]
li2 = set(list1)
print(li2)

#两个列表转字典

list1 = ['key1','key2','key3']
list2 = ['1','2','3']
dic = dict(zip(list1,list2))  #zip集合打包
print(dic)

#嵌套列表转字典
list3 = [['key1','value1'],['key2','value2'],['key3','value3']]
dic2 = dict(list3)
print(dic2)

# 列表、元组转字符串 用jion 拼接
list2 = ['a', 'a', 'b']
str1 = ''.join(list2)
print(str1)

tup1 = ('a', 'a', 'b')
str2 = ''.join(tup1)
print(str2)