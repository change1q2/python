"""
============================
作者:seak
时间:
邮件:274882401@qq.com
作用：
题目：4、封装一个学生类，(自行分辨定义为类属性还是实例属性，方法定义为实例方法)

-  属性：身份(学生)，姓名，年龄，性别，英语成绩，数学成绩，语文成绩，

-  方法一：计算总分，方法二：计算三科平均分，方法三：打印学生的个人信息。
============================
"""

class Student:
    identity = '学生'

    def __init__(self,name,age,sex,EnglishScore,MathematicsScore,LanguageScore):
        self.name = name
        self.age = age
        self.sex = sex
        self.EnglishScore = EnglishScore
        self.MathematicsScore = MathematicsScore
        self.LanguageScore = LanguageScore

    #方法一：计算总分
    def TotalScore(self):
        return self.EnglishScore + self.MathematicsScore + self.LanguageScore

    #方法二：计算三科平均分
    def AvgScore(self):
        return (self.EnglishScore + self.MathematicsScore + self.LanguageScore)/3

    #方法三：打印学生的个人信息。
    def StudentMessage(self):
       return ("学生个人信息：\n姓名：{} \n年龄：{}\n性别：{}\n英语成绩：{}\n数学成绩：{}\n"
              "语文成绩：{}".format(self.name,self.age,self.sex,self.EnglishScore,
              self.MathematicsScore,self.LanguageScore)
              )

student1 = Student("小海",22,"男",85,75,68)

# 实列方法的调用
print(student1.StudentMessage())

