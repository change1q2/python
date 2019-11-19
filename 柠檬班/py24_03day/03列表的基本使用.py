"""
============================
Author:柠檬班-木森
Time:2019/10/23
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""

"""
列表：列表是一种可变的数据类型
列表的定义：[]  




"""

# 列表可以通过下标索引取值
# li = [19, 1.3, "python"]
# print(li[2])

# 列表的切片操作
# li1 = [11, 22, 33, 44, 55]
# print(li1[::2])

# 列表中的增删查改的方法，
# li2 = [1, 2, 3]

# 增加元素的方法:append,insert extend
# append：往列表结尾处添加一个元素（追加）
# li2.append("11")

# insert:通过下标指定位置，往列表中加入元素
# li2.insert(1, 999)

# extend:一次性加入多个元素（放在列表的结尾处）
# li2.extend([11, 22, 33])
# print(li2)

# 删除元素的方法： remove  pop  clear
# remove:删除指定的元素(删除找到的第一个)
# li3 = [1, 2, 3, 11, 22, 33, 1, 2, 3]
# li3.remove(1)

# pop方法:指定下标位置进行删除（没有指定下标位置，默认删除的是最后一个）
# li3.pop(3)

# clear:清空列表
# li3.clear()

# print(li3)

# 查找的方法:
# index:查找指定元素的下标，找到了返回下标值，没有找到报错
# res = li3.index(11)
# print(res)

# count:统计列表中某个元素出现的次数
# res2 = li3.count(1)
# print(res2)

# li4 = ["aa", "bb", 11, 22, 33]
# 修改列表中某个元素的值
# 通过下标去指定元素，进行重新赋值
# li4[1] = 999
#
# print(li4)


# 其他的方法
# sort:排序
li5 = [111, 22, 31, 41, 5, 6, 888, 8, 34, 8, 12, 7, 33]

# 对列表进行升序排序
# li5.sort()
# 通过参数(reverse=True)可以指定从大到小，降序排序
# li5.sort(reverse=True)
# print(li5)

# 将列表反转（头变成尾，尾变成头）
# li5.reverse()
# print(li5)

# copy方法：复制(将原有的列表在内存复制一遍)
# li6 = li5
# li7 = li5.copy()
#
# print(id(li5))
# print(id(li6))
# print(id(li7))



#  身份运算符 和成员运算符
