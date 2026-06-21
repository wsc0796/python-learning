"""
Day 7 改错题。错误代码放在字符串里。
"""


# 题 1（考点：字典 key，建议 6 分钟）
bug01 = """
student = {"name": "Tom", "score": 80}
print(student[name])
"""


# 题 2（考点：遍历删除，建议 8 分钟）
bug02 = """
students = [{"id": 1}, {"id": 2}]
for s in students:
    if s["id"] == 1:
        students.remove(s)
"""


# 题 3（考点：输入转换，建议 8 分钟）
bug03 = """
score = input("score:")
if score >= 60:
    print("pass")
"""


if __name__ == "__main__":
    print("Day 7 改错题：请复制每段 bug 到临时区域修复。")

