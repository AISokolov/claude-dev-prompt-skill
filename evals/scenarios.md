# Evaluation scenarios

Evidence levels used in `docs/evaluation.md`:

- **Executed:** a subagent followed the skill in an isolated sandbox with a scripted user persona; resulting files were inspected and checked with Grep/Glob.
- **Simulated:** walked through by reasoning against the skill text without producing files.
- **Reviewed:** verified only by reading the skill/package against the requirement.

The persona is scripted: the subagent answers its own questions from the persona sheet, so *user-side interaction is simulated even in executed runs*. Executed runs also test the plain-text fallback, since subagents have no question tool.

Priority (executed first): persistence, technology approval, Git restrictions, single-agent development, interview resumption, specification consistency.

| # | Scenario | Key checks |
|---|---|---|
| 1 | First-time user, no profile | Offers profile interview; profile written only to the sandbox profile dir, never inside the skill folder |
| 2 | Returning user with saved preferences | Does not re-ask stored answers; Avoid technologies not proposed; nothing auto-promoted to Preferred |
| 3 | Small personal application | ≤3 documents, no empty docs, one prompt |
| 4 | Comprehensive greenfield application | Three checkpoints, roadmap, first milestone prompt only |
| 5 | Multi-platform application | Compares cross-platform vs native-with-shared-core; no default |
| 6 | Preferred stack fully satisfies | One-line confirmation, no invented gap |
| 7 | Preferred stack needs extra technology | Gap analysis, required/optional, explicit approval |
| 8 | User rejects recommended technology | Not in any generated doc except "rejected"; asks before saving Avoid |
| 9 | User delegates a decision | Recorded as delegated; still listed in summary |
| 10 | main/dev Git without feature branches | Policy copied exactly; no feature branches in any doc |
| 11 | User disables Git | All Git operations forbidden in generated docs |
| 12 | User rejects multi-agent | Docs say sequential, no subagents/parallel |
| 13 | User approves parallel development | Approval recorded in project state only; limited to named tasks |
| 14 | Economical resource policy | Prompts concise, reference specs, security checks kept |
| 15 | Interrupted interview and resume | Resume from state; no repeated questions |
| 16 | Existing-project feature request | Read-only inspection; real paths only; short flow |
| 17 | Simple bug-fix prompt | One prompt, regression test requirement, no state files |
| 18 | Conflicting requirements | Conflict named, options offered, no silent choice |
| 19 | Complete spec package generation | Only needed documents; consistent |
| 20 | Validation of documents and references | All relative links resolve; no placeholders; policy greps pass |
| 21 | Public distribution without personal data | No usernames, paths, emails, secrets in the repo |

## Executed run plan

| Run | Covers | Persona essentials |
|---|---|---|
| R1 | 1, 3, 6, 19, 20 | New user, no profile; accepts profile interview; small personal CLI; preferred stack suffices; Git: single branch; single agent |
| R2 | 2, 14 | Saved profile (fixture) with an Avoid entry; economical policy; checks no repeated questions |
| R3 | 7, 8, 9 | Needs a database not in stack; recommendation rejected; one decision delegated |
| R4 | 11, 12 | Git disabled; declines subagents and multi-agent |
| R5 | 10, 13 | main/dev Git, no feature branches; approves one specific parallel task pair for this project (checks scope of approval and that profile is untouched) |
| R6 | 15 | Interview stopped after stage 3, then separate resume run from state |
| R7 | 16, 17 | Existing fixture repo; bug fix prompt; feature request |
| R8 | 18, 5 | Multi-platform app with contradictory requirements |

| R9 (iteration 2) | 11, 19, 20 | Answers "You decide" to the first approval request, then approves |
| R10 (iteration 2) | 15 | Stops in the middle of the functional-requirements stage after answering two of five questions |

Results and evidence levels: see `docs/evaluation.md`. Reviewed or simulated only: 4 (full comprehensive run), 21 (verified by grep scan), skill-update-preserves-profile (reviewed: profile path is outside the skill folder).
