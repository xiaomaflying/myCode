#encoding=utf-8
"""
1. 为什么会有生成器？
    >>> l = [x+1 for x in range(100)]

    通过这种列表生成式的方式，我们可以创建n个元素到列表中，但假如我们只使用其中前几个元素，则相当于整个存储空间利用率很低，如果是更大的列表，则会占用更大的存储空间，仅仅需要访问前面几个元素，后面的空间则大大浪费了。
    如果列表元素可以根据某种规则推算出来，则可以通过一边循环一边计算出元素的值。这样就不用创建完整的列表而大量占用存储。生成器就是这样一种一边循环一边计算的机制。
    >>> g = (x+1 for x in range(100))
    >>> g
    >>> next(g)
    >>> g.next()

2. yield
    使用yield语句返回生成器

3. 一个返回n个元素的斐波那契数列函数。将其改写成生成器。

4. 生成器往往是迭代器的一种。作业：编写一个迭代器，实现斐波那契数列的功能
"""

# 2.yield

def test():
    yield None

def test1():
    for i in range(5):
        yield i

print test()
g = test1()
print g.next()
print next(g)

# 3
def fib(n):
    a, b = 0, 1
    cur = 0
    series = []
    while cur < n:
        series.append(b)
        a, b = b, a + b
        cur += 1
    return series

print fib(8)

def gen_fib(n):
    a, b = 0, 1
    cur = 0
    while cur < n:
        yield b
        a, b = b, a + b
        cur += 1

def test3():
    g = gen_fib(8)
    print g.next()
    print g.next()
    for item in g:
        print item

# 4
class Fib:
    def __init__(self, max):
        self.max = max
        self.a = 0
        self.b = 1
        self.cur = 0
    def __iter__(self):
        return self
    def next(self):
        fib = self.b
        if self.cur >= self.max:
            raise StopIteration
        self.a, self.b = self.b, self.a + self.b
        self.cur += 1
        return fib

def test4():
    fib = Fib(8)
    print list(fib)


test4()

