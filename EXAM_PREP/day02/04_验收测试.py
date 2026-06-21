"""
Day 2 验收测试用例。
"""


TESTS = [
    ("task01", ("python",), "核对前三个、最后两个、倒序"),
    ("task02", ("i love python",), "核对 split 和 join"),
    ("task03", ([3, 0, 2],), "核对添加、删除、排序"),
    ("task04", ((3, 4),), "核对元组解包或索引"),
    ("task05", ("banana",), "核对字符计数字典"),
    ("task06", ([1, 2, 2, 3],), "核对去重结果和数量"),
    ("task07", (8,), "核对偶数平方列表"),
    ("task08", ([{"name": "A", "score": 80}, {"name": "B", "score": 59}],), "核对最高、平均、及格人数"),
]


if __name__ == "__main__":
    for name, args, check in TESTS:
        print(f"{name}{args}: {check}")

