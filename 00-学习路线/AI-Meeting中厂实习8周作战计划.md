# AI-Meeting 中厂实习 8 周作战计划

生成日期：2026-05-31

执行周期：2026-06-01 到 2026-07-26

目标岗位：Java 后端实习 / AI 应用开发实习 / 偏全栈 AI 项目实习

核心目标：8 周后达到“能投中厂、能过项目追问、能做小任务、能把经历写进简历”的水平。

---

## 总判断

你现在的起点是 Python 基础，不是 Java/Spring 老手。所以计划不能按“学完整技术栈”设计，而要按“中厂实习最低可用能力”设计。

8 周结束时，你要能做到：

- 能本地跑通 AI-Meeting 后端、前端、测试或构建。
- 能讲清 AI-Meeting 的业务主链路：登录 -> 上传简历 -> AI 出题 -> 答题 -> 评分 -> 追问 -> 报告。
- 能读懂 Spring Boot 的 Controller -> Service -> Mapper/Repository -> DB 分层。
- 能小改一个接口、一个测试、一个前端 service 或一个文档。
- 能讲清 Redis、MongoDB、MySQL 在项目里的分工。
- 能讲清幂等、锁、状态机、SSE、WebSocket、Agent、RAG/Memory 的基本概念。
- 简历上有 2-3 条保守但可验证的项目描述。

一句话：不是追求“精通”，是追求“能进组干活，不露怯”。

---

## 每周强度

推荐强度：每周 45-50 小时。

节奏：

- 周一到周六：每天 6.5-7.5 小时。
- 周日：2-3 小时复盘、模拟面试、补日志，剩余时间休息。

每日标准时间块：

| 时间 | 内容 | 产物 |
|---|---|---|
| 09:00-10:30 | Java/Spring/中间件基础 | 1 页笔记或 5 个问答 |
| 10:45-12:00 | AI-Meeting 源码入口阅读 | 1 张小链路图 |
| 14:00-16:30 | 项目深读/小验证/小修改 | 测试、构建、接口调用或代码片段 |
| 16:45-17:30 | 破坏实验/错误记录 | 失败原因 + 修复思路 |
| 19:30-20:30 | 面试复述/八股/SQL/算法 | 3 个口述题 |
| 20:30-21:00 | 当天学习记录 | 写入 progress 或学习记录 |

如果当天只有 4 小时：

1. 90 分钟项目主链路
2. 60 分钟 Java/Spring 基础
3. 45 分钟验证或小练习
4. 45 分钟复述和记录

如果当天只有 2 小时：

1. 读一个入口文件
2. 画一张链路图
3. 写 150 字复述

---

## 固定学习闭环

每天必须按这个闭环走：

1. 找入口：Controller、Service、hook、service、配置文件。
2. 画链路：请求怎么进来，谁处理，状态存哪里。
3. 跑验证：测试、构建、接口调用、日志都算。
4. 做破坏：故意传错 token、sessionId、status、requestId，观察失败。
5. 复述：用 150 字讲给面试官听。
6. 记录：今天的产物能不能写进简历。

每天记录模板：

```markdown
## YYYY-MM-DD

### 今日目标

### 阅读入口

### 链路图/流程

### 验证命令和结果

### 破坏实验

### 150 字复述

### 可转化为简历/面试的话

### 明天继续
```

建议记录位置：

`C:\Users\50469\python-learning\progress\YYYY-MM-DD_ai_meeting.md`

---

## 第 0 天：启动准备

日期：2026-05-31

用时：1-2 小时。

任务：

- 读完本计划。
- 打开并收藏：
  - `C:\Users\50469\python-learning\00-学习路线\AI-Meeting实习冲刺教学方案.md`
  - `C:\Users\50469\github-projects\AI_MEETING_15_DAY_ONBOARDING.md`
  - 本文件。
- 确认项目路径：
  - 后端：`C:\Users\50469\github-projects\AI-Meeting`
  - 前端：`C:\Users\50469\github-projects\AI-Meeting-Frontend`
- 建一个 Day 1 学习记录。

验收：

- 你知道明天第一件事不是“学 Java 语法”，而是“跑项目 + 画总图”。

---

## Week 1：跑通项目和建立地图

日期：2026-06-01 到 2026-06-07

目标：把 AI-Meeting 从“陌生仓库”变成“我知道它怎么跑、有哪些模块、主链路在哪”。

