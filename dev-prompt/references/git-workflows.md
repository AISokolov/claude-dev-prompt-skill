# Version control strategy (stage 8)

Git workflow is configured by the user and never imposed. It is independent of the agent strategy and of worktree usage.

## Options

- **No Git:** the coding agent runs no Git commands that change anything. Reading is also unnecessary.
- **Single branch:** one branch, commits as the policy allows.
- **Main + dev:** a production branch and a development branch; no per-feature branches unless stated.
- **Feature branches:** one branch per milestone or task.
- **Custom:** user-defined; restate it precisely.
- **Worktrees:** only for explicitly approved parallel development. Not a default and never required.

## Questions (ask only what is not already known from the profile)

Branching strategy · production and development branch names · who commits and when (per milestone, per task, never) · commit message convention · who merges · who pushes and to which remote · whether worktrees are wanted. Load profile Git preferences, show them in one line, and ask whether this project overrides any.

## Permission matrix (put into the agent instruction file)

State each operation as `allowed`, `ask first`, or `forbidden`:

| Operation | Value |
|---|---|
| Create branches | per policy |
| Commit | per policy |
| Merge | per policy |
| Push | per policy |
| Initialize a repository (`git init`) | ask first, unless the user said otherwise |
| Create worktrees | forbidden unless parallel work is approved |
| Rewrite history, force push, reset --hard, delete branches, clean | always `ask first` with explicit authorization |

Branch names and commit conventions go in the same section. If the user disables Git, every row is `forbidden` except reading status when needed, and the instructions tell the agent to report changed files in its completion report instead.

## Commit points versus completion

Commit points in the policy ("after each completed task or milestone") mean "when the work passes its validation steps". They are independent of milestone status: only the user moves a milestone to `done-confirmed`, and the agent instructions must say so, so the agent never marks a milestone done merely because it committed.

## Rules for generated text

- The policy must be copied consistently into the agent instruction file and every implementation prompt that mentions Git (prefer a one-line reference to the instruction file).
- The agent must not create branches, commits, merges, pushes or worktrees beyond the approved policy.
- Destructive operations require explicit authorization each time.
- When the user delegates this decision, recommend the lightest policy that fits (usually one branch, local commits at milestone boundaries, no push) and record it as delegated.
