"""
Day 3 闭卷练习：函数专项。
"""


# 题 1（考点：函数定义和返回值，建议 5 分钟）
# 定义函数 add，返回两个数的和。
def task01(a: int, b: int) -> int:
    pass


# 题 2（考点：默认参数，建议 6 分钟）
# 定义函数 greet，name 必填，prefix 默认值为 "你好"。
def task02(name: str, prefix: str = "你好") -> str:
    pass


# 题 3（考点：关键字参数，建议 6 分钟）
# 定义函数 show_student，接收 name 和 score，返回 "姓名:分数"。
def task03(name: str, score: int) -> str:
    pass


# 题 4（考点：*args，建议 8 分钟）
# 接收任意多个数字，返回总和。
def task04(*args: int) -> int:
    pass


# 题 5（考点：**kwargs，建议 8 分钟）
# 接收任意学生信息，逐行输出 key=value。
def task05(**kwargs: object) -> None:
    pass


# 题 6（考点：打包与解包，建议 8 分钟）
# 给定 nums=(3,4)，用解包调用 task01。
def task06(nums: tuple[int, int]) -> int:
    pass


# 题 7（考点：lambda，建议 6 分钟）
# 用 lambda 对列表按分数排序：students=[("A",80),("B",90)]。
def task07(students: list[tuple[str, int]]) -> None:
    pass


# 综合题（考点：函数拆分，建议 20 分钟）
# 写 3 个函数：calc_average、find_max、count_pass，然后在 task08 中调用。
def task08(scores: list[int]) -> None:
    pass


if __name__ == "__main__":
    print("Day 3: 请逐个调用 task01-task08 自测。")

