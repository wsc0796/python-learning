"""
Day 6 闭卷练习：老师课堂代码重放。
"""


# 题 1（来源：课堂程序1 函数定义，建议 8 分钟）
# 写函数 calc，接收两个数和运算符 "+/-/*"，返回计算结果。
def task01(a: int, b: int, op: str) -> int:
    pass


# 题 2（来源：课堂程序1 参数打包，建议 8 分钟）
# 写函数 print_names，接收任意多个姓名并逐个输出。
def task02(*names: str) -> None:
    pass


# 题 3（来源：课堂程序2 文件读取，建议 10 分钟）
# 分块读取 source.txt，每次 100 个字符，统计总字符数。
def task03() -> None:
    pass


# 题 4（来源：课堂程序2 CSV/文本写入，建议 10 分钟）
# 把学生姓名和分数按 "name,score" 格式写入 scores.csv。
def task04(students: list[tuple[str, int]]) -> None:
    pass


# 题 5（来源：课堂程序3 类属性，建议 10 分钟）
# 写 Car 类，包含类属性 wheels，实例属性 color。
def task05() -> None:
    pass


# 题 6（来源：课堂程序3 多态，建议 10 分钟）
# 写 Animal、Cat、Dog，并用同一个函数调用 cry。
def task06() -> None:
    pass


# 题 7（来源：课堂程序4 异常，建议 10 分钟）
# 写函数 safe_int，把字符串转整数；失败时返回 None。
def task07(value: str) -> int | None:
    pass


# 综合题（来源：课堂程序1-4 综合，建议 25 分钟）
# 读取 scores.txt，安全转换分数，创建 Student 对象列表，输出及格学生。
def task08() -> None:
    pass


# 题 9（来源：课堂程序3 多继承，建议 10 分钟）
# 定义两个父类 TeacherRole / AdminRole，各有一个 work 方法。
# 定义 HeadTeacher 同时继承它们，创建对象并调用 work，观察方法查找顺序。
def task09() -> None:
    pass


# 题 10（来源：课堂程序3 运算符重载，建议 12 分钟）
# 定义 Money 类，保存 amount，实现 __add__，让两个 Money 对象能相加。
def task10() -> None:
    pass


# 题 11（来源：课堂程序3 析构方法，建议 8 分钟）
# 定义 Resource 类，在 __init__ 中打印"打开资源"，在 __del__ 中打印"释放资源"。
def task11() -> None:
    pass


if __name__ == "__main__":
    print("Day 6: 请逐个调用 task01-task11 自测。")
