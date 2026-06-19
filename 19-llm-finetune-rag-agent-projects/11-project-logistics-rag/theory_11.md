---
aliases:
  - 11-project-logistics-rag
---
# Day 11：项目实战——物流行业 RAG 系统

读完约 20 分钟。

---

## 一、项目背景

某物流公司需要构建一个智能客服系统，帮助客户查询物流状态、运费规则、网点信息、禁运品清单等。

### 需求分析

```
客户问："我的包裹到哪了？"
→ 查询物流轨迹（查数据库）

客户问："寄到新疆多少钱？"
→ 查询运费规则（查知识库）

客户问："能寄打火机吗？"
→ 查询禁运品清单（查知识库）

客户问："最近的网点在哪？"
→ 查询网点信息（查数据库 + 地图）
```

### 技术选型

| 模块 | 选型 | 理由 |
|------|------|------|
| 文本分类 | BERT + PET / P-Tuning | 意图识别，轻量高效 |
| 知识检索 | Milvus + DeepSeek Embedding | 向量检索运费/规则 |
| 数据查询 | NL2SQL（参考 DatabaseAgent） | 物流轨迹、网点 |
| 生成回答 | DeepSeek V4 | 综合上下文生成自然语言 |
| 编排框架 | LangChain / 自建 Pipeline | 分类 → 检索 → 生成 |

---

## 二、第一步：意图分类（BERT + PET）

### 为什么先分类

```
用户问题 → [意图分类] → 
  ├─ "查物流" → 查数据库
  ├─ "查运费" → 查知识库
  ├─ "查网点" → 查数据库
  └─ "查禁运品" → 查知识库
```

不同意图走不同的检索路径，分类是第一步。

### BERT + PET 方案

PET（Pattern-Exploiting Training）把分类任务转化成填空任务：

```
输入：查一下从上海到北京的运费是多少
模板：[CLS] 查一下从上海到北京的运费是多少 [MASK] [SEP]

类别映射（Verbalizer）：
  "查询物流" → "物流"
  "查询运费" → "运费"
  "查询网点" → "网点"
  "查询禁运品" → "禁运"
  "其他"     → "其他"
```

### BERT + PET 训练流程

```
① 准备数据：意图分类数据集
   {"text": "我的包裹到哪了", "label": "查询物流"}
   {"text": "寄到上海多少钱", "label": "查询运费"}

② 设计模板（Pattern）
   原始：[CLS] {text} [MASK] [SEP]
   模板：[CLS] 这句话的意图是 {text} [MASK] [SEP]

③ 定义标签词（Verbalizer）
   "查询物流" → "物流",   "查询运费" → "运费"
   "查询网点" → "网点",   "查询禁运" → "禁运"

④ 训练：只训练 BERT 的 MLM head（少量参数）
⑤ 推理：用 BERT 预测 [MASK] 位置的词 → 映射回类别
```

### 为什么用 PET 而不是直接微调

```
传统 Fine-Tuning：在 BERT 上加分类头，全量微调
                → 每个分类任务单独存一个模型
                → 数据少时容易过拟合

PET：复用 BERT 的 MLM 能力，Few-shot 也能工作
    → 本质上是把分类还原成语言模型擅长的填空
    → 与 Prompt-Tuning 一脉相承
```

---

## 三、第二步：意图分类（BERT + P-Tuning）

### PET 的局限性

```
PET 的模板是固定的，需要人工设计。
模板好坏直接影响效果：
  "这句话的意图是 [MASK]"  ✓
  "[MASK] 这句话"          ✗（效果差）
```

### P-Tuning 的改进

P-Tuning 不依赖人工模板，而是在输入层加可训练的连续向量（Soft Prompt）：

```
原始输入：   [CLS] 我的包裹到哪了 [SEP]
P-Tuning：  [CLS] [P1] [P2] [P3] 我的包裹到哪了 [SEP]
                      ↑ 可训练的连续向量（不映射到任何词）
```

### P-Tuning 训练过程

```python
# 伪代码：P-Tuning 前向传播
class P TuningForClassification:
    def __init__(self, bert, prompt_length=5):
        self.bert = bert
        # 可训练的 Prompt 向量
        self.prompt_embeds = nn.Parameter(
            torch.randn(prompt_length, bert.hidden_size)
        )
        # 分类头
        self.classifier = nn.Linear(bert.hidden_size, num_classes)

    def forward(self, input_ids, attention_mask):
        # 将原始输入转成 embedding
        inputs_embeds = self.bert.embeddings(input_ids)

        # 在 embedding 前插入 Soft Prompt
        batch_size = inputs_embeds.size(0)
        prompts = self.prompt_embeds.unsqueeze(0).expand(batch_size, -1, -1)
        inputs_embeds = torch.cat([prompts, inputs_embeds], dim=1)

        # 通过 BERT
        outputs = self.bert(inputs_embeds=inputs_embeds)
        return self.classifier(outputs.pooler_output)
```

