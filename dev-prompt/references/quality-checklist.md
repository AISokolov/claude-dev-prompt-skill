# Quality checklist

Do this yourself with Read, Glob and Grep. Do not start subagents. Two passes: **content checks** before asking for final approval (they work on decisions in state), **mechanical checks** after the files are written (they need the real files).

## Content checks (before final approval)

- [ ] Every non-functional requirement is met by something in the architecture, and every data store (database, files, uploads) is covered by the reliability, backup and privacy requirements that mention data.
- [ ] Test tools, linters and build tools that the plan needs are in the approved stack or were approved at stage 10.
- [ ] Every number or threshold in an acceptance criterion came from the user or was shown to them as `recommended`.

- [ ] No ambiguous requirement: each MUST/SHOULD is testable or has acceptance criteria.
- [ ] No missing requirement implied by the interview; no requirement that was never confirmed.
- [ ] No contradictions between documents (platform lists, stack, milestones, Git policy, agent policy).
- [ ] No unsupported assumption: every `assumed` item is shown to the user or removed.
- [ ] No invented technical detail (versions, paths, APIs) that nobody confirmed or inspected.
- [ ] Every technology named anywhere appears in the approved stack; rejected ones appear nowhere except as "rejected".
- [ ] No unnecessary complexity or scope creep; out-of-scope list present.
- [ ] Every milestone has acceptance criteria and validation steps.
- [ ] Git instructions match the approved policy exactly everywhere; no extra branches, commits, pushes or worktrees implied.
- [ ] Subagent and parallel-agent text matches state: forbidden unless approved for this project, and if approved, limited to what was approved.
- [ ] Resource policy reflected in prompt length and content.
- [ ] No secrets, personal data, profile contents, or interview state in any generated file.
- [ ] Redundant context removed; documents reference each other instead of repeating.

## Mechanical checks (after writing the package)

If a check fails, fix the file and re-check; any detail added during writing that no earlier checkpoint showed the user must be reported to them before you call the package done.

1. List the generated files with Glob.
2. Grep each file for Markdown links and `@` imports; confirm each relative target exists.
3. Grep the whole package for the names of every rejected technology and for `TODO`, `TBD`, `{{`, and placeholder text. A rejected technology may appear only in a "Rejected" list or in the "alternative considered" column of a decision table, always marked as rejected; anywhere else it is a defect.
4. Grep for Git verbs (`commit`, `push`, `merge`, `branch`, `worktree`, `rebase`, `reset`) and compare each hit to the policy.
5. Grep for `subagent`, `parallel`, `multi-agent`, `worktree` and compare with state.
6. Confirm milestone IDs and requirement IDs referenced in prompts exist in ROADMAP and PROJECT.

## Handling findings

Fix what you can. If a significant unresolved decision remains, ask the user; do not silently invent a requirement. Report the checks you ran and what remained, in two or three lines.
