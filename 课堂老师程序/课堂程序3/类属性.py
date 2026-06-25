__author__ = '86131'
# 类属性声明在类的内部，方法外部的属性
# 类属性可以通过类或对象进行访问
# 类属性只能通过类进行修改
class Car:
    wheels=4     #类属性
    def drive(self):
        print("行驶")
car=Car()        # 创建对象
print(Car.wheels) # 通过类访问类属性 4
print(car.wheels) # 通过对象访问类属性 4
Car.wheels=3      # 通过类修改类属性
print(Car.wheels) # 通过类访问类属性 3
print(car.wheels) # 通过对象访问类属性 3
car.wheels=4      #添加一个与类属性同名的实例属性
print(Car.wheels) # 通过类访问类属性  3
print(car.wheels) # 通过对象访问类属性 4

