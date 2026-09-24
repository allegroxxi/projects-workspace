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

See [Operational Standards](/standards/index.md) for advanced agentic and editing protocols.

---

## III. Error & Troubleshooting Registry

| Problem | Resolution |
| :--- | :--- |
| `edit` fails with "zero occurrences" | Use `read_file` to verify exact whitespace/indentation, then use `write_file` for large changes. |
| Agent stuck in loop | Use `list_agents` to identify and `task_stop` problematic sub-agents, then diagnose via `web_fetch`. |
| Stale content on `write_file` | Always `read_file` immediately before a recovery `write_file` to prevent overwriting concurrent changes. |


| Problem | Resolution |
| :--- | :--- |
| `edit` fails with "zero occurrences" | Use `read_file` to verify exact whitespace/indentation, then use `write_file` for large changes. |
| Agent stuck in loop | Use `list_agents` to identify and `task_stop` problematic sub-agents, then diagnose via `web_fetch`. |
| Stale content on `write_file` | Always `read_file` immediately before a recovery `write_file` to prevent overwriting concurrent changes. |
