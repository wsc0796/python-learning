---
date: 2026-06-10
project: Agentic Internship Coach
phase: 4
status: AI 已实现，里程碑 1 完成
---

# Phase 4 配套学习页 —— Docker + CI + README

## 里程碑 1 完成

Phase 1-4 合在一起，形成了一个**完整、可交付、可展示的 FastAPI 后端项目**。

```
✅ Phase 1: 3 个业务模块 CRUD + 33 条测试 + ruff
✅ Phase 2: SQLite + SQLAlchemy + Alembic
✅ Phase 3: Resume 管理模块
✅ Phase 4: Docker + GitHub Actions CI + README
```

**现在这个项目可以：**
- `docker compose up -d` 一键启动
- `pytest -v --cov=src` 42 条测试 89% 覆盖率
- GitHub push 后自动跑 CI
- README 里展示架构、API、技术栈、亮点

---

## 核心概念

### 1. Dockerfile：把项目打包成镜像

```dockerfile
FROM python:3.12-slim          # 基础环境
WORKDIR /app                     # 工作目录
COPY requirements.txt .         # 先拷贝依赖（利用 Docker 缓存层）
RUN pip install -r requirements.txt
COPY . .                        # 再拷贝代码
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

**分层缓存原理：** Docker 每一行指令是一个层。`COPY requirements.txt` 在前、`COPY . .` 在后 → 如果只改了代码没改依赖，前几层从缓存读取，不用重新 `pip install`。

### 2. docker-compose：编排多个容器

```yaml
services:
  app:        # FastAPI 应用
    build: .
    ports: ["8000:8000"]
    environment:
      - DATABASE_URL=sqlite:////app/data/internship_tracker.db
    depends_on: [redis]
  redis:      # Redis 服务
    image: redis:7-alpine
```

**`depends_on`** = 启动顺序保证（先启动 redis，再启动 app）。
**`environment`** = 往容器里注入环境变量，代码里 `os.getenv("DATABASE_URL")` 读到。

### 3. GitHub Actions：push 代码自动测试

```yaml
on:
  push:
    branches: [main]
jobs:
  test:
    steps:
      - uses: actions/checkout@v4    # 拉代码
      - uses: actions/setup-python@v5 # 装 Python
      - run: pip install -r requirements.txt
      - run: ruff check .
      - run: pytest -v --cov=src --cov-fail-under=80
```

**效果：** 每次 git push，GitHub 自动帮你跑一遍 ruff + pytest。没过就发邮件 / 标红。

### 4. .env.example：环境变量模板

```bash
DATABASE_URL=sqlite:///./internship_tracker.db
LLM_API_KEY=your-api-key   # ← 不要写真实 key，这是公开模板
```

**为什么不是 `.env`？** `.env` 包含真实密钥，在 `.gitignore` 里不提交。`.env.example` 是模板，可以安全提交，新开发者照着复制一份填自己的 key。

---

## 扶墙走练习

### 练习 1：从 0 到启动（如果装了 Docker Desktop）

```powershell
cd C:\Users\50469\github-projects\internship-tracker-api
docker compose up -d
curl http://localhost:8000/health
curl http://localhost:8000/api/v1/companies
docker compose down
```

### 练习 2：看 GitHub Actions 文件（3 分钟）

打开 `.github/workflows/test.yml`，说出每一步在干什么。

### 练习 3：讲清楚（5 分钟）

关掉文件，说出来：

> "里程碑 1 完成了 4 个 Phase。Phase 1 用内存字典实现 3 个模块 CRUD。Phase 2 换成 SQLAlchemy + SQLite，用 Alembic 管理数据库迁移。Phase 3 新增 Resume 模块，验证了 CRUD 模板的可复用性。Phase 4 加了 Docker 一键启动、GitHub Actions 自动测试、README 项目文档。42 条测试，89% 代码覆盖率。"

---

## 里程碑 1 交付物清单

| 文件 | 作用 |
|------|------|
| `src/` (17 个 .py 文件) | 4 个业务模块，3 层架构 |
| `tests/` (5 个测试文件) | 42 条测试，89% 覆盖率 |
| `alembic/` | 2 个迁移文件 |
| `Dockerfile` | 项目镜像 |
| `docker-compose.yml` | 一键启动 app + redis |
| `.github/workflows/test.yml` | CI 自动测试 |
| `.env.example` | 环境变量模板 |
| `README.md` | 完整项目文档 |
| `requirements.txt` | 8 个依赖 |
