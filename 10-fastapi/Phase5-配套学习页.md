---
date: 2026-06-10
project: Agentic Internship Coach
phase: 5
status: AI 已实现，里程碑 2 进行中
---

# Phase 5 配套学习页 —— LLM Client + 岗位匹配 + AiCallLog

## 本 Phase 做了什么

接了 DeepSeek API，实现了一个岗位-简历匹配接口。每次调用自动记录 AiCallLog（成功/失败都记）。

```
POST /api/v1/ai/jobs/{job_id}/match
Body: {"resume_id": 1}
→ LLM 分析岗位 JD + 简历内容
→ 返回 {score, matched_skills, missing_skills, summary, study_suggestions}
→ 记录 AiCallLog（调用耗时、成功/失败、输入输出摘要）
```

**测试用 monkeypatch 替换了 chat_completion，从不调真实 API。**

---

## 核心概念

### 1. OpenAI-compatible API 和 DeepSeek

```python
from openai import OpenAI

client = OpenAI(
    base_url="https://api.deepseek.com/v1",  # ← DeepSeek 的地址，不是 OpenAI
    api_key="sk-xxx",
)

response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "system", "content": "你是求职顾问"},
        {"role": "user", "content": "岗位：... 简历：... 分析匹配度"},
    ],
)
```

**关键点：** DeepSeek 的 API 格式和 OpenAI 完全一样。只要改 `base_url`，代码不用变。这就是"OpenAI-compatible API"的含义。

### 2. LLM Client 的三个工程考量

```python
# ① 懒加载：不调用就不初始化（测试不需要真实 key）
_client: OpenAI | None = None

def _get_client():
    global _client
    if _client is None:
        _client = OpenAI(...)
    return _client

# ② 超时：30 秒不响应就失败
"timeout": 30.0

# ③ 重试：失败后再试 1 次
for attempt in range(2):
    try:
        ...
    except Exception:
        if attempt == 0:
            time.sleep(0.5)  # 等 0.5 秒再试
```

### 3. str.format() 的坑

Prompt 模板里如果要出现 `{` 和 `}`（比如 JSON 示例），必须写成 `{{` 和 `}}`：

```python
# ❌ 错误：str.format() 把 {score: ...} 当占位符
"返回 JSON: { "score": 0-100 }"   # → KeyError

# ✅ 正确：用双花括号转义
"返回 JSON: {{ \"score\": 0-100 }}"
```

### 4. monkeypatch：替换函数实现

```python
from unittest.mock import patch

# 把 chat_completion 替换成直接返回假数据的函数
with patch(
    "src.services.job_matching_service.chat_completion",
    return_value='{"score": 82, ...}',
):
    resp = client.post("/api/v1/ai/jobs/1/match", json={"resume_id": 1})
```

**注意：** patch 的路径是 `"src.services.job_matching_service.chat_completion"`，不是 `"src.ai.llm_client.chat_completion"`。因为 `job_matching_service.py` 里写了 `from src.ai.llm_client import chat_completion`，函数被 import 到了 job_matching_service 的命名空间里。**patch 要打在引用的地方，不是定义的地方。**

### 5. Pydantic 校验 LLM 输出

```python
class JobMatchResult(BaseModel):
    score: int = Field(ge=0, le=100)      # 0-100 之间
    matched_skills: list[str]
    ...

# LLM 可能返回格式不对、分数超出范围、缺字段
# model_validate 一次搞定所有校验
result = JobMatchResult.model_validate(json.loads(raw))
```

不要只相信 Prompt 里的"只返回 JSON"——模型会犯错，必须校验。

### 6. AiCallLog：审计追踪

每次 LLM 调用都记录：
- 哪个模型、哪种请求类型
- 输入摘要（不保存完整简历，只保存 id + 字符数）
- 输出前 200 字符
- 耗时（毫秒）
- 成功/失败 + 错误信息

**为什么？** 1) 排查问题 2) 成本统计 3) Prompt 效果对比。这是 AI 应用的工程基础。

---

## 扶墙走练习

### 练习 1：看 Prompt 模板（3 分钟）

打开 `src/ai/prompts/job_match.txt`，数一下有几个 `{占位符}` 和几个 `{{转义花括号}}`。

### 练习 2：改一个字段（5 分钟）

在 `JobMatchResult` 里加一个 `confidence: str` 字段（值必须是 "high"、"medium"、"low" 之一）。

然后更新 FAKE_LLM_RESPONSE，看测试还能不能过。

### 练习 3：讲清楚（5 分钟）

说出来：

> "Phase 5 接入了 DeepSeek API。LLM Client 用懒加载避免测试时需要真实 key，30 秒超时，失败重试一次。岗位匹配接口从数据库查岗位 JD 和简历内容，拼成 Prompt 发给 LLM，返回结果用 Pydantic 校验（分数 0-100、技能列表等）。每次调用记录 AiCallLog（模型、耗时、成功/失败、输入输出摘要）。测试用 monkeypatch 替换 chat_completion，不调真实 API。"
