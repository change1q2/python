"""
============================
Author:柠檬班-木森
Time:2019/11/4
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""
#  enumerate：获取列表/字符串/元祖/每个元素和对应的下标
li1 = [11, 22, 33, 44, 55, 66]
s = "sfsdgfsk"
li2 = enumerate(s)
print(list(li2))

# filter:过滤器函数
# 参数1：过滤的规则函数
# 参数2： 要被过滤的数据


# 并且将case_id大于3的用例数据过滤出来
# # res1 = [
#     {'case_id': 1, 'case_title': '用例1', 'url': 'www.baudi.com', 'data': '001', 'excepted': 'ok'},
#     {'case_id': 4, 'case_title': '用例4', 'url': 'www.baudi.com', 'data': '002', 'excepted': 'ok'},
#     {'case_id': 2, 'case_title': '用例2', 'url': 'www.baudi.com', 'data': '002', 'excepted': 'ok'},
#     {'case_id': 3, 'case_title': '用例3', 'url': 'www.baudi.com', 'data': '002', 'excepted': 'ok'},
#     {'case_id': 5, 'case_title': '用例5', 'url': 'www.baudi.com', 'data': '002', 'excepted': 'ok'}
# ]


# def func(data):
#     return data['case_id'] > 3
#
# #  使用过滤器对数据进行过滤
# data = filter(func, res1)
# print(list(data))


#
# res2 = filter(lambda x:x["case_id"]>3,res1)
# print(list(res2))
#
# # 上面过滤器执行的原理
# # list3 = []
# # for i in res1:
# #     result = func(i)
# #     if result:
# #         list3.append(i)
#
#
#
# #  匿名函数
#
# f = lambda x,y:x+y
#
# print(f(11,22))


























