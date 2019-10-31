"""
============================
作者:seak
时间:
邮件:274882401@qq.com
作用：
题目：
3、通过函数实现一个计算器，运行程序分别提示用户输入数字1，数字2，
然后再提示用户选择 ：   加【1】    减【2】    乘【3】      除【4】，根据不同的选择完成不同的计算
每个方法使用一个函数来实现， 选择后调用对应的函数，然后返回结果。
============================
"""
num1 = int(input("请输入第一个数字："))
num2= int(input("请输入第二个数字："))
num3 = int(input("请选择\t加【1】    减【2】    乘【3】      除【4】："))

def use_addition():
        res = int(num1 + num2)
        return (res)

def use_subtraction():
        res = int(num1 - num2)
        return (res)
def use_multiplication():
        res = int(num1 * num2)
        return (res)
def use_division():
        res =int(num1 / num2)
        return (res)


if num3 == 1:
    num = use_addition()
    print("你使用了加法结果为：{}+{}={}".format(num1,num2,num))
elif num3 == 2:
    num = use_subtraction()
    print("你使用了减法结果为：{}-{}={}".format(num1, num2, num))
elif num3 == 3:
    num = use_multiplication()
    print("你使用了乘法结果为：{}*{}={}".format(num1,num2,num))
elif num3 == 4:
    num = use_division()
    print("你使用了除法结果为：{}\{}={}".format(num1, num2, num))
else:
    print("你输入的数据有误！")