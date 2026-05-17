---
aliases:
  - 05-module-types
---
# Day 5：模块/import + 类型提示

读完约 6 分钟。

> 相关笔记：[函数基础](../25-function-basics/theory_25_function_basics.md) · [类型提示进阶/DI](../08-typing-di/theory_08_typing_di.md)

---

## 一、模块：把代码拆到多个文件

### 你已经会的（类比 Java）

```java
// Java
import java.util.ArrayList;
import com.myapp.utils.StringHelper;
```

```python
# Python
from collections import defaultdict
from myapp.utils import StringHelper
```

**同一个概念，语法略不同。**

### 三种 import 写法

```python
# 方式1：导入整个模块
import math
print(math.sqrt(16))    # 4.0 —— 用的时候要写 模块名.函数名

# 方式2：从模块里导入特定东西
from math import sqrt
print(sqrt(16))         # 4.0 —— 直接用函数名，不用写模块名

# 方式3：导入所有（不推荐，会污染命名空间）
from math import *
print(sqrt(16))         # 能用但不知道 sqrt 哪来的
```

**推荐方式1和2。** 方式3会导致「这个名字到底从哪来的」之类的问题。

### 自己写模块

假设你有两个文件：

```python
# my_utils.py —— 这是你的模块文件
def greet(name):
    return f"Hello, {name}!"

PI = 3.14159
```

```python
# main.py —— 这是主程序
from my_utils import greet, PI

print(greet("张三"))   # Hello, 张三!
print(PI)              # 3.14159
```

**就这么简单：** 把函数写在 `.py` 文件里 → 另一个文件 import → 直接用。跟 Java 的 import 一样。

### 常用标准库速查

| 模块 | 干什么 | 例子 |
|------|--------|------|
| `math` | 数学函数 | `math.sqrt()`, `math.pi` |
| `random` | 随机数 | `random.randint(1, 10)` |
| `datetime` | 日期时间 | `datetime.datetime.now()` |
| `os` | 操作系统相关 | `os.path.exists("file.txt")` |
| `json` | JSON 读写 | `json.loads('{"a": 1}')` |
| `collections` | 高级容器 | `defaultdict`, `Counter` |

---

## 二、类型提示：让代码更清楚

### 没有类型提示的 Python

```python
def add(a, b):
    return a + b
```

别人（包括三个月后的自己）不知道 a 和 b 应该传什么类型。int？float？str？

### 加了类型提示

```python
def add(a: int, b: int) -> int:
    return a + b
```

看函数签名就知道：传两个 int，返回一个 int。

### 语法

```python
变量名: 类型      # 参数类型
-> 类型           # 返回值类型

def greet(name: str) -> str:
    return f"Hello, {name}!"

def divide(a: int, b: int) -> float:
    return a / b

def get_scores() -> list[int]:      # list[int] = 元素都是int的列表
    return [95, 87, 92]
```

### 类型提示不强制

```python
def add(a: int, b: int) -> int:
    return a + b

add("Hello, ", "World")   # 不会报错！Python 不强制类型检查
```

**类型提示是给人看的，不是给 Python 强制执行的。** 相当于代码里的文档。

### 常见类型

| 类型提示 | 含义 |
|---------|------|
| `int` | 整数 |
| `float` | 浮点数 |
| `str` | 字符串 |
| `bool` | 布尔值 |
| `list[int]` | 元素为 int 的列表 |
| `dict[str, int]` | 键为 str，值为 int 的字典 |
| `tuple[int, str]` | 固定结构的元组 |
| `None` | 空值（返回值类型常用） |
| `Optional[str]` | 可能是 str，也可能是 None |

---

## 当前级别许可

| 内容 | 状态 |
|------|------|
| import/模块 | ✅ 今天可以学（在综合练习中导入 math 等标准库） |
| 自己写模块 | ✅ 今天可以学 |
| 类型提示 | ✅ 今天可以了解，不要求每个函数都写 |
