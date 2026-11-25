# Agent instructions: Pantry Log

## Read first
`spec/PROJECT.md`

## Rules
- Implement only what the prompt asks. No unrequested features or new dependencies.
- Use only the stack in `spec/PROJECT.md`.
- Never write secrets into files.

## Git policy
Single branch `main`. Commit once when the task is complete, message `feat: summary`. Do not create branches or worktrees. Do not push. Destructive Git operations require explicit authorization.

## Execution policy
Work sequentially as a single agent. Do not start subagents or parallel agents.

## Testing
Run `pytest`. Fix failures; never weaken or delete tests to pass. Report tests you could not run.

## Reporting
Implemented functionality · files created or modified · tests run and results · deviations · unresolved issues · next steps.
