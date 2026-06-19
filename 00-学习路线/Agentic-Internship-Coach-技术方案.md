---
date: 2026-06-13
version: V2.1
target_ai: Codex / Claude Code
usage: 每个 Phase 可单独交给 AI 执行，但必须以前一 Phase 验收通过为前置条件
---

# Agentic Internship Coach —— AI 可执行规格书 V2.1

## 项目定位

Agentic Internship Coach 是一个面向后端实习求职的 FastAPI 项目：

- 第一阶段先做成一个稳定、可测试、可启动的求职投递管理后端。
- 第二阶段加入 LLM 岗位匹配、调用日志和 Redis 缓存。
- 第三阶段再加入关键词 RAG 和受控工具调用 Agent。
- 第四阶段再对齐课程中的 LangChain、Milvus、BM25、DeepSeek 原理和综合项目扩展。

这不是一次性堆功能的 Demo，而是一个可以分阶段提交到 GitHub、可在面试中解释架构演进的作品集项目。

## 基本信息

```text
项目名：Agentic Internship Coach
本地项目：C:\Users\50469\github-projects\internship-tracker-api
后端框架：FastAPI + Pydantic + SQLAlchemy + Alembic
数据库：SQLite 优先，MySQL 作为后续扩展，不纳入当前 MVP
缓存：Redis
LLM：OpenAI-compatible API，默认 DeepSeek
Agent：先手写受控 Function Call / ReAct Loop，后续可迁移 LangChain 或 LangGraph
RAG：先关键词检索，后续可升级 BM25 + Milvus 向量检索
架构：routes -> services -> repositories -> models
测试：pytest + pytest-cov，外部服务全部 mock/fake
```

## 课程知识映射与边界

用户当前课程包含“大模型开发与应用”和“综合项目”。本项目吸收课程知识，但分成两类：

- MVP 必做：能直接增强后端项目，并且容易测试、展示、讲清楚。
- 进阶选做：适合课程学习、面试扩展、二期项目，不阻塞主线交付。

| 课程内容 | 本项目落点 | 是否进入 MVP |
| --- | --- | --- |
| Function Call 工作原理、外部函数定义、多函数调用 | Phase 9 的工具白名单、参数校验、数据库查询工具 | 是 |
| AI Agent 基本原理、邮件自动发送案例 | Phase 9 做受控 ReAct Agent；邮件自动发送只作为后续扩展，不默认发送真实邮件 | 是，邮件为选做 |
| RAG 系统介绍 | Phase 7 关键词 RAG MVP | 是 |
| Milvus Collection、向量增删改查 | Phase 10 作为向量 RAG 进阶 | 否，二期 |
| RAG 优化与评估 | Phase 7 先做来源返回；Phase 10 加召回率、命中率、人工评测集 | 部分进入 |
| Flash Attention、MLA、MoE | 写入 README 或学习笔记，用于解释模型能力，不在后端代码中实现 | 否 |
| BM25 | Phase 7 可从简单 TF 升级到 BM25；不影响接口 | 可选 |
| DeepSeek V1/V2/Math/V3/R1 | Phase 5 使用 DeepSeek-compatible API；模型原理作为学习说明 | 部分进入 |
| LangChain LLMs / ChatModels / Prompt / Chains | Phase 11 作为手写 LLM/RAG/Agent 的替代实现对照 | 否，二期 |
| LangChain Agent / Memory / Indexes | Phase 11 迁移实验，不替代 MVP 主线 | 否，二期 |
| 物流行业 RAG 系统 | Phase 12 可复用 RAG 架构做领域版 RAG | 否，作品集扩展 |
| 评论智能分类与信息抽取系统 | Phase 12 可做独立 NLP/LLM 抽取项目，不塞进主项目 | 否，作品集扩展 |

原则：

- 不把 LangChain、Milvus、模型微调一开始塞进 MVP。
- 先自己实现轻量 LLM Client、RAG、Function Call Loop，学清楚底层流程。
- 等主项目可运行、可测试、可展示后，再用 LangChain/Milvus 做二期迁移或扩展。

## 全局执行规则

每个 Phase 必须遵守：

- 只能做当前 Phase 列出的任务，不主动实现后续 Phase。
- 开始前先确认前置条件是否满足，不满足则停止并说明。
- 保持 API 路径、请求体、响应体和业务行为稳定。
- 允许为数据库 Session 注入做最小必要调整，但不得重写整体架构。
- 所有 Python 业务代码放在 `src/` 下，测试放在 `tests/` 下。
- 不提交 `.env`、API Key、Token、简历原文等私密信息。
- LLM、Redis 等外部服务在自动化测试中必须使用 fake/mock。
- 每个 Phase 完成后输出：修改文件、关键设计、验收命令、测试结果。

