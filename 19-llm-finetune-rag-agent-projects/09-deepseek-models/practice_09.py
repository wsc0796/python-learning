"""
Day 9 练习：DeepSeek 模型理解
完成后运行：python practice_09.py

目标：理解 MLA、MoE 的基本概念
"""
import sys
sys.stdout.reconfigure(encoding="utf-8", errors="replace")


# ============================================================
# 第一组：理解 MoE 的参数量节省
# ============================================================

# DeepSeek V3 的规模
total_params = 671_000_000_000  # 671B
active_params = 37_000_000_000  # 37B
experts = 256
active_experts = 2

print("DeepSeek V3 MoE 规模")
print("=" * 50)
print(f"总参数量：{total_params/1e9:.0f}B")
print(f"每次激活参数量：{active_params/1e9:.0f}B")
print(f"激活比例：{active_params/total_params*100:.1f}%")

# TODO 1：如果改用传统 Dense 模型
# 要达到同样效果，参数量大约需要 671B
# 每次推理的计算量相当于 37B 模型
print()
print("计算量对比：")
print(f"  Dense 671B：每次推理用 671B 参数")
print(f"  MoE 671B：每次推理只用 {active_params/1e9:.0f}B 参数")
print(f"  节省：{(1 - active_params/total_params)*100:.1f}% 的计算量")
print()

# TODO 2：如果每次只激活 2/256 的专家
# 理论上推理速度应该是多少？
speed_ratio = active_experts / experts
print(f"专家激活比例：{active_experts}/{experts} = {speed_ratio*100:.1f}%")
print(f"（但实际上 Router 和通信也有开销，不是简单的比例关系）")


# ============================================================
# 第二组：理解 MLA 的 KV Cache 节省
# ============================================================

# 标准 MHA 的 KV Cache
num_layers = 60
num_heads = 32
head_dim = 128
seq_len = 8192
dtype_bytes = 2  # float16

# 标准 MHA
kv_cache_mha = num_layers * num_heads * seq_len * head_dim * 2 * dtype_bytes
# 2 代表 K 和 V

# MLA（假设压缩到 head_dim 的一半）
latent_dim = head_dim // 2
kv_cache_mla = num_layers * seq_len * latent_dim * 2 * dtype_bytes

print(f"\n标准 MHA KV Cache：{kv_cache_mha / 1024**3:.2f} GB")
print(f"MLA KV Cache：{kv_cache_mla / 1024**3:.2f} GB")
print(f"节省比例：{(1 - kv_cache_mla/kv_cache_mha)*100:.0f}%")


# ============================================================
# 第三组：DeepSeek 系列总结
# ============================================================

# TODO 3：填写你的理解
print("\n" + "=" * 50)
print("DeepSeek 系列总结")
print("=" * 50)

qas = [
    "DeepSeek API 为什么比 GPT-4 便宜？",
    "MLA 解决什么问题？",
    "MoE 的核心思想是什么？",
    "R1 和 V3 的区别是什么？",
]

for q in qas:
    print(f"\nQ：{q}")
    print("A：")  # TODO：填你的理解


print("\n✅ Day 9 练习完成！")
print("MLA = 省显存，MoE = 省计算，两个一起 = DeepSeek 又强又便宜。")
