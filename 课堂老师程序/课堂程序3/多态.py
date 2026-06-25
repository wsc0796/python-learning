__author__ = '86131'
# 多态 让不同类的同一个功能 表现出不同的行为
# 定义父类
class Animal:
    def cry(self):
        pass
# 定义子类
class Cat(Animal):
    def cry(self):
        print("喵喵")

# 定义子类
class Dog(Animal):
    def cry(self):
        print("旺旺")

# 定义一个函数完成适配器功能
# 对于cry()这个函数来说，
#它会把不同对象的功能转换成相同的方法处理
def cry(obj):
    obj.cry()

cat=Cat()#喵喵
dog=Dog()
cry(cat)#喵喵
cry(dog)#旺旺


