---
aliases:
  - 07-rag-optimization
---
# Day 7：RAG 优化与评估

读完约 12 分钟。

---

## 一、RAG 常见问题

| 问题 | 可能原因 |
|------|---------|
| 检索不到 | 切分太大/太小、Embedding 模型不合适 |
| 检索不准 | 查询和文档语义差异大 |
| 答案幻觉 | 检索内容不够或 Prompt 约束不足 |
| 上下文太长 | 召回结果过多，超 token 限制 |
| 响应慢 | 检索 + 生成长链路过长 |

---

## 二、优化方向

### 1. 文档切分优化

```
切分太小 → 信息不完整，缺少上下文
切分太大 → 噪音多，检索精度下降

经验值：
- 语义明确的文本：按章节切（你的 ## 方式）
- 无结构文本：256-512 tokens 带 overlap
```

### 2. Chunk Overlap

```
段落1：AAAAA [overlap] BBBBB
段落2：[overlap] BBBBB CCCCC

避免检索时切在关键信息中间。
```

### 3. Embedding 模型选择

| 模型 | 维度 | 适用 |
|------|------|------|
| BGE | 768 | 中文通用 |
| text-embedding-v3 | 1024 | DeepSeek 生态 |
| voyage | 1024 | 多语言 |

### 4. Hybrid Search（混合检索）

```
向量检索 ← 擅长语义相似
BM25 检索 ← 擅长关键词精确匹配

结合方式：
score = α × vector_score + (1-α) × bm25_score
```

### 5. Rerank（重排序）

```
第一步：用轻量检索从 10000 条召回 50 条
第二步：用 Rerank 模型对 50 条精细排序，取前 5 条

为什么需要：
向量检索的第一轮是近似搜索，精度不够。
Rerank 可以精细比较，但速度慢，不能对全量做。
```

### 6. Query Rewrite（查询改写）

```
用户："他叫什么名字？"（代词模糊）
改写为："这篇论文的第一作者叫什么名字？"

方法：用 LLM 把用户问题改得更完整、更明确。
```

### 7. Metadata Filter

```
检索时先按元数据过滤（时间、类型、来源），再向量搜索。

效果：减少无关噪音，提高召回精度。
```

---

## 三、RAG 评估指标

| 指标 | 含义 |
|------|------|
| Recall@K | Top-K 中包含了多少相关文档 |
| Precision@K | Top-K 中有多少是相关的 |
| MRR | 第一个正确答案的排名 |
| Faithfulness | 答案是否忠于检索内容 |
| Answer Relevance | 答案是否回答了问题 |
| Context Relevance | 检索的上下文是否相关 |

### 最简单的评估方式

```python
# 人工评估
def evaluate(question, retrieved_docs, answer):
    # 1. 检索到的文档和问题相关吗？
    # 2. 答案基于检索内容吗？
    # 3. 答案回答了问题吗？
    return {
        "context_relevance": "相关/部分相关/不相关",
        "faithfulness": "忠实/部分编造/编造",
        "answer_relevance": "回答了/部分/没回答",
    }
```

---

## 四、你的 pipeline 的优化空间

你的 `document_pipeline/local_pdf_pipeline.py` 可以加：

```
当前：LLM 读索引 → 选章节 → 读全文 → 回答
优化：
  ① 加 BM25 关键词检索（辅助 LLM 定位）
  ② 加 Rerank（如果召回章节太多）
  ③ 加 Query Rewrite（问题模糊时）
  ④ Metadata Filter（按文档名/类型过滤）
```
