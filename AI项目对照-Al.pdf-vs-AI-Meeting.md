---
aliases:
  - AI项目对照-Al.pdf-vs-AI-Meeting
---
# AI 项目对照：Al.pdf vs AI-Meeting

> 目的：搞清楚这两份资料的 AI 项目各自讲什么、什么关系、怎么用

---

## 一、两个项目概览

| 维度 | Al.pdf 的 AI 项目 | AI-Meeting（GitHub） |
|------|------------------|---------------------|
| **项目名称** | 智能问答知识库系统 | 码上面试平台 |
| **核心场景** | 团队内部知识库问答 | AI 模拟面试 |
| **技术栈** | Java + Redis + Pinecone + Qwen-Plus | Java 17 + Spring Boot 3 + Spring AI + MySQL + MongoDB + Redis + 讯飞 |
| **AI 能力** | RAG 检索增强生成、短期/长期记忆 | 5 Agent 协同面试、SSE 流式对话、语音转写 |
| **定位** | PDF 教程里的"教你做一个 AI 项目" | GitHub 上完整的开源项目 |
| **代码状态** | Java 代码片段（LongTermMemoryManager 等） | 完整可运行的 Spring Boot 项目 |
| **向量数据库** | Pinecone（云服务，方便托管） | 星云工作流（扣子生态） |
| **大模型** | Qwen-Plus | 多模型统一接入（DeepSeek/星火/豆包） |

---

## 二、逐项对比

### 1. 记忆系统

| | Al.pdf | AI-Meeting |
|------|--------|-----------|
| **短期记忆** | 滑动窗口 + 摘要压缩 + Redis | MongoDB 会话消息持久化 + Redis |
| **长期记忆** | 结构化存储（Redis）+ 向量存储（Pinecone），双通道召回 | 未单独实现（Agent 配置代替） |
| **设计思路** | "先召回长期记忆 → 拼接短期上下文 → 检索 RAG → 组成 Prompt" | "面试状态序列化快照 → Redis 懒加载恢复" |
| **复杂度** | 较高（作者自己说"代码写得太复杂"） | 中等（会话状态治理是核心复杂度） |

**关键区别**：Al.pdf 讲的是"怎么做记忆"的通用方案，AI-Meeting 做的是"面试这个特定场景下的状态管理"。

### 2. RAG 知识库

| | Al.pdf | AI-Meeting |
|------|--------|-----------|
| **检索方式** | BM25 + 向量混合检索 | 星云工作流内置知识库 |
| **向量数据库** | Pinecone | 未独立使用（依赖扣子生态） |
| **Embedding** | 对比了不同Embedding模型 | 未暴露 |
| **Query优化** | Query Rewriting（上下文聚合+改写） | — |
| **评测** | 自建测试问题集 + 精确率/召回率 | — |

**关键区别**：Al.pdf 讲的是"RAG 怎么从头搭"，AI-Meeting 用现成的平台能力。Al.pdf 对 RAG 原理的讲解更深。

### 3. Agent 多智能体

| | Al.pdf | AI-Meeting |
|------|--------|-----------|
| **Agent 数量** | 未涉及多Agent | **5 个 Agent 协同**（出题官/提问官/评分官/追问官/表情分析） |
| **编排方式** | — | LiteFlow 规则链 + EnumMap 状态机 |
| **面试话术** | 有"怎么理解 Agent"的八股回答 | 真实的 Agent 协同代码 |

**关键区别**：Al.pdf 讲了"Agent 是什么"，AI-Meeting **做了**多 Agent 协同。这是互补关系——一个教你说，一个让你看代码。

### 4. Function Calling / MCP

| | Al.pdf | AI-Meeting |
|------|--------|-----------|
| **Function Calling** | 有面试回答（八股） | 未显式使用（通过扣子工作流间接实现） |
| **MCP** | 有面试回答 + 链路流程 | 未涉及 |

**关键区别**：Al.pdf 帮你准备面试会被问到的概念，AI-Meeting 没碰这些。

### 5. AI Code Review

| | Al.pdf | AI-Meeting |
|------|--------|-----------|
| **CR Prompt** | **完整的 AI CR 规则 + 输出模板**（第12-18页） | 未涉及 |
| **单元测试生成** | **完整的 JUnit 5 + Mockito 规则**（第20-30页） | 未涉及 |
| **覆盖率校验** | 80%/75%/100% 标准 + 分析报告模板 | 未涉及 |

**Al.pdf 独有，且非常实用。** 这两个 Prompt 模板可以直接复制到 Cursor Rules 使用。

---

## 三、它们的关系：不是竞争，是互补

```
Al.pdf 教你"怎么说"                    AI-Meeting 让你看"怎么做"
─────────────────                    ────────────────
RAG 原理 + 实现思路                   多 Agent 协同面试代码
缓存/秒杀 项目话术                    简历写法的实际案例
Function Calling/MCP 八股             分布式 Single-flight
AI CR Prompt 模板                     SSE 流式输出 + 语音转写
单元测试生成规则                      长会话状态治理
```

### 具体互补场景

| 你要做的事 | 先看哪个 | 再看哪个 |
|-----------|---------|---------|
| 理解 RAG 怎么搭 | Al.pdf（原理+方案对比） | AI-Meeting（看扣子平台怎么用） |
| 理解 Agent 怎么协同 | Al.pdf（八股：怎么理解Agent） | AI-Meeting（5个Agent的实际代码） |
| 面试讲"我怎么做AI项目" | Al.pdf（话术框架） | AI-Meeting（拿它的功能点当素材） |
| 日常开发提效 | Al.pdf（AI CR + 单测 Prompt） | — |
| 简历怎么写AI项目 | Al.pdf（项目描述模板） | AI-Meeting（README 里有简历写法示例） |

---

## 四、对你现在的实际价值排序

| 优先级 | 内容 | 来自 | 怎么用 |
|--------|------|------|--------|
| **1** | AI CR Prompt 模板 | Al.pdf 第12-18页 | 直接复制到 Cursor Rules，每天开发都在用 |
| **2** | 单元测试生成规则 | Al.pdf 第20-30页 | 苍穹外卖的 Service 用这个生成单测 |
| **3** | 面试话术框架（背景→问题→方案→复盘） | Al.pdf 第13-20页 | 套到苍穹外卖和AI-Meeting上练习 |
| **4** | RAG 原理理解 | Al.pdf 第60-90页 | 读一遍，和 18-llm-coze-workflow 的知识库部分对照 |
| **5** | AI-Meeting 架构分析 | GitHub 项目 | 暑假研究它怎么编排 5 个 Agent |
| **6** | Agent/Function Calling/MCP 八股 | Al.pdf 第232-233页 | 面试前翻出来看 |

---

## 五、一句话总结

> **Al.pdf 教你"面试时怎么讲 AI 项目"，AI-Meeting 让你看"一个真实的 AI 项目长什么样"。两个一起用：用 Al.pdf 的话术框架去讲 AI-Meeting 的功能点。**
