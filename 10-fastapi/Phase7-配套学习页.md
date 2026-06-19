---
date: 2026-06-10
project: Agentic Internship Coach
phase: 7
status: AI 已实现
---

# Phase 7 配套学习页 —— 关键词 RAG MVP

## 本 Phase 做了什么

实现了一个关键词 RAG 系统：上传学习笔记 → 提问时自动检索相关内容 → 拼到 Prompt 里让 LLM 回答 → 返回带来源的答案。

```
POST /api/v1/knowledge/documents     ← 上传笔记
POST /api/v1/rag/answer              ← 提问（自动检索+LLM回答）
```

---

## 核心概念

### 1. RAG 的流程（检索增强生成）

```
用户提问 "什么是缓存穿透"
    │
    ▼
① 检索 (Retrieval)
   jieba 分词: "缓存穿透" → ["缓存", "穿透"]
   遍历所有文档, 计算词频匹配分
   → 找到 "Redis缓存笔记" 文档(ID=1, score=0.82)
    │
    ▼
② 增强 (Augmented)
   把检索到的文档片段拼成上下文
   "学习资料: 【Redis缓存笔记】缓存穿透：查询不存在的数据..."
    │
    ▼
③ 生成 (Generation)
   把上下文 + 用户问题发给 LLM
   → "缓存穿透是查询不存在的数据导致请求绕过缓存直接打到数据库的问题。"
    │
    ▼
   返回: {answer: "...", sources: [{document_id: 1, title: "Redis缓存笔记", ...}]}
```

### 2. jieba 分词 + TF 匹配

```python
query_tokens = set(jieba.cut("什么是缓存穿透"))
# → {"什么", "是", "缓存", "穿透"}

chunk_tokens = set(jieba.cut("缓存穿透：查询不存在的数据..."))
# → {"缓存", "穿透", "查询", "不存在", "的", "数据"}

overlap = query_tokens & chunk_tokens  # → {"缓存", "穿透"}
score = len(overlap) / len(query_tokens)  # → 2/4 = 0.5
```

**为什么不用向量？** Phase 7 是关键词 RAG MVP——先理解检索的基本流程。向量 RAG（embedding + Milvus）放到 Phase 10。分层验证，不会失控。

### 3. 长文档切片

```python
def _chunk_text(text, size=200):
    return [text[i:i+size] for i in range(0, len(text), size)]
```

一篇 500 字的笔记会被切成 3 段（200 + 200 + 100），每段独立打分。这样即使文档很长，也能精确定位到相关段落。

### 4. 没有检索结果时的处理

```python
if not sources:
    return {"answer": "未找到相关内容。请先上传相关学习资料。", "sources": []}
```

**不编造、不假装知道。** 这是 RAG 的基本诚信——没找到就说没找到，不要让 LLM 胡编。

### 5. RAG 的 Prompt 结构

```
系统: "你是一个学习助手。根据提供的资料回答问题。"
用户: "学习资料: {检索到的文档片段}
       用户问题: {用户输入}
       返回 JSON: {answer: ...}"
```

关键约束：
- 要求 LLM "根据提供的资料回答"→ 减少幻觉
- 要求 "资料不足以回答时如实说明" → 诚实边界
- 要求 "只返回 JSON" → 结构化输出

---

## 扶墙走练习

### 练习 1：看检索过程（5 分钟）

打开 `src/rag/keyword_retriever.py`，找到 `retrieve` 函数。画出流程图：

```
query → jieba 分词 → query_tokens
docs → 每篇文档切片 → 每片分词 → 计算 overlap → 打分
→ 排序 → 取 top_k → 返回
```

### 练习 2：改切片大小（3 分钟）

把 `_CHUNK_SIZE` 从 200 改成 100，跑 `pytest tests/test_rag.py -v` — 看检索结果有什么变化。

### 练习 3：讲清楚（5 分钟）

说出来：

> "Phase 7 实现了关键词 RAG。用户提问后用 jieba 分词，和所有文档的切片做词频匹配，取 top-3 拼成上下文，发给 LLM 生成回答。返回结果包含 answer（回答）和 sources（来源：文档 ID、标题、摘要、匹配分）。没有检索结果时不编造，直接说没找到。长文档按 200 字符切片，每片独立打分。检索失败或 LLM 失败不影响其他功能。"
