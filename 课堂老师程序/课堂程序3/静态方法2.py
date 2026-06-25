__author__ = '86131'
# 静态方法内部不能直接访问属性和方法
# 静态方法内部可以使用类名访问类属性或调用类方法
class Car:
    wheels=3        # 类属性
    @staticmethod
    def test():     # 静态方法
        Car.wheels=4
        print("我是静态方法")
        print(f"类属性的值为{Car.wheels}") #格式化输出 静态方法中访问类属性
Car.test() # 4
car=Car()
car.test() # 4

