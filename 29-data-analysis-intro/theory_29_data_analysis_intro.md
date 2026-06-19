---
aliases:
  - 29-data-analysis-intro
---
# 29 - 数据分析入门

## 一句话

数据分析不是“会画图”这么简单，而是把原始数据变成可判断、可解释、可行动的信息。

一条常见流程是：

```text
收集数据
  -> 清洗数据
  -> 统计分析
  -> 可视化
  -> 得出结论
  -> 导出结果
```

## 1. Python 做数据分析的优势

Python 适合数据分析，主要因为生态完整：

| 场景 | 常用库 |
|---|---|
| 数值计算 | NumPy |
| 表格处理 | Pandas |
| 可视化 | Matplotlib / Seaborn |
| 机器学习 | scikit-learn |
| 深度学习 | PyTorch |
| 交互式分析 | Jupyter Notebook |

你可以理解成：

```text
NumPy 管数组
Pandas 管表格
Matplotlib 管画图
Jupyter 管实验过程
```

## 2. Jupyter Notebook 是什么

Jupyter Notebook 是一种“边写代码、边看结果、边写笔记”的交互式环境。

它特别适合：

- 数据探索
- 临时实验
- 画图展示
- 记录分析过程

普通 `.py` 文件更适合写正式程序；Notebook 更适合做探索。

## 3. Notebook 基础操作

Notebook 由一个个 cell 组成。

常见 cell 类型：

| 类型 | 用途 |
|---|---|
| Code | 写 Python 代码 |
| Markdown | 写说明文字 |

常用快捷键：

| 快捷键 | 含义 |
|---|---|
| `Shift + Enter` | 运行当前 cell，进入下一个 |
| `Ctrl + Enter` | 运行当前 cell，停留当前 |
| `A` | 在上方插入 cell |
| `B` | 在下方插入 cell |
| `M` | 当前 cell 改成 Markdown |
| `Y` | 当前 cell 改成 Code |
| `DD` | 删除当前 cell |

注意：`A/B/M/Y/DD` 通常要在命令模式下使用，也就是 cell 边框不是正在编辑文字的状态。

## 4. Pycharm / VSCode 连接 Jupyter 的理解

不管是 Pycharm 还是 VSCode，本质都是：

```text
编辑器
  -> 连接 Python 环境
  -> 启动/连接 Jupyter Kernel
  -> 按 cell 运行代码
```

你现在不用纠结 IDE 细节，先掌握 Notebook 的核心用法即可：

```text
一小段代码
  -> 运行
  -> 观察结果
  -> 修改
  -> 再运行
```

这就是数据分析最常见的工作方式。

## 5. 数据分析学习路线

按照你的课程大纲，顺序应该是：

```text
数据分析入门
  -> NumPy
  -> Pandas
  -> 分组聚合 / 透视表
  -> Matplotlib
  -> RFM 用户分组项目
```

不要一开始就追求复杂图表。先能做到：

```text
读入数据
看懂字段
清洗缺失值
按条件筛选
分组统计
画一张图
导出结果
```

## 本章掌握标准

你学完后要能说清：

1. NumPy、Pandas、Matplotlib 分别负责什么。
2. Jupyter Notebook 适合什么场景。
3. 数据分析的一般流程是什么。
4. 为什么 `.py` 文件和 Notebook 都有用。
