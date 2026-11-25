# Adaptive interview guide

Contents: levels · stages · conduct rules · checkpoints · contradictions

## Complexity levels

Recommend one from the request; the user may override. Complexity is independent of the resource policy (economical/balanced/comprehensive).

| Level | When | Interview | Checkpoints | Output |
|---|---|---|---|---|
| Quick | Small, well-defined task | ≤3 task questions, see `existing-project.md` | none | One prompt |
| Standard | Medium feature or small app | Stages 1, 2, 3, 6, 8, 9, 10 in compressed form; add 4, 5 or 7 only where the project has components, a UI or a deployment that need a decision. Merge stages into shared question rounds where answers are small | One merged checkpoint (product + technical + development) that doubles as the final approval | 2–4 documents plus prompt(s) |
| Comprehensive | Greenfield app, complex architecture, several platforms | All relevant stages | Product, technical, development, then final | Full package plus roadmap |

Stage applicability follows the project's needs, not the level: a small app with a database and a UI still decides storage, architecture outline and UI basics, just briefly.

## Stages

Ask 3–5 questions per stage; fewer if the answers are already known, more if an important uncertainty remains. Skip stages that do not apply (no UI → skip 5; no deployment → shrink 7).

| # | Stage | Establish |
|---|---|---|
| 0 | Developer profile | Load saved preferences, list what is missing for *this* project; ask only that |
| 1 | Project discovery | Name, purpose, problem, users, platforms (multi-select), maturity (proof of concept / prototype / MVP / personal / production), initial scope, constraints |
| 2 | Functional requirements | Essential features, workflows, data, integrations; MoSCoW priorities; explicit out-of-scope |
| 3 | Technology selection | See `technology-selection.md` |
| 4 | System architecture | See `architecture-guidelines.md` |
| 5 | UI/UX | Style, layout, navigation, interaction, responsiveness, accessibility, platform conventions |
| 6 | Non-functional | Security, auth, privacy, performance, reliability, maintainability, scalability, error handling |
| 7 | Deployment and distribution | Hosting, installation, environments, configuration, updates |
| 8 | Version control | See `git-workflows.md` |
| 9 | Agents and resources | See `agent-strategies.md` |
| 10 | Development and testing | Milestone approach, order, tests, verification, acceptance criteria (see `milestone-planning.md`, `testing-strategies.md`) |
| 11 | Final approval | Consolidated summary of significant decisions, explicit approval |

Do not assume a cross-platform framework is best for several platforms; evaluate per-platform needs and code-sharing opportunities (see `technology-selection.md`).

## Conduct rules

- Ask only questions that change the specification. Everything answered by the profile, project state or project files (read them, read-only) is not asked again; state it in one line instead ("Using your saved preference: TypeScript, pytest").
- One stage at a time. Wait for the answers, then adapt.
- Let the user answer freely, delegate ("You decide"), skip, or go back to an earlier stage. A delegated decision is your recommendation: record it as `recommended`, source delegated, choose the simplest option that meets the requirements, and show it again at the next checkpoint. Delegation applies to decisions, never to approval requests.
- Cover the interface shape of the product as a requirement when it exists: commands and options for a CLI, endpoints for an API, main screens for a UI. Ask, or mark it "agent decides within these constraints".
- When a stage reveals test tools, linters or build tools the plan needs, treat them as stack items: propose them with the usual approval rules (see `technology-selection.md`) instead of letting them appear in the output unapproved.
- **If the user says they must stop:** immediately write everything confirmed so far, plus any partially answered stage (open points tagged `unresolved`), set the current stage to "interrupted", tell them `/dev-prompt resume` continues, and stop asking. Do not generate the package.
- Explain significant trade-offs briefly, using the decision block in `technology-selection.md`.
- Tag every item `confirmed`, `recommended`, `assumed` or `unresolved`. Show assumptions back to the user at the checkpoint.
- After each stage (or each shared question round that merges stages), write the summary and decisions to `.dev-prompt/state.md`: one edit per stage or round, not per answer, and always before moving to an approval checkpoint.
- Profile saving happens once, at the end of the interview, in one batch: list the new preferences, technologies and rejections, and ask for each whether it is project-only (default) or saved to the profile, and with which classification. This is the only moment the question is asked, including for a rejected technology ("save as Avoid?"). If the user declined a profile interview at the start, do not offer again; mention in one line that `/dev-prompt profile` can create one.

## Approval checkpoints

Comprehensive projects use three plus the final approval; Standard projects use one merged checkpoint that is also the final approval (see the level table). Before each checkpoint, resolve what is pending: every earlier `recommended` or `assumed` item must be listed in the summary the user approves.

- **Product:** purpose, platforms, users, functional requirements, scope, priorities, exclusions. After stage 2 (or 1–2 for small projects).
- **Technical:** stack, architecture, integrations, data storage, security, deployment. After stages 3–7.
- **Development:** milestones, testing, Git, agent strategy, resource policy, acceptance criteria. After stages 8–10.
- **Final:** a concise summary of every significant decision, then explicit approval before generating files.

Record each approval with the date in state.

## Contradictions and gaps

Before each checkpoint scan for: requirements that exclude each other (offline-only versus real-time sync), a chosen technology that cannot satisfy a stated platform or requirement, MUST features that exceed the stated maturity level, and decisions that conflict with the profile's Avoid list. State the conflict in two sentences, offer 2–3 resolutions, and ask. Do not silently pick one.
