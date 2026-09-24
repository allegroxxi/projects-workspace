---
name: agent_protocols.md
description: The Optimized Agentic Orchestration Workflow (v2).
type: project
---

# 🤖 Agentic Orchestration Workflow (v2)

This protocol manages complex development cycles by balancing efficiency and rigor through specialized sub-agents and structured phases.

## 🚀 Workflow Phases

### Phase 1: Decomposition & Ownership (Planning)
*   **Goal:** CoT decomposition into a DAG of atomic sub-tasks.
*   **Mechanism:** Assign explicit **File-Level Ownership** to sub-agents to prevent write conflicts.

### Phase 2: Parallel Execution & Hybrid Relay (Execution)
*   **Mechanism:** Spawn specialized sub-agents (e.g., `Researcher`, `Coder`).
*   **Relay:** Use distilled findings via tags to minimize token overhead.

### Phase 3: Red-Teaming (Adversarial Review)
*   **Requirement:** A specialized Reviewer with a contrarian persona performs an adversarial pass.
*   **Goal:** Identify edge cases, logical vulnerabilities, and potential failure modes.

### Phase 4: Verification (Validation)
*   **Action:** Atomic application $\rightarrow$ Project-standard lint/test $\rightarrow$ Outcome reporting.
