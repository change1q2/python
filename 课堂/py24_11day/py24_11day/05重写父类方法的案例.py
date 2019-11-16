"""
============================
Author:柠檬班-木森
Time:2019/11/11
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""


class BasePhone:

    def call_phone(self):
        print("这个是拨打语言电话的功能")

    def display_music(self):
        print("播放音乐")

    def send_msg(self):
        print("发送信息")


# 需求二：功能机（2005年左右
class PhoneV1(BasePhone):

    def send_msg(self):
        super().send_msg()
        print("在发短信的基础上，根据需求扩展新的功能")