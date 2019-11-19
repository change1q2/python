"""
============================
Author:柠檬班-木森
Time:2019/10/24
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""
"""
1、现有字符串    str1 = "PHP is the best programming language in the world! "
      要求一：将给定字符串的PHP替换为Python
      要求二：替换以后，将字符串以空格为分割点进行分割得到一个列表

2、编写代码，提示用户输入1-7七个数字，分别代表周一到周日，
打印输出“今天是周几”（要求：使用上课学过的知识点来做）


3、现在有一个列表 li2=[1，2，3，4，5]，

     第一步：请通过三行代码将上面的列表，改成这个样子 li2 = [0，1，2，3，66，5，11，22，33]，
     第二步：对li2进行升序排序 （从小到大）
     第三步：对第二步排序后的列表  再进行降序排序（从大到小）

 4、切片
        1、li = [1,2,3,4,5,6,7,8,9] 请通过切片得出结果 [3,6,9]
        2、s = 'python java php',通过切片获取: java

5、定义一个空列表user=[],   分别提示用户输入，姓名，年龄，身高，用户输入完之后，
将输入的信息添加的列表中保存，然后按照一下格式输出：
    用户的姓名为：xxx,年龄为：xxx,  身高为：xxx  ,请仔细核对（要求：输出的身高要求保留2位小数）

"""

# 第一题
str1 = "PHP is the best programming language in the world! "
# 要求一
str2 = str1.replace('PHP', 'python')
print(str2)
# 要求二
li_str = str2.split(' ')
print(li_str)

# 第二题
li = ['周一', '周二', '周三', '周四', '周五', '周六', '周日']
num = int(input('请输入1-7:'))
index = num - 1
data = li[index]
print('今天是:{}'.format(data))

# 第三题
li2 = [1, 2, 3, 4, 5]

# 第一步
li2.insert(0, 0)  # 在最前面加入0
li2[4] = 66
li2.extend([11, 22, 33])  # 在最后加入三个元素
print(li2)

# li2.clear()
# li2.extend([0,1,2,3,66,5,11,22,33])

"""
说明：第三题的第二步和第三步 中途改了题目需求的描述，都算满分
"""
# 第二步：从小到大排序
li2.sort()
print(li2)

# 第三步：从大到小排序
li2.sort(reverse=True)
print(li2)

# 第四题
li = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(li[2::3])

s = 'python java php'
print(s[7:11])

# 第五题
user = []

name = input("请输入姓名：")
age = input("请输入年龄：")
height = input("请输入身高：")

user.extend([name, age, height])


print('用户的姓名为：{},年龄为：{},身高为：{:.2f},请仔细核对'.format(name, age, float(height)))

# print(F'用户的姓名为：{name},年龄为：{age},身高为：{float(height):.2f},请仔细核对')
# print('用户的姓名为：%s,年龄为：%s,身高为：%.2f,请仔细核对' % (name, age, float(height)))
