---
aliases:
  - 05-ai-agent-basic
---
# Day 5：AI Agent 基础

读完约 15 分钟。

---

## 一、Agent 是什么

AI Agent = 能自主理解目标、规划步骤、调用工具、记忆状态、适应反馈的智能系统。

### LLM 应用 vs Agent

```
LLM 应用：用户问一句 → 模型答一句（被动响应）
Agent：用户给目标 → Agent 拆解任务 → 调工具 → 观察 → 再行动（主动执行）
```

### Agent 的基本组成

| 组件 | 角色 | 类比 |
|------|------|------|
| LLM | 大脑 | 思考决策 |
| Prompt | 任务指令 | 岗位说明书 |
| Tools | 工具集 | 手和工具 |
| Memory | 记忆 | 短期/长期记忆 |
| Planner | 规划器 | 项目经理 |
| Executor | 执行器 | 执行者 |

---

## 二、Agent 工作流程

```
用户："帮我查北京明天天气，如果适合出门就推荐景点"
                    ↓
① 理解任务：查天气 → 判断是否适合 → 推荐景点
                    ↓
② 调 get_weather("北京", "明天")
                    ↓
③ 观察结果："晴，26°C"
                    ↓
④ 判断：适合出门
                    ↓
⑤ 调 search_pois("北京", "景点")
                    ↓
⑥ 组织回答："明天天气好，推荐去故宫、颐和园..."
```

这就是 ReAct 模式（Reasoning + Acting）。

---

## 三、ReAct 模式详解

ReAct = 推理（Reason）→ 行动（Act）→ 观察（Observe）循环。

```
Thought: 用户想查北京天气
Action: get_weather(city="北京", date="明天")
Observation: {"weather": "晴", "temp": 26}

Thought: 天气不错，适合推荐景点
Action: search_pois(city="北京", category="景点")
Observation: ["故宫", "颐和园", "长城"]

Thought: 我可以回答了
Answer: 明天北京晴，26°C，推荐去故宫或颐和园。
```

你的 `document_pipeline/paper_pipeline.py` 中的 `query()` 方法用的就是这种模式：

```python
# 1. LLM 推理 → 选择相关章节
plan_prompt = f"用户问：{question}，哪些章节相关？"

# 2. 行动 → 读取章节文件
context = read_files(selected_paths)

# 3. 观察 + 最终回答
answer = generate(question, context)
```

---

## 四、Agent 框架对比

| 框架 | 特点 | 适合场景 |
|------|------|---------|
| LangChain | 组件丰富、生态成熟 | 快速搭建原型 |
| LlamaIndex | 数据索引强 | RAG 场景 |
| AutoGen | 多 Agent 对话 | 复杂协作任务 |
| CrewAI | 角色分工 | 团队式 Agent |
| Dify | 低代码可视化 | 非开发者 |
| Coze | 字节出品，中文友好 | 快速验证 |

你之前在 [[18-llm-coze-workflow]] 中已经用了 Coze。

---

## 五、hello-agents 中的 Agent 实现

你的 `hello-agents/` 目录中有多种 Agent 实现：

```python
# 简化版 ReAct Agent
class ReactAgent:
    def __init__(self, tools: list):
        self.llm = OpenAI(...)
        self.tools = {t.name: t for t in tools}

    def run(self, task: str) -> str:
        messages = [{"role": "user", "content": task}]

        while True:
            response = self.llm(messages, tools=self.tools)
            choice = response.choices[0]

            if choice.finish_reason == "tool_calls":
                # 执行工具
                for tc in choice.message.tool_calls:
                    result = self.execute_tool(tc)
                    messages.append(tool_result)
            else:
                return choice.message.content
```

---

## 六、邮件自动发送 Agent 案例

### 需求

```
用户：帮我给张三发一封邮件，提醒他明天下午3点开会
```

### Agent 执行流程

```
① 提取信息：收件人=张三，时间=明天下午3点，事件=开会
② 查联系人：get_contact("张三") → email: zhangsan@xxx.com
③ 生成正文：先生成邮件内容
④ 发送邮件：send_email(to, subject, body)
⑤ 返回结果：邮件已发送
```
