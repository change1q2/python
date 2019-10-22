"""
============================
作者:seak
时间:
邮件:274882401@qq.com
作用：
题目：
============================
"""
#list.append(单个元素)：在list列表末端增加一个元素；
list = [1,2,3,4,5,6]
list.append(0)
print(list)

#list.extend([元素1，元素2])：在list列表末端增加多个元素；
list2 = [1,2,3,4,5,6]
list2.extend([11,22])
print(list2)

#list.insert(元素序号，元素)：在list列表任意位置增加一个元素
list3 = [1,2,3,4,5,6]
list3.insert(1,"你好")
print(list3)

#list.remove(元素)：从列表中删除一个元素，且并不要求此元素的位置；
list4 = [1,2,3,4,5,6]
list4.remove(2)
print(list4)

#list.pop(下标索引):  删除单个或多个元素，按位删除(根据索引删除)
list5 = [1,2,3,4,5,6]
list5.pop(2)
print(list5)

#del list[下标索引]：它是根据索引(元素所在位置)来删除
list6 = [1,2,3,4,5,6]
del list6[2]
print(list6)
