__author__ = '86131'
# 若子类重写父类的方法，子类对象默认调用的是子类重写的方法
class Person:
    def say_hello(self):
        print("打招呼！")
class Chinese(Person):  #定义子类继承Person类
    def say_hello(self): #重写 父类的方法
        print("吃了吗")
chinese=Chinese()
chinese.say_hello() # 吃了吗