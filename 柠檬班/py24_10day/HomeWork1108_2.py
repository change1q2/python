"""
============================
作者:seak
时间:
邮件:274882401@qq.com
作用：
题目：2、实例方法中的self代表什么？（简答）
============================
"""
#、实例方法中的self代表什么？（简答）

'''
self：代表的是对象本身，那个对象去调用该方法，那么self代表的就是那个对象

class GirlFriend:    # 女朋友类
    def skill1(self):#定义一个skill方法,这里obj1对象来调用skill(self)方法，self代表obj1这个对象
        # print(self)
        print("{} 在买东西".format(self.name))
obj1 = GirlFriend('小花', "好看", 168, "一米")
obj1.skill1()
'''