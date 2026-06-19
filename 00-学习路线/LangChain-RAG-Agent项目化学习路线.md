# LangChain / RAG / Agent 项目化学习路线

> 前置：[[07-pydantic]]、[[08-typing-di]]、[[10-fastapi]]、[[17-context-iterator-async]]、[[18-llm-coze-workflow]]、[[19-llm-finetune-rag-agent-projects]]
> 目标：把 LangChain 学成一个可演示、可写进 GitHub 和简历的 RAG/Agent 项目，而不是只会跟教程敲 API。
> 用时：约 4 周，每天 40-60 分钟。

---

## 一、总路线

```text
Python 工程基础
  -> LLM API 调用
  -> LangChain 基础组件
  -> RAG 知识库
  -> Agentic RAG
  -> LangGraph 工作流
  -> FastAPI Web 化
  -> GitHub / README / 面试表达
```

LangChain 不是替代 Python 基础，也不是替代 RAG 原理。它更像 Spring 生态里的组件编排框架：把模型、Prompt、工具、检索器、状态和回调统一成可组合的工程结构。

---

## 二、和本仓库已有内容的对应关系

| 已有章节 | 对 LangChain 的帮助 | 学 LangChain 时怎么用 |
|---|---|---|
| [[07-pydantic]] | 工具参数、结构化输出、接口模型 | 定义 Tool 入参、API 请求/响应模型 |
| [[08-typing-di]] | 类型标注、依赖注入、Protocol | 拆分 LLM、Retriever、VectorStore 接口 |
| [[10-fastapi]] | Web API、Service/Repository 分层 | 把 RAG 能力暴露为 HTTP 服务 |
| [[17-context-iterator-async]] | 异步、上下文管理、迭代器 | 处理流式输出、异步上传、批量文档处理 |
| [[18-llm-coze-workflow]] | 工作流思维、LLM 基础 | 理解 Chain / Agent / Workflow 的区别 |
| [[19-llm-finetune-rag-agent-projects]] | Prompt、Function Call、Agent、RAG | 作为 LangChain 项目的理论前置 |
| [[26-unit-tests]] | 测试习惯 | 为检索、Prompt、API 接口写最小测试 |
| [[33-notes-api]] / [[34-todo-api]] | 小型后端项目结构 | 迁移到 RAG Web 项目的目录组织 |

---

## 三、四周计划

### 第 1 周：LangChain 基础组件

目标：知道 LangChain 每个组件解决什么问题。

学习内容：

- Chat Model：统一调用 DeepSeek / OpenAI 兼容接口。
- Prompt Template：把提示词从字符串变成模板。
- Output Parser：让模型输出 JSON、列表、字段。
- Runnable / LCEL：理解 `prompt | model | parser` 的管道思想。
- Tool：把普通 Python 函数包装成模型可调用工具。

本仓库关联：

- 复习 [[19-llm-finetune-rag-agent-projects/10-langchain-basic]]
- 对照 [[08-typing-di]] 理解接口拆分。
- 对照 [[07-pydantic]] 理解工具参数 schema。

小项目：

```text
01-langchain-cli-assistant
输入文本 -> Prompt 模板 -> DeepSeek -> JSON 输出
```

验收标准：

- API Key 使用 `.env`，不能写死。
- 至少有 3 个 Prompt 模板。
- 至少有 1 个 Pydantic 输出模型。
- 能解释 Runnable 和普通函数调用的区别。

破坏实验：

- 故意让模型输出非 JSON，观察解析错误。
- 故意删除环境变量，观察 API Key 报错。

---

### 第 2 周：RAG 基础

目标：把你已经理解的 RAG 流程换成 LangChain 标准组件。

学习内容：

- Document Loader：读取 txt、Markdown、PDF。
- RecursiveCharacterTextSplitter：文本分块。
- Embeddings：文本转向量。
- Vector Store：Chroma / FAISS。
- Retriever：top-k 检索。
- RAG Chain：检索 -> 拼接上下文 -> 生成回答。

