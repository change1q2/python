"""
============================
作者:seak
时间:
邮件:274882401@qq.com
作用：
题目：
============================
"""

# old = [1,2,3,4,5]
# new = old
# old = [6]
# print(new)

#1. 请问如何将下边这个列表的'小甲鱼'修改为'小鱿鱼'？
list= [1, [1, 2, ['小甲鱼']], 3, 5, 8, 13, 18]

# #拆开单层
# for i in list1:
#     print(i)

#拆开2层，用sum

# list1 = [[1, 2], [3, 4, 5], [6, 7], [8], [9]] ;
# list3 = sum(list1,[])
# print(list3)

#拆开复杂层 3层，使用递归的方式
#list= [1, [1, 2, ['小甲鱼']], 3, 5, 8, 13, 18]
# list =[1,[2],[[3]],[[4,[5],6]],7,8,[9]]
# def flat(nums):
#     res = []
#     for i in nums:
#         if isinstance(i,list):
#             res.extend(flat(i))
#         else:
#             res.append(i)
#     return res
#
# print(flat)

#层层套取
list1 = [1, [1, 2, ['小甲鱼']], 3, 5, 8, 13, 18]
list1[1][2][0] = '小鱿鱼' #取list1的下标， 开始第一层0，1 ； 第二层 ：0，1，2；第三层 ：0