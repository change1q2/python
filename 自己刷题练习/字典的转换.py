"""
============================
作者:seak
时间:
邮件:274882401@qq.com
作用：
题目：字典转换成字符串
============================
"""
#字典转换成字符串dict——>str
#对于字典转换字符串，需要先生成list和tuple，然后再由list和tuple生成str
# dic1 = {'a':1,'b':2,'c':3}
# for i in dic1:
#     lis = []

# - dict——->list/tuple/set
# 字典可以使用 dict.keys() 和dict.values()返回迭代器，通过list和tuple直接生成列表和元祖
dic1 = {'a':1,'b':2,'c':3}
print(list(dic1.keys())) #获取到key值并放到列表中
print(list(dic1.values()))#获取到values值并放到列表中

print(tuple(dic1.keys()))#获取到key值并放到元祖中
print(tuple(dic1.values()))#获取到values值并放到元祖中

print(set(dic1.keys()))#获取到key值并放到集合中
print(set(dic1.values()))#获取到values值并放到集合

#items() 函数以列表返回可遍历的(键, 值)
print(tuple(dic1.items()))  #生成元祖为单位的元祖
print(list(dic1.items()))  #生成元祖为单位的列表
print(set(dic1.items()))   #生成元祖为单位的集合