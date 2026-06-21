"""
Day 3 改错题。错误代码放在字符串里。
"""


# 题 1（考点：默认参数位置，建议 6 分钟）
bug01 = """
def f(a=1, b):
    return a + b
"""


# 题 2（考点：return，建议 6 分钟）
bug02 = """
def add(a, b):
    c = a + b

print(add(1, 2) + 3)
"""


# 题 3（考点：作用域，建议 8 分钟）
bug03 = """
x = 1
def f():
    x = x + 1
    print(x)
f()
"""


if __name__ == "__main__":
    print("Day 3 改错题：请复制每段 bug 到临时区域修复。")

