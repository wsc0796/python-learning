---
aliases:
  - 18-llm-coze-workflow
---
# 大模型应用开发：扣子工作流 + LLM 基础

> 前置：Python 基础已覆盖、会用 API 的基本概念、对 AI Agent 方向有兴趣
> 目标：能用扣子搭建 AI 工作流 + 理解大模型基本原理 + 跑通本地 LLM 应用
> 用时：约 7 天（每天 40-50 分钟）

---

## 本专题分两大部分

| 部分 | 内容 | 目标 |
|------|------|------|
| Part 1（01-09） | 扣子平台与工作流实战 | 能独立搭建 AI 工作流，完成行业场景项目 |
| Part 2（10-14） | 大模型基础原理与应用 | 理解 LLM 怎么工作的，能用 Ollama 跑本地模型 |

```
扣子工作流（01-09）          大模型基础（10-14）
      │                            │
      ├── 动手做 AI 应用            ├── 理解 AI 怎么工作的
      ├── 零代码/低代码             ├── 有理论基础
      └── 行业项目实战              └── 本地部署实践
                  ↘            ↙
                   AI Agent 开发
              （Hello-Agents 承接）
```

## 核心认知

**你不一定要训练大模型。** 更现实的 AI 参与方式：
1. 学会用大模型 → 2. 学会设计 Prompt → 3. 学会搭建工作流 → 4. 结合行业场景做应用

## 7 天学习计划

| 天 | 内容 | 产出 |
|----|------|------|
| 1 | [[01-ai-trend-and-coze-basic]] + [[02-coze-core-concepts]] | 注册账号，理解平台架构 |
| 2 | [[03-workflow-basic-nodes]] + [[04-coze-platform-setup]] | 搭建第一个简单工作流 |
| 3 | [[05-workflow-entry-practice]] | 跑通完整工作流 + 调试 |
| 4 | [[06-advanced-workflow-nodes]] + [[07-workflow-advanced-integration]] | 掌握代码块/分支/循环 |
| 5 | [[08-industry-cases]] + [[09-workflow-projects]] | 完成一个行业项目 |
| 6 | [[10-llm-basic-introduction]] + [[11-llm-architecture]] + [[12-chatgpt-principle]] | 建立 LLM 理论框架 |
| 7 | [[13-open-source-llm]] + [[14-llm-application-practice]] | 跑通本地大模型应用 |

## 学完后的能力

- 在扣子平台独立搭建多节点工作流
- 理解变量、JSON、节点间的数据传递
- 能设计自媒体/办公/客服/电商场景的 AI 工作流
- 理解 LLM、N-Gram、Decoder-Only 等核心概念
- 了解 GPT/ChatGPT 的发展脉络和 RLHF
- 用 Ollama 在本地运行开源模型
- 为 Hello-Agents 和 AI Agent 开发打好基础

## 相关笔记

- [[17-context-iterator-async]] — 异步编程（Agent 并发调用的基础）
- [[10-fastapi]] — 把工作流变成 API 服务
- [[07-pydantic]] — 结构化数据校验
