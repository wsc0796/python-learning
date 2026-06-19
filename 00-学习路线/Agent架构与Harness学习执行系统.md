# Agent 架构与 Harness 学习执行系统

生成日期：2026-06-08

目标：把 `hello-agents`、AI-Meeting、Claude Code/Codex、AI_HANDOFF 串成一套可执行的学习系统。

---

## 总结论

你现在不需要继续死扣 `hello-agents` 的每个源码类。

正确定位：

- `hello-agents`：Agent 架构认知课。
- AI-Meeting：真实业务项目，用来理解 Agent 在 Java/Spring 项目里的落地。
- Claude Code / Codex harness：真实工程执行系统，用来学习 AI 如何读项目、改代码、跑测试、写 review。
- AI_HANDOFF：你控制 AI 的施工图，防止它乱改，也防止你看不懂。

一句话：

> hello-agents 负责建立 Agent 脑图，AI_HANDOFF + Codex/Claude Code 负责训练真实工程执行能力。

---

## 你需要具备的条件

最低条件：

- Python 基础：函数、类、字典、列表、文件读写。
- 会用 Git 基本命令。
- 能看懂 Markdown 和 Mermaid 流程图。
- 能跑 Python 项目或至少能读 Python 项目结构。
- 能用 Codex/Claude/GPT 辅助理解，但保留自己的判断。

不要求：

- 不要求深度学习训练。
- 不要求精通 LangGraph。
- 不要求看懂 hello-agents 所有源码。
- 不要求现在掌握 Agentic-RL。
- 不要求自己实现企业级多 Agent 平台。

---

## 已经为你准备好的内容

### 1. HelloAgents 架构学习 Skill

路径：

`C:\Users\50469\.codex\skills\hello-agents-architecture-coach\SKILL.md`

触发方式：

```text
用 hello-agents-architecture-coach 讲第 4 章，不要死扣源码，按输入输出、模块职责、流程图、AI-Meeting 对应关系来教我。
```

它会强制输出：

- 这一章解决什么。
- 核心模块表。
- Mermaid 工作流。
- 关键设计点。
- 不要死扣的代码。
- 真正要理解的伪代码。
- 和 AI-Meeting 的对应。
- 和 Codex/Claude Code harness 的对应。
- 面试讲法。
- 今日练习。

### 2. HelloAgents 架构笔记模板

路径：

`C:\Users\50469\python-learning\Templates\HelloAgents架构笔记模板.md`

用途：

- 每学一章复制一份。
- 只填架构、输入输出、流程图、面试讲法。
- 不记录大段源码。

### 3. AI_HANDOFF 四文件模板

路径：

`C:\Users\50469\python-learning\Templates\AI_HANDOFF`

四个文件：

```text
01_REQUIREMENT.md
02_PLAN.md
03_CODEX_TASK.md
04_REVIEW.md
```

用途：

- GPT/Claude 负责需求和方案。
- 你确认业务、边界、能不能解释。
- Codex 按任务单执行。
- 04_REVIEW 保存证据、测试和面试复述。

### 4. GPT 到 Codex Handoff Skill

路径：

`C:\Users\50469\.codex\skills\gpt-codex-handoff-loop\SKILL.md`

用途：

- 当你说“把 GPT 方案变成 Codex 任务单”时使用。
- 当你说“按 AI_HANDOFF/03_CODEX_TASK.md 执行”时使用。

---

## 学习顺序

### Phase 1：hello-agents 架构入门

用时：3-5 天。

只学这些：

| 章节 | 学习目标 | 产物 |
|------|----------|------|
| 第 1 章 初识智能体 | 知道 Agent 是什么 | Agent 定义图 |
| 第 4 章 经典范式 | ReAct / Plan / Reflection | 三种范式对比表 |
| 第 7 章 构建 Agent 框架 | 看 Agent 系统怎么拆模块 | 框架模块图 |
| 第 8 章 记忆与检索 | Memory / RAG 分工 | Memory-RAG 流程图 |
| 第 9 章 上下文工程 | Context 怎么组织 | Context 构建图 |
| 第 12 章 评估 | Agent 怎么判断好坏 | 评估指标表 |

跳过或低优先级：

- 第 5 章低代码平台按钮级教程。
- 第 11 章 Agentic-RL。
- 第 15 章大型模拟项目。
- 缺源码的类定义。

每天产物：

- 1 张图。
- 1 个模块表。
- 150 字复述。
- 1 个和 AI-Meeting 的对应点。

### Phase 2：AI-Meeting 对照

用时：3-5 天。

目标：把 hello-agents 的架构概念套到 AI-Meeting。

重点问题：

- AI-Meeting 里的出题、评分、追问 Agent 分别像 hello-agents 的哪个模块？
- 面试会话状态相当于 Agent 的哪种 memory/context？
- Redis、MongoDB、MySQL 分别保存什么？
- SSE 和 WebSocket 分别服务哪个实时输出场景？
- LiteFlow 是不是某种规则化 planner / evaluator？

产物：

- `AI-Meeting Agent 对照图`
- `出题/评分/追问 Agent 模块表`
- `状态机 + Memory + RAG 区分说明`

