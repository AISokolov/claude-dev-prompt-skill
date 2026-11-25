# Testing and validation strategy

Define verification before implementation begins, sized to the project.

## Choose what applies

Unit · integration · regression · end-to-end · API · UI · visual verification · manual testing · build verification · linting and static analysis · security testing · performance testing. Pick the few that match the risks; a personal script may need only build verification and a manual check.

## TDD is configurable

`Strict TDD` · `TDD when appropriate` · `Conventional implementation and testing`. Use the user's choice or profile preference; never impose strict TDD.

## Acceptance criteria

Concrete, measurable and tied to a requirement: "Given … when … then …", a command that must pass, or a threshold ("search returns within 300 ms for 10,000 records on the reference machine"). Avoid "works well" or "is fast".

## Instructions every generated prompt gives the coding agent

- Establish suitable validation procedures and implement tests where applicable.
- Run the relevant tests and investigate and fix failures.
- Do not weaken, delete or skip tests only to make them pass.
- Report tests that could not be run, and why.
- Report unresolved issues and limitations.

## Resource policy interaction

Economical policy shortens test prose and prefers targeted test runs. It never removes security checks, validation, or acceptance criteria.
