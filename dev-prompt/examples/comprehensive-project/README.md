# Comprehensive example (excerpts): "TrailNotes"

A fictional multi-platform note-taking app for hikers: a web app, an Android app, and a small backend API with sync. Excerpts show how the package is structured.

```text
trailnotes/
├── AGENTS.md                # shared rules (Codex and compatible agents)
├── CLAUDE.md                # "@AGENTS.md" plus Claude-specific lines
└── spec/
    ├── PROJECT.md           # requirements, MoSCoW, exclusions
    ├── STACK.md             # approved technologies and rejected ones
    ├── ARCHITECTURE.md      # components, sync design, one Mermaid diagram
    ├── DESIGN.md            # UI/UX and accessibility
    ├── ROADMAP.md           # milestones M1–M6
    ├── TESTING.md
    └── prompts/
        ├── 00-launch.md
        ├── 01-api-skeleton.md
        └── final-review.md
```

Later milestone prompts (`02-…`, `03-…`) are generated with `/dev-prompt next` after the previous milestone is confirmed, so they reflect what was actually built.

## ROADMAP.md (excerpt)

| ID | Milestone | Depends on | Status |
|---|---|---|---|
| M1 | API skeleton: auth, notes CRUD, storage | none | planned |
| M2 | Web client: list, edit, offline cache | M1 | planned |
| M3 | Sync protocol and conflict handling | M1, M2 | planned |
| M4 | Android client sharing the sync client library | M3 | planned |

### M1: API skeleton
- **Objective:** a running API that creates, reads, updates and deletes notes for an authenticated user.
- **Functionality:** R1–R4, R12.
- **Boundaries:** no sync endpoints, no clients, no deployment.
- **Acceptance criteria:** all CRUD endpoints return the documented status codes; unauthenticated requests return 401; the test suite passes from a clean checkout with one command.
- **Validation:** API tests in `TESTING.md`; build and lint pass.
- **Completion:** the user confirms results or supplies the passing test output.

## 01-api-skeleton.md (excerpt)

> Implement milestone M1 only. Read `AGENTS.md`, `spec/PROJECT.md` (R1–R4, R12), `spec/STACK.md`, `spec/ARCHITECTURE.md` (sections "API" and "Storage"). Out of scope: sync, clients, deployment. Use only the approved stack. Report using the format in `AGENTS.md`. Do not start M2.

## AGENTS.md (excerpt of the execution policy)

> Work sequentially as a single agent. Do not start subagents or parallel agents. (This project's owner declined multi-agent development on the date recorded in the project's private state; if that changes, the user will update this section.)

Note: a project that *approves* parallel work would instead list exactly which tasks may run in parallel, who integrates them, and whether worktrees are allowed.
