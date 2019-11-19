'''
作者：seak
时间：
项目：
题目：1、一、输出99乘法表，结果如下：（提示嵌套for循环，格式化输出）
作用：
备注：
'''

for i in range(1,10):
        for j in range(1,i+1):
            print("{}*{}={}".format(i,j,i*j),end=" ")
        print()