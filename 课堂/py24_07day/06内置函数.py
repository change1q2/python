"""
============================
Author:柠檬班-木森
Time:2019/11/1
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""

#len：获取 列表\字符串\元组\字典 中的元素总数量（数据的长度）
# s1 = "asdfoifjashf"
# print(len(s1))
# li = [11, 22, 33, 44, 55]
# print(len(li))
# dic = {"q": 11, "d": 11, "c": 333}
# print(len(dic))

# li = [11, 22, 33, 44, 55]
# # max():获取数据中元素的最大值
# print(max(li))
# # min():获取数据中元素的最小值
# print(min(li))
# # sum()：对元素进行求和
# print(sum(li))


# eval：识别字符串中的python表达式
# li = "[11,22,33]"
# eval(li)  # ====>[11,22,33]
dic = "{'a':11,'b':22}"
eval(dic)
print(dic)
# s3 = "print('python666')"
# eval(s3)  # ====》print('python666')
# s4 = "python"
# eval(s4) # ===>python
#
# s1 = "[11,22,33]"
s2 = "{'a':11,'b':22}"
# s3 = "print('python666')"
#
# print('------')
# print(res,type(res))


#  #zip: 聚合打包
li = ["name", "age", "gender","8888","sadasd"]
li2 = ["木森", 18, "男"]

# 把上面的列表转换为一个字典？li中的元素作为键，li2中的元素作为值

res2 = zip(li, li2)
print(list(res2))
#
print(dict(res2))
