# Technology selection and gap analysis

## Procedure (stage 3)

1. Start from the profile: list Preferred and Familiar technologies relevant to the project; note Avoid entries.
2. Evaluate the preferred stack against: functional requirements, target platforms, compatibility, performance, security, deployment, implementation complexity, maintainability, licensing, financial cost, developer familiarity, long-term needs.
3. If it fully satisfies the requirements, say so in one line and propose it. Do not invent a gap.
4. If it does not, run the gap analysis below for each missing capability.
5. Get approval, then record each choice as a decision (`confirmed`, source user/delegated).

## Decision block

Present every significant decision in this compact form:

> **Decision: <name>.** <one or two sentences on what must be decided and why now>
> | Option | Advantages | Disadvantages | Fit with your profile |
> **Recommended:** <option>, because <reason tied to this project's requirements>.
> **Implications:** implementation effort, maintenance, learning.
> Approve, choose another, modify, or delegate?

Offer 2–3 alternatives, not a survey. Use `AskUserQuestion` with the recommendation first, plus "You decide" if delegation is acceptable.

## Gap analysis (per missing capability)

State: which capability is missing; why the current stack cannot provide it; the recommended technology; alternatives; advantages and disadvantages; compatibility with the stack; learning requirement; maintenance implications; **required or optional**.

## Approval rules

- A new architectural technology (framework, database, language, runtime, hosting platform, message broker, auth provider, major external service) needs explicit approval or explicit delegation of that decision.
- Routine implementation dependencies (a date library, a linter plugin) may be left to the coding agent, provided they do not affect architecture, licensing, security, cost or maintainability. Say in the stack document that these are delegated and that the agent must report them.
- If the user rejects a technology, record it as rejected for this project, propose the next-best option or a reduced-scope alternative, and do not reintroduce the rejected item later in any document except a "Rejected" list. Ask whether the rejection should be saved to the profile as Avoid in the end-of-interview profile batch (see `interview-guide.md`); never do it silently.
- Test frameworks, linters, formatters and build tools are stack items. Include them in the stack proposal; if they only surface at stage 10, propose them then with the same approval rules.
- Do not recommend something because it is popular or new. The reason must come from requirements, platforms, constraints or the user's skills. Avoid overengineering.

## Multi-platform projects

Do not assume a cross-platform framework wins. Compare: (a) one cross-platform codebase, (b) native per platform with a shared core (logic, API client, data model), (c) a web app with thin shells. Weigh platform-specific requirements (OS integration, performance, store rules, offline use), team skills, and how much code can really be shared. Present the comparison as a decision block and let the user choose.

## Licensing and cost

Flag licenses that restrict the intended distribution (for example copyleft in a closed-source product) and recurring costs (paid APIs, hosting tiers). Do not assume the user has paid subscriptions or infrastructure.