## 全局质量命令

```bash
cd C:\Users\50469\github-projects\internship-tracker-api
ruff check .
ruff format --check .
pytest -v --cov=src --cov-report=term-missing --cov-fail-under=80
```

如果项目尚未引入 `ruff` 或 `pytest-cov`，在对应 Phase 的依赖中加入。

## 统一 API 约定

```text
API 前缀：/api/v1
列表接口：支持 limit、offset，默认 limit=20，最大 limit=100
时间字段：使用 UTC datetime
错误格式：FastAPI 默认 {"detail": "..."}
```

本 MVP 是单用户本地求职管理系统，不包含账号系统、多租户和权限管理。

## 数据删除规则

- Company 下存在 Job 时，删除 Company 返回 409。
- Job 下存在 Application 时，删除 Job 返回 409。
- Resume、KnowledgeDocument、StudyTask 可物理删除；后续如需要再改软删除。

## 状态流转规则

Application 状态：

```text
saved -> applied -> written_test -> interviewing -> offer
任意非终态 -> rejected
任意非 closed 状态 -> closed
closed 为终态
```

明确状态表：

| 当前状态 | 允许进入 |
| --- | --- |
| saved | applied, rejected, closed |
| applied | written_test, interviewing, rejected, closed |
| written_test | interviewing, rejected, closed |
| interviewing | offer, rejected, closed |
| offer | closed |
| rejected | closed |
| closed | 无 |

设置为相同状态视为幂等成功，返回 200。

---

# 里程碑 1：可投递的 FastAPI 后端

目标：先完成一个工程上站得住的求职投递管理后端，包含 CRUD、SQLite、迁移、测试、Docker、CI 和 README。

## Phase 1：Company + Job + Application CRUD（内存版）

### 前置条件

- 项目已有 FastAPI 基础结构。
- 已有 Company CRUD 骨架和 pytest。
- 本 Phase 使用线程内内存 Repository，不使用 SQLAlchemy。

### 目标

补全 Job 和 Application CRUD，保持现有 Company CRUD 可用。

### 存储规则

```text
存储方式：dict[int, Record]
ID：Repository 内部自增
生命周期：应用重启后数据丢失，这是 Phase 1 的预期行为
并发：Phase 1 不处理多进程并发
```

### 必须创建/修改的文件

```text
src/models/enums.py
src/schemas/job.py
src/schemas/application.py
src/repositories/job_repo.py
src/repositories/application_repo.py
src/services/job_service.py
src/services/application_service.py
src/routes/job_router.py
src/routes/application_router.py
src/main.py
tests/test_jobs.py
tests/test_applications.py
```

### Job 字段

```text
id: int
company_id: int
title: str                 # 必填，去除首尾空格后不能为空
city: str | None = None
job_type: str | None = None
salary_range: str | None = None
jd_text: str = ""
requirements: str = ""
tech_stack: str = ""
source_url: str | None = None
status: str = "open"
created_at: datetime
updated_at: datetime
```

### Job 接口

```text
POST   /api/v1/jobs
GET    /api/v1/jobs?company_id=1&tech_stack=Python&limit=20&offset=0
GET    /api/v1/jobs/{job_id}
PUT    /api/v1/jobs/{job_id}
DELETE /api/v1/jobs/{job_id}
```

业务规则：

- `company_id` 必须对应已存在公司，否则 404。
- 同一公司下 `title` 不能重复，大小写和首尾空格归一化后比较，重复返回 409。
- 删除不存在的 Job 返回 404。

### Application 字段

```text
id: int
job_id: int
status: ApplicationStatus = "saved"
applied_at: datetime | None = None
next_step_at: datetime | None = None
notes: str = ""
created_at: datetime
updated_at: datetime
```

### Application 接口

```text
POST   /api/v1/applications
GET    /api/v1/applications?job_id=1&status=interviewing&limit=20&offset=0
GET    /api/v1/applications/{application_id}
PATCH  /api/v1/applications/{application_id}/status
DELETE /api/v1/applications/{application_id}
```

业务规则：

- `job_id` 必须存在，否则 404。
- 同一 `job_id` 只能创建一条 Application，重复返回 409。
- 状态流转必须符合全局状态表，非法流转返回 422。
- 状态从 `saved` 变为 `applied` 时，如果 `applied_at` 为空，自动设置为当前 UTC 时间。

