"""
============================
Author:柠檬班-木森
Time:2019/11/4
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""
"""
文件操作

打开文件：open(参数1，参数2，参数3)
参数1：指定文件
参数2：打开的模式
    r:读取模式,如果被打开的文件不存在，直接报错
    a:追加写入（在文件中原有的内容最后追加写入），被打开的文件不存在，会自动创建一个
    w:覆盖写入（清空文件中原有的内容），被打开的文件不存在，会自动创建一个
    
    # 操作一些图片，视频等文件
    rb:读取模式,如果被打开的文件不存在，直接报错(以二进制模式去打开文件)
    ab:追加写入（在文件中原有的内容最后追加写入），被打开的文件不存在，会自动创建一个(以二进制模式去打开文件)
    wb:覆盖写入（清空文件中原有的内容），被打开的文件不存在，会自动创建一个(以二进制模式去打开文件)

    
参数3：编码方式（"utf-8"）




"""
# 打开一个文件，返回一个操作的句柄
# f = open(file="text.txt", mode="r", encoding="utf-8")

# 读取内容

# 第一种：读取全部的内容
# content = f.read()
# print(content)

# 第二种：读取一行内容
# data = f.readline()
# print(data)

# 第三种：把所有的内容按行读取出来放在列表中
# data2 = f.readlines()
# print(data2)


# 文件写入
# f = open(file=r"C:\project\py24_class\py24_01day\test.txt",mode="a",encoding="utf-8")
# f.write("python24期666")


# f = open('test00001.py','w',encoding='utf-8')


# 以二进制模式去打开文件
# f = open('bj01.png', 'rb')
# print(f.read())

# 关闭文件
# f.close()

# with：开启open返回文件句柄对象的上下文管理器（执行完with的代码语句之后，会自动关闭文件）
with open(file="text.txt", mode="r", encoding="utf-8") as f:
    c = f.read()
    print(c)





