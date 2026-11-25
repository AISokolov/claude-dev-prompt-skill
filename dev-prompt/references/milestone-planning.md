# Milestone planning

## When to split

- Small application: one comprehensive implementation prompt, no roadmap file needed.
- Larger application: a roadmap of milestones, a prompt for the first milestone only, and later prompts generated with `next` against what was really built.

## Each milestone defines

Objective · required functionality (reference requirement IDs) · dependencies · implementation boundaries (what is out of scope) · expected deliverables · acceptance criteria · testing and validation · completion conditions.

## Quality of milestones

- Each produces something testable, ideally a working application or an independently verifiable component.
- Order by dependency, then risk (de-risk unknowns early), then user value.
- Walking skeleton first for multi-component apps: the thinnest end-to-end path.
- Keep scope tight enough for one focused session of the coding agent; split otherwise.
- Include no feature that is not in the confirmed requirements.

## Status handling

States: `planned` → `prompt-generated` → `in-progress` → `done-confirmed`. Generating a prompt moves a milestone only to `prompt-generated`. `in-progress` needs the user to say work started; `done-confirmed` needs the user's confirmation or evidence (tests pass, completion report reviewed). Record the evidence in state.

## Revising

When plans change, update the roadmap and state, list affected milestones, and ask before altering any milestone already `in-progress` or `done-confirmed`.
