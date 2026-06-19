"""
Day 2 练习：提示词工程进阶
完成后运行：python practice_02.py

目标：学会设计 Zero-shot、Few-shot、CoT 提示词
注：这天的练习调 DeepSeek API
"""
import sys
import os
sys.stdout.reconfigure(encoding="utf-8", errors="replace")

from openai import OpenAI
client = OpenAI(
    api_key=os.environ.get("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com/v1"
)


def ask(prompt: str) -> str:
    """调 DeepSeek 的辅助函数"""
    resp = client.chat.completions.create(
        model="deepseek-chat",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3,
        max_tokens=500,
    )
    return resp.choices[0].message.content


# ============================================================
# 第一组：Zero-shot vs Few-shot
# ============================================================

texts = [
    "这个耳机音质不错，但续航太短了。",
    "客服态度很好，问题很快就解决了。",
    "物流太慢了，等了一周还没到。",
]

# TODO 1：写一个 Zero-shot Prompt
zero_shot_prompt = """
请判断情感倾向（正面/负面）：
"""

print("=" * 50)
print("Zero-shot 结果")
print("=" * 50)
for t in texts:
    result = ask(zero_shot_prompt + t)
    print(f"  {t[:20]}... → {result.strip()}")

print()

# TODO 2：写一个 Few-shot Prompt（给 2 个示例）
few_shot_prompt = """判断情感倾向（正面/负面）。

示例1：这家店服务很好。 → 正面
示例2：物流太慢了。 → 负面

"""

print("=" * 50)
print("Few-shot 结果")
print("=" * 50)
for t in texts:
    result = ask(few_shot_prompt + t)
    print(f"  {t[:20]}... → {result.strip()}")

print()


# ============================================================
# 第二组：CoT 思维链
# ============================================================

# TODO 3：用 CoT（加"请一步步思考"）解推理题
reasoning_questions = [
    "一件商品原价200元，打8折后再减30元，最后多少钱？",
    "A比B大5岁，B比C大3岁，三人年龄总和是56岁，C多少岁？",
]

print("=" * 50)
print("CoT 推理结果")
print("=" * 50)
for q in reasoning_questions:
    # TODO 4：补全 CoT Prompt
    cot_prompt = f"{q}\n\n请一步步思考。"
    result = ask(cot_prompt)
    print(f"问题：{q}")
    print(f"回答：\n{result}\n")


# ============================================================
# 第三组：设计一个完整的 Instruction
# ============================================================

# TODO 5：为"商品信息抽取"任务设计 Instruction
# 要求：从评论中抽取 商品名、情感、问题类型、用户诉求
# 输出格式：JSON

instruction = """
你是一名商品评论分析助手。

任务：从用户评论中抽取关键信息。

输出 JSON 格式：
{
    "product": "",
    "sentiment": "",
    "problem_type": "",
    "user_request": ""
}
"""

test_comments = [
    "这个蓝牙耳机音质不错，但是续航太短了，希望改进。",
    "快递三天了还没到，客服也不回消息，我要退货！",
]

print("=" * 50)
print("Instruction 抽取结果")
print("=" * 50)
for c in test_comments:
    result = ask(instruction + f"\n评论：{c}")
    print(f"评论：{c}")
    print(f"结果：{result}\n")


print("✅ Day 2 练习完成！")
print("对比 Zero-shot vs Few-shot 的结果差异，理解 ICL 的作用。")
