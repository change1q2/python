"""
============================
Author:柠檬班-木森
Time:2019/11/6
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""
"""
os模块：python内置的模块

os.path.dirname:获取文件或目录，所在的父类目录路径
os.path.join:路径拼接



魔法变量：

1、__file__: 代表当前文件的绝对路径


2、__name__:
    如果当前文件值程序的启动文件中，它的值是 __main__
    如果不在启动文件中，代表的就是所在的文件（模块）的模块名
"""

#  魔术变量的操作
# print('当前运行文件中打印的__name__：',__name__)
# import ostest


import os

# 路径的处理
print(__file__)

#获取文件/目录所在的父级目录
dir = os.path.dirname(__file__)
print(dir)

#获取父级目录的上一级目录
BASEDIR = os.path.dirname(dir)
print(BASEDIR)


file_path = os.path.join(BASEDIR,r"py24_02day\task_01day.py")

print(file_path)
# # C:/project/py24_class\py24_02day\task_01day.py
# # with open(r'C:\project\py24_class\py24_02day\task_01day.py') as f:
# #     pass
#
# with open(file_path) as f:
#     pass