# 02_PLAN

## 目标

这里放 GPT 产出的方案。Codex 执行前，你先检查业务、边界和自己是否能解释。

## 业务规则

1. 
2. 
3. 

## 涉及模块

- 路由层：`main.py`
- Service 层：`service.py`
- Repository / Model 层：`repository.py`、`models.py`
- 依赖注入：`dependencies.py`
- 测试：`run_checks.py`

## 允许修改

- 按本次任务填写。

## 禁止修改

- 按本次任务填写。

## 架构边界

- 路由层负责：HTTP 请求、响应模型、状态码、异常转换。
- Service 层负责：业务规则和 CRUD。
- Repository 层负责：JSON 文件读写。
- Pydantic Model 负责：输入/输出数据结构和校验。

## 伪代码

```pseudo

```

## 验收标准

- `python run_checks.py` 通过。
- 新增/修改的接口能在 `/docs` 或 TestClient 中跑通。

## 风险点

- 不要把 HTTPException 写进 Service。
- 不要让 Service 直接读写 `tasks.json`。
- 不要让前端创建任务时传入服务端字段，例如 `id`。

## 给 Codex 的压缩结论

本次任务确认后，把这里压缩成 `03_CODEX_TASK.md`。

