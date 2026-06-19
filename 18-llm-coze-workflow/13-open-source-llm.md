---
aliases:
  - 13-open-source-llm
---
# 13. 主流开源大模型

> 前置：[[11-llm-architecture]] · [[12-chatgpt-principle]]
> 目标：了解主流开源模型的特点和选型方式
> 用时：约 10 分钟
>
> 相关笔记：[[14-llm-application-practice]]

---

## 一、开源大模型全景

| 模型 | 开发方 | 特点 | 适合场景 |
|------|--------|------|---------|
| **LLaMA** | Meta | 开源生态最强、衍生模型最多 | 本地部署、学术研究 |
| **Qwen（通义千问）** | 阿里 | 中文能力强、工具调用好 | 中文场景、Agent 开发 |
| **ChatGLM** | 智谱/清华 | 中英双语、GLM 架构 | 中文对话、企业应用 |
| **DeepSeek** | 深度求索 | 推理能力强、API 便宜 | 编程辅助、复杂推理 |
| **Baichuan** | 百川智能 | 中文优化 | 中文生成任务 |
| **BLOOM** | BigScience | 多语言开源协作 | 多语言研究 |

---

## 二、LLaMA 系列

```
Meta 开源
开发生态最强 → 衍生出 Alpaca、Vicuna、Mistral 等
本地部署资料最丰富 → Ollama 支持最完善
```

**适合你**：如果要在自己电脑上跑模型，LLaMA 的变体（通过 Ollama）是最省心的选择。

---

## 三、Qwen（通义千问）

```
阿里开发
中文能力非常强
支持工具调用（Function Calling）
有专门的代码模型（Qwen-Coder）
```

**适合你**：做中文 AI Agent 开发时，Qwen 的工具调用能力是关键优势。

---

## 四、ChatGLM

```
智谱AI / 清华大学
中英双语
GLM 架构（不是纯 Decoder-Only，是混合架构）
在国内社区活跃
```

**适合你**：中文场景的备选方案，特别是需要学术授权或私有化部署时。

---

## 五、DeepSeek

```
深度求索
推理能力强，尤其代码和数学
API 价格极低（几乎是最便宜的商业模型之一）
开源模型在编程评测中表现好
```

**适合你**：你在用 Claude Code 做开发，如果未来想自己写一个编程助手，DeepSeek 是性价比较高的选择。

---

## 六、如何选模型

### 决策树

```text
有网络 → 用 API（GPT/Claude/通义千问/DeepSeek）
没网络 → 用 Ollama 跑本地模型

中文为主 → Qwen / ChatGLM / DeepSeek
英文为主 → LLaMA 系列

需要工具调用 → Qwen / GPT / Claude
需要代码能力 → DeepSeek / GPT / Claude

免费 → 开源模型（Ollama 本地跑）或国产模型免费额度
付费 → GPT-4 / Claude Opus（最强但贵）
```

### 你的场景

| 场景 | 推荐 |
|------|------|
| 学习 AI Agent 开发 | Qwen（免费额度 + 中文好 + 工具调用） |
| 本地实验 | Ollama + LLaMA 3 / Qwen 2.5 |
| 扣子工作流 | 用平台内置模型即可 |
| 写代码辅助 | 继续用 Claude Code |
| 自己做 AI 项目 | Qwen API 或 DeepSeek API（性价比） |

---

## 七、模型 ≠ 产品

```
模型: GPT-4、Claude、Qwen、DeepSeek
      ↓ 通过 API 或本地部署调用
产品: ChatGPT、Claude Code、通义千问 App、DeepSeek Chat
      ↓ 封装了 UI、记忆、工具
你: 可以基于模型 API 自己造产品
```

**你做的 AI Agent 项目就是"基于模型 API 的产品"。**