本周关键词：

- 项目启动
- README
- Maven / npm
- 前后端路径
- 数据库分工
- 总链路图

### Day 1：环境和总图

日期：2026-06-01

任务：

- 读后端 `README.md`、`pom.xml`、`docker-compose.yml`。
- 读前端 `package.json`、`src/lib/request.ts`。
- 跑后端：

```powershell
cd C:\Users\50469\github-projects\AI-Meeting
.\mvnw.cmd -B -ntp test
```

- 跑前端：

```powershell
cd C:\Users\50469\github-projects\AI-Meeting-Frontend
npm run check
```

产物：

- 一张“前端 -> 后端 -> MySQL/Mongo/Redis/AI 服务”的总图。
- 记录测试结果。

### Day 2：仓库地图

日期：2026-06-02

任务：

- 读 `AI-Meeting/skills/xunzhi-repo-map/SKILL.md`。
- 读 `references/common-entrypoints.md`、`request-to-module-map.md`。
- 找出 auth、agent、interview、media、ai、common 模块。

产物：

- 写一份“模块职责表”。
- 能说清 interview 是核心模块，media 是语音模块，agent 是通用聊天模块。

### Day 3：前端请求入口

日期：2026-06-03

任务：

- 读 `src/lib/request.ts`。
- 找 `src/services/interviewService.ts`、authService、agentService。
- 从一个按钮或页面追到后端接口。

产物：

- 画“页面 -> hook -> service -> request -> 后端接口”。

### Day 4：后端请求入口

日期：2026-06-04

任务：

- 找一个简单 Controller。
- 沿 Controller -> Service -> Mapper/Repository -> Entity/DTO 读。
- 对照 `references/fastapi-spring-mapping.md`。

产物：

- 写一段 FastAPI 到 Spring Boot 的类比说明。

### Day 5：统一返回和异常

日期：2026-06-05

任务：

- 找 `Result`、统一异常、全局处理器相关代码。
- 故意找一个异常路径，看错误如何返回给前端。

产物：

- 能解释“后端为什么要统一返回结构”。

### Day 6：跑依赖服务

日期：2026-06-06

任务：

```powershell
cd C:\Users\50469\github-projects\AI-Meeting
docker compose up -d mysql mongo redis
docker compose ps
```

- 看 docker-compose 里 MySQL/Mongo/Redis 配置。
- 不碰真实密钥。

产物：

- 写清每个服务的端口和用途。

### Day 7：周复盘

日期：2026-06-07

任务：

- 复述项目 5 分钟。
- 整理 Week 1 的图和记录。
- 写 10 个问题：
  - 项目是什么？
  - 前后端怎么通信？
  - 后端有哪些模块？
  - MySQL/Mongo/Redis 各存什么？

验收：

- 能不看 README 讲出项目整体结构。

---

## Week 2：Spring Boot 分层和 Java 生存包

日期：2026-06-08 到 2026-06-14

目标：能读懂后端分层，开始具备小改能力。

本周关键词：

- Java 17
- Controller
- DTO
- Service
- Mapper
- MyBatis-Plus
- Validation

### Day 8：Java 最小语法

日期：2026-06-08

任务：

- 学 Java 类、接口、泛型、注解、Optional、Stream 只到能看懂。
- 对照 Python：class、dict/list、typing、decorator。

产物：

- 写一页 Java/Python 对照。

### Day 9：Controller 和 DTO

日期：2026-06-09

任务：

- 找 interview 或 user 的 Controller。
- 读 Request DTO、Response VO、校验注解。

产物：

- 解释 DTO 和 Entity 为什么要分开。

### Day 10：Service 层

日期：2026-06-10

任务：

- 找一个 ServiceImpl。
- 标出它调用了哪些 Mapper、Repository、外部服务。

产物：

- 画 Service 依赖图。

### Day 11：Mapper 和 MyBatis-Plus

日期：2026-06-11

任务：

- 查 MyBatis-Plus Guide，只看 BaseMapper、Service、Wrapper。
- 找项目里的 Mapper。

产物：

- 说明 MyBatis-Plus 省了哪些 CRUD 样板代码。

### Day 12：登录和当前用户

日期：2026-06-12

任务：

- 读 `xunzhi-auth-user/references/login-and-permission.md`。
- 读 `current-user.md`。
- 查 Sa-Token 登录认证。

产物：

