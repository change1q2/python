"""
============================
Author:柠檬班-木森
Time:2019/11/11
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""

"""
对象的.__dict__属性：获取对象的所有属性以字典的形式返回

动态属性设置：

内置函数：setattr（参数1，参数2，参数3）：
参数1：对象
参数2：给对象要设置属性名（字符串类型）
参数3：属性值



"""

# class Cases:
#     def __init__(self, case_id, title, url, data):
#         self.case_id = case_id
#         self.title = title
#         self.url = url
#         self.data = data

# data = {'case_id': 1, 'title': '用例1', 'url': 'www.baudi.com', 'data': '001'}

# 需求：字典中的key作为属性名，value作为属性值

# case = Cases(**data)
#
# print(case)


# 动态属性设置
# setattr
data = {'case_id': 1, 'title': '用例1', 'url': 'www.baudi.com', 'data': '001'}


# 定义一个类
class Cases:
    pass


# 创建了一个对象
case = Cases()

# 给case这个对象，设置一个name属性，值为python666
# setattr(case, "name", "python66")

#  data1:1   data2:2   data3:3  data4:4 ....  data10:10

# for i in range(1,11):
#     setattr(case,"data{}".format(i),i)
#
# print(case)

# print(case.__dict__)
# print(case.name)

for k, v in data.items():
    setattr(case, k, v)

print(case)

# 获取对象属性
getattr(case, "name")

# 删除对象属性
delattr(case, 'case_id')
