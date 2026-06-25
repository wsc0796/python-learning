__author__ = '86131'
# Python通过在类成员的名称前面加双下划线的方式来表示私有成员，在外部不能访问
# Python的私有成员 可以通过调用类内部的公有方法访问
class Car:
    __wheels=4  # 私有属性
    def __drive(self):
        print("行驶") # 私有方法
    def test(self):
        print(f"轿车有{self.__wheels}个车轮") #类的公有方法中访问类的私有属性
        self.__drive()# 类的公有方法中访问类的私有方法
# print(Car.__wheels) # 不能通过类访问类空间的私有属性
car=Car()
# print(car.__wheels)# 不能通过对象访问类空间的私有属性
# car.__drive()# 不能通过对象访问类空间的私有实例方法
car.test()