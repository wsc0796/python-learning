"""
Day 8 模拟改错题。错误代码放在字符串里。
"""


bug01 = """
for i in range(1, 6)
    print(i)
"""

bug02 = """
def total(nums):
    for n in nums:
        s += n
    return s
"""

bug03 = """
class Student:
    def __init__(self, name):
        name = name
"""


if __name__ == "__main__":
    print("Day 8 改错题：限时修复并登记错因。")

