# AI-Meeting 实习冲刺教学方案

生成日期：2026-05-31

目标：用半个月把 AI-Meeting 项目学到“能跑、能讲、能改、能写进简历”的实习入门程度。

---

## 结论

`C:\Users\50469\python-learning` 可以作为学习 AI-Meeting 的底座，但不能单独覆盖这个项目的完整技术栈。

它能帮你解决：

- 学习方法：`python学习固定流程.md` 的“理论 -> 手敲 -> 破坏实验 -> 验证 -> 复述 -> 记录”非常适合继续用。
- 分层理解：`07-pydantic`、`08-typing-di`、`10-fastapi`、`33-notes-api` 可以迁移到 Spring Boot 的 Controller/DTO/Service/Repository 思维。
- AI 基础：`18-llm-coze-workflow`、`19-llm-finetune-rag-agent-projects` 和 `Al.pdf` 能补 RAG、Memory、Agent、Prompt、AI CR、单测生成。
- Redis/项目表达：`黑马点评-速通计划.md`、Redis 笔记、`AI项目对照-Al.pdf-vs-AI-Meeting.md` 可以辅助理解缓存、锁、项目话术。

它暂时不能直接解决：

- Java 17、Spring Boot 3、Spring AI 的工程写法。
- MyBatis-Plus、Sa-Token、Redisson、Spring Data MongoDB 的真实项目用法。
- React + TypeScript + Vite + TanStack Query 的前端阅读能力。
- LiteFlow 规则链、SSE、WebSocket、讯飞实时语音转写这些 AI-Meeting 的项目特性。

所以正确路线不是“先把 python-learning 全部补完”，而是：

> 用 python-learning 的学习方法和类比能力，直接围绕 AI-Meeting 核心链路补最小技术栈。

---

## 学习流改造

原来的 Python 学习流：

1. 读 theory
2. 手敲 practice TODO
3. 做破坏实验
4. 跑通验证
5. 记录错误
6. 口头复述
7. 24h 回顾

改造成项目实习版：

1. 找入口：先定位 Controller/API/页面/Service。
2. 画链路：画出“请求从哪里来，经过谁，数据落到哪里”。
3. 跑验证：跑测试、启动服务、调用接口或构造前端页面行为。
4. 小修改：只改一个字段、一个校验、一个测试、一个文档说明。
5. 破坏实验：故意改错 token、sessionId、status、requestId、Redis key，看项目怎么失败。
6. 复述：用 150 字讲清“业务背景 -> 技术方案 -> 为什么这样做 -> 风险”。
7. 简历转化：每天只沉淀 1 条可以被验证的经历，不写虚的。

每天验收口径：

- 不是“我看完了”，而是“我能画图、能跑命令、能解释一个 bug 为什么会发生”。

---

## 本地材料怎么用

| 本地材料 | 用法 | 优先级 |
|---|---|---|
| `python学习固定流程.md` | 保留学习节奏，改成项目版七步 | 高 |
| `00-学习路线/07-10阶段串联复盘.md` | 把 FastAPI/Pydantic/DI/CRUD 映射到 Spring Boot | 高 |
| `references/fastapi-spring-mapping.md` | 每次读 Java Controller 时对照看 | 高 |
| `33-notes-api` | 复习分层、依赖注入、测试 | 中 |
| `34-todo-api` | 不急着全做，只补 Service/Repository/测试思路 | 中 |
| `18-llm-coze-workflow` | 理解工作流、知识库、RAG 入门 | 高 |
| `19-llm-finetune-rag-agent-projects` | 理解 Agent/RAG/Function Call 概念 | 高 |
| `Al.pdf` | 学 AI 项目表达、AI CR、单测 Prompt、RAG/Memory 话术 | 高 |
| `AI项目对照-Al.pdf-vs-AI-Meeting.md` | 用 Al.pdf 的话术讲 AI-Meeting | 高 |
| `黑马点评-速通计划.md` / Redis 笔记 | 补 Redis、锁、缓存、高并发基本话术 | 中 |

不要现在做：

- 不要把 01-27 所有 Python TODO 全刷完。
- 不要深挖前端 UI 样式。
- 不要背 README 里的高级简历句。
- 不要一开始就改大功能。

---

## Al.pdf 的正确用法

这份 PDF 不是让你从第 1 页啃到第 266 页，而是按 AI-Meeting 的需求抽取。

优先读：

1. AI 怎么用于开发流程：AI CR、单元测试生成、Prompt 结构化。
2. 学习步骤：先基础知识，再项目背景和话术，再面经问题。
3. Memory：短期记忆、长期记忆、上下文窗口、摘要、Redis/向量存储。
4. RAG：Query Rewriting、Embedding、向量库、BM25、混合检索、召回率/精确率。
5. Agent/Function Calling/MCP：作为面试概念补充，不要喧宾夺主。

