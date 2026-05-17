---
aliases:
  - 16-python-gaps
---
# Python 基础补漏：14 个必须知道的知识点

> 都是"天天用但没人专门教"的东西
> 读完约 15 分钟，分 4 组
>
> 相关笔记：[函数基础](../25-function-basics/theory_25_function_basics.md) · [列表深入操作](../21-list-deep/theory_21_list_deep.md)

---

## 第一组：每天都在碰

### 1. None 和真值（Truthiness）

```python
# None = "空"，不是 0 也不是 False
x = None
print(x is None)   # True — 判断 None 用 is，不用 ==
print(x == None)   # 也能跑，但不推荐

# 真值：if x 在检查什么？
# 以下值被视为 False：
#   None, 0, 0.0, ""(空字符串), [](空列表), {}(空字典), set()
# 其他所有值都是 True

if None:       # False
    print("不会执行")

if 0:          # False
    print("不会执行")

if "":         # False
    print("不会执行")

if "abc":      # True
    print("会执行")

if []:         # False
    print("不会执行")

if [1, 2]:     # True
    print("会执行")
```

**实用判断指南**：
- **检查 None**: `if x is None:` / `if x is not None:`
- **检查空列表**: `if not x:`（清晰简洁）
- **检查数值为 0**: `if x != 0:`（而不是 `if x is not 0`）

### 2. `is` vs `==`：身份 vs 相等

```python
a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(a == b)   # True — 内容一样（相等）
print(a is b)   # False — 不是同一个对象（身份）
print(a is c)   # True — c 就是 a 的别名
```

**`==` 调 `__eq__`，`is` 比内存地址**。

```python
# 容易踩的坑
x = 256
y = 256
print(x is y)   # True — Python 对小整数（-5~256）做了缓存

x = 1000
y = 1000
print(x is y)   # 可能是 False！大整数不缓存

# 所以：永远用 == 比数字，用 is 比 None
```

### 3. Mutable vs Immutable

```python
# 不可变（Immutable）：改了就是新对象
a = "hello"
b = a
a += " world"   # 创建了新字符串
print(a)         # "hello world"
print(b)         # "hello" — b 没受影响

# 可变（Mutable）：改了还是同一个对象
a = [1, 2, 3]
b = a
a.append(4)     # 直接在原列表上改
print(a)         # [1, 2, 3, 4]
print(b)         # [1, 2, 3, 4] — b 也变了！
```

| 不可变 | 可变 |
|--------|------|
| `int`, `float`, `bool` | `list` |
| `str` | `dict` |
| `tuple` | `set` |
| `frozenset` | 自定义类实例 |

**最常见的坑**：

```python
# 坑1：默认参数的陷阱
def add_item(item, lst=[]):     # lst 只创建一次
    lst.append(item)
    return lst

print(add_item(1))   # [1]
print(add_item(2))   # [1, 2] — 不是 [2]！
```

```python
# 修复：用 None
def add_item(item, lst=None):
    if lst is None:
        lst = []
    lst.append(item)
    return lst
```

### 4. 三元表达式

```python
# Java: cond ? value_if_true : value_if_false
# Python: value_if_true if cond else value_if_false

age = 20
status = "成年" if age >= 18 else "未成年"
print(status)   # 成年

# 嵌套（不推荐超过一层）
score = 85
grade = "优秀" if score >= 90 else "良好" if score >= 80 else "及格"
```

---

## 第二组：天天用的函数

### 5. `*args` 和 `**kwargs`

```python
# *args = 任意数量的位置参数 → 打包成元组
# **kwargs = 任意数量的关键字参数 → 打包成字典

def log(message, *tags):
    """第一个参数必传，后面的任意数量"""
    print(f"[{', '.join(tags)}] {message}")

log("服务器启动")                  # [] 服务器启动
log("用户登录", "INFO", "AUTH")   # [INFO, AUTH] 用户登录


def create_profile(**info):
    """接收任意关键字参数"""
    for key, value in info.items():
        print(f"{key}: {value}")

create_profile(name="张三", age=25, city="南昌")
# name: 张三
# age: 25
# city: 南昌
```

