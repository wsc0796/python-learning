"""
Day 11 练习：物流行业 RAG 系统设计
完成后运行：python practice_11.py

目标：实现意图分类 + RAG 检索的核心逻辑
"""
import sys
import os
import json
sys.stdout.reconfigure(encoding="utf-8", errors="replace")

from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com/v1"
)


# ============================================================
# 第一组：模拟 BERT + PET 意图分类
# ============================================================

# PET = Pattern-Exploiting Training
# 把分类任务转化成 "填空" 任务

# 类别和对应标签词（Verbalizer）
LABEL_MAP = {
    "查物流": "物流",
    "查运费": "运费",
    "查网点": "网点",
    "查禁运": "禁运",
}

# TODO 1：设计 PET 模板
# 把用户问题填入下面的模板，让 LLM 预测 [MASK] 位置的词
# 模板例子："这句话的意图是 __，查询关于 {text} 的问题"
def classify_with_pet(text: str) -> str:
    """用 PET 风格（填空）做意图分类"""
    prompt = f"""请判断以下查询属于哪一类。

类别：{"、".join(LABEL_MAP.keys())}

查询：{text}

请只输出类别名称："""

    resp = client.chat.completions.create(
        model="deepseek-chat",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.1,
        max_tokens=20,
    )
    return resp.choices[0].message.content.strip()


# 测试
test_queries = [
    "我的包裹到哪了？",
    "寄到新疆多少钱？",
    "最近的网点在哪里？",
    "能寄打火机吗？",
]

print("BERT + PET 意图分类模拟")
print("=" * 50)
for q in test_queries:
    label = classify_with_pet(q)
    print(f"查询：「{q}」")
    print(f"  意图：{label}")
print()


# ============================================================
# 第二组：模拟 P-Tuning 的 Soft Prompt 效果
# ============================================================

# P-Tuning = 在输入前加可训练的连续向量（Soft Prompt）
# 这里我们用 DeepSeek 模拟 "Soft Prompt 让分类更准" 的效果

# TODO 2：给每个类别设计一个 "Soft Prompt" 风格的指令前缀
SOFT_PROMPTS = {
    "查物流": "",
    "查运费": "",
    "查网点": "",
    "查禁运": "",
}

ambiguous_queries = [
    "上海到北京",
    "我要查一个件",
    "这个能寄吗",
]


def classify_with_softprompt(text: str, intent_hint: str) -> str:
    """模拟 P-Tuning：用 Soft Prompt 引导分类"""
    # 在用户问题前加一段 "连续向量"（这里用文字模拟）
    soft_prompt = SOFT_PROMPTS.get(intent_hint, "")
    prompted_text = f"{soft_prompt}{text}" if soft_prompt else text

    resp = client.chat.completions.create(
        model="deepseek-chat",
        messages=[{"role": "user", "content": f"查询：{prompted_text}\n\n意图类别：查物流、查运费、查网点、查禁运\n\n只输出类别名："}],
        temperature=0.1,
        max_tokens=20,
    )
    return resp.choices[0].message.content.strip()


print("P-Tuning 模拟（用前缀引导分类）")
print("=" * 50)
for q in ambiguous_queries:
    # 不加 Soft Prompt
    result_no = classify_with_pet(q)
    # 加一个可能的 Soft Prompt
    hint = "查运费" if "上海" in q or "北京" in q else "查物流"
    result_yes = classify_with_softprompt(q, hint)
    print(f"查询：「{q}」")
    print(f"  无 Soft Prompt：{result_no}")
    print(f"  有 Soft Prompt：{result_yes}")
print()


# ============================================================
# 第三组：模拟 RAG 检索 + 生成
# ============================================================

# 物流知识库（运费规则）
knowledge_base = [
    {"id": 1, "content": "上海到北京，首重12元/kg，续重6元/kg，时效2-3天"},
    {"id": 2, "content": "上海到新疆，首重18元/kg，续重12元/kg，时效5-7天"},
    {"id": 3, "content": "北京到广州，首重15元/kg，续重8元/kg，时效3-4天"},
    {"id": 4, "content": "打火机、火柴等易燃易爆品禁止邮寄"},
    {"id": 5, "content": "液体粉末状物品需单独申报"},
    {"id": 6, "content": "活体动物（除指定宠物外）禁止邮寄"},
]


def retrieve(query: str, docs: list, top_k: int = 2) -> list:
    """模拟向量检索（关键词匹配 + 语义排序）"""
    # 简化：用关键词匹配模拟
    keywords = query.replace("？", "").split()
    scored = []
    for doc in docs:
        score = sum(1 for kw in keywords if kw in doc["content"])
        if score > 0:
            scored.append((score, doc))
    scored.sort(key=lambda x: -x[0])
    return [doc for _, doc in scored[:top_k]]


# TODO 3：实现 RAG 生成
def rag_answer(question: str, contexts: list) -> str:
    """基于检索结果生成回答"""
    context_text = "\n".join([c["content"] for c in contexts])

    prompt = f"""你是一个物流客服助手，请基于以下资料回答问题。

相关资料：
{context_text}

问题：{question}

请用简洁、专业的语气回答："""
    resp = client.chat.completions.create(
        model="deepseek-chat",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3,
    )
    return resp.choices[0].message.content


print("RAG 检索 + 生成")
print("=" * 50)
rag_questions = [
    "寄到新疆多少钱？",
    "能寄打火机吗？",
    "上海到北京运费多少？",
]
for q in rag_questions:
    results = retrieve(q, knowledge_base)
    print(f"\n查询：{q}")
    print(f"检索到 {len(results)} 条相关规则")
    for r in results:
        print(f"  - {r['content']}")
    answer = rag_answer(q, results)
    print(f"回答：{answer}")
print()


# ============================================================
# 第四组：完整流程——意图分类 → 检索 → 生成
# ============================================================

def logistics_rag_pipeline(question: str) -> str:
    """模拟完整的物流 RAG 流程"""
    # Step 1: 意图分类
    intent = classify_with_pet(question)

    # Step 2: 根据意图检索
    if intent in ("查运费", "查禁运"):
        results = retrieve(question, knowledge_base)
        context = results if results else [{"content": "未找到相关信息"}]
    elif intent == "查物流":
        # 模拟 NL2SQL 查数据库
        context = [{"content": f"物流单号查询结果：您的包裹正在运输中，当前位于上海分拣中心"}]
    elif intent == "查网点":
        context = [{"content": f"您附近的网点：上海市浦东新区张江营业部，电话 021-12345678"}]
    else:
        context = [{"content": "抱歉，我无法处理这个问题，请咨询人工客服"}]

    # Step 3: 生成回答
    return rag_answer(question, context)


print("\n" + "=" * 50)
print("完整物流 RAG 流程模拟")
print("=" * 50)
for q in test_queries:
    print(f"\n用户：{q}")
    answer = logistics_rag_pipeline(q)
    print(f"客服：{answer}")


# TODO 4：设计一种新的物流查询场景
# 例如：查时效、查价格、查保价费...
# 并写在下面的字符串中
my_scenario = """
"""

print(f"\n我的场景：{my_scenario}")

print("\n✅ Day 11 练习完成！")
print("物流 RAG = 意图分类 + 路由检索 + LLM 生成")
