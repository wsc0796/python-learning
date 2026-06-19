---
aliases:
  - 11-llm-architecture
---
# 11. LLM 主要架构

> 前置：[[10-llm-basic-introduction]]
> 目标：理解 Encoder-Only、Decoder-Only、Encoder-Decoder 三种架构及其代表模型
> 用时：约 10 分钟
>
> 相关笔记：[[12-chatgpt-principle]]

---

## 一、三种架构全景

| 架构 | 代表模型 | 擅长 | 怎么训练 |
|------|---------|------|---------|
| **Encoder-Only** | BERT | 理解（分类、检索、匹配） | 掩码语言模型（MLM） |
| **Decoder-Only** | GPT、LLaMA、Qwen | 生成（对话、写作、代码） | 自回归（预测下一个 token） |
| **Encoder-Decoder** | T5、BART | 翻译、摘要 | Encoder 理解 + Decoder 生成 |

---

## 二、AE（自编码模型，Encoder-Only）

### 代表：BERT

### 训练方式：Masked Language Model（MLM）

```text
输入：我 [MASK] 学习 Python
目标：预测 [MASK] 处是 "爱"
```

随机遮住 15% 的词，让模型根据上下文填空。**双向**理解——模型同时看左边和右边的词。

### 特点

- 擅长"理解"任务：文本分类、情感分析、语义匹配、信息检索
- **不能直接生成文本**——它只会填空，不会从左到右续写
- 你的苍穹外卖如果要做智能搜索（用户输入自然语言 → 匹配菜品），BERT 是经典方案

---

## 三、AR（自回归模型，Decoder-Only）

### 代表：GPT 系列、LLaMA、Qwen

### 训练方式：预测下一个 token

```text
输入：我 爱 学习
目标：预测下一个是 "Python"
```

只能**从左到右**（单向），不能回头看后面的词。

### 特点

- 擅长"生成"任务：对话、写作、代码生成、翻译
- **当前大模型主流架构**——ChatGPT、Claude、豆包、文心一言都是 Decoder-Only
- 扩展性强：参数越大、数据越多、效果越好

---

## 四、Seq2Seq（Encoder-Decoder）

### 代表：T5、BART

### 结构

```text
Encoder（理解输入）
  "I love Python"
    ↓ 编码成向量表示
Decoder（生成输出）
    ↓
  "我 爱 Python"
```

### 特点

- Encoder 负责理解输入，Decoder 负责生成输出
- 天然适合输入和输出是**不同语言/不同形式**的任务
- 翻译、摘要、问答的经典架构

---

## 五、为什么 Decoder-Only 成为主流

| 原因 | 说明 |
|------|------|
| **架构简单统一** | 不需要 Encoder 和 Decoder 分开设计 |
| **天然适合生成** | 对话和创作都是"续写"，Decoder-Only 天然适配 |
| **易于扩展** | 加参数、加数据，效果持续提升（Scaling Law） |
| **训练目标一致** | 预训练和下游任务都是"预测下一个 token" |
| **指令微调友好** | 把所有任务统一成"输入文本 → 续写文本" |

---

## 六、你应该记住的对应关系

```text
你想做分类/检索/匹配 → BERT 路线（Encoder-Only）
你想做对话/生成/创作 → GPT 路线（Decoder-Only）
你想做翻译/摘要     → T5 路线（Encoder-Decoder）

你现在用的所有 AI 对话产品 → Decoder-Only
```

---

## 七、和你的学习路线关系

`★ Insight ─────────────────────────────────────`
- 你不需要手写 Transformer，但你**需要知道不同架构适合什么任务**。以后你调用 LLM API 做 AI Agent 开发，99% 打交道的是 Decoder-Only 模型（GPT、Claude、Qwen）。但如果你要做 RAG 里面的检索环节，Embedding 模型很多基于 BERT 架构。
- 理解 Decoder-Only 的"自回归生成"机制（一次生成一个 token，用刚生成的 token 作为下一次的输入），会帮你理解为什么 LLM 的回复这么慢、为什么有 token 限制、为什么不能中途"改主意"。
`─────────────────────────────────────────────────`
