'''
作者：seak
时间：
项目：
题目：2、有1 2 3 4 这四个数字，设计程序计算能组成多少个互不相同且无重复数字的3位数？分别是什么？

作用：
备注：
'''

num = 0
for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            if i != j and i != k and j !=k:
                print(i,j,k)
                num += 1
print("不重复的数有{}个".format(num))