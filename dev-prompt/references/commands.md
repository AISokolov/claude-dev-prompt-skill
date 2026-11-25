# Command workflows

Contents: automatic · init · profile · resume · stack · architecture · plan · generate · next · review · quick · help

## Automatic (`/dev-prompt` with no known command)

1. Look for `<project>/.dev-prompt/state.md` (project = current working directory unless the user names another). If found and not finished → offer `resume`.
2. Resolve the profile location (see `developer-profile.md`). If no profile exists and this is the first invocation of a new project (not a quick task), offer a profile interview once; the user may skip, and a skip is recorded in project state and not offered again, including at the end of the interview. For quick tasks never offer it; just use a profile if one exists.
3. If the user supplied text, classify it: new application → `init`; change to an existing codebase → existing-project flow; a clearly bounded small task → `quick`.
4. If nothing is supplied, ask one question: new app, task in an existing project, or quick prompt.
5. Recommend a complexity level (Quick / Standard / Comprehensive, see `interview-guide.md`) and let the user override it.

## init

Greenfield. Run `interview-guide.md` stages according to the chosen complexity. Create `.dev-prompt/` per `state-format.md` at the end of stage 1 (when the project has a name), not before. Continue until the final approval, then follow `generate`.

## profile

1. Load the profile or report that none exists.
2. Offer: review (show a compact summary), modify, add, reset, or run the initial interview. Show the change before saving.
3. Reset requires explicit confirmation; rename the old file to `profile.md.bak` instead of deleting it.
4. Never infer a classification. A technology becomes Preferred, Familiar, Open to learning or Avoid only because the user said so.

## resume

1. Read `.dev-prompt/state.md`. Report in a few lines: stage reached, confirmed decisions count, unresolved items, pending approvals.
2. Continue at the first unfinished stage. Do not repeat answered questions. If project files changed in ways that affect decisions, point that out first.
3. If the user wants to revisit an earlier stage, reopen it, mark dependent decisions as needing re-check, and handle conflicts as described in `SKILL.md` (decision priority).

## stack / architecture

Load the project state, then run only the relevant stage (3 or 4), following `technology-selection.md` or `architecture-guidelines.md`. Update the decision table and, if a package already exists, list which generated files need regeneration and regenerate only those after approval.

## plan

Follow `milestone-planning.md`. Update ROADMAP and milestone status in state. Changing milestones after implementation started requires showing the user what changes.

## generate

1. Check readiness: required approvals recorded? If not, say which checkpoint is missing and offer to run it.
2. Run the quality checklist inline.
3. Select the documents (see "Adaptive document set" below), fill the matching templates, write them into the spec folder.
4. Write only the agent instruction files for the selected target agents.
5. Produce the first implementation prompt (or one comprehensive prompt for small projects) and the launch prompt.
6. Verify relative links with Glob/Grep, report results.

Adaptive document set:

- **Small** (single milestone, no UI or a trivial one): `PROJECT.md` containing short Stack, Architecture outline and Testing sections, plus one prompt, plus the agent instruction file(s). Take the sections from the matching templates and omit what does not apply.
- **Medium** (a few milestones or a real UI): separate `PROJECT`, `STACK`, `ARCHITECTURE`, `TESTING`; add `DESIGN` when there is a UI and `ROADMAP` when there is more than one milestone; plus `prompts/`.
- **Large:** all separate documents.
- Never create an empty document. The Standard level's "2–4 documents" is a guide; the document set follows what the project needs. The agent file(s) and prompts are not counted.
- Templates are skeletons: drop lines that do not apply (for example Git lines when Git is disabled, roadmap references when there is no roadmap, the agent-file reference when no agent file is generated, and in that case state the rules inline in the prompt).

## next

1. Read ROADMAP and milestone status. Ask the user to confirm the previous milestone's outcome (or point to evidence such as the coding agent's completion report). Only then mark it done in state.
2. Adjust the next milestone to what was actually built, then generate its prompt with `templates/implementation-prompt.md`.
3. Do not mark the new milestone as started until the user says so.

## review

Read the supplied prompt or package. Apply `quality-checklist.md`. Report findings ordered by severity with concrete fixes; do not rewrite unless asked.

## quick

Follow `existing-project.md` ("Abbreviated flow"). Ask at most three questions, inspect relevant files read-only, produce one prompt using the implementation-prompt template, trimmed. No project state is created unless a project state already exists.

## help

Print the command table from `SKILL.md`, a three-line description of the workflow (profile → interview → approvals → package → milestone prompts), where data is stored, and the fact that the skill plans but does not implement.
