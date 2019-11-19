"""
============================
作者:seak
时间:
邮件:274882401@qq.com
作用：
题目：第一题：当前有一个txt文件，内容如下：
数据aaa
数据bbb
数据ccc
数据ddd
# 要求：请将数据读取出来，转换为以下格式
{'data0': '数据aaa', 'data1': '数据bbb', 'data2': '数据ccc', 'data3': '数据ddd'}
​
# 提示：
# 可能会用到内置函数enumerate
​
# 注意点：读取出来的数据如果有换行符'\n'，要想办法去掉。
============================
"""

# #补充知识点replace替换
# str.replace(old, new[, max])
#print str.replace("is", "was", 3);
# old -- 将被替换的子字符串。
# new -- 新字符串，用于替换old子字符串。
# max -- 可选字符串, 替换不超过 max 次

#封装成函数
def func():
    #将文档读出来用with ..  as  保证读完with里的数据会关闭文件，可以减轻内存的压力
    with open("test.txt",mode="r",encoding="gbk") as f:  #报这个错误an integer is required (got type str)需要整数来获取字符串,mode 和encoding没有写
        list = f.readlines()  #将读出的数据放在列表中
        print(list)
        #将读出来的数据转化成字典
        dic = {} #1创建一个空字典来接受生成的数据
        #想办法获取key和value
        # 通过enumerate去获取列表中的数据和下标
        for index,data in enumerate(list):#遍历下标（index）和元素(data)在列表中(list)
            #构造数据取获取key和value
            key = 'list{}'.format(index)#获取的列表下标作为数放在列表中
            value = data.replace("\n",' ')#将读出来的\n换成空格
            dic[key] = value #制造键值对
        return dic #封装函数必须要返回结果


res = func()#使用函数
print(res)#打印结果
