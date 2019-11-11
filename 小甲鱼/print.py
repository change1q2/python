"""
============================
作者:seak
时间:
邮件:274882401@qq.com
作用：
题目：如果一个3位数等于其各位数字的立方和，则称这个数为水仙花数。例如153 = 1^3+5^3+3^3，因此153是一个水仙花数。编写一个程序，找出所有的水仙花数。
============================
"""
#寻找水仙花数

li = [0,1,2,3,4,5,6,7,8,9]
for i in li:
    for j in li:
        for k in li:
            #print(i,j,k)
            li2 = [i,j,k]
            #print(li2)
            ss = [str(i) for i in li2]
           # print(ss)
            res = ''.join(ss)
            print(res)
            res2 =int(res)
            if res2 == k**3 + (j*10)**3 +(i*100)**3 :
                print(res2)
            else:
                
