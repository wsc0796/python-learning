# 明天（5/10）6小时计划 — 执行版

目标：Day 6 FastAPI

---

## 文件清单（已全部生成）

| 时段 | 内容 | 文件 |
|------|------|------|
| **09:00-09:30** | Hot100 热身 | `hot100/week1_day2_49_step_by_step.py`（is_anagram填空） |
| | | `hot100/week1_day2_11_container_water.py`（读题+填空） |
| | | `06-dict/practice_06_dict.py`（练习1-3） |
| | | ← 其中 06-dict 练习1-3 放在最后做 |
| **09:30-10:30** | Day 3 Pydantic | `07-pydantic/theory_07_pydantic.md` |
| | | `07-pydantic/practice_07_pydantic.py`（5个练习） |
| **10:30-11:30** | Day 4 类型提示+DI | `08-typing-di/theory_08_typing_di.md` |
| | | `08-typing-di/practice_08_typing_di.py`（5个练习） |
| **11:30-11:40** | 休息 | |
| **11:40-13:10** | Day 5 综合CRUD | `09-crud/theory_09_crud.md` |
| | | `09-crud/practice_09_crud.py`（5步） |
| **13:10-13:20** | 休息 | |
| **13:20-14:50** | Day 6 FastAPI | `10-fastapi/theory_10_fastapi.md` |
| | | `10-fastapi/practice_10_fastapi.py`（7个TODO） |
| **14:50-15:00** | 复盘 | 卡在哪、什么还不熟 |

---

## 执行方式

```
每段都一样：读 theory → 敲 practice TODO → 破坏实验 → 跑通
```

具体：
1. 打开该段的 theory 文件，读 5 分钟
2. 打开 practice 文件，敲 TODO（不要复制粘贴）
3. 故意改错一个条件看报错
4. `python practice_xx.py` 跑通

Day 6 特殊：
```
Day 6 不需要 python 跑，需要：
pip install fastapi uvicorn
uvicorn practice_10_fastapi:app --reload
浏览器打开 http://127.0.0.1:8000/docs
```

---

## 如果某一环节卡住

| 卡在 | 怎么办 |
|------|--------|
| Pydantic 不懂 | 回去看 theory，再不行问 CC |
| 类型提示忘了 | 翻 `05-module-types/theory_05_module_types.md` |
| 文件操作忘了 | 翻 `03-file-exception/` |
| 某个 TODO 不会 | 跳过，做后面的，最后一起问 CC |
| 时间不够 | Day 6 > Day 5 > Day 4，优先保后面的 |

## 下周一（5/11）回头补

这些内容明天跳过，下周一补。文件已全部生成，直接打开练：

| 补什么 | 文件（已就绪） | 预估 |
|--------|--------------|------|
| 类/封装/继承/多态 练习 | `04-listcomp-class/practice_04b_class.py`（5题） | 40min |
| 装饰器（含 @app.get 原理） | `11-closure-decorator/practice_11_decorator.py`（5题） | 40min |
| 闭包 | 同上文件，练习1-2 | 20min |
| 正则表达式 | `07-pydantic/practice_07b_regex.py`（5题） | 20min |
| 设计模式（工厂/策略/观察者/单例） | `12-design-patterns/` theory + practice | 40min |
| 多线程（threading/线程池/Lock） | `13-multithreading/` theory + practice | 40min |
