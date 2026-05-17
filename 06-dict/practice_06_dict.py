"""
06 — 字典 dict 练习
相关 Hot100 题目：第1题（两数之和）、第49题（字母异位词分组）
"""
import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
from typing import Any

# ============================================================
# 练习1：字典的基本操作
# ============================================================

def ex_1_basic():
    """创建字典，增删改查"""
    # ① 创建一个空字典 student
    student: dict[str, Any] = None  # TODO

    # ② 添加 key: "name", value: "张三"
    # TODO

    # ③ 添加 key: "score", value: 95
    # TODO

    # ④ 如果 "name" 在字典中，打印 student["name"]
    # TODO

    # ⑤ 把 "name" 改成 "李四"
    # TODO

    # ⑥ 删除 "score"
    # TODO

    return student


# ============================================================
# 练习2：使用 get 安全取值
# ============================================================

def ex_2_get_safe():
    """用 get 代替直接取"""
    person = {"name": "小明", "age": 18}

    # ① 用 get 取 "name"，期望 "小明"
    name = None  # TODO: 用 get
    print(f"name = {name}")

    # ② 用 get 取 "gender"，不存在时返回 "未知"
    gender = None  # TODO: 用 get + 默认值
    print(f"gender = {gender}")

    # ③ 用 get 取 "age"，不存在时返回 0
    age = None  # TODO: 用 get + 默认值
    print(f"age = {age}")


# ============================================================
# 练习3：遍历字典
# ============================================================

def ex_3_iterate():
    """遍历 key 和 items"""
    scores = {"语文": 85, "数学": 92, "英语": 78}

    # ① 遍历 key，打印"科目名: 分数"
    # TODO: for 循环

    # ② 用 .items() 实现同样的效果
    # TODO: for 循环

    # ③ 计算总分
    total = 0
    # TODO: 遍历 values 累加
    print(f"总分: {total}")


# ============================================================
# 练习4：分组模式（Hot100 第49题）
# ============================================================

def ex_4_group_by():
    """用 dict 对单词按首字母分组"""
    words = ["apple", "banana", "avocado", "blueberry", "cherry"]

    # 用首字母分组：
    # {"a": ["apple", "avocado"], "b": ["banana", "blueberry"], "c": ["cherry"]}
    groups = {}

    for word in words:
        first = None  # TODO: 取首字母
        if None:       # TODO: 首字母不在字典中
            None        # TODO: 初始化空列表
        None            # TODO: 把单词加进去

    print(groups)


# ============================================================
# 练习5：计数模式（dict 的另一个高频用法）
# ============================================================

def ex_5_count():
    """统计每个字母出现的次数"""
    text = "hello world"

    # {"h": 1, "e": 1, "l": 3, "o": 2, " ": 1, "w": 1, "r": 1, "d": 1}
    count = {}

    for char in text:
        if char not in count:
            count[char] = 0
        None  # TODO: 累加

    print(count)


# ============================================================
# 练习6（破坏实验）
# ============================================================

def ex_6_destroy():
    """故意写错，看看报错长什么样"""

    d = {"a": 1, "b": 2}

    # ① 取一个不存在的 key，用 [] 直接取
    # TODO: 取消注释，看报错
    # d["c"]

    # ② 删除一个不存在的 key
    # TODO: 取消注释，看报错
    # del d["c"]

    # ③ key 用可变类型（列表）
    # TODO: 取消注释，看报错
    # d[[1, 2, 3]] = "列表"
    # 报错信息会告诉你为什么——记住这个规则


# ============================================================
# 运行
# ============================================================

if __name__ == "__main__":
    print("=== 练习1 ===")
    print(ex_1_basic())

    print("\n=== 练习2 ===")
    ex_2_get_safe()

    print("\n=== 练习3 ===")
    ex_3_iterate()

    print("\n=== 练习4 ===")
    ex_4_group_by()

    print("\n=== 练习5 ===")
    ex_5_count()

    print("\n=== 练习6 ===")
    ex_6_destroy()
