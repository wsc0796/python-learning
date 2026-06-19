---
aliases:
  - 01-prompt-tuning-basic
---
# Day 1：Prompt-Tuning 基础

读完约 15 分钟。

---

## 一、NL 任务四范式

NLP 的发展经历了四个阶段：

```
① 特征工程范式
   人工设计特征（词频、TF-IDF、词性）→ 分类器

② 预训练 + 微调范式
   BERT/RoBERTa/GPT 预训练 → 下游任务微调整个模型

③ 预训练 + Prompt 范式
   不修改模型，把任务改写成"填空"形式

④ 大模型 + 指令/上下文学习范式
   靠 Prompt + 示例 + 工具调用完成任务，不重新训练
```

你现在用的 DeepSeek API 就属于第四范式。

### 几种范式的对比

| 范式 | 代表 | 需要训练？ | 成本 |
|------|------|-----------|------|
| 特征工程 | SVM + TF-IDF | 是（分类器） | 低 |
| 微调 | BERT Fine-Tune | 是（整个模型） | 高 |
| Prompt | PET / P-Tuning | 可选（少量参数） | 中低 |
| 指令学习 | GPT / DeepSeek | 否（靠 Prompt） | 最低 |

---

## 二、Fine-Tuning 回顾

Fine-Tuning（微调）是在预训练模型基础上，用下游任务数据继续训练。

### 流程

```
加载预训练模型 → 准备下游数据 → 添加任务头 → 训练 → 部署
```

### 问题

| 问题 | 说明 |
|------|------|
| 训练成本高 | 大模型参数多，显存和计算成本高 |
| 存储成本高 | 每个任务可能保存一份完整模型 |
| 灾难性遗忘 | 模型可能遗忘原有能力 |
| 迁移不灵活 | 每个任务都需要重新训练 |

这就是 Prompt-Tuning 出现的原因——**能不能不改变模型参数，只改输入？**

---

## 三、Prompt-Tuning 基本原理

核心思想：不修改模型参数，通过设计或学习 Prompt，让模型完成下游任务。

Prompt 分两类：

| 类型 | 形式 | 是否可读 | 是否训练 |
|------|------|---------|---------|
| **Hard Prompt** | 人工写的文本提示词 | 可读 | 不训练 |
| **Soft Prompt** | 可训练的连续向量 | 不可读 | 可训练 |

### Hard Prompt 例子

```python
# 传统分类器需要训练
# Prompt 方式：直接问
prompt = "这句话的情感是正面还是负面？\n这句话：{}"
```

### Soft Prompt 思路

```
不写文本提示词，而是在 embedding 层加一组可训练向量。
模型主体冻结，只训练这组向量。
```

---

## 四、PET：Pattern-Exploiting Training

PET 把分类任务转成"完形填空"。

### 原理

```
原句：这家餐厅味道很好。

Pattern（模板）：
这家餐厅味道很好。总体来说，它是 [MASK] 的。

Verbalizer（标签词映射）：
正面 → "好"
负面 → "差"
```

### 为什么这样有效

BERT 在预训练时做过大量完形填空（Masked LM），
"它是 [MASK] 的" 这种句式对 BERT 来说很"自然"。

### 代码理解

```python
# 传统分类
# 输入：文本 → BERT → [CLS] → 分类头 → 正面/负面

# PET 分类
# 输入："...它是 [MASK] 的" → BERT → 预测[MASK]位置的词 → 查 Verbalizer
```

---

## 五、Soft Prompt 与 P-Tuning

### Soft Prompt

```
Hard Prompt：
  "这句话的情感是：[MASK]"

Soft Prompt：
  [v1] [v2] [v3] [v4] [v5] 这句话的情感是：[MASK]
   ↑ 可训练的连续向量，不是文字
```

### P-Tuning

P-Tuning 用一个小型网络（LSTM/MLP）生成 Soft Prompt，
比直接训练更稳定。

### 发展脉络

```
人工 Prompt
    ↓
PET：模板 + 标签词映射
    ↓
Soft Prompt：连续向量
    ↓
Prefix-Tuning：每层加前缀
    ↓
P-Tuning v2：深度 Prompt
```

---

## 六、本章重点

```
Fine-Tuning：改模型 → 效果好但贵
Prompt-Tuning：改输入 → 便宜但依赖设计
PET：把分类变成填空
Soft Prompt：可训练的连续向量
P-Tuning：用网络生成 Prompt
```