### 测试要求

```python
def test_create_job_success(): ...
def test_create_job_company_not_found_404(): ...
def test_create_job_duplicate_title_409(): ...
def test_create_job_empty_title_422(): ...
def test_get_job_by_id(): ...
def test_get_job_not_found_404(): ...
def test_list_jobs_filter_by_company(): ...
def test_list_jobs_filter_by_tech_stack(): ...
def test_update_job(): ...
def test_delete_job(): ...

def test_create_application_success(): ...
def test_create_application_job_not_found_404(): ...
def test_create_application_duplicate_409(): ...
def test_patch_status_success(): ...
def test_patch_status_rejected_to_closed_success(): ...
def test_patch_status_closed_cannot_change_422(): ...
def test_get_application(): ...
def test_list_applications_filter_by_status(): ...
```

### 验收命令

```bash
pytest -v --cov=src --cov-report=term-missing --cov-fail-under=80
```

## Phase 2：SQLite + SQLAlchemy + Alembic

### 前置条件

- Phase 1 全部测试通过。
- API 行为已有测试保护。

### 目标

把内存 Repository 替换为 SQLAlchemy + SQLite，并加入 Alembic 初始迁移。

### 必须创建/修改的文件

```text
requirements.txt
src/config.py
src/database.py
src/models/company.py
src/models/job.py
src/models/application.py
src/repositories/company_repo.py
src/repositories/job_repo.py
src/repositories/application_repo.py
tests/conftest.py
alembic.ini
alembic/env.py
alembic/versions/001_init.py
```

### 数据库规则

- 使用 SQLAlchemy 2.x 风格。
- 默认 `DATABASE_URL=sqlite:///./internship_tracker.db`。
- 测试使用内存 SQLite：

```python
connect_args={"check_same_thread": False}
poolclass=StaticPool
```

- `created_at`、`updated_at` 使用 UTC。
- Repository 负责数据访问，Service 负责业务规则。
- 数据库层必须有唯一约束：

```text
jobs: unique(company_id, normalized_title)
applications: unique(job_id)
```

- Service 中仍可提前检查重复数据，数据库 `IntegrityError` 也必须映射为 409。

### 允许修改范围

允许为数据库 Session 注入做最小必要调整，例如：

- 新增 `get_db()`。
- 调整 Route 依赖。
- 调整 Service 或 Repository 的构造方式。
- 调整测试 fixture。

禁止改变已有 API 行为。

### 验收命令

```bash
alembic upgrade head
pytest -v --cov=src --cov-report=term-missing --cov-fail-under=80
```

## Phase 3：Resume 管理

### 前置条件

- Phase 2 通过。
- Alembic 可正常 upgrade。

### 目标

补上后续 AI 匹配和 Agent 需要的 Resume 数据模型，避免每次请求重复传整段简历。

### 必须创建/修改的文件

```text
src/models/resume.py
src/schemas/resume.py
src/repositories/resume_repo.py
src/services/resume_service.py
src/routes/resume_router.py
alembic/versions/002_add_resumes.py
tests/test_resumes.py
```

### Resume 字段

```text
id: int
name: str                  # 简历名称，例如 "后端实习简历"
content: str               # 简历正文，自动化测试用假数据
skills: str                # 逗号分隔或 JSON 字符串，先保持简单
created_at: datetime
updated_at: datetime
```

### 接口

```text
POST   /api/v1/resumes
GET    /api/v1/resumes?limit=20&offset=0
GET    /api/v1/resumes/{resume_id}
PUT    /api/v1/resumes/{resume_id}
DELETE /api/v1/resumes/{resume_id}
```

### 隐私规则

- 测试和 README 不得出现真实姓名、电话、邮箱、学校、证件号。
- AI 日志不直接保存完整 `content`。

### 验收命令

```bash
alembic upgrade head
alembic downgrade -1
alembic upgrade head
pytest -v --cov=src --cov-report=term-missing --cov-fail-under=80
```

## Phase 4：Docker + CI + README（基础项目可交付）

### 前置条件

- Phase 3 通过。

### 目标

让项目形成第一个完整作品集交付物：可启动、可测试、有 CI、有 README。

### 必须创建/修改的文件

```text
Dockerfile
docker-compose.yml
.github/workflows/test.yml
.env.example
README.md
```

### Docker 规则

当前 MVP 使用 SQLite + Redis。MySQL 暂不实现，只在 README 的后续扩展中说明。