迁移方式：

- Al.pdf 讲“团队知识库系统”的话术。
- AI-Meeting 是“AI 模拟面试平台”的真实代码。
- 你要做的是：用 Al.pdf 的“背景 -> 痛点 -> 方案 -> 优化 -> 结果”框架，讲 AI-Meeting 的“登录 -> 简历 -> 出题 -> 答题 -> 评分 -> 追问 -> 报告”链路。

---

## 官方资料索引

这些资料只作为查漏补缺，不要从头看完。

后端主线：

- Spring Boot 3.4 Reference：https://docs.spring.io/spring-boot/3.4/reference/index.html
- Spring AI 1.0 Reference：https://docs.spring.io/spring-ai/reference/1.0/index.html
- MyBatis-Plus Guide：https://mybatis.plus/en/guide/
- Sa-Token 文档：https://sa-token.cc/doc.html
- Spring Data MongoDB：https://docs.spring.io/spring-data/mongodb/reference/index.html
- Redis Data Types：https://redis.io/docs/latest/develop/data-types/
- Redisson Locks：https://redisson.pro/docs/data-and-services/locks-and-synchronizers/index.html
- LiteFlow Spring Boot：https://liteflow.cc/pages/9bf6be/

前端主线：

- React TypeScript：https://react.dev/learn/typescript
- Vite Guide：https://vite.dev/guide/
- TanStack Query React：https://tanstack.com/query/latest/docs/react/

通信和语音：

- Spring MVC SSE/Async：https://docs.enterprise.spring.io/spring-framework/reference/web/webmvc/mvc-ann-async.html
- Spring WebSocket：https://docs.spring.io/spring-framework/reference/web/websocket.html
- 讯飞实时语音转写：https://www.xfyun.cn/doc/asr/rtasr/API.html

---

## 项目路径和基线命令

项目路径：

- 后端：`C:\Users\50469\github-projects\AI-Meeting`
- 前端：`C:\Users\50469\github-projects\AI-Meeting-Frontend`
- 学习方案：`C:\Users\50469\python-learning\00-学习路线\AI-Meeting实习冲刺教学方案.md`
- 另一份冲刺图：`C:\Users\50469\github-projects\AI_MEETING_15_DAY_ONBOARDING.md`

项目版本以本地仓库为准：

- 后端：Java 17、Spring Boot 3.4.4、Spring AI 1.0.0、MyBatis-Plus 3.5.9、Redisson 3.27.2、LiteFlow 2.15.3.2。
- 前端：React 19.2、TypeScript 5.9、Vite 7.3、TanStack Query 5.90。

后端验证：

```powershell
cd C:\Users\50469\github-projects\AI-Meeting
.\mvnw.cmd -B -ntp test
.\mvnw.cmd -B -ntp -Dmaven.test.skip=true clean verify
```

前端验证：

```powershell
cd C:\Users\50469\github-projects\AI-Meeting-Frontend
npm run check
npm run build
```

依赖服务：

```powershell
cd C:\Users\50469\github-projects\AI-Meeting
docker compose up -d mysql mongo redis
```

注意：第三方 AI/讯飞相关密钥不要写进公开简历或公开仓库。

---

## 15 天路线

每天固定产物：

- 1 张链路图或 1 段 150 字解释。
- 1 个验证动作：测试、构建、接口调用、日志截图、代码小改、文档补充任选其一。
- 1 条面试可讲材料：不要超过 3 句话。

### Day 1：建立项目地图

目标：知道 AI-Meeting 是什么、前后端在哪里、怎么验证。

任务：

- 读 `AI-Meeting/README.md`、`docker-compose.yml`、后端 `pom.xml`。
- 读 `AI-Meeting-Frontend/package.json`、`src/lib/request.ts`。
- 读 `AI-Meeting/skills/xunzhi-repo-map/references/common-entrypoints.md`。
- 跑后端测试和前端 check/build。

输出：

- 一张“前端页面 -> 后端接口 -> 数据库/Redis/Mongo/AI 服务”的总图。
- 口述：这个项目是 AI 模拟面试平台，不是普通 CRUD。

### Day 2：Spring Boot 分层生存包

目标：用 FastAPI 类比读懂 Spring Boot。

本地对照：

- `references/fastapi-spring-mapping.md`
- `00-学习路线/07-10阶段串联复盘.md`

任务：

