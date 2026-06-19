# 数据分析与 AI 应用内容索引

## 当前已有模块

| 模块 | 路径 | 内容 |
|---|---|---|
| 数据分析入门 | `29-data-analysis-intro` | Python 数分优势、常用库、Jupyter 思路 |
| NumPy | `29-numpy` | 数组、向量化、统计、矩阵运算 |
| NumPy 补缺 | `29-numpy/theory_29_numpy_gap.md` | axis/广播/np.where/分位数 |
| Pandas | `30-pandas` | DataFrame、CSV、筛选、缺失值、分组聚合 |
| Pandas 补缺 | `30-pandas/theory_30_pandas_gap.md` | value_counts/merge/dt访问器/列运算/astype |
| Matplotlib | `31-matplotlib` | 折线图、柱状图、散点图、多图绘制 |
| Matplotlib 补缺 | `31-matplotlib/theory_31_matplotlib_gap.md` | 直方图 hist |
| RFM 综合项目 | `32-data-analysis-rfm` | 用户分组分析，串联 Pandas 和 Matplotlib |
| FastAPI | `10-fastapi` | Pydantic、DI、Service、Repository、CRUD API |
| LangChain | `19-llm-finetune-rag-agent-projects/10-langchain-basic` | Chain、RAG、Agent、Memory、Indexes 概念 |

## 推荐学习顺序

如果走 Python 后端 + AI 应用主线：

```text
10-fastapi
  -> SQLAlchemy 数据库版 CRUD
  -> LangChain / RAG
  -> Pandas 数据处理
  -> NumPy 向量基础
  -> Matplotlib 报表可视化
```

如果走数据分析主线：

```text
29-data-analysis-intro
  -> 29-numpy
  -> 30-pandas
  -> 31-matplotlib
  -> 32-data-analysis-rfm
```

## 每个模块的达标标准

### 数据分析入门

能说清：

```text
NumPy / Pandas / Matplotlib 分别负责什么
Jupyter Notebook 适合什么场景
数据分析的一般流程是什么
```

### NumPy

能解释：

```text
数组是什么
shape 是什么
为什么可以批量加减乘除
布尔筛选怎么做
```

### Pandas

能完成：

```text
读取 CSV
选择列
按条件筛选
新增列
处理缺失值
分组聚合
导出 CSV
```

### Matplotlib

能完成：

```text
画折线图
画柱状图
画散点图
保存图片
```

### FastAPI

能说清：

```text
main.py 接收 HTTP
models.py 做数据校验
service.py 做业务
repository.py 做数据存取
dependencies.py 做依赖注入
```

### LangChain

能说清：

```text
Prompt 是输入模板
Chain 是多步调用
RAG 是检索后再回答
Agent 是模型选择工具
Memory 是对话状态
```
