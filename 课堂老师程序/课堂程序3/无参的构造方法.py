__author__ = '86131'
# 构造方法在创建对象时负责对对象进行初始化
# 每一个类都有一个默认的构造方法__int__()
# 当使用无参的构造方法创建对象时，所有的属性都有相同的属性值
class Car:
    def __init__(self): #定义无参的构造方法
        self.color="红色"
    def get_color(self):
        print(f"车的颜色为：{self.color}")


car_one= Car() #创建对象并初始化
car_one.get_color()
car_two= Car() #创建对象并初始化
car_two.get_color()