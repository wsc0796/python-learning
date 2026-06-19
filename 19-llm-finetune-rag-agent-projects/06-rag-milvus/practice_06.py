"""
Day 6 练习：RAG 系统理解
完成后运行：python practice_06.py

目标：理解 RAG 流程 + 模拟向量检索
注：不做真实 Milvus 部署，概念理解为主
"""
import sys
import os
import json
import numpy as np
sys.stdout.reconfigure(encoding="utf-8", errors="replace")

from openai import OpenAI
client = OpenAI(
    api_key=os.environ.get("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com/v1"
)


# ============================================================
# 第一组：理解 RAG 流程——模拟检索
# ============================================================

# 假设我们有一个简版"知识库"
documents = [
    "LoRA 通过低秩矩阵适配大模型，训练参数量只有全量微调的 0.1%",
    "RAG 检索增强生成让模型基于外部知识回答问题，减少幻觉",
    "Function Call 让模型能调用外部工具，是 Agent 的基础能力",
    "CoT 思维链让模型展示推理过程，提高复杂问题的准确率",
    "Milvus 是开源向量数据库，专门用于向量相似度搜索",
    "Prompt-Tuning 不修改模型参数，通过设计输入让模型完成任务",
]

# 用 DeepSeek 做 embedding
def embed(text: str) -> list[float]:
    resp = client.embeddings.create(
        model="text-embedding-v3",  # DeepSeek 的 embedding 模型
        input=text,
    )
    return resp.data[0].embedding


# 构建向量知识库（简化版——用第一个文档的 embedding 演示）
query = "LoRA 微调有什么优势？"
print(f"用户提问：{query}")

# 实际 RAG 中，这里会：
# 1. query_embedding = embed(query)
# 2. 在 Milvus 中搜索最近邻
# 3. 返回 Top-K 相关文档

# 这里我们模拟一下：挑出包含关键词的文档
keywords = ["LoRA", "微调", "参数"]
relevant = []
for i, doc in enumerate(documents):
    if any(kw in doc for kw in keywords):
        relevant.append(doc)
        print(f"  匹配文档 {i+1}：{doc[:40]}...")

print(f"\n检索到 {len(relevant)} 个相关文档")
print()


# ============================================================
# 第二组：用检索到的内容生成回答
# ============================================================

if relevant:
    context = "\n".join(relevant)
    prompt = f"""基于以下参考资料回答问题。

资料：
{context}

问题：{query}

回答要求：
1. 基于资料内容作答
2. 如果资料不充分，说明缺少哪些信息
3. 不要编造资料中没有的内容"""

    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3,
    )
    print("RAG 回答：")
    print(response.choices[0].message.content)


# ============================================================
# 第三组：理解你的 pipeline 和标准 RAG 的关系
# ============================================================

# TODO 1：回顾你的 document_pipeline/local_pdf_pipeline.py
# 它的 query() 方法和 RAG 有什么异同？

print("\n" + "=" * 50)
print("你的 pipeline vs 标准 RAG")
print("=" * 50)
print()

# TODO 2：填写对比表
comparison = {
    "检索方式": {
        "你的 pipeline": "LLM 读索引 + grep",  # 用 LLM 选章节
        "标准 RAG": "向量相似度搜索",           # 用 embedding 检索
    },
    "切分方式": {
        "你的 pipeline": "",  # TODO：按什么切？
        "标准 RAG": "固定 token 大小切块",
    },
    "索引方式": {
        "你的 pipeline": "",  # TODO：索引存在哪？
        "标准 RAG": "向量数据库（Milvus）",
    },
}

for k, v in comparison.items():
    print(f"{k}：")
    for k2, v2 in v.items():
        print(f"  {k2}：{v2}")
    print()


print("\n✅ Day 6 练习完成！")
print("RAG = 检索 + 增强 + 生成，你已经在用它的变体了。")
