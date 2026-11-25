# Project state

Internal working state for one project. It is separate from the generated specification documents and is private by default.

## Layout

```text
<project>/
├── .dev-prompt/
│   ├── .gitignore        # contains a single line: *   (keeps all state out of Git by default)
│   └── state.md          # everything below
└── spec/                 # generated package: shareable, may be committed (folder name is configurable)
```

- Create `.dev-prompt/` with its own `.gitignore` containing `*`. This excludes the state without editing the project's `.gitignore`. If the user wants the state committed, they delete that file; mention this once.
- If the project is not under Git, still create the file; it is harmless.
- Never put interview answers, profile data, or state into `spec/`. Spec documents contain only decisions the coding agent needs.
- `<project>` is the current working directory unless the user names another. For an empty greenfield directory this is where the project will live.

## state.md structure

Use `templates/project-state.md`. Sections:

1. **Meta:** schema, project name and slug, mode (greenfield/existing/quick), complexity level, spec folder, target agents, resource policy, profile skipped?
2. **Stage progress:** stage number, status (not started / in progress / done / skipped), one-line summary.
3. **Decisions:** ID, area, decision, status (`confirmed`/`recommended`/`assumed`/`unresolved`), source (user / delegated / profile / default), scope (project / saved to profile).
4. **Approvals:** product, technical, development, final: pending or approved with date.
5. **Execution policy:** `git` policy summary, `subagents`: not-approved | approved, `multi_agent`: not-approved | approved, with the date and user wording. Both default to `not-approved` for every new project.
6. **Milestones:** ID, name, status (`planned` / `prompt-generated` / `in-progress` / `done-confirmed`), evidence or confirmation note.
7. **Unresolved:** open questions that block or qualify the spec.
8. **Change log:** short dated lines for approved changes after the final approval.

## Status meanings

- `confirmed`: the user stated it, or approved it at a checkpoint (keep the source: user, delegated, profile or default).
- `recommended`: your proposal, including every delegated choice, until a checkpoint approves it.
- `assumed`: a gap you filled; it must be shown to the user at the next checkpoint.
- `unresolved`: open question; listed in the Unresolved section.
- Stage status may also be `interrupted`; record which questions of that stage were answered.

## Update rules

- Write once per stage; keep entries terse so resuming costs little context.
- Never store credentials, tokens, or personal data. Store technology names, not account details.
- Project decisions override the global profile for this project only.
- A change that conflicts with an `approved` decision: show the conflict, ask for confirmation, then record it in the change log and flag affected generated files.
- On resume, trust the state file over memory of the conversation, but re-read project files if they may have changed.
- A milestone moves to `done-confirmed` only on the user's confirmation or concrete evidence the user supplies (test output, completion report).
