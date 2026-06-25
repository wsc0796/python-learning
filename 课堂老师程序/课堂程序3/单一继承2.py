__author__ = '86131'

class Animal:# 定义父类 默认继承基类object 相当于class Animal(object)
    def __init__(self,age):
        self.__age=age      # 私有属性
    def get_age(self):
        return self.__age
class Cat(Animal): # 定义子类
    def __init__(self,color,age):
        super().__init__(age)
        self.__color=color
    def get_color(self):
        return self.__color
cat=Cat("灰色",3)
print(cat.get_age(),cat.get_color())