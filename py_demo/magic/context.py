#encoding=utf-8
"""
1. with、as 关键词

2. 上下文管理器的功能：代码执行前做准备，代码执行后清理
使用上下文管理器，能使代码更优雅，更安全

3. 自定义上下文管理器
    要实现上下文管理器至少要实现两个方法，一个负责进入语句块前的准备操作，另一个负责离开语句块的清理操作；还要有个初始化的函数,例如，要实现open的上下文管理器，需要有两个参数，一个是文件名，一个是打开文件的模式。
    python类包含两个特殊的方法__enter__, __exit__, 实现了这两个方法的类就实现了上下文管理器。

4. 一个简单的例子。
    with块中的代码语句无论是否抛出异常，结束时都会调用__exit__函数。其中该函数接受三个参数，异常类型、异常值、异常的堆栈信息。如果是None表示没有发生异常

5. 一个发生异常的例子。
6. 实现类似open的自定义上下文管理器。
"""

def test1():
    f = open('a.txt', 'w')
    f.write('hello')
    f.write('world')  # 如果磁盘空间满，就没有机会执行f.close
    f.close()

    # 另一种方案
    f = open('a.txt', 'w')
    try:
        f.write('hello')
        f.write('world')
    finally:
        f.close()

    # 使用上下文管理器的方案
    # with伴随上下文管理器出现，as 指代with语句后面的语句返回的内容
    with open('a.txt', 'w') as f:
        f.write('hello')
        f.write('world')

def test2():
    class Context(object):
        def __enter__(self):
            print 'in __enter__'
        def __exit__(self, *args):
            print args
            print 'in __exit__'

    with Context() as c:
        print 'in context'

    with Context() as c:
        1/0


def test3():
    class Open(object):
        def __init__(self, path, mode):
            self.path = path
            self.mode = mode
        def __enter__(self):
            self.f = open(self.path, self.mode)
            return self.f
        # 一旦发生异常，需要在__exit__中对异常处理；如果想忽略异常，就在函数内部返回True
        def __exit__(self, *unused):
            self.f.close()
            #return True

    with Open('a.txt', 'w') as f:
        f.write('hello')
        f.write('world')
        #1/0


test3()
