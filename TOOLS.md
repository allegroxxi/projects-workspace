---
type: documentation
scope: tooling_and_workflow
description: Reference for all available commands, scripts, and operational protocols.
---

# 🛠️ Tools & Protocols

## I. Interface Commands (Slash Commands)

| Command | Purpose | Key Parameters/Flags | Example Usage |
| :--- | :--- | :--- | :--- |
| `/dream` | Performs holistic session synthesis and context propagation. | None | `/dream` |
| `/review` | Reviews code for correctness, security, quality, and performance. | `--effort [low\|medium\|high]`, `--fix` | `/review src/file.py --effort high` |
| `/simplify` | Cleans up recent code changes for reuse and efficiency. | `--focus [target]` | `/simplify` |
| `/batch` | Executes batch operations on multiple files in parallel. | `[operation] [pattern]` | `/batch replace pattern` |
| `/loop` | Creates a recurring schedule for commands. | `[duration] [command]` | `/loop 5m check build` |
| `/qc-helper`| Provides help with Qwen Code usage and configuration. | `[question]` | `/qc-helper how to use logs?` |

## II. Agentic Protocols & Operational Best Practices

### [Correct File Editing Protocol]
**Goal**: To modify codebase files safely and reliably by avoiding brittle text-replacement errors.

**Why**: Using `edit` with large blocks of text or empty `old_string` is highly fragile and leads to "zero occurrences found" errors due to subtle whitespace or newline mismatches.

**How to apply (Decision Tree)**:

1.  **Is the change small and targeted ($<$ 10 lines)?**
    *   ✅ **YES**: Use `edit`. 
        *   *Requirement*: Include at least 3 lines of context *before* and *after* the target text to ensure uniqueness and precision.
2.  **Is the change large ($>$ 10 lines) or structural?**
    *   ✅ **YES**: Use `write_file`. Overwriting the target section or file is safer than hunting for non-existent strings.
3.  **Did an `edit` attempt fail?**
    *   ⚠️ **DO NOT REPEAT THE SAME ATTEMPT.** Follow this recovery sequence:
        1.  **Ingest Current State**: Use `read_file` to pull the absolute latest version of the file.
        2.  **Verify Content**: Check for exact whitespace, indentation, or recent changes by others.
        3.  **Attempt Incremental Fix**: Try a much smaller, more focused `edit` block.
        4.  **Fallback to Hard Reset**: If incremental edits fail, use `write_file` for the entire target section/file to ensure integrity.

---

## III. Error & Troubleshooting Registry

| Problem | Resolution |
| :--- | :--- |
| `edit` fails with "zero occurrences" | Use `read_file` to verify exact whitespace/indentation, then use `write_file` for large changes. |
| Agent stuck in loop | Use `list_agents` to identify and `task_stop` problematic sub-agents, then diagnose via `web_fetch`. |
| Stale content on `write_file` | Always `read_file` immediately before a recovery `write_file` to prevent overwriting concurrent changes. |