**解包操作符**（和 `*args`/`**kwargs` 是对称的）：

```python
# 把列表/字典拆开传参
def add(a, b, c):
    return a + b + c

nums = [1, 2, 3]
print(add(*nums))           # 6 — 把列表解包成三个参数

info = {"a": 1, "b": 2, "c": 3}
print(add(**info))          # 6 — 把字典解包成关键字参数

# 合并两个字典
d1 = {"name": "张三", "age": 25}
d2 = {"city": "南昌", "age": 26}
merged = {**d1, **d2}       # 后面的覆盖前面的
print(merged)               # {'name': '张三', 'age': 26, 'city': '南昌'}
```

### 6. `enumerate()` 和 `zip()`

```python
# enumerate：遍历时拿索引
names = ["张三", "李四", "王五"]

for i, name in enumerate(names):
    print(f"{i}: {name}")
# 0: 张三
# 1: 李四
# 2: 王五

for i, name in enumerate(names, 1):  # 从1开始编号
    print(f"{i}. {name}")


# zip：同时遍历多个列表
scores = [92, 88, 75]
grades = ["A", "B", "C"]

for name, score, grade in zip(names, scores, grades):
    print(f"{name}: {score}分 ({grade})")
# 张三: 92分 (A)
# 李四: 88分 (B)
# 王五: 75分 (C)

# zip 转字典
result = dict(zip(names, scores))
print(result)   # {'张三': 92, '李四': 88, '王五': 75}
```

### 7. Dict/Set 推导式

```python
# 列表推导式（已会）
squares = [x**2 for x in range(5)]       # [0, 1, 4, 9, 16]

# 字典推导式
square_dict = {x: x**2 for x in range(5)}
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

names = ["张三", "李四", "王五"]
name_length = {name: len(name) for name in names}
# {'张三': 2, '李四': 2, '王五': 2}

# 集合推导式（去重）
nums = [1, 2, 2, 3, 3, 3]
unique_squares = {x**2 for x in nums}
# {1, 4, 9} — 自动去重

# 带过滤
even_dict = {x: x**2 for x in range(10) if x % 2 == 0}
# {0: 0, 2: 4, 4: 16, 6: 36, 8: 64}
```

### 8. `any()` / `all()` / `sorted(key=)`

```python
# any：有一个为 True 就返回 True
scores = [45, 78, 90, 33]
print(any(s >= 60 for s in scores))   # True — 有及格的人

# all：全部为 True 才返回 True
print(all(s >= 60 for s in scores))   # False — 有人不及格

# 实用场景：检查输入
def validate_user(name, age, email):
    fields = [name, age, email]
    return all(fields is not None for f in fields)


# sorted 的 key 参数
students = [
    {"name": "张三", "score": 92},
    {"name": "李四", "score": 88},
    {"name": "王五", "score": 95},
]

# 按分数排序
by_score = sorted(students, key=lambda s: s["score"])
print([s["name"] for s in by_score])   # ['李四', '张三', '王五']

# 按分数降序
by_score_desc = sorted(students, key=lambda s: s["score"], reverse=True)

# 按名字长度
by_name_len = sorted(students, key=lambda s: len(s["name"]))
```

---

## 第三组：避坑专用

### 9. `if __name__ == "__main__":`

每个 Python 文件只要被导入，顶层的代码就会被执行。

```python
# utils.py
print("utils.py 被加载了")   # 这行会在导入时就执行

def greet(name):
    return f"你好, {name}"
```

```python
# main.py
import utils   # 打印 "utils.py 被加载了"
print(utils.greet("张三"))
```

**`if __name__ == "__main__"` 的作用**：只有直接运行这个文件时才执行，被导入时不执行。

