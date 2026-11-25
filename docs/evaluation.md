# Evaluation results

Date: 2026-11-25. Skill version: first release (after one round of fixes).

## How to read the evidence labels

- **Executed:** a subagent followed the skill in an isolated sandbox (its own profile folder and project folder). Resulting files were inspected, and key properties were checked with Grep/Glob/file hashes.
- **Simulated:** reasoned through against the skill text, no files produced.
- **Reviewed:** verified by reading the skill or repository against the requirement.

Important limits that apply to every "executed" row:

1. The *user side is scripted*. Each subagent answered its own questions from a persona sheet, so the same model played both roles. This tests the skill's instructions, file outputs and policies, not how real people phrase answers.
2. Subagents have no question tool, so every run exercised the **plain-text fallback**. The interactive `AskUserQuestion` path was **not tested**.
3. Each scenario ran once. There was no baseline run without the skill and no repetition for variance.
4. Subagent token use was 70k–134k per run (about 1.14M across the eleven subagent runs, counting R6a and R6b separately). That is the cost of the simulation, not a measure of what a real session costs.

## Runs

| Run | Iteration | Covers scenarios | Result |
|---|---|---|---|
| R1 first-time user, small CLI | 1 | 1, 3, 6, 12, 19, 20 | Pass |
| R2 returning user, saved profile | 1 | 2, 6, 12, 14, 19 | Pass, one defect found (invented threshold) |
| R3 stack gap, rejected technology, delegation | 1 | 7, 8, 9, 12 | Pass |
| R4 Git disabled, single agent, two agent files | 1 | 11, 12, 19 | Pass, one ordering defect found |
| R5 main/dev Git, scoped parallel approval | 1 | 10, 13, 19 | Pass |
| R6a/R6b interrupted interview, resumed in a fresh context | 1 | 4 (partly), 15 | Pass, interruption behavior undefined in skill text |
| R7 existing project: bug fix and feature prompts | 1 | 16, 17 | Pass |
| R8 four-platform app with conflicting requirements | 1 | 4 (partly), 5, 18 | Pass |
| R9 "You decide" given to an approval request | 2 (after fixes) | 11, 19, 20 | Pass |
| R10 interruption in the middle of a stage | 2 (after fixes) | 15 | Pass, with a caveat below |

## Scenario matrix

| # | Scenario | Evidence | Outcome |
|---|---|---|---|
| 1 | First-time user without profile | Executed (R1) | Profile interview offered; `profile.md` written only to the sandbox profile folder; the skill folder still had exactly its 29 original files |
| 2 | Returning user with saved preferences | Executed (R2) | Profile file byte-identical afterwards; no repeated question was logged; no Avoid technology (PHP, MongoDB) appears in the package |
| 3 | Small personal application | Executed (R1, R9) | One combined spec, one prompt, one agent file |
| 4 | Comprehensive greenfield application | Executed in part (R6, R8) | R6 produced six spec documents, an 8-milestone roadmap and a first-milestone prompt. A full run with an ambitious prompt set was not performed |
| 5 | Multi-platform application | Executed (R8) | Cross-platform codebase, native per platform and web-wrapper options compared; recommendation tied to the one-developer constraint |
| 6 | Preferred stack fully satisfies | Executed (R2) | Profile stack proposed without an invented gap |
| 7 | Preferred stack needs extra technology | Executed (R3) | Gap analysis for scheduling and delivery; required/optional stated |
| 8 | User rejects a recommended technology | Executed (R3) | Rejected options appear only under "Rejected" in `STACK.md`; not saved to the profile |
| 9 | User delegates a technical decision | Executed (R3, R1, R8) | Recorded as delegated and shown again at the checkpoint |
| 10 | main/dev Git, no feature branches | Executed (R5) | Permission matrix exact; no feature-branch wording anywhere |
| 11 | User disables Git | Executed (R4, R9) | Every Git command forbidden in the agent file; changed files reported instead |
| 12 | User rejects multi-agent | Executed (R1, R2, R3, R4, R6, R8, R9) | All agent files contain "Do not start subagents or parallel agents"; state records not-approved |
| 13 | User approves parallel development | Executed (R5) | Approval limited to one named task pair and read-only review subagent; recorded in project state only; saved profile unchanged (hash) |
| 14 | Economical resource policy | Executed in part (R1, R2, R6) | Policy recorded and reflected in agent file wording. Effect on prompt length was **not measured** |
| 15 | Interrupted interview and resumption | Executed (R6a/R6b, R10) | Fresh context resumed at the correct stage without repeating questions; partial answers survive an interruption |
| 16 | Existing-project feature request | Executed (R7) | Real files read, nothing modified (hash comparison with the fixture), no state files created |
| 17 | Simple bug-fix prompt | Executed (R7) | Root cause pinpointed to the real line; regression-test requirement included |
| 18 | Conflicting requirements | Executed (R8) | Two planted conflicts named with options, a third found by the skill itself, none silently resolved |
| 19 | Complete specification package | Executed (R1–R6, R8, R9) | Only needed documents; no empty files |
| 20 | Validation of documents and references | Executed (script checks on all eight packages) | All `spec/...` references resolve; Git and agent-policy greps consistent with state |
| 21 | Public distribution without personal data | Executed (scan of the repository) | No usernames, emails, absolute user paths or personal files |

