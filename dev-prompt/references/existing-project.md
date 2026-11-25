# Existing projects and quick prompts

Supported task kinds: feature, bug fix, refactor, UI/UX, performance, architecture change, testing, security, database change, API, deployment, code review, documentation. Do not push these through the greenfield interview.

## Abbreviated flow

1. **Understand the task** in at most three questions (goal, constraints, what must not change). Skip anything already stated. Git and agent-execution policy do not count against the three: take them from the repository's visible convention or the profile, and if still unknown ask one combined question (Git operations allowed; subagents or parallel work, default none).
2. **Inspect read-only:** README, existing `CLAUDE.md`/`AGENTS.md`, manifest and lock files, directory layout, the files touched by the task, test setup. Use Glob, Grep and Read. Do not modify anything.
3. **Record only facts you saw.** Name real files, functions and commands. If something is not found, say "not found" or ask; never invent paths, APIs or behavior.
4. **Respect existing conventions:** stack, style, test framework, Git practice. Do not recommend new technologies for a small task; if one is truly needed, run the approval flow in `technology-selection.md`.
5. **Write one prompt** from `templates/implementation-prompt.md`, trimmed to what the task needs: objective, context found, scope, out of scope, constraints, acceptance criteria, tests to run, reporting.
6. **Git and agents:** use the project's existing practice if visible, or ask once. Apply the same default as everywhere: single agent, no subagents, unless the user approves.

## Bug-fix prompts

Include: observed versus expected behavior, reproduction steps the user gave, suspected files only if evidence supports it, a regression test requirement, and an instruction to find the root cause rather than mask the symptom. If reproduction information is missing, ask for it or tell the agent to reproduce first.

## Level of ceremony

A bug fix or small feature is usually Quick: no state files, one prompt in chat or in a file the user names. Create project state only when the user continues into a multi-step effort.
