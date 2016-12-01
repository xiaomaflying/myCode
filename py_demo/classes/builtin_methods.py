#encoding=utf-8
"""
1. 当初始化对象时，类先调用__new__生成一个对象，然后调用__init__对对象初始化
2. __call__当对对象应用类似函数的调用时发生
3. __len__当对对象调用len时触发

Ex: https://docs.python.org/2/reference/datamodel.html
"""

class Data(object):

    # __getitem__
    # __setitem__
    # __delitem__
    # __init__
    # __str__

    def __new__(cls, data):
        # __new__ is a static method
        print 'args is %s' % data
        return super(Data, cls).__new__(cls, data)

    def __init__(self, data):
        self.data = data

    def __len__(self):
        return len(self.data)

    def __call__(self):
        print 'in __call__'
        return self.data

    def __gt__(self, other):
        print 'in __gt__'
        return self.data > other

    def __lt__(self, other):
        print 'in __lt__'
        return self.data < other


def test1():
    d = Data('hello')
    print len(d)
    d()
    print d > 'world'
    print d < 'world'

test1()
