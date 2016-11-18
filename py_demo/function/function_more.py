#encoding=utf-8

"""
函数的高级话题：

1. 递归函数；
2. 函数也是对象，可以赋值、充当内容添加到数据结构中、可以添加属性；
3. 一些内置的函数编程工具：map、filter、reduce

"""

# test1 递归求和
def mysum(l):
    if not l:
        return 0
    else:
        return l[0] + mysum(l[1:])

def mysum1(l):
    sum = 0
    for i in l:
        sum += i
    return sum

l = [1, 2, 3]
print mysum(l)
print mysum1(l)


# 斐波那契数列 0, 1, 1, 2, 3, 5, 8, 13 ... ...
def fib(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)

def fib1(n):
    if n == 1:
        return 0
    if n == 2:
        return 1

    a = 0
    b = 1
    i = 2
    while(i < n):
        #tmp = a + b
        #a = b
        #b = tmp
        a, b = b, a + b
        i += 1
    return b

print fib1(6)


# test2

def test2():

    def f():
        """f is a function."""
        pass

    print f.__name__
    print f.__doc__
    f.attr = 'function attr'
    print hasattr(f, 'attr')
    print f.attr
    del f.attr
    print hasattr(f, 'attr')

    af = f
    print af.__name__
    d = {'f': f}
    print d

test2()


# test3 map filter reduce

def test3():
    print map(lambda x: x*x, [1, 2, 3])
    # help(map)
    print map(lambda x, y: x + y, [1, 2, 3], [4, 5, 6])

    print reduce(lambda x, y: x + y, [1, 2, 3, 4])
    print reduce(lambda x, y: x + y, [1, 2, 3, 4], -10)

    print filter(lambda x: x > 0, [-1, -2, 0, 1, 2])

if __name__ == '__main__':
    test3()

