---
aliases:
  - 22-copy-os
---
# 深浅拷贝 + os 模块

> 前置：已掌握 mutable/immutable 区别
> 用时：约 8 分钟
>
> 相关笔记：[Mutable vs Immutable](../16-python-gaps/theory_16_python_gaps.md) · [列表引用问题](../21-list-deep/theory_21_list_deep.md)

---

## 一、深浅拷贝

### 为什么需要拷贝？

```python
a = [1, 2, 3]
b = a          # 不是拷贝，是别名
b.append(4)
print(a)       # [1, 2, 3, 4] — a 也被改了！
```

`b = a` 不是拷贝，只是两个变量指向**同一个列表对象**。可以用 `id()` 验证：

```python
a = [1, 2, 3]
b = a

print(id(a), id(b))   # 地址相同
print(a is b)          # True
```

**不可变对象不需要担心这个**：`int`、`str`、`tuple` 不能原地修改，赋值后修改变量只会让它指向新对象，原变量不受影响：

```python
x = 10
y = x
y = 20
print(x)  # 10 — 不受影响

s1 = "hello"
s2 = s1
s2 += " world"
print(s1)  # "hello"
```

需要重点关注的是可变对象：`list`、`dict`、`set`。

### 浅拷贝：只拷贝第一层

```python
import copy

a = [1, 2, [3, 4]]
b = copy.copy(a)   # 浅拷贝

b[0] = 99          # ✅ 第一层独立了
print(a[0])        # 1 — 不受影响

b[2][0] = 999      # ❌ 内层列表还是共享的
print(a[2][0])     # 999 — 被改了！
```

除了 `copy.copy()`，列表还有很多常见的浅拷贝写法：

```python
a = [1, 2, [3, 4]]

b = a.copy()       # ✅ 列表的 .copy() 方法
c = a[:]           # ✅ 切片
d = list(a)        # ✅ list() 构造

# 它们都是浅拷贝：第一层独立，内层共享
c[2][0] = 999
print(a[2][0])     # 999
```

字典和集合也有浅拷贝：

```python
# 字典浅拷贝
a = {"name": "Tom", "scores": [90, 80]}
b = a.copy()

b["name"] = "Jerry"       # ✅ 第一层独立
print(a["name"])          # Tom

b["scores"][0] = 100      # ❌ 内层列表共享
print(a["scores"])        # [100, 80]

# 集合浅拷贝
a = {1, 2, 3}
b = a.copy()
b.add(4)
print(a)  # {1, 2, 3} — 不受影响（集合没有嵌套结构）
```

### 深拷贝：全部独立

```python
import copy

a = [1, 2, [3, 4]]
b = copy.deepcopy(a)

b[2][0] = 999
print(a[2][0])     # 3 — 完全独立，不受影响
```

深拷贝会递归复制内部的可变对象。注意不可变对象（如 `int`、`str`）可能仍然共享，但这不会产生副作用：

```python
a = [1, 2, "hello"]
b = copy.deepcopy(a)

print(a[0] is b[0])   # True — 整数不可变，共享也没关系
print(a[2] is b[2])   # True — 字符串同理
print(a is b)          # False — 列表本身是新的
```

### 深拷贝不是万能药

```python
import copy

# 大数据结构时深拷贝很慢
big_data = [[i] * 1000 for i in range(1000)]
# copy.deepcopy(big_data)  # 可能卡几秒

# 某些对象不能深拷贝
f = open("test.txt", "w")
# copy.deepcopy(f)        # 可能报错（文件句柄）
```

| 操作                 | 新对象？ | 内层共享？ | 适用场景        |
| ------------------ | ---- | ----- | ----------- |
| `b = a`            | 否    | 完全共享  | 不需要独立修改时    |
| `copy.copy(a)`     | 是    | 是     | 只有一层，或内层不修改 |
| `a.copy()`         | 是    | 是     | 列表/字典常用浅拷贝  |
| `a[:]` / `list(a)` | 是    | 是     | 列表浅拷贝       |
| `copy.deepcopy(a)` | 是    | 否     | 嵌套结构需要完全独立  |

### 实用建议

```python
# 90% 的情况不需要拷贝，直接赋值就行
# 8% 的情况浅拷贝够用（列表里没有嵌套可变对象）
# 2% 的情况需要深拷贝（嵌套结构）

# - 纯数字/字符串的列表 → 浅拷贝就够
# - 嵌套列表/字典 → 深拷贝
# - 性能有要求 → 考虑其他方案（深拷贝慢）
```

## 二、os 模块常用函数

```python
import os

# 文件和目录操作
os.getcwd()         # 当前工作目录
os.listdir(".")     # 列出当前目录所有文件和文件夹
os.mkdir("新文件夹") # 创建目录
os.makedirs("a/b/c") # 创建多级目录（a/b/c）
os.rmdir("空文件夹") # 删除空目录
os.remove("文件.txt") # 删除文件
os.rename("旧名", "新名") # 重命名

# 路径操作
os.path.join("a", "b", "c.txt")  # "a/b/c.txt" — 自动处理分隔符
os.path.exists("文件.txt")        # True/False
os.path.isfile("文件.txt")        # 是不是文件
os.path.isdir("文件夹")           # 是不是目录
os.path.getsize("文件.txt")       # 文件大小（字节）
os.path.splitext("a/b/c.txt")    # ('a/b/c', '.txt')

# 用 pathlib 更现代（Python 3.4+）
from pathlib import Path

p = Path("a/b/c.txt")
print(p.parent)     # a/b
print(p.name)       # c.txt
print(p.stem)       # c（不带后缀）
print(p.suffix)     # .txt

Path("新目录").mkdir(exist_ok=True)  # 创建目录，存在也不报错
```
