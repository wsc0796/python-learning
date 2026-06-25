__author__ = '86131'
# 实例属性可以通过对象进行修改
class Car:
    def drive(self):
        self.wheels=4   #添加实例属性
car=Car()     #创建对象
car.drive()
car.wheels=3  #通过对象修改实例属性 3
print(car.wheels) #通过对象访问实例属性
