---
aliases:
  - 01-context-manager
---
# 01. 上下文管理器：with 的底层原理

> 前置：会用 `with open()`、理解装饰器基本概念
> 目标：手写 `__enter__`/`__exit__`，用 `@contextmanager` 写上下文管理器
> 用时：约 15 分钟
>
> 相关笔记：[[03-file-exception]] · [[11-closure-decorator]] · [[02-iterator-generator]]

---

## 一、为什么需要上下文管理器

### 问题：资源需要成对操作

```python
# 打开 → 必须关闭
f = open("data.txt", "r")
content = f.read()
f.close()   # 忘了这行 = 资源泄漏

# 获取锁 → 必须释放
lock.acquire()
# ... 临界区 ...
lock.release()   # 抛出异常这行就跳过了

# 修改配置 → 必须恢复
old_value = settings.DEBUG
settings.DEBUG = True
# ... 临时调试 ...
settings.DEBUG = old_value   # 中间报错就回不来了
```

**核心矛盾**：进入和退出必须配对，但中间可能发生任何事（异常、return、break）。

### 解决方案：`try...finally`

```python
f = open("data.txt", "r")
try:
    content = f.read()
finally:
    f.close()   # 不管是否异常，都会执行
```

`with` 语句是 `try...finally` 的语法糖——更简洁、更难写错。

---

## 二、`with` 的底层执行流程

```python
with EXPR as VAR:
    BLOCK
```

Python 解释器实际执行的逻辑：

```python
manager = EXPR                        # 1. 计算 with 后面的表达式
enter = type(manager).__enter__       # 2. 找到 __enter__ 方法
exit  = type(manager).__exit__        # 3. 找到 __exit__ 方法
VAR = enter(manager)                  # 4. 调用 __enter__，返回值给 as
try:
    BLOCK                             # 5. 执行你的代码块
except Exception as e:
    if not exit(manager, type(e), e, e.__traceback__):
        raise                         # 6. 异常 → 调 __exit__，返回 False 则继续抛
else:
    exit(manager, None, None, None)   # 7. 正常 → 调 __exit__，三个参数都是 None
```

**一句话**：`with` = 帮你自动在进入时调 `__enter__`，退出时调 `__exit__`（不管怎么退出的）。

---

## 三、类版上下文管理器

### 最小示例

```python
class MyContext:
    def __enter__(self):
        print("→ 进入 with")
        return self          # 这个返回值给 as 后面的变量

    def __exit__(self, exc_type, exc_value, traceback):
        print("← 退出 with")

with MyContext() as ctx:
    print("  执行代码块")
    print(f"  ctx 是: {ctx}")

# 输出：
# → 进入 with
#   执行代码块
#   ctx 是: <__main__.MyContext object at ...>
# ← 退出 with
```

### `__exit__` 的三个参数

| 参数 | 含义 | 无异常时的值 |
|------|------|------------|
| `exc_type` | 异常类型 | `None` |
| `exc_value` | 异常对象 | `None` |
| `traceback` | 异常追踪信息 | `None` |

### 异常处理实验

```python
class SpyContext:
    def __enter__(self):
        print("enter")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print(f"exit: exc_type={exc_type}, exc_value={exc_value}")
        return False    # False = 不吞异常，继续往上抛

with SpyContext():
    1 / 0    # 故意制造 ZeroDivisionError

# 输出：
# enter
# exit: exc_type=<class 'ZeroDivisionError'>, exc_value=division by zero
# ZeroDivisionError: division by zero   ← 异常继续抛出
```

**`__exit__` 返回值规则**：

| 返回值 | 行为 |
|--------|------|
| `False` / `None` | 不吞异常，异常继续向上传播 |
| `True` | 吞掉异常，外部代码不感知 |

**一般不要返回 `True`**——除非你明确知道这个异常可以被安全忽略。

### 实战：文件自动关闭器

