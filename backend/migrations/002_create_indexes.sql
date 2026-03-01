-- Indexes per TAD §11.3
CREATE INDEX IF NOT EXISTS idx_crawl_jobs_site_status ON dap.crawl_jobs(site_id, status);
CREATE INDEX IF NOT EXISTS idx_rationale_site_intent ON dap.rationale_templates(site_id, intent);
CREATE INDEX IF NOT EXISTS idx_indexed_pages_site ON dap.indexed_pages(site_id);
CREATE INDEX IF NOT EXISTS idx_indexed_pages_site_indexed ON dap.indexed_pages(site_id, indexed_at DESC);
