__author__ = '86131'
# 类方法定义在类的内部 使用装饰器@classmethod修饰
# 类方法中参数列表的第一个参数为cls,代表类本身，它会在类方法被（对象或类）调用自动接收由系统传递的调用该方法的类

# 类方法定义
class Car:
    @classmethod
    def stop(cls):
        print(type(cls))
        print("我是类方法")
# 类方法调用
Car.stop()   # 通过类调用类方法
car=Car()    # 创建对象
car.stop()   # 通过对象调用类方法