```python
class MyOpen:
    def __init__(self, filename, mode="r", encoding="utf-8"):
        self.filename = filename
        self.mode = mode
        self.encoding = encoding
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, self.mode, encoding=self.encoding)
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        if self.file:
            self.file.close()
        # 不返回 True，让异常正常传播

with MyOpen("test.txt", "w") as f:
    f.write("Hello")
# f 已自动关闭
```

---

## 四、`@contextmanager` — 函数版上下文管理器

**这是装饰器在标准库中的实际应用**。你刚学完装饰器，这是最直接的"装饰器能干什么"的例子。

```python
from contextlib import contextmanager

@contextmanager
def my_context():
    print("→ 进入")
    yield "返回值给 as"
    print("← 退出")

with my_context() as val:
    print(f"  执行: {val}")

# 输出：
# → 进入
#   执行: 返回值给 as
# ← 退出
```

**结构对照**：

| 位置 | 对应 | 说明 |
|------|------|------|
| `yield` 之前的代码 | `__enter__` | 进入逻辑 |
| `yield` 的值 | `as` 接收的值 | 传给调用者 |
| `yield` 之后的代码 | `__exit__` | 退出逻辑（清理） |

### `yield` 后必须用 `try...finally`

```python
@contextmanager
def safe_context():
    # __enter__ 逻辑
    resource = acquire_resource()
    try:
        yield resource       # 交给 with 代码块
    finally:
        resource.release()   # 不管是否异常，一定执行
```

**为什么**：`yield` 之后的代码，如果 `with` 块里抛了异常，`finally` 保证清理逻辑一定执行。

### 实战：计时器

```python
import time
from contextlib import contextmanager

@contextmanager
def timer(name="任务"):
    start = time.time()
    try:
        yield
    finally:
        elapsed = time.time() - start
        print(f"{name} 耗时: {elapsed:.2f}s")

with timer("数据处理"):
    time.sleep(1.5)
# 输出: 数据处理 耗时: 1.50s
```

### 实战：临时切换工作目录

```python
import os
from contextlib import contextmanager

@contextmanager
def chdir(path):
    old = os.getcwd()
    os.chdir(path)
    try:
        yield
    finally:
        os.chdir(old)   # 一定会切回来

# 使用
with chdir("/tmp"):
    print(os.getcwd())  # /tmp
# 退出 with 后自动回到原目录
```

---

## 五、`@contextmanager` 和装饰器的关系

```python
@contextmanager
def demo():
    yield
```

等价于：

```python
def demo():
    yield
demo = contextmanager(demo)
```

`contextmanager` 就是一个**接收生成器函数、返回上下文管理器对象的装饰器**。

这和你刚学的 `@log_calls` 完全一样的模式：
- `log_calls(func)` → 返回 wrapper 函数
- `contextmanager(gen_func)` → 返回 _GeneratorContextManager 对象

---

## 六、实际应用场景总结

| 场景 | 典型代码 | 你会在哪遇到 |
|------|---------|------------|
| 文件操作 | `with open(...) as f:` | 天天用 |
| 数据库连接 | `with get_db() as db:` | FastAPI 项目 |
| 锁管理 | `with threading.Lock():` | 多线程 |
| 计时 | `with timer("task"):` | 性能调试 |
| 临时环境 | `with chdir("/tmp"):` | 脚本工具 |
| HTTP Session | `with requests.Session() as s:` | 网络请求 |

---

## 七、常见易错点

| 易错点 | 后果 | 怎么避免 |
|--------|------|---------|
| `__enter__` 忘记 `return` | `as` 的变量是 `None` | 确保有 `return self` 或 `return resource` |
| `__exit__` 随便返回 `True` | 异常被静默吞掉 | 默认返回 `None`（不吞异常） |
| `@contextmanager` 中 `yield` 不在 `try` 里 | 异常时清理代码不执行 | 养成 `try: yield` + `finally: cleanup` 的习惯 |
| 在 `__exit__` 中再次抛异常 | 覆盖原始异常，调试困难 | `__exit__` 只做清理，不抛异常 |
