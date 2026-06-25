__author__ = '86131'
# 实例属性是在方法内部声明的属性
# Python支持动态添加实例属性
# 实例属性只能通过对象访问，不能通过类访问
class Car:
    def drive(self):
        self.wheels=4   #添加实例属性
car=Car()     #创建对象
car.drive()
print(car.wheels) #  4 通过对象访问实例属性
# print(Car.wheels) #  不能通过类访问实例属性
car.wheels=3 # 通过对象修改实例属性
car.color="red" # 通过对象动态添加实例属性
print(car.wheels) # 3
print(car.color)  # red