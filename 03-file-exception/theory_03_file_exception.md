---
aliases:
  - 03-file-exception
---
# Day 3：文件读写 + 异常处理

读完约 8 分钟。

> 相关笔记：[os 模块/深浅拷贝](../22-copy-os/theory_22_copy_os.md) · [模块与类型提示](../05-module-types/theory_05_module_types.md)

---

## 一、文件读写：`with open`

### Java 对照

```java
// Java：try-with-resources，自动关闭
try (BufferedReader br = new BufferedReader(new FileReader("data.txt"))) {
    String line = br.readLine();
}
```

```python
# Python：with open，自动关闭
with open("data.txt", "r", encoding="utf-8") as f:
    line = f.readline()
```

**`with` 的作用 = Java 的 try-with-resources**：代码块结束后自动关闭文件，不用手动 f.close()。

### 模式参数

| 模式 | 含义 | 文件不存在时 |
|------|------|------------|
| `"r"` | 读 | 报错 |
| `"w"` | 写（覆盖） | 创建新文件 |
| `"a"` | 追加（不覆盖） | 创建新文件 |

### 三种读法

```python
with open("data.txt", "r", encoding="utf-8") as f:
    text = f.read()        # 一次性全读进来，返回一个字符串

with open("data.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()  # 全读进来，返回列表，一行一个元素

with open("data.txt", "r", encoding="utf-8") as f:
    for line in f:         # 逐行读，内存友好（文件大时用这个）
        print(line)
```

**选择规则：** 文件小（<几MB）用 `read()`，文件大用 `for line in f`。

### 写文件

```python
with open("output.txt", "w", encoding="utf-8") as f:
    f.write("第一行\n")
    f.write("第二行\n")
```

**`"w"` 是覆盖写。** 如果文件已存在，旧内容全部清空。不想清空用 `"a"` 追加。

### 不写 `encoding="utf-8"` 的下场

Windows 上默认编码可能是 GBK，中文会乱码。**永远写 `encoding="utf-8"`**。

---

## 二、异常处理：`try/except`

### 为什么需要

```python
# 用户输入一个非数字 → 程序崩溃
age = int(input("输入年龄："))
print(f"明年你 {age + 1} 岁")
```

用户输 `abc` → `ValueError`，程序直接炸。用 `try/except` 兜住：

```python
try:
    age = int(input("输入年龄："))
    print(f"明年你 {age + 1} 岁")
except ValueError:
    print("请输入数字！")
```

**执行流程：** `try` 块没报错 → 跳过 `except`。`try` 块报错 → 跳到对应的 `except`。

### Java 对照

```python
# Python
try:
    x = 1 / 0
except ZeroDivisionError:
    print("不能除零")
```

```java
// Java
try {
    int x = 1 / 0;
} catch (ArithmeticException e) {
    System.out.println("不能除零");
}
```

**同一个模式，语法不同。** Python 用 `except`，Java 用 `catch`。

### 捕获多种异常

```python
try:
    num = int(input("输入数字："))
    result = 100 / num
except ValueError:
    print("请输入数字")
except ZeroDivisionError:
    print("不能输入0")
```

### 常见异常类型

| 异常 | 触发条件 |
|------|---------|
| `ValueError` | 类型转换失败 |
| `ZeroDivisionError` | 除以0 |
| `FileNotFoundError` | 文件不存在 |
| `TypeError` | 类型不对（比如 "a" + 3） |
| `IndexError` | 列表索引越界 |
| `KeyError` | 字典键不存在 |

### 文件和异常处理的组合（实战最常见写法）

```python
try:
    with open("data.txt", "r", encoding="utf-8") as f:
        content = f.read()
except FileNotFoundError:
    print("文件不存在，检查路径")
```

---

## 三、try/except/else/finally：完整异常结构

### else：只有没抛异常时才执行

```python
try:
    x = int(input("What's x? "))
except ValueError:
    print("x is not an integer")
else:
    # 只有 try 成功（没抛异常）才执行
    print(f"x is {x}")
```

**为什么不用直接写在 try 里面？**

```python
# ❌ 不推荐：写在 try 里
try:
    x = int(input("What's x? "))
    print(f"x is {x}")      # 这行也可能报错，一报错就被 except 捕获
except ValueError:
    print("x is not an integer")

# ✅ 推荐：try 只放可能抛异常的代码，成功后放 else
try:
    x = int(input("What's x? "))
except ValueError:
    print("x is not an integer")
else:
    print(f"x is {x}")      # 这里即使报错，也不会被上面的 except ValueError 误吞
```

**`else` 的核心作用**：让 `try` 块只包含**你知道可能抛异常**的代码，正常执行的代码放 `else` 里——避免意外捕获不该捕获的异常。

### finally：不管有没有异常都执行

```python
try:
    f = open("data.txt", "r", encoding="utf-8")
    data = f.read()
except FileNotFoundError:
    print("文件不存在")
finally:
    # 不管 try 成功还是 except 执行了，这里都跑
    print("这段永远执行")
    f.close()  # 关闭文件——finally 最适合做清理工作
```

**`finally` 的应用场景**：释放资源、关闭文件、关闭数据库连接——这些"不管成功失败都要做的事"。

### 四种结构的时间线

```
try 没抛异常时：
   try → else → finally

try 抛异常时：
   try → except → finally
```

```python
def divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("不能除零")
        return None      # ← 即使这里有 return，finally 仍然执行
    else:
        print("除法成功")
        return result
    finally:
        print("finally 永远执行")  # ← return 之前先跑 finally

print(divide(10, 2))  # 除法成功 → finally → 5.0
print(divide(10, 0))  # 不能除零 → finally → None
```

**`finally` 比 `return` 还强**——即使 `except` 里有 `return`，`finally` 也会在返回之前执行。

### 一句话记

> `else` = 没抛异常时做；`finally` = 不管抛没抛都做。

---

## 当前级别许可

| 内容 | 状态 |
|------|------|
| 文件读写 + with open | ✅ 今天可以学（Block 4 或晚间） |
| try/except 异常处理 | ✅ 今天可以学（和文件读写一起） |
| 装饰器 | ❌ 推迟到 Day5 之后 |
| 生成器 yield | ❌ 推迟到 Day5 之后 |

装饰器和生成器是 Python 进阶内容，在你站稳第3层（能讲清楚流程）之前不碰。
