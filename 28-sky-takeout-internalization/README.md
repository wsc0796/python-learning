# 28 - 苍穹外卖内化练习

这一阶段专门把苍穹外卖拆成 Python 后端能力。

## 第一关：员工模块

Java 阅读顺序：

1. `D:\sky-take-out-master\sky-take-out-master\sky-server\src\main\java\com\sky\controller\admin\EmployeeController.java`
2. `D:\sky-take-out-master\sky-take-out-master\sky-server\src\main\java\com\sky\service\impl\EmployeeServiceImpl.java`
3. `D:\sky-take-out-master\sky-take-out-master\sky-server\src\main\java\com\sky\mapper\EmployeeMapper.java`
4. `D:\sky-take-out-master\sky-take-out-master\sky-server\src\main\resources\mapper\EmployeeMapper.xml`
5. `D:\sky-take-out-master\sky-take-out-master\sky-pojo\src\main\java\com\sky\dto\EmployeeDTO.java`
6. `D:\sky-take-out-master\sky-take-out-master\sky-pojo\src\main\java\com\sky\vo\EmployeeLoginVO.java`

Python 练习顺序：

1. 读 `theory_28_employee_module.md`
2. 手敲完成 `practice_28_employee_module.py` 里的 TODO
3. 运行：

```powershell
python practice_28_employee_module.py
```

## 你这关要拿下的东西

- `EmployeeLoginDTO`：登录输入
- `EmployeeDTO`：新增/更新员工输入
- `EmployeeRead`：给前端看的员工信息，不能包含密码
- `EmployeeLoginVO`：登录成功返回 token
- `EmployeeRepository`：模拟 Java Mapper
- `EmployeeService`：模拟 Java ServiceImpl
- 业务异常：账号不存在、密码错误、账号锁定、用户名重复

## 复述模板

完成后不看代码，用这段话复述：

```text
员工登录接口先由 DTO 校验 username/password，
Controller 把 DTO 交给 Service，
Service 通过 Repository 按用户名查员工，
然后判断账号是否存在、密码是否正确、状态是否启用，
通过后生成 token 并返回 VO。
Repository 只负责数据读写，Service 只负责业务规则，HTTP 细节留给 FastAPI 路由层。
```
