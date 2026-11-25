# Contributing

## Principles

- Keep `SKILL.md` short (a router and a few rules). Put detail in `references/`, document skeletons in `templates/`.
- Never duplicate an instruction across files; reference it.
- Never add personal preferences, usernames, machine paths, credentials or real project data. Examples must be fictional.
- No telemetry or network calls. No scripts unless they give a clear reliability gain and have a Markdown fallback.
- The skill must never authorize subagents, multi-agent work, Git operations or new technologies on its own. Changes touching those rules need a matching evaluation scenario.

## Making a change

1. Edit the skill under `dev-prompt/`.
2. Re-run the relevant scenarios from `evals/scenarios.md` and record executed versus simulated versus reviewed in `docs/evaluation.md`.
3. Check: all relative links resolve; `SKILL.md` stays under 500 lines; frontmatter description stays under 1,024 characters.

## Plugin packaging (future)

Place the `dev-prompt/` folder under a plugin's `skills/`. Change only the profile-directory rule in `references/developer-profile.md` (to the plugin's persistent data directory). Choose a plugin name that does not start with `claude-` or `anthropic-`.
