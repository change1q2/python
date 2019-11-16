"""
============================
Author:柠檬班-木森
Time:2019/11/8
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""
"""
# 类里面应该有该类事务共同的特征和行为
特征：属性
行为：方法

方法：定义在类里面的函数
方法的调用：对象.方法名（）

self：代表的是对象本身，那个对象去调用该方法，那么self代表的就是那个对象


"""

#方法：定义在类里面的函数
class GirlFriend:    # 女朋友类
    gender = "女"

    # 初始化方法
    def __init__(self, name, face, height, leg):
        # 对象.属性名 = 属性值
        self.name = name
        self.face = face
        self.height = height
        self.leg = leg

    def skill1(self):#定义一个skill方法
        # print(self)
        print("{} 在买东西".format(self.name))




obj1 = GirlFriend('小花', "好看", 168, "一米")
obj2 = GirlFriend('小红', "很好看", 168, "一米一")

# print(obj1.name)
# print(obj2.name)
# print(obj1)
#方法的调用：对象.方法名（）
obj1.skill1()

print('-------------------------------------')
# print(obj2)
obj2.skill1()