### PET vs P-Tuning 对比

| 维度 | PET | P-Tuning |
|------|-----|----------|
| 模板 | 人工设计自然语言模板 | 自动学习连续向量 |
| 训练参数 | BERT + MLM head | BERT + Prompt 向量 + 分类头 |
| 数据需求 | Few-shot 即可 | 需要更多数据 |
| 效果稳定 | 依赖模板质量 | 更稳定 |
| 推理速度 | 和 BERT 一样 | 和 BERT 一样 |

### 在本项目中的选择

```
物流意图分类：
  类别少（4-5 类）、数据量中等 → PET 就够用
  如果新增类别频繁 → P-Tuning 更灵活
```

---

## 四、第三步：RAG 检索（运费/规则查询）

### 数据准备

```python
# 运费规则文档示例
documents = [
    "上海到北京，首重12元/kg，续重6元/kg，时效2-3天",
    "上海到新疆，首重18元/kg，续重12元/kg，时效5-7天",
    "北京到广州，首重15元/kg，续重8元/kg，时效3-4天",
    # ... 更多规则
]

# 禁运品清单
prohibited_items = [
    "打火机、火柴等易燃易爆品禁止邮寄",
    "液体粉末状物品需单独申报",
    "活体动物（除指定宠物外）禁止邮寄",
    # ...
]
```

### 检索流程

```
用户问："寄到新疆多少钱？"

① 意图分类 → "查询运费"
② 知识检索：用 DeepSeek Embedding 向量化问题 → 在 Milvus 中检索
③ 返回 Top-3 相关运费规则
④ LLM 生成回答
```

### NL2SQL 查物流轨迹

参考你的 `hello-agents/Co-creation-projects/939147533-DatabaseAgent/` 的 NL2SQL 模式：

```
用户问："我的包裹 JD123456789 到哪了？"

① 意图分类 → "查询物流"
② NL2SQL：LLM 将自然语言转成 SQL
   SELECT status, location, update_time 
   FROM logistics 
   WHERE tracking_no = 'JD123456789'
③ 执行 SQL，返回结果
④ LLM 组织自然语言回答
```

---

## 五、完整系统架构

```
用户输入
    ↓
[意图分类] ← BERT + PET / P-Tuning
    │
    ├─ "查物流" → [NL2SQL] → 物流数据库 → 查询结果
    ├─ "查运费" → [向量检索] → Milvus(运费知识库)
    ├─ "查网点" → [NL2SQL] → 网点数据库
    └─ "查禁运" → [向量检索] → Milvus(禁运品知识库)
                         ↓
              [DeepSeek 生成回答]
                         ↓
                   返回用户
```

### 编排方式（参考你的 Pipeline）

```python
class LogisticsRAGPipeline:
    """物流 RAG 系统——基于你的 Pipeline 模式"""

    def __init__(self):
        self.classifier = IntentClassifier()  # BERT + PET
        self.vector_db = MilvusClient()       # 知识库
        self.db_agent = DatabaseAgent()        # NL2SQL
        self.llm = DeepSeekClient()           # 生成

    def run(self, question: str) -> str:
        # Step 1: 意图分类
        intent = self.classifier.predict(question)

        # Step 2: 根据意图选择检索策略
        if intent == "查物流":
            context = self.db_agent.query_tracking(question)
        elif intent == "查运费":
            context = self.vector_db.search(question, top_k=3)
        elif intent == "查网点":
            context = self.db_agent.query_branch(question)
        elif intent == "查禁运":
            context = self.vector_db.search(question, top_k=3)
        else:
            context = ""

        # Step 3: 生成回答
        return self.llm.generate(question, context)
```

---

## 六、和你的 document_pipeline 的关系

```
你的 pipeline：PDF → convert → segment → enrich → index → query

物流 RAG：意图分类 → 路由 → 检索 → 生成

共同点：
  - 都是 Pipeline 编排模式
  - 都有"检索"和"生成"两个阶段
  - 都可以用 Template Method 模式抽象

不同点：
  - 物流 RAG 多了"意图分类"这一步（路由）
  - 物流 RAG 用向量数据库（Milvus）代替 JSON 索引
  - 物流 RAG 需要实时查询数据库（NL2SQL）
```

---

## 七、参考项目

你电脑里已经有的参考：

| 项目 | 参考价值 |
|------|---------|
| `document_pipeline/paper_pipeline.py` | RAG 的 Pipeline 编排模式 |
| `hello-agents/.../DatabaseAgent/` | NL2SQL 的 Tool + ReAct 实现 |
| `hello-agents/.../HealthRecordAgent/` | Milvus 混合检索 + 失败降级 |
| `document_pipeline/local_pdf_pipeline.py` | 本地知识库构建流程 |

---

## 下一步

学习完这个项目设计后，进入 [[12-project-review-classification]]：另一个真实场景的端到端项目。
