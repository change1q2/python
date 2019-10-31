"""
============================
Author:柠檬班-木森
Time:2019/10/30
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""
users = [{"name": "py01", "pwd": "123"},
         {"name": "py02", "pwd": "123"},
         {"name": "py03", "pwd": "123"},
         {"name": "py04", "pwd": "123"}]
#
# # 需求：查找"py03"这个用户是否在列表中
#
for item in users:
    print(item)
#     # 判断字典的name键对应的值是否为py03
#     if item['name'] == "py03":
#         print('找到了该用户')
#         break
#         # continue
#
#     print('比对完用户{}'.format(item))
# else:
#     print("没有找到py03这个用户")


# for循环的嵌套使用

"""
打印如下图形

1
1 2
1 2 3
1 2 3 4
1 2 3 4 5


*
* *
* * *
* * * *


"""
# 外层循环遍历行数
for i in range(1, 6):
    # print(i)
    # 内层循环，根据行数打印该列的数据，第1行，打印1，第二行，打印1，2 第三行，打印1，2，3,...）
    for j in range(1, i + 1):
        print('{} '.format(j), end='')
    print('')








for i in range(1, 6):
    # print(i)
    # 内层循环，根据遍历的行数打印数据（根据行数打印数据，第1行，打印1，第二行，打印1，2 第三行，打印1，2，3,...）
    for j in range(1, i + 1):
        print("* ", end='')
    print('')