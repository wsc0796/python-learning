---
aliases:
  - 12-project-review-classification
---
# Day 12：项目实战——评论智能分类与信息抽取系统

读完约 20 分钟。

---

## 一、项目背景

某电商平台需要对海量用户评论进行自动化分析：

```
原始评论 → 分析系统 → 结构化结果

"质量很差，用了三天就坏了，客服态度也差"
→ 类别：质量投诉 + 服务投诉
→ 实体：产品（三天坏）、客服（态度差）

"物流很快，包装很严实"
→ 类别：物流好评
→ 实体：物流（快）、包装（严实）
```

### 需求拆解

| 需求 | 技术方案 |
|------|---------|
| 评论分类（好评/差评/具体类别） | ChatGLM-6B + LoRA 微调 |
| 抽取评论中的关键信息 | 联合抽取（实体 + 关系同时抽取） |
| 数据标注 | 人工标注 + 数据格式统一 |
| 训练优化 | 梯度检查点降低显存 |
| 部署 | 趋动云 GPU 部署 |

### 为什么用 ChatGLM-6B + LoRA

```
选型理由：
① ChatGLM-6B 对中文理解好，适合评论分析
② 6B 参数单卡能跑（配合 LoRA + 梯度检查点）
③ LoRA 训练快，存储小（只需存几十 MB 的权重）
④ 趋动云提供共享 GPU，成本低
```

---

## 二、数据格式设计

### 输入输出格式

```json
{
    "input": "质量很差，用了三天就坏了，客服态度也差",
    "output": {
        "categories": ["质量投诉", "服务投诉"],
        "entities": [
            {"entity": "产品", "attribute": "寿命", "value": "三天", "sentiment": "负面"},
            {"entity": "客服", "attribute": "态度", "value": "差", "sentiment": "负面"}
        ]
    }
}
```

### 用于微调的纯文本格式

把 JSON 转成 ChatGLM 的对话格式：

```text
[USER] 分析评论：质量很差，用了三天就坏了，客服态度也差

[ASSISTANT] 类别：质量投诉、服务投诉
实体：
- 产品 | 寿命 | 三天 | 负面
- 客服 | 态度 | 差 | 负面
```

### 数据准备流程

```
原始评论（CSV/Excel）
    ↓
人工标注分类标签
    ↓
人工标注实体和属性
    ↓
转成统一训练格式
    ↓
划分训练集/验证集/测试集（8:1:1）
```

---

## 三、ChatGLM-6B + LoRA 微调

### 整体流程

```
基础模型：ChatGLM-6B（冻结全部参数）
    ↓
加入 LoRA 适配器（只训练 ~0.1% 参数）
    ↓
加载训练数据（评论 → 分类 + 抽取）
    ↓
训练（用梯度检查点节省显存）
    ↓
保存 LoRA 权重（~50MB）
    ↓
推理时合并权重或动态加载
```

### LoRA 配置

```python
from peft import LoraConfig, get_peft_model, TaskType

lora_config = LoraConfig(
    task_type=TaskType.CAUSAL_LM,    # 因果语言模型（ChatGLM 属于此类）
    r=8,                              # 秩——控制参数量
    lora_alpha=32,                    # 缩放系数
    lora_dropout=0.1,                 # 防止过拟合
    target_modules=["q_proj", "v_proj", "k_proj", "o_proj"],
    # 对注意力层的 Q/K/V/O 都加 LoRA
)

model = get_peft_model(base_model, lora_config)
```

### 参数选择依据

| 参数 | 值 | 理由 |
|------|----|------|
| r=8 | 较小 | 评论分类任务相对简单，r=8 足够 |
| lora_alpha=32 | 适中 | alpha/r = 4，常见配置 |
| target_modules | Q/K/V/O | 注意力层最关键 |
| lora_dropout=0.1 | 小 | 防止过拟合但不影响收敛 |

---

## 四、梯度检查点（Gradient Checkpointing）

### 为什么要用

```
ChatGLM-6B 的显存占用：
  模型本身：~12GB（FP16）
  优化器状态：~4GB
  中间激活值：~8GB（随 batch size 变化）
  
  总计需要 ~24GB 显存 → 单卡 24GB 勉强，但很紧
  加上 LoRA 的额外参数 + batch > 1 → 显存爆炸
```

### 梯度检查点原理

```
正常训练：
  前向：计算每层激活值 → 存着 → 反向传播用
  显存占用：O(n) 层激活值

梯度检查点：
  前向：正常计算，但丢弃中间激活值
  反向：需要时重新计算一次前向
  显存占用：O(1) 层激活值
  代价：多算一次前向，速度慢 ~20%
```

### 代码实现

```python
from transformers import TrainingArguments

training_args = TrainingArguments(
    output_dir="./checkpoints",
    per_device_train_batch_size=4,
    gradient_checkpointing=True,  # 开启梯度检查点
    optim="adamw_torch",
    save_steps=500,
    logging_steps=100,
    learning_rate=2e-4,
    num_train_epochs=3,
)

# 梯度检查点 + LoRA = 6B 模型能在 16GB 单卡上训练
```

