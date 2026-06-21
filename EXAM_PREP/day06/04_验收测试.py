"""
Day 6 验收测试用例。
"""


TESTS = [
    ("task01", "calc(3, 2, '+') 应能返回正确结果"),
    ("task02", "任意多个姓名都能输出"),
    ("task03", "能分块统计文件字符数"),
    ("task04", "能写入 name,score 文本"),
    ("task05", "能解释类属性和实例属性变化"),
    ("task06", "同一函数能调用 Cat/Dog 的 cry"),
    ("task07", "safe_int('abc') 不崩溃"),
    ("task08", "综合题能串起文件、异常、类、列表"),
]


if __name__ == "__main__":
    for name, check in TESTS:
        print(f"{name}: {check}")

