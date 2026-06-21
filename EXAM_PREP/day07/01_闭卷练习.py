"""
Day 7 闭卷练习：学生管理系统综合题。

要求：优先完成列表+字典版，不要一开始就写类版本。
"""


# 题 1（考点：数据结构，建议 6 分钟）
# 创建一个空学生列表，并添加一名学生字典。
def task01() -> None:
    pass


# 题 2（考点：新增，建议 10 分钟）
# 写 add_student(students, name, score)，自动生成 id。
def task02(students: list[dict], name: str, score: int) -> None:
    pass


# 题 3（考点：查询，建议 10 分钟）
# 按 id 查询学生，找到则输出，找不到输出提示。
def task03(students: list[dict], student_id: int) -> None:
    pass


# 题 4（考点：修改，建议 12 分钟）
# 按 id 修改学生分数。
def task04(students: list[dict], student_id: int, new_score: int) -> None:
    pass


# 题 5（考点：删除，建议 12 分钟）
# 按 id 删除学生。
def task05(students: list[dict], student_id: int) -> None:
    pass


# 题 6（考点：统计，建议 10 分钟）
# 输出平均分、最高分、及格人数。
def task06(students: list[dict]) -> None:
    pass


# 题 7（考点：输入异常，建议 10 分钟）
# 写 safe_input_score，把输入字符串安全转成 0-100 的整数。
def task07(value: str) -> int | None:
    pass


# 综合题（考点：菜单循环，建议 30 分钟）
# 写 main_menu，支持添加、查询、修改、删除、显示、退出。
def task08() -> None:
    pass


if __name__ == "__main__":
    print("Day 7: 请先完成 task01-task07，再写菜单综合题。")

