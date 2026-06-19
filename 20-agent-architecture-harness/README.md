# 20-agent-architecture-harness

目标：把 `hello-agents` 学成 Agent 架构能力，再迁移到 AI-Meeting 和 Codex/Claude Code harness。

---

## 学习原则

- 不死扣缺失源码。
- 每章只抓输入、输出、模块职责、状态、工具、记忆、配置、评估。
- 每章必须画一张图。
- 每章必须写 150 字复述。
- 每章必须写一个和 AI-Meeting 或 AI_HANDOFF 的对应关系。

---

## 推荐顺序

| 顺序  | 内容       | 本地文件                                            | 产物                       |
| --- | -------- | ----------------------------------------------- | ------------------------ |
| 1   | Agent 基础 | `hello-agents/docs/chapter1/第一章 初识智能体.md`       | Agent 基础架构图              |
| 2   | 经典范式     | `hello-agents/docs/chapter4/第四章 智能体经典范式构建.md`   | ReAct/Plan/Reflection 对比 |
| 3   | Agent 框架 | `hello-agents/docs/chapter7/第七章 构建你的Agent框架.md` | Agent 框架模块图              |
| 4   | 记忆与检索    | `hello-agents/docs/chapter8/第八章 记忆与检索.md`       | Memory/RAG 分工图           |
| 5   | 上下文工程    | `hello-agents/docs/chapter9/第九章 上下文工程.md`       | Context 构建图              |
| 6   | 通信协议     | `hello-agents/docs/chapter10/第十章 智能体通信协议.md`    | MCP/A2A/ANP 对比           |
| 7   | 性能评估     | `hello-agents/docs/chapter12/第十二章 智能体性能评估.md`   | Agent 评估指标表              |
| 8   | 综合案例     | chapter13 或 chapter14                           | 完整应用流程图                  |

---

## 固定 Prompt

```text
用 hello-agents-architecture-coach 学习 <章节路径>。
不要死扣源码。
请按：这一章解决什么、核心模块、输入输出、Mermaid 工作流、关键设计点、不要死扣的代码、真正要理解的伪代码、和 AI-Meeting 的对应、和 Codex/Claude Code harness 的对应、面试讲法、今日练习 来教我。
```

---

## 文件索引

| 文件 | 内容 |
|------|------|
| `01-hello-agents-agent-overview.md` | 第 1 章 Agent 基础架构笔记 |
| `02-react-plan-reflection.md` | 第 4 章 ReAct / Plan-and-Solve / Reflection 对比 |