本仓库关联：

- 复习 [[19-llm-finetune-rag-agent-projects/06-rag-milvus]]
- 复习 [[19-llm-finetune-rag-agent-projects/07-rag-optimization]]
- 对照 [[03-file-exception]] 理解文件读取和异常处理。

小项目：

```text
02-local-doc-rag
本地 Markdown/PDF -> 分块 -> 向量库 -> 提问 -> 显示引用片段
```

验收标准：

- 能上传或指定本地文档。
- 每次回答展示至少 2 个引用片段。
- 能调整 `chunk_size`、`chunk_overlap`、`top_k`。
- README 里能画出 Indexing 和 Retrieval 两段流程。

破坏实验：

- 把 `chunk_size` 改得很小，观察回答变碎。
- 把 `top_k` 改成 1，观察召回不足。
- 提问文档里没有的信息，观察模型是否胡编。

---

### 第 3 周：FastAPI RAG Web 应用

目标：从脚本变成可演示的后端项目。

学习内容：

- FastAPI 文件上传。
- RAG Service / Repository 分层。
- `.env`、`config.py`、`.gitignore`。
- logging 日志。
- 简单测试。
- README 和截图。

本仓库关联：

- 直接复用 [[10-fastapi]]、[[33-notes-api]]、[[34-todo-api]] 的项目结构。
- 对照 [[26-unit-tests]] 写接口测试。
- 对照 [[08-typing-di]] 做依赖注入。

推荐目录：

```text
rag-web-app/
  app/
    main.py
    dependencies.py
    config.py
    schemas.py
    services/
      rag_service.py
      document_service.py
    repositories/
      vector_repository.py
    llm/
      deepseek_client.py
  tests/
  data/
  .env.example
  requirements.txt
  README.md
```

小项目：

```text
03-rag-web-api
POST /documents/upload
POST /chat
GET  /documents
GET  /health
```

验收标准：

- 可以通过 API 上传文档并问答。
- API Key 不进 Git。
- 有 `.env.example`。
- 有最少 3 个测试：健康检查、上传、问答 mock。
- README 写清楚本地运行步骤。

破坏实验：

- 上传空文件。
- 上传不支持的格式。
- DeepSeek API Key 为空。
- 向量库目录不存在。

---

### 第 4 周：Agentic RAG + LangGraph + Skill 沉淀

目标：从普通知识库升级成能选择工具、能被 AI 接力维护的项目。

学习内容：

- `create_agent`：让模型选择工具。
- Retrieval Tool：把知识库检索封装成工具。
- 多工具：知识库检索、SQL 查询、计算器、Obsidian 查询。
- LangGraph：把复杂流程画成 State -> Node -> Edge。
- LangSmith / 日志：观察每一步调用。

本仓库关联：

- 对照 [[19-llm-finetune-rag-agent-projects/04-function-call]]
- 对照 [[19-llm-finetune-rag-agent-projects/05-ai-agent-basic]]
- 对照 [[19-llm-finetune-rag-agent-projects/11-project-logistics-rag]]

小项目：

```text
04-agentic-study-rag
用户问题 -> Agent 判断是否查知识库
         -> 必要时调用 Retriever
         -> 必要时生成复习题 / 总结 / 学习计划
```

验收标准：

- 至少 2 个工具：`search_notes`、`generate_quiz`。
- Agent 能在“不需要检索”的问题上直接回答。
- Agent 能在“基于资料”的问题上返回引用片段。
- 有一个 LangGraph 版本的流程图或代码。

破坏实验：

- 工具返回空结果，观察 Agent 怎么处理。
- 工具抛异常，观察是否能返回友好错误。
- 连续追问 5 轮，观察上下文是否混乱。

---

## 四、AI 使用方式

### GPT / ChatGPT

适合做：

- 需求拆解。
- 学习路线规划。
- Prompt 设计。
- README 草稿。
- 面试讲法。

