---
aliases:
  - 30-pandas-gap
---
# 30 - Pandas 补缺：value_counts / merge / 时间字段 / 列运算

> 这 5 个知识点在 `30-pandas` 主笔记里没有覆盖或只提了一句，但验收项目里会用到。
> 前置：已理解 DataFrame、groupby、缺失值处理。

---

## 一句话

`value_counts` 看频数分布，`merge` 关联两张表，`dt` 访问器拆解时间字段，列运算在 groupby 结果上继续加工。

---

## 1. value_counts：频数统计

```python
import pandas as pd

df = pd.DataFrame({
    "endpoint": ["/users", "/orders", "/users", "/login", "/users", "/orders"],
})

# 每个接口被请求了多少次
print(df["endpoint"].value_counts())
# /users     3
# /orders    2
# /login     1

# 看占比
print(df["endpoint"].value_counts(normalize=True))
# /users     0.50
# /orders    0.33
# /login     0.17
```

这等价于 `df.groupby("endpoint").size().sort_values(ascending=False)`，但更简洁。

---

## 2. merge：关联两张表

真实项目里数据很少只在一张表里。用户信息一张表，订单一张表，需要关联。

```python
users = pd.DataFrame({
    "user_id": [1, 2, 3],
    "username": ["Tom", "Alice", "Bob"],
})

orders = pd.DataFrame({
    "order_id": [101, 102, 103, 104],
    "user_id": [1, 2, 1, 5],   # user_id=5 在 users 表里不存在
    "amount": [199, 299, 399, 99],
})
```

### inner：只保留两边都有的

```python
result = orders.merge(users, on="user_id", how="inner")
print(result)
#    order_id  user_id  amount username
# 0       101        1     199      Tom
# 1       103        1     399      Tom
# 2       102        2     299    Alice
# user_id=5 和 user_id=3 被丢弃了（在对方表里找不到）
```

### left：保留左表全部

```python
result = orders.merge(users, on="user_id", how="left")
print(result)
#    order_id  user_id  amount username
# 0       101        1     199      Tom
# 1       102        2     299    Alice
# 2       103        1     399      Tom
# 3       104        5      99      NaN   ← 右表没有，填 NaN
```

记忆口诀：

```text
inner：取交集 — 两边都有才保留
left：取左表全部 — 右表没有的填 NaN
```

| how | 行为 |
|---|---|
| `"inner"` | 只保留两表都匹配的行 |
| `"left"` | 保留左表所有行，右表匹配不上的填 NaN |
| `"right"` | 保留右表所有行 |
| `"outer"` | 保留两表所有行 |

**和 SQL 的对应关系**：`merge` = SQL 的 `JOIN`，`on` = `ON`，`how="left"` = `LEFT JOIN`。

---

## 3. 时间字段：`pd.to_datetime` + `dt` 访问器

时间字段拿到手第一件事就是转换类型，否则它就是普通字符串。

```python
df = pd.DataFrame({
    "timestamp": ["2026-06-01 08:00:00", "2026-06-01 09:30:00", "2026-06-02 14:15:00"],
})

# 关键：先转换成 datetime 类型
df["timestamp"] = pd.to_datetime(df["timestamp"])

# 然后用 .dt 拆解
df["hour"] = df["timestamp"].dt.hour        # 8, 9, 14
df["date"] = df["timestamp"].dt.date        # 2026-06-01, 2026-06-01, 2026-06-02
df["weekday"] = df["timestamp"].dt.day_name()  # Monday, Monday, Tuesday
df["month"] = df["timestamp"].dt.month      # 6, 6, 6
```

常用 dt 属性一览：

| 属性 | 得到 | 示例 |
|---|---|---|
| `.dt.hour` | 小时 (0-23) | 8, 14, 22 |
| `.dt.date` | 日期（去掉时间） | 2026-06-01 |
| `.dt.day_name()` | 星期几（英文） | Monday |
| `.dt.month` | 月份 | 6 |
| `.dt.day` | 日 | 1, 15, 30 |

**读取 CSV 时直接转换**（省一步）：

```python
df = pd.read_csv("api_logs.csv", parse_dates=["timestamp"])
```

---

## 4. groupby 结果的列运算

groupby 聚合完得到的是一个 DataFrame，可以继续在上面做列运算。

```python
# 聚合结果
report = df.groupby("endpoint").agg(
    requests=("endpoint", "size"),
    errors=("is_error", "sum"),
)

# 在聚合结果上新增计算列
report["error_rate"] = report["errors"] / report["requests"]
report["success_rate"] = 1 - report["error_rate"]
```

这本质上就是 DataFrame 的基本操作——聚合结果也是一个 DataFrame，所以选择列、新增列、排序这些操作全部适用。

---

## 5. astype：强制类型转换

```python
df["user_id"] = df["user_id"].fillna(-1).astype(int)

df["status_code"] = df["status_code"].astype(int)

df["endpoint"] = df["endpoint"].astype("category")  # 节省内存
```

常见转换：

| 代码 | 效果 |
|---|---|
| `.astype(int)` | 转整数 |
| `.astype(float)` | 转小数 |
| `.astype(str)` | 转字符串 |
| `.astype("category")` | 转分类类型（有限个取值时省内存） |

---

## 本章掌握标准

你学完后要能做到：

1. 用 `value_counts` 快速看一列的频数分布。
2. 用 `merge` 把两张表按某个字段关联起来，说清 `inner` 和 `left` 的区别。
3. 用 `pd.to_datetime` + `.dt.hour` 从时间戳提取小时。
4. 在 groupby 聚合结果上做列运算（比如算错误率）。
5. 用 `astype` 转换列的数据类型。