- 讲清 token 怎么从前端进入后端。
- 讲清 `@CurrentUser` 为什么比前端传 userId 安全。

### Day 13：做一个小阅读任务

日期：2026-06-13

任务：

- 任选一个简单接口，写出完整调用链。
- 不改大功能，只读懂。

产物：

- 1 份“接口链路说明”。

### Day 14：周复盘

日期：2026-06-14

任务：

- 模拟面试 30 分钟。
- 问题范围：Java 基础、Spring 分层、DTO、Mapper、登录。

验收：

- 能从 Controller 追到数据库。

---

## Week 3：AI-Meeting 核心业务链路

日期：2026-06-15 到 2026-06-21

目标：拿下面试业务主线。

本周关键词：

- 面试会话
- 简历上传
- AI 出题
- 状态机
- 答题
- 评分
- 追问

### Day 15：面试生命周期

日期：2026-06-15

任务：

- 读 `xunzhi-interview-domain/references/lifecycle.md`。
- 读 `state-machine.md`。

产物：

- 画 `DRAFT -> READY -> IN_PROGRESS -> FINISHED`。

### Day 16：创建面试会话

日期：2026-06-16

任务：

- 找创建 session 的 Controller/Facade。
- 看前端创建入口。

产物：

- 讲清“创建会话时创建了什么数据”。

### Day 17：简历上传和回填

日期：2026-06-17

任务：

- 找 resume upload/parse/score/question generation。
- 看 `resumeFileUrl`、`resumeScore`、题目列表如何进入 session。

产物：

- 解释为什么上传简历后不是直接进入面试。

### Day 18：答题流水线第一遍

日期：2026-06-18

任务：

- 读 `answer-pipeline.md`。
- 找 `InterviewAnswerPipeline`。

产物：

- 画“提交回答 -> 参数校验 -> 幂等 -> 锁 -> 评分 -> 追问/推进”。

### Day 19：评分和追问

日期：2026-06-19

任务：

- 读 `scoring-followup-rules.md`。
- 找评分 Agent、追问规则相关代码。

产物：

- 解释 AI 判断和业务规则的关系。

### Day 20：报告和收尾

日期：2026-06-20

任务：

- 读报告生成、finalize、record 相关代码。

产物：

- 解释面试完成后怎么落库、怎么生成报告。

### Day 21：周复盘

日期：2026-06-21

任务：

- 做一次 5 分钟项目主链路讲解。
- 整理 10 个项目追问和答案。

验收：

- 能把 AI-Meeting 核心业务完整讲下来。

---

## Week 4：Redis、MongoDB、幂等、锁、状态恢复

日期：2026-06-22 到 2026-06-28

目标：拿下中厂后端最爱追问的工程点。

本周关键词：

- Redis
- MongoDB
- MySQL
- Redisson
- requestId
- 分布式锁
- 快照
- 恢复

### Day 22：MySQL/Mongo/Redis 分工

日期：2026-06-22

任务：

- 找 session、record、message、snapshot 相关存储。
- 查 Redis data types。
- 查 Spring Data MongoDB。

产物：

- 画三种存储的职责图。

### Day 23：幂等

日期：2026-06-23

任务：

- 找 requestId 幂等服务。
- 理解重复提交为什么危险。

产物：

- 解释“为什么同一个回答不能重复评分”。

### Day 24：锁

日期：2026-06-24

任务：

- 查 Redisson lock 文档。
- 找项目里的同题锁或并发保护。

产物：

- 解释“为什么锁后还要再次校验题号”。

### Day 25：快照和恢复

日期：2026-06-25

任务：

- 读 `restore-and-finalize.md`。
- 找 Redis 快照恢复代码。

产物：

- 解释刷新页面后怎么恢复面试状态。

### Day 26：破坏实验

日期：2026-06-26

任务：

- 构造 3 个失败场景：
  - 重复 requestId
  - 错误 session 状态
  - 错误题号

产物：

- 写失败表现、错误原因、项目防护点。

### Day 27：小测试准备

日期：2026-06-27

任务：

- 找一个适合补测试的 Service 或状态机方法。
- 只设计测试用例，不急着大改。

产物：

- 测试用例清单。

### Day 28：周复盘和第一次试投准备

日期：2026-06-28

任务：

- 整理 Week 1-4 成果。
- 写第一版简历项目描述。
- 可开始小范围试投 3-5 个岗位，用来感受反馈。

验收：

