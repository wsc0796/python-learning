---
date: 2026-06-10
project: Agentic Internship Coach
phase: 1
status: AI 已实现，待学习
---

# Phase 1 配套学习页 —— 内存版 CRUD

## 本 Phase 你拿到了什么

AI 帮你写了一个**能跑起来的 FastAPI 后端**，包含：

- 3 个业务模块：公司(Company)、岗位(Job)、投递(Application)
- 每个模块 5 个接口：增/查列表/查单个/改/删
- 33 条自动化测试，覆盖率 90%
- 代码检查工具 ruff 零报错

代码在 `C:\Users\50469\github-projects\internship-tracker-api\src\`。

## 架构全景图

```
浏览器 / curl / 前端
        │
        │  HTTP 请求 (GET /api/v1/jobs?company_id=1)
        ▼
┌─────────────────────────────────────┐
│  Route 层 (src/api/routes/)         │  ← 收请求、发响应
│  "这个 URL 归我管"                   │
│  companies.py / jobs.py /           │
│  applications.py                    │
└──────────────┬──────────────────────┘
               │ 调用 Service
               ▼
┌─────────────────────────────────────┐
│  Service 层 (src/services/)         │  ← 做判断、定规则
│  "这个操作能不能做"                   │
│  company.py / job.py /             │
│  application.py                     │
└──────────────┬──────────────────────┘
               │ 调用 Repository
               ▼
┌─────────────────────────────────────┐
│  Repository 层 (src/repositories/)  │  ← 存取数据
│  "数据放哪、怎么查"                   │
│  company.py / job.py /             │
│  application.py                     │
└──────────────┬──────────────────────┘
               │
               ▼
          dict[int, Record]  (内存字典)
          (Phase 2 会换成 SQLite 数据库)
```

**为什么分三层？** 直接在一个函数里搞定不就行了吗？

```
❌ 不分层（一个函数做所有事）:
def create_job(request):
    # 校验数据
    # 查公司是否存在
    # 查标题是否重复
    # 存到数据库
    # 返回结果
    → 100 行代码搅在一起，改一处可能坏十处

✅ 分层:
Route    → 只负责 HTTP（收请求、调 Service、返回 HTTP 状态码）
Service  → 只负责业务规则（能不能创建、什么情况报什么错）
Repository → 只负责存储（存哪了、怎么查、不管业务逻辑）
    → 每层只做一件事，改存储不影响业务规则，改规则不影响 HTTP
