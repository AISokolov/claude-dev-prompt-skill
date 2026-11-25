# Developer profile

The profile is the user's private, reusable preferences. It lives **outside the distributable skill** so updating or reinstalling the skill never overwrites it, and it is never committed to a project repository.

## Storage (single place to change for plugin packaging)

Resolve the profile directory in this order:

1. The directory named by the environment variable `DEV_PROMPT_HOME`, or one the user states explicitly in this conversation.
2. `<claude-config-dir>/dev-prompt/` where `<claude-config-dir>` is `$CLAUDE_CONFIG_DIR` if set, otherwise `.claude` in the user's home directory.

Check the variables with a shell command if unsure (`echo $CLAUDE_CONFIG_DIR` / `$env:CLAUDE_CONFIG_DIR`); do not guess a username or absolute path. The profile file is `<profile-dir>/profile.md`. Create the directory only when saving. Never write into the skill's own folder.

If this skill is later packaged as a plugin, replace rule 2 with the plugin's persistent data directory; nothing else in the skill depends on it.

## Lifecycle

- **No profile on first invocation:** offer an interactive profile interview once. It is optional; "skip" proceeds with project-only answers.
- **Saving a new profile:** after the profile interview, show the profile in compact form, and write the file only once the user accepts it (or edits it). Create the profile directory at that moment.
- **Profile exists:** load it silently at stage 0, summarize in at most three lines, and ask only about categories that matter to this project and are missing. Never re-ask what is stored.
- **Review / modify / reset / update:** `profile` command. Show changes before saving; reset renames the old file to `profile.md.bak`.
- **Updating from a project:** at the end of an interview offer to save newly learned preferences, each as project-only or global, with a classification the user chooses. Do not save anything the user did not agree to save.

## Interview for the profile

Adaptive, 3–5 questions per round, only categories the user wants to cover. Categories:

- **Technology:** languages, frontend, backend, databases, desktop, mobile, testing, package managers, build tools, infrastructure and deployment, operating systems and environments, external services and APIs.
- **Engineering:** architecture style, methodology, testing strategy, TDD preference, documentation detail, commenting conventions, dependency policy, Git workflow, commit conventions, deployment preferences.
- **AI development:** preferred coding agents, prompt language, prompt verbosity, resource policy (economical/balanced/comprehensive), preferred development strategy, general attitude toward subagents and parallel work.

## Classifications

Each technology is `Preferred`, `Familiar`, `Open to learning` or `Avoid`. Rules:

- Only the user assigns a classification. Past usage or approval in a project does not make something Preferred.
- Prefer Preferred technologies when they suit the requirements; never recommend an Avoid technology unless the user asks for it or no alternative exists, and then flag it explicitly.
- Attitudes about subagents or parallel execution in the profile are *context only*. They never authorize anything; each project asks again.

## File format

Use `templates/developer-profile.md`. Plain Markdown with tables so a human can edit it. Include `schema: 1` at the top; future versions must migrate by adding fields, not by discarding content. No secrets, tokens, account names, or machine-specific absolute paths.
