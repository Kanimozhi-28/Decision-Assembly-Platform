# DAP: Executive Technical Briefing (CTO Level)

## 1. High-Level Vision
The **Decision Assembly Platform (DAP)** is an AI-native infrastructure layer designed to solve "decision friction" on enterprise websites. Unlike traditional chatbots or static product grids, DAP is a **passive observation and active assembly engine** that uses real-time behavioral telemetry to dynamically construct decision aids (Grids/Comparisons) via a RAG-based pipeline.

---

## 2. Core Architectural Pillars

### A. Zero-Config SDK & Behavioral Telemetry
The SDK is a lightweight (Vanilla JS) distribution that enables **event-driven observation** without slowing down the host DOM.
- **Passive Tracking:** Captures scroll depth, dwell time, navigation loops, and element hovers (CTA hesitation).
- **Rule Engine:** Evaluates behavioral patterns locally to determine the "Decision Trigger" point.
- **Dynamic Inset:** Injects a Commentary Strip and Decision Grid via a Shadow DOM to ensure zero CSS/JS conflict with the client site.

### B. Agentic Content Discovery (LangGraph)
Onboarding is fully automated through an **Agentic Scraping Pipeline**:
- **Crawl4AI + LLM:** Uses a LangGraph-orchestrated workflow to navigate homepages, identify product hierarchies, and extract CSS selectors automatically.
- **Rationale Generation:** The LLM pre-generates rationale templates for 5 distinct shopping intents during the "Discovery" phase, stored in PostgreSQL.

### C. The "Assemble" Engine (RAG Hybrid)
This is the system's "Brain," implementing a **Multi-Stage Retrieval-Augmented Generation (RAG)** pipeline:
1. **Context Extraction:** Captures the user's recent navigation history and current page semantics.
2. **Category Isolation:** Strict mapping ensuring cross-domain product "noise" is filtered out.
3. **Vector Retrieval (Qdrant):** Performs semantic search against a 384-dimensional embedding space (`all-MiniLM-L6-v2`) to find the top 4 matching products.
4. **Dynamic Mapping:** Maps the user's intent to a specific UI Block Configuration (Comparison, Shortlist, or Checklist).

---

## 3. Technology Stack

| Layer | Technology | Rationale |
| :--- | :--- | :--- |
| **Backend** | FastAPI (ASGI) | Asynchronous, non-blocking I/O for high-concurrency assembly requests. |
| **Vector Index** | Qdrant | High-performance semantic retrieval with metadata filtering (Site-level multi-tenancy). |
| **Search/LLM** | Ollama / OpenAI | Local inference for data privacy; OpenAI for high-complexity rationale generation. |
| **Embeddings** | Sentence-Transformers | Local execution of `all-MiniLM-L6-v2` to maintain sub-100ms latency. |
| **State/Config** | PostgreSQL | Robust relational storage for site configurations and telemetry logs. |
| **Agentic Logic** | LangGraph | State-machine-based scraping and discovery pipeline. |

---

## 4. Why This Wins (The CTO Perspective)

1. **Scalability (Multi-Tenancy):** The architecture supports thousands of sites with strict data isolation via Qdrant payload filters and PostgreSQL schema-level partitioning.
2. **Performance:** By using local embedding models and an ASGI backend, we target an **End-to-End latency of <200ms** for grid assembly.
3. **Intelligence without Intruision:** DAP doesn't require users to input queries. It "pulls" the answer based on "push" behavior, reducing user cognitive load.
4. **Automated Maintenance:** The discovery DAG means minimal manual maintenance as client websites update their layout; the agent simply re-crawls and re-learns.

---

## 5. Current Technical Status & Roadmap

### Current Focus
- **Grid Stability:** Hardening the RAG pipeline to prevent cross-domain leakage.
- **Process Robustness:** Managing backend worker lifecycle and port availability.

### Next Technical Milestones
- **Admin Dashboard (React/Vite):** Transitioning from script-based onboarding to a central control plane.
- **Adaptive Triggers:** Using ML to normalize trigger thresholds per-site based on historical conversion data.
- **Advanced State Persistence:** Session restoration across tab/device refreshes.

---

**Summary:** DAP is not just a widget; it is a **Real-Time Context Synthesis Layer** that bridges the gap between static content and user intent.
