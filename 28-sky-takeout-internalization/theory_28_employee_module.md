# theory 28 - 员工模块：把 Spring Boot 翻译成 Python

## 1. 员工登录调用链

Java 版：

```text
EmployeeController.login(EmployeeLoginDTO)
  -> EmployeeServiceImpl.login(EmployeeLoginDTO)
  -> EmployeeMapper.getByUsername(username)
  -> JwtUtil.createJWT(...)
  -> Result.success(EmployeeLoginVO)
```

Python 版先按这个心智模型写：

```text
login_route(EmployeeLoginDTO)
  -> EmployeeService.login(EmployeeLoginDTO)
  -> EmployeeRepository.get_by_username(username)
  -> create_token(...)
  -> EmployeeLoginVO
```

注意：第一关先写纯 Python，不急着接 FastAPI。你先把业务吃透，再挂 HTTP。

## 2. DTO / Entity / VO 的区别

| 名字 | Java 文件 | Python 对应 | 作用 |
|---|---|---|---|
| LoginDTO | `EmployeeLoginDTO` | `EmployeeLoginDTO(BaseModel)` | 外部登录输入 |
| DTO | `EmployeeDTO` | `EmployeeDTO(BaseModel)` | 新增/更新输入 |
| Entity | `Employee` | `EmployeeRecord(BaseModel)` | 仓库内部保存的数据 |
| VO | `EmployeeLoginVO` | `EmployeeLoginVO(BaseModel)` | 返回给前端的数据 |

最重要的一点：密码只能存在内部记录里，不能出现在 `EmployeeRead` / `EmployeeLoginVO` 这种响应模型里。

## 3. Service 层的四个判断

`EmployeeServiceImpl.login()` 做的是业务规则，不是 HTTP：

1. 根据用户名查员工。
2. 查不到：账号不存在。
3. 查到了但密码不对：密码错误。
4. 密码对但状态为禁用：账号锁定。
5. 全部通过：返回员工信息，外层再生成/返回 token。

Python 里也一样：Service 抛业务异常，不直接返回 404、401 这些 HTTP 细节。

## 4. Mapper 翻译成 Repository

Java 的 `EmployeeMapper`：

```text
getByUsername(username)
insertEmployee(employee)
listEmployee(query)
getById(id)
update(employee)
```

Python 第一关先用内存仓库表达：

```text
get_by_username(username)
insert(employee)
list_employees(name=None)
get_by_id(employee_id)
update(employee)
```

以后换成 SQLAlchemy 时，Service 不应该大改。这就是 DI 的价值。

## 5. 和你前面章节的连接

- Pydantic：做 DTO/VO 校验和输出过滤。
- typing/Protocol：给 Repository 定义行为约定。
- CRUD：新增、查询、更新状态、分页查询。
- DI：Service 依赖 Repository，而不是自己 new 数据库。
- 异常：业务异常从 Service 抛出，FastAPI 层统一转换。
- 装饰器/AOP：后面再把创建时间、更新时间、当前用户自动填充抽出去。

## 6. 破坏实验

完成练习后，至少做一个：

1. 把登录密码改错，观察是否抛 `PasswordError`。
2. 把管理员状态改为 0，观察是否抛 `AccountLockedError`。
3. 新增一个重复用户名，观察是否抛 `DuplicateUsernameError`。
4. 把手机号改成 `123`，观察 Pydantic 是否在入口拦住。

把你的观察写到文件底部注释区：现象、猜测、真实原因、下次怎么定位。
