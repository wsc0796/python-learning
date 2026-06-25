__author__ = '86131'
class Car:
    def __init__(self,color): #定义有参的构造方法
        self.color=color
    def get_color(self):
        print(f"车的颜色为：{self.color}")


car_one= Car("红色") #创建对象并初始化
car_one.get_color()
car_two= Car("蓝色") #创建对象并初始化
car_two.get_color()