- 项目主链路 + 后端工程点能讲 8 分钟。

---

## Week 5：前端最小闭环和通信机制

日期：2026-06-29 到 2026-07-05

目标：不做前端高手，但能读懂前端怎么调用后端。

本周关键词：

- React
- TypeScript
- Vite
- TanStack Query
- Axios
- SSE
- WebSocket

### Day 29：React/TS 最小生存包

日期：2026-06-29

任务：

- 只学 props、state、hooks、type/interface。
- 看一个面试页面组件。

产物：

- 解释组件、hook、service 的关系。

### Day 30：TanStack Query

日期：2026-06-30

任务：

- 只学 query、mutation、queryKey、invalidate。
- 找项目中使用 query/mutation 的地方。

产物：

- 解释服务端状态为什么不直接全放 Redux。

### Day 31：前端面试页面

日期：2026-07-01

任务：

- 读 InterviewIntroPage / InterviewRoom / Report 相关页面。
- 找它们调用的 hook 和 service。

产物：

- 画页面状态流。

### Day 32：SSE

日期：2026-07-02

任务：

- 查 Spring SSE/Async。
- 找前后端 SSE 代码。

产物：

- 解释为什么 AI 输出适合 SSE。

### Day 33：WebSocket 和语音

日期：2026-07-03

任务：

- 读 `xunzhi-media-domain/references/realtime-asr.md`。
- 查 Spring WebSocket 和讯飞实时语音转写。
- 看前端 audioToTextWs。

产物：

- 解释 WebSocket 和 SSE 的区别。

### Day 34：前端小修或文档

日期：2026-07-04

任务：

- 选一个前端 service 的字段兼容、错误提示、测试或文档说明。
- 跑：

```powershell
cd C:\Users\50469\github-projects\AI-Meeting-Frontend
npm run check
```

产物：

- 1 个小修改或 1 份前端链路文档。

### Day 35：周复盘

日期：2026-07-05

任务：

- 复述一次“从页面点击到后端返回”的完整链路。

验收：

- 面试官问“前端怎么调你的接口”，你能回答。

---

## Week 6：AI 应用能力和工程保护

日期：2026-07-06 到 2026-07-12

目标：把 AI-Meeting 的 AI 亮点讲得像工程，不像背概念。

本周关键词：

- Spring AI
- Agent
- RAG
- Memory
- Prompt
- AI Guard
- SingleFlight
- 限流

### Day 36：Spring AI 和模型接入

日期：2026-07-06

任务：

- 查 Spring AI 1.0 文档，只看 Chat Client / model 调用概念。
- 读项目 AI runtime 入口。

产物：

- 解释项目为什么要封装统一 AI 调用层。

### Day 37：Agent 概念和项目 Agent

日期：2026-07-07

任务：

- 读 `xunzhi-agent-domain/references/session-flow.md`。
- 对照 Al.pdf 的 Agent 相关内容。

产物：

- 解释 Agent 和普通 LLM 调用的区别。

### Day 38：RAG 和 Memory

日期：2026-07-08

任务：

- 读 Al.pdf 中 RAG、短期记忆、长期记忆相关页。
- 对照 AI-Meeting 的会话状态治理。

产物：

- 解释“知识库 RAG”和“面试状态恢复”不是一回事。

### Day 39：AI Guard

日期：2026-07-09

任务：

- 读 `xunzhi-ai-runtime/references/ai-guard.md`。

产物：

- 解释 AI 调用为什么需要超时、降级、保护。

### Day 40：SingleFlight 和限流

日期：2026-07-10

任务：

- 读 `ai-singleflight.md`、`flow-limit.md`。

产物：

- 解释 SingleFlight 解决什么重复请求问题。

### Day 41：AI CR 和单测 Prompt

日期：2026-07-11

任务：

- 用 Al.pdf 的 AI CR/单测思路审一个小模块。
- 不是盲信 AI，而是人工判断建议是否合理。

产物：

- 1 份小型 Code Review 记录。

### Day 42：周复盘

日期：2026-07-12

任务：

- 模拟 AI 应用开发面试 45 分钟。

验收：

- 能讲 AI/RAG/Agent/Memory，但不会把没做过的说成自己实现过。

---

## Week 7：测试、小修复、作品集证据

日期：2026-07-13 到 2026-07-19

目标：把“学习过”升级成“我做过一个可验证改动”。

本周关键词：