```

**Java/Spring 类比：** Route = Controller, Service = Service, Repository = Mapper/DAO, Schema = DTO。

---

## 文件清单 —— 17 个文件，每个是干什么的

### 第一层：定义数据结构 (schemas + models)

| 文件 | 干什么的 | 你要看吗 |
|------|---------|---------|
| `src/models/enums.py` | 定义 Application 的 7 种状态(saved→applied→...→closed) | **必看** |
| `src/schemas/company.py` | Company 的输入/输出格式 | 略看 |
| `src/schemas/job.py` | Job 的输入/输出格式 | **必看** |
| `src/schemas/application.py` | Application 的输入/输出格式 | **必看** |

> **关键概念：Schema 分三种**
>
> ```python
> # JobCreate  —— 创建时客户端传什么
> # JobUpdate  —— 修改时客户端传什么（所有字段可选）
> # JobResponse —— 服务端返回什么（多了 id、created_at、updated_at）
> ```
>
> 为什么不能用一个？因为**创建、修改、返回的数据结构不同**。创建时不需要 id（服务端分配），修改时所有字段都可选（只传要改的），返回时有 id 和时间戳。

### 第二层：存取数据 (repositories)

| 文件 | 干什么的 | 你要看吗 |
|------|---------|---------|
| `src/repositories/company.py` | Company 的存取（增删改查 + 去重检查） | 略看 |
| `src/repositories/job.py` | Job 的存取 + 按公司/技术栈筛选 + 去重 | **精读** |
| `src/repositories/application.py` | Application 的存取 + 按岗位/状态筛选 + 去重 | **精读** |

> **关键概念：Protocol（协议/接口）**
>
> ```python
> class JobRepository(Protocol):
>     def create(self, data: JobCreate) -> JobResponse: ...
>     def list(self, ...) -> list[JobResponse]: ...
>     # ...
>
> class InMemoryJobRepository:  # 具体实现
>     def __init__(self):
>         self._jobs: dict[int, JobResponse] = {}  # 用字典当数据库
> ```
>
> Protocol 定义了"一个 Repository 必须有什么方法"，但不写具体实现。
> InMemoryJobRepository 是用 Python 字典模拟数据库。
> Phase 2 会换成 SqlAlchemyJobRepository —— 方法签名不变，只改内部实现。
> **这就是分层的好处：换存储不用改 Service 和 Route。**

### 第三层：业务规则 (services)

| 文件 | 干什么的 | 你要看吗 |
|------|---------|---------|
| `src/services/company.py` | 公司名去重、删除前检查有没有岗位 | **精读** |
| `src/services/job.py` | 公司必须存在、同公司标题去重、删除前检查有无投递 | **精读** |
| `src/services/application.py` | 岗位必须存在、不能重复投递、状态流转校验 | **精读** |

> **关键概念：自定义异常 → HTTP 状态码**
>
> ```python
> # Service 层抛出业务异常：
> raise JobNotFoundError(job_id=5)
> raise DuplicateJobTitleError(title="后端", company_id=1)
>
> # Route 层把异常翻译成 HTTP 响应：
> except JobNotFoundError → 404 {"detail": "Job with id 5 was not found"}
> except DuplicateJobTitleError → 409 {"detail": "..."}
> ```
>
> Service 不说 HTTP —— 它不知道自己是 Web 应用还是命令行工具。
> Route 不说业务规则 —— 它只负责把异常映射成 HTTP 状态码。
> **这就是分层的第二个好处：核心逻辑和传输协议解耦。**

### 第四层：HTTP 入口 (routes)

| 文件 | 干什么的 | 你要看吗 |
|------|---------|---------|
| `src/api/routes/companies.py` | 5 个端点 + 4 种错误翻译 | **精读** |
| `src/api/routes/jobs.py` | 5 个端点 + 分页参数 + 3 种错误翻译 | **精读** |
| `src/api/routes/applications.py` | 5 个端点 + 分页 + 4 种错误翻译 | **精读** |

> **关键概念：FastAPI 路由**
>
> ```python
> @router.post("", response_model=JobResponse, status_code=201)
> def create_job(
>     data: JobCreate,                                    # 请求体
>     service: Annotated[JobService, Depends(get_job_service)],  # 依赖注入
> ) -> JobResponse:
> ```
>
> `@router.post("")` → 这个函数处理 `POST /api/v1/jobs`
> `data: JobCreate` → FastAPI 自动把请求的 JSON 转成 Pydantic 对象并校验
> `Depends(get_job_service)` → FastAPI 自动创建/注入 Service（依赖注入）
> `response_model=JobResponse` → FastAPI 自动把返回值转成 JSON
>
> **你写的 Python 类被 FastAPI 自动变成了 REST API —— 这是 FastAPI 的核心价值。**

### 基础设施

| 文件 | 干什么的 |
|------|---------|
| `src/main.py` | 创建 FastAPI app，注册路由，加 `/api/v1` 前缀 |
| `src/api/dependencies.py` | 创建 Repository 单例，提供 Service 工厂函数 |
| `tests/conftest.py` | 每个测试前重置三个 Repository（保证测试隔离） |

---

## 一个请求的一生

以 `POST /api/v1/jobs` 为例，从头到尾发生了什么：

```
1. 客户端发送:
   POST /api/v1/jobs
   Body: {"company_id": 1, "title": "后端实习生", "tech_stack": "Python"}

2. FastAPI 路由匹配:
   main.py 里 app.include_router(jobs_router, prefix="/api/v1")
   jobs_router 的 prefix="/jobs"
   → 匹配到 POST ""  → 完整路径 /api/v1/jobs

3. FastAPI 解析请求体:
   读到 Body 的 JSON → 用 JobCreate 校验
   - company_id 是 int 吗？是。
   - title 非空吗？是。
   → 校验通过，变成 data: JobCreate 对象

4. FastAPI 解析依赖:
   service: Depends(get_job_service)
   → 调用 get_job_service()
   → 返回 JobService(job_repository, company_repository, application_repository)

5. 进入 Route 函数:
   def create_job(data, service):
       try:
           return service.create_job(data)

6. 进入 Service:
   def create_job(self, data):
       # 6a. 查公司 1 是否存在
       company = self.company_repository.get(1)
       if company is None → raise CompanyReferenceNotFoundError(1)

       # 6b. 查公司 1 下"后端实习生"是否已存在
       if exists_by_title_and_company("后端实习生", 1) → raise DuplicateJobTitleError

       # 6c. 创建
       return self.job_repository.create(data)

