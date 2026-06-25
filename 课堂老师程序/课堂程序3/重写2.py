__author__ = '86131'
# 子类重写父类的方法后，无法直接访问父类的同名方法，
#可以使用super()函数间接调用父类中重写前的方法
class Person:
    def say_hello(self):
        print("打招呼！")
class Chinese(Person):  #定义子类继承Person类
    def say_hello(self): #重写 父类的方法
        super().say_hello() # 调用父类重写前的方法 打招呼！
        print("吃了吗?") # 吃了吗?
chinese=Chinese()
chinese.say_hello()