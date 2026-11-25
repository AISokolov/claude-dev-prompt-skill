# Software Engineering Prompt Generator (`/dev-prompt`)

A [Claude Code](https://code.claude.com) skill that turns an application idea into an implementation-ready package of Markdown specifications and prompts for AI coding agents (Claude Code, Codex, or others). It plans; it never writes the application itself.

## Features

- Adaptive interview, 3–5 questions per stage, skipping what is already known.
- Reusable **developer profile** (technology preferences, engineering habits, AI-agent habits) kept outside the skill and outside your repositories.
- Explicit approval of significant technical decisions, with alternatives and a recommendation; technology gap analysis against your preferred stack.
- MoSCoW requirements, milestone roadmap, measurable acceptance criteria, testing strategy.
- Configurable Git policy and agent strategy. Default is a single agent working sequentially; subagents and parallel work are asked about in every project and never assumed.
- Output sized to the project: from one prompt to a full spec package.
- Also supports existing projects (features, bug fixes, refactors) with a short interview and read-only inspection.

## Installation

The skill is the `dev-prompt/` folder. Copy it into a skills directory:

```powershell
# Personal (all projects), Windows PowerShell
Copy-Item -Recurse .\dev-prompt "$HOME\.claude\skills\dev-prompt"
```

```bash
# Personal (all projects), macOS/Linux
cp -r dev-prompt ~/.claude/skills/dev-prompt
```

Or copy it to `<your-project>/.claude/skills/dev-prompt` for one project. The folder is self-contained and has no scripts or dependencies. The layout is ready to drop into a plugin's `skills/` folder later.

## First-time setup

Run `/dev-prompt`. If no developer profile exists you are offered a short optional interview. Skip it and the skill works with per-project answers only; run `/dev-prompt profile` any time.

## Commands

| Command | Purpose |
|---|---|
| `/dev-prompt` | Pick the right workflow automatically |
| `/dev-prompt init` | Start a new application project |
| `/dev-prompt profile` | Create, review, update or reset your profile |
| `/dev-prompt resume` | Continue an interrupted project |
| `/dev-prompt stack` / `architecture` | Evaluate or revise stack / architecture |
| `/dev-prompt plan` | Generate or revise the roadmap |
| `/dev-prompt generate` | Write the approved specification package or a prompt |
| `/dev-prompt next` | Next milestone prompt, after you confirm the previous one |
| `/dev-prompt review` | Review a prompt or spec package |
| `/dev-prompt quick` | Concise prompt for a well-defined task |
| `/dev-prompt help` | Explain workflows |

Claude Code has no native subcommands for skills, so the skill reads the first word of its arguments.

## Developer profile management

One Markdown file you can edit by hand. Technologies are classified Preferred, Familiar, Open to learning or Avoid, and only you assign the classification: using or approving a technology never promotes it. After a project the skill asks whether new preferences are project-only or saved to the profile. Reset keeps a `profile.md.bak`.

## Project initialization and interview workflow

`/dev-prompt init` recommends a level (Quick, Standard, Comprehensive; you can override) and then runs the relevant stages: profile, discovery, functional requirements, technology, architecture, UI/UX, non-functional, deployment, version control, agents and resources, development and testing, final approval. Approval checkpoints (product, technical, development, final) are merged for small projects. You can answer freely, delegate a decision ("you decide"), skip, go back, or stop and resume later. Every item is tagged confirmed, recommended, assumed or unresolved.

## Generated deliverables

Written to `spec/` (configurable), only the files the project needs:

```text
spec/PROJECT.md  STACK.md  ARCHITECTURE.md  DESIGN.md  ROADMAP.md  TESTING.md
spec/prompts/    00-launch.md, 01-….md, final-review.md
AGENTS.md / CLAUDE.md / INSTRUCTIONS.md      (project root, only for selected agents)
```

Small projects collapse to two or three files. You also receive a short copy-ready launch prompt. See `dev-prompt/examples/`.

## Agent compatibility

The spec files are agent-neutral. Instruction files are generated only for the agents you pick. `CLAUDE.md` imports `AGENTS.md` (`@AGENTS.md`) when both exist, so shared rules live in one place. Conventions were verified against official documentation in November 2026 and may change.

## Example usage

```text
/dev-prompt init a command-line tool that tracks pantry expiry dates
/dev-prompt quick fix the off-by-one in pagination in src/list.ts
/dev-prompt resume
```

## Data storage and privacy

| Data | Location | In Git? |
|---|---|---|
| Developer profile | `$DEV_PROMPT_HOME`, else `$CLAUDE_CONFIG_DIR/dev-prompt/`, else `~/.claude/dev-prompt/` | Never (outside every repo) |
| Interview and progress state | `<project>/.dev-prompt/state.md` with its own `.gitignore` (`*`) | Excluded by default; delete that file to commit it |
| Generated spec package | `<project>/spec/` | Yours to commit |

Skill updates replace only the `dev-prompt/` skill folder; the profile and project state live elsewhere. No telemetry, no network access, no secrets stored. The skill does not spawn subagents.

## Limitations

- Interview questions use Claude Code's question tool when available (4 questions per call, 2–4 options); otherwise it falls back to plain text.
- Agent-file conventions (`AGENTS.md`, `CLAUDE.md`) change over time; verify for your agent version.
- The skill cannot guarantee that a coding agent obeys its instructions, only state them clearly.
- No scripts: link and consistency checks are done by Claude with its file tools.

## Troubleshooting

- *Profile not found:* run `/dev-prompt profile`; check `DEV_PROMPT_HOME` and `CLAUDE_CONFIG_DIR`.
- *Skill does not appear:* the folder must be named `dev-prompt` and contain `SKILL.md`; restart the session.
- *Repeated questions:* make sure `.dev-prompt/state.md` exists in the project directory you launched from.
- *Spec folder in the wrong place:* say where at project start, or move it and update the path in state.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

[MIT](LICENSE).
