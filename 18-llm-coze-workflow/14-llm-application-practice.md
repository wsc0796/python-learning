---
aliases:
  - 14-llm-application-practice
---
# 14. 大模型应用实践

> 前置：[[13-open-source-llm]]
> 目标：用 Ollama 在本地跑模型、搭知识库问答系统、用 Streamlit 做界面
> 用时：约 15 分钟（实操时间另计，约 1-2 小时）
>
> 相关笔记：[[03-async-await]] · [[10-fastapi]]

---

## 一、对话机器人基础流程

```python
# 最简对话机器人（伪代码）
while True:
    user_input = input("你: ")
    if user_input == "退出":
        break
    response = call_llm_api(user_input)
    print(f"AI: {response}")
```

**核心循环**：获取输入 → 调 LLM API → 返回输出。你在 [[03-async-await]] 里学的 `async/await`，在这里直接用于非阻塞地调 LLM API。

---

## 二、Ollama：本地运行大模型

### 安装

官网下载：ollama.com（支持 Windows/Mac/Linux）

### 常用命令

```bash
# 拉取模型
ollama pull qwen2.5:7b        # 7B 参数，约 4GB，适合普通电脑
ollama pull llama3.2:3b       # 更轻量，约 2GB

# 运行模型（交互式对话）
ollama run qwen2.5:7b

# 查看已下载的模型
ollama list

# 启动 API 服务（后台运行）
ollama serve
```

### API 调用

Ollama 启动后，本地就有了一个 HTTP API：

```python
import requests
import json

def ask_ollama(prompt: str, model: str = "qwen2.5:7b") -> str:
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": model,
            "prompt": prompt,
            "stream": False
        }
    )
    return response.json()["response"]

# 使用
answer = ask_ollama("用一句话解释什么是 Python")
print(answer)
```

### 异步版调用

```python
import httpx
import asyncio

async def ask_ollama_async(prompt: str, model: str = "qwen2.5:7b") -> str:
    async with httpx.AsyncClient() as client:
        response = await client.post(
            "http://localhost:11434/api/generate",
            json={"model": model, "prompt": prompt, "stream": False},
            timeout=60.0
        )
        return response.json()["response"]

async def main():
    answer = await ask_ollama_async("什么是闭包")
    print(answer)

asyncio.run(main())
```

---

## 三、AnythingLLM：快速搭知识库问答

### 是什么

一个**开源的桌面应用**，让你：
1. 上传文档（PDF、Word、TXT、网页）
2. 自动把文档变成知识库
3. 基于知识库做问答

### 核心概念

```
你的文档 → 切片(chunk) → 向量化(embedding) → 存入向量数据库
                                       ↓
用户提问 → 向量化 → 检索相关文档片段 → 拼接成 prompt → LLM 生成回答
```

**这就是 RAG（检索增强生成）的完整流程。** AnythingLLM 帮你封装好了。

### 部署方式

1. 下载 AnythingLLM 桌面版
2. 配置 LLM 提供商（选择 Ollama 本地模型或 API）
3. 上传文档创建工作空间
4. 开始提问

---

## 四、Streamlit：快速做 AI 应用界面

### 安装

```bash
pip install streamlit
```

### 最简聊天界面

```python
# chat_app.py
import streamlit as st
import requests

st.title("🤖 我的第一个 AI 助手")

# 输入框
user_input = st.text_input("你:", placeholder="输入你的问题...")

if user_input:
    # 调 Ollama API
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={"model": "qwen2.5:7b", "prompt": user_input, "stream": False}
    )

    # 显示回复
    st.write("AI:", response.json()["response"])
```

运行：

```bash
streamlit run chat_app.py
```

浏览器自动打开 → 你有了一个带界面的 AI 应用。

### 扩展方向

```python
# 加对话历史
if "messages" not in st.session_state:
    st.session_state.messages = []

# 显示历史消息
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# 用户输入
if prompt := st.chat_input("说点什么..."):
    st.session_state.messages.append({"role": "user", "content": prompt})

    # 调模型
    response = call_llm(prompt)

    st.session_state.messages.append({"role": "assistant", "content": response})
```

---

## 五、你的技术栈整合

```
┌─────────────────────────────────┐
│  Streamlit 前端（界面）          │
├─────────────────────────────────┤
│  FastAPI 后端（业务逻辑）        │
├─────────────────────────────────┤
│  Ollama / LLM API（AI 能力）    │
├─────────────────────────────────┤
│  AnythingLLM（知识库/RAG）       │
├─────────────────────────────────┤
│  Coze 工作流（快速原型）         │
└─────────────────────────────────┘
```

**这几个工具不是"选一个"，是"组合用"：**
- Coze → 快速验证想法
- Ollama → 本地免费跑模型
- FastAPI → 写业务逻辑和 API
- Streamlit → 快速搭界面展示
- AnythingLLM → 知识库问答原型

---

## 六、你的第一个完整 AI 应用（建议）

```text
题目：本地知识库问答助手

技术栈：
  - Ollama（qwen2.5:7b 本地模型）
  - Streamlit（聊天界面）
  - 知识库：把 CS50P 笔记或苍穹外卖文档放进去

功能：
  - 上传文档 → 自动建立知识库
  - 用户提问 → 检索相关文档片段 → LLM 基于文档回答
  - 显示引用来源

工期：1-2 天（周末可以做完）
```

这是你简历上第一个可以写的 AI 项目。
