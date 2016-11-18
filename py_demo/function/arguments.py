#encoding=utf-8

"""
函数的参数

a. 参数传递
1. 函数的左右参数是通过指针（引用）进行的，即作为参数被传递的对象从来不自动拷贝；
2. 不可变的参数通过“值”进行传递；(C语言的理解)
3. 可变对象通过“指针”进行传递；

如果未使用其他语言，就相当于将对象赋给变量名。
ex: test1

b. 如何避免可变参数的修改？
1. 在函数内部使用拷贝；
2. 使用不可变对象，如将列表改成元组

c. 参数的模式匹配 -- 位置参数和关键字参数
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

test2(a, tuple(l))
print a, l
