---
date: 2026-06-10
project: Agentic Internship Coach
phase: 6
status: AI 已实现
---

# Phase 6 配套学习页 —— Redis 缓存 AI 结果

## 本 Phase 做了什么

给岗位匹配加了 Redis 缓存。同一份简历 + 同一个岗位 JD，24 小时内不重复调 LLM。

```
第一次请求 → 调 LLM (2秒) → 结果写入 Redis → 返回
第二次请求 → 命中缓存 (<1ms) → 直接返回
Redis 挂了 → 降级到直接调 LLM（不影响用户）
```

---

## 核心概念

### 1. 缓存 Key 设计

```python
key = f"ai:job_match:v1:{model}:{prompt_hash}:{resume_hash}:{job_content_hash}"
```

**为什么包含这么多信息？**
- `ai:job_match` → 前缀，标识这是哪个业务
- `v1` → Prompt 版本。如果改了 Prompt，改版本号让旧缓存失效
- `{model}` → 不同模型结果不同，不能混用缓存
- `{prompt_hash}` → Prompt 不同，结果不同
- `{resume_hash}` → 简历改了，缓存必须失效
- `{job_content_hash}` → JD 改了，缓存必须失效（只用 id 不够——JD 可能会被修改）

### 2. 缓存降级（Graceful Degradation）

```python
def get_cached_match(...) -> dict | None:
    r = get_redis()
    if r is None:           # ① Redis 连不上
        return None         #    降级：假装没缓存
    
    try:
        cached = r.get(key)
        if cached:
            return json.loads(cached)
    except Exception:        # ② Redis 读写出错
        pass                 #    降级：假装没缓存
    
    return None              # ③ 没命中或降级 → 走 LLM
```

**原则：缓存是优化，不是核心路径。缓存挂了，LLM 还能用。**

### 3. 缓存读写在服务中的位置

```python
def match(self, job_id, resume_id):
    # ① 查数据
    job = ...
    resume = ...
    
    # ② 查缓存（命中直接返回）
    cached = get_cached_match(...)
    if cached is not None:
        return cached      # ← 不调 LLM，不记 AiCallLog
    
    # ③ 调 LLM
    raw = chat_completion(...)
    result = validate(raw)
    
    # ④ 写缓存（失败了也不影响返回）
    set_cached_match(..., result)
    
    # ⑤ 记日志 & 返回
    record_call(...)
    return result
```

---

## 扶墙走练习

### 练习 1：看缓存 Key（3 分钟）

打开 `src/cache/ai_result_cache.py`，找到 `_build_cache_key` 函数。数一下 Key 里有多少个分段（冒号分隔的部分），说出每段的作用。

### 练习 2：改缓存时长（2 分钟）

在 `set_cached_match` 调用中，把 `ttl` 从 `86400`（24小时）改成 `3600`（1小时）。跑测试确认还能过。

### 练习 3：讲清楚（5 分钟）

说出来：

> "Phase 6 给岗位匹配加了 Redis 缓存。缓存 Key 包含模型名、Prompt 版本、Prompt 哈希、简历哈希、JD 内容哈希——任何一个变了，缓存自动失效。TTL 默认 24 小时。缓存命中直接返回，不调 LLM、不记日志。Redis 不可用时降级到直接调 LLM，缓存读写异常不影响接口。测试用 monkeypatch 模拟缓存命中和 Redis 故障。"