7. 进入 Repository:
   def create(self, data):
       # 分配 id=自增计数器
       # 设 created_at=updated_at=datetime.now(UTC)
       # 存入 self._jobs[id] = job_response
       return job_response

8. 返回路径:
   JobResponse → Service → Route → FastAPI
   → FastAPI 把 JobResponse 序列化成 JSON
   → 状态码 201 Created
   → 客户端收到:
   {
     "id": 1,
     "company_id": 1,
     "title": "后端实习生",
     "tech_stack": "Python",
     "created_at": "2026-06-10T12:00:00Z",
     ...
   }
```

---

## 核心概念速查表

| 概念 | 一句话解释 | 类比 |
|------|-----------|------|
| **Pydantic BaseModel** | 带自动校验的 Python 类 | Java 的 `@Valid` 注解 + DTO |
| **Pydantic Field** | 给字段加约束（最小长度、最大长度、默认值） | `@NotNull` `@Size(min=1, max=100)` |
| **field_validator** | 自定义校验逻辑（如"去空格后不能为空"） | 自定义 Validator |
| **ConfigDict(from_attributes=True)** | 让 Pydantic 能从 ORM 对象直接转换 | `BeanUtils.copyProperties` |
| **Protocol** | 定义接口但不定义实现 | Java 的 `interface` |
| **Depends(fn)** | FastAPI 自动调用 fn 来注入依赖 | Spring 的 `@Autowired` |
| **Annotated[T, Depends(fn)]** | 类型标注 + 依赖声明二合一 | `@Autowired` 注解在参数上 |
| **HTTPException** | FastAPI 的标准错误响应 | `throw new ResponseStatusException(HttpStatus.NOT_FOUND)` |
| **APIRouter** | 一组相关接口的路由器 | Spring 的 `@RestController` + `@RequestMapping` |
| **Query(default=20, ge=1, le=100)** | 查询参数，默认 20，最小 1，最大 100 | `@RequestParam(defaultValue="20")` |

---

## 扶墙走练习

### 练习 1：跟读（10 分钟）

打开 `src/services/job.py`，对着上面「一个请求的一生」第 6 步，在代码里找到每一步对应的行。

目标：**能说出 `create_job` 方法先做什么、再做什么、什么情况报什么错。**

### 练习 2：改一处（5 分钟）

在 `src/services/job.py` 的 `create_job` 方法中，找到校验 `company_id` 是否存在的代码。

把报错信息从英文改成中文：

```python
# 原来：
super().__init__(f"Company with id {company_id} was not found")

# 改成：
super().__init__(f"公司 {company_id} 不存在")
```

改完后运行 `pytest -v`，看哪些测试会失败（因为测试里断言了英文错误信息）。

### 练习 3：讲清楚（10 分钟）

关掉所有文件，用嘴说出来：

> "用户请求 POST /api/v1/jobs，传了 company_id 和 title。
> FastAPI 先把 JSON 转成 JobCreate 对象校验，
> 然后调用 JobService.create_job()，
> Service 先查公司是否存在（不存在返回 404），
> 再查同公司同 title 是否已存在（存在返回 409），
> 都通过后调用 Repository 存入字典，
> 最后把 JobResponse 转成 JSON 返回 201。"

能讲清楚 → 你进入了扶墙走第 3 层。

---

## Phase 2 前置知识

Phase 2 会把内存字典换成 SQLite 数据库，核心新概念：

| 新概念 | 一句话 | 先学哪个 |
|--------|--------|---------|
| SQLAlchemy ORM | 把 Python 类映射到数据库表 | **必须先学** |
| Session | 数据库连接/事务的管理单元 | 第二 |
| Alembic | 数据库版本迁移工具（像 git 一样管数据库结构变化） | 第三 |
| IntegrityError | 数据库唯一约束冲突时抛的异常 | 用到再看 |

**建议：** 在 AI 执行 Phase 2 之前，花 20 分钟看一遍 SQLAlchemy 的 declarative_base、Column、Session 三个核心概念。不需要能写，只需要能读。

---

## 当前项目状态

```
✅ Phase 1 完成
   - ruff check: 0 errors
   - pytest: 33 passed
   - coverage: 90%
   
⏳ Phase 2 待启动
```
