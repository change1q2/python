"""
============================
作者:seak
时间:
邮件:274882401@qq.com
作用：
题目：3、类中__init__方法在什么时候调用的？（简答）
============================
"""

#类中__init__方法在什么时候调用的？（简答）
'''

#在参数传递过程中使用
class GirlFriend: # 女朋友类
    gender = "女" #类属性


    def __init__(self, name, face, height, leg):  # 初始化方法，self代表本函数自身
        #实列属性
        self.name = name
        self.face = face
        self.height = height
        self.leg = leg
obj1 = GirlFriend('小花', "好看", 168, "一米")



'''