---
aliases:
  - 02-iterator-generator
---
# 02. 迭代器和生成器深入

> 前置：会用 for 循环、见过 yield、理解函数是一等公民
> 目标：手写迭代器类 + 生成器函数，理解 for 循环底层原理，搞懂 yield from
> 用时：约 20 分钟（分两次读：上半=迭代器协议，下半=生成器深入）
>
> 相关笔记：[[25-function-basics]] · [[18-loops-deep]] · [[16-python-gaps]] · [[01-context-manager]]

---

## Part A：迭代器协议

### 一、两个概念：Iterable vs Iterator

这是 Python 里最容易混淆的概念对之一。搞清楚了，for 循环就不再是魔法。

| 概念 | 中文 | 实现的方法 | 能做啥 |
|------|------|-----------|--------|
| **Iterable** | 可迭代对象 | `__iter__()` | 可以被 `for` 遍历 |
| **Iterator** | 迭代器 | `__iter__()` + `__next__()` | 可以被 `for` 遍历 + 可以被 `next()` 逐个取值 |

**关键区别**：list 是 Iterable，但不是 Iterator。

```python
from collections.abc import Iterable, Iterator

nums = [1, 2, 3]

print(isinstance(nums, Iterable))  # True  — list 可以 for 遍历
print(isinstance(nums, Iterator))  # False — list 不能直接 next()

it = iter(nums)                    # iter() 把 Iterable 变成 Iterator
print(isinstance(it, Iterator))    # True
print(next(it))  # 1
print(next(it))  # 2
print(next(it))  # 3
# next(it) → StopIteration  ← 取完了，不是错误，是"结束"信号
```

**一句话**：Iterable 是"能被遍历的东西"，Iterator 是"正在被遍历的那个东西"。

---

### 二、for 循环的底层原理

```python
for x in [1, 2, 3]:
    print(x)
```

Python 实际执行的是：

```python
it = iter([1, 2, 3])          # 1. 调 __iter__，拿到迭代器

while True:
    try:
        x = next(it)           # 2. 不断调 __next__
        print(x)
    except StopIteration:      # 3. 取完了 → 结束循环
        break
```

**`StopIteration` 不是错误——它是迭代完成的正常信号。**

---

### 三、手写迭代器类

```python
class CountUpTo:
    """从 1 数到 max_num 的迭代器"""
    def __init__(self, max_num):
        self.max_num = max_num
        self.current = 1

    def __iter__(self):
        return self            # 迭代器的 __iter__ 返回自身

    def __next__(self):
        if self.current > self.max_num:
            raise StopIteration   # 到头了，发信号

        value = self.current
        self.current += 1
        return value

# 用 for 循环
for num in CountUpTo(3):
    print(num)   # 1, 2, 3

# 用手动 next
c = CountUpTo(3)
print(next(c))  # 1
print(next(c))  # 2
print(next(c))  # 3
```

**迭代器的状态是内部的**——`self.current` 记录了"走到哪了"。同一个迭代器不能"倒回去"——取完了就是取完了。

---

### 四、可迭代对象 ≠ 迭代器（重点）

```python
class CountUpTo:
    def __init__(self, max_num):
        self.max_num = max_num

    def __iter__(self):
        """每次调用都返回一个新的迭代器"""
        return _CountIterator(self.max_num)


class _CountIterator:
    def __init__(self, max_num):
        self.max_num = max_num
        self.current = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.max_num:
            raise StopIteration
        value = self.current
        self.current += 1
        return value

# 这样每次 for 循环都能从头开始
for num in CountUpTo(3):
    print(num)   # 1, 2, 3

for num in CountUpTo(3):   # ← 第二次 for 也能正常工作
    print(num)   # 1, 2, 3
```

**设计原则**：可迭代对象的 `__iter__()` 每次返回**新的**迭代器；迭代器的 `__iter__()` 返回**自己**。

---

## Part B：生成器深入

### 五、生成器函数 — 包含 yield 的函数

