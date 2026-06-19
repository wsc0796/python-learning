---
date: 2026-06-10
project: Agentic Internship Coach
phase: 9
status: AI 已实现，里程碑 3 完成
---

# Phase 9 配套学习页 —— 受控 Function Call / ReAct Agent

## 本 Phase 做了什么

实现了一个能调用工具的 ReAct Agent。用户说"我想投岗位1，该怎么准备？"，Agent 自动调工具查岗位要求、查简历技能、搜学习笔记，最后生成学习计划。

```
POST /api/v1/agent/chat
{
  "job_id": 1, "resume_id": 1,
  "message": "我该怎么准备？",
  "create_tasks": false
}
→ Agent 自动调用 get_job_requirements → get_resume_skills → 生成回答
→ {answer, iterations, tools_called, created_task_ids}
```

---

## 核心概念

### 1. ReAct 循环（Reasoning + Acting）

```
第 1 轮: LLM 思考 → "我需要先看岗位要求" → 调 get_job_requirements(1)
         系统执行工具 → 返回 {title: "后端", requirements: "Python..."}
         
第 2 轮: LLM 思考 → "岗位要Python，我看看你的简历" → 调 get_resume_skills(1)
         系统执行工具 → 返回 {skills: "Python, FastAPI"}

第 3 轮: LLM 思考 → "匹配度蛮高的，但岗位还要Docker，建议学习"
         → 返回 Final Answer
```

**ReAct = Reason + Act。** LLM 不是一次性回答，而是边想边做——想一下 → 调工具 → 看结果 → 再想 → 再调工具 → 直到有足够信息回答。

### 2. 工具白名单

```python
TOOLS = {
    "get_job_requirements": ToolSpec(
        description="获取岗位技能要求",
        args_model=GetJobRequirementsArgs,  # Pydantic 校验: job_id 必须是 int
        function=get_job_requirements,      # 实际执行的函数
    ),
    ...
}
```

每个工具有三个要素：
- **description** — 告诉 LLM 这个工具干什么
- **args_model** — 用 Pydantic 校验参数（LLM 可能传错类型）
- **function** — 实际执行的 Python 函数

### 3. 安全约束

```python
# ① 工具名必须在白名单
if tool_name not in tools:
    → "Unknown tool"  # LLM 想调"delete_all_data"？拒绝

# ② 参数必须通过 Pydantic 校验
validated_args = args_model.model_validate(args)

# ③ create_tasks=false 时不注册写入工具
if create_tasks:
    tools["create_study_task"] = ...  # 只有这个开关打开才注册

# ④ 重复调相同工具+参数 2 次 → 停止
if call_history.count((tool_name, args_json)) >= 2:
    → "检测到重复调用，已停止"

# ⑤ 最大迭代数
max_iterations = 5  # 防止无限循环
```

**Agent 安全的第一原则：永远不要完全信任 LLM 的输出。** 每个工具调用都要校验——工具名、参数类型、重复次数、副作用开关。

### 4. JSON 输出格式 vs 自由文本解析

```
❌ 自由文本解析（容易出错）:
"Thought: I need job info
Action: get_job_requirements
Action Input: job_id=1"
→ 需要写正则解析 → 模型换一种写法就挂了

✅ JSON 格式（Pydantic 校验）:
{"type": "tool_call", "tool": "get_job_requirements", "arguments": {"job_id": 1}}
→ json.loads → ToolCallOutput.model_validate → 一行搞定
```

### 5. FakeLLM 测试

```python
# 第 1 次调用 → 返回 tool_call
# 第 2 次调用 → 返回 final_answer
responses = [TOOL_CALL_JSON, FINAL_ANSWER_JSON]

with patch("src.agent.react_loop.chat_completion", side_effect=responses):
    resp = client.post("/api/v1/agent/chat", ...)
    assert "get_job_requirements" in resp.json()["tools_called"]
```

**FakeLLM 的好处：** 不调真实 API、可精确控制返回顺序、可以模拟异常路径。

---

## Agent 架构全景图

```
POST /api/v1/agent/chat
        │
        ▼
agent_router.py
  ├── 校验 job_id, resume_id, message
  ├── _build_tools(db, create_tasks)
  │     ├── get_job_requirements → SqlAlchemyJobRepository
  │     ├── get_resume_skills → SqlAlchemyResumeRepository
  │     ├── search_learning_notes → SqlAlchemyKnowledgeDocumentRepository
  │     └── create_study_task → SqlAlchemyStudyTaskRepository (if create_tasks)
  │
  ├── react_loop(user_message, tools)
  │     ├── _build_system_prompt(tools) → 读取 react_system.txt
  │     ├── for iteration in 1..5:
  │     │     ├── chat_completion(system, messages)
  │     │     ├── json.loads → type=tool_call|final
  │     │     ├── tool_call: 校验 → 执行 → 拼接 observation → 继续
  │     │     └── final: 返回 answer
  │     └── 超限: 返回"已达到最大迭代次数"
  │
  ├── AgentCallLog 记录
  └── 返回 {answer, iterations, tools_called, created_task_ids}
```

---

## 扶墙走练习

### 练习 1：走一遍循环（10 分钟）

打开 `src/agent/react_loop.py`，找到 `for iteration in range(...)` 那行。用笔画出循环的流程图：

```
开始 → 调 LLM → 解析 JSON → type是什么？
  ├── "tool_call" → 校验工具名 → 校验参数 → 执行工具 → 拼接结果 → 回到循环
  ├── "final" → 返回 answer
  └── 无法解析 → 返回错误
```

### 练习 2：讲清楚（5 分钟）

说出来：

> "Phase 9 实现了一个受控 ReAct Agent。每次循环 LLM 返回 JSON——要么是 tool_call 要么是 final。tool_call 会校验工具名是否在白名单、参数是否符合 Pydantic Schema，通过后执行工具函数，把结果拼成 observation 进入下一轮。create_study_task 只在 create_tasks=true 时注册，防止 Agent 随意写数据。重复调用相同工具+参数 2 次自动停止，最大 5 轮。测试用 FakeLLM 控制返回序列，不调真实 API。"