```yaml
services:
  app:
    build: .
    ports:
      - "8000:8000"
    environment:
      - DATABASE_URL=sqlite:////app/data/internship_tracker.db
      - REDIS_URL=redis://redis:6379/0
    volumes:
      - ./data:/app/data
    depends_on:
      - redis
  redis:
    image: redis:7-alpine
```

### CI 规则

- GitHub Actions 运行 ruff 和 pytest。
- CI 不调用真实 LLM。
- 如 Redis 测试需要服务，使用 GitHub Actions Redis service；单元测试优先 fake/mock。

### README 必须包含

- 项目定位一句话。
- 架构说明：routes、services、repositories、models、schemas。
- 快速开始：本地启动和 docker compose 启动。
- API 列表。
- 数据库迁移命令。
- 测试命令。
- 技术亮点。
- 当前范围：单用户、本地 MVP、SQLite。
- 后续扩展：MySQL、认证、向量 RAG、前端。

### 验收命令

```bash
docker compose up -d
curl http://localhost:8000/health
ruff check .
ruff format --check .
pytest -v --cov=src --cov-report=term-missing --cov-fail-under=80
```

---

# 里程碑 2：AI 岗位匹配

目标：在稳定后端基础上加入结构化 LLM 调用、AI 调用日志和 Redis 缓存。

## Phase 5：LLM Client + 岗位匹配 + AiCallLog

### 前置条件

- Phase 4 通过。
- Resume、Job、Application 均已落库。

### 依赖

```text
openai
httpx
pydantic-settings
```

### 环境变量

写入 `.env.example`，不要写真实 `.env`：

```text
LLM_BASE_URL=https://api.deepseek.com/v1
LLM_API_KEY=your-api-key
LLM_MODEL=deepseek-chat
```

### 必须创建/修改的文件

```text
src/config.py
src/ai/__init__.py
src/ai/llm_client.py
src/ai/prompts/job_match.txt
src/models/ai_call_log.py
src/repositories/ai_call_log_repo.py
src/services/ai_call_log_service.py
src/schemas/ai.py
src/services/job_matching_service.py
src/routes/ai_router.py
alembic/versions/003_add_ai_call_logs.py
tests/test_ai_job_match.py
```

### LLM Client

```python
def chat_completion(
    system_prompt: str,
    user_prompt: str,
    response_format: dict | None = None,
) -> str:
    """调用 OpenAI-compatible API，超时 30s，失败重试 1 次，返回文本。"""
```

第一版可以使用同步客户端。若后续改为 `AsyncOpenAI`，必须统一调整所有 LLM Service。

### Function Call 学习落点

本 Phase 先不使用 OpenAI SDK 原生 `tools/function_call`，而是通过普通 Chat Completion 返回结构化 JSON，练清楚：

- 如何定义输入 Schema。
- 如何约束模型输出。
- 如何做 JSON 解析和 Pydantic 校验。
- 如何把模型错误映射成 HTTP 502。
- 如何记录调用日志。

原生 Function Call 放到 Phase 9 的 Agent 工具调用中对齐。

### 岗位匹配接口

```text
POST /api/v1/ai/jobs/{job_id}/match
```

请求体：

```json
{
  "resume_id": 1
}
```

响应体：

```json
{
  "score": 82,
  "matched_skills": ["Python", "FastAPI"],
  "missing_skills": ["Docker"],
  "summary": "岗位匹配度较高，但需要补齐部署能力。",
  "study_suggestions": ["复习 FastAPI 分层结构", "补 Docker 基础"]
}
```

错误规则：

- Job 不存在：404。
- Resume 不存在：404。
- LLM 调用失败：502，`{"detail": "AI 服务暂时不可用"}`。
- LLM 返回 JSON 解析或校验失败：502，并记录失败日志。

### 结构化输出校验

必须使用 Pydantic 校验 LLM 返回：

```python
class JobMatchResult(BaseModel):
    score: int = Field(ge=0, le=100)
    matched_skills: list[str]
    missing_skills: list[str]
    summary: str
    study_suggestions: list[str]
```

不要只相信 Prompt 中的“只返回 JSON”。

### AiCallLog 模型

```text
id: int
provider: str              # deepseek
model: str                 # deepseek-chat
request_type: str          # job_match
prompt_hash: str           # SHA256(prompt)
input_summary: str         # 不保存简历原文，只保存 resume_id、job_id、字符数、技能摘要
output_summary: str        # 前 200 字符
latency_ms: int
success: bool
error_message: str | None
created_at: datetime
```

### 测试规则

