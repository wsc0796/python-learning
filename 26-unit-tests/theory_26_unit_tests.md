---
aliases:
  - 26-unit-tests
---
# 单元测试：assert + pytest

> 前置：函数基础、异常处理
> 目标：能用代码验证自己代码的正确性
> 用时：约 15 分钟
>
> 相关笔记：[异常处理](../03-file-exception/theory_03_file_exception.md) · [模块与类型提示](../05-module-types/theory_05_module_types.md)

---

## 为什么要写测试

你的苍穹外卖项目里，改了一个 Service 方法，怎么确认没搞坏其他功能？一个个手动点？**测试就是"用代码验证代码"**。

CS50P 里的原话：*"You want to make sure that yesterday's code is still correct after today's changes."*

测试不只是"找 bug"——它让你**敢重构**。没有测试的代码就像一个没扶手的楼梯，能用，但走快了会摔。

---

## 一、`assert` — Python 内置的最小测试单元

```python
# 最简单的断言
assert 1 + 1 == 2          # 通过，什么都不发生
assert 1 + 1 == 3          # AssertionError！

# 带错误信息
assert 2 * 3 == 5, "乘法计算错误"  # AssertionError: 乘法计算错误
```

`assert` 的工作方式：**条件为 True → 静默通过；条件为 False → 抛 AssertionError**。

### 用 assert 测试函数

```python
def square(n):
    return n * n

# 一组测试
assert square(2) == 4
assert square(3) == 9
assert square(0) == 0
assert square(-2) == 4, "负数平方应该为正"
print("所有测试通过！")
```

不够——一个 assert 失败，后面的不跑了。

---

## 二、`pytest` — 工业标准测试框架

```bash
pip install pytest
```

**基本语法**：测试函数必须以 `test_` 开头

```python
# test_calculator.py
from calculator import square

def test_positive():
    assert square(2) == 4
    assert square(3) == 9

def test_negative():
    assert square(-2) == 4
    assert square(-3) == 9

def test_zero():
    assert square(0) == 0
```

运行：`pytest test_calculator.py`

pytest 会**运行所有 `test_` 函数**，每个函数是独立的测试用例。一个失败了，不影响其他。

### 测试异常 — `pytest.raises`

```python
import pytest

def sqrt(n):
    if n < 0:
        raise ValueError("不能对负数开平方")
    return n ** 0.5

def test_negative_input():
    with pytest.raises(ValueError):
        sqrt(-4)    # 期望这里抛出 ValueError
```

`pytest.raises` 检查代码是否抛出了指定类型的异常——**抛出 = 测试通过**。

### 测试组织（推荐结构）

```
project/
├── calculator.py          ← 源码
├── test/
│   ├── __init__.py        ← 空文件，让 test/ 成为 package
│   └── test_calculator.py ← 测试代码
```

然后运行：`pytest test/`

---

## 三、测试什么？— 核心原则

| 场景 | 示例 | 为什么 |
|------|------|--------|
| **正常输入** | `square(5) == 25` | 最基本的功能正确 |
| **边界值** | `square(0) == 0`, `square(1) == 1` | 边界最容易出 bug |
| **异常输入** | `sqrt(-1)` 应抛异常 | 代码要能处理非法情况 |
| **空值/None** | 传入 None 的行为 | Python 最常见运行时错误来源 |

---

## 四、测试的好处（不只是"找bug"）

1. **回归保护**：改代码后跑一遍 `pytest`，马上知道有没有搞坏旧功能
2. **活的文档**：测试代码本身就是最好的"这个函数怎么用"的说明
3. **降低心理负担**：有测试 → 敢重构 → 代码越来越好。没测试 → 不敢改 → 代码越来越差

---

## 与Java的对比

| 概念 | Java (JUnit) | Python (pytest) |
|------|-------------|-----------------|
| 断言 | `assertEquals(expected, actual)` | `assert actual == expected` |
| 测试方法 | `@Test` 注解 + `testXxx()` | `test_xxx()` 函数 |
| 异常测试 | `@Test(expected = Exception.class)` | `pytest.raises(Exception)` |
| 运行 | `mvn test` / IDE | `pytest` |
| Mock | Mockito | `unittest.mock` / `pytest-mock` |

**关键区别**：Java 的 `assertEquals` 需要静态导入 + 记得预期值写左边。Python 的 `assert` 是语言内置关键字，任何地方都能用。

---

## 补充练习建议

用你苍穹外卖项目里的一个 Service 方法来练：
1. 找一个纯计算/纯逻辑的方法（比如金额计算、状态判断）
2. 写 3-5 个 `test_xxx()` 函数
3. 跑 `pytest` 看结果
4. 故意把源码改错，看测试能不能抓到
