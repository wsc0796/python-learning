class Car:
    wheels=4 # 类属性
    def drive(self):
        print("行驶")
print(Car.wheels) # 4
# Car.drive()  #  类不能访问实例方法
car=Car()  # 创建Car类的对象
print(car.wheels) # 4 可以通过对象访问类属性
Car.wheels=3 # 可以通过类修改类属性
print(car.wheels)  # 3
car.color="red"  # 在对象空间通过对象建立实例属性
car.wheels=4 # 4 在对象空间通过对象建立实例属性
# Car.color  #   不能通过类访问实例属性
print(car.wheels)  # 4 通过对象访问实例属性
print(car.color)  # red 通过对象访问实例属性
car.drive()# 行驶 通过对象访问实例方法