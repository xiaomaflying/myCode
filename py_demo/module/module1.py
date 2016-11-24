#encoding=utf-8
"""
一、 为什么要有模块？
    1. 代码重用
    2. 命名空间的划分
    3. 更好的组织代码，共享服务和数据，编写大型程序

二、如何导入模块？
    1. import指令和from xxx import yyy
    2. from xxx import yyy
    3. from xxx import yyy as y

三、import的工作方式
    1. 找到模块；
    2. 编译成位码； (只在第一次的导入的时候) demo
    3. 执行模块代码创建定义的对象

四、模块的查找顺序
    1. 程序的主目录
    2. PYTHONPATH目录
    3. 标准链接库的目录
    sys.path 从左到右搜索

>>> import module1
>>> import module1  # the first time import is different

>>> dir(module1)
>>> module1.name
>>> module1.sys
>>> module1.get_name
>>> module1.someClass

"""


print 'starting to load the module ...'
import sys

name = 'John'

age = 18

def get_name():
    pass

class someClass:
    pass

print sys.path
print 'finish to load the module ...'
