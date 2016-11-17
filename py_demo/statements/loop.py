#encoding=utf-8
import math


def test1():
    u"""演示while & for循环语句"""
    x = 1
    while x <= 100:
        print x
        x += 1

    for x in range(1, 101):
        print x


def test2():
    u"""对各种对象的循环遍历方式."""
    l = ['ab', 'cd', 1, 12]
    for item in l:
        print item

    d = {'key1': 'value1', 'key2': 'value2'}
    for key in d:
        print key, d[key]

    for key, value in d.items():
        print key, value

    for i in range(5, 1, -1):
        print i


def test3():
    u"""打印1-99第一次出现的平方数. break 语句"""
    for i in range(99, 1, -1):
        root = math.sqrt(i)
        if root == int(root):
            print i
            break

    # 打印所有平方数 continue
    for i in range(99, 1, -1):
        root = math.sqrt(i)
        if root == int(root):
            print i
            continue
            print 'sth'

def test4():
    u"""for else 和while else 语句"""
    for i in range(82, 99):
        root = math.sqrt(i)
        if root == int(root):
            print root
    else:
        print 'not found'

    i = 82
    while i < 100:
        root = math.sqrt(i)
        if root == int(root):
            print root
        i += 1
    else:
        print 'not found'


def test5():
    u"""列表解析."""
    l = range(1, 11)
    l1 = [i*i for i in l]
    print l1
    l2 = [i*i for i in l if i % 2 != 0]
    print l2

    d = {i: i*i for i in l if i % 2 != 0}
    print d

if __name__ == "__main__":
    test5()
