"""
Day 12 练习：评论智能分类与信息抽取系统
完成后运行：python practice_12.py

目标：理解联合抽取、LoRA 微调、梯度检查点的核心概念
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
# 第一组：数据格式转换
# ============================================================

# 原始评论
raw_reviews = [
    "质量很差，用了三天就坏了，客服态度也差",
    "物流很快，包装很严实，非常满意",
    "价格便宜但质量一般，一分钱一分货",
    "颜色和图片不一样，申请退货客服半天不回复",
]

# TODO 1：设计评论数据的统一格式
# 每一条评论转成：
#   {"input": "...", "categories": [...], "entities": [...]}
def format_training_data(text: str) -> dict:
    """将原始评论转成训练格式"""
    # 用 LLM 帮助标注
    prompt = f"""分析以下评论，输出 JSON 格式：

评论：{text}

输出格式：
{{
    "categories": ["类别1", "类别2"],
    "entities": [
        {{"entity": "实体类型", "attribute": "属性", "value": "描述", "sentiment": "正面/负面/中性"}}
    ]
}}

类别范围：质量好评、质量投诉、物流好评、物流投诉、服务好评、服务投诉、价格好评、价格投诉
注意：只输出 JSON，不要其他文字。"""

    resp = client.chat.completions.create(
        model="deepseek-chat",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.1,
        response_format={"type": "json_object"},
    )
    content = resp.choices[0].message.content
    try:
        return json.loads(content)
    except:
        return {"categories": [], "entities": []}


print("评论数据标注")
print("=" * 50)
training_data = []
for r in raw_reviews:
    labeled = format_training_data(r)
    labeled["input"] = r
    training_data.append(labeled)
    print(f"\n评论：{r}")
    print(f"  类别：{labeled.get('categories', [])}")
    print(f"  实体：{labeled.get('entities', [])}")

# 保存到 JSON
with open(os.path.join(os.path.dirname(__file__), "training_data.json"), "w", encoding="utf-8") as f:
    json.dump(training_data, f, ensure_ascii=False, indent=2)
print(f"\n已保存 {len(training_data)} 条训练数据到 training_data.json")
print()


# ============================================================
# 第二组：模拟 ChatGLM-6B + LoRA 联合抽取
# ============================================================

# 联合抽取 = Joint Extraction = 同时抽实体和关系
# 这里用 DeepSeek API 模拟微调后的效果

def joint_extract(text: str) -> dict:
    """模拟联合抽取：一次性输出实体 + 关系"""
    prompt = f"""从以下评论中抽取结构化信息。

评论：{text}

请提取：
1. 评论类别（质量、物流、服务、价格 等，带好评/投诉）
2. 涉及实体（产品、客服、物流、包装、价格 等）
3. 每个实体的属性、值、情感倾向
4. 实体之间的关系

输出 JSON 格式："""
    resp = client.chat.completions.create(
        model="deepseek-chat",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.1,
        response_format={"type": "json_object"},
    )
    content = resp.choices[0].message.content
    try:
        return json.loads(content)
    except:
        return {"error": "解析失败"}


print("联合抽取模拟（实体 + 关系同时输出）")
print("=" * 50)
for r in raw_reviews:
    result = joint_extract(r)
    print(f"\n评论：{r}")
    print(f"  抽取结果：{json.dumps(result, ensure_ascii=False)}")
print()


# ============================================================
# 第三组：计算 LoRA 参数量
# ============================================================

# TODO 2：计算 LoRA 节省的参数量

# ChatGLM-6B 的配置
hidden_size = 4096          # 隐藏层维度
num_layers = 28             # 层数
num_heads = 32              # 注意力头数
head_dim = hidden_size // num_heads  # 每个头的维度

# 需要加 LoRA 的目标模块
target_modules = ["q_proj", "k_proj", "v_proj", "o_proj"]
weight_shape = (hidden_size, hidden_size)  # 每个注意力权重矩阵的形状

# 标准 Fine-Tuning 要训练的参数
ft_params = sum(hidden_size * hidden_size for _ in target_modules) * num_layers
print(f"\n标准 Fine-Tuning 要训练的参数：{ft_params/1e6:.1f}M")

# TODO 3：补全 LoRA 参数量计算
lora_r = 8  # LoRA 秩

# LoRA 每个权重矩阵：A (d×r) + B (r×d) = 2×d×r
lora_params_per_module = 2 * hidden_size * lora_r
lora_params_total = lora_params_per_module * len(target_modules) * num_layers

print(f"LoRA (r={lora_r}) 要训练的参数：{lora_params_total/1e3:.1f}K")
print(f"节省比例：{(1 - lora_params_total/ft_params)*100:.2f}%")
print()


# ============================================================
# 第四组：梯度检查点显存计算
# ============================================================

# ChatGLM-6B 的显存分析
model_params = 6_000_000_000  # 6B
dtype_bytes = 2  # FP16

# 模型本身（FP16）
model_memory = model_params * dtype_bytes

# TODO 4：计算不同配置下的显存占用
# 假设中间激活值占用是模型参数的 1.5 倍（无梯度检查点）
# 梯度检查点后，中间激活值减少 80%
activation_ratio = 1.5
activation_memory = model_memory * activation_ratio
activation_memory_ckpt = activation_memory * 0.2  # 梯度检查点减少 80%

print("ChatGLM-6B 显存分析")
print("=" * 50)
print(f"模型参数（FP16）：{model_memory / 1024**3:.1f} GB")

optimizer_memory = model_memory * 0.67  # Adam 优化器状态
print(f"优化器状态：{optimizer_memory / 1024**3:.1f} GB")

print(f"\n--- 有梯度检查点 ---")
total_ckpt = (model_memory + optimizer_memory + activation_memory_ckpt) / 1024**3
print(f"中间激活值：{activation_memory_ckpt / 1024**3:.1f} GB")
print(f"总计：{total_ckpt:.1f} GB")
print(f"（16GB 单卡{'✅ 可训练' if total_ckpt < 14 else '❌ 不够用'}）")

print(f"\n--- 无梯度检查点 ---")
total_no_ckpt = (model_memory + optimizer_memory + activation_memory) / 1024**3
print(f"中间激活值：{activation_memory / 1024**3:.1f} GB")
print(f"总计：{total_no_ckpt:.1f} GB")
print(f"（16GB 单卡{'✅ 可训练' if total_no_ckpt < 14 else '❌ 不够用'}）")
print()


# ============================================================
# 第五组：模拟趋动云部署
# ============================================================

# TODO 5：写一个简单的推理函数
def predict_review(text: str, model_path: str = "lora_weights") -> str:
    """模拟加载 LoRA 权重后进行推理"""
    prompt = f"""你是一个评论分析模型，基于 ChatGLM-6B + LoRA 微调。

评论：{text}

请输出结构化分析结果（JSON 格式）：
- categories: 评论类别列表
- entities: 抽取的实体列表（含实体、属性、值、情感）
- summary: 一句话总结"""

    resp = client.chat.completions.create(
        model="deepseek-chat",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.1,
        response_format={"type": "json_object"},
    )
    return resp.choices[0].message.content


print("趋动云部署模拟（推理测试）")
print("=" * 50)
test_reviews = [
    "这个手机壳手感很好，就是有点贵",
    "快递员态度太差了，投诉！",
    "第二次购买了，质量一如既往的好",
]
for r in test_reviews:
    result = predict_review(r)
    print(f"\n输入：{r}")
    print(f"输出：{result}")


print("\n✅ Day 12 练习完成！")
print("评论分析 = ChatGLM + LoRA + 联合抽取 + 梯度检查点 + 趋动云")