- JUnit
- Mockito
- Vitest
- 小修复
- 文档
- README
- commit plan

### Day 43：后端测试阅读

日期：2026-07-13

任务：

- 找项目已有测试。
- 学 JUnit 5、Mockito 的基本结构。

产物：

- 写出 Arrange / Act / Assert 对照。

### Day 44：补一个后端测试

日期：2026-07-14

任务：

- 选择一个小 Service 或状态校验。
- 补测试。
- 跑相关测试。

产物：

- 1 个测试改动。

### Day 45：前端测试或 check

日期：2026-07-15

任务：

- 看 Vitest 测试。
- 如果前端测试成本高，就做 service 兼容逻辑和 check。

产物：

- 1 个前端验证记录。

### Day 46：项目文档

日期：2026-07-16

任务：

- 写一份“AI-Meeting 面试答题流水线说明”。
- 内容只写你读懂的，不夸大。

产物：

- 1 份项目文档，可作为面试讲稿底稿。

### Day 47：README/简历素材

日期：2026-07-17

任务：

- 整理 3 条简历 bullet。
- 标注每条背后的证据文件、验证命令。

产物：

- 第一版简历项目经历。

### Day 48：完整验证

日期：2026-07-18

任务：

```powershell
cd C:\Users\50469\github-projects\AI-Meeting
.\mvnw.cmd -B -ntp test

cd C:\Users\50469\github-projects\AI-Meeting-Frontend
npm run check
```

产物：

- 验证记录。

### Day 49：周复盘

日期：2026-07-19

任务：

- 判断哪些内容可公开，哪些只留私有学习笔记。
- 准备正式投递材料。

验收：

- 至少有 1 个小测试/小修复/文档产物能证明你不是只看过。

---

## Week 8：面试冲刺和投递

日期：2026-07-20 到 2026-07-26

目标：把项目、基础、八股、简历讲顺。

本周关键词：

- 模拟面试
- 简历
- 项目追问
- Java 基础
- Spring
- MySQL
- Redis
- HTTP
- AI 项目话术

### Day 50：项目 5 分钟讲稿

日期：2026-07-20

任务：

- 写 5 分钟项目介绍。
- 结构：
  - 项目背景
  - 核心业务
  - 技术架构
  - 重点链路
  - 我做的验证/小修
  - 遇到的问题

产物：

- 5 分钟讲稿。

### Day 51：Java/Spring 面试题

日期：2026-07-21

任务：

- Java 基础 20 题。
- Spring Boot 分层、依赖注入、事务、异常处理 20 题。

产物：

- 40 个问答。

### Day 52：MySQL/Redis 面试题

日期：2026-07-22

任务：

- MySQL 索引、事务、SQL 基础。
- Redis 缓存、数据结构、锁、过期、穿透/击穿/雪崩。

产物：

- 30 个问答。

### Day 53：项目追问

日期：2026-07-23

任务：

- 准备 20 个 AI-Meeting 项目追问：
  - 为什么用 Redis？
  - 为什么用 Mongo？
  - requestId 怎么做幂等？
  - 锁粒度怎么选？
  - SSE 和 WebSocket 区别？
  - AI 调用失败怎么办？

产物：

- 20 个项目追问答案。

### Day 54：AI/RAG/Agent 话术

日期：2026-07-24

任务：

- 用 Al.pdf 的框架整理 AI 项目表达。
- 严格区分“我理解过”和“我实现过”。

产物：

- 10 个 AI 应用追问答案。

### Day 55：模拟面试

日期：2026-07-25

任务：

- 模拟 2 轮：
  - 1 轮后端基础
  - 1 轮项目深挖

产物：

- 记录卡住的问题，补答案。

### Day 56：正式投递周复盘

日期：2026-07-26

任务：

- 简历定稿。
- 投递 10-20 个岗位。
- 建立投递表：公司、岗位、投递日期、进度、面试问题。

验收：

- 你已经可以开始中厂实习投递，并能承受第一轮项目追问。

---

## 每周验收表

