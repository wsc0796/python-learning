---
aliases:
  - 31-matplotlib
---
# 31 - Matplotlib 基础

## 一句话

Matplotlib 是 Python 里最基础、最通用的画图库。

Pandas 负责处理表格，Matplotlib 负责把数据画成图。

```text
数据 -> Pandas 清洗统计 -> Matplotlib 可视化
```

## 1. 基本折线图

```python
import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y = [10, 20, 15, 30]

plt.plot(x, y)
plt.show()
```

`plt.show()` 会弹出图像窗口。

如果你在脚本里想保存图片：

```python
plt.savefig("line_chart.png")
```

## 2. 标题、坐标轴、网格

```python
plt.plot(x, y)
plt.title("Sales Trend")
plt.xlabel("Day")
plt.ylabel("Sales")
plt.grid(True)
plt.show()
```

常见元素：

| 方法 | 作用 |
|---|---|
| `title()` | 标题 |
| `xlabel()` | x 轴名称 |
| `ylabel()` | y 轴名称 |
| `grid()` | 网格 |
| `legend()` | 图例 |

设置刻度：

```python
plt.xticks([1, 2, 3, 4], ["周一", "周二", "周三", "周四"])
plt.yticks([0, 50, 100, 150])
```

刻度就是坐标轴上显示哪些点、显示什么文字。

## 3. 柱状图

```python
cities = ["南昌", "杭州", "上海"]
sales = [1200, 1800, 1500]

plt.bar(cities, sales)
plt.show()
```

柱状图适合比较不同类别。

```text
城市销量对比
各部门人数
不同商品销售额
```

## 4. 散点图

```python
hours = [1, 2, 3, 4, 5]
scores = [55, 60, 70, 78, 88]

plt.scatter(hours, scores)
plt.show()
```

散点图适合看两个变量之间的关系。

```text
学习时长 vs 成绩
广告费用 vs 销售额
价格 vs 销量
```

## 5. 多图绘制

```python
fig, axes = plt.subplots(1, 2, figsize=(10, 4))

axes[0].plot(x, y)
axes[0].set_title("Line")

axes[1].bar(cities, sales)
axes[1].set_title("Bar")

plt.tight_layout()
plt.show()
```

`subplots()` 是更推荐的写法，适合复杂图。

## 6. 多个坐标系

有时候两组数据量纲不同，比如：

```text
销售额：几千
转化率：0 到 1
```

可以使用双 y 轴：

```python
fig, ax1 = plt.subplots()

ax1.plot(days, sales, color="blue")
ax1.set_ylabel("Sales")

ax2 = ax1.twinx()
ax2.plot(days, rate, color="red")
ax2.set_ylabel("Conversion Rate")

plt.show()
```

## 7. 中文显示问题

Matplotlib 默认可能显示不了中文。Windows 上可以设置：

```python
plt.rcParams["font.sans-serif"] = ["Microsoft YaHei", "SimHei"]
plt.rcParams["axes.unicode_minus"] = False
```

如果中文还是乱码，先用英文标题也可以，不影响学习主线。

## 8. Matplotlib 和项目的关系

你后面做 RFM 用户分组分析时会用到：

```text
Pandas 统计用户分组
Matplotlib 画出分组人数、消费金额、趋势图
```

你后面做后端项目时也可能用到：

```text
后台生成报表图片
接口返回图表文件
训练结果可视化
模型评估可视化
```

## 本章掌握标准

你学完后要能做到：

1. 能画折线图。
2. 能画柱状图。
3. 能画散点图。
4. 能设置标题、坐标轴、网格。
5. 能保存图片。
6. 能理解什么时候用哪种图。
