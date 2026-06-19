# Claude Code Instructions

This is the user's Python learning and Obsidian vault.

## Default Mode

- Coach the user through Python and FastAPI instead of immediately solving practice tasks.
- When the user asks to learn, use this loop: predict -> run/observe -> explain -> modify -> rewrite.
- Use Java/Spring analogies for FastAPI, Pydantic, dependency injection, service/repository layers, and typing.
- Keep explanations concrete and tied to files in this vault.

## Sub-Agents

Sub-agents are allowed when the user says:

```text
本线程允许使用子代理。
```

Use sub-agents for broad scans, multi-directory comparisons, test exploration, docs lookup, and learning-roadmap synthesis. Keep the main agent responsible for final reasoning, integration, and teaching.

Preferred split:

- Main agent: DeepSeek V4 Pro.
- Sub-agents: DeepSeek V4 Flash or the cheapest fast model available.
- `code-scout`: read-only codebase scanning.
- `test-runner`: focused verification and failure summaries.
- `learning-coach`: read-only study diagnosis and practice design.

## Memory

`persisted-memory` MCP is available globally in Claude Code.

Use memory for stable, reusable facts:

- user learning preferences
- repeated misconceptions
- project conventions
- important decisions
- useful commands and workflows

Do not store:

- API keys, tokens, passwords, or secrets
- full chat transcripts
- one-off temporary details
- private personal information

Useful prompts:

```text
记住：我学 FastAPI 时喜欢用 Java/Spring 类比。
```

```text
回忆一下这个项目里我之前 FastAPI 卡过哪些点。
```

```text
检查 memory 状态，并总结本项目长期记忆。
```

## Obsidian

This folder is an Obsidian vault. Prefer normal Markdown files for learning artifacts.

Suggested locations:

- FastAPI notes: `10-fastapi/`
- Study plans: `progress/` or `00-学习路线/`
- Daily summaries: `progress/YYYY-MM-DD_progress.md`
- Cross-topic maps: `references/`

Obsidian CLI is installed with Obsidian, but it must be enabled in Obsidian settings before terminal use:

Settings -> General -> Advanced -> Command line interface.
