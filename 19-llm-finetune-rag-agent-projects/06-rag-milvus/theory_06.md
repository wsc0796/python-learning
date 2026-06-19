---
aliases:
  - 06-rag-milvus
---
# Day 6：RAG 系统与 Milvus

读完约 15 分钟。

---

## 一、RAG 是什么

RAG = Retrieval-Augmented Generation（检索增强生成）。

### 为什么需要 RAG

| 问题 | 说明 | RAG 怎么解决 |
|------|------|-------------|
| 知识过时 | 模型训练后知识就冻结了 | 从外部知识库实时检索 |
| 幻觉 | 模型会编造答案 | 答案基于检索到的内容 |
| 私有知识 | 模型没看过企业数据 | 检索企业知识库 |
| 可追溯 | 不知道答案来源 | 可以引用原文 |

### RAG vs 微调

```
RAG：给模型加"参考书"——回答问题前先查资料
微调：让模型"记住"——把知识学到参数里

RAG 适合：知识更新快、需要可追溯的场景
微调适合：需要改变模型行为/风格的场景
```

---

## 二、RAG 基本流程

```
文档收集 → 清洗 → 切分 → 向量化 → 存入向量库
                                                   用户提问 → 向量化 → 检索 → 构造 Prompt → LLM 回答
```

### 详细流程

```text
① 文档处理
   收集文档 → 清洗噪音 → 按段落/章节切分 → Embedding → 写入向量数据库

② 检索
   用户提问 → Embedding（用同一模型） → 向量数据库搜索 Top-K → 返回相关片段

③ 生成
   把检索到的片段 + 用户问题 → 拼成 Prompt → LLM 生成 → 返回答案 + 引用
```

---

## 三、你已经在用 RAG

你的 `document_pipeline/` 就是 RAG 的变体：

```
你的管道：PDF → markitdown → 分节 → 摘要 → 索引 → query()

标准 RAG：文档 → 切分 → Embedding → 向量库 → 检索 → 回答
```

区别：

| 你的方案 | 标准 RAG |
|---------|---------|
| 用 LLM 选章节 | 用向量相似度检索 |
| 手动确定语义边界（##） | 按固定 token 切块 |
| 用文件系统做索引 | 用向量数据库 |

你的方案对**结构清晰的文档**效果更好。
标准 RAG 对**大规模、无结构文本**更具扩展性。

---

## 四、Milvus 向量数据库

Milvus 是开源的向量数据库，专门存向量 + 做相似度搜索。

### 核心概念

| 概念 | 类比 SQL | 说明 |
|------|---------|------|
| Collection | 表 | 存储向量和元数据 |
| Schema | 表结构 | 定义字段类型 |
| Vector Field | 向量列 | 存储 embedding |
| Scalar Field | 普通列 | 存文本、标签等 |
| Index | 索引 | 加速向量搜索 |
| Partition | 分区 | 按标签物理隔离 |

### 基本操作

```python
from pymilvus import connections, Collection, CollectionSchema

# 连接
connections.connect(host="localhost", port="19530")

# 定义 Schema
schema = CollectionSchema([
    FieldSchema("id", DataType.INT64, is_primary=True),
    FieldSchema("vector", DataType.FLOAT_VECTOR, dim=768),
    FieldSchema("text", DataType.VARCHAR, max_length=1000),
])

# 创建 Collection
collection = Collection("knowledge_base", schema)

# 插入
collection.insert([ids, vectors, texts])

# 创建索引
collection.create_index("vector", {"index_type": "IVF_FLAT", "metric_type": "L2"})

# 加载到内存
collection.load()

# 搜索
results = collection.search(
    data=[query_vector],
    anns_field="vector",
    param={"metric_type": "L2", "params": {"nprobe": 10}},
    limit=5,
)
```

---

## 五、Milvus 的部署方式

| 方式 | 适用场景 | 资源需求 |
|------|---------|---------|
| Milvus Lite | 本地测试、教学 | Python 包，轻量 |
| Docker 单机 | 开发环境 | 2C4G |
| K8s 集群 | 生产环境 | 多节点 |

本专题用 Milvus Lite 就够了：

```bash
pip install pymilvus
```

---

## 六、RAG 和你已有的 pipeline 的关系

```
你的 pipeline（基于 Template Method）：
Pipeline.run() → collect → convert → segment → enrich → index → query
                                                         ↑       ↑
                                                      向量库   检索+LLM

RAG 的流程：
文档 → 切分 → Embedding → Milvus → 检索 → LLM → 回答

你可以直接在 pipeline 的 enrich 和 index 步骤接入 Milvus，
替换当前的 JSON 文件索引。
```
