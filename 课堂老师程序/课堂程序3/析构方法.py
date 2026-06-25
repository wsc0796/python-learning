__author__ = '86131'
# 每个类默认都有一个析构方法，销毁该类对象时会默认调用
class Car:
    def __init__(self,color): #定义无参的构造方法
        self.color=color
        print(f"{self.color}对象被创建")
    def __del__(self):  #定义析构方法
        print(f"{self.color}对象被销毁")
car= Car("red") #创建对象并初始化
print(car.color)
del car #删除对象的引用
car= Car("blue") #创建对象并初始化
print(car.color)

