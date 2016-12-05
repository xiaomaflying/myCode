#encoding=utf-8
"""
1. 什么是可迭代对象？
    可以直接用作for循环的对象统称为可迭代对象（Iterable）
    >>> l = [1, 2, 3]
    >>> for item in l: print item
    >>> d = {1: 1, 2: 2, 3: 3}
    >>> for key in d: print key, d[key]

2. 可以使用手动迭代
    手动迭代要先将可迭代对象转化为迭代器对象（Iterator）, 然后调用next方法，直到该方法抛出StopItertion异常
    >>> l = [1, 2, 3]
    >>> it = iter(l)
    >>> it.next(); it.next(); it.next(); it.next()
    >>> next(it)

    结论：
    1. 可迭代对象中含有__iter__方法，该方法返回迭代器对象；
    2. 迭代器对象含有next方法，用来获取可迭代对象的下一个值；
    3. for循环内部实现原理：调用iter把可迭代对象转化成迭代器，在通过next方法进行循环迭代。

3. 如何判断对象为可迭代对象还是迭代器对象？
    >>> from collections import Iterator, Iterable
    >>> isinstance(l, Iterable)
    >>> isinstance(l, Iterator)
    >>> isinstance(it, Iterable)
    >>> isinstance(it, Iterator)

4. 如何自定义迭代器
    自定义迭代器，只需要在类里面定义__iter__方法，用它返回一个带next()方法的对象就可以了。但是要注意设置退出条件

    打印10以内的奇数 test1

    也可以将__iter__, next都定义在一个类中，__iter__ return self, 通过这种方式定义，意思就是通过这样的类生成的对象，即使可迭代对象也是迭代器对象。test2

5. 如果不在next里面设置StopIteration条件，则需要在调用的时候设置退出条件
"""

class Iterable:
    def __iter__(self):
        return Iterator()

class Iterator:
    def __init__(self):
        self.start = -1

    def next(self):
        self.start += 2
        if self.start > 10:
            raise StopIteration
        return self.start

def test1():
    i = Iterable()
    for _i in i:
        print(_i)


##################test2###########

class Iterable1:
    def __init__(self, start, end):
        self.start = start
        self.end = end
    def __iter__(self):
        return self
    def next(self):
        self.start += 2
        if self.start > self.end:
            raise StopIteration
        return self.start

def test2():
    i = Iterable1(1, 10)
    for _i in i:
        print(_i)


##################test3###########
class Iterable2(Iterable1):
    def next(self):
        self.start += 2
        return self.start

def test3():
    i = Iterable2(1, 10)
    for count, _i in zip(range(5), i):
        print _i


test3()
