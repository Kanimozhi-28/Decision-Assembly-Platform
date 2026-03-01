/**
 * DAP SDK - Multi-Site Ready Platform (UX Restored)
 */
(function () {
    class CommentarySystem {
        constructor(siteId, apiBase) {
            this.siteId = siteId;
            this.apiBase = apiBase;
            this.config = null;
            this.timer = null;
            this.lastAction = "";

            // PERSISTENCE: Restore from sessionStorage if exists (PRD §7.7)
            const savedViews = sessionStorage.getItem('dap_history');
            this.productViews = savedViews ? JSON.parse(savedViews) : [];

            this.dwellStartTime = Date.now();
            this.triggerState = {
                multiView: false,
                hesitation: false,
                explicit: false,
                loop: false,
                ctaHover: false
            };
            this.visitCounts = {};
            this.ctaHoverStart = 0;
            this.lastCtaHover = "";

            this.init();
        }

        async init() {
            try {
                const resp = await fetch(`${this.apiBase}/config/${this.siteId}`);
                this.config = await resp.json();
                this.createUI();
                this.initTracking();
                this.showWelcome();
            } catch (e) {
                console.error("[DAP SDK] Init failed", e);
            }
        }

        createUI() {
            const branding = this.config?.branding || { primaryColor: '#0a1628', accentColor: '#d4af37' };
            this.strip = document.createElement('div');
            this.strip.id = 'dap-commentary-strip';

            // UNIVERSAL THEME: Force light grey background with dark text for maximum legibility
            this.strip.style.cssText = `
                position: fixed !important; bottom: 0 !important; left: 0 !important; width: 100% !important;
                background: #f1f5f9 !important; color: #000000 !important; padding: 12px 24px !important;
                box-shadow: 0 -4px 25px rgba(0,0,0,0.1) !important; z-index: 10000 !important;
                font-family: 'Inter', system-ui, sans-serif !important; display: flex !important;
                align-items: center !important; gap: 20px !important; transition: transform 0.6s cubic-bezier(0.16, 1, 0.3, 1) !important;
                transform: translateY(100%) !important; border-top: 2px solid ${branding.accentColor} !important;
            `;

            this.strip.innerHTML = `
                <div style="display: flex !important; align-items: center !important; gap: 10px !important; flex: 1 !important;">
                    <div id="dap-indicator" style="width: 10px !important; height: 10px !important; background: ${branding.accentColor} !important; border-radius: 50% !important; transition: all 0.3s !important;"></div>
                    <div style="background: ${branding.accentColor} !important; color: #ffffff !important; padding: 2px 8px !important; border-radius: 4px !important; font-weight: 700 !important; font-size: 11px !important;">DAP LIVE</div>
                    <span id="dap-text" style="font-size: 14px !important; color: #000000 !important; font-weight: 700 !important; transition: opacity 0.3s !important; opacity: 1 !important; display: inline !important;">Initializing...</span>
                </div>
                <button id="dap-cta" style="background: ${branding.accentColor} !important; color: #ffffff !important; border: none !important; padding: 8px 16px !important; border-radius: 4px !important; font-weight: 700 !important; font-size: 12px !important; cursor: pointer !important; transition: transform 0.2s !important;">WANT HELP?</button>
            `;
            document.body.appendChild(this.strip);
            this.strip.querySelector('#dap-cta').onclick = () => this.showIntentSelector();
            setTimeout(() => { this.strip.style.transform = 'translateY(0)'; }, 500);

            // Add Pulse Styles
            if (!document.getElementById('dap-style-pulse')) {
                const s = document.createElement('style');
                s.id = 'dap-style-pulse';
                s.innerHTML = `@keyframes dap-pulse { 0% { transform: scale(1); opacity: 1; } 50% { transform: scale(1.5); opacity: 0.5; } 100% { transform: scale(1); opacity: 1; } }`;
                document.head.appendChild(s);
            }
        }

        showWelcome() {
            const name = this.config?.name || "Assistant";
            this.updateUI(`${name}: Monitoring session for personalized insights.`);
        }

        initTracking() {
            this.trackCurrentPage();
            window.addEventListener('popstate', () => this.handleNavChange());
            const self = this;
            ['pushState', 'replaceState'].forEach(m => {
                const orig = history[m];
                history[m] = function () { orig.apply(this, arguments); self.handleNavChange(); };
            });

            // ENRICHMENT: CTA Hover Tracking (PRD §7.2.3)
            document.addEventListener('mouseover', (e) => {
                if (e.target.closest('[id^="dap-"]') || e.target.closest('[class^="dap-"]')) return;

                const ctaSelectors = this.config?.cta_selectors || ['button', 'a.btn', '.cta', '[role="button"]'];
                const isCTA = ctaSelectors.some(sel => e.target.closest(sel));

                if (isCTA) {
                    const text = e.target.innerText?.trim();
                    if (text && text.length > 2) {
                        this.lastCtaHover = text;
                        this.ctaHoverStart = Date.now();
                    }
                }

                const text = e.target.innerText?.trim();
                if (text && text.length > 5 && text.length < 100 && this.lastAction !== text) {
                    this.debounceLog('hover', text);
                    this.lastAction = text;
                }
            });

            document.addEventListener('mouseout', (e) => {
                this.ctaHoverStart = 0;
            });

            setInterval(() => this.checkTriggers(), 5000);
        }

        normalizeUrl(url) {
            try {
                const u = new URL(url);
                return u.origin + u.pathname.replace(/\/$/, "");
            } catch (e) { return url; }
        }

        trackCurrentPage() {
            const url = this.normalizeUrl(window.location.href);
            const path = window.location.pathname;
            const segments = path.split('/').filter(Boolean);
            const exclusions = ["/", "/home", "/index.html", "/about", "/contact", "/faq", "/login"];

            // Loop Detection: Track visit counts
            this.visitCounts = this.visitCounts || {};
            this.visitCounts[url] = (this.visitCounts[url] || 0) + 1;

            // PRODUCT PAGE RULES (TAD §2.2 Alignment)
            const productRules = this.config?.product_page_rules || { url_patterns: [], dom_selectors: [] };

            let isProductPage = false;

            // 1. Check URL Patterns
            if (productRules.url_patterns && productRules.url_patterns.length > 0) {
                isProductPage = productRules.url_patterns.some(pattern => {
                    const regex = new RegExp(pattern.replace(/\*/g, '.*'));
                    return regex.test(path);
                });
            }

            // 2. Check DOM Selectors (Fallback if URL doesn't match)
            if (!isProductPage && productRules.dom_selectors && productRules.dom_selectors.length > 0) {
                isProductPage = productRules.dom_selectors.some(sel => document.querySelector(sel));
            }

            // 3. Current fallback if no rules defined
            if (!isProductPage && (!productRules.url_patterns?.length && !productRules.dom_selectors?.length)) {
                isProductPage = !exclusions.includes(path) && segments.length >= 2;
            }

            if (isProductPage) {
                if (this.productViews.indexOf(url) === -1) {
                    this.productViews.push(url);
                    if (this.productViews.length > 10) this.productViews.shift();
                    sessionStorage.setItem('dap_history', JSON.stringify(this.productViews));
                }
            }
        }

        handleNavChange() {
            this.trackCurrentPage();
            this.dwellStartTime = Date.now();
            this.triggerState.hesitation = false;
        }

        getRelevantHistory() {
            const currentPath = window.location.pathname;
            const segments = currentPath.split('/').filter(Boolean);
            if (segments.length === 0) return [];
            const activeRoot = segments[0];
            return this.productViews.filter(url => {
                try {
                    const path = new URL(url).pathname;
                    return path.includes(`/${activeRoot}`);
                } catch (e) { return false; }
            });
        }

        checkTriggers() {
            // DISMISSAL / COOLDOWN CHECK (PRD §7.2.5)
            const sessionsDismissals = parseInt(sessionStorage.getItem('dap_dismissals') || '0');
            if (sessionsDismissals >= 2) return; // Silent suppression

            const lastTrigger = parseInt(sessionStorage.getItem('dap_last_trigger') || '0');
            if (Date.now() - lastTrigger < 30000) return; // 30s Cooldown

            if (this.triggerState.explicit) return;

            const name = this.config?.name || "Assistant";
            const relevantCount = this.getRelevantHistory().length;
            const triggers = this.config?.triggers || {};
            const dwellTime = (Date.now() - this.dwellStartTime) / 1000;

            // Priority 1: Navigation Loop (PRD E7)
            const loopThreshold = triggers.navigationLoops?.threshold || 2;
            const currentUrl = this.normalizeUrl(window.location.href);
            if (this.visitCounts[currentUrl] >= loopThreshold && !this.triggerState.loop) {
                this.triggerState.loop = true;
                this.updateUI(`${name}: I noticed you've returned to this page a few times. Need specific details?`, true);
                sessionStorage.setItem('dap_last_trigger', Date.now());
                return;
            }

            // Priority 2: CTA Hover (PRD E5)
            const hoverDuration = this.ctaHoverStart ? (Date.now() - this.ctaHoverStart) : 0;
            if (hoverDuration > 3000 && !this.triggerState.ctaHover) {
                this.triggerState.ctaHover = true;
                this.updateUI(`${name}: Unsure about clicking "${this.lastCtaHover}"? Let's check the requirements together.`, true);
                sessionStorage.setItem('dap_last_trigger', Date.now());
                return;
            }

            // Priority 3: Multi-View
            if (relevantCount >= (triggers.multipleProductViews?.threshold || 2) && !this.triggerState.multiView) {
                this.triggerState.multiView = true;
                this.updateUI(`${name}: Comparing ${relevantCount} options? I can give you a side-by-side view.`, true);
                sessionStorage.setItem('dap_last_trigger', Date.now());
                return;
            }

            // Priority 4: Hesitation
            if (dwellTime > (triggers.sessionHesitation?.dwellTime || 45) && !this.triggerState.hesitation) {
                this.triggerState.hesitation = true;
                this.updateUI(`${name}: Taking your time? I can clarify the details for you.`, true);
                sessionStorage.setItem('dap_last_trigger', Date.now());
            }
        }

        debounceLog(type, metadata) {
            clearTimeout(this.timer);
            this.timer = setTimeout(() => this.logBehavior(type, metadata), 1500);
        }

        async logBehavior(type, metadata) {
            this.setThinkingState(true);
            try {
                const dwell = (Date.now() - this.dwellStartTime) / 1000;
                const safePayload = {
                    site_id: String(this.siteId || ""),
                    type: String(type || "unknown"),
                    metadata: String(metadata || "").substring(0, 500),
                    url: String(window.location.href),
                    history: this.getRelevantHistory(),
                    dwell_time: Number(dwell) || 0.0
                };

                const res = await fetch(`${this.apiBase}/behavior/analyze`, {
                    method: 'POST',
                    body: JSON.stringify(safePayload),
                    headers: { 'Content-Type': 'application/json' }
                });
                const data = await res.json();
                if (data.commentary) this.updateUI(data.commentary);
            } finally { this.setThinkingState(false); }
        }

        updateUI(text, highlight = false) {
            const el = this.strip?.querySelector('#dap-text');
            const ind = this.strip?.querySelector('#dap-indicator');
            const accent = this.config?.branding?.accentColor || '#d4af37';

            if (el) {
                el.style.opacity = '0';
                setTimeout(() => {
                    el.innerText = text;
                    el.style.opacity = '1';
                    el.style.color = (highlight ? accent : '#000000') + ' !important';
                    el.style.fontWeight = (highlight ? '700' : '700') + ' !important'; // Keep bold for clarity
                    if (ind) ind.style.background = (highlight ? '#00ff00' : accent) + ' !important';
                }, 300);
            }
        }

        setThinkingState(isThinking) {
            const ind = this.strip?.querySelector('#dap-indicator');
            if (ind) ind.style.animation = isThinking ? 'dap-pulse 1.5s infinite' : 'none';
        }

        showIntentSelector() {
            this.triggerState.explicit = true;
            if (document.getElementById('dap-intent-modal')) return;
            const modal = document.createElement('div');
            modal.id = 'dap-intent-modal';
            const branding = this.config?.branding || { primaryColor: '#0a1628', accentColor: '#d4af37' };

            modal.style.cssText = `
                position: fixed; bottom: 80px; right: 24px; width: 340px;
                background: #fff; color: #0a1628; border-radius: 12px; border: 1px solid #eee;
                box-shadow: 0 10px 40px rgba(0,0,0,0.2); z-index: 10001; overflow: hidden;
                font-family: 'Inter', sans-serif;
            `;

            const intents = this.config?.intents || [{ id: 'compare', label: 'Compare options' }];
            modal.innerHTML = `
                <div style="background: ${branding.primaryColor}; color: #fff; padding: 16px; font-weight: 700; display: flex; justify-content: space-between; align-items: center;">
                    <span style="letter-spacing: 0.5px; font-size: 11px;">CHOOSE YOUR INTENT</span>
                    <span id="dap-close-modal" style="cursor:pointer; font-size: 20px;">&times;</span>
                </div>
                <div style="padding: 10px;">
                    ${intents.map(i => `
                        <button class="dap-intent-btn" data-intent="${i.id}" style="width:100%; padding:15px; border:none; border-radius: 8px; background:none; text-align:left; cursor:pointer; transition: background 0.2s;">
                            <div style="font-weight:700; font-size: 14px; color: ${branding.primaryColor}">${i.label}</div>
                            <div style="font-size: 11px; color: #666; margin-top: 2px;">${i.description || 'Proceed to assembly'}</div>
                        </button>
                    `).join('')}
                </div>
            `;
            document.body.appendChild(modal);

            // Add Hover effects
            modal.querySelectorAll('.dap-intent-btn').forEach(btn => {
                btn.onmouseenter = () => btn.style.background = '#f5f7fa';
                btn.onmouseleave = () => btn.style.background = 'none';
            });

            modal.querySelector('#dap-close-modal').onclick = () => {
                modal.remove();
                this.triggerState.explicit = false;
            };

            modal.querySelectorAll('.dap-intent-btn').forEach(b => b.onclick = () => {
                this.assembleGrid(b.getAttribute('data-intent'));
                modal.remove();
            });
        }

        async assembleGrid(intent) {
            this.updateUI(`Assembling ${intent.replace('_', ' ')}...`);
            try {
                const relevantHistory = this.getRelevantHistory();
                const res = await fetch(`${this.apiBase}/assemble`, {
                    method: 'POST',
                    body: JSON.stringify({
                        site_id: this.siteId, intent_id: intent,
                        context: {
                            url: window.location.href,
                            page_title: document.title,
                            product_ids: relevantHistory.length > 0 ? relevantHistory : this.productViews
                        }
                    }),
                    headers: { 'Content-Type': 'application/json' }
                });
                const data = await res.json();

                // RESTORE PERSISTENCE: Use saved block order/visibility
                const savedBlocks = sessionStorage.getItem('dap_grid_blocks');
                const savedExpanded = sessionStorage.getItem('dap_grid_expanded_blocks');

                if (savedBlocks) data.blocks = JSON.parse(savedBlocks);
                data.expandedBlocks = savedExpanded ? JSON.parse(savedExpanded) : [];

                this.renderGrid(data);
            } catch (e) { this.updateUI("Error assembling grid."); }
        }

        saveGridState(overlay) {
            const blocks = Array.from(overlay.querySelectorAll('.dap-block span:first-child')).map(s => s.innerText);
            sessionStorage.setItem('dap_grid_blocks', JSON.stringify(blocks));

            const expanded = Array.from(overlay.querySelectorAll('.dap-block-content[style*="display: block"]'))
                .map(el => el.getAttribute('data-block-name'));
            sessionStorage.setItem('dap_grid_expanded_blocks', JSON.stringify(expanded));
        }

        renderGrid(data) {
            if (document.getElementById('dap-grid-overlay')) return;

            // PERSISTENCE: Save assembly state
            sessionStorage.setItem('dap_last_grid', JSON.stringify(data));

            const overlay = document.createElement('div');
            overlay.id = 'dap-grid-overlay';
            const branding = this.config?.branding || { primaryColor: '#0a1628', accentColor: '#d4af37' };

            overlay.style.cssText = `
                position: fixed; top: 0; left: 0; width: 100%; height: 100%;
                background: rgba(10, 22, 40, 0.98); z-index: 10002; display: flex;
                flex-direction: column; padding: 60px; color: #fff; overflow-y: auto;
                font-family: 'Inter', sans-serif;
            `;

            const categoryLabel = data.category ? data.category.toUpperCase() : "ASSEMBLY";

            overlay.innerHTML = `
                <div style="max-width:1200px; margin:0 auto; width:100%;">
                    <div style="display:flex; justify-content:space-between; align-items: center; margin-bottom:40px; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 20px;">
                        <div>
                            <div style="color: ${branding.accentColor}; font-size: 12px; font-weight: 800; letter-spacing: 2px; margin-bottom: 5px;">DECISION ${categoryLabel}</div>
                            <h1 style="font-size:36px; margin:0; font-weight: 800;">${data.intent ? data.intent.replace('_', ' ').toUpperCase() : 'GRID'}</h1>
                        </div>
                        <span id="dap-grid-close" style="font-size:40px; cursor:pointer; color: rgba(255,255,255,0.5);">&times;</span>
                    </div>
                    
                    <div id="dap-product-grid" style="display:grid; grid-template-columns: repeat(auto-fill, minmax(320px, 1fr)); gap:30px;">
                        ${(data.items || []).map(item => `
                            <div class="dap-product-card" style="background:rgba(255,255,255,0.03); padding:32px; border-radius:16px; border: 1px solid rgba(255,255,255,0.08); display:flex; flex-direction:column; position: relative;">
                                <h3 style="margin-top:0; font-size: 20px; line-height: 1.2;">${item.title}</h3>
                                <p style="font-size:13px; color:#94a3b8; flex:1; line-height: 1.5; margin-bottom: 24px;">${item.description}</p>
                                
                                <div style="background:rgba(212,175,55,0.05); border-radius: 8px; padding:16px; margin-bottom: 24px;">
                                    <div style="color: ${branding.accentColor}; font-size: 10px; font-weight: 800; margin-bottom: 8px;">ASSISTANT RATIONALE</div>
                                    <div style="font-size:13px; font-style: italic; color: #cbd5e1;">"${item.rationale}"</div>
                                </div>
                                
                                <a href="${item.url}" style="display:block; background:${branding.accentColor}; color:${branding.primaryColor}; text-align:center; padding:14px; border-radius:8px; text-decoration:none; font-weight:800; font-size: 14px;">DETAILS</a>
                            </div>
                        `).join('')}
                    </div>

                    <div style="margin-top: 60px; padding-top: 30px; border-top: 1px solid rgba(255,255,255,0.1);">
                        <h4 style="font-size: 14px; color: rgba(255,255,255,0.4); margin-bottom: 20px;">NEXT STEP BLOCKS (DRAG TO REORDER)</h4>
                        <div id="dap-block-container" style="display:flex; gap: 15px; flex-wrap: wrap;">
                            ${(data.blocks || []).map((b, idx) => {
                const isExpanded = data.expandedBlocks?.includes(b);
                return `
                                <div class="dap-block-wrapper" style="display:flex; flex-direction:column; gap:5px;">
                                    <div class="dap-block" draggable="true" data-index="${idx}" style="padding: 10px 16px; background: rgba(255,255,255,0.08); border: 1px solid rgba(255,255,255,0.1); border-radius: 8px; font-size: 12px; font-weight: 700; color: #fff; cursor: move; display:flex; align-items:center; gap:12px; transition: background 0.2s;">
                                        <span class="dap-block-toggle" style="cursor:pointer; font-size:16px; width: 20px; text-align: center;">${isExpanded ? '▼' : '▶'}</span>
                                        <span style="flex: 1;">${b}</span>
                                        <span class="dap-remove-block" style="cursor:pointer; opacity:0.4; font-size:18px; line-height: 1;">&times;</span>
                                    </div>
                                    <div class="dap-block-content" data-block-name="${b}" style="display: ${isExpanded ? 'block' : 'none'}; padding: 15px; background: rgba(255,255,255,0.02); border-radius: 6px; font-size: 13px; color: rgba(255,255,255,0.8); max-width: 400px; line-height: 1.6; border-left: 2px solid ${branding.accentColor};">
                                        ${isExpanded ? 'Analyzing context...' : 'Click to analyze...'}
                                    </div>
                                </div>
                            `}).join('')}
                        </div>
                    </div>
                </div>
            `;
            document.body.appendChild(overlay);

            // Interaction: Drag & Drop
            const container = overlay.querySelector('#dap-block-container');
            let draggedItem = null;

            container.querySelectorAll('.dap-block').forEach(block => {
                block.addEventListener('dragstart', (e) => {
                    draggedItem = block;
                    setTimeout(() => block.style.display = 'none', 0);
                });
                block.addEventListener('dragend', () => {
                    setTimeout(() => {
                        draggedItem.style.display = 'flex';
                        draggedItem = null;
                        this.saveGridState(overlay);
                    }, 0);
                });
                block.addEventListener('dragover', (e) => e.preventDefault());
                block.addEventListener('drop', (e) => {
                    e.preventDefault();
                    if (draggedItem) {
                        container.insertBefore(draggedItem, block);
                    }
                });
            });

            // Interaction: Expand/Collapse
            container.querySelectorAll('.dap-block-toggle').forEach(btn => {
                btn.onclick = async (e) => {
                    const wrapper = e.target.closest('.dap-block-wrapper');
                    const content = wrapper.querySelector('.dap-block-content');
                    const isNowExpanded = content.style.display === 'none';

                    if (isNowExpanded) {
                        content.style.display = 'block';
                        btn.innerText = '▼';

                        // Fetch content if it's the placeholder or empty
                        if (content.innerText.includes('Click to analyze') || content.innerText.includes('Analyzing context')) {
                            content.innerHTML = '<div class="dap-loading-dots">Analyzing patterns...</div>';
                            try {
                                const blockName = content.getAttribute('data-block-name');
                                const res = await fetch(`${this.apiBase}/block-content`, {
                                    method: 'POST',
                                    headers: { 'Content-Type': 'application/json' },
                                    body: JSON.stringify({
                                        site_id: this.siteId,
                                        block_id: blockName,
                                        product_ids: this.getRelevantHistory().length > 0 ? this.getRelevantHistory() : this.productViews
                                    })
                                });
                                const result = await res.json();
                                content.innerHTML = `
                                    <div style="font-weight: 800; font-size: 11px; color: ${this.config?.branding?.accentColor || '#d4af37'}; letter-spacing: 1px; margin-bottom: 12px; text-transform: uppercase;">
                                        ${blockName}
                                    </div>
                                    <div style="color: rgba(255,255,255,0.9);">${result.content}</div>
                                `;
                            } catch (err) {
                                content.innerText = 'Failed to load contextual analysis.';
                            }
                        }
                    } else {
                        content.style.display = 'none';
                        btn.innerText = '▶';
                    }
                    this.saveGridState(overlay);
                };
            });

            // Interaction: Remove Block
            container.querySelectorAll('.dap-remove-block').forEach(btn => {
                btn.onclick = (e) => {
                    e.target.closest('.dap-block-wrapper').remove();
                    this.saveGridState(overlay);
                };
            });

            overlay.querySelector('#dap-grid-close').onclick = () => {
                overlay.remove();
                this.triggerState.explicit = false;

                // Track Dismissal (PRD §7.2.5)
                const d = parseInt(sessionStorage.getItem('dap_dismissals') || '0') + 1;
                sessionStorage.setItem('dap_dismissals', d);
                sessionStorage.setItem('dap_last_trigger', Date.now()); // Start cooldown on close
            };
        }
    }

    const s = document.querySelector('script[data-site-id]');
    if (s) window.dap = new CommentarySystem(s.getAttribute('data-site-id'), s.getAttribute('data-api-base'));
})();
