__author__ = '86131'
# 静态方法是定义在类的内部，使用装饰器@staticmethod修饰的方法
# 静态方法没有任何默认参数，适用与与类无关的操作
# 静态方法可以通过类和对象调用
class Car:
    @staticmethod
    def test():                # 静态方法
        print("我是静态方法")
Car.test()                     #通过类读调用静态方法
car=Car()
car.test()                     #通过对象读调用静态方法