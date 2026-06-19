---
aliases:
  - 19-llm-finetune-rag-agent-projects
---
# 大模型进阶应用：微调、RAG、Agent 与综合项目

> 前置：[[18-llm-coze-workflow]] + Python 基础 + 会用 API 调模型
> 目标：掌握 Prompt-Tuning、LoRA 微调、Function Call、Agent、RAG、LangChain，能做综合项目
> 用时：约 12 天（每天 40-60 分钟）

---

## 本专题学什么

```
Part 1：微调与提示词（01-03）
  Prompt-Tuning → P-Tuning → LoRA
         ↓
Part 2：开发与应用（04-10）
  Function Call → Agent → RAG → LangChain
         ↓
Part 3：综合项目（11-12）
  物流 RAG 系统 → 评论智能分类系统
```

## 和已有内容的关系

| 前置 | 这里 | 后续 |
|------|------|------|
| [[18-llm-coze-workflow]]（AI 应用基础） | **19 进阶技术原理 + 实现** | 可以自己做项目 |
| `document_pipeline/`（管道模式） | Agent / RAG 用到同一种编排思想 | 整合成完整应用 |
| `hello-agents/`（Datawhale 教程） | 参考其中的 Agent 架构和代码 | 精读对应章节 |

## 12 天计划

| 天 | 内容 | 产出 |
|----|------|------|
| 1 | Prompt-Tuning 基础 + PET | 跑通分类 Prompt 模板 |
| 2 | 进阶提示方法（CoT/ICL） | 写 Zero-shot/Few-shot/CoT |
| 3 | PEFT + LoRA 原理 | 理解为什么 LoRA 最常用 |
| 4 | Function Call | 实现天气/数据库查询函数 |
| 5 | AI Agent 基础 | 理解 Agent 架构 + 邮件案例 |
| 6 | RAG 系统 + Milvus | 画 RAG 流程图 + 理解向量库 |
| 7 | RAG 优化与评估 | 知道优化方向和评估指标 |
| 8 | 扩展知识 | Flash Attention / BM25 |
| 9 | DeepSeek 模型架构 | MLA / MoE |
| 10 | LangChain 基础 | 理解 Chain / RAG / Agent 标准化 |
| 11 | 项目：物流 RAG 系统 | 意图分类 + NL2SQL + 向量检索 |
| 12 | 项目：评论分类与信息抽取 | ChatGLM+LoRA + 联合抽取 + 部署 |

---

## 目录

- [[#01 Prompt-Tuning 基础]]
- [[#02 提示词工程进阶]]
- [[#03 PEFT / Prefix-Tuning / Adapter / LoRA]]
- [[#04 Function Call]]
- [[#05 AI Agent 基础]]
- [[#06 RAG 系统与 Milvus]]
- [[#07 RAG 优化与评估]]
- [[#08 大模型知识扩展]]
- [[#09 DeepSeek 模型]]
- [[#10 LangChain 基础]]
- [[#11 项目：物流 RAG 系统]]
- [[#12 项目：评论分类与信息抽取]]
