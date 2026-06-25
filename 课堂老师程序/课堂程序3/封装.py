__author__ = '86131'
# 封装的基本思想是对外隐藏类的细节，提供用于访问类成员的公开接口
# 要求1.将属性声明为私有属性。2.提供两个供外界调用的公有方法，分别用于设置和获取私有属性的值，
class Person:
    def __init__(self):
        self.__age=1  #私有属性 ，默认为1岁
    # 设置私有属性值的方法
    def set_age(self,age):
        if 0<age<=120 :
            self.__age=age
        else:
            print("输入错误")
    #获取私有属性值的方法
    def get_age(self):
        return self.__age
person=Person()
person.set_age(220)
# print (person.__age)  # 对象不能直接访问其私有属性
print(f"年龄为{person.get_age()}岁 ")# 年龄为20岁

