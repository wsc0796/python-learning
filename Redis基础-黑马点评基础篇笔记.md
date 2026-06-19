---
aliases:
  - Redis基础-黑马点评基础篇
---
# Redis 基础：黑马点评基础篇（01-22集）

> 对应黑马点评 B站视频 基础篇 01-22 集
> 用途：为后续缓存模块、秒杀模块打基础
> 和你的关系：Python dict 你已经很熟了，Redis 就是"网络版 dict + 持久化 + 过期"

---

## 一、Redis 是什么

```
MySQL：数据存硬盘，读写慢，但数据不丢
Redis：数据存内存，读写极快（微秒级），但重启会丢（除非持久化）

所以通常 MySQL 做主存储，Redis 做缓存：
  用户请求 → 先查 Redis → 有就直接返回
                        → 没有 → 查 MySQL → 写回 Redis → 返回
```

**一句话**：Redis 是一个**基于内存的高性能 key-value 数据库**，最常用的场景是**缓存**。

---

## 二、Redis 五种基本数据类型

### 1. String（字符串）— 最基础

```bash
SET name "张三"
GET name              # "张三"
SET age 20
INCR age              # 21  自增1
INCRBY age 5          # 26  自增5
SETEX code 60 "1234"  # 60秒后过期
TTL code              # 剩余秒数
```

**和 Python 的对应**：`{"name": "张三"}` 就是 Redis 里的 String

**常用场景**：
- 缓存 JSON 字符串（对象序列化后存进去）
- 计数器（点赞数、库存数）
- 分布式锁（`SET lock:xxx value NX EX 10`）
- 短信验证码（`SETEX` 设过期时间）

### 2. Hash（哈希）— 存对象

```bash
HSET user:1 name "张三" age 20 city "北京"
HGET user:1 name      # "张三"
HGETALL user:1         # 全部字段
HDEL user:1 age        # 删除字段
```

**和 Python 的对应**：`{"user:1": {"name": "张三", "age": 20}}`

**常用场景**：
- 缓存对象（比 String 存 JSON 更灵活，可以单独改一个字段）
- 购物车（用户ID → {商品ID: 数量}）

### 3. List（列表）— 有序可重复

```bash
LPUSH messages "msg1"  # 左边插入
RPUSH messages "msg2"  # 右边插入
LPOP messages           # 左边弹出
LRANGE messages 0 -1    # 查看全部
```

**和 Python 的对应**：`["msg1", "msg2"]` 但是双向链表

**常用场景**：
- 消息队列（`LPUSH` + `BRPOP` 阻塞等待）
- 最新评论列表
- 朋友圈时间线

### 4. Set（集合）— 无序不重复

```bash
SADD tags:1 "Java" "Spring" "Redis"
SADD tags:2 "Python" "Redis"
SINTER tags:1 tags:2   # 交集 → {"Redis"}
SUNION tags:1 tags:2   # 并集 → {"Java","Spring","Redis","Python"}
SISMEMBER tags:1 "Java" # 判断是否存在
```

**和 Python 的对应**：`{"Java", "Spring", "Redis"}`

**常用场景**：
- 共同关注（交集）
- 文章标签
- 抽奖（`SRANDMEMBER` 随机抽）

### 5. ZSet（有序集合）— 排行榜必备

```bash
ZADD rank 100 "张三" 80 "李四" 95 "王五"
ZRANGE rank 0 -1           # 按分数升序
ZREVRANGE rank 0 -1        # 按分数降序
ZRANK rank "张三"           # 查排名
ZSCORE rank "张三"          # 查分数
```

**和 Python 的对应**：`[("张三", 100), ("李四", 80)]` 但自动按分数排序

**常用场景**：
- 排行榜（积分榜/热搜榜）
- 延迟队列（分数 = 执行时间戳）
- 带权重的标签

---

## 三、Redis 的 Java 客户端

黑马点评用的是 **Spring Data Redis**，底层是 Jedis 或 Lettuce。

### Jedis（原生客户端）

```java
Jedis jedis = new Jedis("localhost", 6379);
jedis.set("name", "张三");
String name = jedis.get("name");
jedis.close();
```

