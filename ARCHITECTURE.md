# Architecture: Onion Architecture

This project implements the **Onion Architecture** pattern to ensure a high degree of decoupling between core routing logic and external technical implementations (such as LLMs, vector databases, and embedding providers).

## Core Principle: Dependency Inversion
All dependencies point **inward** toward the Domain. High-level routing policies do not depend on low-level infrastructure details. Instead, the infrastructure implements interfaces (Ports) defined by the core.

---

## Architectural Layers

### 1. Domain Model (The Core)
The most stable layer, containing pure data structures and fundamental business concepts. This layer has zero external dependencies.

* **Location:** `Context/src/context_router/models.py`
* **Contents:** 
    * `Query`: The user's input request.
    * `Document`: Representations of retrieved context chunks.
    * `RoutedContext`: The final, optimized context block.
    * `RouterError`: Domain-specific error definitions.

### 2. Application Services (Orchestration)
Defines the "Use Cases" of the system—the specific sequences of operations that constitute the context routing pipeline. It orchestrates the flow of data but does not know how the data is fetched or processed. This layer also serves as the enforcement point for the **Observation-Evaluation Protocol**.

* **Location:** `Context/src/context_router/router.py`
* **Contents:** 
    * `ContextRouter`: The primary orchestrator that manages the transition from `Query` $\rightarrow$ `Document` $\rightarrow$ `RoutedContext`.
    * **Interfaces (Ports):** Defines the abstractions (e.g., `BaseRouter`) that the Infrastructure layer must implement.

### 3. Infrastructure & Adapters (Implementation)
The outermost layer where the "dirty" work happens. This layer provides concrete implementations for the interfaces defined in the Application layer.

* **Location:** (Planned) `Context/src/context_router/infrastructure/`
* **Contents:** 
    * **Current (Mock):** A lightweight `SemanticRouter` currently resides in the Application layer for MVP/testing purposes but is slated for relocation to Infrastructure.
    * **Planned Implementations:**
        * **Semantic Router Adapter:** Implementation using Bi-Encoders (e.g., via SentenceTransformers).
        * **Reranker Adapter:** Implementation using Cross-Encoders or LLM-based scoring.
        * **Compressor Adapter:** Implementation of LLMLingua-style token pruning.
        * **External Clients:** API clients for OpenAI, Anthropic, or local model servers.

---

## Dependency Flow & Inversion

### The Golden Rule
**Dependencies always point inward.** 

The `ContextRouter` (Application) depends only on the `BaseRouter` abstraction (Interface). It does not depend on the specific implementation of how routing is performed. This allows us to swap out a mock `SemanticRouter` for a production-grade embedding-based one without changing a single line of orchestration logic.