| 周次 | 必须产物 | 不达标补救 |
|---|---|---|
| Week 1 | 项目总图、模块职责表、跑通记录 | 延后新内容，先补环境和地图 |
| Week 2 | 1 条后端接口完整链路 | 继续读 Controller/Service，不急着 AI |
| Week 3 | 面试主链路图、10 个项目问答 | 重读 lifecycle/answer-pipeline |
| Week 4 | Redis/Mongo/MySQL 分工图、幂等和锁说明 | 用破坏实验补理解 |
| Week 5 | 前端调用链路、SSE/WebSocket 对比 | 只保留前端 service/hook 阅读 |
| Week 6 | AI/RAG/Agent/Guard 话术 | 用 Al.pdf 框架重写 |
| Week 7 | 1 个测试/小修/文档产物 | 不许只写学习笔记，必须有验证 |
| Week 8 | 简历、讲稿、模拟面试记录、投递表 | 继续模拟到能讲顺 |

---

## 简历版本控制

第 4 周末：

- 可以写“学习并梳理 AI 模拟面试平台核心链路”。
- 不要写“负责开发”。

第 7 周末：

- 如果完成测试或小修，可以写“为局部模块补充测试/修复兼容逻辑”。
- 必须有验证命令。

第 8 周末：

- 简历项目 bullet 应该类似：

```text
参与 AI 模拟面试平台学习与二次验证，梳理登录、简历上传、AI 出题、答题评分、追问和报告生成链路，输出面试会话生命周期与答题流水线说明。
阅读并验证 Spring Boot + MyBatis-Plus + Redis + MongoDB 的状态治理方案，理解 requestId 幂等、同题锁、状态机推进和 Redis 快照恢复机制。
为项目局部模块补充测试/修复小问题，并通过 Maven/Vitest 校验，沉淀问题定位和验证记录。
```

如果没有完成测试或小修，第三条不要写。

---

## 投递节奏

不要等到“全部学完”再投。

- 2026-06-28：小范围试投 3-5 个，收集岗位要求和反馈。
- 2026-07-13：开始每周投 10 个左右。
- 2026-07-26：正式进入高强度投递，10-20 个岗位。

投递优先级：

1. Java 后端实习，技术栈含 Spring Boot/MySQL/Redis。
2. AI 应用开发实习，要求 RAG/Agent/Prompt/LLM API，但不要求算法训练。
3. 偏全栈实习，React + Spring Boot。

暂时不优先：

- 纯算法岗。
- 要求深度学习训练/论文/模型微调的岗位。
- 要求强 C++ 或底层基础设施的岗位。

---

## 面试题清单

第 8 周前必须能答：

Java/Spring：

- Java 面向对象、接口、泛型、异常。
- Spring Boot 分层。
- 依赖注入是什么。
- Controller/Service/Mapper 各自职责。
- DTO/Entity/VO 区别。
- 全局异常和统一返回。

数据库/Redis：

- MySQL 索引基本原理。
- 事务 ACID。
- Redis 常用数据结构。
- 缓存穿透、击穿、雪崩。
- 分布式锁为什么需要过期时间。
- Redisson 锁解决什么问题。

项目：

- AI-Meeting 是什么。
- 面试 session 生命周期。
- 答题流水线。
- requestId 幂等。
- 同题锁。
- Redis/Mongo/MySQL 分工。
- SSE 和 WebSocket 区别。
- AI 调用失败怎么办。
- 追问规则为什么不能只信 AI。

AI 应用：

- RAG 是什么。
- 短期记忆和长期记忆区别。
- Agent 和普通对话区别。
- Function Calling/MCP 了解到什么程度。
- Prompt 如何结构化。
- AI CR 和单测生成如何在开发流程中用。

---

## 红线

这些事会拖慢你：

- 试图先把 `python-learning` 所有 TODO 清完。
- 深挖 React 动画、样式、组件库。
- 深挖 Spring 源码。
- 背高级名词，但项目链路讲不出来。
- 简历写“主导”“精通”“负责架构设计”。
- 没有验证命令就写自己做过。

这些事要坚持：

- 每天画一个小链路。
- 每天跑一个验证。
- 每天写 150 字复述。
- 每周至少一次模拟面试。
- 第 7 周前必须做出一个可验证产物。

---

## 明天开始做什么

2026-06-01 第一任务：

```powershell
cd C:\Users\50469\github-projects\AI-Meeting
.\mvnw.cmd -B -ntp test
```

第二任务：

```powershell
cd C:\Users\50469\github-projects\AI-Meeting-Frontend
npm run check
```

第三任务：

- 画项目总图。
- 写 Day 1 学习记录。
- 用 150 字回答：“AI-Meeting 到底是什么项目？”

这是整个 8 周的第一块砖。
