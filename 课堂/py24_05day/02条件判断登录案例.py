"""
============================
Author:柠檬班-木森
Time:2019/10/28
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""

"""
登录的小案例



关键字pass: 没有任何语义，占个位置，表示通过的意思

"""
user = {"user": "python24", "pwd": "lemonban"}

username = input("请输入账号")
password = input("请输入密码")

# if username == user['user']:
#     if password == user['pwd']:
#         print("账号密码正确，登录成功")
#     else:
#         print("用户密码有误")
# else:
#     print("用户名不存在")


# 同时判断多个条件（逻辑运算符）
# and   or

if username == user['user'] and password == user['pwd']:
    print("用户登录成功")
else:
    print("账号名或者密码有误！")