- 使用 monkeypatch 或 FakeLLMClient，不调用真实 API。
- 测试成功返回、Job 404、Resume 404、日志成功写入、LLM 失败记录日志。

### 验收命令

```bash
alembic upgrade head
pytest -v --cov=src --cov-report=term-missing --cov-fail-under=80
```

## Phase 6：Redis 缓存 AI 结果

### 前置条件

- Phase 5 通过。
- 岗位匹配结果已有结构化校验。

### 依赖

```text
redis
hiredis
```

### 必须创建/修改的文件

```text
src/cache/__init__.py
src/cache/redis_client.py
src/cache/ai_result_cache.py
src/services/job_matching_service.py
tests/test_ai_job_match_cache.py
.env.example
```

### 缓存 Key

Key 必须包含模型、Prompt 版本、简历、岗位内容：

```text
ai:job_match:v1:{model}:{prompt_hash}:{resume_hash}:{job_content_hash}
```

其中 `job_content_hash` 至少包含：

- `jd_text`
- `requirements`
- `tech_stack`

### 缓存规则

- TTL 默认 86400 秒。
- 命中缓存时不调用 LLM。
- 命中缓存时不新增 AiCallLog，或者记录一条 `request_type=job_match_cache_hit`，二选一并在 README 说明。
- Redis 不可用时降级为直接调用 LLM。
- 缓存读取或写入失败不得导致接口失败。
- 第一版不要求分布式锁。

### 测试规则

- 使用 fake Redis 或 monkeypatch。
- 测试第一次调用走 LLM，第二次相同请求命中缓存。
- 测试 Redis 故障时仍能返回 LLM 结果。

### 验收命令

```bash
pytest -v --cov=src --cov-report=term-missing --cov-fail-under=80
```

---

# 里程碑 3：RAG 与受控 Agent

目标：把项目从“AI 接口”推进到“能基于学习资料生成准备计划”的 Agentic 后端，但保持实现可解释、可测试。

## Phase 7：关键词 RAG MVP

### 前置条件

- Phase 6 通过。
- LLM Client 可被 fake/mock。

### 依赖

```text
jieba
```

可选进阶：

```text
rank-bm25
```

### 必须创建/修改的文件

```text
src/models/knowledge_document.py
src/schemas/knowledge_document.py
src/repositories/knowledge_repo.py
src/services/knowledge_service.py
src/routes/knowledge_router.py
src/rag/__init__.py
src/rag/keyword_retriever.py
src/rag/rag_service.py
src/routes/rag_router.py
alembic/versions/004_add_knowledge_documents.py
tests/test_knowledge_documents.py
tests/test_rag.py
```

### KnowledgeDocument 字段

```text
id: int
title: str
content: str
source_type: str       # resume | jd | note | review
created_at: datetime
updated_at: datetime
```

### 接口

```text
POST /api/v1/knowledge/documents
GET  /api/v1/knowledge/documents?source_type=note&limit=20&offset=0
GET  /api/v1/knowledge/documents/{document_id}

POST /api/v1/rag/answer
```

RAG 请求：

```json
{
  "question": "什么是缓存穿透？"
}
```

RAG 响应：

```json
{
  "answer": "缓存穿透是查询不存在的数据，请求绕过缓存直接打到数据库。",
  "sources": [
    {
      "document_id": 1,
      "title": "Redis 缓存笔记",
      "snippet": "缓存穿透：查询不存在的数据...",
      "score": 0.82
    }
  ]
}
```

### 检索规则

- 本 Phase 是关键词检索 RAG，不是向量 RAG。
- 使用 `jieba` 分词 + 简单词频匹配。
- `retrieve(query, top_k=5) -> list[dict]`。
- 未检索到内容时返回可解释答案，不编造来源。
- 长文档先按固定长度切片，保留标题作为来源。
- 如果课程已经学到 BM25，可以在不改变 API 的前提下新增 `bm25_retriever.py`，用 BM25 替换简单词频打分。
- 本 Phase 不引入 Milvus。Milvus 放到 Phase 10，避免数据库、向量索引和 RAG 一起失控。

### 验收命令

```bash
alembic upgrade head
alembic downgrade -1
alembic upgrade head
pytest -v --cov=src --cov-report=term-missing --cov-fail-under=80
```

## Phase 8：StudyTask 管理

### 前置条件

- Phase 7 通过。
- RAG 可以返回来源。

### 目标

补上 Agent 创建学习任务所需的数据模型，避免工具调用没有落点。

### 必须创建/修改的文件