- 找 1 个 Controller，沿着 Controller -> Service -> Mapper/Repository -> Entity/DTO 读。
- 对照 FastAPI：route -> Pydantic schema -> dependency/service -> repository。
- 故意找一个异常处理路径，看统一返回怎么处理。

输出：

- 解释“DTO 为什么不是 Entity”。
- 解释“Controller 不应该写复杂业务逻辑”。

### Day 3：登录、权限、当前用户

目标：拿下“谁在操作”的链路。

任务：

- 读 `xunzhi-auth-user/references/login-and-permission.md`。
- 读 `xunzhi-auth-user/references/current-user.md`。
- 读前端 `src/lib/request.ts` 和 auth service。
- 查 Sa-Token 文档，只看登录认证、权限认证、Redis 集成。

输出：

- 解释 token 怎么从前端请求进入后端。
- 解释为什么后端要用 `@CurrentUser`，不能相信前端传 userId。

### Day 4：MySQL、MyBatis-Plus、基础数据

目标：看懂持久层。

任务：

- 查 MyBatis-Plus Guide，只看 Mapper、Service、条件构造器。
- 找用户表或面试会话相关 Entity/Mapper。
- 看一次增删改查如何被封装。

输出：

- 画 Controller -> Service -> Mapper -> MySQL。
- 能讲清 MyBatis-Plus 帮你省了哪些 CRUD 样板代码。

### Day 5：React/TypeScript/Vite 最小阅读能力

目标：能从页面找到请求。

任务：

- 查 React TypeScript，只看 props、state、hooks 类型。
- 查 Vite Guide，只知道项目怎么启动、env 怎么读。
- 查 TanStack Query，只知道 query/mutation/queryKey 是干什么的。
- 在前端找“创建面试/进入面试间/报告页”的页面和 service。

输出：

- 画 页面组件 -> hook -> service -> request -> 后端接口。
- 能解释“前端状态”和“服务端状态”的区别。

### Day 6：普通 Agent 聊天和 SSE

目标：先理解简单 AI 流式对话，再进面试核心链路。

任务：

- 读 `xunzhi-agent-domain/references/session-flow.md`。
- 读 `xunzhi-ai-runtime/references/agent-binding.md`。
- 查 Spring SSE/Async 文档，理解 `SseEmitter` / `text/event-stream`。
- 找前端 SSE hook。

输出：

- 解释 SSE 为什么适合 AI 流式输出。
- 解释一次聊天消息如何保存历史。

### Day 7：面试会话生命周期

目标：拿下主业务的状态流。

任务：

- 读 `xunzhi-interview-domain/references/lifecycle.md`。
- 读 `xunzhi-interview-domain/references/state-machine.md`。
- 找面试 session Controller/Facade。

输出：

- 画 `DRAFT -> READY -> IN_PROGRESS -> FINISHED` 状态图。
- 解释状态机为什么比散落 if/else 更稳。

### Day 8：简历上传和 AI 出题

目标：理解“简历进入系统后发生什么”。

任务：

- 找 resume upload / parse / score / question generation 相关入口。
- 看文件 URL、面试类型、题目列表如何回填到 session。
- 对照 Al.pdf 的“项目背景 -> 痛点 -> 方案”写 150 字说明。

输出：

- 解释为什么上传简历后不是立刻开始面试，而是要生成结构化结果。

### Day 9：答题流水线

目标：拿下最重要、最能写简历的一条链路。

任务：

- 读 `xunzhi-interview-domain/references/answer-pipeline.md`。
- 读幂等、题号校验、同题锁、评分、追问、推进下一题相关代码。
- 查 Redisson Locks，理解分布式锁只学到能讲清即可。

输出：

- 画“提交回答 -> 幂等 -> 锁 -> 评分 -> 追问/推进 -> 刷新快照”。
- 解释为什么要 requestId 幂等。
- 解释为什么锁后还要再次校验题号。

### Day 10：追问规则和 LiteFlow

目标：理解 AI 判断不等于最终业务决策。

任务：

- 读 `xunzhi-interview-domain/references/scoring-followup-rules.md`。
- 读 LiteFlow Spring Boot 官方文档，只看组件、规则文件、执行链。
- 看项目里的 follow-up rule yaml/xml。

输出：

- 解释“AI 说要追问”为什么还要经过规则链。
- 解释追问次数上限、主问题推进、评分之间的关系。

### Day 11：Redis、MongoDB、会话恢复

目标：理解长会话状态治理。

任务：

- 读 `xunzhi-interview-domain/references/restore-and-finalize.md`。
- 查 Spring Data MongoDB，只看 Repository/MongoTemplate/文档映射。
- 查 Redis Data Types，只看 string/hash/list/set/zset 的用途。
- 找 Redis 快照、Mongo 消息历史、MySQL session 的分工。

