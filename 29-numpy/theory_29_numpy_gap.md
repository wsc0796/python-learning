---
aliases:
  - 29-numpy-gap
---
# 29 - NumPy 补缺：axis / 广播 / where / 分位数

> 这 4 个知识点在 `29-numpy` 主笔记里没有覆盖，但在 pandas 和验收项目中会用到。
> 前置：已理解 `np.array`、向量化计算、布尔筛选。

---

## 一句话

`axis` 决定"沿着哪个方向压缩"，`np.where` 是数组版的 if-else，`np.percentile` 看数据分布，广播让你不用写循环也能让不同形状的数组一起算。

---

## 1. axis：沿轴计算

`axis` 是 NumPy 里最容易卡住的概念。先记住一句话：

```text
axis=0 → 纵向压缩 → 得到每一列的结果
axis=1 → 横向压缩 → 得到每一行的结果
```

```python
import numpy as np

scores = np.array([
    [80, 90, 70],   # 学生A：三科成绩
    [60, 75, 85],   # 学生B
    [95, 88, 92],   # 学生C
])

print(scores.shape)          # (3, 3) → 3行3列

print(scores.mean())         # 81.7  → 所有9个数据的平均值
print(scores.mean(axis=0))   # [78.3 84.3 82.3] → 每列（每科）的平均分
print(scores.mean(axis=1))   # [80.  73.3 91.7] → 每行（每人）的平均分
```

直观理解：

```text
原始 (3, 3)

axis=0 压缩：把 3 行压成 1 行 → 结果 shape (3,) → 每列的统计
axis=1 压缩：把 3 列压成 1 列 → 结果 shape (3,) → 每行的统计
```

| 代码 | 含义 | 结果 shape |
|---|---|---|
| `arr.sum()` | 全部求和 | 标量 |
| `arr.sum(axis=0)` | 每列求和 | `(列数,)` |
| `arr.sum(axis=1)` | 每行求和 | `(行数,)` |

**axis 和 pandas groupby 的关系**：pandas 的 `groupby` 本质上也是"沿某个轴分组后聚合"，理解 axis 后 groupby 就不是死记硬背。

---

## 2. np.where：数组版 if-else

```python
latency = np.array([120, 350, 80, 500, 200])

# 语法：np.where(条件, 满足时的值, 不满足时的值)
level = np.where(latency >= 300, "slow", "normal")
print(level)  # ['normal' 'slow' 'normal' 'slow' 'normal']
```

对比 Python 原生写法：

```python
# 不推荐：写循环
level = []
for v in latency:
    if v >= 300:
        level.append("slow")
    else:
        level.append("normal")

# 推荐：向量化
level = np.where(latency >= 300, "slow", "normal")
```

多层分类可以嵌套：

```python
level = np.where(
    latency >= 500, "very_slow",
    np.where(latency >= 200, "slow", "normal")
)
```

**和 pandas 的关系**：`np.where` 在 DataFrame 里同样能用，比 `apply` 快得多：

```python
df["level"] = np.where(df["latency_ms"] >= 300, "slow", "normal")
```

---

## 3. 广播（Broadcasting）

广播 = 不同形状的数组之间自动"扩展"再计算。

```python
matrix = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
])

bonus = np.array([10, 20, 30])  # shape (3,)

result = matrix + bonus
print(result)
# [[11 22 33]
#  [14 25 36]
#  [17 28 39]]
```

发生了什么：

```text
matrix (3, 3)    bonus (3,)
[[1 2 3]          [10 20 30]    → 自动复制成
 [4 5 6]    +     [10 20 30]      (3, 3) 再相加
 [7 8 9]]         [10 20 30]
```

你现在不需要记住所有广播规则。只需要知道：

```text
一行数据（或一列数据）可以自动应用到多行（或多列）
```

---

## 4. np.median 和 np.percentile

平均值容易被极端值拉偏，中位数和分位数更稳健。

```python
latency = np.array([120, 150, 180, 200, 250, 300, 5000])
#                                                     ↑ 极端值

print(latency.mean())              # 885.7 — 被 5000 拉偏了
print(np.median(latency))          # 200.0 — 更接近"大多数请求"
print(np.percentile(latency, 95))  # 300.0 — 95% 的请求低于这个值
print(np.percentile(latency, 99))  # 5000.0
```

常见分位数：

| 函数 | 含义 |
|---|---|
| `np.median(arr)` | 中位数 = 50 分位 |
| `np.percentile(arr, 95)` | P95：95% 数据 ≤ 这个值 |
| `np.percentile(arr, 99)` | P99：99% 数据 ≤ 这个值 |

**和后端监控的关系**：线上接口延迟通常看 P95/P99 而不是平均值——平均值会被少量超时请求拉偏，P95 反映"绝大多数用户的真实体验"。

---

## 本章掌握标准

你学完后要能做到：

1. 说出 `axis=0` 和 `axis=1` 的区别。
2. 用 `np.where` 替代简单的 if-else 循环。
3. 知道广播是"小数组自动扩展成大数组再算"。
4. 用 `np.median` 和 `np.percentile` 替代只看平均值。
