# Agent strategy, resource policy, and agent instruction files (stage 9)

## Strategies

| Strategy | Meaning | Default? |
|---|---|---|
| Single agent | One coding agent works sequentially | **Yes, always supported** |
| Single agent + subagents | The primary agent may delegate tasks (testing, research, review) | Only with approval |
| Multi-agent | Independent agents implement separate parts in parallel | Only with approval |
| Hybrid | Sequential by default; parallel only for explicitly approved tasks | Only with approval |

## Authorization rules

- Ask about subagents and about multi-agent or parallel work in **every** new project, even if the profile or an earlier project said yes. Record the answer and its date in state (`subagents`, `multi_agent`).
- Never assume that multiple agents, multiple subscriptions, unlimited usage, parallel support in the chosen agent, or Git worktrees are available or wanted.
- Without recorded approval, generated documents say: *"Work sequentially as a single agent. Do not start subagents or parallel agents."*
- Stage 9 establishes only whether subagents or parallel work are acceptable in principle for this project. The concrete approval, naming the exact tasks, is requested at stage 10, when the roadmap shows which tasks are independent, and recorded in state with the date and the task names. Without that second step parallel work stays forbidden.
- If you recommend parallel work, first explain: why it helps, which tasks are independent, expected token and resource use, coordination and integration needs, conflict risk, and whether worktrees or other infrastructure are needed. Always offer the sequential alternative. Approval covers only the tasks and agents named.
- This skill itself does not use subagents. Quality review is done inline.

## Resource policy (independent of project complexity)

| Policy | Behavior in generated prompts |
|---|---|
| Economical | Concise prompts, minimal context, reference spec files instead of repeating them, avoid extra agent calls and unnecessary documentation, sequential work |
| Balanced | Balance quality, verification, documentation and consumption |
| Comprehensive | Allow broader analysis, testing, documentation and review where justified |

A large app can be economical through small sequential milestones. No policy removes security checks, validation or acceptance criteria.

## Agent instruction files

Generate only the files for the selected target agents; keep the core spec agent-neutral. Conventions verified against official documentation in November 2026; re-verify if you can before relying on them, and say so if you cannot.

- `AGENTS.md`: Codex and other agents that read it. Codex concatenates files from the repository root down and caps combined size (32 KiB by default), so keep it short.
- `CLAUDE.md`: Claude Code reads `CLAUDE.md`; it reads `AGENTS.md` only when no `CLAUDE.md` exists. When both are generated, make `CLAUDE.md` contain `@AGENTS.md` followed by Claude-specific lines, so shared rules live in one place. Do not use symlinks (they break on Windows checkouts). Keep each under about 200 lines.
- `INSTRUCTIONS.md`: for other agents or as an attachment.
- Place them in the project root, not in the spec folder, because agents look for them there. If a file already exists, do not overwrite it; propose a merge.

Content (see `templates/agent-instructions.md`): which spec files to read and in what order; decisions to respect; how to implement a milestone; permitted Git operations; whether subagents or parallel execution are permitted; how to test; how to report; which actions need extra approval. Reference the specs; do not duplicate them.
