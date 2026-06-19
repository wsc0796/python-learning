# 苍穹外卖 Python 内化路线

目标不是“看懂一个 Java 项目”，而是把它拆成你自己的 Python 后端能力：

```text
苍穹外卖 Java/Spring Boot 项目
  -> 抽出业务模型、接口、分层、异常、鉴权、事务、状态流转
  -> 用你已经学过的 Python 路线重新表达
  -> 最后能独立写出一个 FastAPI 版简化外卖后端
```

## 一、先建立总地图

项目源码位置：

```text
D:\sky-take-out-master\sky-take-out-master
```

核心模块：

| Java 模块 | 项目职责 | Python 视角 |
|---|---|---|
| `sky-pojo` | DTO / Entity / VO | Pydantic 输入模型、数据库模型、响应模型 |
| `sky-common` | Result、异常、JWT、常量、工具类 | 统一响应、业务异常、配置、工具函数 |
| `sky-server/controller` | HTTP 接口 | FastAPI router |
| `sky-server/service` | 业务逻辑 | Service 层 |
| `sky-server/mapper` + XML | 数据访问 | Repository / SQLAlchemy |
| `handler` | 全局异常处理 | FastAPI exception handler |
| `interceptor` | JWT 拦截、当前用户上下文 | Depends 鉴权依赖 + contextvars |
| `aspect` | 自动填充创建/更新时间/用户 | 装饰器 / ORM 事件 / Service 辅助函数 |
| `service/state` | 订单状态机 | Enum + 状态模式 |
| `task` | 定时任务 | APScheduler / 后台任务 |
| `websocket` | 催单、订单通知 | FastAPI WebSocket |

## 二、和你的 Python 路线一一对上

| 你已学阶段 | 在苍穹外卖里的影子 | 你要内化出的能力 |
|---|---|---|
| 07 Pydantic | `EmployeeDTO`、`OrdersSubmitDTO`、`EmployeeLoginVO` | 区分输入 DTO、输出 VO、内部 Entity |
| 08 typing + DI | `@Autowired EmployeeService`、`EmployeeMapper` | Service 不直接写死依赖，用构造函数注入 Repository |
| 09 CRUD | 员工、分类、菜品、地址、购物车 | 把接口动作拆成增删改查和业务规则 |
| 10 FastAPI | `@RestController`、`@PostMapping` | 用 router 暴露 HTTP API |
| 11 装饰器 | `@AutoSet` + `AutoSetAspect` | 用装饰器/钩子抽离重复逻辑 |
| 12 设计模式 | `service/state` 订单状态模式 | 用状态机保护订单流转规则 |
| 13 多线程/并发 | WebSocket session、Redis、定时任务 | 理解共享状态、后台任务、连接生命周期 |
| 17 async | WebSocket、外部 HTTP 调用 | 为 FastAPI async 接口和 AI 服务调用打基础 |

## 三、内化顺序

不要从订单开始。订单模块很肥，会把鉴权、购物车、地址、金额、事务、状态机、WebSocket 一起砸过来。

正确顺序：

1. 员工模块：登录、JWT、员工 CRUD、分页
2. 分类模块：最标准的后台 CRUD
3. 菜品模块：主表 + 口味子表，开始理解事务
4. 用户端浏览：分类、菜品、套餐，只读接口
5. 购物车模块：同类商品合并、数量增减
6. 地址模块：当前用户上下文、默认地址
7. 下单模块：订单 + 订单明细 + 清空购物车，事务核心
8. 订单状态机：支付、接单、派送、完成、取消
9. 横切能力：统一异常、统一响应、JWT、自动填充、Redis、定时任务、WebSocket、报表

## 四、每个模块固定流程

沿用你的固定学习流程，但把对象换成真实项目：

```text
读 Java 调用链
  -> 画出请求从 Controller 到 Mapper 的路径
  -> 翻译 DTO / VO / Entity
  -> 写纯 Python Service + Repository
  -> 再挂到 FastAPI
  -> 做破坏实验
  -> 用自己的话复述
```

每次只抓一条链，例如员工登录：

```text
POST /admin/employee/login
  -> EmployeeController.login()
  -> EmployeeService.login()
  -> EmployeeMapper.getByUsername()
  -> Result.success(EmployeeLoginVO)
```

翻译成 Python：

```text
POST /admin/employee/login
  -> router.login()
  -> EmployeeService.login()
  -> EmployeeRepository.get_by_username()
  -> EmployeeLoginVO
```

## 五、第一阶段产物

目录：

```text
C:\Users\50469\python-learning\28-sky-takeout-internalization
```

第一关只做员工模块，不碰数据库，先用内存 Repository：

| 文件 | 作用 |
|---|---|
| `theory_28_employee_module.md` | 员工模块拆解笔记 |
| `practice_28_employee_module.py` | 你手敲 TODO 的练习 |

这关完成后，你应该能不看 Java 代码说清楚：

1. DTO、Entity、VO 为什么要分开。
2. Controller 为什么不要直接写业务。
3. Service 为什么只抛业务异常，不关心 HTTP 状态码。
4. Mapper/Repository 为什么是独立一层。
5. 登录为什么包含“查用户、比密码、查状态、生成 token”四步。

## 六、破坏实验清单

每关至少选一个：

| 模块 | 故意破坏 | 观察点 |
|---|---|---|
| 员工登录 | 密码写错 | Service 抛 `PasswordError`，API 层再转响应 |
| 员工新增 | 重复 username | 业务异常应该比数据库唯一索引更早出现 |
| Pydantic | 手机号少一位 | 请求入口直接被校验拦住 |
| 分页 | pageSize 传 0 | 参数边界要在 DTO 层挡住 |
| 鉴权 | token 缺失 | 依赖/中间件应阻止进入业务层 |
| 订单 | 空购物车下单 | Service 抛业务异常，不应该创建订单 |
| 状态机 | 未付款直接接单 | 状态转换被拒绝 |

## 七、最终目标

你不需要完整复刻所有 Java 细节。真正属于你的版本应该是：

```text
FastAPI
  app/
    api/
    schemas/
    services/
    repositories/
    models/
    core/
    tests/
```

先内存版，再 SQLite/SQLAlchemy 版，最后再补 JWT、Redis、WebSocket、定时任务。这样苍穹外卖就不是“一个看过的项目”，而是你能迁移、能改造、能解释、能重写的后端样本。
