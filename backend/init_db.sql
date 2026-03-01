-- DAP Database Initialization Script
-- Based on Technical Architecture Document (TAD)
-- Database: dap_banking_demo

-- Drop existing tables if they exist (for clean setup)
DROP TABLE IF EXISTS indexed_pages CASCADE;
DROP TABLE IF EXISTS rationale_templates CASCADE;
DROP TABLE IF EXISTS crawl_jobs CASCADE;
DROP TABLE IF EXISTS site_config CASCADE;
DROP TABLE IF EXISTS sites CASCADE;
DROP TABLE IF EXISTS users CASCADE;
DROP TABLE IF EXISTS admin_users CASCADE;

-- Create users table
CREATE TABLE users (
    user_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    email VARCHAR(255) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

-- Create sites table
CREATE TABLE sites (
    site_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    domain VARCHAR(255) UNIQUE NOT NULL,
    name VARCHAR(255) NOT NULL,
    owner_user_id UUID REFERENCES users(user_id) ON DELETE CASCADE,
    allowed_origins JSONB NOT NULL DEFAULT '[]', -- List of allowed domains for CORS
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

-- Create site_config table
CREATE TABLE site_config (
    site_id UUID PRIMARY KEY REFERENCES sites(site_id) ON DELETE CASCADE,
    branding JSONB NOT NULL DEFAULT '{}',
    triggers JSONB NOT NULL DEFAULT '{}',
    intents JSONB NOT NULL DEFAULT '[]',
    cta_selectors JSONB NOT NULL DEFAULT '["button", "a.btn", ".cta", "[role=\\"button\\"]"]',
    product_page_rules JSONB NOT NULL DEFAULT '{"url_patterns": [], "dom_selectors": []}',
    updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

-- Create crawl_jobs table
CREATE TABLE crawl_jobs (
    job_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    site_id UUID NOT NULL REFERENCES sites(site_id) ON DELETE CASCADE,
    status VARCHAR(50) NOT NULL DEFAULT 'pending',
    started_at TIMESTAMPTZ,
    completed_at TIMESTAMPTZ,
    pages_crawled INT DEFAULT 0,
    error_message TEXT,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

-- Create rationale_templates table
CREATE TABLE rationale_templates (
    template_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    site_id UUID REFERENCES sites(site_id) ON DELETE CASCADE,
    category VARCHAR(100),
    template_text TEXT NOT NULL,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

-- Create indexed_pages table
CREATE TABLE indexed_pages (
    page_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    site_id UUID NOT NULL REFERENCES sites(site_id) ON DELETE CASCADE,
    url TEXT NOT NULL,
    title VARCHAR(500),
    content_hash VARCHAR(64),
    metadata JSONB DEFAULT '{}',
    indexed_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    UNIQUE(site_id, url)
);

-- Create indexes for performance
CREATE INDEX idx_sites_domain ON sites(domain);
CREATE INDEX idx_crawl_jobs_site_id ON crawl_jobs(site_id);
CREATE INDEX idx_crawl_jobs_status ON crawl_jobs(status);
CREATE INDEX idx_indexed_pages_site_id ON indexed_pages(site_id);
CREATE INDEX idx_indexed_pages_url ON indexed_pages(url);
CREATE INDEX idx_rationale_templates_site_id ON rationale_templates(site_id);
CREATE INDEX idx_rationale_templates_category ON rationale_templates(category);

-- Insert default admin user (password: 'admin123' - CHANGE IN PRODUCTION)
INSERT INTO users (email, password_hash) VALUES 
('admin@apexbank.com', '$2b$12$LQv3c1yqBWVHxkd0LHAkCOYz6TtxMQJqhN8/LewY5GyYzpLaEg7Iq');

-- Insert ApexBank demo site
INSERT INTO sites (site_id, domain, name, owner_user_id, allowed_origins) 
VALUES (
    '8cc359fc-63cf-4270-998e-fb5c789c3c95',
    'localhost:5173',
    'ApexBank Demo',
    (SELECT user_id FROM users WHERE email = 'admin@apexbank.com'),
    '["http://localhost:5173", "http://127.0.0.1:5173"]'
);

-- Insert default site configuration
INSERT INTO site_config (site_id, branding, triggers, intents, updated_at) VALUES (
    '8cc359fc-63cf-4270-998e-fb5c789c3c95',
    '{
        "primaryColor": "#0a1628",
        "accentColor": "#d4af37",
        "logoUrl": "/logo.png",
        "name": "Apex Assistant"
    }',
    '{
        "multipleProductViews": {"threshold": 2, "timeWindow": 300},
        "sessionHesitation": {"dwellTime": 45, "scrollDepth": 0.6},
        "ctaHover": {"hoverCount": 2, "noClick": true},
        "navigationLoops": {"threshold": 2},
        "cooldowns": {"afterTrigger": 30, "afterDismiss": 60}
    }',
    '[
        {"id": "compare", "label": "Compare options", "description": "See products side-by-side"},
        {"id": "help_choose", "label": "Help me choose", "description": "Get personalized recommendations"},
        {"id": "exploring", "label": "Just exploring", "description": "Browse without commitment"}
    ]',
    '["button", "a.btn", ".cta", ".apex-cta"]',
    '{
        "url_patterns": ["/loans/*", "/cards/*", "/accounts/*"],
        "dom_selectors": [".product-detail-view", "#product-id"]
    }',
    NOW()
);

-- REMOVED ALTER STATEMENTS (Merged into CREATE TABLE)
UPDATE site_config SET commentary_templates = '{
    "welcome": "Monitoring session for personalized insights.",
    "hesitation": "Taking your time? I can clarify the details for you.",
    "multi_view": "You''ve viewed {n} products - want a side-by-side comparison?",
    "cta_hover": "Interested in {item}? I can show you the eligibility requirements.",
    "revisit": "Back again? Let''s pick up where you left off."
}' WHERE site_id = '8cc359fc-63cf-4270-998e-fb5c789c3c95';

-- Insert sample rationale templates
INSERT INTO rationale_templates (site_id, category, template_text) VALUES
('8cc359fc-63cf-4270-998e-fb5c789c3c95', 'cards', 'This card is relevant as it provides specific value for your {intent} journey.'),
('8cc359fc-63cf-4270-998e-fb5c789c3c95', 'loans', 'On the {title} page, this loan is relevant for comparison based on its competitive rates.'),
('8cc359fc-63cf-4270-998e-fb5c789c3c95', 'accounts', 'This account type is relevant based on your browsing pattern.');

COMMENT ON TABLE sites IS 'Stores registered websites using DAP';
COMMENT ON TABLE site_config IS 'Configuration for each site including branding and triggers';
COMMENT ON TABLE crawl_jobs IS 'Tracks crawling jobs for content indexing';
COMMENT ON TABLE indexed_pages IS 'Stores metadata about crawled and indexed pages';
COMMENT ON TABLE rationale_templates IS 'Templates for generating product rationales';
