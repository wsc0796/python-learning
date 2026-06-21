"""
Day 4 改错题。错误代码放在字符串里。
"""


# 题 1（考点：self，建议 6 分钟）
bug01 = """
class Student:
    def show():
        print("hello")

s = Student()
s.show()
"""


# 题 2（考点：构造方法参数，建议 6 分钟）
bug02 = """
class Car:
    def __init__(self, color):
        self.color = color

car = Car()
"""


# 题 3（考点：私有属性访问，建议 8 分钟）
bug03 = """
class Person:
    def __init__(self):
        self.__age = 20

p = Person()
print(p.__age)
"""


# 题 4（考点：运算符重载，建议 8 分钟）
bug04 = """
class Score:
    def __init__(self, value):
        self.value = value

s1 = Score(80)
s2 = Score(10)
print(s1 + s2)  # 目标：输出 90
"""


# 题 5（考点：多继承方法查找，建议 8 分钟）
bug05 = """
class A:
    def show(self):
        print("A")

class B:
    def show(self):
        print("B")

class C(A, B):
    pass

c = C()
print(c.show)  # 目标：调用 show 方法并观察输出
"""


if __name__ == "__main__":
    print("Day 4 改错题：请复制每段 bug 到临时区域修复。")
