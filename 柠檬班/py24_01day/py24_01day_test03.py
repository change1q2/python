"""
============================
Author:柠檬班-木森
Time:2019/10/18
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""
"""
标识符：只要是自己起的名字都叫标识符
变量、函数名、类名、模块名（py文件） 包名

标识符的命名规范
变量的命名规范：只可以使用数字、字母和下划线组成(不能使用数字开头)
变量命名尽量做到见名知意（尽量不要使用拼音）

标识符命名的时候不能有python关键字

python关键字：每个关键字都是有特殊的作用的。

'False', 'None', 'True', 'and', 'as', 
'assert', 'async', 'await', 'break',
 'class', 'continue', 'def', 'del', 
 'elif', 'else', 'except', 'finally', 
 'for', 'from', 'global', 'if', 'import',
  'in', 'is', 'lambda', 'nonlocal', 'not', 
  'or', 'pass', 'raise', 'return', 'try', 
  'while', 'with', 'yield'

"""


and1 = 999

# 在控制台输出python 所有的关键字
import keyword

print(keyword.kwlist)
