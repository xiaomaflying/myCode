#encoding=utf-8
"""
装饰器：扩展函数，面向切面编程
1. 最简单的函数
2. 包装函数
3. 希望调用的时候再去执行before 和 after, 而不是包装的时候执行
4. 例子3等价于语法糖@
5. 装饰带参数的函数
6. 装饰任意参数的函数
"""

# 1
def func():
    print 'in func'
    return None


# 2
def deco(func):
    print 'before run func'
    func()
    print 'after run func'
    return func

# 3
def deco3(func):
    def wrapper():
        print 'before run func'
        result = func()
        print 'after run func'
        return result
    return wrapper

# 4
@deco3
def func1():
    print 'in func1'
    return None

# 5
def deco5(func):
    def wrapper(a, b):
        print 'before'
        result = func(a, b)
        print 'after'
        return result
    return wrapper

@deco5
def func5(a, b):
    print 'in func5'
    return a + b

# 6
def deco6(func):
    def wrapper(*args, **kwargs):
        print args, kwargs
        result = func(*args, **kwargs)
        print 'after'
        return result
    return wrapper

@deco6
def func6(a, b, c, w='a', k='b'):
    pass

@deco6
def func6_1(x, y):
    pass


def test2():
    myfunc = deco(func)
    myfunc()

def test3():
    myfunc = deco3(func)
    myfunc()

def test4():
    func1()

def test5():
    print func5(1, 2)

def test6():
    func6(1, 2, 3, w='hello', k='world')
    func6_1(1, 3)


test6()

