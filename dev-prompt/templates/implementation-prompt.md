# {{Task title}}

## Objective
{{One or two sentences.}}

## Context
<!-- Drop references that do not exist in this project (no agent file: state the Git, execution and reporting rules inline; no Git: say so). -->
Read `{{spec}}/PROJECT.md`, `{{spec}}/STACK.md`{{, ARCHITECTURE.md, ...}}. Follow `{{AGENTS.md | CLAUDE.md}}` for Git, execution and reporting rules. {{For existing projects: facts found in the repository, with real file paths.}}

## Scope
- Implement: {{requirements by ID or list}}
- Out of scope: {{explicit exclusions; do not change unrelated code}}

## Constraints
- Mandatory: {{requirements the agent must satisfy}}
- Recommended (agent may deviate and must report why): {{}}
- Delegated to the agent: {{implementation details}}
- Dependencies: only the approved stack; ask before adding anything else.

## Acceptance criteria
- {{measurable criterion}}

## Validation
{{Commands and checks to run. Do not weaken or delete tests to pass; report tests that could not run.}}

## Deliverables
{{Files, behavior, documentation.}}

## Report back
Implemented functionality · created or modified files · tests executed and results · deviations from the specification · unresolved issues · recommended next steps. Stop after this task unless told to continue.
