---
aliases:
  - 05-cs50p-supplement
---
# Day 5 补充：`sys.argv`、`random` 全家桶、`statistics` 模块

> 来源：CS50P Lecture 5 (Libraries)
> 补充你原笔记缺失的命令行参数和标准库细节

---

## 补充一：`sys.argv` — 命令行参数

**你原笔记有 `import sys` 但没有 `sys.argv`。这是写 CLI 工具的基础。**

```python
import sys

# sys.argv 是一个列表
# sys.argv[0] = 脚本名
# sys.argv[1] = 第一个参数
# 以此类推...

# 例：python greet.py David
# sys.argv = ["greet.py", "David"]

if len(sys.argv) < 2:
    print("用法: python greet.py <名字>")
    sys.exit(1)

name = sys.argv[1]
print(f"Hello, {name}")
```

### 切片获取所有参数

```python
# sys.argv[1:] = 除脚本名外的所有参数
for arg in sys.argv[1:]:
    print(arg)
```

### `sys.exit()` — 主动退出程序

```python
import sys

if len(sys.argv) != 3:
    print("用法: python script.py <arg1> <arg2>")
    sys.exit(1)    # 退出码 1 = 异常退出，0 = 正常退出
```

---

## 补充二：`random` 模块完整用法

**你原笔记只用了 `randint`，CS50P 还重点用了这些：**

```python
import random

# 1. random.choice(seq) — 从序列中随机选一个
houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]
house = random.choice(houses)

# 2. random.shuffle(list) — 原地打乱列表（返回 None！）
cards = ["A", "K", "Q", "J", "10"]
random.shuffle(cards)
print(cards)  # 随机顺序

# ❌ 常见错误：shuffled = random.shuffle(cards)
#    shuffle 返回 None，修改的是原列表

# 3. random.randint(a, b) — [a, b] 之间随机整数（包含两端）
dice = random.randint(1, 6)

# 4. random.random() — [0, 1) 之间随机浮点数
if random.random() < 0.3:   # 30% 概率
    print("触发随机事件")
```

---

## 补充三：`statistics` 模块

```python
import statistics

scores = [85, 92, 78, 90, 88]

print(statistics.mean(scores))    # 平均值: 86.6
print(statistics.median(scores))  # 中位数: 88

grades = ["A", "B", "A", "C", "A", "B"]
print(statistics.mode(grades))    # 众数: "A"
```

这三个函数在数据处理场景很常用，比你手写求和/排序再计算方便。

---

## 补充四：`json` 模块独立用法

**你原笔记在 Pydantic 上下文中用了 JSON，但独立 `json` 模块也有必要了解：**

```python
import json

# Python dict → JSON 字符串
data = {"name": "Harry", "house": "Gryffindor"}
json_str = json.dumps(data)              # 紧凑
json_str = json.dumps(data, indent=2)    # 格式化

# JSON 字符串 → Python dict
json_str = '{"name": "Harry", "house": "Gryffindor"}'
data = json.loads(json_str)

# 直接在文件里读/写 JSON
with open("data.json", "w") as f:
    json.dump(data, f, indent=2)

with open("data.json", "r") as f:
    data = json.load(f)
```

---

## 与Java的对比

| 概念 | Java | Python |
|------|------|--------|
| 命令行参数 | `main(String[] args)` | `sys.argv`（list）|
| 参数切片 | `Arrays.copyOfRange(args, 1, args.length)` | `sys.argv[1:]` |
| 退出程序 | `System.exit(1)` | `sys.exit(1)` |
| 随机数 | `new Random().nextInt(6) + 1` | `random.randint(1, 6)` |
| 随机选一个 | 手写 `list.get(random.nextInt(n))` | `random.choice(list)` |
| 打乱 | `Collections.shuffle(list)` | `random.shuffle(list)` |
| 统计 | 无内置，需 Apache Commons Math | `statistics.mean/median/mode` |
| JSON | Jackson/Gson 库 | `json` 标准库 |
