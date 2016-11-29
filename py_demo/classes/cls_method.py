#encoding=utf-8

"""
知识点：
1. 类属性
2. 类方法和静态方法
3. 装饰器语法
"""

class SomeCLs(object):

    instance_num = 0

    def __init__(self):
        SomeCLs.instance_num += 1

    #@classmethod
    def cls_stat(cls):
        print 'instance number is ', cls.instance_num

    #@staticmethod
    def static_stat():
        print 'instance number is ', SomeCLs.instance_num

    cls_stat = classmethod(cls_stat)
    static_stat = staticmethod(static_stat)


def test1():
    cls, cls1 = SomeCLs(), SomeCLs()
    SomeCLs.cls_stat()
    SomeCLs.static_stat()
    cls2 = SomeCLs()
    print cls.instance_num

test1()

