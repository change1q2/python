"""
============================
Author:柠檬班-木森
Time:2019/11/8
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""
"""

except  可以指定捕获异常类型



"""

#  捕获单个异常类型
# try:
#     # print(a)  # NameError
#     int("a")   # ValueError
# except NameError:
#     print("捕获到了异常")
print("----start------")

# 捕获多个异常类型(不同的异常类型需要做不同的处理的时候)
# try:
#     print(a)  # NameError
#     b = int("a")   # ValueError
#     print("---------2--------")
# except NameError as e:
#     a = 100
#     print(a)
#     print("捕获到了异常NameError:{}".format(e))
# except ValueError as e2:
#     b = 99
#     print("捕获到了异常ValueError:{}".format(e2))


# 捕获多个异常类型(不同的异常类型,做统一处理的时候)
# try:
#     # print(a)  # NameError
#     b = int("a")   # ValueError
#     print("---------2--------")
# except (NameError,ValueError) as e:
#     a = 100
#     print(a)
#     print("捕获到了异常:{}".format(e))


# 捕获所有的异常类型
# try:
#     # print(a)  # NameError
#     b = int("a")   # ValueError
#     print("---------2--------")
# except:
#     a = 100
#     print(a)
#     print("捕获到了异常:")

# 捕获场景的异常类型
# try:
#     # print(a)  # NameError
#     b = int("a")  # ValueError
#     print("---------2--------")
# except Exception as e:
#     print("捕获到了异常:{}".format(e))

# try:
#     # print(a)  # NameError
#     b = int("a")  # ValueError
#     print("---------2--------")
# except BaseException as e:
#     print("捕获到了异常:{}".format(e))


# 断言
# # 实际结果
# res = "888"
# # 预期结果
# expected = "888"

# if res == expected:
#     print("通过")
# else:
#     print("不通过")



#  断言  assert  表达式
# 断言：比较两个数据是否一致
# try:
#     print(aaa)
#     assert res == expected
# except AssertionError as e:
#     print("用例未通过")
# else:
#     print("用例执行通过")
# finally:
#     print("用例执行出现了其他错误")

# print("-----------------")

# 主动引发一个异常
# raise NameError
# raise ValueError

res = "8889"
# 预期结果
expected = "888"

try:
    assert res == expected
except AssertionError as e:
    print("用例未通过")
    raise e
