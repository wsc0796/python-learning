__author__ = '86131'
# 实例方法定义在类内部 以self（代表对象本身）为第一个形参，只能通过对象调用
class Car:
    def drive(self):          # 实例方法
        print("我是实例方法")
car=Car()
car.drive()
# Car.drive() # 不能通过类调用实例方法

