---
aliases:
  - 06-advanced-workflow-nodes
---
# 06. 高级工作流节点

> 前置：[[05-workflow-entry-practice]]（已能跑通基本工作流）
> 目标：掌握代码块、条件分支、循环、异步任务
> 用时：约 15 分钟
>
> 相关笔记：[[04-listcomp-class]] · [[23-if-conditionals]] · [[03-async-await]]

---

## 一、代码块节点

### 适用场景

当 LLM 和插件都处理不了时，写代码。

```text
不适合 LLM 的事：
- JSON 精确清洗（容易丢字段）
- 字符串精确拼接（容易多加空格）
- 列表循环处理（每个元素做同样的操作）
- 格式转换（JSON → Markdown 表格 → CSV 字符串）
```

### Python 代码块模板

```python
def main(input_data: dict) -> dict:
    # input_data 包含你在节点配置里指定的输入参数
    title = input_data.get("title", "")
    content = input_data.get("content", "")

    # 你的处理逻辑
    result = f"# {title}\n\n{content}"

    # 返回 dict，key 就是输出参数名
    return {
        "markdown_output": result
    }
```

### 实战示例：清洗 LLM 输出的 JSON

```python
import json

def main(input_data: dict) -> dict:
    raw_text = input_data.get("llm_output", "")
    # LLM 经常在 JSON 外面包 Markdown 代码块标记
    raw_text = raw_text.replace("```json", "").replace("```", "").strip()
    try:
        data = json.loads(raw_text)
        return {"parsed_data": data, "is_valid": True}
    except json.JSONDecodeError:
        return {"parsed_data": {}, "is_valid": False}
```

### 代码块的限制

- 不能 pip install 第三方包（只能用内置库）
- 执行时间有限制（通常 30 秒）
- 不能访问文件系统
- 不能发网络请求（用 HTTP 插件代替）

---

## 二、条件分支节点

### 用途

根据某个变量的值，走不同的处理路径。

### 配置方式

```
判断条件：{{LLM节点.intent}} == "查天气"
  ├── True  → 调用天气插件
  └── False → 判断下一个条件：{{LLM节点.intent}} == "写文案"
                ├── True  → 调用文案 LLM
                └── False → 回复"请说明您的需求"
```

### 常见分支场景

| 场景 | 判断依据 | 分支 |
|------|---------|------|
| 意图识别 | LLM 分类结果 | 不同意图 → 不同处理 |
| 内容长度 | `len(text) > 500` | 长文用摘要模式，短文直接处理 |
| 是否含图片 | `has_image == True` | 有图走图+文，无图走纯文 |
| 用户等级 | `user_level` | VIP 走高级模型，普通走基础模型 |

---

## 三、循环节点

### 用途

对一个列表里的每一项，重复执行相同的操作。

### 循环配置

```text
循环源：{{代码块节点.title_list}}
  ↓
循环体（对每个 item 执行）：
  LLM 节点生成该标题对应的文案
  ↓
收集所有结果到 result_list
```

### 实战场景

```text
输入：5 个商品名称
循环体：为每个商品生成 3 个卖点
输出：5 个商品 × 3 个卖点 = 15 条文案
```

### 循环注意事项

- 循环体内的节点可以使用 `{{loop_item}}` 引用当前元素
- 循环次数有限制（免费版通常 10-20 次）
- 批量任务不要设置太大循环次数——会被限流

---

## 四、异步运行配置

### 什么时候用异步

```text
不用异步：LLM 生成文本（3-5秒） → 直接返回
用异步：  生成图片（30-60秒） → 先告诉用户"正在生成"，生成完再通知
```

### 异步任务流程

```
用户请求生成图片
    ↓
LLM 生成提示词（同步）
    ↓
图片生成插件（异步）──→ 用户收到"正在生成，稍后通知"
    ↓（30 秒后）
图片生成完成 → 通知用户
```

---

## 五、节点组合决策速查

| 你要做的事 | 用哪个节点 |
|-----------|-----------|
| AI 写内容 | LLM 节点 |
| 查外部数据 | 插件节点 |
| 清洗/转换数据 | 代码块节点 |
| 根据不同情况做不同处理 | 条件分支 |
| 重复处理一批东西 | 循环节点 |
| 耗时任务不阻塞 | 异步配置 |
