-- Create schema
CREATE SCHEMA IF NOT EXISTS dap;

-- Sites table
CREATE TABLE IF NOT EXISTS dap.sites (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    name VARCHAR(255) NOT NULL,
    base_url VARCHAR(2048) NOT NULL,
    created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

-- Site config table (1:1 with sites)
CREATE TABLE IF NOT EXISTS dap.site_config (
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
CREATE TABLE IF NOT EXISTS dap.crawl_jobs (
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
CREATE TABLE IF NOT EXISTS dap.rationale_templates (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    site_id UUID REFERENCES dap.sites(id),
    intent VARCHAR(64) NOT NULL,
    template_text TEXT NOT NULL,
    created_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

-- Indexed pages table
CREATE TABLE IF NOT EXISTS dap.indexed_pages (
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
CREATE TABLE IF NOT EXISTS dap.admin_users (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    email VARCHAR(255) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    created_at TIMESTAMPTZ NOT NULL DEFAULT now()
);
