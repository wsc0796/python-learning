---
aliases:
  - 03-cs50p-supplement
---
# Day 3 补充：`raise` 语句 + CSV 模块

> 来源：CS50P Lecture 4 (Exceptions) + Lecture 7 (File I/O)
> 补充你原笔记缺失的 `raise`、`pass`、`csv` 模块

---

## 补充一：`raise` — 主动抛出异常

**你原笔记覆盖了 `try/except`（接住异常），但没覆盖 `raise`（主动抛出）。**

### 什么时候用 `raise`

当函数的参数不合法时，你应该**主动告诉调用者**，而不是：
- `print("出错了")` → 程序继续跑，数据已经脏了
- `sys.exit()` → 太暴力，整个程序都没了

```python
def create_student(name):
    if not name:
        raise ValueError("学生必须有名字")  # 主动抛出
    return {"name": name}

# 调用者可以选择接住
try:
    student = create_student("")
except ValueError as e:
    print(f"创建失败: {e}")
```

### `raise` vs `return None`

```python
# ❌ 不好：返回 None，调用者可能忘了检查
def get_score(student):
    if student not in scores:
        return None
    return scores[student]

# ✅ 好：抛出异常，强迫调用者处理
def get_score(student):
    if student not in scores:
        raise KeyError(f"学生 {student} 不在成绩表中")
    return scores[student]
```

**Python 的设计哲学**：与其返回错误码让调用者忘记检查，不如抛异常让代码在错误处直接停下来。

### 在 `__init__` 中用 `raise` 做验证

这是 CS50P OOP 讲的核心模式——在对象创建时就验证数据：

```python
class Student:
    def __init__(self, name, house):
        if not name:
            raise ValueError("Missing name")
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError(f"Invalid house: {house}")
        self.name = name
        self.house = house
```

---

## 补充二：`pass` — 占位符语句

`pass` 就是"什么都不做"。你原笔记只在 ABC 抽象方法中用到，但它的通用场景更多：

```python
# 1. 占位 — 函数还没想好怎么写，但需要语法正确
def future_feature():
    pass    # TODO: 以后实现

# 2. 空异常处理 — 有些错误可以安全忽略
try:
    os.remove("temp.txt")
except FileNotFoundError:
    pass    # 文件本来就不存在，无所谓

# 3. 空类
class EmptyContainer:
    pass
```

---

## 补充三：`csv` 模块 — 别再手动 `split(",")` 了

**你原笔记解析 CSV 用 `line.split(",")`，这在字段包含逗号时会出错。Python 标准库的 `csv` 模块处理了所有边界情况。**

### `csv.reader` — 按行读取

```python
import csv

with open("students.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(f"{row[0]} is in {row[1]}")
        # row 是一个 list，每个元素是一个字段
```

### `csv.DictReader` — 按列名读取（推荐）

```python
with open("students.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(f"{row['name']} is in {row['house']}")
        # row 是一个 OrderedDict，用列名访问
```

这是最推荐的方式 —— 不需要记住列的顺序，代码可读性最高。

### `csv.writer` / `csv.DictWriter` — 写入 CSV

```python
# writer: list 方式写入
with open("output.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["name", "house"])        # 写表头
    writer.writerow(["Harry", "Gryffindor"])  # 写数据

# DictWriter: 字典方式写入
with open("output.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["name", "house"])
    writer.writeheader()
    writer.writerow({"name": "Harry", "house": "Gryffindor"})
```

| 对比 | 手动 `split(",")` | `csv` 模块 |
|------|-------------------|-----------|
| 字段含逗号 | ❌ 错误 | ✅ 正确处理（引号包裹） |
| 字段含换行 | ❌ 错误 | ✅ 正确处理 |
| 字段含引号 | ❌ 需手动处理 | ✅ 自动转义 |
| 代码量 | 少 | 多 2 行 |
| 可靠性 | 差 | 好 |
