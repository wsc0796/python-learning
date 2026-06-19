# Redis 五种数据类型实操

> 日期：2026-06-13
> 目标：手敲五种数据类型，每条命令都对应到项目中的实际用途

---

## 启动 Redis

```bash
redis-cli ping    # 确认服务在运行 → 应返回 PONG
redis-cli          # 进入交互式命令行
```

---

## 1. String — 最基础，对应 Python `dict[key] = "value"`

### 基础操作

```bash
SET  name  "张三"
GET  name
SET  view_count  0
INCR view_count      # 原子自增 → 1
INCR view_count      # → 2
INCRBY view_count 10 # 原子加10 → 12
```

### 带过期时间（最常用模式）

```bash
SETEX  verification_code  60  "883421"   # 60秒后自动删除
TTL    verification_code                # 查剩余秒数
```

### 项目中的实际用途

| 场景 | 命令 | Python伪代码等价 |
|------|------|-----------------|
| 缓存API响应 | `SETEX jobs:backend 300 '[...]'` | `cache.set("jobs:backend", data, ttl=300)` |
| 浏览次数计数 | `INCR job:5:views` | `views["job:5"] += 1` (但Redis是原子操作) |
| 短信验证码 | `SETEX sms:13800138000 60 "1234"` | 自己写过期逻辑很麻烦 |
| 分布式锁 | `SET lock:task:5 NX EX 10` | 多进程共享锁，Python本地锁做不到 |

---

## 2. Hash — 存对象，对应 Python `{"user:1": {"name": "张", "age": 20}}`

### 基础操作

```bash
HSET  user:1001  name  "张三"  age  22  city  "南昌"
HGET  user:1001  name           # "张三"
HGETALL  user:1001              # 所有字段
HINCRBY  user:1001  login_count  1   # Hash里的字段也能自增
HDEL  user:1001  city           # 删一个字段（String存JSON做不到）
```

### 项目中的实际用途

| 场景 | 命令 | 为什么用Hash而不是String |
|------|------|------------------------|
| 缓存用户信息 | `HGET user:1001 skills` | 可以只改一个字段，不用整个JSON重写 |
| Agent会话状态 | `HSET session:abc step 3 status "waiting_approval"` | 多个维度的状态存在一个key下 |
| 购物车 | `HSET cart:user5 item:101 2` | 商品ID→数量映射 |

---

## 3. List — 双向链表，对应 Python `deque`

### 基础操作

```bash
LPUSH  messages  "msg1"  "msg2"  "msg3"   # 左插入 → [msg3, msg2, msg1]
RPUSH  messages  "msg4"                   # 右插入 → [msg3, msg2, msg1, msg4]
LPOP   messages                            # 左弹出 → "msg3"
LRANGE messages  0  -1                     # 查看全部
LTRIM  messages  0  9                      # 只保留前10条
```

### 项目中的实际用途

| 场景 | 命令 | 说明 |
|------|------|------|
| Agent对话历史（滑动窗口） | `LPUSH chat:user5 "{...}"` + `LTRIM chat:user5 0 19` | 只保留最近20轮对话 |
| 后台任务队列 | `LPUSH task_queue "{...}"` + `BRPOP task_queue 0` | 生产者推送，消费者阻塞等待 |
| 最近浏览记录 | `LPUSH recent:user5 "job:42"` + `LTRIM recent:user5 0 9` | 保留最近10条 |

---

## 4. Set — 无序不重复，对应 Python `set`

### 基础操作

```bash
SADD  tags:job:1  "Python"  "FastAPI"  "Redis"
SADD  tags:job:2  "Java"    "Spring"   "Redis"
SADD  tags:job:3  "Python"  "Django"   "PostgreSQL"

SINTER  tags:job:1  tags:job:2          # 交集 → {"Redis"}
SUNION  tags:job:1  tags:job:3          # 并集 → {"Python","FastAPI","Redis","Django","PostgreSQL"}
SDIFF   tags:job:1  tags:job:3          # 差集 → {"FastAPI", "Redis"} (job1有而job3没有)

SISMEMBER  tags:job:1  "Python"         # 判断存在 → 1
```

### 项目中的实际用途

| 场景 | 命令 | 说明 |
|------|------|------|
| 岗位标签交集 | `SINTER resume:me:skills job:5:requirements` | 我的技能 ∩ 岗位要求 = 匹配度 |
| 共同投递者 | `SINTER job:5:applicants job:8:applicants` | 同时投了两个岗位的人 |
| 标签去重 | `SADD all_tags "Python"` (重复添加无影响) | 自动去重 |

---

## 5. ZSet — 有序集合，排行榜专用

### 基础操作

```bash
ZADD  leaderboard  100  "张三"  85  "李四"  92  "王五"
ZREVRANGE  leaderboard  0  -1  WITHSCORES    # 降序 → 张三(100), 王五(92), 李四(85)
ZRANK  leaderboard  "张三"                     # 排名（升序，0开始）
ZINCRBY  leaderboard  5  "李四"               # 加分 → 李四变成90
```

### 项目中的实际用途

| 场景 | 命令 | 说明 |
|------|------|------|
| 岗位匹配度排行 | `ZADD match:resume7 0.85 "job:5" 0.72 "job:8"` | 按匹配度自动排序 |
| RAG检索结果排序 | 分数 = 相关性得分 | 检索结果自然按相关度排 |
| 热度排行 | `ZINCRBY hot_jobs 1 "job:5"` | 每次查看自动+1 |
| 延迟队列 | 分数 = 执行时间戳 | 定时任务按时间排序执行 |

---

## 六、关键认知：Redis vs Python 原生数据结构

```
Python dict/list/set     →  程序重启就没了，只能自己进程用
Redis                    →  独立进程，程序重启数据还在（可选持久化），多个程序共享

关键差异不是"数据结构不同"（几乎一一对应），而是：
1. Redis 是独立的网络服务 → 多进程/多服务器共享
2. Redis 自带过期 → 验证码、缓存TTL不用自己写
3. Redis 操作原子 → 计数、锁不会出现竞态条件
4. Redis 持久化（RDB/AOF）→ 重启不丢数据
```

---

## 实操检查清单

逐条敲完，在 `[ ]` 里打 `[x]`：

- [x] `SET` / `GET` / `INCR` / `SETEX` / `TTL`
- [x] `HSET` / `HGET` / `HGETALL` / `HINCRBY`
- [x] `LPUSH` / `RPUSH` / `LPOP` / `LRANGE` / `LTRIM`
- [x] `SADD` / `SINTER` / `SUNION` / `SDIFF` / `SISMEMBER`
- [x] `ZADD` / `ZREVRANGE` / `ZRANK` / `ZINCRBY`

---

## 下一步

暑假给 `10-fastapi/repository.py` 加 Redis 缓存层时，你自然会用到：
- `SETEX` 缓存岗位列表
- `HSET` 存 Agent 会话状态
- `ZADD` 做岗位匹配度排行
- `LPUSH` + `LTRIM` 管理对话历史
