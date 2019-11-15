"""
============================
作者:seak
时间:
邮件:274882401@qq.com
作用：
题目：1、上课的手机类继承代码自己敲一遍进行提交，
============================
"""
#生成一个手机类作为父类，大哥大
class BasePhone:

    def call_phone(self):#定义拨打语音的一个方法
        print("这个是拨打电话语音的功能")

#生成一个新类,继承BasePhone里面的方法，功能机
class PhoneV1(BasePhone):

    def dislay_music(self):
        print("音乐功能")

    def send_msg(self):
        print("发送信息功能")

#生成一个新的类，智能机，继承大哥大和功能机的功能
class PhoneV2(PhoneV1):

    #重写父类
    def call_phone(self):
        print("拨打视频电话")
        print("拨打视频电话5分钟，自动切换为语音通话")

        #调用父类的同名方法，有两种方式推荐使用suoer方式
        #BasePhone.call_phone(self)
        # 父类名.方法

        #定义一个游戏方法
        def game(self):
            print("打游戏")

phone = PhoneV1()#调用PhoneV1()继承的类
phone.call_phone()