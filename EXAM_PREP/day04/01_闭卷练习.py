"""
Day 4 闭卷练习：面向对象。
"""


# 题 1（考点：class/self，建议 6 分钟）
# 定义 Student 类，包含 name 属性和 show 方法。
def task01() -> None:
    pass


# 题 2（考点：__init__，建议 8 分钟）
# 定义 Car 类，创建对象时传入 color，并能输出颜色。
def task02() -> None:
    pass


# 题 3（考点：__str__，建议 8 分钟）
# 定义 Book 类，打印对象时显示书名和价格。
def task03() -> None:
    pass


# 题 4（考点：类属性，建议 8 分钟）
# 定义 Car.wheels=4，创建两个对象，观察类属性和实例属性区别。
def task04() -> None:
    pass


# 题 5（考点：类方法/静态方法，建议 10 分钟）
# 定义一个类方法输出类名，一个静态方法判断分数是否及格。
def task05() -> None:
    pass


# 题 6（考点：继承/重写，建议 10 分钟）
# 定义 Animal.cry，Cat 和 Dog 重写 cry。
def task06() -> None:
    pass


# 题 7（考点：封装，建议 10 分钟）
# 定义 Person，私有属性 __age，通过 set_age/get_age 控制范围 0-120。
def task07() -> None:
    pass


# 题 8（考点：多继承，建议 10 分钟）
# 定义 Flyable.run / Swimmable.run 两个父类，再定义 Duck 同时继承它们。
# 创建 Duck 对象并调用 run，观察调用的是哪个父类的方法。
def task08() -> None:
    pass


# 题 9（考点：运算符重载，建议 12 分钟）
# 定义 Score 类，保存 value；实现 __add__，让 Score(80) + Score(10) 得到新的 Score。
# 输出相加后的 value。
def task09() -> None:
    pass


# 题 10（考点：析构方法，建议 8 分钟）
# 定义 FileDemo 类，实现 __init__ 和 __del__，分别打印"创建"和"销毁"。
# 创建对象后使用 del 删除对象，观察输出顺序。
def task10() -> None:
    pass


# 综合题（考点：类+列表，建议 20 分钟）
# 定义 Student 类，保存 name/score；给学生列表，输出最高分学生和平均分。
def task11() -> None:
    pass


if __name__ == "__main__":
    print("Day 4: 请逐个调用 task01-task11 自测。")
