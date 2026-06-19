# FastAPI CRUD 串联项目

这个小项目专门用来把下面几个知识点连起来：

```text
Pydantic 模型
  -> CRUD 业务逻辑
  -> DI 依赖注入
  -> FastAPI 接口
  -> JSON 文件持久化
```

## 推荐阅读顺序

1. `models.py`
   - 看 `TaskCreate` 和 `TaskRead`
   - 理解 Pydantic 如何校验输入数据和规范输出数据

2. `repository.py`
   - 看 `TaskRepository` 这个 `Protocol`
   - 看 `JsonTaskRepository` 如何读写 `tasks.json`
   - 重点看 `TaskRead.model_validate(raw_task)`，这是“从文件读出来后重新校验”

3. `service.py`
   - 看 `TaskService`
   - 这里是真正的 CRUD：新增、查询、完成、删除
   - 注意它只依赖 `TaskRepository`，不关心数据到底存在 JSON、MySQL 还是测试假对象里

4. `dependencies.py`
   - 看 `get_task_service()`
   - 这是 FastAPI 依赖注入的来源函数

5. `main.py`
   - 看 `@app.get()`、`@app.post()` 这些装饰器
   - 看 `Depends(get_task_service)` 如何把 service 注入到接口函数里
   - 看业务异常如何转换成 HTTP 404

## 运行

在本目录执行：

```powershell
uvicorn main:app --reload
```

然后打开：

```text
http://127.0.0.1:8000/docs
```

## 自检

在本目录执行：

```powershell
python run_checks.py
```
