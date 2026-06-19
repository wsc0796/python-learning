"""
Day 3 练习：PEFT / LoRA 理解
完成后运行：python practice_03.py

目标：理解 LoRA 的参数量计算和配置
注：不实际训练，只做计算和理解
"""
import sys
sys.stdout.reconfigure(encoding="utf-8", errors="replace")


# ============================================================
# 第一组：理解 LoRA 的参数量节省
# ============================================================

# 假设一个权重矩阵 W 的形状是 4096 × 4096（LLaMA 规模）

d = 4096       # 输入维度
k = 4096       # 输出维度

# 原始权重参数量
original_params = d * k
print(f"原始权重参数：{original_params:,} ({original_params/1e6:.1f}M)")

# TODO 1：计算不同 r 值下 LoRA 的两个小矩阵总参数量
for r in [4, 8, 16, 32, 64]:
    # LoRA: A ∈ R^(d×r), B ∈ R^(r×k)
    lora_params = d * r + r * k  # A 的参数量 + B 的参数量
    ratio = lora_params / original_params * 100
    print(f"  r={r:2d}: LoRA 参数 {lora_params:>8,} ({lora_params/1e3:.1f}K) = {ratio:.3f}% 的原始参数")
print()


# ============================================================
# 第二组：理解为什么 LoRA 推理时无额外延迟
# ============================================================

# Fine-Tuning：W' = W 更新了，推理时直接用 W'
# LoRA：W' = W + BA，推理时可以合并到 W 中

print("LoRA 推理过程：")
print("  训练时：h = Wx + BAx（需要额外计算 BA）")
print("  推理时：W' = W + BA（先把 BA 合并到 W，然后 h = W'x）")
print("  结论：推理时零额外延迟 ✅")
print()

# TODO 2：为什么合并可行？
# 因为 W 和 BA 都是线性变换，可以合并成一个矩阵
# 你的理解：
reason = ""
print(f"合并可行的原因：{reason}")


# ============================================================
# 第三组：选择合适的 LoRA 配置
# ============================================================

# 下面有 3 个场景，请选择 r 值并说明理由

scenarios = [
    {
        "name": "情感分类任务",
        "data_size": 1000,
        "task_complexity": "低",
        "my_r": 0,  # TODO 3：填你的选择
        "reason": "",
    },
    {
        "name": "代码生成适配",
        "data_size": 50000,
        "task_complexity": "高",
        "my_r": 0,  # TODO 4：填你的选择
        "reason": "",
    },
    {
        "name": "领域术语适配",
        "data_size": 10000,
        "task_complexity": "中",
        "my_r": 0,  # TODO 5：填你的选择
        "reason": "",
    },
]

print("LoRA 配置选择练习：")
print("  r 的选择原则：任务越复杂、数据越多 → r 应该越大")
print("  参考：r=4(简单), r=8(中等), r=16(复杂), r=32(很复杂)")
print()

for s in scenarios:
    print(f"场景：{s['name']}（数据量：{s['data_size']}，复杂度：{s['task_complexity']}）")
    print(f"  选择的 r：{s['my_r']}")
    print(f"  理由：{s['reason']}")


print("\n✅ Day 3 练习完成！")
print("LoRA 的核心记忆点：两个小矩阵 + 推理时可合并 = 零额外开销")
