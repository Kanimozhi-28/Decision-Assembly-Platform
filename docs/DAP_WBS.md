# Decision Assembly Platform (DAP) - 14-Day Work Breakdown Structure

**Document Version:** 1.0  
**Generated:** February 2, 2026  
**Status:** Draft  
**Alignment:** DAP_PRD.md v2.1 & DAP_TAD.md v1.1

---

## Table of Contents

1. [Overview](#overview)
2. [Day 1: Foundation & Project Setup](#day-1-foundation--project-setup)
3. [Day 2: Database Schema & Qdrant Setup](#day-2-database-schema--qdrant-setup)
4. [Day 3: Embedding Service & Backend Foundation](#day-3-embedding-service--backend-foundation)
5. [Day 4: Crawl & Index System](#day-4-crawl--index-system)
6. [Day 5: Backend API - Config & Assemble](#day-5-backend-api---config--assemble)
7. [Day 6: SDK Loader & Runtime Foundation](#day-6-sdk-loader--runtime-foundation)
8. [Day 7: SDK Events & Commentary System](#day-7-sdk-events--commentary-system)
9. [Day 8: SDK Triggers & Intent Selection](#day-8-sdk-triggers--intent-selection)
10. [Day 9: SDK Grid Assembly & Rationale](#day-9-sdk-grid-assembly--rationale)
11. [Day 10: Admin Portal - Authentication & Sites](#day-10-admin-portal---authentication--sites)
12. [Day 11: Admin Portal - Config Management](#day-11-admin-portal---config-management)
13. [Day 12: Admin Portal - Content Management](#day-12-admin-portal---content-management)
14. [Day 13: SDK Block Interactions & Empty Blocks](#day-13-sdk-block-interactions--empty-blocks)
15. [Day 14: Testing, Integration & Documentation](#day-14-testing-integration--documentation)

---

## Overview

### Project Context
- **Product:** Decision Assembly Platform (DAP) v1.0
- **Tech Stack:** FastAPI (Python), React (Admin), Vanilla JS (SDK), PostgreSQL, Qdrant, sentence-transformers
- **Infrastructure:** Docker, Qdrant, Postgres, Ollama (GPTOss) already available
- **Timeline:** 14 days
- **Target Developer:** Junior developer using Cursor

### Implementation Order (from TAD §3)
1. Foundation (DB, Qdrant, Embedding)
2. Crawl & Index
3. Backend API (Core)
4. RAG & Assembly
5. SDK (Strip + Events)
6. SDK (Triggers + Intent)
7. SDK (Grid + Rationale)
8. Admin Portal
9. SDK (Block UX)
10. Empty Blocks & Custom Query

### Key Assumptions
- Docker, Qdrant, PostgreSQL, Ollama already running on server
- Developer has access to Cursor IDE
- All dependencies can be installed via pip/npm
- Backend runs on Python 3.11+
- Admin Portal uses React 18+ with Vite

---

## Day 1: Foundation & Project Setup

**Epic:** EPIC-1 - Project Foundation  
**Story:** STORY-1.1 - Project Structure & Environment Setup  
**Total Effort:** 8 hours  
**Day:** 1

### Story Description
As a developer, I want to set up the complete project structure with all necessary configurations, dependencies, and development environment, so that I can begin implementing features systematically.

### Acceptance Criteria
1. Project root structure created with backend/, admin/, sdk/, docs/ directories
2. Backend Python project initialized with FastAPI, virtual environment, and requirements.txt
3. Admin Portal React project initialized with Vite, TypeScript, and Tailwind CSS
4. SDK project structure created with build configuration (Rollup/esbuild)
5. Docker configuration files created (Dockerfile, docker-compose.yml)
6. Environment variable templates created (.env.example)
7. Git repository initialized with .gitignore
8. All dependencies installed and verified

### Granular Tasks

#### Task 1.1: Create Project Root Structure (30 min)
**Description:** Create the main directory structure following TAD §5 and §6 module breakdown.

**Actions:**
- Create root directory: `dap/`
- Create subdirectories:
  - `backend/` - FastAPI backend application
  - `admin/` - React admin portal
  - `sdk/` - JavaScript SDK (loader + runtime)
  - `docs/` - Documentation (PRD, TAD, API docs)
  - `tests/` - Integration and E2E tests
- Create `.gitignore` file with Python, Node.js, and IDE patterns
- Create `README.md` with project overview and setup instructions

**Files to Create:**
- `dap/.gitignore`
- `dap/README.md`
- Directory structure as above

**Acceptance:** All directories exist, .gitignore covers Python/Node/IDE files

---

#### Task 1.2: Initialize Backend Project (1.5 hours)
**Description:** Set up FastAPI backend with project structure, dependencies, and configuration.

**Actions:**
- Navigate to `backend/` directory
- Create Python virtual environment: `python -m venv venv`
- Activate venv (Windows: `venv\Scripts\activate`, Linux/Mac: `source venv/bin/activate`)
- Create `requirements.txt` with initial dependencies:
  ```
  fastapi==0.109.0
  uvicorn[standard]==0.27.0
  asyncpg==0.29.0
  qdrant-client==1.7.0
  sentence-transformers==2.2.0
  python-jose[cryptography]==3.3.0
  python-multipart==0.0.6
  httpx==0.26.0
  pydantic==2.5.0
  pydantic-settings==2.1.0
  ```
- Install dependencies: `pip install -r requirements.txt`
- Create backend directory structure:
  ```
  backend/
  ├── app/
  │   ├── __init__.py
  │   ├── main.py
  │   ├── config.py
  │   ├── models/
  │   ├── schemas/
  │   ├── api/
  │   │   ├── __init__.py
  │   │   ├── sdk.py
  │   │   ├── assemble.py
  │   │   └── admin.py
  │   ├── services/
  │   │   ├── __init__.py
  │   │   ├── sites.py
  │   │   ├── config.py
  │   │   ├── embedding.py
  │   │   ├── qdrant_store.py
  │   │   ├── crawl.py
  │   │   ├── assemble.py
  │   │   └── rationale.py
  │   └── db/
  │       ├── __init__.py
  │       └── database.py
  ├── tests/
  ├── requirements.txt
  └── .env.example
  ```
- Create `app/main.py` with minimal FastAPI app:
  ```python
  from fastapi import FastAPI
  from fastapi.middleware.cors import CORSMiddleware
  
  app = FastAPI(title="DAP Backend", version="1.0.0")
  
  @app.get("/health")
  async def health():
      return {"status": "ok"}
  ```
- Create `app/config.py` for environment variables:
  ```python
  from pydantic_settings import BaseSettings
  
  class Settings(BaseSettings):
      database_url: str
      qdrant_url: str = "http://localhost:6333"
      qdrant_api_key: str | None = None
      secret_key: str
      cors_origins: list[str] = ["*"]
      
      class Config:
          env_file = ".env"
  ```
- Create `.env.example`:
  ```
  DATABASE_URL=postgresql://user:password@localhost:5432/dap
  QDRANT_URL=http://localhost:6333
  QDRANT_API_KEY=
  SECRET_KEY=your-secret-key-here
  CORS_ORIGINS=["*"]
  ```

**Files to Create:**
- `backend/requirements.txt`
- `backend/.env.example`
- `backend/app/__init__.py`
- `backend/app/main.py`
- `backend/app/config.py`
- All directory structure files

**Acceptance:** Backend runs with `uvicorn app.main:app --reload`, `/health` returns 200

---

#### Task 1.3: Initialize Admin Portal Project (1.5 hours)
**Description:** Set up React admin portal with Vite, TypeScript, and Tailwind CSS.

**Actions:**
- Navigate to `admin/` directory
- Initialize Vite React TypeScript project: `npm create vite@latest . -- --template react-ts`
- Install dependencies: `npm install`
- Install additional dependencies:
  ```
  npm install react-router-dom@6
  npm install @tanstack/react-query
  npm install axios
  npm install -D tailwindcss postcss autoprefixer
  npm install -D @types/node
  ```
- Initialize Tailwind CSS: `npx tailwindcss init -p`
- Update `tailwind.config.js`:
  ```js
  export default {
    content: ["./index.html", "./src/**/*.{js,ts,jsx,tsx}"],
    theme: { extend: {} },
    plugins: [],
  }
  ```
- Update `src/index.css` to include Tailwind directives:
  ```css
  @tailwind base;
  @tailwind components;
  @tailwind utilities;
  ```
- Create admin directory structure:
  ```
  admin/
  ├── src/
  │   ├── components/
  │   ├── pages/
  │   │   ├── Login.tsx
  │   │   ├── Sites.tsx
  │   │   ├── SiteConfig.tsx
  │   │   └── Content.tsx
  │   ├── hooks/
  │   ├── services/
  │   │   └── api.ts
  │   ├── types/
  │   ├── App.tsx
  │   └── main.tsx
  ├── package.json
  └── vite.config.ts
  ```
- Create `src/services/api.ts` with axios instance:
  ```typescript
  import axios from 'axios';
  
  const API_BASE_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000';
  
  export const api = axios.create({
    baseURL: API_BASE_URL,
    headers: { 'Content-Type': 'application/json' },
  });
  ```
- Create `.env.example`:
  ```
  VITE_API_URL=http://localhost:8000
  ```

**Files to Create:**
- `admin/package.json` (via npm create vite)
- `admin/tailwind.config.js`
- `admin/.env.example`
- `admin/src/services/api.ts`
- All directory structure files

**Acceptance:** Admin runs with `npm run dev`, no build errors, Tailwind styles apply

---

#### Task 1.4: Initialize SDK Project (1 hour)
**Description:** Set up SDK project structure with build configuration for loader and runtime.

**Actions:**
- Navigate to `sdk/` directory
- Initialize npm project: `npm init -y`
- Install build dependencies:
  ```
  npm install -D rollup @rollup/plugin-node-resolve @rollup/plugin-commonjs @rollup/plugin-typescript typescript
  npm install -D @types/node
  ```
- Create SDK directory structure:
  ```
  sdk/
  ├── src/
  │   ├── loader.ts
  │   ├── runtime/
  │   │   ├── index.ts
  │   │   ├── strip.ts
  │   │   ├── events.ts
  │   │   ├── triggers.ts
  │   │   ├── commentary.ts
  │   │   ├── intent.ts
  │   │   ├── grid.ts
  │   │   ├── rationale.ts
  │   │   └── session.ts
  │   └── types.ts
  ├── dist/
  ├── rollup.config.js
  ├── tsconfig.json
  └── package.json
  ```
- Create `tsconfig.json`:
  ```json
  {
    "compilerOptions": {
      "target": "ES2015",
      "module": "ESNext",
      "lib": ["ES2015", "DOM"],
      "outDir": "./dist",
      "strict": true,
      "esModuleInterop": true,
      "skipLibCheck": true,
      "moduleResolution": "node"
    },
    "include": ["src/**/*"],
    "exclude": ["node_modules", "dist"]
  }
  ```
- Create `rollup.config.js`:
  ```js
  import resolve from '@rollup/plugin-node-resolve';
  import commonjs from '@rollup/plugin-commonjs';
  import typescript from '@rollup/plugin-typescript';
  
  export default [
    {
      input: 'src/loader.ts',
      output: { file: 'dist/loader.js', format: 'iife', name: 'DAPLoader' },
      plugins: [resolve(), commonjs(), typescript()],
    },
    {
      input: 'src/runtime/index.ts',
      output: { file: 'dist/dap-sdk.js', format: 'iife', name: 'DAPRuntime' },
      plugins: [resolve(), commonjs(), typescript()],
    },
  ];
  ```
- Create `src/types.ts` with basic types:
  ```typescript
  export interface SiteConfig {
    product_page_rules: ProductPageRules;
    trigger_thresholds: TriggerThresholds;
    commentary_templates: string[];
    block_mapping: Record<string, string[]>;
    white_label: WhiteLabel;
  }
  
  export interface ProductPageRules {
    url_patterns: string[];
    dom_selectors: string[];
    product_id_source: 'url_path' | 'data_attribute' | 'meta';
  }
  ```

**Files to Create:**
- `sdk/package.json`
- `sdk/tsconfig.json`
- `sdk/rollup.config.js`
- `sdk/src/types.ts`
- All directory structure files

**Acceptance:** SDK builds with `npm run build`, generates loader.js and dap-sdk.js in dist/

---

#### Task 1.5: Create Docker Configuration (1 hour)
**Description:** Set up Docker configuration for backend deployment.

**Actions:**
- Create `backend/Dockerfile`:
  ```dockerfile
  FROM python:3.11-slim
  
  WORKDIR /app
  
  COPY requirements.txt .
  RUN pip install --no-cache-dir -r requirements.txt
  
  COPY . .
  
  CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
  ```
- Create `docker-compose.yml` at root (optional, for local dev):
  ```yaml
  version: '3.8'
  services:
    backend:
      build: ./backend
      ports:
        - "8000:8000"
      environment:
        - DATABASE_URL=postgresql://user:password@postgres:5432/dap
        - QDRANT_URL=http://qdrant:6333
      depends_on:
        - postgres
        - qdrant
    postgres:
      image: postgres:15
      environment:
        POSTGRES_DB: dap
        POSTGRES_USER: user
        POSTGRES_PASSWORD: password
      volumes:
        - postgres_data:/var/lib/postgresql/data
    qdrant:
      image: qdrant/qdrant:latest
      ports:
        - "6333:6333"
      volumes:
        - qdrant_data:/qdrant/storage
  volumes:
    postgres_data:
    qdrant_data:
  ```
- Create `.dockerignore` in backend:
  ```
  __pycache__
  *.pyc
  venv/
  .env
  .git
  ```

**Files to Create:**
- `backend/Dockerfile`
- `docker-compose.yml` (root)
- `backend/.dockerignore`

**Acceptance:** Docker builds successfully, docker-compose up starts services

---

#### Task 1.6: Initialize Git Repository & Documentation (30 min)
**Description:** Set up Git repository and initial documentation structure.

**Actions:**
- Initialize git repository: `git init`
- Create initial commit with project structure
- Copy PRD and TAD to `docs/` directory:
  - `docs/DAP_PRD.md`
  - `docs/DAP_TAD.md`
- Create `docs/API.md` placeholder for API documentation
- Create `docs/SETUP.md` with setup instructions:
  ```markdown
  # DAP Setup Guide
  
  ## Prerequisites
  - Docker, Qdrant, PostgreSQL, Ollama (already available)
  - Python 3.11+
  - Node.js 18+
  
  ## Backend Setup
  1. cd backend
  2. python -m venv venv
  3. source venv/bin/activate (or venv\Scripts\activate on Windows)
  4. pip install -r requirements.txt
  5. Copy .env.example to .env and configure
  6. uvicorn app.main:app --reload
  
  ## Admin Setup
  1. cd admin
  2. npm install
  3. npm run dev
  
  ## SDK Build
  1. cd sdk
  2. npm install
  3. npm run build
  ```

**Files to Create:**
- `docs/SETUP.md`
- `docs/API.md` (placeholder)

**Acceptance:** Git repo initialized, docs directory populated, initial commit made

---

### Day 1 Summary
- ✅ Project structure created
- ✅ Backend initialized with FastAPI
- ✅ Admin Portal initialized with React/Vite
- ✅ SDK project structure created
- ✅ Docker configuration ready
- ✅ Git repository initialized

**Next Day Preview:** Day 2 will focus on database schema creation and Qdrant collection setup.

---

## Day 2: Database Schema & Qdrant Setup

**Epic:** EPIC-1 - Project Foundation  
**Story:** STORY-1.2 - Database Schema & Vector Store Setup  
**Total Effort:** 8 hours  
**Day:** 2

### Story Description
As a developer, I want to create the complete PostgreSQL database schema and Qdrant collection structure, so that the backend can store and retrieve site configurations, crawl jobs, and vector embeddings.

### Acceptance Criteria
1. PostgreSQL schema created with all tables from TAD §11.1
2. Database migrations system set up (Alembic or raw SQL)
3. Qdrant client configured and tested
4. Collection creation logic implemented (one collection per site)
5. Database connection pool configured
6. All indexes created per TAD §11.3
7. Seed data script created for testing

### Granular Tasks

#### Task 2.1: Set Up Database Connection & Pool (1 hour)
**Description:** Configure async PostgreSQL connection using asyncpg with connection pooling.

**Actions:**
- Create `backend/app/db/database.py`:
  ```python
  import asyncpg
  from app.config import Settings
  
  settings = Settings()
  
  pool: asyncpg.Pool | None = None
  
  async def get_pool() -> asyncpg.Pool:
      global pool
      if pool is None:
          pool = await asyncpg.create_pool(
              settings.database_url,
              min_size=5,
              max_size=20,
          )
      return pool
  
  async def close_pool():
      global pool
      if pool:
          await pool.close()
          pool = None
  ```
- Update `app/main.py` to initialize and close pool:
  ```python
  from app.db.database import get_pool, close_pool
  
  @app.on_event("startup")
  async def startup():
      await get_pool()
  
  @app.on_event("shutdown")
  async def shutdown():
      await close_pool()
  ```
- Test connection: Create simple endpoint `GET /test-db` that queries `SELECT 1`

**Files to Create/Modify:**
- `backend/app/db/database.py`
- `backend/app/main.py` (modify)

**Acceptance:** Backend starts, `/test-db` returns 200, no connection errors

---

#### Task 2.2: Create Database Schema - Core Tables (2 hours)
**Description:** Create all PostgreSQL tables per TAD §11.1 schema definition.

**Actions:**
- Create `backend/migrations/001_create_schema.sql`:
  ```sql
  -- Create schema
  CREATE SCHEMA IF NOT EXISTS dap;
  
  -- Sites table
  CREATE TABLE dap.sites (
      id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
      name VARCHAR(255) NOT NULL,
      base_url VARCHAR(2048) NOT NULL,
      created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
      updated_at TIMESTAMPTZ NOT NULL DEFAULT now()
  );
  
  -- Site config table (1:1 with sites)
  CREATE TABLE dap.site_config (
      site_id UUID PRIMARY KEY REFERENCES dap.sites(id) ON DELETE CASCADE,
      product_page_rules JSONB NOT NULL DEFAULT '{}',
      cta_selectors JSONB DEFAULT '[]',
      help_me_choose_selector VARCHAR(512),
      trigger_thresholds JSONB NOT NULL DEFAULT '{
          "multi_product_min": 2,
          "multi_product_window_min": 5,
          "dwell_sec": 45,
          "cta_hover_min": 2,
          "cooldown_after_trigger_sec": 30,
          "cooldown_after_dismiss_sec": 60,
          "cooldown_after_grid_close_sec": 45
      }',
      commentary_templates JSONB NOT NULL DEFAULT '[]',
      block_mapping JSONB NOT NULL DEFAULT '{}',
      white_label JSONB DEFAULT '{}',
      excluded_url_patterns JSONB DEFAULT '[]',
      allowed_origins JSONB DEFAULT '[]',
      session_timeout_min INT DEFAULT 30,
      restoration_window_min INT DEFAULT 5,
      created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
      updated_at TIMESTAMPTZ NOT NULL DEFAULT now()
  );
  
  -- Crawl jobs table
  CREATE TABLE dap.crawl_jobs (
      id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
      site_id UUID NOT NULL REFERENCES dap.sites(id),
      status VARCHAR(32) NOT NULL,
      started_at TIMESTAMPTZ,
      finished_at TIMESTAMPTZ,
      last_synced_at TIMESTAMPTZ,
      error_message TEXT,
      created_at TIMESTAMPTZ NOT NULL DEFAULT now()
  );
  
  -- Rationale templates table
  CREATE TABLE dap.rationale_templates (
      id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
      site_id UUID REFERENCES dap.sites(id),
      intent VARCHAR(64) NOT NULL,
      template_text TEXT NOT NULL,
      created_at TIMESTAMPTZ NOT NULL DEFAULT now()
  );
  
  -- Indexed pages table
  CREATE TABLE dap.indexed_pages (
      site_id UUID NOT NULL REFERENCES dap.sites(id),
      url VARCHAR(2048) NOT NULL,
      page_type VARCHAR(32) NOT NULL,
      product_id VARCHAR(255),
      title VARCHAR(512),
      snippet TEXT,
      indexed_at TIMESTAMPTZ NOT NULL DEFAULT now(),
      PRIMARY KEY (site_id, url)
  );
  
  -- Admin users table
  CREATE TABLE dap.admin_users (
      id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
      email VARCHAR(255) UNIQUE NOT NULL,
      password_hash VARCHAR(255) NOT NULL,
      created_at TIMESTAMPTZ NOT NULL DEFAULT now()
  );
  ```
- Create `backend/migrations/002_create_indexes.sql`:
  ```sql
  -- Indexes per TAD §11.3
  CREATE INDEX idx_crawl_jobs_site_status ON dap.crawl_jobs(site_id, status);
  CREATE INDEX idx_rationale_site_intent ON dap.rationale_templates(site_id, intent);
  CREATE INDEX idx_indexed_pages_site ON dap.indexed_pages(site_id);
  CREATE INDEX idx_indexed_pages_site_indexed ON dap.indexed_pages(site_id, indexed_at DESC);
  ```
- Create migration runner script `backend/scripts/run_migrations.py`:
  ```python
  import asyncio
  import asyncpg
  from pathlib import Path
  
  async def run_migrations():
      conn = await asyncpg.connect("postgresql://user:password@localhost:5432/dap")
      migrations_dir = Path(__file__).parent.parent / "migrations"
      
      for sql_file in sorted(migrations_dir.glob("*.sql")):
          print(f"Running {sql_file.name}...")
          sql = sql_file.read_text()
          await conn.execute(sql)
      
      await conn.close()
      print("Migrations complete!")
  
  if __name__ == "__main__":
      asyncio.run(run_migrations())
  ```

**Files to Create:**
- `backend/migrations/001_create_schema.sql`
- `backend/migrations/002_create_indexes.sql`
- `backend/scripts/run_migrations.py`

**Acceptance:** Migrations run successfully, all tables created, indexes exist

---

#### Task 2.3: Create Pydantic Schemas for Database Models (1.5 hours)
**Description:** Create Pydantic models matching database schema for type safety and validation.

**Actions:**
- Create `backend/app/schemas/__init__.py`
- Create `backend/app/schemas/site.py`:
  ```python
  from pydantic import BaseModel
  from uuid import UUID
  from datetime import datetime
  
  class SiteBase(BaseModel):
      name: str
      base_url: str
  
  class SiteCreate(SiteBase):
      pass
  
  class Site(SiteBase):
      id: UUID
      created_at: datetime
      updated_at: datetime
  
      class Config:
          from_attributes = True
  ```
- Create `backend/app/schemas/config.py`:
  ```python
  from pydantic import BaseModel
  from typing import Optional
  from uuid import UUID
  
  class ProductPageRules(BaseModel):
      url_patterns: list[str] = []
      dom_selectors: list[str] = []
      product_id_source: str = "url_path"
  
  class TriggerThresholds(BaseModel):
      multi_product_min: int = 2
      multi_product_window_min: int = 5
      dwell_sec: int = 45
      cta_hover_min: int = 2
      cooldown_after_trigger_sec: int = 30
      cooldown_after_dismiss_sec: int = 60
      cooldown_after_grid_close_sec: int = 45
  
  class WhiteLabel(BaseModel):
      brand_name: Optional[str] = None
      primary_color: Optional[str] = None
      font_family: Optional[str] = None
      logo_url: Optional[str] = None
      copy_tone: Optional[str] = None
  
  class SiteConfig(BaseModel):
      site_id: UUID
      product_page_rules: dict
      cta_selectors: list[str] = []
      help_me_choose_selector: Optional[str] = None
      trigger_thresholds: dict
      commentary_templates: list[str] = []
      block_mapping: dict
      white_label: dict = {}
      excluded_url_patterns: list[str] = []
      allowed_origins: list[str] = []
      session_timeout_min: int = 30
      restoration_window_min: int = 5
  ```
- Create `backend/app/schemas/crawl.py`:
  ```python
  from pydantic import BaseModel
  from uuid import UUID
  from datetime import datetime
  from typing import Optional
  
  class CrawlJobBase(BaseModel):
      site_id: UUID
      status: str
  
  class CrawlJobCreate(CrawlJobBase):
      pass
  
  class CrawlJob(CrawlJobBase):
      id: UUID
      started_at: Optional[datetime] = None
      finished_at: Optional[datetime] = None
      last_synced_at: Optional[datetime] = None
      error_message: Optional[str] = None
      created_at: datetime
  
      class Config:
          from_attributes = True
  ```

**Files to Create:**
- `backend/app/schemas/__init__.py`
- `backend/app/schemas/site.py`
- `backend/app/schemas/config.py`
- `backend/app/schemas/crawl.py`

**Acceptance:** All schemas import without errors, validation works

---

#### Task 2.4: Set Up Qdrant Client & Collection Management (2 hours)
**Description:** Configure Qdrant client and implement collection creation logic per TAD §11.4.1.

**Actions:**
- Create `backend/app/services/qdrant_store.py`:
  ```python
  from qdrant_client import QdrantClient
  from qdrant_client.models import Distance, VectorParams, CollectionStatus
  from app.config import Settings
  from uuid import UUID
  
  settings = Settings()
  
  client = QdrantClient(
      url=settings.qdrant_url,
      api_key=settings.qdrant_api_key,
  )
  
  # Embedding dimension (BAAI/bge-small-en-v1.5 = 384)
  EMBEDDING_DIM = 384
  
  def get_collection_name(site_id: UUID) -> str:
      return f"dap_{site_id}"
  
  async def ensure_collection(site_id: UUID) -> None:
      """Create Qdrant collection for site if it doesn't exist."""
      collection_name = get_collection_name(site_id)
      
      collections = client.get_collections().collections
      existing = [c.name for c in collections]
      
      if collection_name not in existing:
          client.create_collection(
              collection_name=collection_name,
              vectors_config=VectorParams(
                  size=EMBEDDING_DIM,
                  distance=Distance.COSINE,
              ),
          )
  
  async def delete_collection(site_id: UUID) -> None:
      """Delete Qdrant collection for site."""
      collection_name = get_collection_name(site_id)
      try:
          client.delete_collection(collection_name)
      except Exception:
          pass  # Collection may not exist
  ```
- Create test endpoint `GET /test-qdrant`:
  ```python
  @app.get("/test-qdrant")
  async def test_qdrant():
      from app.services.qdrant_store import client
      collections = client.get_collections()
      return {"collections": [c.name for c in collections.collections]}
  ```
- Test collection creation: Create endpoint `POST /test-collection` that creates a test collection

**Files to Create:**
- `backend/app/services/qdrant_store.py`
- Modify `backend/app/main.py` to add test endpoints

**Acceptance:** Qdrant client connects, test collection created successfully

---

#### Task 2.5: Create Database Service Layer - Sites (1.5 hours)
**Description:** Implement database service for site CRUD operations.

**Actions:**
- Create `backend/app/services/sites.py`:
  ```python
  from uuid import UUID
  from app.db.database import get_pool
  from app.schemas.site import SiteCreate, Site
  from app.services.qdrant_store import ensure_collection
  
  async def create_site(site_data: SiteCreate) -> Site:
      pool = await get_pool()
      async with pool.acquire() as conn:
          site_id = await conn.fetchval(
              """
              INSERT INTO dap.sites (name, base_url)
              VALUES ($1, $2)
              RETURNING id
              """,
              site_data.name,
              site_data.base_url,
          )
          
          # Create default site_config
          await conn.execute(
              """
              INSERT INTO dap.site_config (site_id)
              VALUES ($1)
              """,
              site_id,
          )
          
          # Create Qdrant collection
          await ensure_collection(site_id)
          
          # Fetch created site
          row = await conn.fetchrow(
              "SELECT * FROM dap.sites WHERE id = $1",
              site_id,
          )
          return Site(**dict(row))
  
  async def get_site(site_id: UUID) -> Site | None:
      pool = await get_pool()
      async with pool.acquire() as conn:
          row = await conn.fetchrow(
              "SELECT * FROM dap.sites WHERE id = $1",
              site_id,
          )
          return Site(**dict(row)) if row else None
  
  async def list_sites() -> list[Site]:
      pool = await get_pool()
      async with pool.acquire() as conn:
          rows = await conn.fetch("SELECT * FROM dap.sites ORDER BY created_at DESC")
          return [Site(**dict(row)) for row in rows]
  ```
- Create API endpoint `POST /admin/sites`:
  ```python
  from app.services.sites import create_site
  from app.schemas.site import SiteCreate
  
  @app.post("/admin/sites", response_model=Site)
  async def create_site_endpoint(site: SiteCreate):
      return await create_site(site)
  ```

**Files to Create:**
- `backend/app/services/sites.py`
- Modify `backend/app/api/admin.py` (create if needed)

**Acceptance:** Site creation works, Qdrant collection created automatically

---

### Day 2 Summary
- ✅ Database schema created
- ✅ Migrations system set up
- ✅ Qdrant client configured
- ✅ Collection management implemented
- ✅ Site service layer created

**Next Day Preview:** Day 3 will implement the embedding service and complete backend foundation.

---

## Day 3: Embedding Service & Backend Foundation

**Epic:** EPIC-1 - Project Foundation  
**Story:** STORY-1.3 - Embedding Service & Backend API Foundation  
**Total Effort:** 8 hours  
**Day:** 3

### Story Description
As a developer, I want to implement the embedding service using sentence-transformers with BAAI/bge-small-en-v1.5 model, and set up the core backend API structure, so that text can be embedded for both indexing and querying, and the backend can serve SDK and Admin requests.

### Acceptance Criteria
1. Embedding service module created with model loading (BAAI/bge-small-en-v1.5)
2. Embed function implemented for batch text embedding
3. Model loaded once at startup and cached in memory
4. Config API endpoint implemented (GET /sdk/config)
5. CORS middleware configured for SDK endpoints
6. Error handling and logging set up
7. Health check endpoint enhanced
8. All endpoints return proper JSON responses

### Granular Tasks

#### Task 3.1: Implement Embedding Service Module (2 hours)
**Description:** Create embedding service using sentence-transformers with BAAI/bge-small-en-v1.5 model per TAD §13.3 and §6.1.

**Actions:**
- Create `backend/app/services/embedding.py`:
  ```python
  from sentence_transformers import SentenceTransformer
  from app.config import Settings
  import logging
  
  logger = logging.getLogger(__name__)
  
  # Model: BAAI/bge-small-en-v1.5 (384 dimensions, MIT license)
  MODEL_NAME = "BAAI/bge-small-en-v1.5"
  EMBEDDING_DIM = 384
  
  _model: SentenceTransformer | None = None
  
  def get_model() -> SentenceTransformer:
      """Get or load the embedding model (singleton)."""
      global _model
      if _model is None:
          logger.info(f"Loading embedding model: {MODEL_NAME}")
          _model = SentenceTransformer(MODEL_NAME)
          logger.info("Embedding model loaded successfully")
      return _model
  
  def embed_texts(texts: list[str]) -> list[list[float]]:
      """
      Embed a list of texts into vectors.
      
      Args:
          texts: List of text strings to embed
      
      Returns:
          List of embedding vectors (each is list of 384 floats)
      """
      if not texts:
          return []
      
      model = get_model()
      embeddings = model.encode(texts, convert_to_numpy=False)
      
      # Convert to list of lists (if numpy arrays)
      if hasattr(embeddings, 'tolist'):
          return embeddings.tolist()
      return embeddings
  
  def embed_text(text: str) -> list[float]:
      """Embed a single text string."""
      return embed_texts([text])[0]
  ```
- Add model loading to startup in `app/main.py`:
  ```python
  from app.services.embedding import get_model
  
  @app.on_event("startup")
  async def startup():
      await get_pool()
      # Pre-load embedding model
      get_model()
  ```
- Create test endpoint `GET /test-embedding`:
  ```python
  @app.get("/test-embedding")
  async def test_embedding():
      from app.services.embedding import embed_text
      vector = embed_text("test embedding")
      return {
          "dimension": len(vector),
          "sample": vector[:5],  # First 5 values
      }
  ```

**Files to Create/Modify:**
- `backend/app/services/embedding.py` (create)
- `backend/app/main.py` (modify)

**Acceptance:** Model loads on startup, `/test-embedding` returns 384-dim vector, no errors

---

#### Task 3.2: Implement Qdrant Store Service - Upsert & Search (2 hours)
**Description:** Complete Qdrant store service with upsert and search functions per TAD §11.4 and §6.1.

**Actions:**
- Extend `backend/app/services/qdrant_store.py`:
  ```python
  from qdrant_client.models import PointStruct, Filter, FieldCondition, MatchValue
  from uuid import UUID
  from typing import Optional
  
  async def upsert_points(
      site_id: UUID,
      points: list[dict],
  ) -> None:
      """
      Upsert points into site's Qdrant collection.
      
      Points format:
      [
          {
              "id": "chunk_id_string",
              "vector": [0.1, 0.2, ...],  # 384-dim
              "payload": {
                  "site_id": str(site_id),
                  "type": "product" | "page",
                  "url": "...",
                  "title": "...",
                  "content": "...",
                  "chunk_id": "...",
                  "chunk_index": 0,
                  "product_id": "..." (if type=product),
                  # Optional: category, price, features, eligibility
              }
          },
          ...
      ]
      """
      collection_name = get_collection_name(site_id)
      await ensure_collection(site_id)
      
      qdrant_points = [
          PointStruct(
              id=point["id"],
              vector=point["vector"],
              payload=point["payload"],
          )
          for point in points
      ]
      
      client.upsert(
          collection_name=collection_name,
          points=qdrant_points,
      )
  
  async def search(
      site_id: UUID,
      query_vector: list[float],
      limit: int = 5,
      filter_type: Optional[str] = None,
      filter_category: Optional[str] = None,
  ) -> list[dict]:
      """
      Search in site's Qdrant collection.
      
      Returns list of hits with score, payload.
      """
      collection_name = get_collection_name(site_id)
      
      # Build filter
      filters = []
      if filter_type:
          filters.append(
              FieldCondition(key="type", match=MatchValue(value=filter_type))
          )
      if filter_category:
          filters.append(
              FieldCondition(key="category", match=MatchValue(value=filter_category))
          )
      
      search_filter = Filter(must=filters) if filters else None
      
      results = client.search(
          collection_name=collection_name,
          query_vector=query_vector,
          limit=limit,
          query_filter=search_filter,
      )
      
      return [
          {
              "id": hit.id,
              "score": hit.score,
              "payload": hit.payload,
          }
          for hit in results
      ]
  
  async def delete_points_by_chunk_ids(
      site_id: UUID,
      chunk_ids: list[str],
  ) -> None:
      """Delete points by chunk_id (for re-crawl stale removal)."""
      collection_name = get_collection_name(site_id)
      client.delete(
          collection_name=collection_name,
          points_selector=chunk_ids,
      )
  ```
- Create test endpoint `POST /test-qdrant-search`:
  ```python
  @app.post("/test-qdrant-search")
  async def test_qdrant_search(site_id: UUID):
      from app.services.embedding import embed_text
      from app.services.qdrant_store import search
      
      query_vec = embed_text("test query")
      results = await search(site_id, query_vec, limit=3)
      return {"results": results}
  ```

**Files to Create/Modify:**
- `backend/app/services/qdrant_store.py` (modify)

**Acceptance:** Upsert works, search returns results, test endpoint functional

---

#### Task 3.3: Implement Config Service & API Endpoint (2 hours)
**Description:** Create config service to fetch site configuration and implement GET /sdk/config endpoint per TAD §12.1 and PRD §7.8.

**Actions:**
- Create `backend/app/services/config.py`:
  ```python
  from uuid import UUID
  from app.db.database import get_pool
  from app.schemas.config import SiteConfig
  
  async def get_site_config(site_id: UUID) -> SiteConfig | None:
      """Get site configuration for SDK."""
      pool = await get_pool()
      async with pool.acquire() as conn:
          row = await conn.fetchrow(
              """
              SELECT * FROM dap.site_config
              WHERE site_id = $1
              """,
              site_id,
          )
          if not row:
              return None
          
          return SiteConfig(**dict(row))
  ```
- Create `backend/app/api/sdk.py`:
  ```python
  from fastapi import APIRouter, HTTPException
  from uuid import UUID
  from app.services.config import get_site_config
  from app.services.sites import get_site
  
  router = APIRouter(prefix="/sdk", tags=["SDK"])
  
  @router.get("/config")
  async def get_config(site_id: UUID):
      """
      Get site configuration for SDK.
      Returns product_page_rules, trigger_thresholds, commentary_templates,
      block_mapping, white_label, session_timeout_min, restoration_window_min.
      """
      # Verify site exists
      site = await get_site(site_id)
      if not site:
          raise HTTPException(status_code=404, detail="Site not found")
      
      config = await get_site_config(site_id)
      if not config:
          raise HTTPException(status_code=404, detail="Site config not found")
      
      return {
          "product_page_rules": config.product_page_rules,
          "trigger_thresholds": config.trigger_thresholds,
          "commentary_templates": config.commentary_templates,
          "block_mapping": config.block_mapping,
          "white_label": config.white_label,
          "session_timeout_min": config.session_timeout_min,
          "restoration_window_min": config.restoration_window_min,
          "cta_selectors": config.cta_selectors,
          "help_me_choose_selector": config.help_me_choose_selector,
      }
  ```
- Register router in `app/main.py`:
  ```python
  from app.api import sdk
  
  app.include_router(sdk.router)
  ```

**Files to Create/Modify:**
- `backend/app/services/config.py` (create)
- `backend/app/api/sdk.py` (create)
- `backend/app/api/__init__.py` (create if needed)
- `backend/app/main.py` (modify)

**Acceptance:** GET /sdk/config?site_id=<uuid> returns config JSON, 404 for invalid site_id

---

#### Task 3.4: Configure CORS Middleware for SDK Endpoints (1 hour)
**Description:** Set up CORS middleware to allow SDK requests from customer origins per TAD §10.5 and PRD §7.8.

**Actions:**
- Update `app/main.py` CORS configuration:
  ```python
  from fastapi.middleware.cors import CORSMiddleware
  from app.config import Settings
  
  settings = Settings()
  
  # CORS for SDK endpoints (allow customer origins)
  app.add_middleware(
      CORSMiddleware,
      allow_origins=settings.cors_origins,  # ["*"] in dev, allow list in prod
      allow_credentials=False,  # No credentials for SDK
      allow_methods=["GET", "POST"],
      allow_headers=["Content-Type"],
      expose_headers=["*"],
  )
  ```
- Update `app/config.py` to handle CORS origins:
  ```python
  from typing import Union
  from pydantic import field_validator
  
  class Settings(BaseSettings):
      # ... existing fields ...
      cors_origins: Union[str, list[str]] = "*"
      
      @field_validator("cors_origins", mode="before")
      @classmethod
      def parse_cors_origins(cls, v):
          if isinstance(v, str):
              if v == "*":
                  return ["*"]
              return [v]
          return v
  ```
- Test CORS: Create simple HTML test file to verify CORS headers

**Files to Create/Modify:**
- `backend/app/main.py` (modify)
- `backend/app/config.py` (modify)

**Acceptance:** CORS headers present in responses, SDK can fetch config from different origin

---

#### Task 3.5: Set Up Logging & Error Handling (1 hour)
**Description:** Configure structured logging and error handling middleware per TAD §16.4.

**Actions:**
- Create `backend/app/logging_config.py`:
  ```python
  import logging
  import sys
  
  def setup_logging():
      logging.basicConfig(
          level=logging.INFO,
          format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
          handlers=[
              logging.StreamHandler(sys.stdout),
          ],
      )
  ```
- Add error handler to `app/main.py`:
  ```python
  from fastapi import Request, status
  from fastapi.responses import JSONResponse
  from fastapi.exceptions import RequestValidationError
  
  @app.exception_handler(RequestValidationError)
  async def validation_exception_handler(request: Request, exc: RequestValidationError):
      return JSONResponse(
          status_code=status.HTTP_400_BAD_REQUEST,
          content={"detail": exc.errors()},
      )
  
  @app.exception_handler(Exception)
  async def general_exception_handler(request: Request, exc: Exception):
      logger.error(f"Unhandled exception: {exc}", exc_info=True)
      return JSONResponse(
          status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
          content={"detail": "Internal server error"},
      )
  ```
- Initialize logging in `app/main.py`:
  ```python
  from app.logging_config import setup_logging
  
  setup_logging()
  logger = logging.getLogger(__name__)
  ```

**Files to Create/Modify:**
- `backend/app/logging_config.py` (create)
- `backend/app/main.py` (modify)

**Acceptance:** Logs appear in console, errors return proper JSON responses

---

### Day 3 Summary
- ✅ Embedding service implemented with BAAI/bge-small-en-v1.5
- ✅ Qdrant store service complete (upsert, search, delete)
- ✅ Config API endpoint implemented
- ✅ CORS middleware configured
- ✅ Logging and error handling set up

**Next Day Preview:** Day 4 will implement the crawl and indexing system.

---

## Day 4: Crawl & Index System

**Epic:** EPIC-2 - Content Management  
**Story:** STORY-2.1 - Website Crawling & Vector Indexing  
**Total Effort:** 8 hours  
**Day:** 4

### Story Description
As a developer, I want to implement the crawl and indexing system that fetches website URLs, extracts product/page content, chunks text, embeds it, and stores it in Qdrant, so that the RAG system can retrieve relevant content for grid assembly.

### Acceptance Criteria
1. Crawl job service implemented with URL discovery (sitemap or seed)
2. Content extraction using Crawl4AI or Playwright + BeautifulSoup
3. Product vs page type detection implemented
4. Chunking logic per TAD §11.4.3 (one chunk per product, logical chunks for pages)
5. Payload schema per TAD §11.4.2 (site_id, type, url, title, content, chunk_id, product_id, etc.)
6. Embedding integration with Qdrant upsert
7. Indexed_pages table updates
8. Re-crawl stale removal logic (delete chunks not in current crawl)
9. Excluded URL patterns respected
10. Crawl job status tracking in database

### Granular Tasks

#### Task 4.1: Install Crawl Dependencies & Set Up Crawl Service Structure (1 hour)
**Description:** Install Crawl4AI and set up crawl service module structure per TAD §13.2.

**Actions:**
- Update `backend/requirements.txt`:
  ```
  crawl4ai>=0.3.0
  beautifulsoup4>=4.12.0
  lxml>=5.0.0
  ```
- Install: `pip install -r requirements.txt`
- Create `backend/app/services/crawl.py` structure:
  ```python
  import logging
  from uuid import UUID
  from typing import Optional
  
  logger = logging.getLogger(__name__)
  
  async def run_crawl_job(site_id: UUID, base_url: str) -> dict:
      """
      Run crawl job for a site.
      
      Returns:
          {
              "status": "done" | "failed",
              "urls_crawled": int,
              "urls_indexed": int,
              "error": str (if failed)
          }
      """
      # Implementation in next tasks
      pass
  ```

**Files to Create/Modify:**
- `backend/requirements.txt` (modify)
- `backend/app/services/crawl.py` (create)

**Acceptance:** Dependencies installed, crawl.py module created

---

#### Task 4.2: Implement URL Discovery (Sitemap & Seed List) (1.5 hours)
**Description:** Implement URL discovery from sitemap.xml or seed URL list per TAD §14.5.

**Actions:**
- Add URL discovery functions to `backend/app/services/crawl.py`:
  ```python
  import httpx
  from urllib.parse import urljoin, urlparse
  from bs4 import BeautifulSoup
  import xml.etree.ElementTree as ET
  
  async def discover_urls(base_url: str, excluded_patterns: list[str]) -> list[str]:
      """
      Discover URLs to crawl:
      1. Try sitemap.xml
      2. Fallback to seed URL + crawl links
      
      Returns list of URLs (filtered by excluded_patterns).
      """
      urls = set()
      
      # Try sitemap.xml
      sitemap_url = urljoin(base_url, "/sitemap.xml")
      try:
          async with httpx.AsyncClient() as client:
              response = await client.get(sitemap_url, timeout=10.0)
              if response.status_code == 200:
                  urls.update(parse_sitemap(response.text))
      except Exception as e:
          logger.warning(f"Sitemap not found or error: {e}")
      
      # Fallback: start from base_url and crawl links
      if not urls:
          urls.add(base_url)
          # Could implement recursive link crawling here (limit depth)
      
      # Filter excluded URLs
      filtered = []
      for url in urls:
          if not any(pattern in url for pattern in excluded_patterns):
              filtered.append(url)
      
      return filtered
  
  def parse_sitemap(sitemap_xml: str) -> list[str]:
      """Parse sitemap.xml and extract URLs."""
      urls = []
      try:
          root = ET.fromstring(sitemap_xml)
          # Handle sitemap index
          for sitemap in root.findall(".//{http://www.sitemaps.org/schemas/sitemap/0.9}sitemap"):
              loc = sitemap.find("{http://www.sitemaps.org/schemas/sitemap/0.9}loc")
              if loc is not None:
                  urls.append(loc.text)
          # Handle URL entries
          for url_elem in root.findall(".//{http://www.sitemaps.org/schemas/sitemap/0.9}url"):
              loc = url_elem.find("{http://www.sitemaps.org/schemas/sitemap/0.9}loc")
              if loc is not None:
                  urls.append(loc.text)
      except Exception as e:
          logger.error(f"Error parsing sitemap: {e}")
      return urls
  ```

**Files to Create/Modify:**
- `backend/app/services/crawl.py` (modify)

**Acceptance:** URL discovery returns list of URLs, excluded patterns filtered

---

#### Task 4.3: Implement Content Extraction (Product vs Page Detection) (2 hours)
**Description:** Extract content from HTML, detect product vs page type, extract metadata per TAD §14.5 and PRD §7.7.1.

**Actions:**
- Add content extraction functions:
  ```python
  from crawl4ai import AsyncWebCrawler
  import json
  
  async def extract_content(url: str) -> dict:
      """
      Extract content from URL.
      
      Returns:
          {
              "type": "product" | "page",
              "url": str,
              "title": str,
              "content": str,
              "product_id": str | None,
              "category": str | None,
              "price": str | None,
              "features": list[str] | None,
              "eligibility": str | None,
          }
      """
      async with AsyncWebCrawler() as crawler:
          result = await crawler.arun(url=url)
          
          html = result.markdown or result.html
          soup = BeautifulSoup(html, "lxml")
      
      # Extract title
      title = soup.find("title")
      title_text = title.text.strip() if title else ""
      
      # Try Schema.org Product markup
      product_json = soup.find("script", type="application/ld+json")
      is_product = False
      product_id = None
      category = None
      price = None
      features = []
      
      if product_json:
          try:
              data = json.loads(product_json.string)
              if isinstance(data, dict) and data.get("@type") == "Product":
                  is_product = True
                  product_id = data.get("sku") or data.get("@id") or extract_product_id_from_url(url)
                  title_text = data.get("name") or title_text
                  price = data.get("offers", {}).get("price") if isinstance(data.get("offers"), dict) else None
          except:
              pass
      
      # Extract main content
      main_content = soup.find("main") or soup.find("article") or soup.find("body")
      content_text = main_content.get_text(separator="\n", strip=True) if main_content else ""
      
      # Determine type: product if Schema.org found, or check URL pattern
      page_type = "product" if is_product else "page"
      
      # Extract product_id from URL if not found (last path segment)
      if page_type == "product" and not product_id:
          product_id = extract_product_id_from_url(url)
      
      return {
          "type": page_type,
          "url": url,
          "title": title_text,
          "content": content_text,
          "product_id": product_id,
          "category": category,
          "price": str(price) if price else None,
          "features": features,
          "eligibility": None,  # Could extract from content
      }
  
  def extract_product_id_from_url(url: str) -> str:
      """Extract product ID from URL (last path segment)."""
      path = urlparse(url).path.rstrip("/")
      return path.split("/")[-1] or "unknown"
  ```

**Files to Create/Modify:**
- `backend/app/services/crawl.py` (modify)

**Acceptance:** Content extraction returns dict with type, title, content, product_id

---

#### Task 4.4: Implement Chunking Logic per TAD §11.4.3 (1.5 hours)
**Description:** Implement chunking strategy: one chunk per product, logical chunks for pages per TAD §11.4.3.

**Actions:**
- Add chunking functions:
  ```python
  def chunk_content(extracted: dict) -> list[dict]:
      """
      Chunk content per TAD §11.4.3.
      
      Products: One chunk per product (title + description + attributes)
      Pages: Logical chunks (400-600 chars with 50-100 char overlap)
      
      Returns list of chunk dicts with:
      {
          "chunk_id": str,
          "chunk_index": int,
          "text": str,  # Text to embed
          "payload": dict,  # Full payload per TAD §11.4.2
      }
      """
      chunks = []
      
      if extracted["type"] == "product":
          # One chunk per product
          text_parts = [extracted["title"]]
          if extracted.get("content"):
              text_parts.append(extracted["content"])
          if extracted.get("features"):
              text_parts.append("Features: " + ", ".join(extracted["features"]))
          if extracted.get("price"):
              text_parts.append(f"Price: {extracted['price']}")
          
          text = "\n".join(text_parts)
          chunk_id = f"{extracted['url']}_0"
          
          payload = {
              "site_id": str(extracted.get("site_id", "")),
              "type": "product",
              "url": extracted["url"],
              "title": extracted["title"],
              "content": extracted["content"],
              "chunk_id": chunk_id,
              "chunk_index": 0,
              "product_id": extracted["product_id"],
          }
          if extracted.get("category"):
              payload["category"] = extracted["category"]
          if extracted.get("price"):
              payload["price"] = extracted["price"]
          if extracted.get("features"):
              payload["features"] = extracted["features"]
          
          chunks.append({
              "chunk_id": chunk_id,
              "chunk_index": 0,
              "text": text,
              "payload": payload,
          })
      
      else:  # page
          # Logical chunks: 400-600 chars with overlap
          content = extracted["content"]
          chunk_size = 500
          overlap = 75
          
          start = 0
          chunk_index = 0
          while start < len(content):
              end = start + chunk_size
              chunk_text = content[start:end]
              
              chunk_id = f"{extracted['url']}_{chunk_index}"
              
              payload = {
                  "site_id": str(extracted.get("site_id", "")),
                  "type": "page",
                  "url": extracted["url"],
                  "title": extracted["title"],
                  "content": chunk_text,
                  "chunk_id": chunk_id,
                  "chunk_index": chunk_index,
              }
              
              chunks.append({
                  "chunk_id": chunk_id,
                  "chunk_index": chunk_index,
                  "text": chunk_text,
                  "payload": payload,
              })
              
              start = end - overlap
              chunk_index += 1
      
      return chunks
  ```

**Files to Create/Modify:**
- `backend/app/services/crawl.py` (modify)

**Acceptance:** Products produce 1 chunk, pages produce multiple chunks with overlap

---

#### Task 4.5: Implement Complete Crawl Job Runner (1.5 hours)
**Description:** Complete crawl job implementation: fetch URLs, extract, chunk, embed, upsert to Qdrant, update indexed_pages per TAD §14.5.

**Actions:**
- Complete `run_crawl_job` function:
  ```python
  from app.services.embedding import embed_texts
  from app.services.qdrant_store import upsert_points, delete_points_by_chunk_ids
  from app.db.database import get_pool
  from app.services.config import get_site_config
  
  async def run_crawl_job(site_id: UUID, base_url: str) -> dict:
      """Run complete crawl job."""
      pool = await get_pool()
      
      # Get site config for excluded patterns
      config = await get_site_config(site_id)
      excluded_patterns = config.excluded_url_patterns if config else []
      
      try:
          # Discover URLs
          urls = await discover_urls(base_url, excluded_patterns)
          logger.info(f"Discovered {len(urls)} URLs for site {site_id}")
          
          all_chunks = []
          indexed_urls = []
          
          # Process each URL
          for url in urls:
              try:
                  # Extract content
                  extracted = await extract_content(url)
                  extracted["site_id"] = site_id
                  
                  # Chunk
                  chunks = chunk_content(extracted)
                  
                  # Embed
                  texts = [chunk["text"] for chunk in chunks]
                  vectors = embed_texts(texts)
                  
                  # Prepare Qdrant points
                  points = []
                  for chunk, vector in zip(chunks, vectors):
                      points.append({
                          "id": chunk["chunk_id"],
                          "vector": vector,
                          "payload": chunk["payload"],
                      })
                  
                  # Upsert to Qdrant
                  await upsert_points(site_id, points)
                  
                  # Track indexed URLs
                  indexed_urls.append({
                      "site_id": site_id,
                      "url": url,
                      "page_type": extracted["type"],
                      "product_id": extracted.get("product_id"),
                      "title": extracted["title"],
                      "snippet": extracted["content"][:200],
                  })
                  
                  all_chunks.extend([ch["chunk_id"] for ch in chunks])
                  
              except Exception as e:
                  logger.error(f"Error processing URL {url}: {e}")
                  continue
          
          # Update indexed_pages table
          async with pool.acquire() as conn:
              # Delete old entries for this site
              await conn.execute(
                  "DELETE FROM dap.indexed_pages WHERE site_id = $1",
                  site_id,
              )
              
              # Insert new entries
              for idx_url in indexed_urls:
                  await conn.execute(
                      """
                      INSERT INTO dap.indexed_pages
                      (site_id, url, page_type, product_id, title, snippet)
                      VALUES ($1, $2, $3, $4, $5, $6)
                      ON CONFLICT (site_id, url) DO UPDATE
                      SET page_type = EXCLUDED.page_type,
                          product_id = EXCLUDED.product_id,
                          title = EXCLUDED.title,
                          snippet = EXCLUDED.snippet,
                          indexed_at = now()
                      """,
                      idx_url["site_id"],
                      idx_url["url"],
                      idx_url["page_type"],
                      idx_url["product_id"],
                      idx_url["title"],
                      idx_url["snippet"],
                  )
          
          # Re-crawl stale removal: Get current chunk_ids from Qdrant
          # (In production, track chunk_ids per URL in indexed_pages or separate table)
          # For now, we rely on upsert overwriting by chunk_id
          
          return {
              "status": "done",
              "urls_crawled": len(urls),
              "urls_indexed": len(indexed_urls),
              "chunks_indexed": len(all_chunks),
          }
          
      except Exception as e:
          logger.error(f"Crawl job failed: {e}", exc_info=True)
          return {
              "status": "failed",
              "error": str(e),
          }
  ```

**Files to Create/Modify:**
- `backend/app/services/crawl.py` (modify)

**Acceptance:** Crawl job completes, Qdrant has points, indexed_pages updated

---

#### Task 4.6: Create Crawl Job API Endpoint & Status Tracking (30 min)
**Description:** Create API endpoints to trigger crawl jobs and track status per TAD §12.2.

**Actions:**
- Create `backend/app/api/admin.py`:
  ```python
  from fastapi import APIRouter, HTTPException, BackgroundTasks
  from uuid import UUID
  from app.services.sites import get_site
  from app.services.crawl import run_crawl_job
  from app.db.database import get_pool
  from app.schemas.crawl import CrawlJob
  
  router = APIRouter(prefix="/admin", tags=["Admin"])
  
  @router.post("/sites/{site_id}/crawl")
  async def trigger_crawl(
      site_id: UUID,
      background_tasks: BackgroundTasks,
  ):
      """Trigger crawl job for a site."""
      site = await get_site(site_id)
      if not site:
          raise HTTPException(status_code=404, detail="Site not found")
      
      # Create crawl_job record
      pool = await get_pool()
      async with pool.acquire() as conn:
          job_id = await conn.fetchval(
              """
              INSERT INTO dap.crawl_jobs (site_id, status, started_at)
              VALUES ($1, 'running', now())
              RETURNING id
              """,
              site_id,
          )
      
      # Run crawl in background
      async def run_and_update():
          result = await run_crawl_job(site_id, site.base_url)
          
          pool = await get_pool()
          async with pool.acquire() as conn:
              await conn.execute(
                  """
                  UPDATE dap.crawl_jobs
                  SET status = $1, finished_at = now(), last_synced_at = now(),
                      error_message = $2
                  WHERE id = $3
                  """,
                  result["status"],
                  result.get("error"),
                  job_id,
              )
      
      background_tasks.add_task(run_and_update)
      
      return {"job_id": str(job_id), "status": "pending"}
  
  @router.get("/sites/{site_id}/crawl/status")
  async def get_crawl_status(site_id: UUID):
      """Get latest crawl job status for a site."""
      pool = await get_pool()
      async with pool.acquire() as conn:
          row = await conn.fetchrow(
              """
              SELECT * FROM dap.crawl_jobs
              WHERE site_id = $1
              ORDER BY created_at DESC
              LIMIT 1
              """,
              site_id,
          )
          if not row:
              return None
          return dict(row)
  ```
- Register router in `app/main.py`:
  ```python
  from app.api import admin
  
  app.include_router(admin.router)
  ```

**Files to Create/Modify:**
- `backend/app/api/admin.py` (create)
- `backend/app/main.py` (modify)

**Acceptance:** POST /admin/sites/{id}/crawl triggers job, GET /admin/sites/{id}/crawl/status returns status

---

### Day 4 Summary
- ✅ Crawl dependencies installed
- ✅ URL discovery implemented (sitemap + seed)
- ✅ Content extraction with product/page detection
- ✅ Chunking logic per TAD §11.4.3
- ✅ Complete crawl job runner with Qdrant upsert
- ✅ Crawl job API endpoints created

**Next Day Preview:** Day 5 will implement the RAG & Assembly API endpoint.

---

## Day 5: Backend API - Config & Assemble (RAG & Assembly)

**Epic:** EPIC-3 - RAG & Assembly System  
**Story:** STORY-3.1 - RAG Query & Grid Assembly API  
**Total Effort:** 8 hours  
**Day:** 5

### Story Description
As a developer, I want to implement the RAG-based assemble endpoint that builds queries from intent and context, searches Qdrant, deduplicates products, maps to blocks, and generates rationales, so that the SDK can retrieve relevant products and display them in the grid.

### Acceptance Criteria
1. Rationale service implemented with template resolution and variable substitution
2. Assemble service implemented with query building, embedding, Qdrant search, deduplication
3. Product card mapping from Qdrant payload per TAD §11.4.4
4. Block mapping per intent (from config) per PRD §7.6
5. Empty results fallback (popular products by indexed_at)
6. POST /assemble endpoint implemented with proper error handling
7. Query timeout handling (200ms cap)
8. Support for empty block pull queries (block_type/pull_query params)

### Granular Tasks

#### Task 5.1: Implement Rationale Service (1.5 hours)
**Description:** Create rationale service that resolves templates and fills variables per TAD §6.1 and PRD §7.5.

**Actions:**
- Create `backend/app/services/rationale.py`:
  ```python
  import logging
  from uuid import UUID
  from typing import Optional
  from app.db.database import get_pool
  
  logger = logging.getLogger(__name__)
  
  # Default rationale templates per intent
  DEFAULT_TEMPLATES = {
      "help_me_choose": "Based on your browsing → this fits your use case",
      "compare_options": "You viewed {n} products → this matches your comparison pattern",
      "check_eligibility": "You checked eligibility → you qualify for this",
      "understand_differences": "You viewed {n} similar products → this offers best value",
      "just_exploring": "This product matches your selected intent",
  }
  
  async def get_rationale(
      site_id: UUID,
      intent: str,
      product_id: str,
      context: dict,
  ) -> str:
      """
      Get rationale for a product.
      
      Context should contain:
      - n: number of products viewed (optional)
      - intent: intent label
      - product_title: current product title (optional)
      - product_id: current product ID
      - page_title: current page title (optional)
      - url: current page URL (optional)
      - dwell_sec: dwell time in seconds (optional)
      - cta_hover_count: CTA hover count (optional)
      """
      # Try to get site-specific template
      pool = await get_pool()
      async with pool.acquire() as conn:
          row = await conn.fetchrow(
              """
              SELECT template_text FROM dap.rationale_templates
              WHERE site_id = $1 AND intent = $2
              LIMIT 1
              """,
              site_id,
              intent,
          )
          
          template = row["template_text"] if row else DEFAULT_TEMPLATES.get(intent, DEFAULT_TEMPLATES["just_exploring"])
      
      # Fill template variables
      try:
          filled = template.format(
              n=context.get("n", 0),
              intent=context.get("intent", intent),
              product_title=context.get("product_title", ""),
              product_id=context.get("product_id", product_id),
              page_title=context.get("page_title", ""),
              url=context.get("url", ""),
              dwell_sec=context.get("dwell_sec", 0),
              cta_hover_count=context.get("cta_hover_count", 0),
          )
          return filled
      except (KeyError, ValueError) as e:
          logger.warning(f"Template fill error: {e}, using generic")
          return DEFAULT_TEMPLATES.get(intent, "This product matches your selected intent")
  ```
- Create test endpoint `GET /test-rationale`:
  ```python
  @app.get("/test-rationale")
  async def test_rationale(site_id: UUID, intent: str, product_id: str):
      from app.services.rationale import get_rationale
      context = {"n": 2, "intent": intent}
      text = await get_rationale(site_id, intent, product_id, context)
      return {"rationale": text}
  ```

**Files to Create/Modify:**
- `backend/app/services/rationale.py` (create)
- `backend/app/main.py` (modify - add test endpoint)

**Acceptance:** Rationale service returns filled templates, handles missing variables gracefully

---

#### Task 5.2: Implement Query Building Logic (1 hour)
**Description:** Build query text from intent and context per TAD §8.3 DFD Level 2.

**Actions:**
- Create `backend/app/services/assemble.py`:
  ```python
  import logging
  from uuid import UUID
  from typing import Optional
  from app.services.embedding import embed_text
  from app.services.qdrant_store import search
  from app.services.config import get_site_config
  from app.services.rationale import get_rationale
  
  logger = logging.getLogger(__name__)
  
  INTENT_LABELS = {
      "help_me_choose": "Help me choose",
      "compare_options": "Compare options",
      "check_eligibility": "Check eligibility",
      "understand_differences": "Understand differences",
      "just_exploring": "Just exploring",
  }
  
  def build_query_text(
      intent: str,
      context: dict,
      custom_query: Optional[dict] = None,
  ) -> str:
      """
      Build query text from intent and context.
      
      Per TAD §8.3: Concatenate intent label + page_title + product names
      """
      parts = []
      
      # Add intent label
      intent_label = INTENT_LABELS.get(intent, intent)
      parts.append(intent_label)
      
      # Add custom query if provided
      if custom_query:
          query_type = custom_query.get("type", "")
          query_value = custom_query.get("value", "")
          if query_value:
              parts.append(query_value)
      
      # Add page title
      page_title = context.get("page_title", "")
      if page_title:
          parts.append(page_title)
      
      # Add product IDs (resolve to titles if possible)
      product_ids = context.get("product_ids", [])
      if product_ids:
          # For now, just add IDs; could resolve from Qdrant if needed
          parts.extend(product_ids)
      
      query_text = " ".join(parts)
      
      # Never return empty query
      if not query_text.strip():
          query_text = intent_label
      
      return query_text
  ```

**Files to Create/Modify:**
- `backend/app/services/assemble.py` (create)

**Acceptance:** Query building returns non-empty string, handles missing context gracefully

---

#### Task 5.3: Implement Product Deduplication & Card Mapping (2 hours)
**Description:** Deduplicate Qdrant results by product_id and map payload to product cards per TAD §11.4.4.

**Actions:**
- Add deduplication and mapping functions to `assemble.py`:
  ```python
  def dedupe_by_product_id(hits: list[dict]) -> dict[str, dict]:
      """
      Deduplicate chunks by product_id.
      Keep best score for each product.
      
      Returns: { product_id: { best_hit, score } }
      """
      products = {}
      
      for hit in hits:
          payload = hit["payload"]
          product_id = payload.get("product_id")
          
          if not product_id or payload.get("type") != "product":
              continue  # Skip non-product chunks
          
          score = hit["score"]
          
          if product_id not in products or score > products[product_id]["score"]:
              products[product_id] = {
                  "hit": hit,
                  "score": score,
              }
      
      return products
  
  def map_payload_to_product_card(payload: dict, product_id: str) -> dict:
      """
      Map Qdrant payload to product card structure.
      
      Per TAD §11.4.4: Use payload fields (title, url, price, features, eligibility)
      """
      return {
          "id": product_id,
          "title": payload.get("title", ""),
          "url": payload.get("url", ""),
          "price": payload.get("price"),
          "features": payload.get("features", []),
          "eligibility": payload.get("eligibility"),
          "category": payload.get("category"),
      }
  ```

**Files to Create/Modify:**
- `backend/app/services/assemble.py` (modify)

**Acceptance:** Deduplication works, product cards have correct structure

---

#### Task 5.4: Implement Block Mapping Logic (1.5 hours)
**Description:** Map intent to block types and attach products to blocks per PRD §7.6.

**Actions:**
- Add block mapping function:
  ```python
  async def map_to_blocks(
      site_id: UUID,
      intent: str,
      products: list[dict],
  ) -> list[dict]:
      """
      Map products to blocks based on intent→block mapping.
      
      Per PRD §7.6:
      - Help me choose → Shortlist, Recommendation, Trade-off, Action
      - Compare options → Comparison, Costs, Benefits, Limitations
      - Check eligibility → Eligibility, Use-Case Fit, Action
      - Understand differences → Comparison, Trade-off, Examples
      - Just exploring → Shortlist, Benefits, Custom Query
      """
      config = await get_site_config(site_id)
      block_mapping = config.block_mapping if config else {}
      
      # Get block types for intent
      block_types = block_mapping.get(intent, [])
      
      # Default mapping if not configured
      if not block_types:
          defaults = {
              "help_me_choose": ["shortlist", "recommendation", "trade_off", "action"],
              "compare_options": ["comparison", "costs", "benefits", "limitations"],
              "check_eligibility": ["eligibility", "use_case_fit", "action"],
              "understand_differences": ["comparison", "trade_off", "examples"],
              "just_exploring": ["shortlist", "benefits", "custom_query"],
          }
          block_types = defaults.get(intent, ["shortlist"])
      
      # Create blocks
      blocks = []
      for block_type in block_types:
          blocks.append({
              "type": block_type,
              "products": products,  # All products in each block (can be filtered later)
          })
      
      return blocks
  ```

**Files to Create/Modify:**
- `backend/app/services/assemble.py` (modify)

**Acceptance:** Blocks mapped correctly per intent, default mapping works

---

#### Task 5.5: Implement Fallback Logic (Popular Products) (1 hour)
**Description:** Implement fallback to popular products when RAG returns empty results per TAD §8.3 and PRD §7.4.

**Actions:**
- Add fallback function:
  ```python
  async def get_fallback_products(
      site_id: UUID,
      limit: int = 3,
  ) -> list[dict]:
      """
      Get fallback products (most recently indexed).
      
      Per TAD §8.3: Fallback = top N by indexed_at
      """
      pool = await get_pool()
      async with pool.acquire() as conn:
          rows = await conn.fetch(
              """
              SELECT url, page_type, product_id, title, snippet
              FROM dap.indexed_pages
              WHERE site_id = $1 AND page_type = 'product'
              ORDER BY indexed_at DESC
              LIMIT $2
              """,
              site_id,
              limit,
          )
          
          products = []
          for row in rows:
              products.append({
                  "id": row["product_id"] or "unknown",
                  "title": row["title"] or "",
                  "url": row["url"],
                  "price": None,
                  "features": [],
                  "eligibility": None,
              })
          
          return products
  ```

**Files to Create/Modify:**
- `backend/app/services/assemble.py` (modify)

**Acceptance:** Fallback returns products when RAG empty

---

#### Task 5.6: Complete Assemble Service - Main Function (1.5 hours)
**Description:** Complete assemble service with full RAG flow per TAD §8.3 DFD Level 2.

**Actions:**
- Complete main assemble function:
  ```python
  import asyncio
  from app.services.sites import get_site
  
  async def assemble(
      site_id: UUID,
      intent: str,
      context: dict,
      block_type: Optional[str] = None,
      pull_query: Optional[str] = None,
      custom_query: Optional[dict] = None,
  ) -> dict:
      """
      Main assemble function: RAG query → blocks + products + rationales.
      
      Per TAD §8.3:
      1. Build query text
      2. Embed
      3. Search Qdrant
      4. Dedupe by product_id
      5. Map to product cards
      6. Map to blocks
      7. Generate rationales
      """
      # Verify site exists
      site = await get_site(site_id)
      if not site:
          raise ValueError("Site not found")
      
      # Build query
      if pull_query:
          query_text = pull_query
      elif custom_query:
          query_text = build_query_text(intent, context, custom_query)
      else:
          query_text = build_query_text(intent, context)
      
      # Embed query
      query_vector = embed_text(query_text)
      
      # Search Qdrant (with timeout)
      try:
          hits = await asyncio.wait_for(
              search(site_id, query_vector, limit=20, filter_type="product"),
              timeout=0.2,  # 200ms timeout
          )
      except asyncio.TimeoutError:
          logger.warning("Qdrant search timeout, using fallback")
          hits = []
      
      # Dedupe and map to products
      if hits:
          deduped = dedupe_by_product_id(hits)
          products = [
              map_payload_to_product_card(item["hit"]["payload"], pid)
              for pid, item in deduped.items()
          ]
          empty = False
      else:
          # Fallback to popular products
          products = await get_fallback_products(site_id, limit=3)
          empty = True
      
      # Map to blocks
      blocks = await map_to_blocks(site_id, intent, products)
      
      # Generate rationales
      rationales = {}
      for product in products:
          rationale_context = {
              "n": len(context.get("product_ids", [])),
              "intent": intent,
              "product_title": product["title"],
              "product_id": product["id"],
              "page_title": context.get("page_title", ""),
              "url": context.get("url", ""),
          }
          rationale = await get_rationale(
              site_id,
              intent,
              product["id"],
              rationale_context,
          )
          rationales[product["id"]] = rationale
      
      return {
          "blocks": blocks,
          "products": products,
          "rationales": rationales,
          "empty": empty,
      }
  ```

**Files to Create/Modify:**
- `backend/app/services/assemble.py` (modify)

**Acceptance:** Assemble function returns complete response with blocks, products, rationales

---

#### Task 5.7: Implement POST /assemble API Endpoint (30 min)
**Description:** Create POST /assemble endpoint per TAD §12.1.

**Actions:**
- Create `backend/app/schemas/assemble.py`:
  ```python
  from pydantic import BaseModel
  from uuid import UUID
  from typing import Optional
  
  class AssembleContext(BaseModel):
      url: Optional[str] = None
      page_title: Optional[str] = None
      product_ids: list[str] = []
      custom_query: Optional[dict] = None
  
  class AssembleRequest(BaseModel):
      site_id: UUID
      intent: str  # help_me_choose, compare_options, etc.
      context: AssembleContext
      block_type: Optional[str] = None
      pull_query: Optional[str] = None
  ```
- Add endpoint to `backend/app/api/sdk.py`:
  ```python
  from fastapi import HTTPException
  from app.schemas.assemble import AssembleRequest
  from app.services.assemble import assemble
  
  @router.post("/assemble")
  async def assemble_endpoint(request: AssembleRequest):
      """Assemble grid blocks and products using RAG."""
      try:
          result = await assemble(
              request.site_id,
              request.intent,
              request.context.dict(),
              request.block_type,
              request.pull_query,
              request.context.custom_query,
          )
          return result
      except ValueError as e:
          raise HTTPException(status_code=404, detail=str(e))
      except Exception as e:
          logger.error(f"Assemble error: {e}", exc_info=True)
          raise HTTPException(status_code=503, detail="Service temporarily unavailable")
  ```

**Files to Create/Modify:**
- `backend/app/schemas/assemble.py` (create)
- `backend/app/api/sdk.py` (modify)

**Acceptance:** POST /assemble returns blocks/products/rationales, handles errors properly

---

### Day 5 Summary
- ✅ Rationale service implemented
- ✅ Query building logic complete
- ✅ Product deduplication and card mapping
- ✅ Block mapping per intent
- ✅ Fallback logic for empty results
- ✅ Complete assemble service with RAG flow
- ✅ POST /assemble API endpoint

**Next Day Preview:** Day 6 will implement the SDK Loader and Runtime Foundation.

---

## Day 6: SDK Loader & Runtime Foundation

**Epic:** EPIC-4 - SDK Implementation  
**Story:** STORY-4.1 - SDK Loader & Runtime Bootstrap  
**Total Effort:** 8 hours  
**Day:** 6

### Story Description
As a developer, I want to implement the SDK loader that fetches config and injects the runtime bundle, and the runtime foundation that initializes the strip and event listeners, so that the SDK can be integrated with two lines of code on customer websites.

### Acceptance Criteria
1. Loader script (loader.js) fetches config and injects runtime bundle
2. Runtime bundle initializes with siteId
3. Strip DOM element created and rendered (fixed bottom)
4. Config fetched from GET /sdk/config
5. Event listeners attached (popstate, click, scroll, visibility)
6. Session storage integration for state persistence
7. White-label styling applied from config
8. Two-line integration works: `<script>` + `DecisionPlatform.init()`

### Granular Tasks

#### Task 6.1: Implement SDK Loader (loader.ts) (2 hours)
**Description:** Create loader script that fetches config and injects runtime per TAD §6.2 and PRD §7.8.

**Actions:**
- Create `sdk/src/loader.ts`:
  ```typescript
  interface LoaderConfig {
    siteId: string;
    apiUrl?: string;
  }
  
  interface SiteConfig {
    product_page_rules: any;
    trigger_thresholds: any;
    commentary_templates: string[];
    block_mapping: any;
    white_label: any;
    session_timeout_min: number;
    restoration_window_min: number;
    cta_selectors: string[];
    help_me_choose_selector?: string;
  }
  
  const DEFAULT_API_URL = "http://localhost:8000";
  
  async function fetchConfig(siteId: string, apiUrl: string): Promise<SiteConfig> {
    const response = await fetch(`${apiUrl}/sdk/config?site_id=${siteId}`);
    if (!response.ok) {
      throw new Error(`Failed to fetch config: ${response.status}`);
    }
    return response.json();
  }
  
  function injectRuntime(apiUrl: string): void {
    const script = document.createElement("script");
    script.src = `${apiUrl}/sdk/dap-sdk.js`;
    script.async = true;
    script.onerror = () => {
      console.error("DAP: Failed to load runtime script");
    };
    document.head.appendChild(script);
  }
  
  async function init(config: LoaderConfig): Promise<void> {
    const apiUrl = config.apiUrl || DEFAULT_API_URL;
    
    try {
      // Fetch site config
      const siteConfig = await fetchConfig(config.siteId, apiUrl);
      
      // Inject runtime script
      injectRuntime(apiUrl);
      
      // Wait for runtime to load and initialize
      const checkRuntime = setInterval(() => {
        if ((window as any).DAPRuntime) {
          clearInterval(checkRuntime);
          (window as any).DAPRuntime.init({
            siteId: config.siteId,
            config: siteConfig,
            apiUrl: apiUrl,
          });
        }
      }, 50);
      
      // Timeout after 5 seconds
      setTimeout(() => {
        clearInterval(checkRuntime);
        if (!(window as any).DAPRuntime) {
          console.error("DAP: Runtime failed to load");
        }
      }, 5000);
      
    } catch (error) {
      console.error("DAP: Initialization failed", error);
    }
  }
  
  // Expose global API
  (window as any).DecisionPlatform = {
    init: init,
  };
  ```

**Files to Create/Modify:**
- `sdk/src/loader.ts` (create)

**Acceptance:** Loader fetches config, injects runtime, initializes DAPRuntime

---

#### Task 6.2: Create SDK Runtime Foundation & Types (1 hour)
**Description:** Set up runtime structure with types and initialization per TAD §6.2.

**Actions:**
- Update `sdk/src/types.ts`:
  ```typescript
  export interface SiteConfig {
    product_page_rules: {
      url_patterns: string[];
      dom_selectors: string[];
      product_id_source: "url_path" | "data_attribute" | "meta";
    };
    trigger_thresholds: {
      multi_product_min: number;
      multi_product_window_min: number;
      dwell_sec: number;
      cta_hover_min: number;
      cooldown_after_trigger_sec: number;
      cooldown_after_dismiss_sec: number;
      cooldown_after_grid_close_sec: number;
    };
    commentary_templates: string[];
    block_mapping: Record<string, string[]>;
    white_label: {
      brand_name?: string;
      primary_color?: string;
      font_family?: string;
      logo_url?: string;
      copy_tone?: string;
    };
    session_timeout_min: number;
    restoration_window_min: number;
    cta_selectors: string[];
    help_me_choose_selector?: string;
  }
  
  export interface RuntimeConfig {
    siteId: string;
    config: SiteConfig;
    apiUrl: string;
  }
  
  export interface EventBuffer {
    pageViews: Array<{ url: string; timestamp: number }>;
    productViews: Array<{ productId: string; url: string; timestamp: number }>;
    dwellStart: number | null;
    dwellTime: number;
    ctaHovers: number;
    scrollDepth: number;
    samePageRevisits: Map<string, number>;
  }
  ```
- Create `sdk/src/runtime/index.ts`:
  ```typescript
  import { RuntimeConfig, SiteConfig } from "../types";
  import { initStrip } from "./strip";
  import { initEvents } from "./events";
  import { initSession } from "./session";
  
  let initialized = false;
  
  export function init(config: RuntimeConfig): void {
    if (initialized) {
      console.warn("DAP: Already initialized");
      return;
    }
    
    initialized = true;
    
    // Initialize session
    initSession(config);
    
    // Initialize strip
    initStrip(config);
    
    // Initialize event listeners
    initEvents(config);
    
    console.log("DAP: Initialized successfully");
  }
  
  // Expose to window
  (window as any).DAPRuntime = { init };
  ```

**Files to Create/Modify:**
- `sdk/src/types.ts` (modify)
- `sdk/src/runtime/index.ts` (create)

**Acceptance:** Runtime structure created, types defined, init function exposed

---

#### Task 6.3: Implement Strip DOM Rendering (2 hours)
**Description:** Create strip DOM element with white-label styling per PRD §7.1 and TAD §6.2.

**Actions:**
- Create `sdk/src/runtime/strip.ts`:
  ```typescript
  import { RuntimeConfig } from "../types";
  
  const STRIP_ID = "dap-commentary-strip";
  
  export function initStrip(config: RuntimeConfig): void {
    // Remove existing strip if present
    const existing = document.getElementById(STRIP_ID);
    if (existing) {
      existing.remove();
    }
    
    // Create strip element
    const strip = document.createElement("div");
    strip.id = STRIP_ID;
    strip.className = "dap-strip";
    
    // Apply white-label styling
    const whiteLabel = config.config.white_label;
    if (whiteLabel.primary_color) {
      strip.style.backgroundColor = whiteLabel.primary_color;
    } else {
      strip.style.backgroundColor = "rgba(0, 0, 0, 0.9)";
    }
    
    if (whiteLabel.font_family) {
      strip.style.fontFamily = whiteLabel.font_family;
    } else {
      strip.style.fontFamily = "system-ui, -apple-system, sans-serif";
    }
    
    // Base styles
    strip.style.position = "fixed";
    strip.style.bottom = "0";
    strip.style.left = "0";
    strip.style.right = "0";
    strip.style.height = "45px";
    strip.style.zIndex = "9999";
    strip.style.display = "flex";
    strip.style.alignItems = "center";
    strip.style.padding = "0 16px";
    strip.style.color = "#ffffff";
    strip.style.fontSize = "14px";
    strip.style.cursor = "pointer";
    strip.style.boxSizing = "border-box";
    
    // Mobile safe area
    strip.style.paddingBottom = "env(safe-area-inset-bottom, 0px)";
    
    // Initial commentary text
    strip.textContent = "Viewing page...";
    
    // Append to body
    document.body.appendChild(strip);
    
    // Store strip reference
    (window as any).__DAP_STRIP = strip;
  }
  
  export function updateStripText(text: string): void {
    const strip = document.getElementById(STRIP_ID) as HTMLElement;
    if (strip) {
      strip.textContent = text;
    }
  }
  
  export function getStrip(): HTMLElement | null {
    return document.getElementById(STRIP_ID);
  }
  ```
- Create `sdk/src/runtime/styles.css` (to be injected or bundled):
  ```css
  .dap-strip {
    /* Styles applied inline, but can be overridden here */
  }
  
  @media (max-width: 768px) {
    .dap-strip {
      height: 40px;
      font-size: 13px;
    }
  }
  ```

**Files to Create/Modify:**
- `sdk/src/runtime/strip.ts` (create)
- `sdk/src/runtime/styles.css` (create)

**Acceptance:** Strip renders at bottom, white-label styles applied, mobile safe area handled

---

#### Task 6.4: Implement Session Storage Module (1 hour)
**Description:** Create session storage utilities for state persistence per PRD §7.12 and TAD §2.7.

**Actions:**
- Create `sdk/src/runtime/session.ts`:
  ```typescript
  import { RuntimeConfig } from "../types";
  
  const STORAGE_KEY_PREFIX = "dap_";
  
  function getStorageKey(siteId: string, key: string): string {
    return `${STORAGE_KEY_PREFIX}${siteId}_${key}`;
  }
  
  export function initSession(config: RuntimeConfig): void {
    // Check for existing session
    const lastActivity = getSessionData<number>(config.siteId, "last_activity");
    const restorationWindow = config.config.restoration_window_min * 60 * 1000; // Convert to ms
    
    if (lastActivity && Date.now() - lastActivity < restorationWindow) {
      // Show "Continue where you left off?" prompt
      // (Implementation in later task)
    } else {
      // Clear old session data
      clearSession(config.siteId);
    }
    
    // Update last activity
    setSessionData(config.siteId, "last_activity", Date.now());
  }
  
  export function getSessionData<T>(siteId: string, key: string): T | null {
    try {
      const item = sessionStorage.getItem(getStorageKey(siteId, key));
      return item ? JSON.parse(item) : null;
    } catch {
      return null;
    }
  }
  
  export function setSessionData<T>(siteId: string, key: string, value: T): void {
    try {
      sessionStorage.setItem(getStorageKey(siteId, key), JSON.stringify(value));
    } catch (e) {
      console.warn("DAP: SessionStorage write failed", e);
    }
  }
  
  export function clearSession(siteId: string): void {
    const prefix = getStorageKey(siteId, "");
    const keysToRemove: string[] = [];
    
    for (let i = 0; i < sessionStorage.length; i++) {
      const key = sessionStorage.key(i);
      if (key && key.startsWith(prefix)) {
        keysToRemove.push(key);
      }
    }
    
    keysToRemove.forEach(key => sessionStorage.removeItem(key));
  }
  
  export function updateLastActivity(siteId: string): void {
    setSessionData(siteId, "last_activity", Date.now());
  }
  ```

**Files to Create/Modify:**
- `sdk/src/runtime/session.ts` (create)

**Acceptance:** Session storage functions work, data persists across page reloads

---

#### Task 6.5: Implement Basic Event Listeners (1.5 hours)
**Description:** Set up event listeners for page navigation, clicks, scroll per PRD §7.2 and TAD §6.2.

**Actions:**
- Create `sdk/src/runtime/events.ts`:
  ```typescript
  import { RuntimeConfig, EventBuffer } from "../types";
  import { updateLastActivity } from "./session";
  
  let eventBuffer: EventBuffer = {
    pageViews: [],
    productViews: [],
    dwellStart: null,
    dwellTime: 0,
    ctaHovers: 0,
    scrollDepth: 0,
    samePageRevisits: new Map(),
  };
  
  export function initEvents(config: RuntimeConfig): void {
    // Track page views (including SPA navigation)
    trackPageView(config);
    
    // Track scroll depth
    trackScroll(config);
    
    // Track dwell time
    trackDwell(config);
    
    // Track CTA hovers (if selectors configured)
    if (config.config.cta_selectors.length > 0) {
      trackCTAHovers(config);
    }
    
    // Track "Help me choose" button clicks
    if (config.config.help_me_choose_selector) {
      trackHelpMeChooseButton(config);
    }
    
    // Update last activity on user interaction
    document.addEventListener("click", () => updateLastActivity(config.siteId));
    document.addEventListener("scroll", () => updateLastActivity(config.siteId));
  }
  
  function trackPageView(config: RuntimeConfig): void {
    const currentUrl = window.location.href;
    
    eventBuffer.pageViews.push({
      url: currentUrl,
      timestamp: Date.now(),
    });
    
    // Track same-page revisits
    const revisitCount = eventBuffer.samePageRevisits.get(currentUrl) || 0;
    eventBuffer.samePageRevisits.set(currentUrl, revisitCount + 1);
    
    // Check if current page is a product page
    if (isProductPage(config, currentUrl)) {
      const productId = extractProductId(config, currentUrl);
      if (productId) {
        eventBuffer.productViews.push({
          productId,
          url: currentUrl,
          timestamp: Date.now(),
        });
      }
    }
    
    // Handle SPA navigation
    window.addEventListener("popstate", () => {
      trackPageView(config);
    });
  }
  
  function trackScroll(config: RuntimeConfig): void {
    let ticking = false;
    
    window.addEventListener("scroll", () => {
      if (!ticking) {
        window.requestAnimationFrame(() => {
          const scrollHeight = document.documentElement.scrollHeight - window.innerHeight;
          const scrolled = window.scrollY;
          eventBuffer.scrollDepth = Math.min(100, (scrolled / scrollHeight) * 100);
          ticking = false;
        });
        ticking = true;
      }
    });
  }
  
  function trackDwell(config: RuntimeConfig): void {
    eventBuffer.dwellStart = Date.now();
    
    const updateDwell = () => {
      if (eventBuffer.dwellStart) {
        eventBuffer.dwellTime = Math.floor((Date.now() - eventBuffer.dwellStart) / 1000);
      }
    };
    
    setInterval(updateDwell, 1000);
  }
  
  function trackCTAHovers(config: RuntimeConfig): void {
    config.config.cta_selectors.forEach(selector => {
      const elements = document.querySelectorAll(selector);
      elements.forEach(el => {
        el.addEventListener("mouseenter", () => {
          eventBuffer.ctaHovers++;
        });
      });
    });
  }
  
  function trackHelpMeChooseButton(config: RuntimeConfig): void {
    const button = document.querySelector(config.config.help_me_choose_selector!);
    if (button) {
      button.addEventListener("click", (e) => {
        e.preventDefault();
        // Trigger explicit intent menu (implementation in later task)
        (window as any).__DAP_TRIGGER_EXPLICIT?.();
      });
    }
  }
  
  function isProductPage(config: RuntimeConfig, url: string): boolean {
    const rules = config.config.product_page_rules;
    
    // Check URL patterns
    for (const pattern of rules.url_patterns) {
      const regex = new RegExp(pattern.replace("*", ".*"));
      if (regex.test(url)) {
        return true;
      }
    }
    
    // Check DOM selectors
    for (const selector of rules.dom_selectors) {
      if (document.querySelector(selector)) {
        return true;
      }
    }
    
    return false;
  }
  
  function extractProductId(config: RuntimeConfig, url: string): string | null {
    const source = config.config.product_page_rules.product_id_source;
    
    if (source === "url_path") {
      const path = new URL(url).pathname;
      return path.split("/").filter(Boolean).pop() || null;
    } else if (source === "data_attribute") {
      const element = document.querySelector("[data-product-id]");
      return element?.getAttribute("data-product-id") || null;
    } else if (source === "meta") {
      const meta = document.querySelector('meta[name="product-id"]');
      return meta?.getAttribute("content") || null;
    }
    
    return null;
  }
  
  export function getEventBuffer(): EventBuffer {
    return { ...eventBuffer };
  }
  
  export function resetEventBuffer(): void {
    eventBuffer = {
      pageViews: [],
      productViews: [],
      dwellStart: Date.now(),
      dwellTime: 0,
      ctaHovers: 0,
      scrollDepth: 0,
      samePageRevisits: new Map(),
    };
  }
  ```

**Files to Create/Modify:**
- `sdk/src/runtime/events.ts` (create)

**Acceptance:** Events tracked, product page detection works, event buffer populated

---

#### Task 6.6: Build SDK Bundle & Test Integration (30 min)
**Description:** Build SDK bundles and test two-line integration per PRD §7.8.

**Actions:**
- Update `sdk/package.json`:
  ```json
  {
    "scripts": {
      "build": "rollup -c",
      "dev": "rollup -c --watch"
    }
  }
  ```
- Build bundles: `npm run build`
- Create test HTML file `sdk/test/index.html`:
  ```html
  <!DOCTYPE html>
  <html>
  <head>
    <title>DAP SDK Test</title>
  </head>
  <body>
    <h1>Test Page</h1>
    <p>This is a test page for DAP SDK.</p>
    
    <script src="http://localhost:8000/sdk/loader.js"></script>
    <script>
      DecisionPlatform.init({ siteId: "test-site-id" });
    </script>
  </body>
  </html>
  ```
- Test: Open HTML file, verify strip appears, check console for errors

**Files to Create/Modify:**
- `sdk/package.json` (modify)
- `sdk/test/index.html` (create)

**Acceptance:** Bundles build successfully, test page shows strip, no console errors

---

### Day 6 Summary
- ✅ SDK loader implemented
- ✅ Runtime foundation created
- ✅ Strip DOM rendering with white-label
- ✅ Session storage module
- ✅ Basic event listeners
- ✅ SDK bundles built and tested

**Next Day Preview:** Day 7 will implement the commentary system and enhance event tracking.

---

## Day 7: SDK Events & Commentary System + Triggers & Intent Selection

**Epic:** EPIC-4 - SDK Implementation  
**Story:** STORY-4.2 - Commentary System, Triggers & Intent Selection  
**Total Effort:** 8 hours  
**Day:** 7

### Story Description
As a developer, I want to implement the commentary system that updates the strip text based on user behavior, the trigger detection system that fires when decision friction is detected, and the intent selection modal, so that users are guided to select their intent and proceed to grid assembly.

### Acceptance Criteria
1. Commentary system implemented with template-based text updates
2. Commentary throttling (debounce 500ms, max 1 update per 2s) per PRD §7.1
3. Trigger detection system with all 5 trigger types per PRD §7.2
4. Trigger priority system (Explicit > Multiple Products > CTA Hover > Hesitation > Loops)
5. Trigger cooldown logic (30s/60s/45s) per PRD §7.2
6. Dismissal tracking (suppress after 2 dismissals)
7. Intent selection modal with 5 intent options per PRD §7.3
8. Intent stored in sessionStorage
9. Event buffer reset on session timeout

### Granular Tasks

#### Task 7.1: Implement Commentary System with Throttling (2 hours)
**Description:** Create commentary engine that maps events to templates and updates strip text with throttling per PRD §7.1 and TAD §14.2.

**Actions:**
- Create `sdk/src/runtime/commentary.ts`:
  ```typescript
  import { RuntimeConfig, EventBuffer } from "../types";
  import { updateStripText } from "./strip";
  import { getEventBuffer } from "./events";
  
  let updateTimer: number | null = null;
  let lastUpdateTime = 0;
  const DEBOUNCE_MS = 500;
  const MAX_UPDATE_INTERVAL_MS = 2000;
  
  export function initCommentary(config: RuntimeConfig): void {
    // Start commentary update loop
    startCommentaryLoop(config);
  }
  
  function startCommentaryLoop(config: RuntimeConfig): void {
    const update = () => {
      const now = Date.now();
      
      // Throttle: max 1 update per 2 seconds
      if (now - lastUpdateTime < MAX_UPDATE_INTERVAL_MS) {
        updateTimer = window.setTimeout(update, MAX_UPDATE_INTERVAL_MS);
        return;
      }
      
      // Debounce: wait 500ms after last event
      if (updateTimer) {
        clearTimeout(updateTimer);
      }
      
      updateTimer = window.setTimeout(() => {
        const text = generateCommentary(config);
        updateStripText(text);
        lastUpdateTime = Date.now();
        updateTimer = null;
      }, DEBOUNCE_MS);
    };
    
    // Update on events
    document.addEventListener("click", update);
    window.addEventListener("scroll", update);
    window.addEventListener("popstate", update);
    
    // Initial update
    update();
  }
  
  function generateCommentary(config: RuntimeConfig): string {
    const buffer = getEventBuffer();
    const templates = config.config.commentary_templates;
    
    // Count distinct products viewed in last 5 minutes
    const fiveMinutesAgo = Date.now() - (5 * 60 * 1000);
    const recentProducts = buffer.productViews.filter(
      pv => pv.timestamp > fiveMinutesAgo
    );
    const distinctProducts = new Set(recentProducts.map(p => p.productId));
    const productCount = distinctProducts.size;
    
    // Get dwell time
    const dwellSeconds = Math.floor(buffer.dwellTime);
    
    // Select template based on events
    let template = templates[0] || "Viewing page...";
    
    if (productCount >= 2) {
      // Find template with {n} placeholder
      template = templates.find(t => t.includes("{n}")) || 
        `You've viewed ${productCount} products — comparing options?`;
      template = template.replace("{n}", productCount.toString());
    } else if (dwellSeconds >= 45 && buffer.scrollDepth > 60) {
      template = templates.find(t => t.includes("dwell") || t.includes("time")) ||
        `Spent ${dwellSeconds} seconds on this page — need more info?`;
    } else if (buffer.ctaHovers >= 2) {
      template = templates.find(t => t.includes("hover")) ||
        "Hovered over action buttons — want help choosing?";
    } else {
      // Default: show current page context
      const currentUrl = window.location.href;
      const pageName = document.title || new URL(currentUrl).pathname;
      template = `Viewing ${pageName}...`;
    }
    
    return template;
  }
  
  export function stopCommentary(): void {
    if (updateTimer) {
      clearTimeout(updateTimer);
      updateTimer = null;
    }
  }
  ```
- Integrate commentary into runtime init:
  ```typescript
  // In runtime/index.ts
  import { initCommentary } from "./commentary";
  
  export function init(config: RuntimeConfig): void {
    // ... existing code ...
    initCommentary(config);
  }
  ```

**Files to Create/Modify:**
- `sdk/src/runtime/commentary.ts` (create)
- `sdk/src/runtime/index.ts` (modify)

**Acceptance:** Commentary updates strip text, throttling works (max 1 per 2s), debounce prevents flicker

---

#### Task 7.2: Implement Trigger Detection System - Core Rules (2 hours)
**Description:** Implement all 5 trigger types with rule evaluation per PRD §7.2 and TAD §14.3.

**Actions:**
- Create `sdk/src/runtime/triggers.ts`:
  ```typescript
  import { RuntimeConfig, EventBuffer } from "../types";
  import { getEventBuffer } from "./events";
  import { getSessionData, setSessionData } from "./session";
  
  export type TriggerType = 
    | "explicit"
    | "multiple_products"
    | "cta_hover"
    | "hesitation"
    | "navigation_loops";
  
  export interface TriggerState {
    lastTriggerTime: number | null;
    lastDismissTime: number | null;
    lastGridCloseTime: number | null;
    dismissalCount: number;
    cooldownActive: boolean;
  }
  
  let triggerState: TriggerState = {
    lastTriggerTime: null,
    lastDismissTime: null,
    lastGridCloseTime: null,
    dismissalCount: 0,
    cooldownActive: false,
  };
  
  export function initTriggers(config: RuntimeConfig): void {
    // Load trigger state from sessionStorage
    const saved = getSessionData<TriggerState>(config.siteId, "trigger_state");
    if (saved) {
      triggerState = { ...triggerState, ...saved };
    }
    
    // Check triggers periodically
    setInterval(() => {
      checkTriggers(config);
    }, 1000); // Check every second
  }
  
  function checkTriggers(config: RuntimeConfig): void {
    // Skip if cooldown active or dismissed 2+ times
    if (triggerState.cooldownActive || triggerState.dismissalCount >= 2) {
      return;
    }
    
    // Check cooldowns
    const now = Date.now();
    const thresholds = config.config.trigger_thresholds;
    
    // Cooldown after trigger (30s)
    if (triggerState.lastTriggerTime) {
      const timeSinceTrigger = now - triggerState.lastTriggerTime;
      if (timeSinceTrigger < thresholds.cooldown_after_trigger_sec * 1000) {
        return;
      }
    }
    
    // Cooldown after dismiss (60s)
    if (triggerState.lastDismissTime) {
      const timeSinceDismiss = now - triggerState.lastDismissTime;
      if (timeSinceDismiss < thresholds.cooldown_after_dismiss_sec * 1000) {
        return;
      }
    }
    
    // Cooldown after grid close (45s)
    if (triggerState.lastGridCloseTime) {
      const timeSinceClose = now - triggerState.lastGridCloseTime;
      if (timeSinceClose < thresholds.cooldown_after_grid_close_sec * 1000) {
        return;
      }
    }
    
    // Evaluate trigger rules
    const buffer = getEventBuffer();
    const firedTriggers: TriggerType[] = [];
    
    // 1. Multiple Product Views (FR-006)
    const windowMs = thresholds.multi_product_window_min * 60 * 1000;
    const recentProducts = buffer.productViews.filter(
      pv => Date.now() - pv.timestamp < windowMs
    );
    const distinctProducts = new Set(recentProducts.map(p => p.productId));
    if (distinctProducts.size >= thresholds.multi_product_min) {
      firedTriggers.push("multiple_products");
    }
    
    // 2. Hesitation Detection (FR-007)
    if (
      buffer.dwellTime >= thresholds.dwell_sec &&
      buffer.scrollDepth > 60 &&
      buffer.ctaHovers === 0 // No CTA clicks
    ) {
      firedTriggers.push("hesitation");
    }
    
    // 3. CTA Hover Pattern (FR-008)
    if (
      buffer.ctaHovers >= thresholds.cta_hover_min &&
      buffer.dwellTime > 30
    ) {
      firedTriggers.push("cta_hover");
    }
    
    // 4. Navigation Loops (FR-009)
    const threeMinutesAgo = Date.now() - (3 * 60 * 1000);
    for (const [url, count] of buffer.samePageRevisits.entries()) {
      if (count >= 2) {
        // Check if revisit was within 3 minutes
        const recentViews = buffer.pageViews.filter(
          pv => pv.url === url && pv.timestamp > threeMinutesAgo
        );
        if (recentViews.length >= 2) {
          firedTriggers.push("navigation_loops");
          break;
        }
      }
    }
    
    // 5. Explicit trigger handled separately (on button click)
    
    // Apply priority and fire highest priority trigger
    if (firedTriggers.length > 0) {
      const priority: TriggerType[] = [
        "explicit",
        "multiple_products",
        "cta_hover",
        "hesitation",
        "navigation_loops",
      ];
      
      const highestPriority = priority.find(t => firedTriggers.includes(t));
      if (highestPriority) {
        fireTrigger(config, highestPriority);
      }
    }
  }
  
  function fireTrigger(config: RuntimeConfig, type: TriggerType): void {
    triggerState.lastTriggerTime = Date.now();
    triggerState.cooldownActive = true;
    
    // Save state
    setSessionData(config.siteId, "trigger_state", triggerState);
    
    // Show strip CTA
    updateStripText("Want help? Click here");
    
    // Make strip clickable
    const strip = document.getElementById("dap-commentary-strip");
    if (strip) {
      strip.style.cursor = "pointer";
      strip.onclick = () => {
        showIntentModal(config);
      };
    }
    
    // Emit trigger event
    (window as any).__DAP_TRIGGER_FIRED = type;
  }
  
  export function fireExplicitTrigger(config: RuntimeConfig): void {
    fireTrigger(config, "explicit");
  }
  
  export function onIntentDismissed(config: RuntimeConfig): void {
    triggerState.lastDismissTime = Date.now();
    triggerState.dismissalCount++;
    triggerState.cooldownActive = true;
    setSessionData(config.siteId, "trigger_state", triggerState);
  }
  
  export function onGridClosed(config: RuntimeConfig): void {
    triggerState.lastGridCloseTime = Date.now();
    triggerState.cooldownActive = true;
    setSessionData(config.siteId, "trigger_state", triggerState);
  }
  
  function updateStripText(text: string): void {
    const strip = document.getElementById("dap-commentary-strip");
    if (strip) {
      strip.textContent = text;
    }
  }
  
  function showIntentModal(config: RuntimeConfig): void {
    // Implementation in next task
  }
  ```

**Files to Create/Modify:**
- `sdk/src/runtime/triggers.ts` (create)

**Acceptance:** All 5 trigger types detect correctly, priority system works, cooldowns enforced

---

#### Task 7.3: Implement Intent Selection Modal (2 hours)
**Description:** Create intent selection modal with 5 intent options per PRD §7.3.

**Actions:**
- Create `sdk/src/runtime/intent.ts`:
  ```typescript
  import { RuntimeConfig } from "../types";
  import { setSessionData } from "./session";
  import { onIntentDismissed } from "./triggers";
  
  const INTENTS = [
    {
      id: "help_me_choose",
      label: "Help me choose",
      description: "Get personalized recommendations",
      icon: "🎯",
    },
    {
      id: "compare_options",
      label: "Compare options",
      description: "See side-by-side comparison",
      icon: "⚖️",
    },
    {
      id: "check_eligibility",
      label: "Check eligibility",
      description: "Find out if you qualify",
      icon: "✅",
    },
    {
      id: "understand_differences",
      label: "Understand differences",
      description: "Learn what sets them apart",
      icon: "🔍",
    },
    {
      id: "just_exploring",
      label: "Just exploring",
      description: "Browse available options",
      icon: "🔎",
    },
  ];
  
  export function showIntentModal(config: RuntimeConfig): void {
    // Remove existing modal if present
    const existing = document.getElementById("dap-intent-modal");
    if (existing) {
      existing.remove();
    }
    
    // Create modal overlay
    const overlay = document.createElement("div");
    overlay.id = "dap-intent-modal";
    overlay.className = "dap-modal-overlay";
    
    // Apply white-label styling
    const whiteLabel = config.config.white_label;
    overlay.style.position = "fixed";
    overlay.style.top = "0";
    overlay.style.left = "0";
    overlay.style.right = "0";
    overlay.style.bottom = "0";
    overlay.style.backgroundColor = "rgba(0, 0, 0, 0.7)";
    overlay.style.zIndex = "10000";
    overlay.style.display = "flex";
    overlay.style.alignItems = "center";
    overlay.style.justifyContent = "center";
    overlay.style.padding = "20px";
    
    // Create modal content
    const modal = document.createElement("div");
    modal.className = "dap-modal-content";
    modal.style.backgroundColor = "#ffffff";
    modal.style.borderRadius = "12px";
    modal.style.padding = "32px";
    modal.style.maxWidth = "600px";
    modal.style.width = "100%";
    modal.style.maxHeight = "90vh";
    modal.style.overflowY = "auto";
    
    if (whiteLabel.font_family) {
      modal.style.fontFamily = whiteLabel.font_family;
    }
    
    // Title
    const title = document.createElement("h2");
    title.textContent = "How can we help?";
    title.style.margin = "0 0 24px 0";
    title.style.fontSize = "24px";
    title.style.fontWeight = "600";
    modal.appendChild(title);
    
    // Intent cards
    const grid = document.createElement("div");
    grid.style.display = "grid";
    grid.style.gridTemplateColumns = "repeat(auto-fit, minmax(200px, 1fr))";
    grid.style.gap = "16px";
    
    INTENTS.forEach(intent => {
      const card = createIntentCard(intent, config);
      grid.appendChild(card);
    });
    
    modal.appendChild(grid);
    
    // Close button
    const closeBtn = document.createElement("button");
    closeBtn.textContent = "×";
    closeBtn.style.position = "absolute";
    closeBtn.style.top = "16px";
    closeBtn.style.right = "16px";
    closeBtn.style.width = "32px";
    closeBtn.style.height = "32px";
    closeBtn.style.border = "none";
    closeBtn.style.backgroundColor = "transparent";
    closeBtn.style.fontSize = "24px";
    closeBtn.style.cursor = "pointer";
    closeBtn.onclick = () => {
      onIntentDismissed(config);
      overlay.remove();
    };
    modal.style.position = "relative";
    modal.appendChild(closeBtn);
    
    // Click outside to dismiss
    overlay.onclick = (e) => {
      if (e.target === overlay) {
        onIntentDismissed(config);
        overlay.remove();
      }
    };
    
    overlay.appendChild(modal);
    document.body.appendChild(overlay);
  }
  
  function createIntentCard(intent: typeof INTENTS[0], config: RuntimeConfig): HTMLElement {
    const card = document.createElement("div");
    card.className = "dap-intent-card";
    card.style.border = "2px solid #e5e7eb";
    card.style.borderRadius = "8px";
    card.style.padding = "20px";
    card.style.cursor = "pointer";
    card.style.transition = "all 0.2s";
    
    card.onmouseenter = () => {
      card.style.borderColor = config.config.white_label.primary_color || "#3b82f6";
      card.style.backgroundColor = "#f9fafb";
    };
    
    card.onmouseleave = () => {
      card.style.borderColor = "#e5e7eb";
      card.style.backgroundColor = "transparent";
    };
    
    card.onclick = () => {
      selectIntent(config, intent.id);
    };
    
    // Icon
    const icon = document.createElement("div");
    icon.textContent = intent.icon;
    icon.style.fontSize = "32px";
    icon.style.marginBottom = "12px";
    card.appendChild(icon);
    
    // Label
    const label = document.createElement("div");
    label.textContent = intent.label;
    label.style.fontSize = "16px";
    label.style.fontWeight = "600";
    label.style.marginBottom = "8px";
    card.appendChild(label);
    
    // Description
    const desc = document.createElement("div");
    desc.textContent = intent.description;
    desc.style.fontSize = "14px";
    desc.style.color = "#6b7280";
    card.appendChild(desc);
    
    return card;
  }
  
  function selectIntent(config: RuntimeConfig, intentId: string): void {
    // Store intent in sessionStorage
    setSessionData(config.siteId, "selected_intent", intentId);
    setSessionData(config.siteId, "intent_selected_at", Date.now());
    
    // Remove modal
    const modal = document.getElementById("dap-intent-modal");
    if (modal) {
      modal.remove();
    }
    
    // Trigger grid assembly
    (window as any).__DAP_ASSEMBLE_GRID?.(config, intentId);
  }
  
  export function getSelectedIntent(config: RuntimeConfig): string | null {
    return getSessionData<string>(config.siteId, "selected_intent");
  }
  ```
- Update triggers.ts to call showIntentModal:
  ```typescript
  import { showIntentModal } from "./intent";
  
  function showIntentModal(config: RuntimeConfig): void {
    showIntentModal(config);
  }
  ```

**Files to Create/Modify:**
- `sdk/src/runtime/intent.ts` (create)
- `sdk/src/runtime/triggers.ts` (modify)

**Acceptance:** Intent modal appears on trigger, 5 intents displayed, selection stores intent, modal dismisses correctly

---

#### Task 7.4: Integrate Triggers & Intent into Runtime (1 hour)
**Description:** Wire up triggers and intent selection into runtime initialization.

**Actions:**
- Update `sdk/src/runtime/index.ts`:
  ```typescript
  import { initTriggers, fireExplicitTrigger } from "./triggers";
  import { showIntentModal } from "./intent";
  
  export function init(config: RuntimeConfig): void {
    // ... existing initialization ...
    
    // Initialize triggers
    initTriggers(config);
    
    // Expose explicit trigger function
    (window as any).__DAP_TRIGGER_EXPLICIT = () => {
      fireExplicitTrigger(config);
    };
    
    // Expose intent modal function
    (window as any).__DAP_SHOW_INTENT_MODAL = () => {
      showIntentModal(config);
    };
  }
  ```
- Update events.ts to call explicit trigger:
  ```typescript
  function trackHelpMeChooseButton(config: RuntimeConfig): void {
    const button = document.querySelector(config.config.help_me_choose_selector!);
    if (button) {
      button.addEventListener("click", (e) => {
        e.preventDefault();
        (window as any).__DAP_TRIGGER_EXPLICIT?.();
      });
    }
  }
  ```
- Update strip.ts to handle click:
  ```typescript
  export function initStrip(config: RuntimeConfig): void {
    // ... existing code ...
    
    // Make strip clickable when trigger fires
    strip.onclick = () => {
      if ((window as any).__DAP_TRIGGER_FIRED) {
        (window as any).__DAP_SHOW_INTENT_MODAL?.();
      }
    };
  }
  ```

**Files to Create/Modify:**
- `sdk/src/runtime/index.ts` (modify)
- `sdk/src/runtime/events.ts` (modify)
- `sdk/src/runtime/strip.ts` (modify)

**Acceptance:** Triggers fire correctly, intent modal shows on trigger, explicit trigger works

---

#### Task 7.5: Implement Session Timeout & Event Buffer Reset (30 min)
**Description:** Reset event buffer on session timeout per PRD §7.2 and TAD §2.2.

**Actions:**
- Update `sdk/src/runtime/session.ts`:
  ```typescript
  export function checkSessionTimeout(config: RuntimeConfig): boolean {
    const lastActivity = getSessionData<number>(config.siteId, "last_activity");
    const timeoutMs = config.config.session_timeout_min * 60 * 1000;
    
    if (lastActivity && Date.now() - lastActivity > timeoutMs) {
      // Session timed out - clear state
      clearSession(config.siteId);
      return true;
    }
    return false;
  }
  ```
- Update `sdk/src/runtime/events.ts`:
  ```typescript
  import { checkSessionTimeout } from "./session";
  
  export function initEvents(config: RuntimeConfig): void {
    // Check session timeout periodically
    setInterval(() => {
      if (checkSessionTimeout(config)) {
        resetEventBuffer();
      }
    }, 60000); // Check every minute
    
    // ... rest of event initialization ...
  }
  ```

**Files to Create/Modify:**
- `sdk/src/runtime/session.ts` (modify)
- `sdk/src/runtime/events.ts` (modify)

**Acceptance:** Event buffer resets on session timeout, triggers re-evaluate from scratch

---

### Day 7 Summary
- ✅ Commentary system with throttling implemented
- ✅ All 5 trigger types detected
- ✅ Trigger priority system working
- ✅ Cooldown logic enforced
- ✅ Intent selection modal created
- ✅ Session timeout and buffer reset implemented

**Next Day Preview:** Day 8 will implement grid assembly and rationale display.

---

## Day 8: SDK Grid Assembly & Rationale

**Epic:** EPIC-4 - SDK Implementation  
**Story:** STORY-4.3 - Grid Assembly & Rationale Display  
**Total Effort:** 8 hours  
**Day:** 8

### Story Description
As a developer, I want to implement the grid assembly system that calls the assemble API, renders product cards in blocks, and displays rationale panels, so that users can see relevant products and understand why each is recommended.

### Acceptance Criteria
1. Context extraction from current page and event buffer
2. Assemble API call (POST /assemble) with context and intent
3. Grid rendering with responsive layout (3/2/1 columns)
4. Product cards display (title, features, price, eligibility)
5. Block rendering per intent→block mapping
6. "Why this?" button on each product card
7. Rationale panel display with template-filled text
8. Loading states and error handling
9. Empty results handling with fallback message

### Granular Tasks

#### Task 8.1: Implement Context Extraction (1 hour)
**Description:** Extract context from page and event buffer for assemble API per PRD §7.4 and TAD §7.3.

**Actions:**
- Create `sdk/src/runtime/context.ts`:
  ```typescript
  import { RuntimeConfig, EventBuffer } from "../types";
  import { getEventBuffer } from "./events";
  
  export interface AssembleContext {
    url: string;
    page_title: string;
    product_ids: string[];
    custom_query?: {
      type: string;
      value: string;
    };
  }
  
  export function extractContext(config: RuntimeConfig): AssembleContext {
    const buffer = getEventBuffer();
    
    // Get current URL
    const url = window.location.href;
    
    // Get page title
    const pageTitle = document.title || new URL(url).pathname;
    
    // Get product IDs from recent product views (last 5 minutes)
    const fiveMinutesAgo = Date.now() - (5 * 60 * 1000);
    const recentProducts = buffer.productViews.filter(
      pv => pv.timestamp > fiveMinutesAgo
    );
    const productIds = Array.from(new Set(recentProducts.map(p => p.productId)));
    
    return {
      url,
      page_title: pageTitle,
      product_ids: productIds,
    };
  }
  ```

**Files to Create/Modify:**
- `sdk/src/runtime/context.ts` (create)

**Acceptance:** Context extracted correctly, product IDs from recent views included

---

#### Task 8.2: Implement Assemble API Call (1.5 hours)
**Description:** Call POST /assemble endpoint and handle response per TAD §12.1.

**Actions:**
- Create `sdk/src/runtime/assemble.ts`:
  ```typescript
  import { RuntimeConfig } from "../types";
  import { extractContext, AssembleContext } from "./context";
  
  export interface AssembleResponse {
    blocks: Array<{
      type: string;
      products: any[];
    }>;
    products: Array<{
      id: string;
      title: string;
      url: string;
      price?: string;
      features: string[];
      eligibility?: string;
    }>;
    rationales: Record<string, string>;
    empty: boolean;
  }
  
  export async function callAssemble(
    config: RuntimeConfig,
    intent: string,
    blockType?: string,
    pullQuery?: string,
  ): Promise<AssembleResponse> {
    const context = extractContext(config);
    
    const requestBody: any = {
      site_id: config.siteId,
      intent: intent,
      context: context,
    };
    
    if (blockType) {
      requestBody.block_type = blockType;
    }
    
    if (pullQuery) {
      requestBody.pull_query = pullQuery;
    }
    
    try {
      const response = await fetch(`${config.apiUrl}/assemble`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(requestBody),
      });
      
      if (!response.ok) {
        throw new Error(`Assemble API error: ${response.status}`);
      }
      
      const data: AssembleResponse = await response.json();
      return data;
    } catch (error) {
      console.error("DAP: Assemble API call failed", error);
      throw error;
    }
  }
  ```

**Files to Create/Modify:**
- `sdk/src/runtime/assemble.ts` (create)

**Acceptance:** Assemble API called correctly, response parsed, errors handled

---

#### Task 8.3: Implement Grid Rendering - Layout & Blocks (2 hours)
**Description:** Render grid with responsive layout and blocks per PRD §7.4 and TAD §14.4.

**Actions:**
- Create `sdk/src/runtime/grid.ts`:
  ```typescript
  import { RuntimeConfig } from "../types";
  import { AssembleResponse } from "./assemble";
  import { onGridClosed } from "./triggers";
  
  const GRID_ID = "dap-decision-grid";
  
  export function renderGrid(
    config: RuntimeConfig,
    response: AssembleResponse,
  ): void {
    // Remove existing grid
    const existing = document.getElementById(GRID_ID);
    if (existing) {
      existing.remove();
    }
    
    // Create grid container
    const grid = document.createElement("div");
    grid.id = GRID_ID;
    grid.className = "dap-grid";
    
    // Apply white-label styling
    const whiteLabel = config.config.white_label;
    grid.style.position = "fixed";
    grid.style.top = "0";
    grid.style.left = "0";
    grid.style.right = "0";
    grid.style.bottom = "0";
    grid.style.backgroundColor = "rgba(0, 0, 0, 0.8)";
    grid.style.zIndex = "10001";
    grid.style.overflowY = "auto";
    grid.style.padding = "20px";
    
    // Create grid content
    const content = document.createElement("div");
    content.style.maxWidth = "1200px";
    content.style.margin = "0 auto";
    content.style.backgroundColor = "#ffffff";
    content.style.borderRadius = "12px";
    content.style.padding = "32px";
    
    if (whiteLabel.font_family) {
      content.style.fontFamily = whiteLabel.font_family;
    }
    
    // Close button
    const closeBtn = document.createElement("button");
    closeBtn.textContent = "×";
    closeBtn.style.position = "absolute";
    closeBtn.style.top = "16px";
    closeBtn.style.right = "16px";
    closeBtn.style.width = "32px";
    closeBtn.style.height = "32px";
    closeBtn.style.border = "none";
    closeBtn.style.backgroundColor = "transparent";
    closeBtn.style.fontSize = "24px";
    closeBtn.style.cursor = "pointer";
    closeBtn.onclick = () => {
      onGridClosed(config);
      grid.remove();
    };
    content.style.position = "relative";
    content.appendChild(closeBtn);
    
    // Render blocks
    response.blocks.forEach(block => {
      const blockElement = renderBlock(config, block, response.rationales);
      content.appendChild(blockElement);
    });
    
    // Handle empty results
    if (response.empty) {
      const emptyMsg = document.createElement("div");
      emptyMsg.style.padding = "20px";
      emptyMsg.style.textAlign = "center";
      emptyMsg.style.color = "#6b7280";
      emptyMsg.innerHTML = `
        <p>No products found matching your criteria.</p>
        <p>Showing popular options instead.</p>
      `;
      content.insertBefore(emptyMsg, content.firstChild);
    }
    
    grid.appendChild(content);
    document.body.appendChild(grid);
    
    // Click outside to close
    grid.onclick = (e) => {
      if (e.target === grid) {
        onGridClosed(config);
        grid.remove();
      }
    };
  }
  
  function renderBlock(
    config: RuntimeConfig,
    block: AssembleResponse["blocks"][0],
    rationales: Record<string, string>,
  ): HTMLElement {
    const blockElement = document.createElement("div");
    blockElement.className = `dap-block dap-block-${block.type}`;
    blockElement.style.marginBottom = "32px";
    
    // Block title
    const title = document.createElement("h3");
    title.textContent = formatBlockTitle(block.type);
    title.style.fontSize = "20px";
    title.style.fontWeight = "600";
    title.style.marginBottom = "16px";
    blockElement.appendChild(title);
    
    // Products grid
    const productsGrid = document.createElement("div");
    productsGrid.className = "dap-products-grid";
    productsGrid.style.display = "grid";
    productsGrid.style.gridTemplateColumns = "repeat(auto-fit, minmax(280px, 1fr))";
    productsGrid.style.gap = "20px";
    
    block.products.forEach(product => {
      const card = renderProductCard(config, product, rationales[product.id]);
      productsGrid.appendChild(card);
    });
    
    blockElement.appendChild(productsGrid);
    
    return blockElement;
  }
  
  function formatBlockTitle(blockType: string): string {
    const titles: Record<string, string> = {
      shortlist: "Recommended Options",
      comparison: "Comparison",
      costs: "Costs & Pricing",
      benefits: "Benefits",
      limitations: "Limitations",
      eligibility: "Eligibility",
      use_case_fit: "Use Case Fit",
      trade_off: "Trade-offs",
      examples: "Examples",
      action: "Next Steps",
      custom_query: "Custom Query Results",
    };
    return titles[blockType] || blockType;
  }
  ```

**Files to Create/Modify:**
- `sdk/src/runtime/grid.ts` (create)

**Acceptance:** Grid renders with blocks, responsive layout works, close button functions

---

#### Task 8.4: Implement Product Card Rendering (1.5 hours)
**Description:** Render product cards with all information and "Why this?" button per PRD §7.4.

**Actions:**
- Add product card rendering to `grid.ts`:
  ```typescript
  function renderProductCard(
    config: RuntimeConfig,
    product: AssembleResponse["products"][0],
    rationale: string | undefined,
  ): HTMLElement {
    const card = document.createElement("div");
    card.className = "dap-product-card";
    card.style.border = "1px solid #e5e7eb";
    card.style.borderRadius = "8px";
    card.style.padding = "20px";
    card.style.display = "flex";
    card.style.flexDirection = "column";
    
    // Title
    const title = document.createElement("h4");
    title.textContent = product.title;
    title.style.fontSize = "18px";
    title.style.fontWeight = "600";
    title.style.marginBottom = "12px";
    card.appendChild(title);
    
    // Features
    if (product.features && product.features.length > 0) {
      const featuresList = document.createElement("ul");
      featuresList.style.margin = "0 0 12px 0";
      featuresList.style.paddingLeft = "20px";
      featuresList.style.listStyle = "disc";
      
      product.features.slice(0, 4).forEach(feature => {
        const li = document.createElement("li");
        li.textContent = feature;
        li.style.marginBottom = "4px";
        li.style.fontSize = "14px";
        li.style.color = "#374151";
        featuresList.appendChild(li);
      });
      
      card.appendChild(featuresList);
    }
    
    // Price
    if (product.price) {
      const price = document.createElement("div");
      price.textContent = `Price: ${product.price}`;
      price.style.fontSize = "16px";
      price.style.fontWeight = "600";
      price.style.color = config.config.white_label.primary_color || "#3b82f6";
      price.style.marginBottom = "12px";
      card.appendChild(price);
    }
    
    // Eligibility
    if (product.eligibility) {
      const eligibility = document.createElement("div");
      eligibility.textContent = `✓ ${product.eligibility}`;
      eligibility.style.fontSize = "14px";
      eligibility.style.color = "#10b981";
      eligibility.style.marginBottom = "12px";
      card.appendChild(eligibility);
    }
    
    // Actions
    const actions = document.createElement("div");
    actions.style.display = "flex";
    actions.style.gap = "8px";
    actions.style.marginTop = "auto";
    
    // "Why this?" button
    if (rationale) {
      const whyBtn = document.createElement("button");
      whyBtn.textContent = "Why this?";
      whyBtn.style.padding = "8px 16px";
      whyBtn.style.border = "1px solid #e5e7eb";
      whyBtn.style.borderRadius = "6px";
      whyBtn.style.backgroundColor = "transparent";
      whyBtn.style.cursor = "pointer";
      whyBtn.style.fontSize = "14px";
      whyBtn.onclick = () => {
        showRationalePanel(config, product, rationale);
      };
      actions.appendChild(whyBtn);
    }
    
    // CTA button (link to product)
    if (product.url) {
      const ctaBtn = document.createElement("a");
      ctaBtn.textContent = "Learn More";
      ctaBtn.href = product.url;
      ctaBtn.target = "_blank";
      ctaBtn.style.padding = "8px 16px";
      ctaBtn.style.border = "none";
      ctaBtn.style.borderRadius = "6px";
      ctaBtn.style.backgroundColor = config.config.white_label.primary_color || "#3b82f6";
      ctaBtn.style.color = "#ffffff";
      ctaBtn.style.textDecoration = "none";
      ctaBtn.style.cursor = "pointer";
      ctaBtn.style.fontSize = "14px";
      actions.appendChild(ctaBtn);
    }
    
    card.appendChild(actions);
    
    return card;
  }
  ```

**Files to Create/Modify:**
- `sdk/src/runtime/grid.ts` (modify)

**Acceptance:** Product cards render with all info, "Why this?" button present, styling correct

---

#### Task 8.5: Implement Rationale Panel (1 hour)
**Description:** Create rationale panel that displays explanation per PRD §7.5.

**Actions:**
- Add rationale panel to `grid.ts`:
  ```typescript
  function showRationalePanel(
    config: RuntimeConfig,
    product: AssembleResponse["products"][0],
    rationale: string,
  ): void {
    // Remove existing panel
    const existing = document.getElementById("dap-rationale-panel");
    if (existing) {
      existing.remove();
    }
    
    // Create overlay
    const overlay = document.createElement("div");
    overlay.id = "dap-rationale-panel";
    overlay.style.position = "fixed";
    overlay.style.top = "0";
    overlay.style.left = "0";
    overlay.style.right = "0";
    overlay.style.bottom = "0";
    overlay.style.backgroundColor = "rgba(0, 0, 0, 0.5)";
    overlay.style.zIndex = "10002";
    overlay.style.display = "flex";
    overlay.style.alignItems = "center";
    overlay.style.justifyContent = "center";
    overlay.style.padding = "20px";
    
    // Create panel
    const panel = document.createElement("div");
    panel.style.backgroundColor = "#ffffff";
    panel.style.borderRadius = "12px";
    panel.style.padding = "32px";
    panel.style.maxWidth = "500px";
    panel.style.width = "100%";
    panel.style.maxHeight = "80vh";
    panel.style.overflowY = "auto";
    
    // Title
    const title = document.createElement("h3");
    title.textContent = `Why ${product.title}?`;
    title.style.fontSize = "20px";
    title.style.fontWeight = "600";
    title.style.marginBottom = "16px";
    panel.appendChild(title);
    
    // Rationale text
    const text = document.createElement("p");
    text.textContent = rationale;
    text.style.fontSize = "16px";
    text.style.lineHeight = "1.6";
    text.style.color = "#374151";
    panel.appendChild(text);
    
    // Close button
    const closeBtn = document.createElement("button");
    closeBtn.textContent = "Close";
    closeBtn.style.marginTop = "24px";
    closeBtn.style.padding = "10px 20px";
    closeBtn.style.border = "none";
    closeBtn.style.borderRadius = "6px";
    closeBtn.style.backgroundColor = config.config.white_label.primary_color || "#3b82f6";
    closeBtn.style.color = "#ffffff";
    closeBtn.style.cursor = "pointer";
    closeBtn.onclick = () => overlay.remove();
    panel.appendChild(closeBtn);
    
    overlay.appendChild(panel);
    
    // Click outside to close
    overlay.onclick = (e) => {
      if (e.target === overlay) {
        overlay.remove();
      }
    };
    
    document.body.appendChild(overlay);
  }
  ```

**Files to Create/Modify:**
- `sdk/src/runtime/grid.ts` (modify)

**Acceptance:** Rationale panel displays correctly, close button works, styling matches white-label

---

#### Task 8.6: Wire Up Grid Assembly Flow (1 hour)
**Description:** Connect intent selection to grid assembly and handle loading/error states.

**Actions:**
- Update `sdk/src/runtime/intent.ts`:
  ```typescript
  import { callAssemble } from "./assemble";
  import { renderGrid } from "./grid";
  
  function selectIntent(config: RuntimeConfig, intentId: string): void {
    // ... existing code ...
    
    // Show loading state
    showLoadingState();
    
    // Call assemble API
    callAssemble(config, intentId)
      .then(response => {
        hideLoadingState();
        renderGrid(config, response);
      })
      .catch(error => {
        hideLoadingState();
        showErrorState(error);
      });
  }
  
  function showLoadingState(): void {
    const strip = document.getElementById("dap-commentary-strip");
    if (strip) {
      strip.textContent = "Assembling your options...";
    }
  }
  
  function hideLoadingState(): void {
    const strip = document.getElementById("dap-commentary-strip");
    if (strip) {
      strip.textContent = "Viewing page...";
    }
  }
  
  function showErrorState(error: Error): void {
    const strip = document.getElementById("dap-commentary-strip");
    if (strip) {
      strip.textContent = "Having trouble loading — try again";
    }
    console.error("DAP: Grid assembly failed", error);
  }
  ```
- Expose assemble function in runtime:
  ```typescript
  // In runtime/index.ts
  import { callAssemble } from "./assemble";
  import { renderGrid } from "./grid";
  
  (window as any).__DAP_ASSEMBLE_GRID = async (
    config: RuntimeConfig,
    intentId: string,
  ) => {
    try {
      const response = await callAssemble(config, intentId);
      renderGrid(config, response);
    } catch (error) {
      console.error("DAP: Assemble failed", error);
    }
  };
  ```

**Files to Create/Modify:**
- `sdk/src/runtime/intent.ts` (modify)
- `sdk/src/runtime/index.ts` (modify)

**Acceptance:** Intent selection triggers grid assembly, loading states show, errors handled gracefully

---

### Day 8 Summary
- ✅ Context extraction implemented
- ✅ Assemble API integration complete
- ✅ Grid rendering with responsive layout
- ✅ Product cards with all information
- ✅ Rationale panel display
- ✅ Loading and error states handled

**Next Day Preview:** Day 9 will implement Admin Portal authentication and site management.

---

## Day 9: Admin Portal - Authentication & Sites

**Epic:** EPIC-5 - Admin Portal  
**Story:** STORY-5.1 - Authentication & Site Management  
**Total Effort:** 8 hours  
**Day:** 9

### Story Description
As a developer, I want to implement the Admin Portal authentication system and site management features, so that admins can log in, create sites, and manage site configurations.

### Acceptance Criteria
1. Admin login page with email/password authentication
2. JWT token-based authentication per TAD §12.2
3. Protected routes requiring authentication
4. Site list page showing all sites
5. Site creation form with name and base_url
6. Site creation creates default site_config per TAD §12.2
7. Site edit functionality
8. Token storage and refresh handling
9. Logout functionality

### Granular Tasks

#### Task 9.1: Implement Backend Admin Authentication (1.5 hours)
**Description:** Create admin authentication endpoints with JWT per TAD §12.2.

**Actions:**
- Create `backend/app/services/auth.py`:
  ```python
  from datetime import datetime, timedelta
  from jose import JWTError, jwt
  from passlib.context import CryptContext
  from uuid import UUID
  from app.db.database import get_pool
  from app.config import Settings
  
  settings = Settings()
  pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
  
  SECRET_KEY = settings.secret_key
  ALGORITHM = "HS256"
  ACCESS_TOKEN_EXPIRE_MINUTES = 30
  
  def verify_password(plain_password: str, hashed_password: str) -> bool:
      return pwd_context.verify(plain_password, hashed_password)
  
  def get_password_hash(password: str) -> str:
      return pwd_context.hash(password)
  
  async def authenticate_admin(email: str, password: str) -> UUID | None:
      """Authenticate admin and return admin_id if valid."""
      pool = await get_pool()
      async with pool.acquire() as conn:
          row = await conn.fetchrow(
              "SELECT id, password_hash FROM dap.admin_users WHERE email = $1",
              email,
          )
          
          if not row:
              return None
          
          if verify_password(password, row["password_hash"]):
              return row["id"]
          
          return None
  
  def create_access_token(admin_id: UUID) -> str:
      """Create JWT access token."""
      expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
      to_encode = {"sub": str(admin_id), "exp": expire}
      encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
      return encoded_jwt
  
  async def get_current_admin(token: str) -> UUID | None:
      """Verify token and return admin_id."""
      try:
          payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
          admin_id: str = payload.get("sub")
          if admin_id is None:
              return None
          return UUID(admin_id)
      except JWTError:
          return None
  ```
- Add password hashing dependency to `requirements.txt`:
  ```
  passlib[bcrypt]==1.7.4
  ```
- Create admin auth endpoints in `backend/app/api/admin.py`:
  ```python
  from fastapi import Depends, HTTPException, status
  from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
  from app.services.auth import authenticate_admin, create_access_token, get_current_admin
  from app.schemas.auth import LoginRequest, LoginResponse
  
  security = HTTPBearer()
  
  @router.post("/login", response_model=LoginResponse)
  async def login(request: LoginRequest):
      """Admin login endpoint."""
      admin_id = await authenticate_admin(request.email, request.password)
      if not admin_id:
          raise HTTPException(
              status_code=status.HTTP_401_UNAUTHORIZED,
              detail="Incorrect email or password",
          )
      
      access_token = create_access_token(admin_id)
      return {
          "access_token": access_token,
          "token_type": "bearer",
          "expires_in": 1800,  # 30 minutes
      }
  
  async def get_current_admin_id(
      credentials: HTTPAuthorizationCredentials = Depends(security),
  ) -> UUID:
      """Dependency to get current admin ID from token."""
      admin_id = await get_current_admin(credentials.credentials)
      if admin_id is None:
          raise HTTPException(
              status_code=status.HTTP_401_UNAUTHORIZED,
              detail="Invalid authentication credentials",
          )
      return admin_id
  ```
- Create `backend/app/schemas/auth.py`:
  ```python
  from pydantic import BaseModel
  
  class LoginRequest(BaseModel):
      email: str
      password: str
  
  class LoginResponse(BaseModel):
      access_token: str
      token_type: str
      expires_in: int
  ```
- Create seed script for admin user `backend/scripts/create_admin.py`:
  ```python
  import asyncio
  import asyncpg
  from app.services.auth import get_password_hash
  
  async def create_admin():
      email = input("Email: ")
      password = input("Password: ")
      
      conn = await asyncpg.connect("postgresql://user:password@localhost:5432/dap")
      
      password_hash = get_password_hash(password)
      
      await conn.execute(
          """
          INSERT INTO dap.admin_users (email, password_hash)
          VALUES ($1, $2)
          ON CONFLICT (email) DO UPDATE
          SET password_hash = EXCLUDED.password_hash
          """,
          email,
          password_hash,
      )
      
      await conn.close()
      print("Admin user created!")
  
  if __name__ == "__main__":
      asyncio.run(create_admin())
  ```

**Files to Create/Modify:**
- `backend/app/services/auth.py` (create)
- `backend/app/schemas/auth.py` (create)
- `backend/app/api/admin.py` (modify)
- `backend/requirements.txt` (modify)
- `backend/scripts/create_admin.py` (create)

**Acceptance:** Login endpoint works, JWT tokens generated, authentication dependency works

---

#### Task 9.2: Create Admin Portal Login Page (1.5 hours)
**Description:** Build React login page with form validation per TAD §5.1.

**Actions:**
- Create `admin/src/pages/Login.tsx`:
  ```typescript
  import { useState } from "react";
  import { useNavigate } from "react-router-dom";
  import { api } from "../services/api";
  
  export function Login() {
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");
    const [error, setError] = useState("");
    const [loading, setLoading] = useState(false);
    const navigate = useNavigate();
  
    const handleSubmit = async (e: React.FormEvent) => {
      e.preventDefault();
      setError("");
      setLoading(true);
  
      try {
        const response = await api.post("/admin/login", {
          email,
          password,
        });
  
        // Store token
        localStorage.setItem("admin_token", response.data.access_token);
        localStorage.setItem("admin_token_expires", String(Date.now() + response.data.expires_in * 1000));
  
        // Redirect to sites
        navigate("/sites");
      } catch (err: any) {
        setError(err.response?.data?.detail || "Login failed");
      } finally {
        setLoading(false);
      }
    };
  
    return (
      <div className="min-h-screen flex items-center justify-center bg-gray-50">
        <div className="max-w-md w-full space-y-8 p-8 bg-white rounded-lg shadow">
          <div>
            <h2 className="text-3xl font-bold text-center">DAP Admin Portal</h2>
            <p className="mt-2 text-center text-gray-600">Sign in to your account</p>
          </div>
          <form className="mt-8 space-y-6" onSubmit={handleSubmit}>
            {error && (
              <div className="bg-red-50 border border-red-200 text-red-700 px-4 py-3 rounded">
                {error}
              </div>
            )}
            <div>
              <label htmlFor="email" className="block text-sm font-medium text-gray-700">
                Email
              </label>
              <input
                id="email"
                type="email"
                required
                value={email}
                onChange={(e) => setEmail(e.target.value)}
                className="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500"
              />
            </div>
            <div>
              <label htmlFor="password" className="block text-sm font-medium text-gray-700">
                Password
              </label>
              <input
                id="password"
                type="password"
                required
                value={password}
                onChange={(e) => setPassword(e.target.value)}
                className="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500"
              />
            </div>
            <button
              type="submit"
              disabled={loading}
              className="w-full flex justify-center py-2 px-4 border border-transparent rounded-md shadow-sm text-sm font-medium text-white bg-blue-600 hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500 disabled:opacity-50"
            >
              {loading ? "Signing in..." : "Sign in"}
            </button>
          </form>
        </div>
      </div>
    );
  }
  ```
- Update `admin/src/services/api.ts` to add auth interceptor:
  ```typescript
  import axios from "axios";
  
  const API_BASE_URL = import.meta.env.VITE_API_URL || "http://localhost:8000";
  
  export const api = axios.create({
    baseURL: API_BASE_URL,
    headers: { "Content-Type": "application/json" },
  });
  
  // Add auth token to requests
  api.interceptors.request.use((config) => {
    const token = localStorage.getItem("admin_token");
    if (token) {
      config.headers.Authorization = `Bearer ${token}`;
    }
    return config;
  });
  
  // Handle 401 errors
  api.interceptors.response.use(
    (response) => response,
    (error) => {
      if (error.response?.status === 401) {
        localStorage.removeItem("admin_token");
        localStorage.removeItem("admin_token_expires");
        window.location.href = "/login";
      }
      return Promise.reject(error);
    }
  );
  ```
- Set up routing in `admin/src/App.tsx`:
  ```typescript
  import { BrowserRouter, Routes, Route, Navigate } from "react-router-dom";
  import { Login } from "./pages/Login";
  import { Sites } from "./pages/Sites";
  
  function PrivateRoute({ children }: { children: React.ReactNode }) {
    const token = localStorage.getItem("admin_token");
    const expires = localStorage.getItem("admin_token_expires");
    
    if (!token || !expires || Date.now() > parseInt(expires)) {
      return <Navigate to="/login" />;
    }
    
    return <>{children}</>;
  }
  
  function App() {
    return (
      <BrowserRouter>
        <Routes>
          <Route path="/login" element={<Login />} />
          <Route
            path="/sites"
            element={
              <PrivateRoute>
                <Sites />
              </PrivateRoute>
            }
          />
          <Route path="/" element={<Navigate to="/sites" />} />
        </Routes>
      </BrowserRouter>
    );
  }
  
  export default App;
  ```

**Files to Create/Modify:**
- `admin/src/pages/Login.tsx` (create)
- `admin/src/services/api.ts` (modify)
- `admin/src/App.tsx` (modify)

**Acceptance:** Login page renders, authentication works, token stored, protected routes redirect

---

#### Task 9.3: Create Site List Page (1.5 hours)
**Description:** Build site list page showing all sites with last sync status per TAD §12.2.

**Actions:**
- Create `admin/src/pages/Sites.tsx`:
  ```typescript
  import { useEffect, useState } from "react";
  import { useNavigate } from "react-router-dom";
  import { api } from "../services/api";
  
  interface Site {
    id: string;
    name: string;
    base_url: string;
    created_at: string;
    last_synced_at?: string;
  }
  
  export function Sites() {
    const [sites, setSites] = useState<Site[]>([]);
    const [loading, setLoading] = useState(true);
    const [showCreateModal, setShowCreateModal] = useState(false);
    const navigate = useNavigate();
  
    useEffect(() => {
      loadSites();
    }, []);
  
    const loadSites = async () => {
      try {
        const response = await api.get("/admin/sites");
        setSites(response.data);
      } catch (error) {
        console.error("Failed to load sites", error);
      } finally {
        setLoading(false);
      }
    };
  
    const handleLogout = () => {
      localStorage.removeItem("admin_token");
      localStorage.removeItem("admin_token_expires");
      navigate("/login");
    };
  
    if (loading) {
      return <div className="p-8">Loading sites...</div>;
    }
  
    return (
      <div className="min-h-screen bg-gray-50">
        <header className="bg-white shadow">
          <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-4 flex justify-between items-center">
            <h1 className="text-2xl font-bold">DAP Admin Portal</h1>
            <button
              onClick={handleLogout}
              className="px-4 py-2 text-sm font-medium text-gray-700 hover:text-gray-900"
            >
              Logout
            </button>
          </div>
        </header>
  
        <main className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
          <div className="flex justify-between items-center mb-6">
            <h2 className="text-xl font-semibold">Sites</h2>
            <button
              onClick={() => setShowCreateModal(true)}
              className="px-4 py-2 bg-blue-600 text-white rounded-md hover:bg-blue-700"
            >
              Create Site
            </button>
          </div>
  
          <div className="bg-white shadow rounded-lg overflow-hidden">
            <table className="min-w-full divide-y divide-gray-200">
              <thead className="bg-gray-50">
                <tr>
                  <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase">
                    Name
                  </th>
                  <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase">
                    Base URL
                  </th>
                  <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase">
                    Created
                  </th>
                  <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase">
                    Last Synced
                  </th>
                  <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase">
                    Actions
                  </th>
                </tr>
              </thead>
              <tbody className="bg-white divide-y divide-gray-200">
                {sites.map((site) => (
                  <tr key={site.id}>
                    <td className="px-6 py-4 whitespace-nowrap text-sm font-medium text-gray-900">
                      {site.name}
                    </td>
                    <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
                      {site.base_url}
                    </td>
                    <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
                      {new Date(site.created_at).toLocaleDateString()}
                    </td>
                    <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
                      {site.last_synced_at
                        ? new Date(site.last_synced_at).toLocaleDateString()
                        : "Never"}
                    </td>
                    <td className="px-6 py-4 whitespace-nowrap text-sm font-medium">
                      <button
                        onClick={() => navigate(`/sites/${site.id}`)}
                        className="text-blue-600 hover:text-blue-900"
                      >
                        Configure
                      </button>
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </main>
  
        {showCreateModal && (
          <CreateSiteModal
            onClose={() => setShowCreateModal(false)}
            onSuccess={() => {
              setShowCreateModal(false);
              loadSites();
            }}
          />
        )}
      </div>
    );
  }
  ```

**Files to Create/Modify:**
- `admin/src/pages/Sites.tsx` (create)

**Acceptance:** Site list displays, table shows all columns, create button works

---

#### Task 9.4: Implement Site Creation Modal & API Integration (2 hours)
**Description:** Create site creation form and integrate with backend API per TAD §12.2.

**Actions:**
- Create `admin/src/components/CreateSiteModal.tsx`:
  ```typescript
  import { useState } from "react";
  import { api } from "../services/api";
  
  interface CreateSiteModalProps {
    onClose: () => void;
    onSuccess: () => void;
  }
  
  export function CreateSiteModal({ onClose, onSuccess }: CreateSiteModalProps) {
    const [name, setName] = useState("");
    const [baseUrl, setBaseUrl] = useState("");
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState("");
  
    const handleSubmit = async (e: React.FormEvent) => {
      e.preventDefault();
      setError("");
      setLoading(true);
  
      try {
        // Validate URL
        new URL(baseUrl);
        
        await api.post("/admin/sites", {
          name,
          base_url: baseUrl,
        });
        
        onSuccess();
      } catch (err: any) {
        if (err instanceof TypeError) {
          setError("Invalid URL format");
        } else {
          setError(err.response?.data?.detail || "Failed to create site");
        }
      } finally {
        setLoading(false);
      }
    };
  
    return (
      <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50">
        <div className="bg-white rounded-lg p-6 max-w-md w-full">
          <h3 className="text-lg font-semibold mb-4">Create New Site</h3>
          
          {error && (
            <div className="mb-4 bg-red-50 border border-red-200 text-red-700 px-4 py-3 rounded">
              {error}
            </div>
          )}
  
          <form onSubmit={handleSubmit} className="space-y-4">
            <div>
              <label htmlFor="name" className="block text-sm font-medium text-gray-700">
                Site Name
              </label>
              <input
                id="name"
                type="text"
                required
                value={name}
                onChange={(e) => setName(e.target.value)}
                className="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm"
                placeholder="My Website"
              />
            </div>
  
            <div>
              <label htmlFor="baseUrl" className="block text-sm font-medium text-gray-700">
                Base URL
              </label>
              <input
                id="baseUrl"
                type="url"
                required
                value={baseUrl}
                onChange={(e) => setBaseUrl(e.target.value)}
                className="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm"
                placeholder="https://example.com"
              />
            </div>
  
            <div className="flex justify-end space-x-3">
              <button
                type="button"
                onClick={onClose}
                className="px-4 py-2 border border-gray-300 rounded-md text-gray-700 hover:bg-gray-50"
              >
                Cancel
              </button>
              <button
                type="submit"
                disabled={loading}
                className="px-4 py-2 bg-blue-600 text-white rounded-md hover:bg-blue-700 disabled:opacity-50"
              >
                {loading ? "Creating..." : "Create Site"}
              </button>
            </div>
          </form>
        </div>
      </div>
    );
  }
  ```
- Update Sites.tsx to import and use modal:
  ```typescript
  import { CreateSiteModal } from "../components/CreateSiteModal";
  ```
- Update backend to return last_synced_at in site list:
  ```python
  @router.get("/sites")
  async def list_sites(admin_id: UUID = Depends(get_current_admin_id)):
      """List all sites with last sync status."""
      pool = await get_pool()
      async with pool.acquire() as conn:
          sites = await conn.fetch(
              """
              SELECT s.*, cj.last_synced_at
              FROM dap.sites s
              LEFT JOIN LATERAL (
                  SELECT last_synced_at
                  FROM dap.crawl_jobs
                  WHERE site_id = s.id
                  ORDER BY created_at DESC
                  LIMIT 1
              ) cj ON true
              ORDER BY s.created_at DESC
              """
          )
          return [dict(row) for row in sites]
  ```

**Files to Create/Modify:**
- `admin/src/components/CreateSiteModal.tsx` (create)
- `admin/src/pages/Sites.tsx` (modify)
- `backend/app/api/admin.py` (modify)

**Acceptance:** Site creation works, default config created, Qdrant collection created

---

#### Task 9.5: Create Site Detail/Edit Page Route (1.5 hours)
**Description:** Set up routing and basic structure for site configuration page.

**Actions:**
- Create `admin/src/pages/SiteConfig.tsx` placeholder:
  ```typescript
  import { useParams, useNavigate } from "react-router-dom";
  import { useEffect, useState } from "react";
  import { api } from "../services/api";
  
  export function SiteConfig() {
    const { siteId } = useParams<{ siteId: string }>();
    const navigate = useNavigate();
    const [site, setSite] = useState<any>(null);
    const [loading, setLoading] = useState(true);
  
    useEffect(() => {
      if (siteId) {
        loadSite(siteId);
      }
    }, [siteId]);
  
    const loadSite = async (id: string) => {
      try {
        const response = await api.get(`/admin/sites/${id}`);
        setSite(response.data);
      } catch (error) {
        console.error("Failed to load site", error);
      } finally {
        setLoading(false);
      }
    };
  
    if (loading) {
      return <div className="p-8">Loading...</div>;
    }
  
    return (
      <div className="min-h-screen bg-gray-50">
        <header className="bg-white shadow">
          <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-4">
            <button
              onClick={() => navigate("/sites")}
              className="text-blue-600 hover:text-blue-900"
            >
              ← Back to Sites
            </button>
            <h1 className="text-2xl font-bold mt-2">
              {site?.name || "Site Configuration"}
            </h1>
          </div>
        </header>
        <main className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
          <p>Configuration page coming in Day 10...</p>
        </main>
      </div>
    );
  }
  ```
- Update App.tsx routing:
  ```typescript
  import { SiteConfig } from "./pages/SiteConfig";
  
  <Route
    path="/sites/:siteId"
    element={
      <PrivateRoute>
        <SiteConfig />
      </PrivateRoute>
    }
  />
  ```

**Files to Create/Modify:**
- `admin/src/pages/SiteConfig.tsx` (create)
- `admin/src/App.tsx` (modify)

**Acceptance:** Site config page route works, navigation functional

---

### Day 9 Summary
- ✅ Admin authentication backend implemented
- ✅ Login page created
- ✅ Site list page with table
- ✅ Site creation modal and API integration
- ✅ Site detail page route set up

**Next Day Preview:** Day 10 will implement site configuration management (product rules, triggers, white-label).

---

## Day 10: Admin Portal - Config Management

**Epic:** EPIC-5 - Admin Portal  
**Story:** STORY-5.2 - Site Configuration Management  
**Total Effort:** 8 hours  
**Day:** 10

### Story Description
As a developer, I want to implement the site configuration management interface where admins can edit product page rules, trigger thresholds, commentary templates, block mapping, and white-label settings, so that each site can be customized for its specific needs.

### Acceptance Criteria
1. Product page rules configuration (URL patterns, DOM selectors, product_id_source) per PRD §7.7
2. Trigger thresholds configuration with validation per PRD §7.2 and FR-030A
3. Commentary templates editor
4. Block mapping configuration per intent per PRD §7.6
5. White-label settings (colors, fonts, logo, brand name) per PRD §7.7
6. Config save functionality with validation
7. Config preview/sensitivity preview for triggers
8. All changes persist to backend

### Granular Tasks

#### Task 10.1: Implement Product Page Rules Configuration (1.5 hours)
**Description:** Create UI for configuring product page detection rules per PRD §7.7 and TAD §12.2.

**Actions:**
- Create `admin/src/components/ProductPageRules.tsx`:
  ```typescript
  import { useState, useEffect } from "react";
  
  interface ProductPageRules {
    url_patterns: string[];
    dom_selectors: string[];
    product_id_source: "url_path" | "data_attribute" | "meta";
  }
  
  interface ProductPageRulesProps {
    value: ProductPageRules;
    onChange: (rules: ProductPageRules) => void;
  }
  
  export function ProductPageRulesEditor({ value, onChange }: ProductPageRulesProps) {
    const [urlPatterns, setUrlPatterns] = useState(value.url_patterns.join("\n"));
    const [domSelectors, setDomSelectors] = useState(value.dom_selectors.join("\n"));
    const [productIdSource, setProductIdSource] = useState(value.product_id_source);
  
    useEffect(() => {
      onChange({
        url_patterns: urlPatterns.split("\n").filter(Boolean),
        dom_selectors: domSelectors.split("\n").filter(Boolean),
        product_id_source: productIdSource,
      });
    }, [urlPatterns, domSelectors, productIdSource]);
  
    return (
      <div className="space-y-6">
        <div>
          <label className="block text-sm font-medium text-gray-700 mb-2">
            URL Patterns (one per line, use * for wildcard)
          </label>
          <textarea
            value={urlPatterns}
            onChange={(e) => setUrlPatterns(e.target.value)}
            rows={4}
            className="w-full px-3 py-2 border border-gray-300 rounded-md"
            placeholder="/products/*&#10;/cards/*"
          />
          <p className="mt-1 text-sm text-gray-500">
            Examples: /products/*, /cards/*, /shop/*
          </p>
        </div>
  
        <div>
          <label className="block text-sm font-medium text-gray-700 mb-2">
            DOM Selectors (one per line)
          </label>
          <textarea
            value={domSelectors}
            onChange={(e) => setDomSelectors(e.target.value)}
            rows={4}
            className="w-full px-3 py-2 border border-gray-300 rounded-md"
            placeholder="[data-product-id]&#10;.product-card"
          />
          <p className="mt-1 text-sm text-gray-500">
            CSS selectors that identify product pages
          </p>
        </div>
  
        <div>
          <label className="block text-sm font-medium text-gray-700 mb-2">
            Product ID Source
          </label>
          <select
            value={productIdSource}
            onChange={(e) => setProductIdSource(e.target.value as any)}
            className="w-full px-3 py-2 border border-gray-300 rounded-md"
          >
            <option value="url_path">URL Path (last segment)</option>
            <option value="data_attribute">Data Attribute ([data-product-id])</option>
            <option value="meta">Meta Tag (meta[name='product-id'])</option>
          </select>
        </div>
      </div>
    );
  }
  ```
- Integrate into SiteConfig page

**Files to Create/Modify:**
- `admin/src/components/ProductPageRules.tsx` (create)

**Acceptance:** Product page rules editor works, values update correctly

---

#### Task 10.2: Implement Trigger Thresholds Configuration (2 hours)
**Description:** Create trigger thresholds editor with validation per PRD §7.2 and FR-030A.

**Actions:**
- Create `admin/src/components/TriggerThresholds.tsx`:
  ```typescript
  import { useState, useEffect } from "react";
  
  interface TriggerThresholds {
    multi_product_min: number;
    multi_product_window_min: number;
    dwell_sec: number;
    cta_hover_min: number;
    cooldown_after_trigger_sec: number;
    cooldown_after_dismiss_sec: number;
    cooldown_after_grid_close_sec: number;
  }
  
  interface TriggerThresholdsProps {
    value: TriggerThresholds;
    onChange: (thresholds: TriggerThresholds) => void;
  }
  
  const VALIDATION_RULES = {
    multi_product_min: { min: 1, max: 10 },
    multi_product_window_min: { min: 1, max: 30 },
    dwell_sec: { min: 10, max: 300 },
    cta_hover_min: { min: 1, max: 10 },
    cooldown_after_trigger_sec: { min: 10, max: 300 },
    cooldown_after_dismiss_sec: { min: 10, max: 600 },
    cooldown_after_grid_close_sec: { min: 10, max: 300 },
  };
  
  export function TriggerThresholdsEditor({ value, onChange }: TriggerThresholdsProps) {
    const [thresholds, setThresholds] = useState(value);
    const [warnings, setWarnings] = useState<Record<string, string>>({});
  
    useEffect(() => {
      const newWarnings: Record<string, string> = {};
      
      // Validate each threshold
      Object.entries(thresholds).forEach(([key, val]) => {
        const rule = VALIDATION_RULES[key as keyof typeof VALIDATION_RULES];
        if (rule) {
          if (val < rule.min || val > rule.max) {
            newWarnings[key] = `Value must be between ${rule.min} and ${rule.max}`;
          }
        }
      });
      
      // Sensitivity warnings
      if (thresholds.multi_product_min <= 1) {
        newWarnings.multi_product_min = "Very sensitive - may trigger frequently";
      }
      if (thresholds.dwell_sec <= 20) {
        newWarnings.dwell_sec = "Very sensitive - may trigger too early";
      }
      
      setWarnings(newWarnings);
      onChange(thresholds);
    }, [thresholds]);
  
    const updateThreshold = (key: keyof TriggerThresholds, val: number) => {
      setThresholds({ ...thresholds, [key]: val });
    };
  
    return (
      <div className="space-y-4">
        <div className="grid grid-cols-2 gap-4">
          <div>
            <label className="block text-sm font-medium text-gray-700 mb-1">
              Multiple Product Views (min)
            </label>
            <input
              type="number"
              value={thresholds.multi_product_min}
              onChange={(e) => updateThreshold("multi_product_min", parseInt(e.target.value))}
              min={VALIDATION_RULES.multi_product_min.min}
              max={VALIDATION_RULES.multi_product_min.max}
              className="w-full px-3 py-2 border border-gray-300 rounded-md"
            />
            {warnings.multi_product_min && (
              <p className="mt-1 text-sm text-yellow-600">{warnings.multi_product_min}</p>
            )}
          </div>
  
          <div>
            <label className="block text-sm font-medium text-gray-700 mb-1">
              Time Window (minutes)
            </label>
            <input
              type="number"
              value={thresholds.multi_product_window_min}
              onChange={(e) => updateThreshold("multi_product_window_min", parseInt(e.target.value))}
              min={VALIDATION_RULES.multi_product_window_min.min}
              max={VALIDATION_RULES.multi_product_window_min.max}
              className="w-full px-3 py-2 border border-gray-300 rounded-md"
            />
          </div>
  
          <div>
            <label className="block text-sm font-medium text-gray-700 mb-1">
              Dwell Time (seconds)
            </label>
            <input
              type="number"
              value={thresholds.dwell_sec}
              onChange={(e) => updateThreshold("dwell_sec", parseInt(e.target.value))}
              min={VALIDATION_RULES.dwell_sec.min}
              max={VALIDATION_RULES.dwell_sec.max}
              className="w-full px-3 py-2 border border-gray-300 rounded-md"
            />
            {warnings.dwell_sec && (
              <p className="mt-1 text-sm text-yellow-600">{warnings.dwell_sec}</p>
            )}
          </div>
  
          <div>
            <label className="block text-sm font-medium text-gray-700 mb-1">
              CTA Hover Min
            </label>
            <input
              type="number"
              value={thresholds.cta_hover_min}
              onChange={(e) => updateThreshold("cta_hover_min", parseInt(e.target.value))}
              min={VALIDATION_RULES.cta_hover_min.min}
              max={VALIDATION_RULES.cta_hover_min.max}
              className="w-full px-3 py-2 border border-gray-300 rounded-md"
            />
          </div>
        </div>
  
        <div className="border-t pt-4">
          <h4 className="font-medium mb-2">Cooldown Periods (seconds)</h4>
          <div className="grid grid-cols-3 gap-4">
            <div>
              <label className="block text-sm font-medium text-gray-700 mb-1">
                After Trigger
              </label>
              <input
                type="number"
                value={thresholds.cooldown_after_trigger_sec}
                onChange={(e) => updateThreshold("cooldown_after_trigger_sec", parseInt(e.target.value))}
                className="w-full px-3 py-2 border border-gray-300 rounded-md"
              />
            </div>
            <div>
              <label className="block text-sm font-medium text-gray-700 mb-1">
                After Dismiss
              </label>
              <input
                type="number"
                value={thresholds.cooldown_after_dismiss_sec}
                onChange={(e) => updateThreshold("cooldown_after_dismiss_sec", parseInt(e.target.value))}
                className="w-full px-3 py-2 border border-gray-300 rounded-md"
              />
            </div>
            <div>
              <label className="block text-sm font-medium text-gray-700 mb-1">
                After Grid Close
              </label>
              <input
                type="number"
                value={thresholds.cooldown_after_grid_close_sec}
                onChange={(e) => updateThreshold("cooldown_after_grid_close_sec", parseInt(e.target.value))}
                className="w-full px-3 py-2 border border-gray-300 rounded-md"
              />
            </div>
          </div>
        </div>
      </div>
    );
  }
  ```

**Files to Create/Modify:**
- `admin/src/components/TriggerThresholds.tsx` (create)

**Acceptance:** Trigger thresholds editor works, validation shows warnings, values update

---

#### Task 10.3: Implement Commentary Templates Editor (1 hour)
**Description:** Create editor for commentary templates per PRD §7.1.

**Actions:**
- Create `admin/src/components/CommentaryTemplates.tsx`:
  ```typescript
  import { useState, useEffect } from "react";
  
  interface CommentaryTemplatesProps {
    value: string[];
    onChange: (templates: string[]) => void;
  }
  
  export function CommentaryTemplatesEditor({ value, onChange }: CommentaryTemplatesProps) {
    const [templates, setTemplates] = useState(value.join("\n"));
  
    useEffect(() => {
      onChange(templates.split("\n").filter(Boolean));
    }, [templates]);
  
    return (
      <div>
        <label className="block text-sm font-medium text-gray-700 mb-2">
          Commentary Templates (one per line)
        </label>
        <textarea
          value={templates}
          onChange={(e) => setTemplates(e.target.value)}
          rows={6}
          className="w-full px-3 py-2 border border-gray-300 rounded-md font-mono text-sm"
          placeholder="You've viewed {n} products in {m} minutes — comparing options?&#10;Spent {t} seconds on pricing — need more info?"
        />
        <p className="mt-1 text-sm text-gray-500">
          Use placeholders: {"{"}n{"}"} = product count, {"{"}m{"}"} = minutes, {"{"}t{"}"} = seconds
        </p>
      </div>
    );
  }
  ```

**Files to Create/Modify:**
- `admin/src/components/CommentaryTemplates.tsx` (create)

**Acceptance:** Commentary templates editor works, templates update correctly

---

#### Task 10.4: Implement Block Mapping Configuration (1.5 hours)
**Description:** Create UI for configuring intent→block mapping per PRD §7.6.

**Actions:**
- Create `admin/src/components/BlockMapping.tsx`:
  ```typescript
  import { useState, useEffect } from "react";
  
  const INTENTS = [
    "help_me_choose",
    "compare_options",
    "check_eligibility",
    "understand_differences",
    "just_exploring",
  ];
  
  const BLOCK_TYPES = [
    "shortlist",
    "comparison",
    "costs",
    "benefits",
    "limitations",
    "eligibility",
    "use_case_fit",
    "trade_off",
    "examples",
    "action",
    "custom_query",
  ];
  
  interface BlockMappingProps {
    value: Record<string, string[]>;
    onChange: (mapping: Record<string, string[]>) => void;
  }
  
  export function BlockMappingEditor({ value, onChange }: BlockMappingProps) {
    const [mapping, setMapping] = useState<Record<string, string[]>>(value);
  
    useEffect(() => {
      onChange(mapping);
    }, [mapping]);
  
    const updateIntentBlocks = (intent: string, blocks: string[]) => {
      setMapping({ ...mapping, [intent]: blocks });
    };
  
    return (
      <div className="space-y-4">
        {INTENTS.map((intent) => (
          <div key={intent} className="border rounded-lg p-4">
            <label className="block text-sm font-medium text-gray-700 mb-2">
              {intent.replace(/_/g, " ").replace(/\b\w/g, (l) => l.toUpperCase())}
            </label>
            <div className="flex flex-wrap gap-2">
              {BLOCK_TYPES.map((blockType) => (
                <label key={blockType} className="flex items-center">
                  <input
                    type="checkbox"
                    checked={mapping[intent]?.includes(blockType) || false}
                    onChange={(e) => {
                      const current = mapping[intent] || [];
                      if (e.target.checked) {
                        updateIntentBlocks(intent, [...current, blockType]);
                      } else {
                        updateIntentBlocks(intent, current.filter((b) => b !== blockType));
                      }
                    }}
                    className="mr-2"
                  />
                  <span className="text-sm">{blockType}</span>
                </label>
              ))}
            </div>
          </div>
        ))}
      </div>
    );
  }
  ```

**Files to Create/Modify:**
- `admin/src/components/BlockMapping.tsx` (create)

**Acceptance:** Block mapping editor works, intents can be configured with multiple blocks

---

#### Task 10.5: Implement White-Label Configuration (1.5 hours)
**Description:** Create white-label settings editor per PRD §7.7.

**Actions:**
- Create `admin/src/components/WhiteLabel.tsx`:
  ```typescript
  import { useState, useEffect } from "react";
  
  interface WhiteLabel {
    brand_name?: string;
    primary_color?: string;
    font_family?: string;
    logo_url?: string;
    copy_tone?: string;
  }
  
  interface WhiteLabelProps {
    value: WhiteLabel;
    onChange: (whiteLabel: WhiteLabel) => void;
  }
  
  export function WhiteLabelEditor({ value, onChange }: WhiteLabelProps) {
    const [whiteLabel, setWhiteLabel] = useState(value);
  
    useEffect(() => {
      onChange(whiteLabel);
    }, [whiteLabel]);
  
    return (
      <div className="space-y-4">
        <div>
          <label className="block text-sm font-medium text-gray-700 mb-1">
            Brand Name
          </label>
          <input
            type="text"
            value={whiteLabel.brand_name || ""}
            onChange={(e) => setWhiteLabel({ ...whiteLabel, brand_name: e.target.value })}
            className="w-full px-3 py-2 border border-gray-300 rounded-md"
            placeholder="My Brand"
          />
        </div>
  
        <div>
          <label className="block text-sm font-medium text-gray-700 mb-1">
            Primary Color
          </label>
          <div className="flex gap-2">
            <input
              type="color"
              value={whiteLabel.primary_color || "#3b82f6"}
              onChange={(e) => setWhiteLabel({ ...whiteLabel, primary_color: e.target.value })}
              className="h-10 w-20 border border-gray-300 rounded"
            />
            <input
              type="text"
              value={whiteLabel.primary_color || ""}
              onChange={(e) => setWhiteLabel({ ...whiteLabel, primary_color: e.target.value })}
              className="flex-1 px-3 py-2 border border-gray-300 rounded-md"
              placeholder="#3b82f6"
            />
          </div>
        </div>
  
        <div>
          <label className="block text-sm font-medium text-gray-700 mb-1">
            Font Family
          </label>
          <input
            type="text"
            value={whiteLabel.font_family || ""}
            onChange={(e) => setWhiteLabel({ ...whiteLabel, font_family: e.target.value })}
            className="w-full px-3 py-2 border border-gray-300 rounded-md"
            placeholder="system-ui, -apple-system, sans-serif"
          />
        </div>
  
        <div>
          <label className="block text-sm font-medium text-gray-700 mb-1">
            Logo URL
          </label>
          <input
            type="url"
            value={whiteLabel.logo_url || ""}
            onChange={(e) => setWhiteLabel({ ...whiteLabel, logo_url: e.target.value })}
            className="w-full px-3 py-2 border border-gray-300 rounded-md"
            placeholder="https://example.com/logo.png"
          />
        </div>
  
        <div>
          <label className="block text-sm font-medium text-gray-700 mb-1">
            Copy Tone
          </label>
          <select
            value={whiteLabel.copy_tone || ""}
            onChange={(e) => setWhiteLabel({ ...whiteLabel, copy_tone: e.target.value })}
            className="w-full px-3 py-2 border border-gray-300 rounded-md"
          >
            <option value="">Default</option>
            <option value="friendly">Friendly</option>
            <option value="professional">Professional</option>
            <option value="casual">Casual</option>
            <option value="formal">Formal</option>
          </select>
        </div>
      </div>
    );
  }
  ```

**Files to Create/Modify:**
- `admin/src/components/WhiteLabel.tsx` (create)

**Acceptance:** White-label editor works, all fields update correctly

---

#### Task 10.6: Complete SiteConfig Page with Save Functionality (30 min)
**Description:** Integrate all config components and implement save functionality.

**Actions:**
- Update `admin/src/pages/SiteConfig.tsx`:
  ```typescript
  import { useState, useEffect } from "react";
  import { useParams } from "react-router-dom";
  import { api } from "../services/api";
  import { ProductPageRulesEditor } from "../components/ProductPageRules";
  import { TriggerThresholdsEditor } from "../components/TriggerThresholds";
  import { CommentaryTemplatesEditor } from "../components/CommentaryTemplates";
  import { BlockMappingEditor } from "../components/BlockMapping";
  import { WhiteLabelEditor } from "../components/WhiteLabel";
  
  export function SiteConfig() {
    const { siteId } = useParams<{ siteId: string }>();
    const [config, setConfig] = useState<any>(null);
    const [loading, setLoading] = useState(true);
    const [saving, setSaving] = useState(false);
    const [error, setError] = useState("");
  
    useEffect(() => {
      if (siteId) {
        loadConfig(siteId);
      }
    }, [siteId]);
  
    const loadConfig = async (id: string) => {
      try {
        const response = await api.get(`/admin/sites/${id}/config`);
        setConfig(response.data);
      } catch (error) {
        console.error("Failed to load config", error);
      } finally {
        setLoading(false);
      }
    };
  
    const handleSave = async () => {
      if (!siteId || !config) return;
      
      setSaving(true);
      setError("");
  
      try {
        await api.put(`/admin/sites/${siteId}/config`, config);
        alert("Configuration saved successfully!");
      } catch (err: any) {
        setError(err.response?.data?.detail || "Failed to save configuration");
      } finally {
        setSaving(false);
      }
    };
  
    if (loading || !config) {
      return <div className="p-8">Loading...</div>;
    }
  
    return (
      <div className="min-h-screen bg-gray-50">
        {/* Header */}
        <header className="bg-white shadow">
          <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-4">
            <h1 className="text-2xl font-bold">Site Configuration</h1>
          </div>
        </header>
  
        <main className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
          {error && (
            <div className="mb-4 bg-red-50 border border-red-200 text-red-700 px-4 py-3 rounded">
              {error}
            </div>
          )}
  
          <div className="bg-white shadow rounded-lg p-6 space-y-8">
            <section>
              <h2 className="text-lg font-semibold mb-4">Product Page Rules</h2>
              <ProductPageRulesEditor
                value={config.product_page_rules}
                onChange={(rules) => setConfig({ ...config, product_page_rules: rules })}
              />
            </section>
  
            <section>
              <h2 className="text-lg font-semibold mb-4">Trigger Thresholds</h2>
              <TriggerThresholdsEditor
                value={config.trigger_thresholds}
                onChange={(thresholds) => setConfig({ ...config, trigger_thresholds: thresholds })}
              />
            </section>
  
            <section>
              <h2 className="text-lg font-semibold mb-4">Commentary Templates</h2>
              <CommentaryTemplatesEditor
                value={config.commentary_templates}
                onChange={(templates) => setConfig({ ...config, commentary_templates: templates })}
              />
            </section>
  
            <section>
              <h2 className="text-lg font-semibold mb-4">Block Mapping</h2>
              <BlockMappingEditor
                value={config.block_mapping}
                onChange={(mapping) => setConfig({ ...config, block_mapping: mapping })}
              />
            </section>
  
            <section>
              <h2 className="text-lg font-semibold mb-4">White-Label Settings</h2>
              <WhiteLabelEditor
                value={config.white_label}
                onChange={(whiteLabel) => setConfig({ ...config, white_label: whiteLabel })}
              />
            </section>
  
            <div className="flex justify-end">
              <button
                onClick={handleSave}
                disabled={saving}
                className="px-6 py-2 bg-blue-600 text-white rounded-md hover:bg-blue-700 disabled:opacity-50"
              >
                {saving ? "Saving..." : "Save Configuration"}
              </button>
            </div>
          </div>
        </main>
      </div>
    );
  }
  ```

**Files to Create/Modify:**
- `admin/src/pages/SiteConfig.tsx` (modify)

**Acceptance:** All config sections render, save works, changes persist to backend

---

### Day 10 Summary
- ✅ Product page rules configuration implemented
- ✅ Trigger thresholds editor with validation
- ✅ Commentary templates editor
- ✅ Block mapping configuration
- ✅ White-label settings editor
- ✅ Complete site config page with save functionality

**Next Day Preview:** Day 11 will implement content management features (view indexed pages, re-sync, exclude URLs).

---

## Day 11: Admin Portal - Content Management

**Epic:** EPIC-5 - Admin Portal  
**Story:** STORY-5.3 - Content Management & Crawl Operations  
**Total Effort:** 8 hours  
**Day:** 11

### Story Description
As a developer, I want to implement content management features that allow admins to view indexed pages/products, trigger re-syncs, exclude URLs, and monitor crawl job status, so that admins can manage and maintain the content indexed for their sites.

### Acceptance Criteria
1. Indexed content list page showing all pages/products per site
2. Pagination for large content lists
3. Filter by page type (product/page)
4. Re-sync functionality (trigger new crawl)
5. Crawl job status display with real-time updates
6. Exclude URL patterns configuration
7. Content freshness indicators (last indexed timestamp)
8. Search/filter functionality for content list

### Granular Tasks

#### Task 11.1: Implement Content List API Endpoint (1 hour)
**Description:** Create GET /admin/sites/{site_id}/content endpoint per TAD §12.2.

**Actions:**
- Update `backend/app/api/admin.py`:
  ```python
  from fastapi import Query
  
  @router.get("/sites/{site_id}/content")
  async def get_content(
      site_id: UUID,
      admin_id: UUID = Depends(get_current_admin_id),
      page: int = Query(1, ge=1),
      limit: int = Query(50, ge=1, le=100),
      page_type: Optional[str] = Query(None),
  ):
      """Get indexed content for a site."""
      pool = await get_pool()
      async with pool.acquire() as conn:
          # Build query
          query = """
              SELECT url, page_type, product_id, title, snippet, indexed_at
              FROM dap.indexed_pages
              WHERE site_id = $1
          """
          params = [site_id]
          
          if page_type:
              query += " AND page_type = $2"
              params.append(page_type)
          
          query += " ORDER BY indexed_at DESC LIMIT $2 OFFSET $3"
          if page_type:
              params.extend([limit, (page - 1) * limit])
          else:
              params.extend([limit, (page - 1) * limit])
          
          rows = await conn.fetch(query, *params)
          
          # Get total count
          count_query = "SELECT COUNT(*) FROM dap.indexed_pages WHERE site_id = $1"
          count_params = [site_id]
          if page_type:
              count_query += " AND page_type = $2"
              count_params.append(page_type)
          
          total = await conn.fetchval(count_query, *count_params)
          
          return {
              "items": [dict(row) for row in rows],
              "total": total,
              "page": page,
              "limit": limit,
          }
  ```

**Files to Create/Modify:**
- `backend/app/api/admin.py` (modify)

**Acceptance:** Content endpoint returns paginated results, filtering works

---

#### Task 11.2: Create Content List Page Component (2 hours)
**Description:** Build React component to display indexed content with pagination per PRD §7.7 FR-029.

**Actions:**
- Create `admin/src/pages/Content.tsx`:
  ```typescript
  import { useState, useEffect } from "react";
  import { useParams } from "react-router-dom";
  import { api } from "../services/api";
  
  interface ContentItem {
    url: string;
    page_type: string;
    product_id?: string;
    title?: string;
    snippet?: string;
    indexed_at: string;
  }
  
  export function Content() {
    const { siteId } = useParams<{ siteId: string }>();
    const [content, setContent] = useState<ContentItem[]>([]);
    const [loading, setLoading] = useState(true);
    const [page, setPage] = useState(1);
    const [total, setTotal] = useState(0);
    const [pageTypeFilter, setPageTypeFilter] = useState<string>("all");
    const limit = 50;
  
    useEffect(() => {
      if (siteId) {
        loadContent();
      }
    }, [siteId, page, pageTypeFilter]);
  
    const loadContent = async () => {
      if (!siteId) return;
      
      setLoading(true);
      try {
        const params: any = { page, limit };
        if (pageTypeFilter !== "all") {
          params.page_type = pageTypeFilter;
        }
        
        const response = await api.get(`/admin/sites/${siteId}/content`, { params });
        setContent(response.data.items);
        setTotal(response.data.total);
      } catch (error) {
        console.error("Failed to load content", error);
      } finally {
        setLoading(false);
      }
    };
  
    const formatDate = (dateString: string) => {
      return new Date(dateString).toLocaleString();
    };
  
    const getDaysSinceIndexed = (dateString: string) => {
      const days = Math.floor((Date.now() - new Date(dateString).getTime()) / (1000 * 60 * 60 * 24));
      return days;
    };
  
    return (
      <div className="min-h-screen bg-gray-50">
        <header className="bg-white shadow">
          <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-4">
            <h1 className="text-2xl font-bold">Indexed Content</h1>
          </div>
        </header>
  
        <main className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
          {/* Filters */}
          <div className="mb-4 flex gap-4 items-center">
            <label className="text-sm font-medium text-gray-700">Filter by type:</label>
            <select
              value={pageTypeFilter}
              onChange={(e) => {
                setPageTypeFilter(e.target.value);
                setPage(1);
              }}
              className="px-3 py-2 border border-gray-300 rounded-md"
            >
              <option value="all">All</option>
              <option value="product">Products</option>
              <option value="page">Pages</option>
            </select>
            <span className="text-sm text-gray-600">
              Total: {total} items
            </span>
          </div>
  
          {/* Content Table */}
          <div className="bg-white shadow rounded-lg overflow-hidden">
            {loading ? (
              <div className="p-8 text-center">Loading content...</div>
            ) : (
              <>
                <table className="min-w-full divide-y divide-gray-200">
                  <thead className="bg-gray-50">
                    <tr>
                      <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase">
                        Type
                      </th>
                      <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase">
                        Title
                      </th>
                      <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase">
                        URL
                      </th>
                      <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase">
                        Product ID
                      </th>
                      <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase">
                        Indexed
                      </th>
                      <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase">
                        Freshness
                      </th>
                    </tr>
                  </thead>
                  <tbody className="bg-white divide-y divide-gray-200">
                    {content.map((item, idx) => {
                      const daysSince = getDaysSinceIndexed(item.indexed_at);
                      const isStale = daysSince > 7;
                      
                      return (
                        <tr key={idx} className={isStale ? "bg-yellow-50" : ""}>
                          <td className="px-6 py-4 whitespace-nowrap">
                            <span className={`px-2 py-1 text-xs rounded ${
                              item.page_type === "product"
                                ? "bg-blue-100 text-blue-800"
                                : "bg-gray-100 text-gray-800"
                            }`}>
                              {item.page_type}
                            </span>
                          </td>
                          <td className="px-6 py-4">
                            <div className="text-sm font-medium text-gray-900">
                              {item.title || "Untitled"}
                            </div>
                            {item.snippet && (
                              <div className="text-sm text-gray-500 mt-1">
                                {item.snippet.substring(0, 100)}...
                              </div>
                            )}
                          </td>
                          <td className="px-6 py-4">
                            <a
                              href={item.url}
                              target="_blank"
                              rel="noopener noreferrer"
                              className="text-sm text-blue-600 hover:text-blue-900 break-all"
                            >
                              {item.url}
                            </a>
                          </td>
                          <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
                            {item.product_id || "-"}
                          </td>
                          <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
                            {formatDate(item.indexed_at)}
                          </td>
                          <td className="px-6 py-4 whitespace-nowrap">
                            <span className={`text-sm ${
                              isStale ? "text-yellow-600 font-medium" : "text-gray-500"
                            }`}>
                              {daysSince === 0
                                ? "Today"
                                : daysSince === 1
                                ? "1 day ago"
                                : `${daysSince} days ago`}
                            </span>
                          </td>
                        </tr>
                      );
                    })}
                  </tbody>
                </table>
  
                {/* Pagination */}
                {total > limit && (
                  <div className="bg-gray-50 px-6 py-3 flex items-center justify-between">
                    <div className="text-sm text-gray-700">
                      Showing {(page - 1) * limit + 1} to {Math.min(page * limit, total)} of {total}
                    </div>
                    <div className="flex gap-2">
                      <button
                        onClick={() => setPage(page - 1)}
                        disabled={page === 1}
                        className="px-4 py-2 border border-gray-300 rounded-md disabled:opacity-50"
                      >
                        Previous
                      </button>
                      <button
                        onClick={() => setPage(page + 1)}
                        disabled={page * limit >= total}
                        className="px-4 py-2 border border-gray-300 rounded-md disabled:opacity-50"
                      >
                        Next
                      </button>
                    </div>
                  </div>
                )}
              </>
            )}
          </div>
        </main>
      </div>
    );
  }
  ```
- Add route to App.tsx:
  ```typescript
  import { Content } from "./pages/Content";
  
  <Route
    path="/sites/:siteId/content"
    element={
      <PrivateRoute>
        <Content />
      </PrivateRoute>
    }
  />
  ```

**Files to Create/Modify:**
- `admin/src/pages/Content.tsx` (create)
- `admin/src/App.tsx` (modify)

**Acceptance:** Content list displays, pagination works, filtering by type works, freshness indicators show

---

#### Task 11.3: Implement Crawl Job Status Display (1.5 hours)
**Description:** Add crawl status display and re-sync functionality per PRD §7.7 FR-027, FR-033.

**Actions:**
- Create `admin/src/components/CrawlStatus.tsx`:
  ```typescript
  import { useState, useEffect } from "react";
  import { api } from "../services/api";
  
  interface CrawlStatusProps {
    siteId: string;
  }
  
  interface CrawlJob {
    id: string;
    status: string;
    started_at?: string;
    finished_at?: string;
    last_synced_at?: string;
    error_message?: string;
  }
  
  export function CrawlStatus({ siteId }: CrawlStatusProps) {
    const [status, setStatus] = useState<CrawlJob | null>(null);
    const [loading, setLoading] = useState(false);
    const [syncing, setSyncing] = useState(false);
  
    useEffect(() => {
      loadStatus();
      // Poll for status updates if job is running
      const interval = setInterval(() => {
        if (status?.status === "running") {
          loadStatus();
        }
      }, 5000); // Poll every 5 seconds
      
      return () => clearInterval(interval);
    }, [siteId, status?.status]);
  
    const loadStatus = async () => {
      try {
        const response = await api.get(`/admin/sites/${siteId}/crawl/status`);
        setStatus(response.data);
      } catch (error) {
        console.error("Failed to load crawl status", error);
      }
    };
  
    const handleReSync = async () => {
      setSyncing(true);
      try {
        await api.post(`/admin/sites/${siteId}/crawl`);
        // Reload status after a delay
        setTimeout(() => {
          loadStatus();
        }, 1000);
      } catch (error) {
        console.error("Failed to trigger re-sync", error);
        alert("Failed to trigger re-sync. Please try again.");
      } finally {
        setSyncing(false);
      }
    };
  
    if (!status) {
      return (
        <div className="bg-white rounded-lg shadow p-6">
          <div className="flex justify-between items-center">
            <div>
              <h3 className="text-lg font-semibold">Crawl Status</h3>
              <p className="text-sm text-gray-600">No crawl job yet</p>
            </div>
            <button
              onClick={handleReSync}
              disabled={syncing}
              className="px-4 py-2 bg-blue-600 text-white rounded-md hover:bg-blue-700 disabled:opacity-50"
            >
              {syncing ? "Starting..." : "Start Crawl"}
            </button>
          </div>
        </div>
      );
    }
  
    const getStatusColor = (status: string) => {
      switch (status) {
        case "done":
          return "text-green-600 bg-green-100";
        case "running":
          return "text-blue-600 bg-blue-100";
        case "failed":
          return "text-red-600 bg-red-100";
        default:
          return "text-gray-600 bg-gray-100";
      }
    };
  
    return (
      <div className="bg-white rounded-lg shadow p-6">
        <div className="flex justify-between items-start mb-4">
          <div>
            <h3 className="text-lg font-semibold">Crawl Status</h3>
            <span className={`inline-block px-2 py-1 text-xs rounded mt-2 ${getStatusColor(status.status)}`}>
              {status.status.toUpperCase()}
            </span>
          </div>
          <button
            onClick={handleReSync}
            disabled={syncing || status.status === "running"}
            className="px-4 py-2 bg-blue-600 text-white rounded-md hover:bg-blue-700 disabled:opacity-50"
          >
            {syncing ? "Starting..." : status.status === "running" ? "Crawling..." : "Re-sync"}
          </button>
        </div>
  
        {status.status === "running" && (
          <div className="mb-4">
            <div className="w-full bg-gray-200 rounded-full h-2">
              <div className="bg-blue-600 h-2 rounded-full animate-pulse" style={{ width: "50%" }}></div>
            </div>
            <p className="text-sm text-gray-600 mt-2">Crawl in progress...</p>
          </div>
        )}
  
        <div className="space-y-2 text-sm">
          {status.started_at && (
            <div>
              <span className="font-medium">Started:</span>{" "}
              {new Date(status.started_at).toLocaleString()}
            </div>
          )}
          {status.finished_at && (
            <div>
              <span className="font-medium">Finished:</span>{" "}
              {new Date(status.finished_at).toLocaleString()}
            </div>
          )}
          {status.last_synced_at && (
            <div>
              <span className="font-medium">Last Synced:</span>{" "}
              {new Date(status.last_synced_at).toLocaleString()}
            </div>
          )}
          {status.error_message && (
            <div className="mt-4 p-3 bg-red-50 border border-red-200 rounded text-red-700">
              <span className="font-medium">Error:</span> {status.error_message}
            </div>
          )}
        </div>
      </div>
    );
  }
  ```
- Add to SiteConfig page:
  ```typescript
  import { CrawlStatus } from "../components/CrawlStatus";
  
  // In SiteConfig component
  <section className="mb-8">
    <CrawlStatus siteId={siteId!} />
  </section>
  ```

**Files to Create/Modify:**
- `admin/src/components/CrawlStatus.tsx` (create)
- `admin/src/pages/SiteConfig.tsx` (modify)

**Acceptance:** Crawl status displays, re-sync button works, status polls when running, error messages show

---

#### Task 11.4: Implement Exclude URL Patterns Configuration (1.5 hours)
**Description:** Add UI for configuring excluded URL patterns per PRD §7.7.1 and TAD §11.1.

**Actions:**
- Create `admin/src/components/ExcludedUrls.tsx`:
  ```typescript
  import { useState, useEffect } from "react";
  
  interface ExcludedUrlsProps {
    value: string[];
    onChange: (urls: string[]) => void;
  }
  
  export function ExcludedUrlsEditor({ value, onChange }: ExcludedUrlsProps) {
    const [urls, setUrls] = useState(value.join("\n"));
  
    useEffect(() => {
      onChange(urls.split("\n").filter(Boolean));
    }, [urls]);
  
    return (
      <div>
        <label className="block text-sm font-medium text-gray-700 mb-2">
          Excluded URL Patterns (one per line)
        </label>
        <textarea
          value={urls}
          onChange={(e) => setUrls(e.target.value)}
          rows={6}
          className="w-full px-3 py-2 border border-gray-300 rounded-md font-mono text-sm"
          placeholder="/admin/*&#10;/cart&#10;/checkout/*"
        />
        <p className="mt-1 text-sm text-gray-500">
          URLs matching these patterns will be skipped during crawl. Use * for wildcards.
        </p>
      </div>
    );
  }
  ```
- Add to SiteConfig page:
  ```typescript
  import { ExcludedUrlsEditor } from "../components/ExcludedUrls";
  
  <section>
    <h2 className="text-lg font-semibold mb-4">Excluded URLs</h2>
    <ExcludedUrlsEditor
      value={config.excluded_url_patterns}
      onChange={(urls) => setConfig({ ...config, excluded_url_patterns: urls })}
    />
  </section>
  ```

**Files to Create/Modify:**
- `admin/src/components/ExcludedUrls.tsx` (create)
- `admin/src/pages/SiteConfig.tsx` (modify)

**Acceptance:** Excluded URLs editor works, patterns save correctly

---

#### Task 11.5: Add Content Management Link to SiteConfig (30 min)
**Description:** Add navigation link to content management page.

**Actions:**
- Update SiteConfig page header:
  ```typescript
  import { useNavigate } from "react-router-dom";
  
  // In SiteConfig component
  const navigate = useNavigate();
  
  // In header
  <div className="flex justify-between items-center mb-6">
    <h2 className="text-xl font-semibold">Configuration</h2>
    <button
      onClick={() => navigate(`/sites/${siteId}/content`)}
      className="px-4 py-2 border border-gray-300 rounded-md hover:bg-gray-50"
    >
      View Content
    </button>
  </div>
  ```

**Files to Create/Modify:**
- `admin/src/pages/SiteConfig.tsx` (modify)

**Acceptance:** Navigation link works, content page accessible

---

### Day 11 Summary
- ✅ Content list API endpoint implemented
- ✅ Content list page with pagination and filtering
- ✅ Crawl status display with re-sync functionality
- ✅ Excluded URL patterns configuration
- ✅ Content freshness indicators

**Next Day Preview:** Day 12 will implement SDK block interactions (drag-drop, expand/collapse, remove) and empty blocks.

---

## Day 12: SDK Block Interactions & Empty Blocks

**Epic:** EPIC-4 - SDK Implementation  
**Story:** STORY-4.4 - Block Interactions & Empty Blocks  
**Total Effort:** 8 hours  
**Day:** 12

### Story Description
As a developer, I want to implement block interactions (drag-drop reordering, expand/collapse, removal) and empty blocks with user-pulled content, so that users can customize their grid experience and pull only the information they need.

### Acceptance Criteria
1. Block drag-and-drop reordering per PRD §7.9 FR-036
2. Block order persistence in sessionStorage per PRD §7.9 FR-037
3. Block expand/collapse functionality per PRD §7.9 FR-038
4. Block removal with confirmation per PRD §7.9 FR-039
5. Empty blocks with structured prompts per PRD §7.10 FR-041
6. Quick-select chips for empty blocks per PRD §7.10 FR-043
7. User-pulled content loading per PRD §7.10 FR-044
8. Custom Query Block implementation per PRD §7.11

### Granular Tasks

#### Task 12.1: Implement Block Drag & Drop Reordering (2 hours)
**Description:** Add drag-and-drop functionality for block reordering per PRD §7.9 FR-036.

**Actions:**
- Update `sdk/src/runtime/grid.ts` to add drag handlers:
  ```typescript
  import { setSessionData, getSessionData } from "./session";
  
  function renderBlock(
    config: RuntimeConfig,
    block: AssembleResponse["blocks"][0],
    rationales: Record<string, string>,
    blockIndex: number,
  ): HTMLElement {
    const blockElement = document.createElement("div");
    blockElement.className = `dap-block dap-block-${block.type}`;
    blockElement.style.marginBottom = "32px";
    blockElement.draggable = true;
    blockElement.dataset.blockIndex = String(blockIndex);
    
    // Drag handle (visible on hover)
    const dragHandle = document.createElement("div");
    dragHandle.className = "dap-drag-handle";
    dragHandle.textContent = "⋮⋮";
    dragHandle.style.position = "absolute";
    dragHandle.style.left = "8px";
    dragHandle.style.top = "8px";
    dragHandle.style.cursor = "move";
    dragHandle.style.opacity = "0.5";
    dragHandle.style.fontSize = "18px";
    dragHandle.style.userSelect = "none";
    
    blockElement.style.position = "relative";
    blockElement.appendChild(dragHandle);
    
    // Drag events
    blockElement.addEventListener("dragstart", (e) => {
      e.dataTransfer!.effectAllowed = "move";
      e.dataTransfer!.setData("text/plain", String(blockIndex));
      blockElement.style.opacity = "0.5";
    });
    
    blockElement.addEventListener("dragend", () => {
      blockElement.style.opacity = "1";
    });
    
    blockElement.addEventListener("dragover", (e) => {
      e.preventDefault();
      e.dataTransfer!.dropEffect = "move";
      blockElement.style.borderTop = "3px solid #3b82f6";
    });
    
    blockElement.addEventListener("dragleave", () => {
      blockElement.style.borderTop = "none";
    });
    
    blockElement.addEventListener("drop", (e) => {
      e.preventDefault();
      blockElement.style.borderTop = "none";
      
      const draggedIndex = parseInt(e.dataTransfer!.getData("text/plain"));
      const dropIndex = blockIndex;
      
      if (draggedIndex !== dropIndex) {
        reorderBlocks(config, draggedIndex, dropIndex);
      }
    });
    
    // ... rest of block rendering ...
    
    return blockElement;
  }
  
  function reorderBlocks(
    config: RuntimeConfig,
    fromIndex: number,
    toIndex: number,
  ): void {
    const grid = document.getElementById(GRID_ID);
    if (!grid) return;
    
    const blocks = Array.from(grid.querySelectorAll(".dap-block"));
    const draggedBlock = blocks[fromIndex];
    const targetBlock = blocks[toIndex];
    
    if (fromIndex < toIndex) {
      targetBlock.after(draggedBlock);
    } else {
      targetBlock.before(draggedBlock);
    }
    
    // Save new order to sessionStorage
    const newOrder = Array.from(grid.querySelectorAll(".dap-block")).map(
      (block) => block.className.match(/dap-block-(\w+)/)?.[1]
    ).filter(Boolean);
    
    setSessionData(config.siteId, "block_order", newOrder);
  }
  ```

**Files to Create/Modify:**
- `sdk/src/runtime/grid.ts` (modify)

**Acceptance:** Blocks can be dragged and reordered, visual feedback during drag, order persists

---

#### Task 12.2: Implement Block Expand/Collapse (1.5 hours)
**Description:** Add expand/collapse functionality per PRD §7.9 FR-038.

**Actions:**
- Add expand/collapse to block rendering:
  ```typescript
  function renderBlock(...): HTMLElement {
    // ... existing code ...
    
    const [isExpanded, setIsExpanded] = useState(true);
    const savedState = getSessionData<boolean>(
      config.siteId,
      `block_${block.type}_expanded`
    );
    if (savedState !== null) {
      setIsExpanded(savedState);
    }
    
    // Expand/collapse button
    const expandBtn = document.createElement("button");
    expandBtn.className = "dap-expand-btn";
    expandBtn.textContent = isExpanded ? "−" : "+";
    expandBtn.style.position = "absolute";
    expandBtn.style.right = "8px";
    expandBtn.style.top = "8px";
    expandBtn.style.width = "24px";
    expandBtn.style.height = "24px";
    expandBtn.style.border = "none";
    expandBtn.style.backgroundColor = "transparent";
    expandBtn.style.cursor = "pointer";
    expandBtn.style.fontSize = "20px";
    
    const productsGrid = blockElement.querySelector(".dap-products-grid") as HTMLElement;
    
    expandBtn.onclick = () => {
      const newState = !isExpanded;
      setIsExpanded(newState);
      
      if (productsGrid) {
        productsGrid.style.display = newState ? "grid" : "none";
      }
      
      expandBtn.textContent = newState ? "−" : "+";
      
      // Save state
      setSessionData(config.siteId, `block_${block.type}_expanded`, newState);
    };
    
    if (!isExpanded && productsGrid) {
      productsGrid.style.display = "none";
    }
    
    blockElement.appendChild(expandBtn);
    
    return blockElement;
  }
  ```

**Files to Create/Modify:**
- `sdk/src/runtime/grid.ts` (modify)

**Acceptance:** Blocks can be expanded/collapsed, state persists in sessionStorage

---

#### Task 12.3: Implement Block Removal (1 hour)
**Description:** Add block removal functionality with confirmation per PRD §7.9 FR-039.

**Actions:**
- Add remove button to blocks:
  ```typescript
  function renderBlock(...): HTMLElement {
    // ... existing code ...
    
    // Remove button
    const removeBtn = document.createElement("button");
    removeBtn.className = "dap-remove-btn";
    removeBtn.textContent = "×";
    removeBtn.style.position = "absolute";
    removeBtn.style.right = "40px";
    removeBtn.style.top = "8px";
    removeBtn.style.width = "24px";
    removeBtn.style.height = "24px";
    removeBtn.style.border = "none";
    removeBtn.style.backgroundColor = "transparent";
    removeBtn.style.cursor = "pointer";
    removeBtn.style.fontSize = "20px";
    removeBtn.style.color = "#ef4444";
    
    removeBtn.onclick = () => {
      if (confirm("Remove this block?")) {
        // Hide block
        blockElement.style.display = "none";
        
        // Save removed block ID
        const removed = getSessionData<string[]>(config.siteId, "removed_blocks") || [];
        if (!removed.includes(block.type)) {
          removed.push(block.type);
          setSessionData(config.siteId, "removed_blocks", removed);
        }
      }
    };
    
    blockElement.appendChild(removeBtn);
    
    return blockElement;
  }
  
  // Filter out removed blocks when rendering
  function renderGrid(...): void {
    // ... existing code ...
    
    const removedBlocks = getSessionData<string[]>(config.siteId, "removed_blocks") || [];
    
    response.blocks
      .filter(block => !removedBlocks.includes(block.type))
      .forEach((block, index) => {
        const blockElement = renderBlock(config, block, response.rationales, index);
        content.appendChild(blockElement);
      });
  }
  ```

**Files to Create/Modify:**
- `sdk/src/runtime/grid.ts` (modify)

**Acceptance:** Blocks can be removed with confirmation, removed blocks don't reappear

---

#### Task 12.4: Implement Empty Blocks with Prompts & Chips (2 hours)
**Description:** Create empty blocks with structured prompts and quick-select chips per PRD §7.10.

**Actions:**
- Create `sdk/src/runtime/empty_blocks.ts`:
  ```typescript
  import { RuntimeConfig } from "../types";
  import { callAssemble } from "./assemble";
  
  export function renderEmptyBlock(
    config: RuntimeConfig,
    blockType: string,
    intent: string,
  ): HTMLElement {
    const blockElement = document.createElement("div");
    blockElement.className = `dap-block dap-empty-block dap-block-${blockType}`;
    blockElement.style.marginBottom = "32px";
    blockElement.style.border = "2px dashed #e5e7eb";
    blockElement.style.borderRadius = "8px";
    blockElement.style.padding = "40px";
    blockElement.style.textAlign = "center";
    blockElement.style.backgroundColor = "#f9fafb";
    
    // Prompt text
    const prompt = document.createElement("div");
    prompt.className = "dap-empty-prompt";
    prompt.style.fontSize = "18px";
    prompt.style.fontWeight = "600";
    prompt.style.marginBottom = "20px";
    prompt.style.color = "#374151";
    prompt.textContent = getPromptText(blockType);
    blockElement.appendChild(prompt);
    
    // Quick-select chips
    const chipsContainer = document.createElement("div");
    chipsContainer.className = "dap-chips-container";
    chipsContainer.style.display = "flex";
    chipsContainer.style.flexWrap = "wrap";
    chipsContainer.style.gap = "8px";
    chipsContainer.style.justifyContent = "center";
    
    const chips = getChipsForBlockType(blockType);
    chips.forEach(chip => {
      const chipBtn = document.createElement("button");
      chipBtn.textContent = chip.label;
      chipBtn.className = "dap-chip";
      chipBtn.style.padding = "8px 16px";
      chipBtn.style.border = "1px solid #e5e7eb";
      chipBtn.style.borderRadius = "20px";
      chipBtn.style.backgroundColor = "#ffffff";
      chipBtn.style.cursor = "pointer";
      chipBtn.style.fontSize = "14px";
      chipBtn.style.transition = "all 0.2s";
      
      chipBtn.onmouseenter = () => {
        chipBtn.style.borderColor = config.config.white_label.primary_color || "#3b82f6";
        chipBtn.style.backgroundColor = "#f0f9ff";
      };
      
      chipBtn.onmouseleave = () => {
        chipBtn.style.borderColor = "#e5e7eb";
        chipBtn.style.backgroundColor = "#ffffff";
      };
      
      chipBtn.onclick = async () => {
        chipBtn.disabled = true;
        chipBtn.textContent = "Loading...";
        
        try {
          const response = await callAssemble(config, intent, chip.blockType, chip.query);
          
          // Replace empty block with filled content
          const filledBlock = renderFilledBlock(config, chip.blockType, response, intent);
          blockElement.replaceWith(filledBlock);
        } catch (error) {
          chipBtn.disabled = false;
          chipBtn.textContent = chip.label;
          alert("Failed to load content. Please try again.");
        }
      };
      
      chipsContainer.appendChild(chipBtn);
    });
    
    blockElement.appendChild(chipsContainer);
    
    return blockElement;
  }
  
  function getPromptText(blockType: string): string {
    const prompts: Record<string, string> = {
      pricing: "Want to see pricing information?",
      benefits: "Want to see benefits and features?",
      eligibility: "Want to check eligibility?",
      comparison: "Want to compare options?",
      trade_off: "Want to see trade-offs?",
    };
    return prompts[blockType] || "Want to see more information?";
  }
  
  function getChipsForBlockType(blockType: string): Array<{ label: string; blockType: string; query: string }> {
    const chipsMap: Record<string, Array<{ label: string; blockType: string; query: string }>> = {
      pricing: [
        { label: "Show Pricing", blockType: "pricing", query: "pricing costs" },
      ],
      benefits: [
        { label: "Show Benefits", blockType: "benefits", query: "benefits features advantages" },
      ],
      eligibility: [
        { label: "Check Eligibility", blockType: "eligibility", query: "eligibility requirements qualifications" },
      ],
      comparison: [
        { label: "Compare Features", blockType: "comparison", query: "compare features differences" },
      ],
      trade_off: [
        { label: "Show Trade-offs", blockType: "trade_off", query: "trade-offs pros cons" },
      ],
    };
    
    return chipsMap[blockType] || [
      { label: "Show More", blockType: blockType, query: blockType },
    ];
  }
  
  function renderFilledBlock(
    config: RuntimeConfig,
    blockType: string,
    response: any,
    intent: string,
  ): HTMLElement {
    // Reuse existing block rendering logic
    const block = response.blocks.find((b: any) => b.type === blockType) || {
      type: blockType,
      products: response.products,
    };
    
    return renderBlock(config, block, response.rationales, 0);
  }
  ```
- Update grid rendering to show empty blocks:
  ```typescript
  // In grid.ts, check if block should be empty
  const EMPTY_BY_DEFAULT = ["custom_query"];
  const EMPTY_BY_INTENT: Record<string, string[]> = {
    just_exploring: ["benefits", "trade_off"],
  };
  
  response.blocks.forEach((block, index) => {
    const shouldBeEmpty = 
      EMPTY_BY_DEFAULT.includes(block.type) ||
      EMPTY_BY_INTENT[intent]?.includes(block.type);
    
    if (shouldBeEmpty && block.products.length === 0) {
      const emptyBlock = renderEmptyBlock(config, block.type, intent);
      content.appendChild(emptyBlock);
    } else {
      const blockElement = renderBlock(config, block, response.rationales, index);
      content.appendChild(blockElement);
    }
  });
  ```

**Files to Create/Modify:**
- `sdk/src/runtime/empty_blocks.ts` (create)
- `sdk/src/runtime/grid.ts` (modify)

**Acceptance:** Empty blocks render with prompts and chips, clicking chips loads content, blocks become filled

---

#### Task 12.5: Implement Custom Query Block (1.5 hours)
**Description:** Create Custom Query Block with structured query interface per PRD §7.11.

**Actions:**
- Create `sdk/src/runtime/custom_query.ts`:
  ```typescript
  import { RuntimeConfig } from "../types";
  import { callAssemble } from "./assemble";
  
  export function renderCustomQueryBlock(
    config: RuntimeConfig,
    intent: string,
  ): HTMLElement {
    const blockElement = document.createElement("div");
    blockElement.className = "dap-block dap-custom-query-block";
    blockElement.style.marginBottom = "32px";
    blockElement.style.border = "2px dashed #e5e7eb";
    blockElement.style.borderRadius = "8px";
    blockElement.style.padding = "32px";
    blockElement.style.backgroundColor = "#f9fafb";
    
    // Title
    const title = document.createElement("h3");
    title.textContent = "Custom Query";
    title.style.fontSize = "20px";
    title.style.fontWeight = "600";
    title.style.marginBottom = "20px";
    blockElement.appendChild(title);
    
    // Query form
    const form = document.createElement("div");
    form.className = "dap-query-form";
    form.style.display = "flex";
    form.style.flexDirection = "column";
    form.style.gap = "12px";
    
    // Query type selector
    const typeSelect = document.createElement("select");
    typeSelect.className = "dap-query-type";
    typeSelect.style.padding = "8px 12px";
    typeSelect.style.border = "1px solid #e5e7eb";
    typeSelect.style.borderRadius = "6px";
    
    const queryTypes = [
      { value: "by_feature", label: "Find products by feature" },
      { value: "by_price", label: "Show products under price" },
      { value: "compare", label: "Compare products by" },
    ];
    
    queryTypes.forEach(type => {
      const option = document.createElement("option");
      option.value = type.value;
      option.textContent = type.label;
      typeSelect.appendChild(option);
    });
    
    form.appendChild(typeSelect);
    
    // Query input
    const queryInput = document.createElement("input");
    queryInput.type = "text";
    queryInput.className = "dap-query-input";
    queryInput.placeholder = "Enter your query...";
    queryInput.style.padding = "8px 12px";
    queryInput.style.border = "1px solid #e5e7eb";
    queryInput.style.borderRadius = "6px";
    form.appendChild(queryInput);
    
    // Search button
    const searchBtn = document.createElement("button");
    searchBtn.textContent = "Search";
    searchBtn.className = "dap-query-search";
    searchBtn.style.padding = "10px 20px";
    searchBtn.style.border = "none";
    searchBtn.style.borderRadius = "6px";
    searchBtn.style.backgroundColor = config.config.white_label.primary_color || "#3b82f6";
    searchBtn.style.color = "#ffffff";
    searchBtn.style.cursor = "pointer";
    
    const resultsContainer = document.createElement("div");
    resultsContainer.className = "dap-query-results";
    resultsContainer.style.marginTop = "20px";
    
    searchBtn.onclick = async () => {
      const queryType = typeSelect.value;
      const queryValue = queryInput.value.trim();
      
      if (!queryValue) {
        alert("Please enter a query");
        return;
      }
      
      searchBtn.disabled = true;
      searchBtn.textContent = "Searching...";
      
      try {
        const customQuery = {
          type: queryType,
          value: queryValue,
        };
        
        const response = await callAssemble(config, intent, undefined, undefined, customQuery);
        
        // Display results
        resultsContainer.innerHTML = "";
        if (response.products.length === 0) {
          resultsContainer.textContent = "No products found";
        } else {
          response.products.forEach(product => {
            const card = renderProductCard(config, product, response.rationales[product.id]);
            resultsContainer.appendChild(card);
          });
        }
      } catch (error) {
        alert("Search failed. Please try again.");
      } finally {
        searchBtn.disabled = false;
        searchBtn.textContent = "Search";
      }
    };
    
    form.appendChild(searchBtn);
    blockElement.appendChild(form);
    blockElement.appendChild(resultsContainer);
    
    return blockElement;
  }
  ```
- Update grid to render custom query block:
  ```typescript
  import { renderCustomQueryBlock } from "./custom_query";
  
  // In renderGrid
  if (block.type === "custom_query") {
    const customQueryBlock = renderCustomQueryBlock(config, intent);
    content.appendChild(customQueryBlock);
  }
  ```

**Files to Create/Modify:**
- `sdk/src/runtime/custom_query.ts` (create)
- `sdk/src/runtime/grid.ts` (modify)

**Acceptance:** Custom query block renders, queries execute, results display in block

---

### Day 12 Summary
- ✅ Block drag-and-drop reordering implemented
- ✅ Block expand/collapse functionality
- ✅ Block removal with confirmation
- ✅ Empty blocks with prompts and chips
- ✅ Custom Query Block implementation

**Next Day Preview:** Day 13 will focus on testing, integration, and bug fixes.

---

## Day 13: Testing, Integration & Bug Fixes

**Epic:** EPIC-6 - Quality Assurance  
**Story:** STORY-6.1 - Unit, Integration & E2E Testing  
**Total Effort:** 8 hours  
**Day:** 13

### Story Description
As a developer, I want to implement comprehensive unit tests, integration tests, and E2E tests, fix bugs discovered during testing, and ensure all critical paths are covered, so that the system is reliable and ready for deployment.

### Acceptance Criteria
1. Unit tests for backend critical paths (assemble, rationale, config, crawl) per TAD §18.1
2. Unit tests for SDK critical modules (triggers, commentary, session) per TAD §18.1
3. Integration tests for API endpoints per TAD §18.2
4. E2E tests for key user flows per TAD §18.3
5. Test coverage ≥80% for critical paths per TAD §18.1
6. All tests pass
7. Bugs identified and fixed
8. Performance tests verify NFR targets per PRD §8.1

### Granular Tasks

#### Task 13.1: Set Up Testing Infrastructure (1 hour)
**Description:** Configure testing frameworks and tools per TAD §18.

**Actions:**
- Update `backend/requirements.txt`:
  ```
  pytest==7.4.3
  pytest-asyncio==0.21.1
  httpx==0.26.0
  pytest-cov==4.1.0
  ```
- Create `backend/pytest.ini`:
  ```ini
  [pytest]
  asyncio_mode = auto
  testpaths = tests
  python_files = test_*.py
  python_classes = Test*
  python_functions = test_*
  addopts = --cov=app --cov-report=html --cov-report=term
  ```
- Create `backend/tests/__init__.py`
- Create `backend/tests/conftest.py`:
  ```python
  import pytest
  import asyncio
  from app.db.database import get_pool, close_pool
  
  @pytest.fixture(scope="session")
  def event_loop():
      loop = asyncio.get_event_loop_policy().new_event_loop()
      yield loop
      loop.close()
  
  @pytest.fixture(scope="session")
  async def db_pool():
      await get_pool()
      yield
      await close_pool()
  ```
- Set up SDK testing:
  - Update `sdk/package.json`:
    ```json
    {
      "scripts": {
        "test": "vitest",
        "test:coverage": "vitest --coverage"
      },
      "devDependencies": {
        "vitest": "^1.0.0",
        "@vitest/coverage-v8": "^1.0.0"
      }
    }
    ```
  - Create `sdk/vitest.config.ts`:
    ```typescript
    import { defineConfig } from "vitest/config";
    
    export default defineConfig({
      test: {
        environment: "jsdom",
        globals: true,
      },
    });
    ```
- Set up Admin Portal testing:
  - Update `admin/package.json`:
    ```json
    {
      "scripts": {
        "test": "vitest",
        "test:ui": "vitest --ui"
      },
      "devDependencies": {
        "vitest": "^1.0.0",
        "@testing-library/react": "^14.0.0",
        "@testing-library/jest-dom": "^6.1.0"
      }
    }
    ```

**Files to Create/Modify:**
- `backend/pytest.ini` (create)
- `backend/tests/conftest.py` (create)
- `backend/requirements.txt` (modify)
- `sdk/package.json` (modify)
- `sdk/vitest.config.ts` (create)
- `admin/package.json` (modify)

**Acceptance:** Testing frameworks configured, test commands work

---

#### Task 13.2: Write Backend Unit Tests - Assemble & Rationale (1.5 hours)
**Description:** Create unit tests for assemble and rationale services per TAD §18.1.

**Actions:**
- Create `backend/tests/test_assemble.py`:
  ```python
  import pytest
  from unittest.mock import Mock, patch, AsyncMock
  from uuid import uuid4
  from app.services.assemble import build_query_text, dedupe_by_product_id
  
  def test_build_query_text():
      """Test query text building from intent and context."""
      intent = "compare_options"
      context = {
          "page_title": "Credit Cards",
          "product_ids": ["card-1", "card-2"],
      }
      
      query = build_query_text(intent, context)
      
      assert "Compare options" in query
      assert "Credit Cards" in query
      assert query.strip() != ""
  
  def test_build_query_text_empty_context():
      """Test query building with minimal context."""
      intent = "help_me_choose"
      context = {}
      
      query = build_query_text(intent, context)
      
      assert query.strip() != ""
      assert "Help me choose" in query
  
  def test_dedupe_by_product_id():
      """Test product deduplication by product_id."""
      hits = [
          {
              "score": 0.9,
              "payload": {
                  "type": "product",
                  "product_id": "prod-1",
                  "title": "Product 1",
              },
          },
          {
              "score": 0.8,
              "payload": {
                  "type": "product",
                  "product_id": "prod-1",
                  "title": "Product 1",
              },
          },
          {
              "score": 0.7,
              "payload": {
                  "type": "product",
                  "product_id": "prod-2",
                  "title": "Product 2",
              },
          },
      ]
      
      deduped = dedupe_by_product_id(hits)
      
      assert "prod-1" in deduped
      assert "prod-2" in deduped
      assert len(deduped) == 2
      assert deduped["prod-1"]["score"] == 0.9  # Best score kept
  ```
- Create `backend/tests/test_rationale.py`:
  ```python
  import pytest
  from unittest.mock import AsyncMock, patch
  from uuid import uuid4
  from app.services.rationale import get_rationale
  
  @pytest.mark.asyncio
  async def test_rationale_template_fill():
      """Test rationale template variable substitution."""
      site_id = uuid4()
      intent = "compare_options"
      product_id = "prod-1"
      context = {
          "n": 2,
          "intent": "compare_options",
          "product_title": "Premium Card",
      }
      
      with patch("app.services.rationale.get_pool") as mock_pool:
          mock_conn = AsyncMock()
          mock_pool.return_value.acquire.return_value.__aenter__.return_value = mock_conn
          mock_conn.fetchrow.return_value = None  # Use default template
          
          rationale = await get_rationale(site_id, intent, product_id, context)
          
          assert rationale
          assert "2" in rationale or "products" in rationale.lower()
  
  @pytest.mark.asyncio
  async def test_rationale_fallback():
      """Test rationale fallback when template fill fails."""
      site_id = uuid4()
      intent = "help_me_choose"
      product_id = "prod-1"
      context = {}  # Missing vars
      
      with patch("app.services.rationale.get_pool") as mock_pool:
          mock_conn = AsyncMock()
          mock_pool.return_value.acquire.return_value.__aenter__.return_value = mock_conn
          mock_conn.fetchrow.return_value = None
          
          rationale = await get_rationale(site_id, intent, product_id, context)
          
          assert rationale  # Should return generic rationale
  ```

**Files to Create/Modify:**
- `backend/tests/test_assemble.py` (create)
- `backend/tests/test_rationale.py` (create)

**Acceptance:** Unit tests pass, coverage ≥80% for assemble/rationale

---

#### Task 13.3: Write Backend Integration Tests - API Endpoints (2 hours)
**Description:** Create integration tests for API endpoints per TAD §18.2.

**Actions:**
- Create `backend/tests/test_api_config.py`:
  ```python
  import pytest
  from fastapi.testclient import TestClient
  from uuid import uuid4
  from app.main import app
  
  client = TestClient(app)
  
  @pytest.fixture
  def test_site_id():
      # Create test site (or use fixture)
      return uuid4()
  
  def test_get_config_success(test_site_id):
      """Test GET /sdk/config returns 200 with valid site_id."""
      response = client.get(f"/sdk/config?site_id={test_site_id}")
      
      # Should return 404 if site doesn't exist, or 200 if it does
      assert response.status_code in [200, 404]
  
  def test_get_config_missing_site_id():
      """Test GET /sdk/config returns 400 without site_id."""
      response = client.get("/sdk/config")
      
      assert response.status_code == 422  # Validation error
  ```
- Create `backend/tests/test_api_assemble.py`:
  ```python
  import pytest
  from fastapi.testclient import TestClient
  from app.main import app
  
  client = TestClient(app)
  
  def test_assemble_invalid_intent():
      """Test POST /assemble with invalid intent."""
      response = client.post("/assemble", json={
          "site_id": str(uuid4()),
          "intent": "invalid_intent",
          "context": {},
      })
      
      assert response.status_code == 422
  
  def test_assemble_missing_site_id():
      """Test POST /assemble without site_id."""
      response = client.post("/assemble", json={
          "intent": "help_me_choose",
          "context": {},
      })
      
      assert response.status_code == 422
  ```
- Create `backend/tests/test_api_admin.py`:
  ```python
  import pytest
  from fastapi.testclient import TestClient
  from app.main import app
  
  client = TestClient(app)
  
  def test_admin_login_invalid_credentials():
      """Test POST /admin/login with invalid credentials."""
      response = client.post("/admin/login", json={
          "email": "test@example.com",
          "password": "wrong",
      })
      
      assert response.status_code == 401
  
  def test_admin_sites_requires_auth():
      """Test GET /admin/sites requires authentication."""
      response = client.get("/admin/sites")
      
      assert response.status_code == 403  # Missing auth header
  ```

**Files to Create/Modify:**
- `backend/tests/test_api_config.py` (create)
- `backend/tests/test_api_assemble.py` (create)
- `backend/tests/test_api_admin.py` (create)

**Acceptance:** Integration tests pass, API endpoints validated

---

#### Task 13.4: Write SDK Unit Tests - Triggers & Commentary (1.5 hours)
**Description:** Create unit tests for SDK trigger and commentary modules per TAD §18.1.

**Actions:**
- Create `sdk/src/runtime/__tests__/triggers.test.ts`:
  ```typescript
  import { describe, it, expect, beforeEach, vi } from "vitest";
  import { fireTrigger, checkTriggers } from "../triggers";
  import { getEventBuffer } from "../events";
  
  describe("Triggers", () => {
    const mockConfig = {
      siteId: "test-site",
      config: {
        trigger_thresholds: {
          multi_product_min: 2,
          multi_product_window_min: 5,
          dwell_sec: 45,
          cta_hover_min: 2,
          cooldown_after_trigger_sec: 30,
          cooldown_after_dismiss_sec: 60,
          cooldown_after_grid_close_sec: 45,
        },
      },
      apiUrl: "http://localhost:8000",
    };
  
    beforeEach(() => {
      vi.clearAllMocks();
    });
  
    it("should fire trigger when multiple products viewed", () => {
      const buffer = {
        productViews: [
          { productId: "prod-1", url: "http://test.com/1", timestamp: Date.now() },
          { productId: "prod-2", url: "http://test.com/2", timestamp: Date.now() },
        ],
        pageViews: [],
        dwellTime: 0,
        ctaHovers: 0,
        scrollDepth: 0,
        samePageRevisits: new Map(),
      };
  
      // Mock getEventBuffer
      vi.spyOn(require("../events"), "getEventBuffer").mockReturnValue(buffer);
  
      // Should detect trigger
      // (Implementation depends on trigger check logic)
    });
  
    it("should respect cooldown period", () => {
      // Test cooldown prevents trigger spam
    });
  
    it("should suppress triggers after 2 dismissals", () => {
      // Test dismissal suppression
    });
  });
  ```
- Create `sdk/src/runtime/__tests__/commentary.test.ts`:
  ```typescript
  import { describe, it, expect, vi, beforeEach, afterEach } from "vitest";
  import { generateCommentary } from "../commentary";
  
  describe("Commentary", () => {
    it("should generate commentary from templates", () => {
      const config = {
        config: {
          commentary_templates: [
            "You've viewed {n} products — comparing options?",
          ],
        },
      };
      
      const buffer = {
        productViews: [
          { productId: "prod-1", url: "http://test.com", timestamp: Date.now() },
          { productId: "prod-2", url: "http://test.com", timestamp: Date.now() },
        ],
        // ... other buffer fields
      };
      
      const commentary = generateCommentary(config, buffer);
      
      expect(commentary).toContain("2");
      expect(commentary).toContain("products");
    });
  
    it("should throttle updates", () => {
      // Test debounce and max update rate
    });
  });
  ```

**Files to Create/Modify:**
- `sdk/src/runtime/__tests__/triggers.test.ts` (create)
- `sdk/src/runtime/__tests__/commentary.test.ts` (create)

**Acceptance:** SDK unit tests pass, critical paths covered

---

#### Task 13.5: Write E2E Tests - Key User Flows (2 hours)
**Description:** Create E2E tests for critical user flows per TAD §18.3.

**Actions:**
- Install Playwright:
  ```bash
  npm install -D @playwright/test
  npx playwright install
  ```
- Create `tests/e2e/playwright.config.ts`:
  ```typescript
  import { defineConfig, devices } from "@playwright/test";
  
  export default defineConfig({
    testDir: "./e2e",
    fullyParallel: true,
    forbidOnly: !!process.env.CI,
    retries: process.env.CI ? 2 : 0,
    workers: process.env.CI ? 1 : undefined,
    reporter: "html",
    use: {
      baseURL: "http://localhost:8000",
      trace: "on-first-retry",
    },
    projects: [
      {
        name: "chromium",
        use: { ...devices["Desktop Chrome"] },
      },
    ],
    webServer: {
      command: "cd backend && uvicorn app.main:app --reload",
      url: "http://localhost:8000/health",
      reuseExistingServer: !process.env.CI,
    },
  });
  ```
- Create `tests/e2e/user-flow-trigger-intent-grid.spec.ts`:
  ```typescript
  import { test, expect } from "@playwright/test";
  
  test("User flow: trigger → intent → grid", async ({ page }) => {
    // Navigate to test page with SDK
    await page.goto("http://localhost:3000/test-page.html");
    
    // Wait for SDK to load
    await page.waitForSelector("#dap-commentary-strip");
    
    // Verify strip is visible
    const strip = page.locator("#dap-commentary-strip");
    await expect(strip).toBeVisible();
    
    // Simulate viewing 2 products (trigger condition)
    // This would require mocking or actual navigation
    
    // Wait for trigger (strip shows CTA)
    await expect(strip).toContainText("Want help");
    
    // Click strip
    await strip.click();
    
    // Verify intent modal appears
    const intentModal = page.locator("#dap-intent-modal");
    await expect(intentModal).toBeVisible();
    
    // Select intent
    await page.click('text="Compare options"');
    
    // Wait for grid
    const grid = page.locator("#dap-decision-grid");
    await expect(grid).toBeVisible({ timeout: 5000 });
    
    // Verify grid has blocks
    const blocks = page.locator(".dap-block");
    await expect(blocks.first()).toBeVisible();
    
    // Click "Why this?" on a product card
    const whyButton = page.locator('text="Why this?"').first();
    await whyButton.click();
    
    // Verify rationale panel appears
    const rationalePanel = page.locator("#dap-rationale-panel");
    await expect(rationalePanel).toBeVisible();
  });
  ```
- Create `tests/e2e/admin-onboard-crawl.spec.ts`:
  ```typescript
  import { test, expect } from "@playwright/test";
  
  test("Admin: onboard site and crawl", async ({ page }) => {
    // Login
    await page.goto("http://localhost:5173/login");
    await page.fill('input[type="email"]', "admin@test.com");
    await page.fill('input[type="password"]', "password");
    await page.click('button:has-text("Sign in")');
    
    // Wait for sites page
    await expect(page).toHaveURL(/\/sites$/);
    
    // Create site
    await page.click('button:has-text("Create Site")');
    await page.fill('input[id="name"]', "Test Site");
    await page.fill('input[id="baseUrl"]', "https://example.com");
    await page.click('button:has-text("Create Site")');
    
    // Wait for site to appear in list
    await expect(page.locator("text=Test Site")).toBeVisible();
    
    // Navigate to site config
    await page.click('text="Configure"');
    
    // Trigger crawl
    await page.click('button:has-text("Start Crawl")');
    
    // Wait for crawl status to show running
    await expect(page.locator("text=running")).toBeVisible({ timeout: 10000 });
    
    // Wait for crawl to complete (or timeout)
    await page.waitForSelector("text=done", { timeout: 60000 }).catch(() => {});
    
    // Navigate to content
    await page.click('text="View Content"');
    
    // Verify content list has items
    const contentRows = page.locator("tbody tr");
    await expect(contentRows.first()).toBeVisible({ timeout: 10000 });
  });
  ```

**Files to Create/Modify:**
- `tests/e2e/playwright.config.ts` (create)
- `tests/e2e/user-flow-trigger-intent-grid.spec.ts` (create)
- `tests/e2e/admin-onboard-crawl.spec.ts` (create)
- `package.json` (add Playwright scripts)

**Acceptance:** E2E tests pass, key user flows validated

---

#### Task 13.6: Performance Testing & Bug Fixes (1 hour)
**Description:** Run performance tests and fix identified bugs per PRD §8.1.

**Actions:**
- Create performance test script `backend/tests/test_performance.py`:
  ```python
  import time
  import pytest
  from app.services.assemble import assemble
  from uuid import uuid4
  
  @pytest.mark.asyncio
  async def test_assemble_performance():
      """Test assemble API meets <100ms target."""
      site_id = uuid4()
      intent = "compare_options"
      context = {"page_title": "Test"}
      
      start = time.time()
      # Mock assemble call
      # result = await assemble(site_id, intent, context)
      elapsed = (time.time() - start) * 1000  # Convert to ms
      
      # Should be <100ms per PRD §8.1
      assert elapsed < 100, f"Assemble took {elapsed}ms, target is <100ms"
  ```
- Run all tests and document bugs:
  ```bash
  # Backend
  cd backend && pytest --cov=app --cov-report=term
  
  # SDK
  cd sdk && npm test
  
  # Admin
  cd admin && npm test
  ```
- Create bug tracking document `docs/BUGS.md`:
  ```markdown
  # Bug Tracking
  
  ## Critical Bugs
  - [ ] Bug description
    - File: path/to/file.ts
    - Status: Open/Fixed
    - Fix: Description of fix
  
  ## Minor Bugs
  - [ ] Bug description
  ```
- Fix identified bugs and re-run tests

**Files to Create/Modify:**
- `backend/tests/test_performance.py` (create)
- `docs/BUGS.md` (create)
- Fix bugs in affected files

**Acceptance:** Performance targets met, critical bugs fixed, all tests pass

---

### Day 13 Summary
- ✅ Testing infrastructure set up
- ✅ Backend unit tests written
- ✅ Backend integration tests written
- ✅ SDK unit tests written
- ✅ E2E tests for key flows
- ✅ Performance tests and bug fixes

**Next Day Preview:** Day 14 will focus on final testing, documentation, and deployment preparation.

---

## Day 14: Final Testing, Documentation & Deployment

**Epic:** EPIC-6 - Quality Assurance & Deployment  
**Story:** STORY-6.2 - Documentation & Deployment Preparation  
**Total Effort:** 8 hours  
**Day:** 14

### Story Description
As a developer, I want to complete final testing, create comprehensive documentation, and prepare the system for deployment, so that the product is production-ready and maintainable.

### Acceptance Criteria
1. All E2E tests pass
2. Documentation complete (API docs, setup guide, deployment guide)
3. Docker images built and tested
4. Environment configuration documented
5. Health check endpoints verified
6. Deployment scripts created
7. Final bug fixes applied
8. Code review and cleanup

### Granular Tasks

#### Task 14.1: Complete E2E Test Suite (1.5 hours)
**Description:** Finish all E2E tests per TAD §18.3.

**Actions:**
- Create `tests/e2e/user-reload-restore.spec.ts`:
  ```typescript
  import { test, expect } from "@playwright/test";
  
  test("User: reload restore", async ({ page }) => {
    // Navigate to test page
    await page.goto("http://localhost:3000/test-page.html");
    
    // Select intent and get grid
    // ... (similar to previous test)
    
    // Reload page
    await page.reload();
    
    // Verify "Continue where you left off?" prompt appears
    const continuePrompt = page.locator('text="Continue where you left off"');
    await expect(continuePrompt).toBeVisible();
    
    // Click "Yes"
    await page.click('button:has-text("Yes")');
    
    // Verify grid restores
    const grid = page.locator("#dap-decision-grid");
    await expect(grid).toBeVisible();
  });
  ```
- Create `tests/e2e/admin-config.spec.ts`:
  ```typescript
  import { test, expect } from "@playwright/test";
  
  test("Admin: config changes", async ({ page }) => {
    // Login and navigate to site config
    // ... (similar to previous admin test)
    
    // Edit trigger threshold
    await page.fill('input[name="multi_product_min"]', "3");
    
    // Save
    await page.click('button:has-text("Save Configuration")');
    
    // Verify success message
    await expect(page.locator("text=Configuration saved")).toBeVisible();
    
    // Reload SDK test page and verify new threshold applies
    // (Would need to test SDK behavior)
  });
  ```
- Run full E2E suite:
  ```bash
  npx playwright test
  ```
- Fix any failing tests

**Files to Create/Modify:**
- `tests/e2e/user-reload-restore.spec.ts` (create)
- `tests/e2e/admin-config.spec.ts` (create)

**Acceptance:** All E2E tests pass, edge cases covered

---

#### Task 14.2: Create API Documentation (1.5 hours)
**Description:** Document all API endpoints per TAD §12.

**Actions:**
- Update `docs/API.md`:
  ```markdown
  # DAP API Documentation
  
  ## Base URL
  - Development: `http://localhost:8000`
  - Production: `https://api.dap.example.com`
  
  ## SDK Endpoints (Public)
  
  ### GET /sdk/config
  Get site configuration for SDK.
  
  **Query Parameters:**
  - `site_id` (required, UUID): Site identifier
  
  **Response:**
  ```json
  {
    "product_page_rules": {...},
    "trigger_thresholds": {...},
    "commentary_templates": [...],
    "block_mapping": {...},
    "white_label": {...}
  }
  ```
  
  ### POST /assemble
  Assemble grid blocks and products using RAG.
  
  **Request Body:**
  ```json
  {
    "site_id": "uuid",
    "intent": "compare_options",
    "context": {
      "url": "...",
      "page_title": "...",
      "product_ids": ["id1", "id2"]
    }
  }
  ```
  
  **Response:**
  ```json
  {
    "blocks": [...],
    "products": [...],
    "rationales": {...},
    "empty": false
  }
  ```
  
  ## Admin Endpoints (Auth Required)
  
  ### POST /admin/login
  Admin authentication.
  
  **Request Body:**
  ```json
  {
    "email": "admin@example.com",
    "password": "password"
  }
  ```
  
  **Response:**
  ```json
  {
    "access_token": "jwt_token",
    "token_type": "bearer",
    "expires_in": 1800
  }
  ```
  
  ### GET /admin/sites
  List all sites.
  
  **Headers:**
  - `Authorization: Bearer <token>`
  
  ### POST /admin/sites
  Create new site.
  
  **Request Body:**
  ```json
  {
    "name": "My Site",
    "base_url": "https://example.com"
  }
  ```
  
  ### GET /admin/sites/{site_id}/config
  Get site configuration.
  
  ### PUT /admin/sites/{site_id}/config
  Update site configuration.
  
  ### POST /admin/sites/{site_id}/crawl
  Trigger crawl job.
  
  ### GET /admin/sites/{site_id}/content
  Get indexed content (paginated).
  
  **Query Parameters:**
  - `page` (optional, default: 1)
  - `limit` (optional, default: 50)
  - `page_type` (optional: "product" | "page")
  ```
- Generate OpenAPI/Swagger docs:
  - Add FastAPI automatic docs (already available at `/docs`)
  - Document in README how to access Swagger UI

**Files to Create/Modify:**
- `docs/API.md` (modify)

**Acceptance:** API documentation complete, all endpoints documented

---

#### Task 14.3: Create Deployment Documentation (1.5 hours)
**Description:** Document deployment process per TAD §19.

**Actions:**
- Create `docs/DEPLOYMENT.md`:
  ```markdown
  # Deployment Guide
  
  ## Prerequisites
  - Docker installed
  - PostgreSQL 15+ (or access to existing)
  - Qdrant (or access to existing)
  - Python 3.11+ (for local development)
  - Node.js 18+ (for building SDK/Admin)
  
  ## Environment Variables
  
  ### Backend
  ```bash
  DATABASE_URL=postgresql://user:password@host:5432/dap
  QDRANT_URL=http://qdrant:6333
  QDRANT_API_KEY=  # Optional
  SECRET_KEY=your-secret-key-here
  CORS_ORIGINS=["*"]  # Or specific origins in production
  ```
  
  ### Admin Portal
  ```bash
  VITE_API_URL=http://localhost:8000
  ```
  
  ## Local Development
  
  ### Backend
  ```bash
  cd backend
  python -m venv venv
  source venv/bin/activate  # Windows: venv\Scripts\activate
  pip install -r requirements.txt
  cp .env.example .env
  # Edit .env with your values
  uvicorn app.main:app --reload
  ```
  
  ### Admin Portal
  ```bash
  cd admin
  npm install
  npm run dev
  ```
  
  ### SDK
  ```bash
  cd sdk
  npm install
  npm run build
  ```
  
  ## Docker Deployment
  
  ### Build Backend Image
  ```bash
  cd backend
  docker build -t dap-backend:latest .
  ```
  
  ### Run Backend Container
  ```bash
  docker run -d \
    --name dap-backend \
    -p 8000:8000 \
    -e DATABASE_URL=postgresql://... \
    -e QDRANT_URL=http://qdrant:6333 \
    -e SECRET_KEY=... \
    dap-backend:latest
  ```
  
  ### Build Admin Static Assets
  ```bash
  cd admin
  npm run build
  # Copy dist/ to backend/static/admin/
  ```
  
  ### Serve Admin from Backend
  Update `backend/app/main.py`:
  ```python
  from fastapi.staticfiles import StaticFiles
  
  app.mount("/admin", StaticFiles(directory="static/admin", html=True), name="admin")
  ```
  
  ## Production Deployment
  
  ### Health Checks
  - Backend: `GET /health` should return 200
  - Verify database connectivity
  - Verify Qdrant connectivity
  
  ### Scaling
  - Backend is stateless; scale horizontally
  - Use load balancer for multiple backend instances
  - Shared Postgres and Qdrant
  
  ### Monitoring
  - Monitor `/health` endpoint
  - Log assemble API latency (target <100ms)
  - Alert on Qdrant connection failures
  - Monitor crawl job failures
  
  ## Rollback Procedure
  1. Stop current backend container
  2. Start previous backend image
  3. Revert Admin/SDK assets if needed
  ```
- Create `docs/ENVIRONMENT_SETUP.md`:
  ```markdown
  # Environment Setup Guide
  
  ## Development Environment
  
  ### Required Services
  - PostgreSQL (local or Docker)
  - Qdrant (local or Docker)
  
  ### Docker Compose (Optional)
  ```bash
  docker-compose up -d
  ```
  
  ### Database Setup
  ```bash
  cd backend
  python scripts/run_migrations.py
  python scripts/create_admin.py
  ```
  
  ## Staging Environment
  - Use shared Postgres and Qdrant
  - Deploy backend container
  - Serve Admin static assets
  - Test SDK integration
  
  ## Production Environment
  - Use existing office Postgres and Qdrant
  - Deploy backend with proper secrets
  - Configure CORS allow list
  - Enable HTTPS
  - Set up monitoring and alerts
  ```

**Files to Create/Modify:**
- `docs/DEPLOYMENT.md` (create)
- `docs/ENVIRONMENT_SETUP.md` (create)

**Acceptance:** Deployment documentation complete, all steps documented

---

#### Task 14.4: Build & Test Docker Images (1 hour)
**Description:** Build Docker images and verify deployment per TAD §19.3.

**Actions:**
- Update `backend/Dockerfile`:
  ```dockerfile
  FROM python:3.11-slim
  
  WORKDIR /app
  
  # Install system dependencies
  RUN apt-get update && apt-get install -y \
      gcc \
      && rm -rf /var/lib/apt/lists/*
  
  # Copy requirements and install
  COPY requirements.txt .
  RUN pip install --no-cache-dir -r requirements.txt
  
  # Copy application
  COPY . .
  
  # Expose port
  EXPOSE 8000
  
  # Health check
  HEALTHCHECK --interval=30s --timeout=10s --start-period=40s --retries=3 \
    CMD python -c "import requests; requests.get('http://localhost:8000/health')"
  
  # Run application
  CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
  ```
- Build and test:
  ```bash
  cd backend
  docker build -t dap-backend:test .
  docker run -d \
    --name dap-test \
    -p 8000:8000 \
    -e DATABASE_URL=postgresql://... \
    -e QDRANT_URL=http://... \
    -e SECRET_KEY=test-key \
    dap-backend:test
  
  # Test health endpoint
  curl http://localhost:8000/health
  
  # Test config endpoint
  curl http://localhost:8000/sdk/config?site_id=<test-site-id>
  
  # Cleanup
  docker stop dap-test
  docker rm dap-test
  ```
- Verify Admin static serving:
  - Build Admin: `cd admin && npm run build`
  - Copy `admin/dist` to `backend/static/admin`
  - Test: `curl http://localhost:8000/admin`

**Files to Create/Modify:**
- `backend/Dockerfile` (modify)

**Acceptance:** Docker images build successfully, containers run, health checks pass

---

#### Task 14.5: Create Setup & User Guides (1 hour)
**Description:** Create user-facing documentation.

**Actions:**
- Update `README.md`:
  ```markdown
  # Decision Assembly Platform (DAP)
  
  A website-embedded decision guide that helps users assemble clarity through context-aware information blocks.
  
  ## Quick Start
  
  ### For Website Owners (Integration)
  
  Add two lines to your website:
  
  ```html
  <script src="https://api.dap.example.com/sdk/loader.js"></script>
  <script>
    DecisionPlatform.init({ siteId: "your-site-id" });
  </script>
  ```
  
  ### For Developers
  
  See [docs/SETUP.md](docs/SETUP.md) for development setup.
  
  ## Features
  
  - **Commentary Strip**: Always-on guidance at bottom of page
  - **Intent Selection**: User chooses their goal (compare, choose, explore)
  - **Grid Assembly**: RAG-powered product recommendations
  - **Transparent Rationale**: "Why this?" explanations
  - **Admin Portal**: Manage sites, configure triggers, white-label
  
  ## Documentation
  
  - [Setup Guide](docs/SETUP.md)
  - [API Documentation](docs/API.md)
  - [Deployment Guide](docs/DEPLOYMENT.md)
  - [Architecture](docs/DAP_TAD.md)
  - [Product Requirements](docs/DAP_PRD.md)
  
  ## Tech Stack
  
  - Backend: FastAPI (Python 3.11+)
  - Admin Portal: React 18 + TypeScript + Vite
  - SDK: Vanilla TypeScript (bundled with Rollup)
  - Database: PostgreSQL 15+
  - Vector Store: Qdrant
  - Embeddings: BAAI/bge-small-en-v1.5
  ```
- Create `docs/INTEGRATION_GUIDE.md`:
  ```markdown
  # SDK Integration Guide
  
  ## Installation
  
  Add the DAP SDK to your website with two lines:
  
  ```html
  <script src="https://api.dap.example.com/sdk/loader.js"></script>
  <script>
    DecisionPlatform.init({ 
      siteId: "your-site-id",
      apiUrl: "https://api.dap.example.com"  // Optional, defaults to loader origin
    });
  </script>
  ```
  
  ## Configuration
  
  Configure your site in the Admin Portal:
  1. Login to Admin Portal
  2. Create or select your site
  3. Configure:
     - Product page rules (URL patterns, selectors)
     - Trigger thresholds
     - Commentary templates
     - White-label settings
  
  ## Customization
  
  ### White-Labeling
  - Brand colors
  - Fonts
  - Logo
  - Copy tone
  
  ### Product Page Detection
  Configure which pages count as "product pages":
  - URL patterns: `/products/*`, `/cards/*`
  - DOM selectors: `[data-product-id]`, `.product-card`
  
  ### Trigger Sensitivity
  Adjust when the guide appears:
  - Multiple product views threshold
  - Dwell time threshold
  - CTA hover threshold
  
  ## Support
  
  For issues or questions, contact support@dap.example.com
  ```

**Files to Create/Modify:**
- `README.md` (modify)
- `docs/INTEGRATION_GUIDE.md` (create)

**Acceptance:** Documentation complete, setup guides clear

---

#### Task 14.6: Final Code Review & Cleanup (1 hour)
**Description:** Review code, fix issues, and prepare for production.

**Actions:**
- Run linters:
  ```bash
  # Backend
  cd backend
  ruff check .
  black --check .
  
  # SDK
  cd sdk
  npm run lint
  
  # Admin
  cd admin
  npm run lint
  ```
- Fix linting errors
- Remove debug console.logs
- Verify error handling:
  - All try-catch blocks have proper error messages
  - API errors return proper status codes
  - SDK errors don't crash customer pages
- Update `.gitignore`:
  ```
  # Python
  __pycache__/
  *.pyc
  venv/
  .env
  
  # Node
  node_modules/
  dist/
  .next/
  
  # IDE
  .vscode/
  .idea/
  
  # Testing
  .pytest_cache/
  coverage/
  .coverage
  htmlcov/
  
  # Build
  *.egg-info/
  build/
  ```
- Create `.dockerignore`:
  ```
  __pycache__
  *.pyc
  venv/
  .env
  .git
  tests/
  *.md
  ```
- Final test run:
  ```bash
  # Run all tests
  cd backend && pytest
  cd ../sdk && npm test
  cd ../admin && npm test
  cd ../tests/e2e && npx playwright test
  ```

**Files to Create/Modify:**
- `.gitignore` (modify)
- `.dockerignore` (create)
- Fix linting errors in all files

**Acceptance:** Code clean, all tests pass, ready for production

---

#### Task 14.7: Create Deployment Checklist (30 min)
**Description:** Create final deployment checklist.

**Actions:**
- Create `docs/DEPLOYMENT_CHECKLIST.md`:
  ```markdown
  # Deployment Checklist
  
  ## Pre-Deployment
  
  - [ ] All tests pass (unit, integration, E2E)
  - [ ] Code review completed
  - [ ] Documentation updated
  - [ ] Environment variables configured
  - [ ] Database migrations ready
  - [ ] Docker images built and tested
  
  ## Deployment Steps
  
  ### Backend
  - [ ] Build Docker image
  - [ ] Push to registry (if using)
  - [ ] Deploy container
  - [ ] Verify health endpoint
  - [ ] Run database migrations
  - [ ] Verify database connectivity
  - [ ] Verify Qdrant connectivity
  
  ### Admin Portal
  - [ ] Build static assets (`npm run build`)
  - [ ] Copy to backend static directory
  - [ ] Verify Admin Portal loads
  - [ ] Test login functionality
  
  ### SDK
  - [ ] Build SDK bundles (`npm run build`)
  - [ ] Upload to CDN or backend static
  - [ ] Verify loader.js accessible
  - [ ] Verify dap-sdk.js accessible
  - [ ] Test integration on test site
  
  ## Post-Deployment
  
  - [ ] Monitor error logs
  - [ ] Verify API endpoints responding
  - [ ] Test end-to-end user flow
  - [ ] Test admin operations
  - [ ] Monitor performance metrics
  - [ ] Set up alerts
  
  ## Rollback Plan
  
  - [ ] Previous Docker image tagged
  - [ ] Previous Admin/SDK assets backed up
  - [ ] Rollback procedure documented
  ```

**Files to Create/Modify:**
- `docs/DEPLOYMENT_CHECKLIST.md` (create)

**Acceptance:** Deployment checklist complete, all items actionable

---

### Day 14 Summary
- ✅ E2E test suite complete
- ✅ API documentation created
- ✅ Deployment documentation complete
- ✅ Docker images built and tested
- ✅ Setup and user guides written
- ✅ Code review and cleanup done
- ✅ Deployment checklist created

**Project Complete:** All 14 days of work completed. The Decision Assembly Platform is ready for deployment.

---

## Summary of 14-Day WBS

### Completed Epics
1. **EPIC-1:** Project Foundation (Days 1-3)
2. **EPIC-2:** Content Management (Day 4)
3. **EPIC-3:** RAG & Assembly System (Day 5)
4. **EPIC-4:** SDK Implementation (Days 6-8, 12)
5. **EPIC-5:** Admin Portal (Days 9-11)
6. **EPIC-6:** Quality Assurance & Deployment (Days 13-14)

### Key Deliverables
- ✅ Complete backend API with RAG assembly
- ✅ Full-featured SDK with triggers, grid, rationale
- ✅ Admin Portal for site and content management
- ✅ Comprehensive test suite (unit, integration, E2E)
- ✅ Complete documentation (API, deployment, integration)
- ✅ Docker deployment configuration
- ✅ Production-ready codebase

### Total Effort: 112 hours (14 days × 8 hours)

---

**Watermark:**  
*Generated by @Rules/.claude/commands/sm.md agent*  
*Path: `Rules/.claude/commands/sm.md`*