### Spring Data Redis（Spring Boot 集成）

```java
@Autowired
private StringRedisTemplate redisTemplate;

// 存
redisTemplate.opsForValue().set("name", "张三");

// 取
String name = redisTemplate.opsForValue().get("name");

// Hash 操作
redisTemplate.opsForHash().put("user:1", "name", "张三");

// 设过期时间
redisTemplate.opsForValue().set("code", "1234", 60, TimeUnit.SECONDS);
```

**StringRedisTemplate vs RedisTemplate**：
- `StringRedisTemplate`：key 和 value 都是 String（推荐，序列化简单）
- `RedisTemplate`：可以存对象（需要序列化，默认是 JDK 序列化——**不要用，用 JSON 序列化**）

---

## 四、缓存的基本概念

### 缓存能解决什么

```
查 MySQL 一次：10ms
查 Redis 一次：0.1ms（快 100 倍）

如果每秒 1000 个请求 → 1000 次 MySQL 查询 = 数据库扛不住
                      → 1000 次 Redis 查询 = 轻松
```

### 缓存的基本流程

```
1. 请求来了 → 先查 Redis
2. Redis 有 → 直接返回
3. Redis 没有 → 查 MySQL
4. 把 MySQL 结果写入 Redis（设 TTL）
5. 返回数据
```

### 缓存要关心的三个问题

| 问题 | 场景 | 后果 |
|------|------|------|
| **缓存穿透** | 查一个数据库里也不存在的数据 | Redis 永远不命中 → 全打到 MySQL |
| **缓存击穿** | 热点数据的缓存刚好过期 | 大量请求同时打到 MySQL |
| **缓存雪崩** | 大量缓存在同一时间过期 | MySQL 瞬时压力巨大 |

这三个是面试最高频的问题，也是黑马点评的缓存模块核心内容。

---

## 五、Redis 常用命令速查

| 命令 | 作用 |
|------|------|
| `SET key value` | 存字符串 |
| `GET key` | 取字符串 |
| `DEL key` | 删除 |
| `EXISTS key` | 判断是否存在 |
| `EXPIRE key seconds` | 设过期时间 |
| `TTL key` | 查剩余时间（-1=永不过期，-2=已过期/不存在） |
| `KEYS pattern` | 查匹配的 key（**生产禁用**，用 SCAN 代替） |
| `FLUSHALL` | 清空所有数据（**生产禁用**） |

---

## 六、Redis 为什么快

| 原因 | 说明 |
|------|------|
| **纯内存操作** | 绝大多数操作在内存完成，不读写磁盘 |
| **单线程模型** | 没有线程切换开销、没有锁竞争（6.0+ 部分多线程但核心网络IO仍是单线程） |
| **IO 多路复用** | 一个线程同时监听多个连接 |
| **数据结构简单** | 就是为了快而设计的 |

**但单线程不意味着"慢"**——Redis 的主要瓶颈是网络带宽和内存大小，不是 CPU。

---

## 七、你的 Python 背景迁移

| Python | Redis | 区别 |
|--------|-------|------|
| `dict = {}` | `SET key value` + `GET key` | Redis 是独立进程，多个程序共享 |
| `dict["user"] = {...}` | `HSET user:1 name "张三"` | Redis 的 Hash 单字段可修改 |
| `list = [1,2,3]` | `LPUSH list 1 2 3` | Redis 的 List 是双向链表 |
| `set = {1,2,3}` | `SADD set 1 2 3` | 一样，但 Redis 可以求交集/并集 |
| `dict.expire_time` | `EXPIRE key 60` | Redis 原生支持，Python 要自己实现 |

---

## 八、看完视频后你应该能回答

- [ ] Redis 五种数据类型各自适合什么场景？
- [ ] `SETEX` 和 `SET` + `EXPIRE` 有什么区别？（前者是原子操作）
- [ ] 为什么缓存不能永不过期？（内存有限 + 数据可能过时）
- [ ] `KEYS *` 为什么生产环境不能用？（阻塞整个 Redis 实例）
- [ ] StringRedisTemplate 和 RedisTemplate 该用哪个？（用前者，序列化干净）
