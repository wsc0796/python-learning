"""
22 — 深浅拷贝 + os 模块 练习
"""
import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
import copy
import os


# ============================================================
# 练习1：浅拷贝 vs 深拷贝
# ============================================================
original = [1, 2, [3, 4]]

# TODO: 用 copy.copy 浅拷贝，修改内层列表，观察 original 是否受影响
shallow = copy.copy(original)
shallow[2][0] = 99
print("original:", original)   # ? 99 还是 3？
print("shallow:", shallow)

# TODO: 用 copy.deepcopy 深拷贝，再改内层列表
original = [1, 2, [3, 4]]    # 重置
deep = copy.deepcopy(original)
deep[2][0] = 99
print("original:", original)   # ? 3（不受影响）
print("deep:", deep)


# ============================================================
# 练习2：os 模块
# ============================================================
# TODO: 打印当前工作目录
print("当前目录:", os.getcwd())

# TODO: 列出当前目录所有 .py 文件
files = [f for f in os.listdir(".") if f.endswith(".py")]
print("Python 文件:", files)


# ============================================================
# 练习3：pathlib
# ============================================================
from pathlib import Path

# TODO: 创建一个 Path 对象指向 "a/b/c/data.txt"
p = Path("a/b/c/data.txt")
print("文件名:", p.name)       # data.txt
print("不带后缀:", p.stem)     # data
print("后缀:", p.suffix)      # .txt
print("父目录:", p.parent)     # a/b/c


print("\n✅ 22-拷贝os 练习完成！")
