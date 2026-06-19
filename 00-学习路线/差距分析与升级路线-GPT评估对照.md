# 差距分析与升级路线 —— GPT评估对照你的学习计划

> 起因：GPT 对当前项目方案评估为"普通后端实习有竞争力，AI Agent 平台岗位约 40% 匹配"
> 目标：把这份评估翻译成**你可以执行的学习动作**，而不是焦虑清单

---

## 一、先理解评估在说什么

GPT 把岗位能力分了 12 项，你的当前项目覆盖情况：

```
Python 后端工程       ██████████████░░░░  75%  ← 你最强的一块
DB/Redis/Docker/CI  █████████████░░░░░  70%
Function Calling    ███████████░░░░░░░  55%
Agent 任务循环       ██████████░░░░░░░░░  50%
领域知识增强          ████████░░░░░░░░░░░  40%
────────────────────────────────────────  ── 及格线以上
记忆管理              ████░░░░░░░░░░░░░░░  20%  ← 关键短板
Agent 评估           ███░░░░░░░░░░░░░░░░  15%  ← 最关键短板
安全/审批/风险控制     ███░░░░░░░░░░░░░░░░  15%
多 Agent 协作         ██░░░░░░░░░░░░░░░░░  10%
NLP/ML/DL 算法       ███░░░░░░░░░░░░░░░░  15%  ← 需要长期补
强化学习              ░░░░░░░░░░░░░░░░░░░   0%  ← 短期放弃
金融交易领域           ░░░░░░░░░░░░░░░░░░░   0%  ← 不需要补
```

**核心结论：你的项目方向对了，缺的是深度不是广度。** 不需要加 Kafka/K8s/微调/前端，需要的是把 Agent 做成"有记忆、有工具、有审批、有评估"的受控系统。

---

## 二、差距 → 现有材料的覆盖情况

好消息：你已有的材料能覆盖不少差距。

| GPT 指出的差距 | 已有材料能覆盖多少 | 覆盖内容 | 还缺什么 |
|-------------|----------------|---------|---------|
| 记忆管理 | ★★★ Al.pdf 有完整方案 | 短期记忆(滑动窗口+摘要+Redis)、长期记忆(双通道召回:结构化+向量) | 需要自己实现到项目里 |
| RAG 太浅 | ★★ Al.pdf 有 BM25+向量混合检索方案 | Query Rewriting、Embedding对比、混合检索、精确率/召回率评估 | 需要从 jieba 升级到向量检索 |
| Agent 评估 | ☆ 几乎没有 | — | 需要从零建立评估体系 |
| 安全审批 | ☆ 几乎没有 | — | 需要设计读写分离和审批流 |
| 多 Agent | ★ AI-Meeting 有 5 Agent 协同参考 | LiteFlow 规则链、状态机编排 | 不需要全做，做 3 角色即可 |
| ML/DL 基础 | ★ 课程大纲第七~八章 | LLM架构、微调、Transformer基础 | 需要系统学，但不要现在开始 |
| 算法基础 | ★★ Hot100 + algorithm 目录 | 已开始刷题 | 持续保持即可 |

---

## 三、逐条差距的升级方案（按优先级）

### 差距1：Agent 评估体系 ← 最关键的短板，简历区分度最大

**当前状态**：只有 `test_agent_returns_answer()` 这种功能测试

**升级方案**（暑假第三阶段做）：

```
在项目中新增 evals/ 目录：

evals/
├── cases.json           # 30个固定测试案例
│   ├── "帮我找一份后端实习"
│   ├── "我Java和Redis都会，能投什么岗位"
│   ├── "给我制定下周的学习计划"
│   └── ...
├── evaluator.py         # 评估运行器
└── report.md            # 评估报告模板
```

**你要实现的 5 个核心指标**：

| 指标 | 含义 | 怎么做 |
|------|------|--------|
| Task Success Rate | Agent 是否完成了用户目标 | 每个 case 预设期望结果，对比 Agent 实际输出 |
| Tool Selection Accuracy | 是否选了正确的工具 | 预设每个 case 应该调哪些 tool，对比实际调用 |
| Groundedness | 回答是否基于真实数据 | 检查 Agent 输出中的岗位名/技能名是否在数据库中存在 |
| Hallucination Rate | 是否编造了不存在的岗位或技能 | 同上反向检查 |
| Avg Iterations | 平均调用几轮工具 | 统计 ReAct 循环次数 |

**这一步的简历价值**：你可以说"我建立了一套 30 个案例的 Agent 评估集，追踪任务成功率、工具选择准确率和幻觉率"——这比"我调用了大模型 API"有区分度得多。

---

### 差距2：记忆管理 ← Al.pdf 已经给你方案，暑假落地

**当前状态**：一次请求内的 ReAct 循环，没有跨会话记忆

**Al.pdf 教你的方案**（你已经读过）：

```text
短期记忆：滑动窗口（保留最近 N 轮对话）+ 摘要压缩（超出窗口的自动压缩）
长期记忆：结构化存储（Redis Hash，存用户目标/技能/偏好）+ 向量存储（Pinecone/Milvus，存历史对话的语义向量）
召回策略：先召回长期记忆 → 拼接到短期上下文 → 检索 RAG → 组成最终 Prompt
```

