---
aliases:
  - 30-pandas
---
# 30 - Pandas 基础

## 一句话

Pandas 是 Python 里做表格数据处理的核心库。

如果 NumPy 主要处理“数组/矩阵”，Pandas 主要处理“带列名的表格”。

```text
NumPy  -> 数组
Pandas -> 表格
```

## 1. Series 和 DataFrame

Pandas 有两个核心对象：

| 对象 | 类比 | 含义 |
|---|---|---|
| `Series` | 一列数据 | 带索引的一维数据 |
| `DataFrame` | 一张表 | 多列组成的二维数据 |

```python
import pandas as pd

s = pd.Series([80, 90, 100], name="score")

df = pd.DataFrame({
    "name": ["张三", "李四", "王五"],
    "score": [80, 90, 100],
})
```

## 2. 读取和查看数据

```python
df = pd.read_csv("students.csv")

df.head()
df.tail()
df.info()
df.describe()
```

常见含义：

| 方法 | 用途 |
|---|---|
| `head()` | 看前几行 |
| `tail()` | 看后几行 |
| `info()` | 看列名、缺失值、类型 |
| `describe()` | 看数值列统计 |

## 3. 选择列和行

选择一列：

```python
df["score"]
```

选择多列：

```python
df[["name", "score"]]
```

按条件筛选：

```python
df[df["score"] >= 60]
```

按位置选择可以用 `iloc`：

```python
df.iloc[0]       # 第 1 行
df.iloc[0:3]     # 前 3 行
df.iloc[:, 0:2]  # 所有行，前 2 列
```

按标签选择可以用 `loc`：

```python
df.loc[df["city"] == "南昌", ["name", "score"]]
```

简单记：

```text
iloc 看位置
loc 看标签/条件
```

## 4. 新增列

```python
df["passed"] = df["score"] >= 60
```

也可以基于多个字段计算：

```python
df["total"] = df["math"] + df["english"]
```

删除列：

```python
df = df.drop(columns=["passed"])
```

修改列：

```python
df["name"] = df["name"].str.strip()
```

## 5. 数据类型

```python
df.dtypes
df["score"] = df["score"].astype(float)
```

常见类型：

| 类型 | 含义 |
|---|---|
| `int64` | 整数 |
| `float64` | 小数 |
| `object` | 字符串或混合类型 |
| `bool` | 布尔值 |
| `datetime64` | 日期时间 |

## 6. apply 函数

`apply()` 用来把一个函数应用到一列或一行。

```python
def level(score: int) -> str:
    if score >= 90:
        return "优秀"
    if score >= 60:
        return "及格"
    return "不及格"

df["level"] = df["score"].apply(level)
```

如果是一行一行处理：

```python
df["total"] = df.apply(lambda row: row["math"] + row["english"], axis=1)
```

## 7. 缺失值处理

真实数据经常有空值：

```python
df.isna().sum()
df["score"] = df["score"].fillna(0)
df = df.dropna()
```

常见策略：

| 方法 | 含义 |
|---|---|
| `isna()` | 判断是否缺失 |
| `fillna()` | 填充缺失值 |
| `dropna()` | 删除缺失行 |

## 8. 排序

```python
df.sort_values("score", ascending=False)
```

含义：

```text
按 score 从高到低排序
```

## 9. 数据合并 concat

```python
df1 = pd.DataFrame({"name": ["张三"], "score": [90]})
df2 = pd.DataFrame({"name": ["李四"], "score": [80]})

df = pd.concat([df1, df2], ignore_index=True)
```

`concat` 常用于：

```text
合并多个月份订单
合并多个 CSV
把多批数据拼成一张表
```

## 10. 分组聚合

这是 Pandas 的重点。

```python
df.groupby("city")["amount"].sum()
```

意思是：

```text
按 city 分组
每组统计 amount 总和
```

更完整：

```python
df.groupby("city").agg(
    total_amount=("amount", "sum"),
    avg_amount=("amount", "mean"),
    order_count=("amount", "count"),
)
```

## 11. 透视表

透视表适合做交叉统计。

```python
pd.pivot_table(
    df,
    values="amount",
    index="city",
    columns="category",
    aggfunc="sum",
    fill_value=0,
)
```

意思是：

```text
行：城市
列：商品类别
值：销售额求和
```

## 12. 文件读写

```python
df.to_csv("result.csv", index=False, encoding="utf-8-sig")
df.to_excel("result.xlsx", index=False)
```

读取 txt 时，如果是逗号或制表符分隔，也可以用：

```python
pd.read_csv("data.txt", sep="\t")
```

`encoding="utf-8-sig"` 对中文 Excel 比较友好。

## 13. Pandas 和后端/AI 的关系

Pandas 不只是数据分析课会用，后端和 AI 项目也常用：

```text
读 CSV/Excel
清洗用户上传数据
批量生成报表
处理 RAG 文档元数据
评估模型结果
导出运营数据
```

比如一个 AI 聊天记录系统，后面可以用 Pandas 统计：

```text
每天请求量
每个用户使用次数
平均响应时长
高频问题分类
```

## 本章掌握标准

你学完后要能做到：

1. 知道 DataFrame 是“表格”。
2. 能读取 CSV。
3. 能选择列、筛选行。
4. 能新增计算列。
5. 能处理缺失值。
6. 能按字段分组统计。
7. 能导出 CSV。
