# zip() 与推导式 笔记

---

## 一、zip()：把多个列表"拉链"在一起

```python
names = ["张三", "李四", "王五"]
scores = [92, 88, 75]
```

`zip(names, scores)` 做的事情：
```
[("张三", 92), ("李四", 88), ("王五", 75)]
```
把每个列表的第 1 个元素拼成元组，第 2 个拼成元组……以此类推。

**等价的不使用 zip 的写法：**
```python
for i in range(len(names)):
    name = names[i]
    score = scores[i]
```

**用 zip 的写法：**
```python
for name, score in zip(names, scores):
    print(f"{name}: {score}")
```

**zip 转字典：**
```python
result = dict(zip(names, scores))
# {'张三': 92, '李四': 88, '王五': 75}
```
`zip` 先配对成 `(键,值)` 元组列表，`dict()` 直接认。

**坑：** zip 以最短的列表为准，长的被静默丢弃。

---

## 二、推导式本质：把 for 循环压缩成一行

### 列表推导式
```python
# 普通循环
squares = []
for x in range(5):
    squares.append(x**2)

# 推导式
squares = [x**2 for x in range(5)]
```
公式：`[要放进去的东西 for 变量 in 范围]`

### 字典推导式（有冒号 :）
```python
# 普通循环
square_dict = {}
for x in range(5):
    square_dict[x] = x**2

# 推导式
square_dict = {x: x**2 for x in range(5)}
```
公式：`{键:值 for 变量 in 范围}`

### 集合推导式（无冒号，自动去重）
```python
nums = [1, 2, 2, 3, 3, 3]
unique = {x**2 for x in nums}  # {1, 4, 9}
```
公式：`{值 for 变量 in 范围}`

### 带过滤条件
```python
even_dict = {x: x**2 for x in range(10) if x % 2 == 0}
# {0: 0, 2: 4, 4: 16, 6: 36, 8: 64}
```

### 区分口诀
- 有冒号 `:` → 字典推导式
- 没冒号 → 集合推导式
- 方括号 `[]` → 列表推导式

---

## 三、zip + 推导式组合
```python
names = ["张三", "李四", "王五"]
scores = [92, 88, 75]

# zip 配对后用字典推导式
result = {name: score for name, score in zip(names, scores)}
# {'张三': 92, '李四': 88, '王五': 75}
```

等价于：
```python
result = {}
for name, score in zip(names, scores):
    result[name] = score
```
