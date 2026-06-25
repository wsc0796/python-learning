__author__ = '86131'
# 如果子类继承多个父类的相同方法，那么子类先继承哪个类，便会先调用哪个类的方法
class House(object):
    def live(self):
        print("供人居住")
    def test(self):
        print("House类测试")
class Car():
    def drive(self):
        print("行驶")
    def test(self):
        print("Car类测试")
#定义一个表示房车的类，继承House类和Cat类
class TouringCar(House,Car):
    pass

tour_car=TouringCar()# 创建房车对象
tour_car.live() # 调用父类House 的方法 供人居住
tour_car.drive()# 调用父类Car 的方法 行驶
# 子类调用了先继承的House类的test（）方法
tour_car.test() # House类测试