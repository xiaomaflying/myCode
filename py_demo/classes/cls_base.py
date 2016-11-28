#encoding=utf-8

"""
一、基本介绍
    1. 类也是一种对象；
    2. 类是实现面向对象的工具，用来包装代码，更好的重用代码；
    3. 定义类，并通过来生成类的实例（对象）

二、类的定义：新式类和老式类
    1. 定义了两种类，通过dir()用来对比
    2. 结论：始终使用新式类

三、用类生成对象
    1. 类名+()的方式
    2. __init__(self, ...)
    3. 为类添加方法
    4. __str__(self) 实现对象的可读性
    5. 以双下划线__开头的方法是特殊的方法，以后还会继续介绍

Ex: 创建一个老师类Teacher, 初始化老师，参数为姓名，科目；
给老师添加方法，add_students, 参数为学生列表；
添加方法，显示老师管辖的学生；
重写__str__方法，打印老师的名字。
"""


class OldCls:
    pass

class NewCls(object):
    pass


class Student(object):

    def __init__(self, name, age=18):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def __str__(self):
        return 'name is %s, age is %s' % (self.name, self.age)


def test1():
    stu = Student('xiaoming')
    print stu.name
    print stu.age
    #print stu

    stu1 = Student('xiaohong', age=19)
    print stu1.get_name()
    print stu1.get_age()


test1()
