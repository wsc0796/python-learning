---
aliases:
  - 16-cs50p-supplement
---
# Day 16 补充：`argparse`、`mypy`、生成器/yield

> 来源：CS50P Lecture 5 + Lecture 10 (Et Cetera)
> 补充你原笔记中标记为 P2 或缺失的知识点

---

## 补充一：`argparse` — 专业的命令行参数解析

`sys.argv` 够简单场景用，但参数多了就需要 `argparse`。CS50P 最后一讲专门讲了它。

```python
import argparse

parser = argparse.ArgumentParser(description="问候程序")
parser.add_argument("-n", "--name", default="World", help="要问候的名字")
args = parser.parse_args()

print(f"Hello, {args.name}")
```

运行效果：
```bash
$ python greet.py -n David
Hello, David

$ python greet.py --help
usage: greet.py [-h] [-n NAME]
问候程序
options:
  -h, --help        show this help message and exit
  -n NAME, --name NAME  要问候的名字
```

### 为什么用 argparse 而不是 sys.argv

| 场景 | `sys.argv` | `argparse` |
|------|-----------|------------|
| 自动 `--help` | ❌ 手写 | ✅ 自动生成 |
| 类型验证 | ❌ 手写 `int()` | ✅ `type=int` |
| 可选参数 | 手写逻辑 | ✅ `--flag` 自动 |
| 错误提示 | ❌ 手写 | ✅ 自动提示用法 |

```python
# argparse 自动做类型转换和验证
parser.add_argument("-c", "--count", type=int, default=1)
# 用户传 "-c abc" 会自动报错
```

---

## 补充二：`mypy` — 类型检查工具

你原笔记学了类型提示语法（`name: str`），但没提运行 `mypy` 做实际检查。

```bash
pip install mypy
```

```python
# example.py
def greet(name: str) -> str:
    return "Hello, " + name

greet(42)   # 类型错误：传了 int 而不是 str
```

```bash
$ mypy example.py
example.py:4: error: Argument 1 to "greet" has incompatible type "int"; expected "str"
Found 1 error in 1 file
```

**类型提示 + mypy = Python 的类型安全方案**。注意：mypy 只检查，不改变运行时行为。

---

## 补充三：生成器与 `yield` — 从 P2 升到 P1

你原笔记 `16-python-gaps` 把 yield 标记为 P2 "稍后用"。CS50P 把它作为核心概念来讲。

### 返回 vs 生成

```python
# 普通函数：一次性返回全部
def get_squares(n):
    result = []
    for i in range(n):
        result.append(i ** 2)
    return result  # 全部算完才返回

# 生成器：逐个产出
def gen_squares(n):
    for i in range(n):
        yield i ** 2   # 返回一个，暂停，等下次调用再继续

# 使用
squares = gen_squares(1000000)  # 没算！只是创建了生成器
print(next(squares))  # 0 — 只算第一个
print(next(squares))  # 1 — 只算第二个

for sq in gen_squares(5):   # 也可以直接遍历
    print(sq)
```

### 什么时候用 yield

- **处理大数据**：文件太大不能一次读入内存？`yield` 逐行产出
- **无限序列**：`yield` 可以表示无限数列（比如斐波那契），list 不行
- **管道处理**：生成器可以串联：`filter(map(source))`

```python
# yield 用于大文件逐行处理
def read_large_file(file_path):
    with open(file_path, "r") as f:
        for line in f:
            yield line.strip()   # 一次只产出一行

for line in read_large_file("huge_file.csv"):
    process(line)   # 内存里永远只有一行
```

---

## 与Java的对比

| 概念 | Java | Python |
|------|------|--------|
| 命令行解析 | 无内置，需 Apache Commons CLI | `argparse` |
| 类型检查 | 编译器强制检查 | `mypy`（可选工具） |
| 生成器/惰性求值 | Java 无原生 yield（需用 Iterator 模拟） | `yield` 关键字 |
| 流式处理 | Stream API (Java 8+) | 生成器 + 推导式 |
