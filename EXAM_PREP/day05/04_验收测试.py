"""
Day 5 验收测试用例。
"""


TESTS = [
    ("task01", "不存在文件时不能崩溃"),
    ("task02", "能说出 readline 和 readlines 的区别"),
    ("task03", "result.txt 应有三行文本"),
    ("task04", "重复运行应追加而不是覆盖"),
    ("task05", "target.txt 内容应与 source.txt 一致"),
    ("task06", "能读取 scores.csv 风格文本，按逗号拆分 name 和 score"),
    ("task07", "输入 'abc' 走 except，输入 '5' 走 else"),
    ("task08", "非法年龄要主动报错"),
    ("task09", "CSV 中非法分数行应跳过或提示，并能统计平均分"),
]


if __name__ == "__main__":
    for name, check in TESTS:
        print(f"{name}: {check}")
