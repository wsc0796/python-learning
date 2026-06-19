# 32 - 数据分析综合项目：RFM 用户分组

这个项目把 NumPy、Pandas、Matplotlib 串起来。

```text
原始订单数据
  -> Pandas 清洗
  -> 计算 R/F/M 指标
  -> 用户分组
  -> 导出 CSV
  -> Matplotlib 画图
```

## RFM 是什么

RFM 是一种用户价值分析方法：

| 指标 | 全称 | 含义 |
|---|---|---|
| R | Recency | 最近一次消费距离现在多久 |
| F | Frequency | 消费次数 |
| M | Monetary | 消费金额 |

简单理解：

```text
最近买过 + 买得多 + 花得多 = 高价值用户
```

## 对照课程大纲

这个项目覆盖：

- RFM 模型介绍
- 数据加载与处理
- 用户分组聚合
- 区间划分与评估
- 结果分析
- 导出 CSV
- 可视化

Excel 导出和 MySQL 导出属于增强项。当前项目先导出 CSV，后面学到数据库版 CRUD / SQLAlchemy 后，可以再把结果写入数据库。

## 推荐学习顺序

1. 先学 `29-numpy`
2. 再学 `30-pandas`
3. 再学 `31-matplotlib`
4. 最后跑本项目

## 运行

```powershell
python rfm_project.py
```

如果没有 matplotlib，会跳过画图，只导出 CSV。
