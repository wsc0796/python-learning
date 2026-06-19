---
date: 2026-06-10
project: Agentic Internship Coach
phase: 2
status: AI 已实现，待学习
---

# Phase 2 配套学习页 —— SQLite + SQLAlchemy + Alembic

## 本 Phase 做了什么

把 Phase 1 的内存字典替换成了真正的数据库。**API 行为完全不变，33 条测试全部照过。**

```
Phase 1:  Route → Service → InMemoryRepo(dict)
Phase 2:  Route → Service → SqlAlchemyRepo(Session) → SQLite
                              ↑ 接口签名完全不变
```

---

## 核心概念

### 1. ORM：把 Python 类映射成数据库表

```python
# 你写的 Python 类
class Company(Base):
    __tablename__ = "companies"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)

# SQLAlchemy 自动生成 SQL：
# CREATE TABLE companies (id INTEGER PRIMARY KEY, name VARCHAR(100) NOT NULL)
```

**Java 类比：** Hibernate/JPA 的 `@Entity` + `@Table` + `@Column`。

**关键规则：**
- `Mapped[int]` = 这个字段在 Python 里是 int 类型
- `mapped_column(Integer, ...)` = 这个字段在数据库里是 INTEGER 列
- `nullable=False` = NOT NULL 约束
- `server_default="open"` = 数据库层面的默认值

### 2. Session：数据库连接的管理单元

```python
db = SessionLocal()    # 从连接池拿一个连接
company = db.get(Company, 1)  # SELECT * FROM companies WHERE id = 1
company.name = "新名字"
db.commit()            # UPDATE companies SET name = '新名字' WHERE id = 1
db.close()             # 归还连接
```

**事务边界：** 一次 `commit()` 是一个事务。如果中间出错 → `rollback()` 回滚。

**Java 类比：** MyBatis 的 `SqlSession`，或 JPA 的 `EntityManager`。

### 3. Alembic：数据库的版本控制

```bash
# 就像 git 管理代码版本一样，Alembic 管理数据库结构版本：
alembic revision --autogenerate -m "添加 resumes 表"   # git add
alembic upgrade head                                    # git commit
alembic downgrade -1                                    # git revert
```

每次改数据库结构（加表、加字段）都生成一个迁移文件，存在 `alembic/versions/` 里。上线时只需要跑 `alembic upgrade head`。

### 4. dependency_overrides：测试的杀手锏

```python
# 正常请求：get_db() → 生产数据库
# 测试时：overide get_db() → 内存数据库
app.dependency_overrides[get_db] = override_get_db
```

**不需要改任何业务代码**，FastAPI 自动把所有用到 `get_db` 的地方换成测试版。

---

## Phase 2 新增/修改的文件

| 文件 | 干什么 |
|------|--------|
| `src/database.py` | 创建 engine、Session、Base、get_db |
| `src/config.py` | 读 DATABASE_URL 环境变量 |
| `src/models/company.py` | Company ORM 模型 |
| `src/models/job.py` | Job ORM 模型（含唯一约束） |
| `src/models/application.py` | Application ORM 模型（含唯一约束） |
| `src/repositories/*.py` | 新增 SqlAlchemy*Repository |
| `alembic/` | 迁移目录，含 001_init 迁移 |
| `tests/conftest.py` | 改为内存 SQLite + dependency_overrides |

---

## 扶墙走练习

### 练习 1：看 SQL（5 分钟）

在 `tests/conftest.py` 的 `engine = create_engine(...)` 那行后面加一句：

```python
engine = create_engine(
    "sqlite:///:memory:",
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
    echo=True,  # ← 加这一行
)
```

然后跑 `pytest tests/test_companies.py::test_create_and_get_company -v -s`

观察终端输出的 SQL 语句：CREATE TABLE、INSERT、SELECT 分别是什么。

### 练习 2：对比两个 Repository（10 分钟）

打开 `src/repositories/company.py`，找到 `InMemoryCompanyRepository`（Phase 1）和 `SqlAlchemyCompanyRepository`（Phase 2）。

对比它们的 `create` 方法，填空：

| 步骤 | InMemory | SqlAlchemy |
|------|----------|------------|
| 创建对象 | `CompanyRead(id=..., ...)` | `Company(**data.model_dump())` |
| 存储 | `self._companies[id] = company` | `self.db.add(company)` |
| 持久化 | 不需要（内存） | `________` |
| 返回 | `return company` | `________` |

### 练习 3：讲清楚（5 分钟）

关掉文件，说出：

> "Phase 2 把字典换成了 SQLAlchemy。ORM 模型用 Mapped 和 mapped_column 定义字段，Session 管理数据库连接。Repository 的方法签名没变——create 还是收 Schema 返回 Schema，但内部从字典存取变成了 db.add/db.commit/db.refresh。测试用 dependency_overrides 把 Session 换成内存 SQLite，每个测试自动建表。Alembic 管数据库版本迁移。"
