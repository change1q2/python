"""
============================
作者:seak
时间:
邮件:274882401@qq.com
作用：
题目：
============================
"""
# #str.split(str="", num=string.count(str)).
# str -- 分隔符，默认为所有的空字符，包括空格、换行(\n)、制表符(\t)等。
# num -- 分割次数。默认为 -1, 即分隔所有。
'''
str = "Line1-abcdef \nLine2-abc \nLine4-abcd";
print str.split( );       # 以空格为分隔符，包含 \n
print str.split(' ', 1 ); # 以空格为分隔符，分隔成两个

['Line1-abcdef', 'Line2-abc', 'Line4-abcd']
['Line1-abcdef', '\nLine2-abc \nLine4-abcd']
'''

# 读出数据并放到list列表中
with open('case.txt', mode='r', encoding='utf-8') as f:  # 打开数据
    list = f.readlines()  # 读出数据并放到list列表中
   # print(list)
    #创建一个空列表
    li2 = []
    #遍历列表中的数据
    for i in list:
       # print(i)
       # print(".......................................")
        item =i.split(',')
       # print(item)

    #创建一个字典存放用例数据
    dic = {}
    for j in item:
        print(j)
    #将遍历出来的数据创建key和value值放到字典中
    key = j.split(',')[0]
    value = j.split(':')[1].replace('\n','')
    dic[key] = value
    #将数据加入列表中
    list.append(dic)
    print(dic)