不要让 GPT 直接长期改整个项目，因为它不一定看到真实文件状态。

### Codex

适合做：

- 读本地项目。
- 小步重构。
- 跑测试。
- 检查 API Key 是否泄露。
- 写 README、`.env.example`、测试脚本。

推荐使用方式：

```text
先让 Codex 读目录 -> 给出风险 -> 再让它只改指定文件 -> 跑测试 -> 总结结果
```

### Claude Code + DeepSeek

适合做：

- 长时间批量编码。
- 按 AI_HANDOFF 执行明确任务。
- 补全前端、接口、测试、Docker。

推荐使用方式：

```text
GPT/Codex 先产出 AI_HANDOFF
Claude Code + DeepSeek 负责执行
Codex 最后 review 和跑测试
```

### Obsidian

适合做：

- 项目上下文。
- 每日错误记录。
- 面试故事。
- 技术决策。
- 下一步任务。

不要把原始聊天记录整段塞进去，只写结构化结论。

---

## 五、Skill 思考

这里的 skill 不是“知识点”，而是“以后可以重复触发的工作流”。

### 候选 Skill 1：langchain-rag-lesson-pack

触发：

```text
当你要学习 LangChain 的某个小概念，并希望生成 theory + practice + 破坏实验。
```

工作流：

1. 选一个最小概念，例如 Retriever、TextSplitter、Tool。
2. 生成 10-15 分钟理论笔记。
3. 生成 4-8 个 TODO 练习。
4. 添加 1 个破坏实验。
5. 给出运行命令和口头复述问题。

建议：后续可以创建。

### 候选 Skill 2：rag-project-review

触发：

```text
当你完成 RAG 项目一阶段，希望检查是否能上 GitHub / 写简历。
```

工作流：

1. 检查 API Key、`.env`、`.gitignore`。
2. 检查目录结构。
3. 检查 README、截图、运行说明。
4. 检查是否有测试和日志。
5. 输出简历表达和面试讲法。

建议：优先创建，因为它直接服务作品集。

### 候选 Skill 3：ai-handoff-for-langchain-project

触发：

```text
当你要把 LangChain 项目任务交给 Claude Code + DeepSeek 执行。
```

工作流：

1. 写清任务目标。
2. 限定允许修改文件。
3. 写清禁止事项，例如不能提交 API Key。
4. 写清验证命令。
5. 写清交付总结格式。

建议：在你开始重构 RAG Web 项目前创建。

---

## 六、最终 GitHub 项目目标

项目名建议：

```text
personal-rag-knowledge-base
```

简历表达：

```text
基于 FastAPI + LangChain + ChromaDB + DeepSeek API 实现个人知识库 RAG 系统，
支持文档上传、文本分块、向量检索、引用片段展示与多轮问答；
进一步将知识库检索封装为 Agent Tool，并通过日志和评估脚本分析检索命中率与回答质量。
```

README 必须包含：

- 项目背景：解决什么问题。
- 技术栈：FastAPI、LangChain、ChromaDB、DeepSeek、Pydantic。
- 架构图：上传、索引、检索、生成。
- 本地运行：安装依赖、配置 `.env`、启动服务。
- API 示例：上传文档、提问。
- 效果截图：问答和引用片段。
- 核心难点：分块策略、引用片段、错误处理、API Key 安全。
- 后续计划：多用户、Redis、Celery、LangGraph。

---

## 七、每天固定执行格式

```text
读：读官方文档或本仓库 theory
敲：手写最小 practice
破：做一个破坏实验
跑：执行脚本或测试
记：写 progress
述：30 秒口头复述
沉淀：判断是否能变成 README / Skill / GitHub 证据
```

30 秒口头复述模板：

```text
今天我学的是 ______。
它在 RAG 项目里负责 ______。
不用它时，我需要手写 ______。
用了它以后，代码变成 ______。
今天踩的坑是 ______，以后定位方式是 ______。
```

