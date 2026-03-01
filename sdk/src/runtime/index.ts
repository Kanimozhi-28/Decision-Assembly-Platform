import { Stripper } from './strip';
import { EventRecorder } from './events';
import { CommentaryUI } from './commentary';
import { AdminToolbar } from './admin';
import { TriggerSystem } from './triggers';

export class DAPRuntime {
    private siteId: string;
    private config: any = null;
    private baseUrl: string = 'http://localhost:8000';
    private events: EventRecorder | null = null;
    private ui: CommentaryUI | null = null;
    private triggers: TriggerSystem | null = null;
    private admin: AdminToolbar | null = null;
    private ready: boolean = false;

    constructor(siteId: string) {
        this.siteId = siteId;
        console.log(`[DAP] Runtime initialized for site: ${siteId}`);
    }

    async init() {
        try {
            // 1. Fetch Config (with 5s timeout)
            try {
                const controller = new AbortController();
                const timeoutId = setTimeout(() => controller.abort(), 5000);

                const configResp = await fetch(`${this.baseUrl}/sites/${this.siteId}/config`, {
                    signal: controller.signal
                });

                clearTimeout(timeoutId);

                if (configResp.ok) {
                    this.config = await configResp.json();
                    if ((window as any).DAP) {
                        (window as any).DAP.config = this.config;
                    }
                    // Refresh UI if it already exists
                    if (this.ui) {
                        this.ui.refreshPresence();
                    }
                }
            } catch (configError) {
                console.warn('[DAP] Config fetch failed or timed out, using defaults.', configError);
            }

            // 2. Wait for document.body to be ready
            if (!document.body) {
                console.log('[DAP] Waiting for document.body...');
                await new Promise<void>(resolve => {
                    const checkBody = () => {
                        if (document.body) {
                            resolve();
                        } else {
                            setTimeout(checkBody, 50);
                        }
                    };
                    checkBody();
                });
            }

            // 3. Init Subsystems
            this.events = new EventRecorder(this.siteId);
            this.ui = new CommentaryUI();
            this.ui.render();

            this.triggers = new TriggerSystem(this.siteId, this.config?.trigger_thresholds);

            // 3. Admin Toolbar (Universal DAG Control)
            const urlParams = new URLSearchParams(window.location.search);
            const isAdmin = urlParams.get('dap_admin') === 'true' || localStorage.getItem('dap_admin_mode') === 'true';

            if (isAdmin) {
                console.log('[DAP] Admin mode detected. Initializing toolbar.');
                this.admin = new AdminToolbar(this.siteId);
                this.admin.render();
                localStorage.setItem('dap_admin_mode', 'true');
            }

            // 3. Behavioral Triggers (FR-002, FR-007)
            this.setupBehavioralTriggers();

            // 4. Handle Assembly Request (PRD FR-015)
            window.addEventListener('dap-request-assembly', (e: any) => {
                const intent = e.detail?.intent || 'help_me_choose';
                this.fetchInsights(intent);
            });

            // 5. CTA Hover Trigger (PRD FR-008)
            this.setupCTAHoverTracking();

            // 6. Start Trigger Polling
            setInterval(() => this.checkBehavioralTriggers(), 2000);

            this.ready = true;
            console.log('[DAP] Runtime ready');

        } catch (error) {
            console.error('[DAP] Initialization failed:', error);
        }
    }

    private checkBehavioralTriggers() {
        if (!this.triggers || !this.ui || this.ui.getIsOpen()) return;

        const trigger = this.triggers.checkTriggers();
        if (trigger) {
            this.ui.showTriggerSuggestion(
                trigger.message,
                () => this.ui?.showIntentMenu(),
                () => this.triggers?.dismiss()
            );
        }
    }

    private setupCTAHoverTracking() {
        // Look for buttons that look like CTAs
        const ctas = document.querySelectorAll('button, .button, .btn, a.btn, a[class*="button"]');
        ctas.forEach(cta => {
            cta.addEventListener('mouseenter', () => {
                this.triggers?.reportCTAInteraction('hover');
            });
            cta.addEventListener('click', () => {
                this.triggers?.reportCTAInteraction('click');
            });
        });
    }

    private get storageKey(): string {
        return `dap_views_${this.siteId}`;
    }

    private setupBehavioralTriggers() {
        if (!this.ui) return;

        // Cleanup stale data on start
        this.pruneOldViews();

        this.trackProductView();
        // this.updateDynamicCommentary(); // Removed to prioritize real-time behavior
    }

    private trackProductView() {
        // Normalize URL: remove hash and query params
        const url = window.location.href.split('#')[0].split('?')[0];

        // Dynamic detection (PRD FR-006)
        let isProductPage = url.includes('product-'); // Default heuristic

        if (this.config && this.config.product_page_rules) {
            try {
                const rules = typeof this.config.product_page_rules === 'string'
                    ? JSON.parse(this.config.product_page_rules)
                    : this.config.product_page_rules;

                if (Array.isArray(rules)) {
                    isProductPage = rules.some((rule: string) => url.includes(rule));
                }
            } catch (e) {
                console.warn('[DAP] Failed to parse product_page_rules', e);
            }
        }

        if (isProductPage) {
            const products = this.getRawViewedProducts();
            const now = Date.now();

            const existingIdx = products.findIndex(p => p.url === url);
            if (existingIdx > -1) {
                products[existingIdx].timestamp = now;
            } else {
                products.push({ url, timestamp: now });
            }

            localStorage.setItem(this.storageKey, JSON.stringify(products));
            console.log(`[DAP] Product tracked: ${url}`);
        }
    }

