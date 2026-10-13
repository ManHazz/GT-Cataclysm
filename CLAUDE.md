# CLAUDE.md

Project: GT-Cataclysm — Minecraft 1.20.1 Forge modpack (GregTech CEu Modern + L_Ender's Cataclysm). See PLAN.md for architecture.

## Orchestration
- Main model (Opus) orchestrates only. Delegate writing and editing to cheaper subagents (haiku for simple writes, sonnet for multi-file or reasoning-heavy edits).
- The user has authorized subagent use for write/edit work in this project.

## Token budget rules (whole session)

### Output
- Lead with the answer or the result. No preamble, no restating the request, no closing summary.
- Default to short. Expand only when asked or the task truly needs it.
- No apologies, hedging filler, or "great question" style openers.
- Don't explain things not asked about.
- Prose for simple answers. Lists or tables only when comparing or scanning.

### Input and context
- Don't re-read files or re-run searches already in context.
- Read only the lines needed (offset/limit), not whole files.
- Grep or glob before reading. Don't dump big outputs; filter with head, tail, or targeted queries.
- Don't paste back code or text the user already gave; reference by name or line number.

### Edits and code
- Edit in place with minimal diffs. Never rewrite a whole file for a small change.
- No unrequested refactors, comments, docstrings, or extra features.
- Don't re-read a file after editing just to verify unless something looks off.

### Tools and agents
- Batch independent tool calls in one turn.
- Skip tool calls when answerable from context.

### Thinking
- Reasoning proportional to difficulty.
- Don't revisit decisions already made unless the user raises a problem.

### Ambiguity
- If unclear and a wrong guess is cheap to redo, pick the most reasonable reading, state it in one line, and go.
- Ask one short question only when a wrong guess would be expensive.

### Format of results
- When a task is done: one or two sentences on the outcome, plus the file or answer. Nothing else.
