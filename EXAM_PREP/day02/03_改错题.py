"""
Day 2 改错题。错误代码放在字符串里，避免文件无法运行。
"""


# 题 1（考点：字符串不可变，建议 6 分钟）
bug01 = """
s = "hello"
s[0] = "H"
print(s)
"""#结果-hello


# 题 2（考点：列表索引，建议 5 分钟）
bug02 = """
nums = [1, 2, 3]
print(nums[3]) 范围是0-2
"""
#索引越界


# 题 3（考点：字典 KeyError，建议 6 分钟）
bug03 = """
scores = {"Tom": 80}
print(scores["Jerry"])
"""
#没有jerry，没有key就没法对应value

if __name__ == "__main__":
    print("Day 2 改错题：请复制每段 bug 到临时区域修复。")