**升级方案**（暑假第二阶段做）：

```python
# 在项目中新增 memory.py

class ConversationMemory:
    """短期记忆：本次对话的完整历史 + 当前任务状态"""
    messages: list[dict]           # 对话历史
    current_task: dict | None     # 当前正在执行的任务
    tool_calls: list[dict]        # 已调用的工具和结果

class UserProfileMemory:
    """长期记忆：跨会话的用户画像"""
    user_id: str
    target_role: str              # "后端开发"
    skills: list[str]             # ["Python", "Java", "Redis"]
    learning_goals: list[str]     # ["掌握Spring Boot", "理解RAG"]
    past_plans: list[str]         # 历史学习计划ID列表
    preferences: dict             # {"study_time": "evening", "pace": "slow"}

# 存储方案：
# - 结构化数据 → Redis Hash（快速读写）
# - 历史对话语义检索 → Chroma 或 pgvector（向量相似度搜索）
```

**这一步的简历价值**：面试官问"你怎么做记忆管理"，你不再背八股，而是说"我实现了三层记忆——短期存对话轮次、长期存用户画像、情景存历史计划，用 Redis Hash + Chroma 向量库双通道召回"。

---

### 差距3：RAG 升级 ← 从 jieba 升级到向量检索

**当前状态**：jieba 分词 + TF 匹配

**升级方案**（暑假第一阶段就能做）：

```
Phase 1：最小升级（1天）
  jieba + TF → sentence-transformers 做 Embedding → FAISS 做向量检索

Phase 2：混合检索（2天）
  BM25 关键词召回（保留） + 向量语义召回（新增）
  → RRF (Reciprocal Rank Fusion) 融合排序
  → 返回 Top-K 结果 + 来源片段

Phase 3：检索评估（1天）
  自建 20 条测试查询
  计算 Precision@5 / Recall@5 / MRR
```

| 工具选择 | 推荐 | 理由 |
|---------|------|------|
| Embedding 模型 | `sentence-transformers/all-MiniLM-L6-v2` | 轻量，本地可跑，不需要 GPU |
| 向量存储 | FAISS 或 Chroma | FAISS 更轻，Chroma 有更好的查询接口 |
| 关键词检索 | rank_bm25 库 | 直接替换 jieba TF |

**这一步的简历价值**：你可以说"我实现了混合检索——BM25 精确匹配 + 向量语义召回 + RRF 融合，Precision@5 达到 XX%"。有具体数字的项目比"用了RAG"强 10 倍。

---

### 差距4：安全与审批机制 ← 区分"玩具Agent"和"工程Agent"的关键

**当前状态**：Agent 可以直接调用 `create_study_task`，无审批

**升级方案**（暑假第二阶段做）：

```
工具分类：
  只读工具（自动执行）：
    - search_jobs
    - get_job_detail
    - get_resume
    - search_notes

  写操作工具（需用户确认）：
    - create_study_task
    - update_application
    - delete_resource

审批流程：
  Agent 调用写工具 → 系统返回 "pending_approval" 
  → 前端展示提案 → 用户确认/拒绝 
  → 记录审计日志 → 执行或拒绝
```

```python
# 在项目中新增 guard.py

class ActionGuard:
    READ_ONLY_TOOLS = {"search_jobs", "get_job_detail", "get_resume", "search_notes"}
    WRITE_TOOLS = {"create_study_task", "update_application"}
    
    def classify(self, tool_name: str) -> str:
        if tool_name in self.READ_ONLY_TOOLS:
            return "auto"
        if tool_name in self.WRITE_TOOLS:
            return "approval_required"
        return "blocked"
    
    def approve(self, action: dict) -> bool:
        # 参数校验：title 不能为空、priority 在 1-5 之间等
        # 频率限制：同一用户 1 分钟内不能创建超过 10 个任务
        # 记录审计日志
        ...
```

**这一步的简历价值**：面试官问"你的 Agent 安全吗"，你说"我把工具分成只读和写操作两类，写操作需要用户审批才能执行，所有审批记录写审计日志"。这个回答直接命中岗位的"稳定、可干预"要求。

---

### 差距5：ML/DL/算法基础 ← 长期工程，不能突击

**GPT 说这是"无法通过多写几个 FastAPI 接口弥补的差距"**。说明这部分需要系统补。

**你的课程大纲已有的**：

| 课程章节 | 覆盖内容 | 深度 |
|---------|---------|------|
| 第七章 LLM基础 | N-Gram、BLEU/ROUGE/PPL、Encoder-Decoder、Decoder-Only | ★★★ 够用 |
| 第八章 微调 | Prompt-Tuning、P-Tuning、LoRA、CoT | ★★★ 够用 |
| 第九章 Function Call/Agent/RAG | 原理和应用 | ★★★ 对应用开发够用 |

**还需要补的**：

