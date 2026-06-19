---
date: 2026-05-20
status: configured
---

# Claude Code + DeepSeek + Memory + Obsidian 配置说明

## 当前分工

```text
Claude Code
  -> DeepSeek V4 Pro: 主代理，负责关键判断、架构、解释、最终实现
  -> DeepSeek V4 Flash: 子代理，负责扫描、检索、测试、整理
  -> persisted-memory MCP: 长期记忆，保存稳定偏好和项目经验
  -> Obsidian vault: 人类可读学习笔记、复盘、路线图
```

## 使用口令

需要大范围扫描或并行分析时，在新线程开头说：

```text
本线程允许使用子代理。
```

适合子代理的任务：

- 扫描多个学习目录并总结薄弱点
- 对比 `07-pydantic`、`08-typing-di`、`10-fastapi`
- 跑测试并整理失败原因
- 查调用链、找文件、整理学习计划

不需要子代理的任务：

- 解释一个函数
- 带你走一条 FastAPI 调用链
- 批改一个短练习
- 做问答式陪练

## 记忆规则

可以让 Claude 记住：

- 学习偏好
- 反复卡住的知识点
- 项目约定
- 重要决策
- 常用命令

不要写入记忆：

- API key、token、密码
- 完整聊天记录
- 一次性临时信息
- 私密个人信息

## Obsidian

本目录就是 Obsidian vault。学习复盘、计划和知识地图优先写 Markdown 文件。

Obsidian CLI 已加入用户 PATH，但还需要在 Obsidian 内手动启用：

```text
Settings -> General -> Advanced -> Command line interface
```

启用后，新终端里可以用：

```powershell
obsidian --help
```
