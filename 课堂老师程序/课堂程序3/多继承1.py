__author__ = '86131'
class House:
    def live(self):
        print("供人居住")
class Car:
    def drive(self):
        print("行驶")
#定义一个表示房车的类，继承House类和Cat类
class TouringCar(House,Car):
    pass

tour_car=TouringCar()# 创建房车对象
tour_car.live() # 调用父类House 的方法 供人居住
tour_car.drive()# 调用父类Car 的方法 行驶


