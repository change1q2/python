"""
============================
作者:seak
时间:
邮件:274882401@qq.com
作用：
题目：实现剪刀石头布游戏（），提示用户输入要出的拳 ：石头（1）／剪刀（2）／布（3）/退出（4） 电脑随机出拳比较胜负，显示 用户胜、负还是平局。
============================
"""
import random

print("请按下面提示出拳：")
list = [" ","石头","剪刀","布"] #索引下标从0开始，用一个" "空字符串占位置就可以从1获取列表数据了
#思考一;
# 1如果变量num和computer相等就是平局
# 2如果用 (num+1) 除以 3 得到的余数与computer相等就是num(人)获得胜利
# 3其余情况都是计算机获胜


#数据比较
#数据这里可以使用加减法来进行判断

while True:
    print('石头【1】 剪刀【2】 布【3】 结束【4】')
    try:
        num = int(input("请输入你的选项;"))
    except:
        num = int(input("你输入的不是数字，请重新输入："))
    computer = int(random.randint(1, 3))
    # print(computer) 用来看电脑随机出什么数
    if (num >= 1 and num <= 3):
        str = "你出拳为：{0} ,\t电脑出拳为:{1}".format(list[num],list[computer])
        if num == computer:
            print(str+ ",\t平局")
        elif computer ==(num + 1)%3: # 2如果用 (num+1) 除以 3 得到的余数与computer相等就是num(人)获得胜利（关键步骤）
            print(str + ",\t你胜利了")

        else:
            print(str + ",\t你输了")
    elif num == 4:
            print('游戏结束')
            break
    else:
        print("你的输入有误请重新输入")
        15945375663