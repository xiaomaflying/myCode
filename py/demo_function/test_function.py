#encoding=utf-8

"""
a. 函数基础


python函数的两个作用
1. 最大化代码重用和最小代码冗余；
2. 流程分解，使用函数完成子任务；

函数的一般形式：
def <name>(arg1, arg2, ... , argN):
    <statements>
    return <value>

def语句用来创建一个函数对象，python里面一切皆对象，函数也一样。

python是解释型语言，def语句是实时执行的。也就是说python函数在运行之前不需要
全部定义。参见test1 test2

甚至你可以在程序运行的时候动态定义函数。参见test3

通过以上例子，我们掌握了，如何定义函数，如何调用函数。
"""


#====================
def test1():
    print 'in test1'
    test2()


def test2():
    print 'in test2'


def test3(debug=True):
    if debug:
        def func():
            print 'in debug mode'
    else:
        def func():
            print 'in nondebug mode'

    func()
#====================

def intersect(seq1, seq2):
    u"""返回两个可序列对象的交集.
    该例子同时说明了函数的多态性，提供接口，并不限制类型
    """
    seq = []
    for x in seq1:
        if x in seq2:
            seq.append(x)
    return seq

    # return [x for x in seq1 if x in seq2]


if __name__ == '__main__':
    #test1()

    #test3(False)

    #print intersect('abd', 'bcd')
    #print intersect([1, 2, 3], [2, 3, 5])
    #print intersect((1, 2, 3), [2, 3, 5])

    pass