| 主题 | 最低要求 | 暑假优先级 | 学习来源 |
|------|---------|----------|---------|
| Transformer + Attention | 能画出架构图，解释 Q/K/V | 高 | 课程第七章 + 李沐论文精读 |
| Embedding 与向量相似度 | 理解 cosine/dot product，知道怎么选 Embedding 模型 | 高 | 课程第五章(NumPy) + MTEB Leaderboard |
| 强化学习基本概念 | 理解 state/action/reward/policy，知道 RLHF 的大致流程 | 中 | 不需要深入，能讲清楚概念即可 |
| PyTorch 基础 | Tensor、自动求导、简单的前向传播 | 中 | 暑假后期 |
| 数据结构与算法 | Hot100 持续刷 | 持续 | 你已经在做 |

**对于这个岗位，诚实比装懂更重要。** 面试时如果被问到"你做过模型训练吗"，正确回答是：

> "我的重点在 Agent 工程侧——Function Calling、记忆管理、工具编排和评估体系。模型方面我理解 Transformer、Embedding 和微调的基本原理，课程里也学过 P-Tuning 和 LoRA，但我目前的核心能力在把模型接入可控的工程系统，而不是训练模型本身。"

---

## 四、差距升级全时间线（融入你的暑假9周）

```
暑假 9 周（06-29 ~ 08-31）

第1-2周：项目地基打牢
├─ 完成 Phase 1-4（CRUD + SQLAlchemy + Redis + Docker）
├─ RAG 升级：jieba → sentence-transformers + FAISS      ← 差距3
└─ 简历/学习任务模型补齐

第3-4周：Agent 核心能力
├─ 记忆管理实现（短期+长期+Redis+Chroma）                  ← 差距2
├─ 安全审批机制（读写分离+审批流+审计日志）                  ← 差距4
└─ 结构化 Tool Calling（JSON Schema + Pydantic）

第5-6周：Agent 评估体系
├─ 建立 30 个评估案例                                     ← 差距1
├─ 实现 5 个评估指标
├─ 跑出第一份评估报告
└─ 根据报告优化 Agent

第7-8周：多 Agent（可选） + 面试准备
├─ Planner + Retriever + Reviewer 三角色                  ← 差距5(多Agent部分)
├─ 用 Al.pdf 四步话术写项目介绍
├─ 对着 Al.pdf 面经逐题过
└─ 项目 README 完善（架构图+评估报告+使用指南）

第9周：决策 + 收尾
├─ 考研 vs 就业判断
└─ 简历定稿
```

---

## 五、什么不要做

GPT 的警告非常明确——**不要堆技术名词**。以下是你暑假**不应该碰的**：

| 不要做的事               | 原因                          |
| ------------------- | --------------------------- |
| 加 Kafka / RabbitMQ  | 你没有海量数据场景，加了也讲不清楚           |
| 加 K8s / 微服务         | 你的项目规模不需要，Docker Compose 足够 |
| 做模型微调 / LoRA 训练     | 不是你的方向，且需要 GPU 和数据          |
| 加前端 Dashboard       | 分散精力，后端深度更有区分度              |
| 做真正的多 Agent 系统      | 在评估和记忆没做好之前，多 Agent 只是花架子   |
| 同时学 Go / Java / C++ | 选定 Python + Java 两条就够了      |

---

## 六、最终判断：你的定位是什么

GPT 说得很清楚——你不需要对标那个"交易平台 Agent 架构"岗位。你的正确定位是：

```
┌─────────────────────────────────────────┐
│  你的定位：AI 应用后端 + Agent 工程          │
│                                         │
│  核心能力：                                │
│  ├─ FastAPI/Spring Boot 分层架构           │
│  ├─ 数据库 + Redis 缓存                   │
│  ├─ Agent 工具调用 + 记忆 + 审批            │
│  ├─ RAG 混合检索 + 评估                   │
│  └─ CI/CD + Docker 部署                  │
│                                         │
│  竞争力：                                 │
│  ├─ 对普通后端实习：有竞争力                  │
│  ├─ 对 AI 应用工程实习：基本够用              │
│  └─ 对 Agent 平台岗位：需要评估+记忆升级后      │
│     可达到 65-75% 匹配                      │
└─────────────────────────────────────────┘
```

**你不做算法研究员，你做 Agent 工程师。** 这两种角色的能力模型不同：
- 算法研究员：训模型、发论文、刷 benchmark
- Agent 工程师（你的方向）：把模型接入可控、可观测、可评估的工程系统

认清这个定位，面试时就不需要为"不会强化学习"心虚。你展示的是工程能力，不是算法能力。

---

## 七、现在立刻可以做的三件事

不需要等到暑假。考试碎片时间就能完成：

| # | 动作 | 耗时 | 产出 |
|---|------|------|------|
| 1 | 把 AI CR Prompt 模板复制到 Cursor Rules | 5min | 每天开发都在用 |
| 2 | 读 Al.pdf 的短期/长期记忆方案那节 | 20min | 脑子里有"三层记忆"的框架 |
| 3 | 敲 Redis 五种数据类型命令 | 15min | 手感恢复，顺便为记忆管理做准备 |
