"""
============================
Author:柠檬班-木森
Time:2019/11/6
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""
import os


"""
linux：

os.getcwd():pwd    获取当前的工作路径 

os.chdir:cd      切换工作路径

os.mkdir():mkdir:  创建文件夹

os.listdir:ls   获取当前工作路径下，所有的文件和目录   

"""
# 获取当前的工作路径
# print(os.getcwd())
# 切换工作路径
# os.chdir("..")
#
# print(os.getcwd())
#
# os.chdir("..")
#
# print(os.getcwd())
# 创建文件夹

# os.mkdir('python6666')
# 获取当前工作路径下，所有的文件和目录
# print(os.listdir())

# 给定一个路径，判断是否是目录的路径
res = os.path.isdir(r'C:\project\py24_class\py24_02day')
print(res)
# 给定一个路径，判断是否是文件的路径
res2 = os.path.isfile(r'C:\project\py24_class\py24_02day\task_01day.py')
print(res2)















