"""
Day 10 练习：LangChain 基础理解
完成后运行：python practice_10.py

目标：理解 LangChain 核心组件
注：本练习不安装 LangChain，理解概念为主
"""
import sys
import os
sys.stdout.reconfigure(encoding="utf-8", errors="replace")

from openai import OpenAI
client = OpenAI(
    api_key=os.environ.get("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com/v1"
)


# ============================================================
# 第一组：理解 Chain 的概念
# ============================================================

# LangChain 的 Chain 就是把多步 LLM 调用串起来
# 这里我们不用 LangChain，手动模拟 Chain

def step1_translate(text: str) -> str:
    """第一步：翻译"""
    resp = client.chat.completions.create(
        model="deepseek-chat",
        messages=[{"role": "user",
                   "content": f"把以下中文翻译成英文：{text}"}],
        temperature=0.3,
    )
    return resp.choices[0].message.content


def step2_summarize(text: str) -> str:
    """第二步：总结"""
    resp = client.chat.completions.create(
        model="deepseek-chat",
        messages=[{"role": "user",
                   "content": f"用一句话概括以下英文：{text}"}],
        temperature=0.3,
    )
    return resp.choices[0].message.content


# TODO 1：模拟 Chain——先翻译再总结
input_text = "人工智能正在改变世界"

print("模拟 Chain 执行")
print("=" * 50)
print(f"输入：{input_text}")

translated = step1_translate(input_text)
print(f"Step 1（翻译）：{translated}")

summary = step2_summarize(translated)
print(f"Step 2（总结）：{summary}")

# 这就是 LangChain 中 SequentialChain 的原理
print()


# ============================================================
# 第二组：理解 RAG Chain
# ============================================================

# LangChain 的 RetrievalQA 背后就是：
# 检索 → 拼接 Prompt → LLM 回答

# 模拟一个 RAG Chain
documents = [
    "LoRA 是一种参数高效微调方法",
    "RAG 通过检索外部知识增强回答",
    "Agent 能自主调用工具完成任务",
]

def retrieve(query: str, docs: list) -> str:
    """模拟检索（关键词匹配）"""
    kw = query.split()[0]  # 简化版
    relevant = [d for d in docs if kw in d]
    return "\n".join(relevant) if relevant else "未找到相关信息"


def generate(query: str, context: str) -> str:
    """基于检索结果生成回答"""
    prompt = f"""基于以下资料回答问题。

资料：{context}

问题：{query}

回答："""
    resp = client.chat.completions.create(
        model="deepseek-chat",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3,
    )
    return resp.choices[0].message.content


# TODO 2：模拟 RAG Chain
query = "LoRA 是什么？有什么用？"
print("模拟 RAG Chain")
print("=" * 50)
print(f"查询：{query}")

# Step 1: 检索
context = retrieve(query, documents)
print(f"检索结果：{context}")

# Step 2: 生成
answer = generate(query, context)
print(f"回答：{answer}")
print()


# ============================================================
# 第三组：理解工具调用（Agent 的基础）
# ============================================================

# LangChain 的 Agent = LLM + Tools + Memory
# 这里模拟 Agent 的工具选择

# TODO 3：定义工具
tools_info = {
    "get_weather": "查询城市天气",
    "calculate": "数学计算",
    "search_knowledge": "搜索知识库",
}


def choose_tool(query: str) -> str:
    """让 LLM 选择工具"""
    prompt = f"""用户查询：{query}

可用工具：
{chr(10).join(f'- {k}: {v}' for k, v in tools_info.items())}

请选择最合适的工具名称，只输出工具名。"""
    resp = client.chat.completions.create(
        model="deepseek-chat",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.1,
        max_tokens=20,
    )
    return resp.choices[0].message.content.strip()


# 测试不同的查询
test_queries = [
    "北京的天气怎么样？",
    "25×4+100等于多少？",
    "LoRA 和微调有什么区别？",
]

print("Agent 工具选择模拟")
print("=" * 50)
for q in test_queries:
    tool = choose_tool(q)
    print(f"查询：{q}")
    print(f"  选择工具：{tool}")
    print()


print("✅ Day 10 练习完成！")
print("LangChain 就是把你已经会的东西（Chain、RAG、Agent）标准化了。")