```python
def count_up_to(max_num):
    """生成器版本 — 比类版短得多"""
    current = 1
    while current <= max_num:
        yield current
        current += 1

# 调用生成器函数 → 返回生成器对象（不执行函数体！）
g = count_up_to(3)
print(g)        # <generator object count_up_to at 0x...>

print(next(g))  # 1 — 执行到第一个 yield，暂停
print(next(g))  # 2 — 从上次暂停处继续，到下一个 yield
print(next(g))  # 3
# next(g) → StopIteration
```

**`yield` 做了什么**：
1. 返回一个值（和 `return` 一样）
2. **暂停函数**，记住当前位置和所有局部变量
3. 下次 `next()` 时从暂停处**继续执行**

**`return` vs `yield`**：

| | `return` | `yield` |
|---|---|---|
| 返回值 | ✓ | ✓ |
| 函数结束 | ✓ | ✗（只是暂停） |
| 下次调用 | 从头开始 | 从上次暂停处继续 |
| 可以多次 | ✗ | ✓ |

---

### 六、生成器的惰性求值

```python
# 列表：一次性生成 100 万个数字，占大量内存
nums = [x * x for x in range(1_000_000)]

# 生成器：什么都没算，只是一个"承诺"
nums_gen = (x * x for x in range(1_000_000))
# 用的时候才算
print(next(nums_gen))  # 0
print(next(nums_gen))  # 1
```

**生成器表达式**：把列表推导式的 `[]` 换成 `()`。

```python
sum(x * x for x in range(1_000_000))   # 不需要中间列表
```

---

### 七、`yield from` — 委托给另一个生成器

```python
def gen_a():
    yield 1
    yield 2

def gen_b():
    yield from gen_a()    # 把产出委托给 gen_a
    yield 3

for x in gen_b():
    print(x)   # 1, 2, 3
```

`yield from iterable` 近似等价于：

```python
for item in iterable:
    yield item
```

但 `yield from` 更强大——它还处理了 `send()`、`throw()`、`close()` 等协程协议。这在 async/await 的底层实现中是关键机制。

### 实战：递归展平嵌套列表

```python
def flatten(nested):
    for item in nested:
        if isinstance(item, list):
            yield from flatten(item)   # 递归委托
        else:
            yield item

nested = [1, [2, 3], [4, [5, 6]]]
print(list(flatten(nested)))  # [1, 2, 3, 4, 5, 6]
```

---

### 八、生成器和上下文管理器的关联

`@contextmanager` 就是基于生成器实现的：

```python
from contextlib import contextmanager

@contextmanager
def demo():
    # __enter__ 逻辑
    print("enter")
    yield "value"
    # __exit__ 逻辑
    print("exit")
```

`yield` 在这里扮演了"分界线"角色：
- 之前 = `__enter__`
- 之后 = `__exit__`

---

### 九、生成器和 async/await 的历史关系

Python 的协程（coroutine）最早就是从生成器演化来的：

```
Python 2.5: yield 可以接收值（send）
Python 3.3: yield from（委托子生成器）
Python 3.4: asyncio 模块诞生
Python 3.5: async def / await 成为正式语法
```

核心思想一脉相承：**暂停 → 让出控制权 → 等待恢复**。理解了 `yield` 的暂停/恢复，`await` 就好理解一半了。

---

## 十、常见易错点

| 易错点 | 说明 |
|--------|------|
| list 可以 for 但不能 next | list 是 Iterable，不是 Iterator。用 `iter()` 转换 |
| 迭代器是一次性的 | 取完后不会自动重头开始，需要新建 |
| 调用生成器函数不会执行函数体 | 返回的是生成器对象，`next()` 才开始执行 |
| `yield` 不是 `return` | yield 暂停 + 可恢复，return 是终点 |
| `StopIteration` 是正常信号 | 不是异常情况，for 循环自动处理 |
| 生成器耗尽后再 next | 抛 `StopIteration` |