```text
src/models/study_task.py
src/schemas/study_task.py
src/repositories/study_task_repo.py
src/services/study_task_service.py
src/routes/study_task_router.py
alembic/versions/005_add_study_tasks.py
tests/test_study_tasks.py
```

### StudyTask 字段

```text
id: int
title: str
description: str = ""
priority: str             # low | medium | high
status: str               # todo | doing | done | canceled
related_job_id: int | None
created_by: str           # user | agent
created_at: datetime
updated_at: datetime
completed_at: datetime | None
```

### 接口

```text
POST  /api/v1/study-tasks
GET   /api/v1/study-tasks?status=todo&priority=high&limit=20&offset=0
GET   /api/v1/study-tasks/{task_id}
PATCH /api/v1/study-tasks/{task_id}/status
DELETE /api/v1/study-tasks/{task_id}
```

### 验收命令

```bash
alembic upgrade head
pytest -v --cov=src --cov-report=term-missing --cov-fail-under=80
```

## Phase 9：受控 Function Call / ReAct Agent

### 前置条件

- Phase 8 通过。
- Job、Resume、KnowledgeDocument、StudyTask 均已实现。

### 目标

实现一个受控工具调用 Agent，根据岗位和简历缺口生成学习计划。第一版优先稳定、可测、可解释，不追求复杂自治。

这对应课程里的 Function Call 和 AI Agent：

- 外部函数定义：用工具白名单和 Pydantic 参数模型表示。
- 意图澄清：缺少 `job_id` 或 `resume_id` 时返回可解释错误或追问信息。
- 多函数调用：允许多轮调用不同工具，但每轮只允许一个工具。
- 数据库查询实现：工具内部调用 Repository/Service 查询 Job、Resume、KnowledgeDocument、StudyTask。
- 有副作用函数：`create_study_task` 必须受 `create_tasks` 开关控制。

### 必须创建/修改的文件

```text
src/agent/__init__.py
src/agent/tool_registry.py
src/agent/react_loop.py
src/agent/prompts/react_system.txt
src/models/agent_call_log.py
src/repositories/agent_call_log_repo.py
src/routes/agent_router.py
alembic/versions/006_add_agent_call_logs.py
tests/test_agent.py
```

### Agent 请求

```text
POST /api/v1/agent/chat
```

```json
{
  "job_id": 1,
  "resume_id": 1,
  "message": "请根据岗位缺口生成学习计划",
  "create_tasks": false
}
```

### Agent 响应

```json
{
  "answer": "建议优先补 Redis 和 Docker...",
  "iterations": 3,
  "tools_called": ["get_job_requirements", "get_resume_skills", "search_learning_notes"],
  "created_task_ids": []
}
```

### 工具白名单

```text
get_job_requirements(job_id: int)
get_resume_skills(resume_id: int)
search_learning_notes(query: str)
create_study_task(title: str, priority: str, description: str, related_job_id: int | None)
```

### 工具定义格式

每个工具必须有独立参数 Schema，避免让 LLM 直接传任意 dict：

```python
class GetJobRequirementsArgs(BaseModel):
    job_id: int

class SearchLearningNotesArgs(BaseModel):
    query: str = Field(min_length=1)
```

工具注册表示例：

```python
TOOLS = {
    "get_job_requirements": ToolSpec(
        description="获取指定岗位的技能要求",
        args_model=GetJobRequirementsArgs,
        function=get_job_requirements,
    )
}
```

如果后续切换 OpenAI 原生 Function Calling 或 LangChain Tools，这个注册表可以作为迁移入口。

### 工具副作用规则

- `create_study_task` 只有在请求体 `create_tasks=true` 时可用。
- `create_tasks=false` 时，Agent 只能生成计划，不写入任务。
- 所有工具参数必须通过 Pydantic 校验。
- 工具名必须在白名单中。
- 单轮只允许一个工具调用。
- 最大迭代数默认 5。
- 重复调用相同工具和相同参数 2 次时停止，返回当前可用答案。

### LLM 输出格式

不要依赖自由文本解析 `Thought/Action`。每轮要求模型返回 JSON：

工具调用：

```json
{
  "type": "tool_call",
  "reasoning_summary": "需要先查看岗位要求。",
  "tool": "get_job_requirements",
  "arguments": {
    "job_id": 1
  }
}
```

最终回答：

```json
{
  "type": "final",
  "reasoning_summary": "信息足够，可以生成学习计划。",
  "answer": "..."
}
```

必须用 Pydantic 校验。不要把完整模型推理保存到日志或 API 响应里，只保存 `reasoning_summary`。

