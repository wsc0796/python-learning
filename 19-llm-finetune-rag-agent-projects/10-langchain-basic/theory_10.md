---
aliases:
  - 10-langchain-basic
---
# Day 10：LangChain 基础

读完约 15 分钟。

---

## 一、LangChain 是什么

LangChain 是一个大模型应用开发框架。

```
你不必从零实现：Prompt 模板、Chain、Agent、Memory、RAG...
LangChain 帮你封装好了。
```

### 核心模块

| 模块 | 功能 |
|------|------|
| Models | 对接各种 LLM API |
| Prompts | Prompt 模板、示例选择器 |
| Chains | 把多个步骤串起来 |
| Agents | 让 LLM 自动选择工具 |
| Memory | 状态/对话记忆 |
| Indexes | 文档加载、切分、向量化、检索 |

---

## 二、Models

```python
from langchain.chat_models import ChatOpenAI
from langchain.embeddings import OpenAIEmbeddings

# LLM
llm = ChatOpenAI(
    model="deepseek-chat",
    openai_api_key="sk-xxx",
    openai_api_base="https://api.deepseek.com/v1",
)

# Embedding
embeddings = OpenAIEmbeddings(
    model="text-embedding-v3",
    openai_api_key="sk-xxx",
    openai_api_base="https://api.deepseek.com/v1",
)
```

---

## 三、Prompts

```python
from langchain.prompts import PromptTemplate
from langchain.prompts import FewShotPromptTemplate

# Zero-shot
template = PromptTemplate.from_template(
    "请将以下文本翻译成英文：{text}"
)

# Few-shot
examples = [
    {"input": "你好", "output": "Hello"},
    {"input": "谢谢", "output": "Thank you"},
]

few_shot = FewShotPromptTemplate(
    examples=examples,
    example_prompt=PromptTemplate.from_template(
        "输入：{input}\n输出：{output}"
    ),
    suffix="输入：{text}\n输出：",
    input_variables=["text"],
)
```

---

## 四、Chains

把多个步骤串起来。

```python
from langchain.chains import LLMChain
from langchain.chains import SimpleSequentialChain

# 单步
chain = LLMChain(llm=llm, prompt=template)
result = chain.run(text="你好")

# 多步串联
chain1 = LLMChain(llm=llm, prompt=translate_prompt)
chain2 = LLMChain(llm=llm, prompt=summarize_prompt)

pipeline = SimpleSequentialChain(
    chains=[chain1, chain2],
    verbose=True,
)
```

---

## 五、Agent

```python
from langchain.agents import AgentExecutor, create_react_agent
from langchain.tools import Tool

# 定义工具
tools = [
    Tool(
        name="get_weather",
        func=get_weather_impl,
        description="查询天气",
    ),
    Tool(
        name="calculate",
        func=calculate_impl,
        description="数学计算",
    ),
]

# 创建 Agent
agent = create_react_agent(llm, tools, prompt)
agent_executor = AgentExecutor(
    agent=agent,
    tools=tools,
    verbose=True,
)

# 运行
agent_executor.invoke({"input": "北京天气怎么样？"})
```

---

## 六、Memory

```python
from langchain.memory import ConversationBufferMemory

memory = ConversationBufferMemory()

# 每次对话后自动保存
chain = LLMChain(llm=llm, prompt=prompt, memory=memory)
chain.run("我的名字是张三")
chain.run("我叫什么名字？")  # 记得"张三"
```

### Memory 类型

| 类型 | 特点 |
|------|------|
| BufferMemory | 保存全部对话 |
| SummaryMemory | 压缩为摘要 |
| VectorStoreMemory | 向量化存储，支持长时记忆 |

---

## 七、Indexes（RAG 相关）

```python
from langchain.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import FAISS

# 加载
loader = TextLoader("note.md")
docs = loader.load()

# 切分
splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50,
)
chunks = splitter.split_documents(docs)

# 向量化 + 存储
vectorstore = FAISS.from_documents(chunks, embeddings)

# 检索
retriever = vectorstore.as_retriever(search_kwargs={"k": 3})

# RAG Chain
from langchain.chains import RetrievalQA
qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=retriever,
)
answer = qa_chain.run("你的问题")
```

---

## 八、LangChain 和你的 pipeline 的对应关系

```
你的 local_pdf_pipeline.py          LangChain
──────────────────────            ──────────
collect() + convert()              Document Loaders
segment()                          Text Splitters
enrich() + build_index()           Vector Stores + Embeddings
query() → LLM 选章节 + 读文件      RetrievalQA Chain
query() → 组织回答                 LLMChain
```

**LangChain 是把你的 pipeline 思路标准化、组件化了。**
你已经理解了核心思想，用 LangChain 只是换一套工具。

---

## 九、学 LangChain 的正确姿势

```
不学的时候：
你是直接用 API 调模型，每个项目重新写 prompt 模板、chain、memory
换项目时：重新写

学的时候：
LangChain 帮你封装了通用组件
换项目时：换配置，不改代码

但不要过度依赖框架——先理解原理（你已经做了），再学工具。
```