Reviewed only:

- Skill updates do not overwrite the profile: the profile path is outside the skill folder by construction. No actual upgrade was performed.
- Interactive questions with `AskUserQuestion` (see limit 2).
- Triggering of the skill from natural-language requests: the description optimizer was not run.
- Behavior on macOS or Linux: runs were on Windows only; the skill avoids OS-specific paths.

## Defects found in iteration 1 and what changed

| Finding | Source | Fix |
|---|---|---|
| Interruption behavior undefined; partial answers could be lost | R6a | Explicit rule: save partial answers, mark stage "interrupted", stop |
| "You decide" at an approval question had no defined meaning | R6a, R6b | Delegation applies to decisions, never approvals; ask again once |
| Delegated choices and defaults were labelled `confirmed` | R1, R2 | Delegated choices are `recommended` until a checkpoint approves them |
| Invented thresholds (a 5000 ml limit) and over-specified delegated details | R1, R2 | Every number must come from the user, a checkpoint item, or "agent decides" |
| Standard level skipped stages (architecture, UI, deployment) the project needed | R2, R3 | Stage applicability follows project needs, not level |
| Checkpoint count unclear for small projects; "2–3 documents" conflicted with templates | R1–R5 | One merged checkpoint doubling as final approval; document set follows project size |
| Mechanical checks ran before the files existed | R4, R5, R8 | Split into content checks (before approval) and mechanical checks (after writing), plus an "added while writing" report |
| A spec file was written before final approval | R4 | Explicit: nothing in the spec folder before final approval |
| Profile-skip rule contradicted the end-of-interview save offer; "save as Avoid" question timed differently in two files | R1, R3, R6b | One batch at the end; no re-offer after a skip |
| Parallel approval requested at stage 9 before the roadmap named the tasks | R5 | Concrete approval at stage 10, naming the tasks |
| "Commit after milestone" read as "milestone done" | R5 | Commit points are independent from `done-confirmed` |
| Architecture covered the database but not file data in a "never lose data" requirement | R6b | Cross-check of non-functional requirements and data stores |
| Quick tasks: three-question cap versus Git and agent questions; profile skip memory with no state file | R7 | Policy questions do not count; quick never offers a profile |
| Test and lint tools appeared without approval | R6b | Treated as stack items needing approval |

Iteration 2 (R9, R10) re-ran only the fixes for approval delegation, write ordering, post-write checks and interruption; the remaining fixes in the table above were applied after the iteration-1 runs and were not individually re-executed.

Caveat for R10: the run wrote the state file once, at the interruption, instead of also after stage 1. A literal reading of the skill would write it after each stage; the runs are single-pass scripts, so real sessions should be checked for this.

## Known limitations

- The interactive question tool, real-user phrasing and real session cost are untested.
- One run per scenario; results can vary between runs.
- Output quality was judged by file inspection and targeted checks, not by building the specified applications.
- Agent-file conventions (AGENTS.md, CLAUDE.md) were verified from official documentation in November 2026 and can change.
