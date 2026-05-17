"""
实践：import模块 + 类型提示
读完 theory_05_module_types.md 后做。
运行：python practice_05.py
"""

# ============================================================
# 第一组：import 标准库
# ============================================================

# TODO 1: 导入 math，打印 pi 和 sqrt(16)
import math
print(f"π = {math.pi}")
print(f"√16 = {math.sqrt(16)}")

# TODO 2: 导入 random，生成 1-100 随机整数
import random
print(f"随机数: {random.randint(1, 100)}")

# TODO 3: 从 datetime 导入 datetime，打印当前时间
from datetime import datetime
# 填 None
print(f"当前时间：{None}")  # TODO: 调用 datetime.now()

# TODO 4: 从 os.path 导入 exists，检查当前目录有没有 practice_05.py
import os
filename = "practice_05.py"
if os.path.exists(filename):
    print(f"{filename} 存在")
else:
    print(f"{filename} 不存在")

# ============================================================
# 第二组：自己写模块（需要先看 my_utils.py）
# ============================================================

# TODO 5: 从 my_utils 导入 greet 和 PI，调用打印
from my_utils import greet, PI

# 调用 greet 和打印 PI
print(None)   # TODO: 调用 greet("张三")
print(None)   # TODO: 打印 PI

# ============================================================
# 第三组：类型提示
# ============================================================

# TODO 6: 给 add 函数加类型提示（int → int）
def add(a, b):
    return a + b

print(f"add(3, 5) = {add(3, 5)}")

# TODO 7: 给 get_first_name 加类型提示（str → str）
def get_first_name(full_name):
    return full_name.split()[0]

print(f"名：{get_first_name('Zhang San')}")

# TODO 8: 给 find_index 加类型提示（list[int], int → Optional[int]）
from typing import Optional

def find_index(items, target):
    for i, item in enumerate(items):
        if item == target:
            return i
    return None

print(f"找到3的索引：{find_index([1, 2, 3, 4], 3)}")
print(f"找不到：{find_index([1, 2, 3, 4], 99)}")

print("\n✅ 05-模块类型 练习完成！")
