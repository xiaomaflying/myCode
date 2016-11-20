# encoding=utf-8

"""
b. 作用域

当你在程序中使用变量名时，python创建、改变、查找变量名都是在命名空间中进行的。
默认情况下，一个函数中的所有变量名都是与函数命名空间相关联的，即
1. 一个定义在def语句中的变量只能在def语句块内被访问；
2. def之内的和def之外相同的变量名并不冲突，因为他们命名空间（作用域）不同.
ex: test1

通过上一个例子得出结论：函数对变量名的查找遵循LEGB作用域查找原则.
1. 从本地变量查找（L）
2. 从任意上层的作用域查找（E）
3. 从全局作用域查找
4. 从内置作用域查找
按照这个顺序，找到了则停止查找。
ex: test2


内置作用域有哪些变量？

由于LEGB规则，本地变量会覆盖全局变量，而全局变量会覆盖内置变量
ex: test3


由于本地变量赋值会覆盖全局变量，那么如何在函数内对全局变量赋值？
请使用global将变量声明为全局变量 ex: test4


深入学习嵌套作用域(闭包)：E. ex: test5

"""

#from math import pi

pi = 100

def test1():
    pi = 99
    def inline():
        pi = 98
        print pi
    inline()
    print pi

print pi

def test2(x):
    z = x + pi
    return z

print test2(1)


def test3():
    open = 'not buildin'
    open('a.txt')  # raise exception


x = 98
def test4():
    global x
    x = 99
test4()
print x


def test5():
    x = 88
    def inline():
        print x
    return inline

inline = test5()
inline()



if __name__ == '__main__':
    test4()
