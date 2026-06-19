---
aliases:
  - 08-llm-knowledge-extension
---
# Day 8：大模型知识扩展

读完约 10 分钟。

---

## 一、Flash Attention

### 解决什么问题

标准 Attention 的计算：
```
Q × K^T → Score → Softmax → Score × V
               ↓
      中间结果（S, P）要写回显存
               ↓
      显存瓶颈在 I/O，不是计算
```

### Flash Attention 的思路

不把中间结果写回显存，而是在计算时就合并。

```
标准：Q×K → 写显存 → Softmax → 写显存 → ×V
Flash：Q×K → Softmax → ×V（一步到位，不写中间结果）
```

### 效果

- 训练速度提升 2-3 倍
- 显存占用降低 70%
- 精度无损

---

## 二、BM25

经典的关键词检索算法，比 TF-IDF 更先进。

### 核心公式理解

```
score = IDF × (TF × (k1 + 1)) / (TF + k1 × (1 - b + b × 文档长度/平均长度))
```

不用记住公式，记住几个直觉：

```
词频越高 → 分数越高（但收益递减）
文档越短 → 关键词命中价值越高
罕见词命中 → 分数加成更高
```

### BM25 在 RAG 中的角色

```
向量检索：语义匹配，"深度学习"能匹配"神经网络"
BM25：关键词精确匹配，"LoRA r=8"能匹配"r=8"这个精确值

两者互补 → Hybrid Search
```

---

## 三、Hybrid Search

```
向量检索的 Top-K + BM25 的 Top-K → 合并 → Rerank → 最终结果
```

### 为什么需要 Hybrid Search

| 场景 | 向量检索 | BM25 |
|------|---------|------|
| "LoRA 和 Adapter 的区别" | ✅ | ❌ |
| "r=8 什么意思" | ❌ | ✅ |
| "RAG 怎么减少幻觉" | ✅ | ❌ |
| "Python 3.14 特性" | ❌ | ✅ |

---

## 四、这些对你有什么实际意义

```
Flash Attention → 你的 DeepSeek API 底层就在用（更快更便宜）
BM25 → 可以加到你的 pipeline 里做关键词辅助检索
Hybrid Search → RAG 系统升级方向

掌握这些不是为了写代码，而是理解底层在做什么。
当你跟别人讨论技术方案时，知道"为什么这么选"比"怎么实现"更重要。
```
