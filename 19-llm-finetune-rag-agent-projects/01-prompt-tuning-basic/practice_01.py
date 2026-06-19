"""
Day 1 练习：Prompt-Tuning 入门
完成后运行：python practice_01.py

目标：理解 Hard Prompt 和 PET 的基本概念
注：这天的练习不调 API，只做概念理解
"""
import sys
sys.stdout.reconfigure(encoding="utf-8", errors="replace")


# ============================================================
# 第一组：理解 Hard Prompt
# ============================================================

# TODO 1：补全 Prompt 模板
# 要求：让模型能理解这是一个情感分类任务
sentiment_prompt = ""

# 示例输入
text = "这家餐厅味道很好，服务也很棒。"
# 期望输出：模型能正确判断为正面

# 请写出一个完整的情感分类 Prompt：
full_prompt = f"{sentiment_prompt}\n{text}"
print("Prompt 示例：")
print(full_prompt)
print()


# ============================================================
# 第二组：理解 PET 的 Verbalizer
# ============================================================

# PET 把分类转成完形填空，需要定义标签→词的映射
# 情感分类：正面/负面 → 好/差

# TODO 2：补全 Verbalizer 映射
verbalizer = {
    "正面": "",  # 填什么词？
    "负面": "",  # 填什么词？
}

# TODO 3：设计一个 Pattern（模板），把分类改成填空
# 原句：这家餐厅味道很好。
# Pattern：____________________ [MASK] ____________________

sentences = [
    "这家餐厅味道很好。",
    "物流太慢了，等了一周。",
    "这个产品性价比很高。",
    "客服态度很差。",
]

print("=" * 50)
print("PET 模式理解")
print("=" * 50)

for s in sentences:
    # TODO 4：用你的 Pattern 包装每个句子
    # pattern_sentence = ?
    pass  # 删除这行，写上你的代码

print()


# ============================================================
# 第三组：理解 Prompt-Tuning 和 Fine-Tuning 的区别
# ============================================================

# 请回答以下问题（用 print 输出你的答案）

# TODO 5：什么时候应该用 Fine-Tuning 而不是 Prompt-Tuning？
print("Q5：Fine-Tuning 比 Prompt-Tuning 更适合的场景：")
print("你的答案：")
print()

# TODO 6：什么时候 Prompt-Tuning 比 Fine-Tuning 更合适？
print("Q6：Prompt-Tuning 比 Fine-Tuning 更合适的场景：")
print("你的答案：")
print()


print("✅ Day 1 练习完成！")
print("如果还有不清楚的概念，回顾 theory_01.md")
