---
aliases:
  - 31-matplotlib-gap
---
# 31 - Matplotlib 补缺：直方图

> `31-matplotlib` 主笔记覆盖了折线图、柱状图、散点图，但漏了直方图。
> 直方图是看"数据分布"最常用的图。

---

## 一句话

折线图看趋势，柱状图比类别，散点图看关系，**直方图看分布**——一组数据大多集中在哪个区间、有没有长尾。

---

## 1. 基础直方图

```python
import matplotlib.pyplot as plt

latency = [120, 150, 180, 200, 220, 250, 280, 300, 350, 500]

fig, ax = plt.subplots()
ax.hist(latency, bins=5)
ax.set_title("Latency Distribution")
ax.set_xlabel("Latency (ms)")
ax.set_ylabel("Frequency")
plt.show()
```

`bins` 控制柱子数量（也就是分多少个区间）：

| bins 值 | 效果 |
|---|---|
| 太小 (如 3) | 太粗糙，看不清分布 |
| 太大 (如 50) | 太细碎，看不出规律 |
| 20 左右 | 多数场景合适的起点 |

---

## 2. 和真实数据的结合

```python
import pandas as pd

df = pd.read_csv("api_logs.csv")

fig, ax = plt.subplots()
ax.hist(df["latency_ms"], bins=20, edgecolor="white")
ax.set_title("API Latency Distribution")
ax.set_xlabel("Latency (ms)")
ax.set_ylabel("Request Count")
plt.show()
```

`edgecolor="white"` 让柱子之间出现白线，看起来更清晰。

---

## 3. 图表选择口诀（补全版）

```text
随时间变化      → 折线图 plot
不同类别比较    → 柱状图 bar
观察数值分布    → 直方图 hist
观察两个变量关系 → 散点图 scatter
```

---

## 本章掌握标准

你学完后要能做到：

1. 用 `ax.hist()` 画直方图。
2. 知道 `bins` 控制柱子数量。
3. 能说出四种图分别适合什么场景。
