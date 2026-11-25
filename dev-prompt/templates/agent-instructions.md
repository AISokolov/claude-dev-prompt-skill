# Agent instructions: {{Application name}}
<!-- Use for AGENTS.md (Codex and compatible agents) or INSTRUCTIONS.md. Keep it short; reference, do not repeat. -->

## Read first
1. `{{spec}}/PROJECT.md` (requirements, scope, exclusions)
2. `{{spec}}/STACK.md` (approved technologies only)
3. `{{spec}}/ARCHITECTURE.md`, `{{spec}}/TESTING.md`, `{{spec}}/ROADMAP.md` {{as present}}

## Rules
- Implement only what the current prompt asks. No unrelated changes, unrequested features, unapproved dependencies, architecture changes, or breaking changes. Do not remove existing functionality or overwrite unrelated user changes.
- Use only the approved stack. Ask before adding anything else.
- Never write credentials or secrets into files. Never run production deployments, irreversible database operations, or infrastructure changes without explicit authorization.

## Git policy
{{Exactly the approved policy. Example: "Single branch `main`. Commit after each completed milestone with the message format `type: summary`. Do not create branches or worktrees. Do not push. Destructive operations (force push, reset --hard, history rewrite, branch deletion) require explicit authorization each time."}}

## Execution policy
{{Without approval: "Work sequentially as a single agent. Do not start subagents or parallel agents."
With approval: state exactly which subagent or parallel tasks were approved by the user for this project, and nothing more.}}

## Testing
Follow `{{spec}}/TESTING.md`. Run relevant tests, fix failures, never weaken or delete tests to pass, report tests you could not run.

## Reporting (end of every task)
Implemented functionality · files created or modified · tests run and results · deviations from the specification · unresolved issues · recommended next steps. Do not continue to the next milestone unless authorized.

## Ask the user first
Anything not covered here, any deviation from the specification, any new technology, any destructive or production-impacting action.

<!-- CLAUDE.md variant, when both files are generated:
@AGENTS.md

(Claude-specific lines only, if any.)
-->
