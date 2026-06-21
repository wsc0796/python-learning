---
aliases:
  - 20-operators
---
# 运算符完整体系

> 前置：已掌握基本语法
> 用时：约 8 分钟
>
> 相关笔记：[类型转换](../19-type-conversion/theory_19_type_conversion.md) · [条件语句](../23-if-conditionals/theory_23_if_conditionals.md)

---

## 一、算术运算符

```python
a, b = 10, 3
print(a + b)   # 13  加
print(a - b)   # 7   减
print(a * b)   # 30  乘
print(a / b)   # 3.333...  除（结果是 float）
print(a // b)  # 3   整除（取整）
print(a % b)   # 1   取余（模）
print(a ** b)  # 1000 幂运算
```

## 二、赋值运算符

```python
x = 10
x += 5    # x = x + 5 → 15
x -= 3    # x = x - 3 → 12
x *= 2    # x = x * 2 → 24
x /= 4    # x = x / 4 → 6.0
x //= 2   # x = x // 2 → 3.0
x %= 2    # x = x % 2 → 1.0
```

## 三、比较运算符

```python
print(5 == 5)   # True  等于
print(5 != 3)   # True  不等于
print(5 > 3)    # True  大于
print(5 < 3)    # False 小于
print(5 >= 5)   # True  大于等于
print(5 <= 3)   # False 小于等于

# 链式比较（Python 特色！）
age = 25
print(18 <= age <= 60)   # True  — Java 要写成 18 <= age && age <= 60
```

## 四、逻辑运算符

```python
a, b = True, False
print(a and b)   # False  与（两者都真才真）
print(a or b)    # True   或（一个真就真）
print(not a)     # False  非（取反）

# 短路求值
print(0 and 1/0)  # 0 — and 左边假就不算右边了，所以不会报错
print(1 or 1/0)   # 1 — or 左边真就不算右边了

# 非布尔值的逻辑运算（返回的是值本身）
print("" or "默认值")    # "默认值"  — "" 是假，返回右边的
print("你好" and "继续") # "继续"   — "你好" 是真，返回右边的
```

## 五、成员运算符

```python
lst = [1, 2, 3]
print(1 in lst)      # True
print(4 in lst)      # False
print(4 not in lst)  # True

# 字符串
print("he" in "hello")  # True
```

## 六、身份运算符

```python
a = [1, 2, 3]
b = [1, 2, 3]
c = a
print(a is c)     # True  同一个对象
print(a is b)     # False 不同对象（内容相同但身份不同）
print(a is None)  # False 判断 None 的标准写法

# is vs ==：is 比身份，== 比值
```

## 七、位运算符

```python
# 了解即可，做算法题时偶尔用
a, b = 5, 3     # 5=0101, 3=0011
print(a & b)    # 1  按位与    0101 & 0011 = 0001
print(a | b)    # 7  按位或    0101 | 0011 = 0111
print(a ^ b)    # 6  按位异或  0101 ^ 0011 = 0110
print(~a)       # -6 按位取反  ~0101 = 1010
print(a << 1)   # 10 左移1位  0101 → 1010
print(a >> 1)   # 2  右移1位  0101 → 0010
```

## 八、运算符优先级（从高到低）

| 优先级 | 运算符 |
|--------|--------|
| 1 | `**` 幂运算 |
| 2 | `~` `+x` `-x` 位非/正/负 |
| 3 | `*` `/` `//` `%` 乘除取余 |
| 4 | `+` `-` 加减 |
| 5 | `<<` `>>` 移位 |
| 6 | `&` 按位与 |
| 7 | `^` 按位异或 |
| 8 | `\|` 按位或 |
| 9 | `==` `!=` `>` `<` `>=` `<=` 比较 |
| 10 | `not` 逻辑非 |
| 11 | `and` 逻辑与 |
| 12 | `or` 逻辑或 |

**记不住就用括号**：
```python
# 不清晰
if a + b > c and d == e:

# 清晰
if (a + b) > c and (d == e):
```

## 备考相关

- [[EXAM_PREP/day01/00_今日任务]] — Day 1 基础语法与流程控制