    private getRawViewedProducts(): { url: string, timestamp: number }[] {
        const stored = localStorage.getItem(this.storageKey);
        if (!stored) return [];
        try {
            const parsed = JSON.parse(stored);
            if (!Array.isArray(parsed)) return [];
            return parsed.filter(p => typeof p === 'object' && p.url && p.timestamp);
        } catch (e) {
            return [];
        }
    }

    private getViewedProducts(): string[] {
        const now = Date.now();
        const fiveMinutes = 5 * 60 * 1000;
        const active = this.getRawViewedProducts()
            .filter(p => (now - p.timestamp) < fiveMinutes);

        if (active.length > 0) {
            console.log('[DAP] Session Views:', active.map(p => p.url));
        }
        return active.map(p => p.url);
    }

    private pruneOldViews() {
        const now = Date.now();
        const fiveMinutes = 5 * 60 * 1000;
        const products = this.getRawViewedProducts().filter(p => (now - p.timestamp) < fiveMinutes);
        localStorage.setItem(this.storageKey, JSON.stringify(products));
    }

    private getVisibleProducts(): string[] {
        const productUrls: string[] = [];
        const rules = this.config?.product_page_rules || ["product-", "product_", "service-", "item-", "loan", "card", "saving", "banking", "account", "detail"];

        console.log('[DAP-DEBUG] getVisibleProducts called. Rules:', rules);

        // 1. Identify "Product Cards" or items with links
        const allLinks = document.querySelectorAll('a');
        console.log('[DAP-DEBUG] Total links on page:', allLinks.length);

        const candidateLinks: HTMLAnchorElement[] = [];

        allLinks.forEach(link => {
            const href = link.href.split('#')[0].split('?')[0];
            if (rules.some((rule: string) => href.includes(rule))) {
                candidateLinks.push(link);
            }
        });

        console.log('[DAP-DEBUG] Candidate links matching rules:', candidateLinks.length, candidateLinks.map(l => l.href));

        // 2. Section Visibility Lock (SL-001)
        // We look for products that are in the "most visible" or "active" part of the page.
        // For simplicity and strict compliance, we filter by the current viewport/page segment.
        candidateLinks.forEach(link => {
            // Relaxed check: Trust the product_page_rules primarily.
            // We only check if the element is not explicitly hidden (display: none).
            const style = window.getComputedStyle(link);
            if (style.display !== 'none' && style.visibility !== 'hidden') {
                const url = link.href.split('#')[0].split('?')[0];
                if (!productUrls.includes(url)) {
                    productUrls.push(url);
                }
            } else {
                console.log('[DAP-DEBUG] Link ignored (CSS hidden):', link.href);
            }
        });

        console.log('[DAP-DEBUG] Final Visible Product URLs:', productUrls);

        // Limit to 6 candidates for backend to pick top 4 from
        return productUrls.slice(0, 6);
    }

    private updateDynamicCommentary() {
        const products = this.getViewedProducts();
        const count = products.length;
        // Generic page title for initial message
        const websiteName = document.title.split(/[|\-–—]/)[0].trim();

        if (count >= 3) {
            this.ui?.updateStripText("Comparison available for the plans you've viewed.");
        } else if (count === 2) {
            this.ui?.updateStripText("Looking at two different options.");
        } else if (count === 1) {
            this.ui?.updateStripText("Reviewing specific details.");
        } else {
            this.ui?.updateStripText(`You're on ${websiteName}.`);
        }
    }

    private async fetchInsights(intent: string = 'help_me_choose') {
        if (!this.ui) return;

        this.ui.showGrid(); // Show the grid immediately with its default loading state

        try {
            const response = await fetch(`${this.baseUrl}/assemble/`, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({
                    site_id: this.siteId,
                    intent: intent,
                    context: {
                        page_title: document.title,
                        url: window.location.href,
                        product_ids: this.getViewedProducts(),
                        visible_product_urls: this.getVisibleProducts()
                    }
                })
            });

            if (!response.ok) throw new Error('Assemble failed');
            const data = await response.json();

            // Delegate all rendering and event binding to the UI class (PRD v1.2 Modular Grid)
            this.ui.updateGridContent(data);

        } catch (error) {
            console.error('[DAP] Assemble error:', error);
            this.ui.updateGridContent({
                intent: 'error',
                blocks: [{
                    type: 'error',
                    message: 'Failed to assemble. Please try again later.',
                    products: []
                }],
                rationales: {}
            });
        }
    }

    private handleEvent(event: any) {
        console.log('[DAP] Processing event:', event);
    }
}

// Auto-boot if global exists
(function () {
    const dap = (window as any).DAP;
    if (dap && dap.siteId) {
        const runtime = new DAPRuntime(dap.siteId);
        runtime.init();
    }
})();
