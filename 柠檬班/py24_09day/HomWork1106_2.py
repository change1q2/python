"""
============================
作者:seak
时间:
邮件:274882401@qq.com
作用：
题目：
============================
"""
def work3():
    # 读取文件中注册用户的数据
 try:
    with open('users.txt', 'r', encoding='utf8') as f:
        users = eval(f.read())# 读取内容,使用eval识别字符串中的列表
 except:
    print("文件不存在！")
 else:
    # 注册功能代码（上次作业写的，不需要改动）
    username = input('请输入新账号:')  # 输入账号
    password1 = input('请输入密码：')  # 输入密码
    password2 = input('请再次确认密码：')  # 再次确认密码

    for user in users:  # 遍历出所有账号，判断账号是否存在
        if username == user['name']:
            print('该账户已存在')  # 账号存在，
            break
    else:
        # 判断两次密码是否一致
        if password1 != password2:
            print('注册失败，两次输入的密码不一致')
        else:
            # 账号不存在 密码一样，则添加到账户列表中
            users.append({'name': username, 'pwd': password2})
            print('注册成功！')

    # 程序运行结束后，将所有用户的数据写入文件
    with open('users.txt', 'w', encoding='utf8') as f:
        # 将列表转换为字符串,写入文件
        f.write(str(users))

work3()

