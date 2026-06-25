__author__ = '86131'
class  Car :
    wheels=4  # 声明类属性
    def drive(self):
        print ("行驶")
print(Car.wheels) # 4 类可以访问类属性
# Car.drive()  # 类不能调用实例方法
car=Car() # 创建对象
print (car.wheels)  # 4 对象可以访问类属性
car.drive()  # 行驶 对象可以调用实例调用方法
Car.wheels=3  # 3  可以通过类修改类属性
print(Car.wheels)
car.wheels=4 # 4 通过对象动态创建实例属性
print(car.wheels)
car.color="red"
print(car.color)
# print(Car.color) # 不能通过类访问实例属性
