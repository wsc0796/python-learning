---
date: 2026-06-10
project: Agentic Internship Coach
phase: 3
status: AI 已实现，待学习
---

# Phase 3 配套学习页 —— Resume 管理

## 本 Phase 做了什么

新增了一个 Resume（简历）CRUD 模块。逻辑和 Company 几乎一样，但**这次你应该能看懂大部分代码了**——因为它的模式和第 1-2 个模块完全一致。

---

## 核心概念

### 1. CRUD 的固定模板

看三个模块的文件列表：

| 层 | Company | Job | Application | **Resume** |
|----|---------|-----|-------------|------------|
| ORM | `models/company.py` | `models/job.py` | `models/application.py` | **`models/resume.py`** |
| Schema | `schemas/company.py` | `schemas/job.py` | `schemas/application.py` | **`schemas/resume.py`** |
| Repository | `repositories/company.py` | `repositories/job.py` | `repositories/application.py` | **`repositories/resume_repo.py`** |
| Service | `services/company.py` | `services/job.py` | `services/application.py` | **`services/resume_service.py`** |
| Router | `routes/companies.py` | `routes/jobs.py` | `routes/applications.py` | **`routes/resume_router.py`** |
| Tests | `tests/test_companies.py` | `tests/test_jobs.py` | `tests/test_applications.py` | **`tests/test_resumes.py`** |

**规律已浮现：新增一个业务模块 = 这 6 个文件。** Resume 是最简单的模块（没有级联删除、没有状态流转），正好用来验证你掌握了这个模式。

### 2. 模块复杂度对比

| 特性 | Company | Job | Application | Resume |
|------|---------|-----|-------------|--------|
| 基本 CRUD | ✓ | ✓ | ✓ | ✓ |
| 字段校验 | name 非空 | title 非空 | — | name 非空 |
| 外键校验 | — | company 必须存在 | job 必须存在 | — |
| 去重 | name 唯一 | 同公司 title 唯一 | 同 job 唯一 | — |
| 级联删除保护 | 有 Job 不能删 | 有 Application 不能删 | — | — |
| 状态流转 | — | — | 7 状态 + 流转表 | — |

Resume 是最简版：没有外键、没有去重、没有级联、没有状态。**这才是你第一个可以独立仿写的模块。**

### 3. Alembic 迁移的完整流程

```
改模型 → 生成迁移 → 应用 → 测试

# 1. 创建/修改 src/models/resume.py
# 2. 生成迁移文件
alembic revision --autogenerate -m "002_add_resumes"

# 3. 检查生成的迁移文件是否合理
#    查看 alembic/versions/xxxx_002_add_resumes.py

# 4. 应用迁移
alembic upgrade head

# 5. 回退测试
alembic downgrade -1

# 6. 重新应用
alembic upgrade head
```

Phase 3 验收命令里的 `upgrade → downgrade → upgrade` 就是在验证迁移可以正常来回切换。

---

## 扶墙走练习

### 练习 1：对比 Company 和 Resume（5 分钟）

同时打开 `src/services/company.py` 和 `src/services/resume_service.py`，左右对比。

找出 CompanyService 比 ResumeService **多了什么**，然后说出来。

> 提示：看 CompanyService 的 `create_company`、`delete_company` 方法，和 ResumeService 有什么不同。

### 练习 2：仿写一个模块（10 分钟）

仿照 Resume 模块，用纸笔写出一个 **Skill** 模块的 5 层函数签名（不需要实现内部逻辑）：

```
Skill 字段：id, name(str), level(int 1-5), created_at, updated_at
接口：POST/GET/GET:id/PUT/DELETE /api/v1/skills
```

写出以下内容即可：

```python
# schemas/skill.py — 写出三个类的字段
# repositories/skill_repo.py — 写出 Repository Protocol 的方法签名
# services/skill_service.py — 写出 Service 的方法签名
# routes/skill_router.py — 写出 5 个 @router 装饰器
```

### 练习 3：讲清楚（5 分钟）

关掉所有文件，说出：

> "给项目新增一个业务模块需要 6 个文件。ORM 定义表结构和字段类型，Schema 定义接口的输入输出格式，Repository 用 Session 做数据库操作，Service 写业务规则，Router 定义 HTTP 端点和错误映射，Tests 验证所有接口。Alembic 用 autogenerate 生成迁移文件，upgrade/downgrade 来回切换验证迁移正确性。"
