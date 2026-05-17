---
aliases:
  - 23-if-conditionals
---
# 条件语句：if / elif / else

> 前置：已掌握变量和基本数据类型
> 目标：能写任意复杂的条件分支
> 用时：约 10 分钟
>
> 相关笔记：[循环深入](../18-loops-deep/theory_18_loops_deep.md) · [运算符完整体系](../20-operators/theory_20_operators.md)

---

## 一、单分支：if

```python
age = 18

if age >= 18:
    print("已成年，可以进入")
```

**结构**：
```
if 条件:
    条件为真时执行的代码
```

- 条件后面有 **冒号 `:`**
- 条件为 True 才执行缩进块
- Python 用**缩进**表示代码块（而不是 Java 的 `{}`）

## 二、双分支：if / else

```python
age = 16

if age >= 18:
    print("已成年")
else:
    print("未成年")
```

**记忆**：`if ... else ...` = "如果...否则..."

## 三、多分支：if / elif / else

```python
score = 85

if score >= 90:
    grade = "优秀"
elif score >= 80:
    grade = "良好"
elif score >= 70:
    grade = "中等"
elif score >= 60:
    grade = "及格"
else:
    grade = "不及格"

print(f"成绩等级：{grade}")   # 良好
```

**注意**：
- `elif` = `else if` 的缩写
- 从上往下判断，碰到第一个 True 就执行，后面的跳过
- `else` 可以省略
- 不要写成 `else if`（Java 写法），Python 里是 `elif`

## 四、嵌套 if

```python
age = 20
has_id = True

if age >= 18:
    if has_id:
        print("可以进入")
    else:
        print("请出示身份证")
else:
    print("未成年禁止进入")
```

**原则**：嵌套不要超过 2 层，超过就用 `and` 合并：

```python
# 上面的嵌套等价于：
if age >= 18 and has_id:
    print("可以进入")
elif age >= 18 and not has_id:
    print("请出示身份证")
else:
    print("未成年禁止进入")
```

## 五、条件表达式（三元运算符）

```python
# Java:  String status = age >= 18 ? "成年" : "未成年"
# Python: value_if_true if condition else value_if_false

age = 20
status = "成年" if age >= 18 else "未成年"
print(status)   # 成年
```

**什么时候用**：简单的二选一赋值。复杂逻辑还是用普通 if。

## 六、真值判断（Truthiness）

```python
# 以下值在 if 判断中相当于 False：
#   None, 0, 0.0, ""（空字符串）, []（空列表）, {}（空字典）, set()

name = ""
if name:           # name 是空字符串 → False
    print("有名字")
else:
    print("名字为空")   # 走这里

items = [1, 2, 3]
if items:          # 非空列表 → True
    print(f"有 {len(items)} 项")  # 走这里
```

**实用写法**：
```
检查空列表:  if not items:
检查 None:   if x is None:
检查非空:    if items:
```

## 七、常见坑

```python
# 坑1：忘写冒号
if age >= 18    # ← SyntaxError，忘记冒号

# 坑2：条件里用 = 而不是 ==
if age = 18:    # ← SyntaxError，= 是赋值，== 才是比较

# 坑3：Java 习惯写 else if
if age >= 18:
    pass
else if age < 18:   # ← SyntaxError，Python 里是 elif
    pass
```

## 总结

| 结构 | 语法 | 场景 |
|------|------|------|
| 单分支 | `if 条件:` | 只需要一种情况 |
| 双分支 | `if ... else ...` | 二选一 |
| 多分支 | `if ... elif ... else ...` | 多选一 |
| 嵌套 | `if 里套 if` | 需要先判断大前提 |
| 三元 | `x if 条件 else y` | 简单的二选一赋值 |
