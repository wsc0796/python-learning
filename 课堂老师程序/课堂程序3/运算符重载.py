__author__ = '86131'
class Calculater(object):
    def __init__(self,number):  # 记录数值
        self.number=number
    def __add__(self, other):  #   重载运算符+
        self.number=self.number+other
        return self.number
    def __sub__(self, other):  #  重载运算符-
        self.number=self.number-other
        return self.number
    def __mul__(self, other):  # 重载运算符*
        self.number=self.number*other
        return self.number
    def __truediv__(self, other):# 重载运算符/
        self.number=self.number/other
        return self.number
calculater=Calculater(10)
print(calculater+5)  # 15 调用calculater对象的__add__方法 实参为5
print(calculater-5)  # 10 调用calculater对象的__sub__方法 实参为5
print(calculater*5)  # 50 调用calculater对象的__mul__方法 实参为5
print(calculater/5)  # 10.0  调用calculater对象的__truediv__方法 实参为5