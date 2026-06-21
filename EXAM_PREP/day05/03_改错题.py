"""
Day 5 改错题。错误代码放在字符串里。
"""


# 题 1（考点：文件关闭/with，建议 6 分钟）
bug01 = """
f = open("data.txt", "r", encoding="utf-8")
content = f.read()
print(content)
"""


# 题 2（考点：写入类型，建议 6 分钟）
bug02 = """
with open("a.txt", "w", encoding="utf-8") as f:
    f.write(123)
"""


# 题 3（考点：异常类型顺序，建议 8 分钟）
bug03 = """
try:
    n = int("abc")
except Exception:
    print("all")
except ValueError:
    print("value")
"""


if __name__ == "__main__":
    print("Day 5 改错题：请复制每段 bug 到临时区域修复。")

