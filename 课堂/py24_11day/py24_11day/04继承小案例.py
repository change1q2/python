"""
============================
Author:柠檬班-木森
Time:2019/11/11
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""
"""
继承的作用，提高代码的重用率

重写父类方法：在子类中定义一个和父类同名的方法，这个操作叫重写父类方法

在子类中调用父类同名的方法：
方式一：父类名.方法名（self）
方式二：super().方法名（）
推荐使用：方式二





"""


#  需求一，大哥大手机（1995）
class BasePhone:

    def call_phone(self):
        print("这个是拨打语言电话的功能")


# 需求二：功能机（2005年左右
class PhoneV1(BasePhone):

    def display_music(self):
        print("播放音乐")

    def send_msg(self):
        print("发送信息")


# 需求三：智能机（2019）
class PhoneV2(PhoneV1):

    # 重写父类方法
    def call_phone(self):
        print("拨打视频电话")
        print("视频电话5分钟后，切换语言通话")
        # 调用父类的同名方法，
        # BasePhone.call_phone(self)
        super().call_phone()


    def game(self):
        print("打游戏")


phone = PhoneV2()
phone.call_phone()
# phone.display_music()
# phone.game()

