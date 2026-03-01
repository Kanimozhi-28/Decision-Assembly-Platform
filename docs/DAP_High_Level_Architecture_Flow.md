# DAP High-Level Architecture Flow

This document provides a high-level overview of the technical architecture and data flows for the Decision Assembly Platform (DAP).

## 1. System Blueprint

The following diagram illustrates the core components of the DAP ecosystem and their primary interactions.

```mermaid
flowchart TB
    subgraph Browser ["End User Browser (Customer Site)"]
        SDK["DAP SDK (JS Bundle)"]
        DOM["Host Page DOM"]
        Storage[("sessionStorage<br/>(State/Intent)")]
        
        SDK <--> DOM
        SDK <--> Storage
    end

    subgraph Backend ["DAP Backend (FastAPI / Python)"]
        API["API Layer<br/>(/config, /assemble)"]
        Crawl["Crawl Service<br/>(Crawl4AI)"]
        Rag["Assemble Service<br/>(RAG Pipeline)"]
        Embed["Embedding Model<br/>(BGE-Small)"]
        
        API --> Rag
        Rag --> Embed
        Crawl --> Embed
    end

    subgraph StorageLayer ["Data Persistent Layer"]
        PG[("PostgreSQL<br/>(Config/Metadata)")]
        Qdrant[("Qdrant<br/>(Vector Store)")]
    end

    %% Interactions
    SDK -- "1. GET /config" --> API
    SDK -- "2. POST /assemble" --> API
    API <--> PG
    Rag <--> Qdrant
    Crawl -- "Crawl HTML" --> DOM
    Crawl -- "Index Chunks" --> Qdrant
```

---

## 2. End-to-End User Journey

This flow traces the path from a user landing on a customer's website to receiving a context-aware decision grid.

```mermaid
sequenceDiagram
    autonumber
    participant User
    participant SDK as DAP SDK
    participant API as Backend API
    participant RAG as Assemble Service
    participant Qdrant

    User->>SDK: Lands on Page
    SDK->>API: Fetch Config (Rules, Branding)
    
    loop Passive Observation
        User->>SDK: Browses Products / Hovers CTA
        SDK->>SDK: Detect Decision Friction
    end
    
    SDK->>User: Show "Want Help?" Strip
    User->>SDK: Click Strip & Select Intent
    
    SDK->>API: POST /assemble (Intent + Context)
    API->>RAG: Construct Query & Embed
    RAG->>Qdrant: Semantic Search (Site Scoped)
    Qdrant-->>RAG: Return Top Products
    
    RAG->>RAG: Map to Blocks & Attach Rationale
    RAG-->>SDK: JSON (Blocks + Cards)
    SDK->>User: Render Decision Grid
```

---

## 3. The "Assemble" (RAG) Architecture

A detailed look at the core RAG (Retrieval-Augmented Assembly) pipeline that powers the Decision Grid.

```mermaid
flowchart LR
    Input["Input:<br/>Intent + Context<br/>(URL, Product IDs, Title)"]
    
    subgraph Pipeline ["Assemble Pipeline"]
        direction TB
        QueryBuilder["Query Builder<br/>(Concatenates Intent + Context)"]
        Embedder["Embedding Engine<br/>(Texts -> Vectors)"]
        Searcher["Vector Search<br/>(Filter by Site ID)"]
        Mapper["Block Mapper<br/>(Intent -> Block Types)"]
        Rationalizer["Rationale Engine<br/>(Template Injection)"]
    end
    
    Output["Output:<br/>Assembled Grid JSON"]
    
    Input --> QueryBuilder
    QueryBuilder --> Embedder
    Embedder --> Searcher
    Searcher --> Mapper
    Mapper --> Rationalizer
    Rationalizer --> Output

    Searcher <--> Qdrant
    Rationalizer <--> PG[(Postgres)]
```

---

## 4. Administrative Flow (Onboarding)

How a customer website is integrated into the platform.

```mermaid
flowchart LR
    Admin["Admin Portal"] -->|"Create Site"| PG[(Postgres)]
    Admin -->|"Start Crawl"| CrawlWorker["Crawl Worker"]
    
    CrawlWorker -->|"Fetch HTML"| CustomerSite["Customer Website"]
    CustomerSite -->|"Extract Content"| CrawlWorker
    
    CrawlWorker -->|"Chunk & Embed"| Embedder["Embedding Service"]
    Embedder -->|"Upsert Vectors"| Qdrant[(Qdrant)]
    CrawlWorker -->|"Metadata"| PG
```