```python
# utils.py
def greet(name):
    return f"你好, {name}"

if __name__ == "__main__":
    # 只有 python utils.py 时执行
    # import utils 时不执行
    print(greet("张三"))
```

### 10. 变量作用域（LEGB 规则）

Python 找变量时按这个顺序：

```
L — Local（局部）：当前函数内
E — Enclosing（闭包）：外层函数
G — Global（全局）：模块顶层
B — Built-in（内置）：print, len 等
```

```python
x = "全局"          # Global

def outer():
    x = "外层"      # Enclosing

    def inner():
        x = "局部"  # Local
        print(x)

    inner()

outer()   # 局部


# global：修改全局变量
count = 0
def increment():
    global count    # 声明用全局的 count
    count += 1

increment()
print(count)   # 1

# nonlocal：修改外层函数的变量（闭包里见过）
def outer():
    x = 0
    def inner():
        nonlocal x  # 没有 nonlocal 会报错
        x += 1
        return x
    return inner
```

### 11. `isinstance()` 和类型检查

```python
# isinstance：检查对象是不是某种类型（包含继承关系）
class Animal: pass
class Dog(Animal): pass

d = Dog()
print(isinstance(d, Dog))      # True
print(isinstance(d, Animal))   # True — 因为是子类
print(type(d) is Dog)          # True — type 不检查继承
print(type(d) is Animal)       # False — type 太严格了
```

---

## 第四组：进阶但常用

### 12. 生成器（Generator）和 `yield`

```python
# 普通函数：一次性算出所有结果
def get_squares(n):
    result = []
    for i in range(n):
        result.append(i ** 2)
    return result

# 生成器：边算边给，不占内存
def gen_squares(n):
    for i in range(n):
        yield i ** 2    # yield = 暂停并返回，下次从这继续

# 区别在哪？
squares = get_squares(1000000)   # 直接占 8MB 内存
gen = gen_squares(1000000)       # 几乎不占内存

# 生成器只能用一次，用 for 遍历
for s in gen_squares(5):
    print(s)   # 0, 1, 4, 9, 16

# 也可以转成列表（但失去省内存的优势）
list(gen_squares(5))   # [0, 1, 4, 9, 16]
```

### 13. 海象运算符 `:=`（Walrus Operator）

Python 3.8+，在表达式里赋值：

```python
# 不用海象
data = input("输入: ")
if len(data) > 0:
    print(f"你输入了: {data}")

# 用海象
if (data := input("输入: ")) and len(data) > 0:
    print(f"你输入了: {data}")

# 更实用的场景：while 循环
# 不用海象
while True:
    line = input("> ")
    if line == "quit":
        break
    print(line.upper())

# 用海象
while (line := input("> ")) != "quit":
    print(line.upper())
```

### 14. 列表/字符串反转和复制

```python
# 反转
nums = [1, 2, 3, 4, 5]
print(nums[::-1])      # [5, 4, 3, 2, 1]
print(list(reversed(nums)))  # [5, 4, 3, 2, 1]

# 复制（浅拷贝）
original = [1, 2, 3]
copy1 = original.copy()       # ✅ 明确
copy2 = original[:]           # ✅ 切片复制
copy3 = list(original)        # ✅ 也行
```

---

## 优先级总结

| 优先级 | 内容 | 预计掌握 |
|--------|------|---------|
| P0 今天就要知道 | None/真值、is vs ==、三元表达式 | 5min |
| P0 今天就要知道 | mutable vs immutable、默认参数陷阱 | 3min |
| P0 今天就要知道 | `*args`/`**kwargs`、`enumerate`/`zip` | 5min |
| P0 今天就要知道 | `if __name__ == "__main__"` | 2min |
| P1 遇到时查 | Dict/Set 推导式、`any`/`all`/`sorted(key=)` | 3min |
| P1 遇到时查 | LEGB 作用域、`isinstance` | 3min |
| P2 苍穹外卖阶段再碰 | `yield` 生成器、海象运算符、自定义上下文管理器 | 用到时 |
