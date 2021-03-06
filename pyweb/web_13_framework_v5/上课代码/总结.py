"""
什么是单元测试框架？？ unit test
unittest , pytest 用的最多的两个单元测试框架。

pytest.  vs unittest
1, unittest 是标准库， pytest 是第三方库。
标准库： python 自带的，安装 python 以后可以直接导入。
第三库： 需要独立安装，要注意兼容性，有可能会存在安装不成功，或者是某些库的功能使用不了。
unittest 兼容性， 赢。

unittest 的使用更加复杂一些， pytest 更加容易使用。
# pytest , 自动收集测试用例
# 自动执行测试用例。


# 安装：  pip install pytest

pytest 运行：
1， pytest.main()   python: 代码形式.  生产环境。
2， 命令行的形式   : 在项目根目录下运行 pytest 命令
3， pycharm 右键运行（如果pycharm 没有出现 pytest 命令，run. configraiton 当中进行配置。）


pytest 收集测试用例的规则（pytest 将怎样的函数看成是测试用例）
1， 模块名：  test_*.py 或者是 *_test.py
2， 类名： TestLogin
3,  方法名： test_


pytest 的测试用例并不一定要以类的形式存在，
可以直接以函数的形式存在


类形式：
class TestYang:

    # 不要写 __init__() 函数， 容易报错

    def test_yangleduo(self):
        pass


当在哪个文件夹，（目录）执行  pytest 指令，那么 pytest 会自动发现当前目录下所有

test_ 开头的 py 文件，将这些文件当成测试用例文件，


修改用例自动发现的规则：在 cppytest.ini 文件当中：
[pytest]
python_files = demo_*.py
python_functions = demo_*
python_classes = Demo*

web 自动化适合什么跑回归，
web 自动化适合跑正向用例。

把正向用例，打一个 success 的标签
使用方法：：
0， 标签最好提前注册（pytest 的版本）在配置文件中配置一下
markers =
    slow
    serial
    success

1， 在对应的用例方法名称上加一个标签： @pytest.mark.标签名称
TODO: 2， 运行的时候，只运行指定标签下面的测试用例  pytest -m  "success", 标签名加双引号，记住，不要用
单引号
3,


可以同时打多个标签吗？
能，直接在方法明上加上多个 @pytest.mark.标签名
可以多个标签一起执行吗？
能， pytest -m "login and success"

或者
pytest -m "login or success"


标签即可以打到函数上，也可以打到类上。

类的标记有 2 中方式：
1，  @pytest.mark.webtest

2， 类属性
class TestClass(object):
    # 加一个 pytestmark 的类属性，属性名称是固定的。
    pytestmark = [pytest.mark.yuz, pytest.mark.linux]


1，跳过测试用例的执行： pytest.mark.skip ,  不是自己定义的，是 pytest 内置的标记，
2， 条件跳过。（环境不同，判断数据库地址，生成环境：“23.45.67.233”）
@pytest.mark.skipif(db_host == 'localhost', reason='只测试线上环境，不测试本地环境')
def test_develop_env(self):
    pass

标记功能的作用：灵活的管理和运行测试用例。
unittest 当中： testloader.loadFromModule, loadfromCaseName()
discover( 指定的文件夹下面 )


用例执行顺序：
unittest 是根据 ascii 编吗 排序
test_login_1_success   test_login_2_error

pytest 的排序： 从上到下。




"""

