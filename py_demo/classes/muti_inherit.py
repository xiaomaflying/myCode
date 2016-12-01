#encoding=utf-8

"""
1. 通过多继承扩展类，可以让类继承多个父类的方法
2. 新式类钻石继承模型满足，从左到右，从下到上的属性查找顺序

EX: 搜索python Mixin主题相关的知识, 理解Mixin的工作原理和设计方法，自定义一个Mixin，并定义一个方法用来，输出实例的所有属性
最终结果：只要继承了这个Mixin的对象，调用改方法，输出这个对象的所有属性。
"""
class Plane(object):
    def fly(self):
        print 'I can fly'

class Car(object):
    def fly(self):
        print 'Special car can fly also'

    def run(self):
        print 'I can run'

class PlaneCar(Plane, Car):
    pass

class PlaneCar1(Car, Plane):
    pass

def test1():
    pc = PlaneCar()
    pc.fly()
    pc.run()

def test2():
    pc = PlaneCar1()
    pc.fly()
    pc.run()

test2()
