"""
字符串方法练习
规则：每个 TODO 手敲代码，不要复制粘贴
"""

# ======== 查找类 ========

# TODO 1: find() 和 index()
text = "Python is great and Python is fun"
# 1.1 用 find 找 "great" 的位置，打印结果
# 1.2 用 find 找 "Java" 的位置，打印结果
# 1.3 用 index 找 "great" 的位置，打印结果
# 1.4 观察 find 和 index 在找不到时的区别

# TODO 2: startswith / endswith
files = ["report_2024.pdf", "photo.jpg", "data_2024.csv", "notes.txt"]
# 2.1 只打印 .pdf 结尾的文件
# 2.2 只打印以 "data" 开头的文件

# TODO 3: 判断字符串类型
user_inputs = ["123", "abc", "abc123", "hello!", ""]
# 3.1 对每个输入，打印 isdigit 结果
# 3.2 对每个输入，打印 isalpha 结果
# 3.3 对每个输入，打印 isalnum 结果
# 观察哪些字符组合返回什么结果

# ======== 修改类 ========

# TODO 4: replace
text = "I like apples, apples are tasty"
# 4.1 把所有 "apples" 替换为 "oranges"
# 4.2 只替换第一个 "apples"
# 4.3 删除所有的空格（替换为空字符串）

# TODO 5: upper / lower / strip
messages = ["  Hello  ", "WORLD", "  python  "]
# 5.1 对每个字符串：先去两端空格，再转小写，打印结果
# （提示：可以链式调用 .strip().lower()）

# TODO 6: strip 实战
user_input = "  张三  "
# 6.1 去掉两端空格
# 6.2 判断去空格后是否为空（使用真值判断）
# 6.3 如果非空，打印 "你好，{name}"

# ======== 拆分与合并 ========

# TODO 7: split
csv_line = "张三,25,南昌,江西农业大学,软件工程"
# 7.1 用逗号拆分成列表，打印结果
# 7.2 只拆分前 3 个字段，打印结果

# TODO 8: join
words = ["Python", "is", "awesome"]
# 8.1 用空格合并成一个句子
# 8.2 用 "..." 合并
# 8.3 用空字符串合并（"".join）

# TODO 9: 综合题 — CSV 行清洗
raw = "  张三 , 25 , 南昌  "
# 去掉两端空格 → 按逗号拆分 → 每个字段去掉两端空格
# 打印清洗后的列表

# ======== 破坏实验 ========

# TODO 10: 猜猜 find 和 index 哪个会报错
# 在 "hello" 中查找 "xyz"

# TODO 11: join 的错误用法
# 试试 [1, 2, 3].join(",") — 观察报错
# 再试试 ",".join([1, 2, 3]) — 观察报错（不是字符串列表）
# 正确的做法：",".join(["1", "2", "3"])
