---
date: 2026-06-10
project: Agentic Internship Coach
phase: 8
status: AI 已实现
---

# Phase 8 配套学习页 —— StudyTask 管理

## 本 Phase 做了什么

新增 StudyTask（学习任务）CRUD，为 Phase 9 的 Agent 自动创建学习任务做准备。

```
POST   /api/v1/study-tasks           ← 创建任务
GET    /api/v1/study-tasks?status=todo&priority=high  ← 按状态+优先级筛选
GET    /api/v1/study-tasks/{id}      ← 查看任务
PATCH  /api/v1/study-tasks/{id}/status  ← 更新状态
DELETE /api/v1/study-tasks/{id}      ← 删除任务
```

---

## 核心概念

### 1. 第七个 CRUD 模块——你该感到无趣了

如果你现在觉得"又是 model → schema → repo → service → routes → test 六件套，好无聊"，那说明你已经内化了这个模式。这就是工程能力的标志——同一个模式重复到第 7 遍就变成了肌肉记忆。

### 2. completed_at 的自动设置

```python
if data.status == "done" and task.completed_at is None:
    extra_updates["completed_at"] = datetime.now(timezone.utc)
```

**和 Application 的 applied_at 一样——状态变化触发时间戳自动记录。** 这种"副作用"在 Service 层处理，不在 Route 层。

### 3. 双维度筛选

```python
GET /study-tasks?status=doing&priority=high
```

Repository 里用两个独立的 `filter` 叠加：
```python
if status is not None:
    q = q.filter(StudyTask.status == status)
if priority is not None:
    q = q.filter(StudyTask.priority == priority)
```

**任何组合都可以：只按 status、只按 priority、两者一起、两者都不。

---

## 扶墙走练习

### 练习 1：对比 Resume 和 StudyTask（5 分钟）

打开 `src/services/resume_service.py` 和 `src/services/study_task_service.py`，左右对比。StudyTask 比 Resume **多了什么**？为什么？

### 练习 2：讲清楚（5 分钟）

说出来：

> "Phase 8 新增了 StudyTask CRUD。和之前模块的区别是多了双维度筛选（status + priority）和状态切换时自动设 completed_at。这个模块是为 Phase 9 的 Agent 准备的数据落点——Agent 分析岗位缺口后，通过 create_study_task 工具创建学习任务。created_by 字段区分 user 手动创建和 agent 自动创建。"
