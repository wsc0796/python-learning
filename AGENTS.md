# Agent Usage Policy

This repository allows sub-agent usage when the user says:

```text
本线程允许使用子代理。
```

Use sub-agents for broad scans, call-chain tracing, test exploration, documentation lookup, and learning-roadmap synthesis. Keep the main agent focused on key judgment, explanation, integration, and final review.

Preferred split:

- Main agent: DeepSeek V4 Pro through Claude Code for architecture, risky edits, final reasoning, and learning explanations.
- Sub-agents: DeepSeek V4 Flash / low-cost model for search, inventory, tests, and summaries.
- Memory: use the `persisted-memory` MCP for stable preferences, decisions, lessons, and recurring mistakes.
- Obsidian: this repository is also the user's Obsidian vault; write full learning notes and daily summaries as Markdown files in this vault when asked.

Learning rules:

- For Python/FastAPI study, coach first and avoid direct answers unless the user asks for implementation.
- Use Java/Spring comparisons when explaining FastAPI, Pydantic, DI, service/repository layering, and typing.
- Prefer exercises in this order: predict, run/observe, explain, modify, rewrite.
- Keep secrets, API keys, tokens, and private data out of memory and notes.

Good sub-agent tasks:

- Scan `07-pydantic`, `08-typing-di`, and `10-fastapi` and summarize the knowledge chain.
- Inspect test failures while the main agent explains the concept.
- Search the vault for recurring weak points and produce a one-week plan.
- Compare two practice implementations and report only behavioral differences.

Tasks that usually do not need sub-agents:

- Explain one function or one file.
- Walk through one FastAPI request path.
- Review a short user attempt.
- Ask quiz questions and check the user's answer.

## Codex + VS Code Parallel Workflow

Codex is available through the OpenAI Codex CLI/app and the VS Code extension. Use it for agentic coding work, local code review, repository scans, and background implementation tasks.

Parallel agent rules:

- If more than one agent will edit files, put each editing task in its own Git worktree or isolated branch.
- Do not let two agents edit the same file at the same time in the same checkout.
- Keep the local checkout for foreground learning, explanation, and final review.
- Use Codex worktrees for background implementation, migration experiments, broad refactors, and test-fixing attempts.
- Use read-only subagents for repository search, call-chain tracing, test inventory, and documentation lookup.
- Before merging worktree changes back, run the relevant checks and summarize changed files.

Recommended split:

- Main learning thread: explanation, architecture choices, risk judgment, and final integration.
- Codex background thread 1: implementation or refactor in an isolated worktree.
- Codex background thread 2: tests, validation, and failure investigation in a separate worktree.
- Claude Code: deep explanation and learning coaching when Python/FastAPI concepts are unclear.

Useful trigger phrase:

```text
本线程允许使用子代理；需要改文件时请使用 Codex worktree，避免直接抢写当前工作区。
```
