"""
Day 8 练习：大模型知识扩展
完成后运行：python practice_08.py

目标：理解 Flash Attention、BM25 的基本概念
"""
import sys
sys.stdout.reconfigure(encoding="utf-8", errors="replace")


# ============================================================
# 第一组：理解 BM25 的直觉
# ============================================================

# 对比向量检索和 BM25
scenarios = [
    {
        "query": "用低秩矩阵适配大模型的方法",
        "best_search": "",  # TODO 1：填 "向量" 还是 "BM25"？
        "reason": "",
    },
    {
        "query": "LoRA r=8 和 lora_alpha=16 的参数区别",
        "best_search": "",
        "reason": "",
    },
    {
        "query": "怎么减少大模型回答时的幻觉问题",
        "best_search": "",
        "reason": "",
    },
]

print("Hybrid Search 场景理解")
print("=" * 50)
for s in scenarios:
    print(f"查询：「{s['query']}」")
    print(f"  最优检索：{s['best_search']}")
    print(f"  理由：{s['reason']}")
    print()


# ============================================================
# 第二组：用 BM25 检索 + 向量检索的概念模拟
# ============================================================

# 我们有 5 个文档
docs = [
    "LoRA 通过低秩矩阵 A 和 B 来适配大模型权重",
    "LoRA 的秩 r 控制参数量，r=8 是常用值",
    "RAG 通过检索外部知识增强大模型回答能力",
    "DeepSeek V3 是 671B 参数的 MoE 模型",
    "DeepSeek R1 用强化学习增强推理能力",
]

query = "LoRA r=8"

# BM25 风格命中（关键词精确匹配）
bm25_hits = sum(1 for d in docs if "r=8" in d)
vector_hits = sum(1 for d in docs if "LoRA" in d or "适配" in d)

print(f"查询：{query}")
print(f"  BM25 风格命中（含 'r=8'）：{bm25_hits} 篇")
print(f"  向量风格命中（含 'LoRA/适配'）：{vector_hits} 篇")

# TODO 2：如果仅用向量检索，可能漏掉"r=8"的精确匹配
# 如果仅用 BM25，可能漏掉语义相关的文档
# Hybrid Search 结合两者优势

print()
print("混合策略：")
print("  向量检索 Top-3 + BM25 Top-3 → 去重 → Rerank → Top-2")
print()


# ============================================================
# 第三组：Flash Attention 理解
# ============================================================

# 标准 Attention 的显存占用
batch = 1
seq_len = 4096
head_dim = 128
num_heads = 32

standard_mem = batch * seq_len * seq_len * 2 * 4  # S 和 P 矩阵各一份
flash_mem = batch * seq_len * head_dim * num_heads * 4  # 不存中间结果

print(f"标准 Attention 中间显存：{standard_mem / 1024**2:.1f} MB")
print(f"Flash Attention 中间显存：{flash_mem / 1024**2:.1f} MB")
print(f"节省：{(1 - flash_mem/standard_mem) * 100:.0f}%")

# TODO 3：为什么 Flash Attention 能做到？
reason = ""
print(f"原因：{reason}")


print("\n✅ Day 8 练习完成！")
print("扩展知识的作用：理解底层原理，做技术选型时有依据。")
