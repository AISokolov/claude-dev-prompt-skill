# Architecture guidelines

## Principle

Design the architecture with the user instead of leaving it to the coding agent, but only as far as the project needs. Prefer the simplest architecture that meets the confirmed requirements. A single deployable unit with clear internal module boundaries is the default.

## What to define (as relevant)

High-level structure · components and responsibilities · communication between components · data flow · data storage and schema outline · API boundaries · external integrations · authentication and authorization · synchronization · error handling · configuration management · deployment architecture · platform-specific components.

Do not constrain routine implementation details (file layout inside a module, naming, small helpers). Write "implementation detail delegated to the coding agent" instead.

## Complexity triggers

Do not introduce microservices, distributed systems, message queues, container orchestration, caches or separate services unless a stated requirement demonstrates the need (scale, isolation, independent deployment, hard latency). When recommending one, name the requirement that demands it, the simpler alternative, and what is lost by choosing the simpler one. These need explicit approval.

## Diagrams

Add a Mermaid diagram only when it clarifies something prose cannot: component relationships, data flow across more than two components, a sync or auth sequence. One or two diagrams per project is typical. Keep them small and consistent with the text.

## Recording decisions

For each significant decision record in ARCHITECTURE: the decision, the main alternative, the reason, and the consequence. Mark which are `confirmed`. Anything `recommended` or `assumed` must be resolved at the technical approval checkpoint.

## Check before approval

Every component maps to a requirement; every requirement maps to a component; no technology appears here that is absent from the approved stack; data stored is justified by a requirement; sensitive data handling matches the non-functional requirements. Cross-check each non-functional requirement against the architecture, and each kind of stored data (database, files such as uploads or photos, configuration) against backup, recovery and privacy requirements, so that "data must never be lost" does not cover the database but forget the files.
