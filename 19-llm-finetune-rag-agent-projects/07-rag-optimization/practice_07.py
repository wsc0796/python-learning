"""
Day 7 练习：RAG 优化与评估
完成后运行：python practice_07.py

目标：理解 Hybrid Search 和 Rerank 的原理
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
# 第一组：理解 BM25 关键词检索
# ============================================================

# BM25 的核心是：词频 × 逆文档频率 × 长度归一化
# 简版理解：出现关键词越多的文档得分越高

documents = [
    "LoRA 是一种参数高效微调方法，通过低秩矩阵适配大模型",
    "RAG 通过检索外部知识来增强大模型的回答能力",
    "Function Call 让大模型能够调用外部工具和函数",
    "CoT 思维链让模型展示推理过程，提高准确率",
    "Milvus 是高性能向量数据库，支持万亿级向量搜索",
    "Prompt-Tuning 通过设计提示词让模型完成任务",
]

# 简版 BM25 计分
def simple_bm25(query: str, doc: str) -> float:
    """极简版 BM25——计算关键词命中率"""
    query_words = set(query.lower().split())
    doc_words = doc.lower().split()
    hits = sum(1 for q in query_words if q in doc_words)
    return hits / len(query_words) if query_words else 0


# TODO 1：测试不同查询的检索效果
test_queries = [
    "LoRA 微调",
    "向量检索",
    "大模型",
]

print("=" * 50)
print("简版 BM25 检索结果")
print("=" * 50)

for q in test_queries:
    scores = [simple_bm25(q, d) for d in documents]
    best_idx = scores.index(max(scores))
    print(f"\n查询：「{q}」")
    print(f"  最佳匹配：{documents[best_idx][:50]}...")
    print(f"  分数：{max(scores):.2f}")


# ============================================================
# 第二组：理解 Rerank
# ============================================================

# 假设第一轮检索返回了 Top-5
# Rerank 对它们重新精确排序

# TODO 2：用 LLM 模拟 Rerank
query = "RAG 怎么减少幻觉？"
candidates = [
    "LoRA 通过低秩矩阵适配大模型，训练参数量只有全量微调的 0.1%",
    "RAG 检索增强生成让模型基于外部知识回答问题，减少幻觉",
    "Function Call 让模型能调用外部工具，是 Agent 的基础能力",
    "Milvus 是开源向量数据库，专门用于向量相似度搜索",
    "Prompt-Tuning 不修改模型参数，通过设计输入让模型完成任务",
]

print("\n" + "=" * 50)
print(f"Rerank 排序 - 查询：{query}")
print("=" * 50)

# 用 LLM 做 Rerank
rerank_prompt = f"""问题：{query}

以下是 5 个候选文档，请按与问题的相关程度从高到低排序。
只输出排序后的序号（逗号分隔）。

{chr(10).join(f"{i+1}. {d}" for i, d in enumerate(candidates))}

排序结果："""

response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[{"role": "user", "content": rerank_prompt}],
    temperature=0.1,
)
print(f"LLM 排序结果：{response.choices[0].message.content}")


# ============================================================
# 第三组：评估一个 RAG 回答
# ============================================================

# TODO 3：评估以下场景
scenario = {
    "question": "LoRA 的秩 r 怎么选择？",
    "retrieved": [
        "LoRA 通过低秩矩阵适配大模型，训练参数量只有全量微调的 0.1%",
        "r 值越大，LoRA 的学习能力越强，但参数量也越大",
    ],
    "answer": "LoRA 的秩 r 可以根据任务复杂度调整。简单任务用 r=4-8，复杂任务用 r=16-32。实际上 r=8 是一个常用的默认值。",
}

print("\n" + "=" * 50)
print("RAG 评估")
print("=" * 50)

print(f"问题：{scenario['question']}")
print(f"检索到 {len(scenario['retrieved'])} 个文档")
print(f"回答：{scenario['answer']}")

# TODO 4：请判断
print("\n评估结果：")
print(f"Context Relevance（检索内容与问题相关吗）：")
print(f"Faithfulness（答案基于检索内容吗）：")
print(f"Answer Relevance（答案回答了问题吗）：")


print("\n✅ Day 7 练习完成！")
print("RAG 优化核心：切分 → 检索 → 排序 → 生成，每个环节都能优化。")
