__author__ = '86131'
# 类方法中可以使用cls访问和修改类属性的值
class Car:
    wheels=3    # 类属性
    @classmethod
    def stop(cls): # 类方法
        cls.wheels=4      # # 使用cls修改类属性
        print(cls.wheels)
Car.stop() # 4
car=Car()
car.stop()  # 4
