---
aliases:
  - 29-numpy
---
# 29 - NumPy 基础

## 一句话

NumPy 是 Python 做数值计算的基础库。它最核心的东西是 `ndarray`，也就是“同一种类型的数据组成的多维数组”。

如果 Python 的 list 像普通表格，NumPy 数组就像专门为计算优化过的矩阵。

## 1. 为什么不用 list

普通 list 可以存不同类型：

```python
data = [1, "2", 3.0]
```

但数值计算通常需要：

- 批量加减乘除
- 矩阵运算
- 快速统计
- 统一的数据类型

NumPy 适合这种场景。

```python
import numpy as np

scores = np.array([80, 90, 100])
print(scores + 5)  # [ 85  95 105]
```

如果用 list，`scores + 5` 会报错；NumPy 可以直接批量计算。

## 2. 创建数组

```python
import numpy as np

a = np.array([1, 2, 3])
b = np.arange(1, 6)
c = np.zeros((2, 3))
d = np.ones((2, 3))
e = np.linspace(0, 1, 5)
```

常见含义：

| 写法 | 含义 |
|---|---|
| `np.array([...])` | 从列表创建数组 |
| `np.arange(1, 6)` | 生成 1 到 5 |
| `np.zeros((2, 3))` | 2 行 3 列，全 0 |
| `np.ones((2, 3))` | 2 行 3 列，全 1 |
| `np.linspace(0, 1, 5)` | 0 到 1 等分成 5 个点 |

随机数组也很常用：

```python
rng = np.random.default_rng(seed=42)

random_ints = rng.integers(1, 10, size=(2, 3))
random_floats = rng.random((2, 3))
normal_data = rng.normal(loc=0, scale=1, size=5)
```

常见含义：

| 写法 | 含义 |
|---|---|
| `integers()` | 随机整数 |
| `random()` | 0 到 1 之间的随机小数 |
| `normal()` | 正态分布随机数 |
| `seed` | 固定随机结果，方便复现实验 |

## 3. 数组属性

```python
arr = np.array([[1, 2, 3], [4, 5, 6]])

print(arr.shape)  # (2, 3)
print(arr.ndim)   # 2
print(arr.dtype)  # int64 或 int32
print(arr.size)   # 6
```

你主要记：

| 属性 | 含义 |
|---|---|
| `shape` | 形状，几行几列 |
| `ndim` | 维度数量 |
| `dtype` | 元素类型 |
| `size` | 元素总数 |

## 4. 类型转换

NumPy 数组里的元素通常是同一种类型。

```python
arr = np.array([1.2, 2.8, 3.5])
int_arr = arr.astype(int)
```

结果：

```text
[1 2 3]
```

注意：转成整数会直接截断小数，不是四舍五入。

## 5. 向量化计算

NumPy 最重要的能力是“批量计算”。

```python
prices = np.array([10, 20, 30])
discounted = prices * 0.8
```

结果：

```text
[ 8. 16. 24.]
```

这叫向量化。你不用写循环，NumPy 会一次性处理整组数据。

## 6. 布尔筛选

```python
scores = np.array([59, 60, 80, 95])
passed = scores[scores >= 60]
```

结果：

```text
[60 80 95]
```

核心逻辑：

```text
scores >= 60 先得到布尔数组
再用布尔数组筛选原数组
```

## 7. 常用函数

```python
scores = np.array([80, 90, 100])

scores.mean()
scores.max()
scores.min()
scores.sum()
scores.std()
```

常见用途：

| 函数 | 含义 |
|---|---|
| `mean()` | 平均值 |
| `max()` | 最大值 |
| `min()` | 最小值 |
| `sum()` | 求和 |
| `std()` | 标准差 |

还有两个非常常用：

```python
arr = np.array([3, 1, 2, 3, 2])

np.unique(arr)  # 去重
np.sort(arr)    # 排序
```

结果：

```text
[1 2 3]
[1 2 2 3 3]
```

## 8. reshape 改形状

```python
arr = np.arange(1, 7)
matrix = arr.reshape(2, 3)
```

结果：

```text
[[1 2 3]
 [4 5 6]]
```

注意：元素总数必须对得上。6 个元素可以变成 `(2, 3)`，不能变成 `(4, 4)`。

## 9. 矩阵运算

```python
a = np.array([[1, 2], [3, 4]])
b = np.array([[10, 20], [30, 40]])

print(a + b)
print(a * b)      # 对应位置相乘
print(a @ b)      # 矩阵乘法
```

重点区别：

```text
*  是逐元素相乘
@  是矩阵乘法
```

## 10. NumPy 和后续内容的关系

```text
NumPy
  -> Pandas 底层大量依赖 NumPy
  -> Matplotlib 常用 NumPy 生成 x/y 数据
  -> 机器学习、向量检索、Embedding 都离不开数组/矩阵
```

你后面学 RAG 时，向量本质上就是一组数字：

```python
embedding = np.array([0.12, -0.05, 0.88])
```

所以 NumPy 是数据分析和 AI 的底层地基。

## 本章掌握标准

你学完后要能做到：

1. 知道 `np.array()` 创建的是数组，不是普通 list。
2. 能用 `shape` 看数组形状。
3. 能进行批量加减乘除。
4. 能用布尔条件筛选数据。
5. 能用 `mean/max/min/sum` 做基础统计。
6. 能理解 `*` 和 `@` 的区别。
