# {{Application name}}: Architecture

## Overview
{{One paragraph: shape of the system and why it is this simple (or why it needs to be complex).}}

```mermaid
{{Optional diagram, only if it clarifies. Delete this block otherwise.}}
```

## Components

| Component | Responsibility | Talks to | Requirements |
|---|---|---|---|
| {{}} | {{}} | {{}} | {{R1}} |

## Data and storage
{{What is stored, where, retention, schema outline.}}

## Integrations and APIs
{{External services, API boundaries, authentication and authorization approach.}}

## Cross-cutting
Error handling: {{}}. Configuration: {{}}. Synchronization: {{if any}}. Deployment: {{}}.

## Decisions
| Decision | Alternative considered | Reason | Consequence |
|---|---|---|---|
| {{}} | {{}} | {{}} | {{}} |

Implementation details not listed here are delegated to the coding agent within these boundaries.
