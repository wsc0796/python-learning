---
aliases:
  - 23-cs50p-supplement
---
# Day 23 补充：`match`/`case` 结构化模式匹配 (Python 3.10+)

> 来源：CS50P Lecture 2 (Conditionals)
> 补充你原笔记完全缺失的 match/case 语句

---

## `match`/`case` — Python 版的 switch

Python 3.10 引入了 `match`/`case`，功能远超传统 switch：

```python
# 基本用法：值匹配
name = input("What's your name? ")

match name:
    case "Harry":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case "Luna":
        print("Ravenclaw")
    case _:
        print("Who?")
```

`_` 是通配符（default），匹配任何值。

### 比 `if/elif` 好在哪

```python
# 传统的 if/elif — 每行都要重复 status ==
status = 404
if status == 200:
    message = "OK"
elif status == 301:
    message = "Moved Permanently"
elif status == 404:
    message = "Not Found"
elif status == 500:
    message = "Internal Server Error"
else:
    message = "Unknown"

# match/case — 更简洁
status = 404
match status:
    case 200:
        message = "OK"
    case 301:
        message = "Moved Permanently"
    case 404:
        message = "Not Found"
    case 500:
        message = "Internal Server Error"
    case _:
        message = "Unknown"
```

### 多值匹配（用 `|`）

```python
match status:
    case 200 | 201 | 204:
        result = "成功"
    case 301 | 302:
        result = "重定向"
    case 400 | 403 | 404:
        result = "客户端错误"
    case 500 | 502 | 503:
        result = "服务端错误"
```

### 解包匹配 — match 的真正威力

```python
# 匹配元组结构
point = (0, 5)

match point:
    case (0, 0):
        print("原点")
    case (0, y):
        print(f"在 Y 轴上，y={y}")
    case (x, 0):
        print(f"在 X 轴上，x={x}")
    case (x, y):
        print(f"坐标 ({x}, {y})")
```

这种"根据结构 + 值同时判断"的能力是 `if/elif` 写不出来的。

---

## 与Java的对比

| 概念 | Java | Python |
|------|------|--------|
| switch 版本 | 传统 switch（Java 17+ 有增强） | `match`/`case`（Python 3.10+） |
| 穿透（fall-through） | 需要 `break` | **无穿透**，每个 case 独立 |
| 通配符/default | `default:` | `case _:` |
| 结构匹配 | Java 21+ 有 record pattern | 支持 tuple/list/dict 解包 |
| 是否需要 break | 需要 | **不需要** |
