Your task: audit and update my instruction files so the latest Claude models (Fable 5.1, Opus 5.5, Sonnet 5) perform at their best. Work in phases, and do not modify any file until I approve.

## Phase 1: Inventory (read-only)
- Find: ~/.claude/CLAUDE.md and, in the current project: CLAUDE.md, .claude/CLAUDE.md, CLAUDE.local.md, AGENTS.md, .claude/rules/*.md, .claude/agents/*.md, .claude/skills/*/SKILL.md, and the project's memory folder if one exists.
- Read the project's config files (package.json, pyproject, Makefile, README, CI config) to learn the real build, check, and test commands.
- If git is available, scan the last 50 commit messages for fix, revert, and hotfix. Those are mistakes that were already paid for, and each deserves a rule. Also check git status and the branches: if another session is working in the repository, don't touch its branch or its files.
- Show me what you found, with the line count and size of each file.

## Phase 2: Audit
Classify every line as keep, rewrite, move, delete, or add-what's-missing, using these principles:
1. The file is an operating manual for a model entering the project cold, not documentation. Keep what the model cannot infer from the code: commands, architectural decisions, non-obvious traps, and the reasons behind constraints. Delete what reading the code reveals and self-evident advice. For each line, ask: would the model make a mistake without it?
2. Size: keep the main file under roughly 200 lines. Folder-specific knowledge moves to .claude/rules/<name>.md with paths: frontmatter. Long recurring procedures become skills. Anything that must happen every time, without exception, should be proposed as a hook. Caveat: a path-scoped rule loads only when files on that path are opened, so anything needed for work that touches no file (direct SQL, a message, a live-site check) stays in the main file, or the main file keeps an explicit pointer saying when to read it.
3. Every rule carries its reason. For any rule without a "because", add a one-sentence reason if the context makes it clear; otherwise flag it for me. Don't invent reasons.
4. Tone: turn ALL-CAPS CRITICAL/MUST/NEVER and "don't be lazy" into plain, calm wording. Turn "try to" and "if possible" into direct instructions wherever they're attached to real requirements.
5. Remove old scaffolding: "think step by step", "plan before acting", scratchpad tags, numbered steps for work that needs judgment, "never use bullets/headers" rules, and "don't post updates while working". Thinking depth is set with the effort setting, not with prose. Keep literal steps only for fragile operations: deletes, data migrations, deploys, auth.
6. No changing numbers or lists written from memory. Turn them into a "source of truth" table: type of fact → the command or file that computes it right now. Mark drifted references "stale reference — do not trust".
7. Named mistakes: collect scattered lessons into one section, each written as: the mistake (what a model would do here) → why it happens (the mechanism, in one sentence) → the rule. Don't add a rule for a one-time stumble unless it was costly. If you find a wrong rule, fix it where it lives instead of adding another rule that warns about it.
8. Escalation: a closed list of situations where you stop and ask me: irreversible deletes, payments and billing, messages that reach real users, production data changes, secrets and auth, and changing a locked decision. Anything answerable from the code or data, you decide and document. When you do ask, ask once: one line of context, then the options with the cost of each, then your recommendation.
9. Definition of done: a verification gate for each type of work, using the real commands you found in Phase 1.
10. Conflicting sources: state the precedence explicitly, in this order: executable code, then live data, then scoped rules, then this file, then memory and old comments.
11. Settled decisions (pricing, approved copy, final architectural choices) go in one section, which states that they are not reopened without an explicit instruction from me.
12. A line of instructions is not enough for anything that must always be blocked for security reasons. Propose a hook or restricted permissions for it, and let the instructions explain why.

## Phase 3: A "How we work" section
Add a short section, or update the existing one, covering these points in your own words and in the file's language:
- Scope: deliver the full request, with no features, refactors, or abstractions nobody asked for. Anything you notice outside the task goes in as a suggestion at the end of your reply.
- When I describe a problem, ask a question, or think out loud, the deliverable is your assessment. Don't fix anything until I ask.
- Before any command that changes system state (deletes, restarts, config edits, pushes), check that the evidence supports that specific action.
- When you have enough information, act. When you're choosing between options, give a recommendation, not a survey of every option. Reversible actions within the request don't need permission.
- Before ending your turn: if your last paragraph is a plan or a promise about work you haven't done, do that work now, unless it falls under escalation. Those you mention in the report and don't carry out.
- Before reporting progress, match each claim to a tool result from this session, and say plainly what you haven't verified. If a test fails, say so and include the output.
- Write the final summary for a reader who didn't watch the work: the outcome first, in full sentences, without shorthand you invented along the way. It covers what was done, the evidence it was verified, what's left, and what was deliberately left untouched.
- Edit files surgically rather than rewriting them whole. Don't commit temporary check scripts as permanent tests.
- For fast-changing facts such as model names, libraries, and versions, check a search or the docs before relying on memory.
- If your tool supports subagents: delegate independent tasks and keep working while they run, and pick the model by how hard the task is, not how big it is. For sensitive work, a separate verifier with its own context is more reliable than self-review.

## Phase 4: Memory
If there's a memory folder: one lesson per file with a one-line summary at the top, and an index with one line per file. Merge duplicates, delete notes that are wrong or stale, and don't save what the code or git already records. Before correcting any fact in it, verify it at its source (the code, git, a live command). Then add this rule to the main file: "Every costly mistake becomes a line in the named-mistakes section, in the same change that fixed it."

## Phase 5: Delivery
1. A report with, for each finding: the file and line, the text, the principle it violates, the proposed action, and your confidence.
2. The new files or a proposed diff. Don't apply anything until I approve.
3. After I approve: back up each file before editing it, then apply. When you move content between files, move it verbatim instead of rewording it, then check with a script that every old line exists in its new location, and tell me the result.
4. For large changes: if your tool supports it, ask an independent agent with a clean context to review them, and apply the findings that hold up after you verify them.
5. At the end, give me: the line counts and sizes before and after, what moved where, and what's left for me to decide.

## Hard limits
- Don't delete any constraint with a business, security, or legal reason, or any information that exists only in these files. Delete only what the principles above justify. If nothing is worth changing, say so and change nothing.
- Never put secrets, keys, or passwords in any instruction file.
- Don't invent commands or paths. Every command you write must be one you've confirmed exists.
- Don't push or publish anything.
