"""
Day 4 验收测试用例。
"""


TESTS = [
    ("task01", "Student 类应有 name 和 show"),
    ("task02", "Car 对象应能保存并输出 color"),
    ("task03", "Book 对象 print 时应显示关键信息"),
    ("task04", "能说明类属性和实例属性的区别"),
    ("task05", "能调用类方法和静态方法"),
    ("task06", "Cat/Dog 同名方法输出不同结果"),
    ("task07", "非法 age 不应被设置"),
    ("task08", "能写最小多继承例子并观察方法查找顺序"),
    ("task09", "能写最小 __add__ 运算符重载例子"),
    ("task10", "能识别 __del__ 析构方法触发时机"),
    ("task11", "能用对象列表完成成绩统计"),
]


if __name__ == "__main__":
    for name, check in TESTS:
        print(f"{name}: {check}")
