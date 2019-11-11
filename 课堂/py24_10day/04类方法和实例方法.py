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

对象方法（实例方法）：
实例方法的定义：直接定义在类里面的函数
第一个参数是self，self代表的是对象本身
实例方法的调用：对象.方法名


类方法：
类方法定义：要通过classmethod装饰器来声明一个类方法
第一个参数是cls，cls代表的是类本身
类方法的调用：类名.方法名   对象.方法名

"""


class GirlFriend:
    # 女朋友类
    gender = "女"

    def __init__(self, name, face, height, leg):# 初始化方法

        self.name = name # 实列属性
        self.face = face
        self.height = height
        self.leg = leg
        # 对象.属性名 = 属性值

    def skill1(self):
        # print(self)
        print("{} 在买东西".format(self.name))

    def skill2(self):
        print("看电视")

    @classmethod  # 通过classmethod装饰器，声明一个类方法
    def cls_func(cls):
        print(cls)
        print("这个是类方法")


obj1 = GirlFriend('小花', "好看", 168, "一米")
obj2 = GirlFriend('小红', "很好看", 168, "一米一")

# 类方法的调用
# print(GirlFriend)
# GirlFriend.cls_func()
# obj1.cls_func()

# 实例方法的调用
obj1.skill1()

# 类不能够去调用实例方法的
# GirlFriend.skill1()