输出：

- 画 MySQL/Mongo/Redis 三者分工图。
- 解释为什么不能把所有状态只放内存里。

### Day 12：AI Guard、SingleFlight、限流

目标：理解工程亮点，不背概念。

任务：

- 读 `xunzhi-ai-runtime/references/ai-guard.md`。
- 读 `xunzhi-ai-runtime/references/ai-singleflight.md`。
- 读 `xunzhi-ai-runtime/references/flow-limit.md`。

输出：

- 解释 SingleFlight 解决“同一个昂贵请求被重复打爆”的问题。
- 解释限流、降级、超时为什么对 AI 调用特别重要。

### Day 13：语音转写和 WebSocket

目标：知道 ASR/TTS 在项目里的位置。

任务：

- 读 `xunzhi-media-domain/references/realtime-asr.md`。
- 读 `xunzhi-media-domain/references/websocket-notification.md`。
- 查 Spring WebSocket 和讯飞实时语音转写文档。
- 看前端 `audioToTextWs` 相关文件。

输出：

- 解释 WebSocket 和 SSE 的区别。
- 解释实时语音为什么适合 WebSocket 而不是普通 HTTP。

### Day 14：测试、AI CR、修一个小点

目标：把学习变成可验证工程痕迹。

任务：

- 用 Al.pdf 的 AI CR/单测 Prompt 思路，审一个小文件或补一个测试。
- 优先选择 Service、状态机、DTO 校验、前端 service 兼容逻辑。
- 跑对应测试或 check。

输出：

- 1 个小修复或 1 个测试。
- 说明：改了什么，为什么改，如何验证。

### Day 15：简历、项目讲解、模拟面试

目标：把 14 天内容变成能讲的话。

任务：

- 整理 3 条简历 bullet。
- 准备 10 个面试问答。
- 做一次 5 分钟项目介绍。

输出：

- 1 份保守、真实、可验证的简历写法。
- 1 份“项目介绍 -> 核心链路 -> 技术亮点 -> 我做了什么 -> 遇到的问题”的讲稿。

---

## 简历转化模板

不要写：

- 主导 AI 模拟面试平台开发。
- 精通 Spring AI、LiteFlow、多 Agent 编排。
- 负责全链路架构设计。

可以写：

- 参与学习并梳理 AI 模拟面试平台核心链路，输出面试会话生命周期、答题流水线、SSE/ASR 通信链路等项目文档。
- 基于 Spring Boot 3 + Redis + MongoDB + MySQL 阅读并验证面试会话状态治理流程，理解 requestId 幂等、同题锁、状态机推进和快照恢复机制。
- 为项目局部模块补充测试或修复兼容逻辑，并通过 Maven/Vitest 校验，沉淀可复盘的问题定位记录。

等你真的完成 Day 14 的小修复/测试后，再把“参与学习并梳理”升级成“补充测试/修复问题”。

---

## 实习达标标准

到第 15 天，你至少要做到：

- 能本地跑后端、前端、测试/构建。
- 能解释 Controller -> Service -> Mapper/Repository -> DB 的请求链路。
- 能解释前端页面 -> hook -> service -> request -> 后端接口。
- 能讲清 MySQL/Mongo/Redis 分别存什么。
- 能讲清 SSE 和 WebSocket 区别。
- 能讲清面试 session 生命周期。
- 能讲清答题流水线的幂等、锁、评分、追问、推进。
- 能讲清 LiteFlow 在追问规则中的作用。
- 能讲清 AI Guard/SingleFlight/限流为什么存在。
- 能做一个很小的测试或 bug 修复，并说清验证命令。

如果只做到“我看过”，不算达标。

如果能做到“我能画、能跑、能改一小点、能讲风险”，就已经够实习入门了。

---

## 每天记录模板

```markdown
## YYYY-MM-DD AI-Meeting 学习记录

### 今天目标
- 

### 读了哪些入口
- 

### 画出的链路
- 

### 做了什么验证
命令：
结果：

### 破坏实验
我故意改了：
项目如何失败：
我学到：

### 150 字复述

### 可写进简历/面试的话

### 明天继续
```

---

## 第一优先级清单

如果时间真的很紧，只保这 6 条：

1. Day 1 项目跑通和总图。
2. Day 2 Spring Boot 分层。
3. Day 7 面试 session 生命周期。
4. Day 9 答题流水线。
5. Day 11 Redis/Mongo/MySQL 状态治理。
6. Day 14 小测试或小修复。

这 6 条能让你从“只会 Python 的旁观者”，变成“能进项目、能跟需求、能定位链路的实习生”。
