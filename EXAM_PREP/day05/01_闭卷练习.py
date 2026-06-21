"""
Day 5 闭卷练习：文件与异常。
"""


# 题 1（考点：open/read，建议 8 分钟）
# 读取 data.txt 全部内容并输出。文件不存在时输出提示。
def task01() -> None:
    pass


# 题 2（考点：readline/readlines，建议 8 分钟）
# 读取 scores.txt 的第一行，再读取所有行。
def task02() -> None:
    pass


# 题 3（考点：write/w，建议 8 分钟）
# 把三行文本写入 result.txt。
def task03() -> None:
    pass


# 题 4（考点：append/a，建议 6 分钟）
# 向 log.txt 追加一行文本。
def task04() -> None:
    pass


# 题 5（考点：文件复制，建议 12 分钟）
# 将 source.txt 内容复制到 target.txt。
def task05() -> None:
    pass


# 题 6（考点：CSV 风格文本读取，建议 12 分钟）
# 读取 scores.csv，每行格式为 name,score。
# 输出每个学生的姓名和整数分数；遇到非法分数时跳过该行。
def task06() -> None:
    pass


# 题 7（考点：try/except/else/finally，建议 10 分钟）
# 输入字符串，尝试转整数，成功输出平方，失败输出错误，最后输出结束。
def task07(value: str) -> None:
    pass


# 题 8（考点：raise/assert，建议 8 分钟）
# 如果 age 不在 0-120，主动抛出异常或断言失败。
def task08(age: int) -> None:
    pass


# 综合题（考点：CSV 文件+异常，建议 20 分钟）
# 读取 scores.csv，每行 name,score，忽略非法行，输出平均分和最高分学生。
def task09() -> None:
    pass


if __name__ == "__main__":
    print("Day 5: 请逐个调用 task01-task08 自测。")
