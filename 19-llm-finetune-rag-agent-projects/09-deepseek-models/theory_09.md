---
aliases:
  - 09-deepseek-models
---
# Day 9：DeepSeek 模型架构

读完约 12 分钟。

---

## 一、DeepSeek 系列概览

| 模型 | 时间 | 特点 |
|------|------|------|
| DeepSeek V1 | 2024 初 | 第一个通用大模型 |
| DeepSeek V2 | 2024 中 | MLA 注意力 + MoE 架构 |
| DeepSeek Math | 2024 | 数学推理专项优化 |
| DeepSeek Coder | 2024 | 代码生成专项 |
| DeepSeek V3 | 2024 末 | 671B MoE，性能接近 GPT-4 |
| DeepSeek R1 | 2025 初 | 强化学习增强推理 |

你现在 API 用的就是 V4 系列（V3/R1 的后续）。

---

## 二、MLA：Multi-head Latent Attention

DeepSeek V2 引入的注意力机制优化。

### 问题

标准 MHA（Multi-Head Attention）中，每个 token 的 KV Cache 占用很大。

```
标准 MHA：每层每个 head 都要存 K 和 V
=> 显存随序列长度线性增长
=> 长上下文时显存爆炸
```

### MLA 的思路

把 Key 和 Value 压缩到低维潜在空间。

```
标准 MHA：K ∈ R^(h×d_k), V ∈ R^(h×d_v)  (h = head 数)
MLA：把 K, V 压缩到 c 维（c << h×d_k）
     K' = W_k × z
     V' = W_v × z  (z 是低维潜在向量)
```

### 效果

- KV Cache 减少 70-80%
- 支持更长上下文
- 推理成本大幅降低

```
你的 DeepSeek API 调用便宜，MLA 是原因之一。
```

---

## 三、MoE：Mixture of Experts

### 核心思想

模型有多个"专家"子网络，每次只激活一部分。

```
输入 → Router（路由器） → Top-2 专家 → 合并输出
                 ↑              ↑
            判断交给谁      只激活最相关的 2 个
```

### 类比

```
传统大模型：一个超级全能的工程师做所有事
MoE：一个项目经理 + 100 个专项专家
     每次只找最擅长的 2 个专家来干活
```

### DeepSeek V3 的 MoE

- 总参数：671B
- 每次激活：37B（约 5.5%）
- 专家数量：256 个路由专家 + 1 个共享专家
- 负载均衡：确保每个专家都被均匀使用

### 为什么 MoE 重要

```
总参数大 → 模型容量大（记住的知识多）
激活参数少 → 推理快、成本低

这就是 DeepSeek 能以更低价格提供接近 GPT-4 性能的原因。
```

---

## 四、DeepSeek R1：强化学习增强推理

### 与 V3 的区别

```
DeepSeek V3：通用对话，快速响应
DeepSeek R1：强化推理，展示思考过程

R1 会在回答前输出一段"思考过程"（类似于 CoT 的内部版本）。
```

### R1 的训练方式

```
基础模型（V3）
    ↓
SFT（监督微调）：用人类标注的推理数据训练
    ↓
RL（强化学习）：用 GRPO 算法优化推理路径
    ↓
R1：推理增强模型
```

---

## 五、对你实际的影响

```text
你现在用 DeepSeek API 时：

选择 deepseek-chat → 对应 V4 通用模型（快速、便宜）
如果未来有 deepseek-reasoning → 对应推理增强版（更准、稍慢）

MLA → API 便宜的原因
MoE → 671B 参数但单卡能跑的原因
R1 → 推理能力强的技术基础

知道这些不是为了理解架构细节，
而是为了做技术选型时有依据：
"为什么选 DeepSeek 而不是其他？"
```
