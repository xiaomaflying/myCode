#encoding=utf-8

"""
函数练习题：
1. 递归版本和非递归版本，编写斐波那契数列
2. 编写一个函数，用来拷贝一个字典对象，返回拷贝的新对象. 提示：使用keys方法：
    def copy_dict(dict): -> dict

    思考：
    a) 复制序列使用[:], 字典是否也可以？
    b) 如果被拷贝的字典为可变对象，如何避免修改被拷贝字典导致拷贝字典值也发生变化的情况？

"""


# 1. 斐波那契数列 0, 1, 1, 2, 3, 5, 8, 13 ... ...
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


# 2. copy_dict

def copy_dict(d):
    copy_d = {}
    for key in d.keys():
        copy_d[key] = d[key]
    return copy_d

d = {1: 1, 2: 'hello'}
d1 = copy_dict(d)
print d, d1
d[2] = 'world'
print d, d1


d2 = {1: [1, 2, ], 2: 'hello'}
d3 = copy_dict(d2)
print d2, d3
d2[1][0] = 'foo'
print d2, d3


def copy_dict2(d):
    return d.copy()
    #import copy
    #return copy.copy(d)

d2 = {1: [1, 2, ], 2: 'hello'}
d3 = copy_dict2(d2)
print d2, d3
d2[1][0] = 'foo'
print d2, d3

print 'copy_dict3'
print
def copy_dict3(d):
    import copy
    return copy.deepcopy(d)


origin = {1: [1, 2, ], 2: 'hello'}
def copy_test(copy_method, origin):
    copy_ = copy_method(origin)
    return origin, copy_

origin, new = copy_test(copy_dict3, origin)
origin[1][0] = 'foo'
print origin, new


# conclusion
# 请注意，引用、浅copy、深拷贝的区别！
import copy
origin = {1: [1, 2, ], 2: 'hello'}

new_ref = origin
new_light_copy = copy.copy(origin)  # or origin.copy()
new_deep_copy = copy.deepcopy(origin)
origin[3] = 'world'
origin[1][0] = 'foo'

print 'origin', origin
print 'ref copy', new_ref
print 'light copy', new_light_copy
print 'deep copy', new_deep_copy