### AgentCallLog 字段

```text
id: int
job_id: int | None
resume_id: int | None
message_summary: str
tools_called: str           # JSON 字符串
iterations: int
success: bool
error_message: str | None
created_at: datetime
```

### 测试规则

- 使用 FakeLLM，不调用真实 API。
- 测试 final answer。
- 测试工具调用顺序。
- 测试 `create_tasks=false` 不创建任务。
- 测试 `create_tasks=true` 创建任务。
- 测试 max_iterations 停止。
- 测试非法工具名被拒绝。

### 验收命令

```bash
alembic upgrade head
alembic downgrade -1
alembic upgrade head
pytest -v --cov=src --cov-report=term-missing --cov-fail-under=80
```

---

# 里程碑 4：课程进阶扩展（不阻塞 MVP）

目标：把课程中的 LangChain、Milvus、RAG 优化、DeepSeek 原理和综合项目沉淀成二期能力。只有当 Phase 1-9 已经稳定后，才进入本里程碑。

## Phase 10：BM25 + Milvus 向量 RAG

### 前置条件

- Phase 7 关键词 RAG 已完成。
- 已有一批 KnowledgeDocument 测试数据。
- README 已明确当前项目是关键词 RAG MVP。

### 目标

把 RAG 从简单关键词检索升级为“关键词 + 向量”的混合检索：

- BM25 负责关键词召回。
- Embedding + Milvus 负责语义召回。
- Rerank 第一版可用简单加权，不引入额外模型。

### 可选依赖

```text
pymilvus
sentence-transformers 或 OpenAI-compatible embedding API
rank-bm25
```

### 新增模块建议

```text
src/rag/bm25_retriever.py
src/rag/embedding_client.py
src/rag/milvus_store.py
src/rag/hybrid_retriever.py
tests/test_hybrid_rag.py
```

### Milvus 学习点

- Collection 创建。
- Field Schema。
- 向量维度。
- Index 类型。
- Insert / Search / Delete。
- 文档 ID 与向量 ID 的映射。

### 评估要求

准备一个小型评测集：

```text
question
expected_source_title
expected_keywords
```

验收至少包含：

- top-3 是否召回正确来源。
- answer 是否引用 sources。
- 没有来源时是否拒绝编造。

## Phase 11：LangChain / LangGraph 对照迁移

### 前置条件

- Phase 9 手写 Agent 已完成。
- 已经能讲清楚手写 LLM Client、Prompt、Retriever、Tool Registry、Agent Loop。

### 目标

不是用 LangChain 重写整个项目，而是做一份对照实现，理解框架把哪些步骤封装掉了。

### 学习映射

| LangChain 组件 | 本项目已有对应 |
| --- | --- |
| LLMs / ChatModels | `src/ai/llm_client.py` |
| PromptTemplate | `src/ai/prompts/*.txt` |
| Chains | `job_matching_service`、`rag_service` |
| Tools | `src/agent/tool_registry.py` |
| Agent | `src/agent/react_loop.py` |
| Memory | 可选：保存 Agent 会话摘要 |
| Indexes / Retrievers | `keyword_retriever`、`hybrid_retriever` |

### 交付物

```text
docs/langchain-migration-notes.md
src/experimental/langchain_agent.py
tests/test_langchain_agent_contract.py
```

要求：

- 不替换主线代码。
- 不改变已有 API。
- 只做实验入口或文档对照。
- 对比手写版和 LangChain 版的优缺点。

## Phase 12：综合项目扩展 A：物流行业 RAG 系统

### 目标

复用当前 RAG 架构，做一个独立的领域 RAG 小项目，用来对应课程中的“物流行业 RAG 系统”。

### 建议边界

- 不塞进 Agentic Internship Coach 主项目。
- 可以新建独立仓库或 `examples/logistics-rag/`。
- 数据处理、文档切分、检索、回答、评估链路要完整。

### 可展示能力

- 领域文档清洗。
- 文档切片策略。
- BM25 / Milvus 检索对比。
- RAG 评估表。
- README 中展示一次完整问答。

## Phase 13：综合项目扩展 B：评论分类与信息抽取

### 目标

把课程中的“评论智能分类与信息抽取系统”作为第二个独立作品集方向，不强行塞入求职 Agent。

### 技术路线

- 第一版：调用 LLM 做结构化抽取，Pydantic 校验输出。
- 第二版：使用传统 BERT 分类或轻量微调。
- 第三版：复习 ChatGLM-6B、LoRA、P-Tuning、梯度检查点等训练知识。