### Phase 3：AI_HANDOFF 工程执行

用时：1 周。

目标：把 AI 辅助编码流程固定下来。

练习 3 个小任务：

1. 只写文档：整理一个接口链路说明。
2. 补测试：给一个 Service 或状态校验补测试。
3. 小修复：修一个字段兼容、错误提示或边界校验。

每个任务都必须走：

```text
01_REQUIREMENT.md
02_PLAN.md
03_CODEX_TASK.md
04_REVIEW.md
```

验收标准：

- 你能说清需求。
- 你能说清允许改什么。
- Codex 没有乱改无关文件。
- 有验证命令。
- 04_REVIEW 能直接变成面试复述。

### Phase 4：Harness 型 Agent 学习

用时：1-2 周。

目标：理解 Codex/Claude Code 这类 coding-agent harness 为什么比单纯 LangGraph 状态图更贴近工程。

学习主题：

| 主题 | 你要理解什么 |
|------|--------------|
| AGENTS.md / CLAUDE.md | 项目级上下文和规则注入 |
| Skills | 可复用工作流 |
| Slash Commands | 手动触发的固定任务 |
| Hooks | 自动检查、自动格式化、阻断危险操作 |
| Subagents | 拆分搜索、审计、测试等上下文 |
| MCP | 外部工具和数据源接入 |
| AI_HANDOFF | 需求到执行的施工图 |
| Tests / Review | harness 的质量闸门 |

最终产物：

- 一个你自己的 `AI_HANDOFF` 工作流样例。
- 一个 `hello-agents` 架构学习笔记。
- 一个小 Agent Demo 或 AI-Meeting 小修复。
- 一段可写进简历的真实表述。

---

## 每次学习的固定 Prompt

学 hello-agents：

```text
用 hello-agents-architecture-coach 学习 C:\Users\50469\github-projects\hello-agents\docs\chapterX\xxx.md。
不要死扣源码。
请按：这一章解决什么、核心模块、输入输出、Mermaid 工作流、关键设计点、不要死扣的代码、真正要理解的伪代码、和 AI-Meeting 的对应、和 Codex/Claude Code harness 的对应、面试讲法、今日练习 来教我。
```

把 GPT 方案交给 Codex：

```text
使用 gpt-codex-handoff-loop。
请把当前方案整理成 AI_HANDOFF/03_CODEX_TASK.md。
要求包含目标、背景、允许修改范围、禁止修改范围、架构边界、业务规则、伪代码、验证命令、验收标准、停止条件。
```

让 Codex 执行：

```text
使用 gpt-codex-handoff-loop。
按 AI_HANDOFF/03_CODEX_TASK.md 执行。
先读项目上下文和现有代码。
不要超出允许修改范围。
改完后运行测试，并写 AI_HANDOFF/04_REVIEW.md。
```

---

## 你的简历转化路径

第 1 层：只学过 hello-agents

```text
系统学习 Agent 应用架构，理解 ReAct、Plan-and-Solve、Reflection、Memory、RAG、上下文工程和评估机制。
```

第 2 层：做了架构笔记和对照

```text
基于 hello-agents 梳理 Agent 系统模块设计，并对照 AI-Meeting 的出题、评分、追问链路输出架构图和模块职责表。
```

第 3 层：完成 AI_HANDOFF + Codex 小任务

```text
构建 GPT/Claude 到 Codex 的 AI_HANDOFF 工作流，沉淀需求、方案、任务单和复盘模板，并用于项目局部测试/文档/小修复验证。
```

第 4 层：做出小 Demo

```text
基于 Python 实现一个带工具调用/记忆/检索的小型 Agent Demo，并记录输入输出、状态流、异常处理和评估方式。
```

不要写：

- 精通多智能体系统。
- 主导设计 Agent 框架。
- 深度掌握 Agentic-RL。
- 完整实现企业级 AI Agent 平台。

---

## 判断是否学到位

你能回答这些问题，就算学到位：

- Agent 和普通 ChatBot 的区别是什么？
- ReAct 的 Action / Observation 是什么？
- Plan-and-Solve 为什么适合复杂任务？
- Reflection 解决什么问题？
- Memory 和 RAG 有什么区别？
- Context Engineering 为什么重要？
- Tool Calling 的输入输出怎么设计？
- Config 系统为什么不能散落在代码里？
- Agent 怎么评估？
- AI-Meeting 里的出题、评分、追问怎么对应 Agent 模块？
- Codex/Claude Code 这种 coding agent 为什么需要规则、任务单、测试和 review？

---

## 现在立刻开始

今天第一步：

```text
用 hello-agents-architecture-coach 学习 C:\Users\50469\github-projects\hello-agents\docs\chapter1\第一章 初识智能体.md。
不要死扣源码。
请输出模块职责、输入输出、流程图、AI-Meeting 对应关系和 150 字面试讲法。
```

今天产物：

- 一张 Agent 基础架构图。
- 一份 `HelloAgents架构笔记模板` 填写版。
- 150 字复述：Agent 到底是什么。

