"""
============================
Author:柠檬班-木森
Time:2019/11/2
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""
# 第一题：
# 1、直接定义在py文件（模块）中的遍历叫做全局变量，全局变量在该文件中任意地方都可以访问
# 2、定义在函数中的变量，叫做局部变量，局部变量只有在该函数内部才能访问
# 3、在函数中定义（或修改）全局变量，需要使用global进行声明
# 4、已经学过的python关键字
"""
学过的：20个

False:bool数据类型
True :bool数据类型
None :表示数据为空

and: 逻辑运算符：与 
or:  逻辑运算符：或
not:  逻辑运算符：非

is  :身份运算符 
in  :成员运算符
del :删除数据
pass :表示通过（一般用来占位的）

if    : 条件判断
elif  : 条件判断
else : 条件判断

while  :条件循环
for    :遍历循环
break  :用来终止循环的
continue :中止当前本轮循环  开启下一轮循环

def  ：定义函数
return ：函数返回值
global  ：定义全局遍历

"""

# 第二题
# 现在有以下数据，
li = ["{'a':11,'b':2}", "[11,22,33,44]"]


# 需要转换为以下格式：
li1 = [{'a': 11, 'b': 2}, [11, 22, 33, 44]]

# 请封装一个函数，按上述要求实现数据的格式转换

def work2(data):
    # 创建一个新列表
    new_list = []
    # 遍历列表中的数据
    for i in data:
        # 将数据使用eval进行转换
        res = eval(i)
        # 将将转换后的数据放入新列表
        new_list.append(res)
    # 返回转换后的数据
    return new_list

res = work2(li)
print(res)



# 有一组用例数据如下：
cases = [
    ['case_id', 'case_title', 'url', 'data', 'excepted'],
    [1, '用例1', 'www.baudi.com', '001', 'ok'],
    [4, '用例4', 'www.baudi.com', '002', 'ok'],
    [2, '用例2', 'www.baudi.com', '002', 'ok'],
    [3, '用例3', 'www.baudi.com', '002', 'ok'],
    [5, '用例5', 'www.baudi.com', '002', 'ok'],
]

# 需要转换为以下格式
res1 = [
    {'case_id': 1, 'case_title': '用例1', 'url': 'www.baudi.com', 'data': '001', 'excepted': 'ok'},
    {'case_id': 4, 'case_title': '用例4', 'url': 'www.baudi.com', 'data': '002', 'excepted': 'ok'},
    {'case_id': 2, 'case_title': '用例2', 'url': 'www.baudi.com', 'data': '002', 'excepted': 'ok'},
    {'case_id': 3, 'case_title': '用例3', 'url': 'www.baudi.com', 'data': '002', 'excepted': 'ok'},
    {'case_id': 5, 'case_title': '用例5', 'url': 'www.baudi.com', 'data': '002', 'excepted': 'ok'}
]
# 封装一个函数，完成上述数据转换的功能，并且将case_id大于3的用例数据过滤出来,得到如下结果
res = [
    {'case_id': 4, 'case_title': '用例4', 'url': 'www.baudi.com', 'data': '002', 'excepted': 'ok'},
    {'case_id': 5, 'case_title': '用例5', 'url': 'www.baudi.com', 'data': '002', 'excepted': 'ok'}
]


# 第三题：

# 要求一
def work3_1(datas):
    # 创建一个新的列表
    new_datas = []
    # 通过下标，获取新数据的key
    title = cases[0]
    # 遍历出第一行之外所有的数据
    for i in datas[1:]:
        # 将遍历的数据和key进行聚合打包，并转换为字典
        c = dict(zip(title, i))
        new_datas.append(c)
    # 返回转换之后的结果
    return new_datas


# 要求二
def work3_2(data):
    new_data = []
    for i in data:
        # 判断转换后数据的case_id是否大于3
        if i['case_id'] > 3:
            # 将转换后的数据，放到新列表中
            new_data.append(i)
    return new_data


work3_1(cases)


