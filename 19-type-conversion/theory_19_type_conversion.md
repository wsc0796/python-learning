---
aliases:
  - 19-type-conversion
---
# 类型转换 + 输入输出格式化

> 前置：已掌握基本数据类型
> 用时：约 8 分钟
>
> 相关笔记：[运算符完整体系](../20-operators/theory_20_operators.md) · [f-string 格式化](../01-fstring/theory_01_fstring.md)

---

## 一、类型转换

```python
# 显式转换
int("123")       # 123
float("3.14")    # 3.14
str(123)         # "123"
bool(1)          # True
bool(0)          # False
list("hello")    # ['h', 'e', 'l', 'l', 'o']
tuple([1, 2, 3]) # (1, 2, 3)
set([1, 2, 2])   # {1, 2}

# 容易踩坑
int("3.14")      # ❌ ValueError — 不能直接转带小数点的
float("3.14")    # ✅ 3.14
int(3.14)        # ✅ 3 — 截断取整，不是四舍五入
int("  123  ")   # ✅ 123 — 自动去空白
```

## 二、三种字符串格式化

```python
name = "张三"
age = 20

# 1. % 格式化（旧的，了解即可）
print("我叫%s，今年%d岁" % (name, age))

# 2. format()（中间代）
print("我叫{}，今年{}岁".format(name, age))

# 3. f-string（现代，主力！）
print(f"我叫{name}，今年{age}岁")   # 推荐
```

## 三、转义符

```python
print("他说：\"你好\"")    # 他说："你好"  — \" 转义双引号
print("第一行\n第二行")    # 换行
print("Tab\t分隔")         # Tab 缩进
print("反斜杠：\\")        # 反斜杠本身

# 原样输出（不转义）
print(r"第一行\n第二行")   # 第一行\n第二行 — 加 r 就不转义了
```

## 四、print 的完整用法

```python
# end 参数：控制结尾（默认 \n）
print("hello", end="")
print("world")           # helloworld

# sep 参数：控制分隔符（默认空格）
print(1, 2, 3)           # 1 2 3
print(1, 2, 3, sep="-")  # 1-2-3
```

## 备考相关

- [[EXAM_PREP/day01/00_今日任务]] — Day 1 基础语法与流程控制
