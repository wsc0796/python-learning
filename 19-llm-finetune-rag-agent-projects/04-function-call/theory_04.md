---
aliases:
  - 04-function-call
---
# Day 4：Function Call

读完约 12 分钟。

---

## 一、Function Call 是什么

Function Call 让大模型从"聊天"变成"调用工具做事"。

### 工作原理

```
用户："北京明天天气怎么样？"
                ↓
模型理解意图 → 选择函数 get_weather
                ↓
模型生成参数 {"city": "北京", "date": "明天"}
                ↓
程序执行 get_weather("北京", "明天")
                ↓
返回结果 {"temp": 26, "weather": "晴"}
                ↓
模型组织回答："北京明天晴，26°C"
```

**关键：模型不执行函数，只决定调哪个函数 + 生成参数。**

---

## 二、函数定义

需要定义：函数名、描述、参数列表。

```python
import json

functions = [
    {
        "name": "get_weather",
        "description": "查询指定城市的天气",
        "parameters": {
            "type": "object",
            "properties": {
                "city": {
                    "type": "string",
                    "description": "城市名称"
                },
                "date": {
                    "type": "string",
                    "description": "日期"
                }
            },
            "required": ["city", "date"]
        }
    }
]

# 调用时把 functions 传给 API
response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[...],
    tools=functions,     # ← 注册可用函数
    tool_choice="auto"   # ← 让模型自己决定是否调用
)
```

---

## 三、意图澄清

当用户信息不完整时，模型应该追问而不是猜。

```
用户："查一下天气"
模型："请问你想查哪个城市的天气？"

用户："查一下北京的天气"
模型："请问查哪天？"
```

实现方式：参数中标记 required 字段。

---

## 四、多函数调用

复杂任务可以串行调用多个函数。

```
用户："帮我查北京明天天气，并推荐适合的景点"

① get_weather(city="北京", date="明天")
② search_pois(city="北京", category="景点", weather="晴")
③ format_result(weather, pois)
```

---

## 五、实际案例：数据库查询

这是你的 `document_pipeline/paper_pipeline.py` 中用到的模式：

```python
# 1. 定义查询工具
query_tool = {
    "name": "query_papers",
    "description": "按关键词搜索论文",
    "parameters": {
        "type": "object",
        "properties": {
            "keywords": {"type": "string", "description": "搜索关键词"},
            "limit": {"type": "integer", "description": "返回数量"}
        },
        "required": ["keywords"]
    }
}

# 2. LLM 决定查询参数
# 3. 程序执行实际搜索
# 4. 结果返回 LLM 组织回答
```

---

## 六、Function Call 和 Agent 的关系

```
Function Call = 让模型会"用工具"
Agent = 让模型会"规划" + "记忆" + "用工具"

Function Call 是 Agent 的基础能力。
你掌握了 Function Call，Agent 就学会了一半。
```
