"""
============================
作者:seak
时间:
邮件:274882401@qq.com
作用：
题目：2、有一组数据，如下格式：
[
{'case_id': 1, 'method': 'post', 'url': '/member/login', 'data': '123', 'actual': '不通过','excepted': '通过'},
{'case_id': 2,  'method': 'post', 'url': '/member/login', 'data': '123','actual': '通过', 'excepted': '通过'},
{'case_id': 3, 'method': 'post', 'url': '/member/login', 'data': '123', 'actual': '不通过','excepted': '通过'},
{'case_id': 4,  'method': 'post', 'url': '/member/login', 'data': '123','actual': '通过', 'excepted': '通过'},
{'case_id': 4, 'method': 'post', 'url': '/member/login', 'data': '123', 'actual': '不通过','excepted': '通过'},
{'case_id': 5,  'method': 'post', 'url': '/member/login', 'data': '123','actual': '通过', 'excepted': '通过'},
]

定义一个如下的类
请列表中的每个字典遍历出来，每个字典的数据用一个对象来保存，
要求：通过setattr 把字典中数据设为对象的属性和值，字典中的key对应属性名，value为属性值。
最后把所有的对象，放入一个列表中，得到如下如格式的数据：
[用例对象，用例对象，用例对象...]
class CaseData:
    pass
============================
"""
class Case:

    def __init__(self,case_id,method,url,data,actual,excepted):
        self.case_id = case_id
        self.method = method
        self.url = url
        self.data = data
        self.actual = actual
        self.excepted = excepted

data = [
{'case_id': 1, 'method': 'post', 'url': '/member/login', 'data': '123', 'actual': '不通过','excepted': '通过'},
{'case_id': 2,  'method': 'post', 'url': '/member/login', 'data': '123','actual': '通过', 'excepted': '通过'},
{'case_id': 3, 'method': 'post', 'url': '/member/login', 'data': '123', 'actual': '不通过','excepted': '通过'},
{'case_id': 4,  'method': 'post', 'url': '/member/login', 'data': '123','actual': '通过', 'excepted': '通过'},
{'case_id': 4, 'method': 'post', 'url': '/member/login', 'data': '123', 'actual': '不通过','excepted': '通过'},
{'case_id': 5,  'method': 'post', 'url': '/member/login', 'data': '123','actual': '通过', 'excepted': '通过'},
]


class CaseData(object):
    pass


def work3_1(data):
    new_data = [] #创建一个新列表
    #遍历列表
    for i in data:
        #创建一个对象
        print(i)
        case = CaseData()
        #便利出当前字典的所有数据
        for k,v in i.items():
            #将遍历出来的数据涉资为对象的属性
            setattr(case,k,v)
            #将设置好的属性的对象，加入到列表中
            new_data.append(case)
    return new_data
data = work3_1(data)
print(data)

# 动态属性设置
# setattr

