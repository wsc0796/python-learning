__author__ = '86131'
# Python支持在类外部使用对象动态的添加实例属性
class Car:
    def drive(self):
        self.wheels=4   #添加实例属性
car=Car()     #创建对象
car.drive()
car.wheels=3  #通过对象修改实例属性 3
print(car.wheels) #通过对象访问实例属性
car.color="红色"  #动态添加实例属性 红色
print(car.color)