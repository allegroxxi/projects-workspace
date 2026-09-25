---
name: observation-evaluation.md
description: Decoupling discovery from decision-making.
type: project
---

# 🎲 Observation-Evaluation Protocol

This protocol decouples non-deterministic environmental discovery from deterministic decision-making logic.

**Why:** To maintain a clear boundary between the non-deterministic "discovery" of the environment and the deterministic "processing," ensuring that while exploration is fluid, the system's decision-making remains testable and robust.

**How to apply (The Hand-off):**

*   **Observation (Agentic):** Agents are responsible for the non-deterministic discovery of state, codebase exploration, and real-time research. They provide the **Raw Observations** (the "What").
*   **Evaluation (Python):** All formal reasoning, semantic scoring, heuristic-based routing, and decision-making logic MUST be implemented as robust, testable Python code. This code processes observations to produce **Structured Insights** (the "So What").

## 🔄 Implementation Workflow

### Phase 1: Decomposition & Ownership (Planning)
*   **Goal:** Identify the scope of the documentation update needed.
*   **Mechanism:** Assign explicit **File-Level Ownership** to sub-agents for documentation updates to prevent conflicts.
*   **Loop Prevention:** Ensure each documentation task has clear boundaries and completion criteria.

### Phase 2: Parallel Execution & Hybrid Relay (Research)
*   **Mechanism:** Spawn specialized sub-agents (e.g., `Documentation Researcher`, `Technical Writer`).
*   **Relay:** Use distilled findings via tags to minimize token overhead.
*   **Loop Prevention:** Implement explicit timeout mechanisms and progress tracking to prevent agents from getting stuck in loops.

### Phase 3: Red-Teaming (Adversarial Review)
*   **Requirement:** A specialized Reviewer with a contrarian persona performs an adversarial pass on documentation updates.
*   **Goal:** Identify edge cases, logical vulnerabilities, and potential failure modes in the documentation.
*   **Loop Prevention:** Apply systematic review techniques to avoid confirmation bias and ensure comprehensive testing.

### Phase 4: Verification (Validation)
*   **Action:** Atomic application $\rightarrow$ Project-standard lint/test $\rightarrow$ Outcome reporting.
*   **Loop Prevention:** Implement automated testing and validation checks to prevent regression issues from being reintroduced.

## 📋 Documentation Standards

*   **Consistency:** All documentation must follow the established project conventions
*   **Completeness:** Every section should include implementation examples and best practices
*   **Clarity:** Technical concepts should be explained with practical examples
