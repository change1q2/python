"""
============================
Author:柠檬班-木森
Time:2019/11/6
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""

"""
try:
    不可控的因素造成的错误，需要使用try来进行异常捕获
    # 用户输入
    
    # 打开文件，文件不存在
    
    # 发送网络请求，网络超时
    
    
except:

else:

finally:

"""

try:
    # try下面写有可能会出现异常的代码
    score = int(input("请输入成绩："))
except:
    # 处理异常之后的处理，
    print("用输入的数据不符合规范，默认给0分")
    score = 0
else:
    # 代码没有出现异常，执行else中的代码
    print("代码没有出现异常，执行esle")
finally:
    # 不管代码有没有出现异常都会去执行的代码
    print("finally不管代码有没有出现异常都会去执行的代码")




if score > 60:
    print('及格了')
else:
    print("你不及格，分数为{}".format(score))

print("程序的其他代码")
