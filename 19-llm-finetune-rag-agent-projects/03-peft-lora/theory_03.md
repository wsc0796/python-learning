---
aliases:
  - 03-peft-lora
---
# Day 3：PEFT、Prefix-Tuning、Adapter、LoRA

读完约 15 分钟。

---

## 一、PEFT 概念

PEFT = Parameter-Efficient Fine-Tuning（参数高效微调）。

### 核心思想

```
冻结大模型大部分参数，只训练少量新增参数或低秩参数。
```

### 为什么需要 PEFT

| 问题 | 传统 Fine-Tuning | PEFT |
|------|-----------------|------|
| 参数量 | 175B 全训练 | 只训练几百万 |
| 显存 | 多卡才能跑 | 单卡能跑 |
| 存储 | 每个任务一个完整模型 | 只存小权重文件 |
| 切换任务 | 重新加载模型 | 换权重文件即可 |

---

## 二、Prefix-Tuning

在 Transformer 每一层的 Key 和 Value 前加一段可训练前缀向量。

### 直观理解

```
传统 Transformer 的 Attention：
Q × [K | V]  ← 只有序列本身的 K 和 V

Prefix-Tuning：
Q × [Prefix_K | Prefix_V | K | V]
      ↑ 可训练的前缀向量
```

### 特点

- 冻结模型主体
- 只训练 Prefix 参数（约占总参数的 0.1%-1%）
- 对生成任务效果较好
- 不同任务可以有不同的 Prefix

---

## 三、Adapter-Tuning

在每个 Transformer 层中插入小型神经网络（Adapter）。

### 结构

```
Transformer Layer
    ↓
Self-Attention
    ↓
Adapter → 先降维 → 非线性激活 → 再升维
    ↓
Feed Forward
    ↓
Adapter → 先降维 → 非线性激活 → 再升维
```

### 特点

- 模型主体冻结
- 每个任务对应一个 Adapter（可以插拔）
- 适合多任务场景
- 会增加推理延迟（多了两层计算）

---

## 四、LoRA（最常用）

LoRA = Low-Rank Adaptation（低秩适配）。

### 核心思想

不直接更新原始权重矩阵 W，而是用两个小矩阵的乘积来近似更新量。

```
原始权重 W ∈ R^(d×k)  冻结，不更新
低秩分解：
  A ∈ R^(d×r)    小矩阵，随机初始化
  B ∈ R^(r×k)    小矩阵，零初始化
  r << min(d, k)  秩，通常取 4-64

实际前向传播：
  h = Wx + BAx
        ↑ LoRA 的增量
```

### 为什么 LoRA 有效

```
大模型的权重矩阵往往是低秩的（存在大量冗余）。
只需要在低维子空间上调整，就能有效改变模型行为。
```

### LoRA 配置参数

| 参数 | 含义 | 典型值 |
|------|------|--------|
| r | 秩，越大代表学习能力越强 | 8, 16, 32 |
| lora_alpha | 缩放系数 | 16, 32 |
| lora_dropout | 防止过拟合 | 0.05, 0.1 |
| target_modules | 对哪些层加 LoRA | q_proj, v_proj |

---

## 五、方法对比

| 方法 | 额外参数位置 | 是否改模型结构 | 训练参数量 | 推理延迟 |
|------|-------------|--------------|-----------|---------|
| Fine-Tuning | 全部参数 | 否 | 100% | 不变 |
| Prefix-Tuning | 每层 K/V 前 | 否 | ~0.1% | 微增 |
| Adapter | 每层中间 | 是 | ~1% | 增加 |
| LoRA | 权重旁路 | 否 | ~0.1% | 不变 |

**实际中最常用的是 LoRA**——效果好、速度快、存储小。

### 你现在已经在用 LoRA

你电脑里的 `hello-agents/` 项目代码中，
如果用到了 HuggingFace PEFT 库，底层就是 LoRA。

```python
from peft import LoraConfig, get_peft_model

lora_config = LoraConfig(
    r=8,
    lora_alpha=32,
    target_modules=["q_proj", "v_proj"],
    lora_dropout=0.1,
)
model = get_peft_model(base_model, lora_config)
```
