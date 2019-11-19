"""
============================
作者:seak
时间:
邮件:274882401@qq.com
作用：
题目：
第二题：当前有一个case.txt文件，里面中存储了很多用例数据: 如下，每一行数据就是一条用例数据，
# 文件中数据
url:www.baidu.com,mobilephone:13760246701,pwd:123456
url:www.baidu.com,mobilephone:15678934551,pwd:234555
url:www.baidu.com,mobilephone:15678934551,pwd:234555
url:www.baidu.com,mobilephone:15678934551,pwd:234555
url:www.baidu.com,mobilephone:15678934551,pwd:234555
# 要求一： 请把这些数据读取出来，到并且存到list中，格式如下
[
{'url': 'www.baidu.com', 'mobilephone': '13760246701', 'pwd': '123456'}, {'url': 'www.baidu.com', 'mobilephone': '15678934551', 'pwd': '234555'},{'url': 'www.baidu.com', 'mobilephone': '15678934551', 'pwd': '234555'},{'url': 'www.baidu.com', 'mobilephone': '15678934551', 'pwd': '234555'},
{'url': 'www.baidu.com', 'mobilephone': '15678934551', 'pwd': '234555'}
]

# 要求二：将上述数据再次进行转换，转换为下面这种字典格式格式
​
{
   'data1':{'url': 'www.baidu.com', 'mobilephone': '13760246701', 'pwd': '123456'},
   'data2':{'url': 'www.baidu.com', 'mobilephone': '15678934551', 'pwd': '234555'},
   'data3':{'url': 'www.baidu.com', 'mobilephone': '15678934551', 'pwd': '234555'},
   'data4':{'url': 'www.baidu.com', 'mobilephone': '15678934551', 'pwd': '234555'},
   'data5':{'url': 'www.baidu.com', 'mobilephone': '15678934551', 'pwd': '234555'}
}
​
# 提示：需要使用字符串的分割方法
​
# 注意点：数据中如果有换行符'\n'，要想办法去掉。
============================
"""
def func(): #先封装成一个函数
        #读出数据并放到list列表中
        with open('case.txt', mode='r', encoding='utf-8') as f:#打开数据
                list = f.readlines()#读出数据并放到list列表中
                print(list)  #报'utf-8' codec can't decode byte 0xca in position 0: invalid continuation byte  (可以将utf8改为gbk，编码格式不一致导致的)

                #把key和value取出来
                dic = {} #（1）创建一个空字典用来接收
                for index,data in enumerate(list): #(2)遍历列表找出需要的数据根据下标
                        key = "data{}".format(index)
                        value = data.replace("\n",'')
                dic[key] = value
                return dic

res = func()
print(res)
