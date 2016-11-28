#encoding=utf-8

"""
一、继承是设计面向对象程序的重要工具之一,是设计、复用代码的重要手段：
    新式类继承object类
    1. 定义一个普通类Bird，继承自object
    2. 定义一个继承的类SongBird，继承自普通类, 可以使用Bird的方法
    3. 扩展普通的类，在继承的类里面添加其他的方法
    4. 复用并修改

二、不仅仅可以继承自自定义类，也可以继承自普通类
ex: test5

EX: 自定义字典，获取字典的value时，若字典key不存在，不要报错，返回None
"""


class Bird(object):

    def __init__(self, category='common'):
        self.category = category
        self.hungry = 1

    def eat(self):
        if self.hungry:
            print 'Eating make me full!!!'
            self.hungry = 0
        else:
            print 'I am full! Thanks!'


# test2
#class SongBird(Bird):
#    pass


# test3
#class SongBird(Bird):
#    def sing(self):
#        print 'I am singing!'

# test4
class SongBird(Bird):
    def __init__(self):
        # Bird.__init__(self)
        # super(SongBird, self).__init__(self)
        self.sound = 'ahaaaa~'

    def sing(self):
        print self.sound

    def eat(self):
        if self.hungry:
            print 'SongBird eating'
            self.hungry = 0
        else:
            print 'SongBird is full!!!'

def test1():
    bird = Bird()
    bird.eat()
    bird.eat()

def test2():
    songbird = SongBird()
    songbird.eat()
    songbird.eat()

def test3():
    songbird = SongBird()
    songbird.sing()

def test4():
    songbird = SongBird()
    songbird.sing()

    songbird.eat() # error


class Mylist(list):
    def __init__(self, *args):
        super(Mylist, self).__init__(*args)
        self.access_count = 0

    def __getitem__(self, index):
        self.access_count += 1
        return super(Mylist, self).__getitem__(index)


    def __setitem__(self, index, value):
        print 'in setitem index: %s , value : %s' % (index, value)
        super(Mylist, self).__setitem__(index, value)

    def __delitem__(self, index):
        print 'in delitem ', index
        super(Mylist, self).__delitem__(index)


def test5():
    my_list = Mylist(range(10))
    print my_list.access_count
    my_list[1] + my_list[2]
    print my_list.access_count

def test6():
    my_list = Mylist(range(10))
    my_list[0] = 'x'
    del my_list[0]


# EX
class Mydict(dict):

    def __getitem__(self, key):
        if key not in self:
            return None
        return super(Mydict, self).__getitem__(key)


def test7():
    mydict = Mydict()
    mydict['1'] = 'hello'
    mydict['2'] = 'world'
    print mydict
    print mydict['1']
    print mydict[1]

if __name__ == "__main__":
    test7()
