"""
============================
Author:柠檬班-木森
Time:2019/10/30
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""
"""
函数的返回值：return

函数的返回值是由return来决定的，return后面写什么，函数的返回值就是什么。
函数中没有return:函数的返回值默认位 None
return 后面没有任何内容，返回值也是None
函数要返回多个数据：再return后面 每个数据之间用逗号隔开,调用函数之后接收到的是个元组形式的数据


return的作用2：结束函数的运行
    只要函数中执行到return,就直接返回内容，跳出函数体

"""


def func():
    print('python666')
    # return "python24期666"
    return [666, 999, 555]
    # print("99999999999999999999")


res = func()
print(res)