### 与主项目关系

主项目只吸收两个经验：

- 结构化抽取结果必须校验。
- 模型训练和在线后端服务要解耦。

## Phase 14：DeepSeek 与大模型原理学习笔记

### 目标

将课程中的 DeepSeek V1/V2/Math/V3/R1、MLA、MoE、Flash Attention 等内容整理成面试可讲的学习笔记。

### 建议文件

```text
00-学习路线/DeepSeek-模型原理与工程应用.md
00-学习路线/RAG-BM25-Milvus-学习笔记.md
00-学习路线/LangChain-基础到项目迁移.md
```

### 注意

- 这些是原理学习笔记，不要求在 FastAPI 项目里实现 Flash Attention、MLA 或 MoE。
- 面试表达重点放在“我知道模型底层优化是什么，但我的项目重点是应用层工程落地”。

---

# 最终目录结构

```text
internship-tracker-api/
├── src/
│   ├── main.py
│   ├── config.py
│   ├── database.py
│   ├── models/
│   │   ├── company.py
│   │   ├── job.py
│   │   ├── application.py
│   │   ├── resume.py
│   │   ├── ai_call_log.py
│   │   ├── knowledge_document.py
│   │   ├── study_task.py
│   │   └── agent_call_log.py
│   ├── schemas/
│   │   ├── company.py
│   │   ├── job.py
│   │   ├── application.py
│   │   ├── resume.py
│   │   ├── ai.py
│   │   ├── knowledge_document.py
│   │   └── study_task.py
│   ├── repositories/
│   │   ├── company_repo.py
│   │   ├── job_repo.py
│   │   ├── application_repo.py
│   │   ├── resume_repo.py
│   │   ├── ai_call_log_repo.py
│   │   ├── knowledge_repo.py
│   │   ├── study_task_repo.py
│   │   └── agent_call_log_repo.py
│   ├── services/
│   │   ├── company_service.py
│   │   ├── job_service.py
│   │   ├── application_service.py
│   │   ├── resume_service.py
│   │   ├── ai_call_log_service.py
│   │   ├── job_matching_service.py
│   │   ├── knowledge_service.py
│   │   └── study_task_service.py
│   ├── routes/
│   │   ├── company_router.py
│   │   ├── job_router.py
│   │   ├── application_router.py
│   │   ├── resume_router.py
│   │   ├── ai_router.py
│   │   ├── knowledge_router.py
│   │   ├── rag_router.py
│   │   ├── study_task_router.py
│   │   └── agent_router.py
│   ├── ai/
│   │   ├── llm_client.py
│   │   └── prompts/
│   │       └── job_match.txt
│   ├── cache/
│   │   ├── redis_client.py
│   │   └── ai_result_cache.py
│   ├── rag/
│   │   ├── keyword_retriever.py
│   │   └── rag_service.py
│   └── agent/
│       ├── tool_registry.py
│       ├── react_loop.py
│       └── prompts/
│           └── react_system.txt
├── tests/
├── alembic/
├── alembic.ini
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── .env.example
├── .github/workflows/test.yml
└── README.md
```

# 依赖清单

```text
# 基础
fastapi
uvicorn
pydantic
pytest
pytest-cov
httpx
ruff

# 数据库
sqlalchemy
alembic

# 配置
pydantic-settings

# LLM
openai

# 缓存
redis
hiredis

# RAG
jieba

# RAG 进阶，可选
rank-bm25
pymilvus

# LangChain 进阶，可选
langchain
langgraph
```

`docker` 不是 Python 依赖，不写入 `requirements.txt`。

# 推荐执行顺序

```text
1. Phase 1：内存版 CRUD
2. Phase 2：SQLite + Alembic
3. Phase 3：Resume
4. Phase 4：Docker + CI + README
5. Phase 5：LLM 岗位匹配
6. Phase 6：Redis 缓存
7. Phase 7：关键词 RAG
8. Phase 8：StudyTask
9. Phase 9：受控 Agent
10. Phase 10：BM25 + Milvus 向量 RAG，可选
11. Phase 11：LangChain / LangGraph 对照迁移，可选
12. Phase 12：物流行业 RAG 系统，独立扩展
13. Phase 13：评论分类与信息抽取系统，独立扩展
14. Phase 14：DeepSeek 与大模型原理学习笔记
```

这个顺序保证：即使后面的 RAG、Agent、LangChain、Milvus 或微调项目暂时没做完，前四个 Phase 也已经能形成一个完整、可展示、可测试的 FastAPI 作品集。
