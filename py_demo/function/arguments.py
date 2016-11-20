#encoding=utf-8

"""
函数的参数

a. 参数传递
1. 函数的参数是通过指针（引用）进行的，即作为参数被传递的对象从来不自动拷贝；
2. 不可变的参数通过“值”进行传递；(C语言的理解)
3. 可变对象通过“指针”进行传递；

如果未使用其他语言，就相当于将对象赋给变量名。
ex: test1

b. 如何避免可变参数的修改？
1. 在函数内部使用拷贝；
2. 使用不可变对象，如将列表改成元组
ex: test2

c. 参数的模式匹配 -- 位置参数和关键字参数
ex: test3

d. 任意参数 -- 两种匹配的扩展
ex: test4

"""

def test1(a, l):
    a = 2
    l[0] = 'foo'
    return a, l

a = 1
l = [1, 2]
test1(a, l)
print a, l

# test2
def test2(a, l):
    a = 2
    l_copy = l[:]
    l_copy[0] = 'foo'
    return a, l_copy

a = 1
l = [1, 2]
test2(a, l)
print a, l

#test2(a, tuple(l))


# test3
# 位置参数
def f(a, b, c):
    print a, b, c

# 关键字参数指定默认值
def f1(a, b=None, c=None):
    print a, b, c

def test3():
    f(1, 2, 3)
    f(a=1, b=2, c=3)
    f(1, b=2, c=3)
    #f(b=2, a=1, 3) # error
    #f(1, 2)  # error

    f1(1)
    f1(1, 2)
    f1(1, c=3, b=2)

test3()

# test4 任意参数

def f2(*args):
    print args

def f3(**kwargs):
    print kwargs

def f23(a, *args, **kwargs):
    print a, args, kwargs

def test4():
    f2()
    f2(1, 2, 3)

    f3()
    f3(a=1, b=2)

    f23(1, 2, 3, b=2, c=3)

test4()