### 显存对比

| 配置 | 显存占用 | 速度 |
|------|---------|------|
| 无梯度检查点 | ~24GB | 基准 |
| 梯度检查点 | ~16GB | 慢 ~20% |
| 梯度检查点 + LoRA r=8 | ~12GB | 慢 ~20% |

---

## 五、联合抽取（Joint Extraction）

### 什么是联合抽取

传统做法是 pipeline 式（分两步）：

```
评论 → [命名实体识别] → 抽取实体 → [关系分类] → 抽取关系
                        ↑ 误差会传递到下一步
```

联合抽取（Joint Extraction）一次性完成：

```
评论 → [一个模型] → 实体 + 关系同时输出
                     ↑ 共享编码层，互相增强
```

### 在 ChatGLM 中实现联合抽取

核心思路：把联合抽取转化为文本生成任务。

```
输入：分析评论：质量很差，用了三天就坏了，客服态度也差

输出：[
  {"实体类型": "产品", "属性": "寿命", "值": "三天", "情感": "负面"},
  {"实体类型": "客服", "属性": "态度", "值": "差", "情感": "负面"}
]
```

这样 ChatGLM 的生成能力直接用于抽取，不需要额外分类头。

### 为什么生成式抽取有效

```
ChatGLM 经过大量中文预训练，天然理解：
  - "用了三天就坏了" → 产品寿命短
  - "客服态度也差" → 服务态度差

LoRA 微调的作用是让模型学会"输出格式"，
而不是学会"理解评论"（它本来就能理解）。
```

---

## 六、趋动云部署

### 什么是趋动云

趋动云（Gemini Cloud）提供共享 GPU 资源，适合：
- 学校实验室没有 GPU
- 自己买卡太贵
- 只需要偶尔训练

### 部署流程

```
① 注册趋动云账号 → 创建工作空间
② 选择镜像（PyTorch + CUDA 预装）
③ 上传代码和数据
```bash
# 上传到工作空间
git clone your-repo
cd review-analysis

# 安装依赖
pip install transformers peft datasets
pip install chatglm-6b  # 或从 HuggingFace 下载
```

④ 启动训练
```bash
python train.py \
    --model_path /path/to/chatglm-6b \
    --data_path ./data/reviews.json \
    --output_dir ./output \
    --batch_size 4 \
    --epochs 3 \
    --lora_r 8
```

⑤ 推理测试
```bash
python predict.py --input "这个产品太差了"
```
```

### 趋动云 vs 本地

| 对比 | 本地（你的笔记本） | 趋动云 |
|------|------------------|--------|
| GPU | Intel Iris Xe（无 CUDA） | 共享 A100 / 4090 |
| 能否训练 6B 模型 | ❌ | ✅ |
| 费用 | 电费 | 按小时计费 |
| 适合 | 小模型、测试 | 大模型训练 |

---

## 七、完整项目结构

```
review-analysis/
├── data/
│   ├── raw_reviews.csv       # 原始评论
│   ├── train.json            # 训练数据（统一格式）
│   └── test.json             # 测试数据
├── model/
│   ├── config.py             # LoRA 配置
│   └── chatglm_lora.py       # 微调代码
├── train.py                  # 训练入口
├── predict.py                # 推理入口
└── deploy.sh                 # 趋动云部署脚本
```

### 训练脚本核心结构

```python
# train.py
def train():
    # 1. 加载 ChatGLM-6B
    tokenizer = AutoTokenizer.from_pretrained("THUDM/chatglm-6b", trust_remote_code=True)
    model = AutoModel.from_pretrained("THUDM/chatglm-6b", trust_remote_code=True)

    # 2. 添加 LoRA
    lora_config = LoraConfig(r=8, ...)
    model = get_peft_model(model, lora_config)

    # 3. 配置训练参数（含梯度检查点）
    training_args = TrainingArguments(
        gradient_checkpointing=True,
        ...
    )

    # 4. 训练
    trainer = Trainer(model=model, args=training_args, train_dataset=train_data)
    trainer.train()

    # 5. 保存 LoRA 权重
    model.save_pretrained("./output/lora_weights")
```

---

## 八、和你的已有知识的关系

```
你之前学的 → 在这个项目中的应用
────────────────────────────────────
Day 3 LoRA → ChatGLM-6B 的 LoRA 微调
Day 1 PET  → 数据的 Pattern 设计
Day 4 Function Call → 趋动云部署的 API 封装
Day 5 Agent → 评论分析 Agent 的 Tool 设计
你的 document_pipeline → 数据预处理流程
```

---

## 九、延伸思考

```
如果能跑通这个项目，你可以扩展的方向：

① 多模态评论分析
   图文评论 → 图片 + 文本联合分析
   （需要多模态模型如 Qwen-VL）

② 实时评论监控
   结合消息队列（Kafka）实现实时分析
   负面评论自动告警

③ 评论情感趋势
   按时间统计情感变化曲线
   发现产品质量问题的爆发点

④ 和 Agent 结合
   评论分析 Agent → 自动生成回复 → 自动发送
   形成"分析 → 决策 → 行动"闭环
```
