export class CommentaryUI {
    private container: HTMLElement | null = null;
    private grid: HTMLElement | null = null;
    private strip: HTMLElement | null = null;
    private intentMenu: HTMLElement | null = null;
    private rationalePanel: HTMLElement | null = null;
    private isOpen: boolean = false;
    private lastAction: string = '';
    private actionTimeout: any = null;
    private isProcessing: boolean = false;
    private behaviorTimer: any = null;

    private static readonly STYLES = `
        :root {
            --dap-primary-color: #74b9ff;
            --dap-secondary-color: #ff4d6d;
            --dap-success-color: #34c759;
            --dap-text-color: #1d1d1f;
            --dap-bg-color: #ffffff;
            --dap-border-radius: 40px;
        }
        #dap-commentary-strip {
            position: fixed;
            bottom: 20px;
            left: 50%;
            transform: translateX(-50%);
            width: 94%;
            max-width: 900px;
            min-height: 64px;
            height: auto;
            background: var(--dap-bg-color);
            color: var(--dap-text-color);
            display: flex;
            align-items: center;
            justify-content: space-between;
            padding: 12px 28px;
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
            font-size: 15px;
            z-index: 1000000;
            border: 3px solid var(--dap-primary-color);
            border-radius: var(--dap-border-radius);
            box-shadow: 0 12px 40px rgba(0,0,0,0.12);
            box-sizing: border-box;
            gap: 20px;
        }
        .dap-strip-content {
            display: flex;
            align-items: center;
            gap: 16px;
            flex: 1;
            min-width: 0;
        }
        #dap-strip-text {
            white-space: normal;
            word-break: break-word;
            line-height: 1.5;
            flex: 1;
            font-weight: 500;
        }
        .dap-right-actions {
            display: flex;
            align-items: center;
            flex-shrink: 0;
            gap: 12px;
        }
        .dap-search-icon {
            color: #ff4d6d;
            font-size: 20px;
            display: flex;
            align-items: center;
        }
        .dap-pulse {
            width: 10px;
            height: 10px;
            background: #34c759;
            border-radius: 50%;
            margin-right: 5px;
            animation: dap-pulse-anim 2s infinite;
        }
        @keyframes dap-pulse-anim {
            0% { transform: scale(0.95); box-shadow: 0 0 0 0 rgba(52, 199, 89, 0.7); }
            70% { transform: scale(1); box-shadow: 0 0 0 8px rgba(52, 199, 89, 0); }
            100% { transform: scale(0.95); box-shadow: 0 0 0 0 rgba(52, 199, 89, 0); }
        }
        .dap-intent-trigger {
            background: #000;
            color: white;
            border: none;
            padding: 10px 24px;
            border-radius: 30px;
            font-weight: 600;
            cursor: pointer;
            font-size: 14px;
            transition: all 0.2s;
            margin-left: 10px;
        }
        .dap-intent-trigger:hover {
            background: #333;
            transform: scale(1.05);
        }
        
        #dap-grid-assembly {
            position: fixed;
            bottom: 60px;
            left: 50%;
            transform: translateX(-50%) translateY(120%);
            width: 90%;
            max-width: 1200px;
            background: rgba(255, 255, 255, 0.98);
            backdrop-filter: blur(20px);
            border-radius: 20px;
            box-shadow: 0 20px 60px rgba(0,0,0,0.15);
            z-index: 999998;
            padding: 32px;
            max-height: 80vh;
            overflow-y: auto;
            transition: transform 0.6s cubic-bezier(0.16, 1, 0.3, 1);
            border: 1px solid rgba(0,0,0,0.05);
        }
        #dap-grid-assembly.open {
            transform: translateX(-50%) translateY(0);
        }
        .dap-grid-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 24px;
        }
        .dap-close-grid {
            cursor: pointer;
            font-size: 24px;
            color: #8e8e93;
        }
        
        .dap-products-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
            gap: 24px;
            justify-content: center;
            max-width: 100%;
        }
        .dap-grid-block {
            margin-bottom: 40px;
            border-bottom: 1px solid rgba(0,0,0,0.05);
            padding-bottom: 24px;
        }
        .dap-grid-block:last-child {
            margin-bottom: 0;
            border-bottom: none;
        }
            gap: 10px;
        }
        .dap-block-title::before {
            content: "";
            display: inline-block;
            width: 4px;
            height: 18px;
            background: #74b9ff;
            border-radius: 2px;
        }
        
        /* New Block Types */
        .dap-empty-block {
            background: #f8f9fa;
            border: 2px dashed #dee2e6;
            border-radius: 12px;
            padding: 32px;
            text-align: center;
        }
        .dap-pull-chips {
            display: flex;
            flex-wrap: wrap;
            gap: 10px;
            justify-content: center;
            margin-top: 20px;
        }
        .dap-pull-chip {
            background: white;
            border: 1px solid #74b9ff;
            color: #74b9ff;
            padding: 8px 16px;
            border-radius: 20px;
            font-size: 13px;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.2s;
        }
        .dap-pull-chip:hover {
            background: #74b9ff;
            color: white;
        }
        .dap-custom-query-form {
            display: flex;
            gap: 10px;
            margin-top: 15px;
        }
        .dap-query-input {
            flex: 1;
            padding: 10px 16px;
            border: 1px solid #ced4da;
            border-radius: 8px;
            font-size: 14px;
        }
        .dap-query-btn {
            background: #000;
            color: white;
            border: none;
            padding: 10px 20px;
            border-radius: 8px;
            font-weight: 600;
            cursor: pointer;
        }
        .dap-product-card {
            background: white;
            border-radius: 16px;
            padding: 24px;
            border: 1px solid rgba(0,0,0,0.08);
            box-shadow: 0 10px 30px rgba(0,0,0,0.02);
            transition: all 0.3s;
        }
        .dap-product-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 15px 40px rgba(0,0,0,0.05);
        }
        .dap-product-title {
            font-weight: 700;
            font-size: 18px;
            margin-bottom: 8px;
            color: #1c1c1e;
        }
        .dap-product-price {
            font-size: 16px;
            color: #34c759;
            font-weight: 700;
            margin-bottom: 16px;
        }
        .dap-product-rationale {
            font-size: 14px;
            color: #636366;
            margin-bottom: 20px;
            line-height: 1.5;
            background: #f2f2f7;
            padding: 12px;
            border-radius: 10px;
        }
        .dap-view-btn {
            display: block;
            background: #000;
            color: white;
            padding: 12px;
            border-radius: 12px;
            font-size: 14px;
            text-decoration: none;
            font-weight: 600;
            text-align: center;
        }

        /* Modular Block Controls */
        .dap-block-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 20px;
        }
        .dap-block-controls {
            display: flex;
            gap: 12px;
            margin-left: auto;
        }
        .dap-block-control {
            cursor: pointer;
            color: #8e8e93;
            font-size: 18px;
            transition: color 0.2s;
            user-select: none;
        }
        .dap-block-control:hover {
            color: #1c1c1e;
        }
        .dap-drag-handle {
            cursor: grab;
            padding: 4px;
        }
        .dap-drag-handle:active {
            cursor: grabbing;
        }
        .dap-grid-block.collapsed .dap-products-grid,
        .dap-grid-block.collapsed .dap-block-message {
            display: none;
        }
        .dap-grid-block.dragging {
            opacity: 0.5;
            border: 2px dashed #74b9ff;
        }

        #dap-intent-menu {
            position: fixed;
            bottom: 100px;
            left: 50%;
            transform: translateX(-50%) translateY(20px);
            width: 90%;
            max-width: 600px;
            background: rgba(255, 255, 255, 0.95);
            backdrop-filter: blur(10px);
            border-radius: 24px;
            padding: 24px;
            box-shadow: 0 15px 35px rgba(0,0,0,0.2);
            z-index: 1000000;
            display: none;
            opacity: 0;
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
            border: 1px solid rgba(0,0,0,0.05);
        }
        #dap-intent-menu.active {
            display: block;
            opacity: 1;
            transform: translateX(-50%) translateY(0);
        }
        .dap-intent-grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 12px;
            margin-top: 16px;
        }
        .dap-intent-option {
            background: #f4f4f7;
            padding: 16px;
            border-radius: 16px;
            cursor: pointer;
            transition: all 0.2s;
            border: 2px solid transparent;
            text-align: left;
        }
        .dap-intent-option:hover {
            background: #e9e9ed;
            border-color: #a0c4ff;
        }
        .dap-intent-option h4 { margin: 0 0 4px 0; color: #1d1d1f; }
        .dap-intent-option p { margin: 0; font-size: 12px; color: #86868b; }

        #dap-rationale-panel {
            position: fixed;
            right: -400px;
            top: 0;
            width: 400px;
            height: 100%;
            background: white;
            box-shadow: -10px 0 30px rgba(0,0,0,0.1);
            z-index: 1000002;
            transition: right 0.3s ease;
            padding: 40px 24px;
            overflow-y: auto;
        }
        #dap-rationale-panel.active { right: 0; }
        .dap-rationale-header { display: flex; justify-content: space-between; align-items: center; margin-bottom: 30px; }
        .dap-rationale-content { line-height: 1.6; color: #333; }
        .dap-rationale-item { 
            background: #f9f9fb; 
            padding: 16px; 
            border-radius: 12px; 
            margin-bottom: 12px;
            border-left: 4px solid #a0c4ff;
        }

        #dap-overlay {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: rgba(0,0,0,0.3);
            backdrop-filter: blur(4px);
            z-index: 999999;
            display: none;
        }
        #dap-overlay.active { display: block; }
        h2 { margin: 0; font-size: 24px; letter-spacing: -0.5px; }
    `;

    public render() {
        // Prevent multiple renders
        if (this.strip && document.getElementById('dap-commentary-strip')) {
            console.log('[DAP] Commentary UI already rendered.');
            return;
        }

        // Inject Styles
        const style = document.createElement('style');
        style.textContent = CommentaryUI.STYLES;
        document.head.appendChild(style);

        // Create Overlay
        const overlay = document.createElement('div');
        overlay.id = 'dap-overlay';
        document.body.appendChild(overlay);

        // Create Strip
        this.strip = document.createElement('div');
        this.strip.id = 'dap-commentary-strip';
        // Get website name from document title or domain
        const websiteName = this.extractWebsiteName();

        this.strip.innerHTML = `
            <div class="dap-strip-content">
                <div class="dap-search-icon">
                    <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round">
                        <circle cx="11" cy="11" r="8"></circle>
                        <line x1="21" y1="21" x2="16.65" y2="16.65"></line>
                    </svg>
                </div>
                <span id="dap-strip-text">You're on ${websiteName}.</span>
            </div>
            <div class="dap-right-actions" id="dap-strip-actions">
                <span class="dap-pulse"></span>
                <button class="dap-intent-trigger" id="dap-open-menu">Help Me Choose</button>
            </div>
        `;
        document.body.appendChild(this.strip);

        // Create Intent Menu (Dynamic Content Placeholder)
        this.intentMenu = document.createElement('div');
        this.intentMenu.id = 'dap-intent-menu';
        this.intentMenu.innerHTML = `
            <h3 style="margin:0 0 16px 0;">How can I help you?</h3>
            <div class="dap-intent-grid" id="dap-intent-grid">
                <!-- Loaded dynamically -->
                <div class="dap-intent-option">
                   <p>Loading options for this site...</p>
                </div>
            </div>
        `;
        document.body.appendChild(this.intentMenu);

        // Create Grid Assembly
        this.grid = document.createElement('div');
        this.grid.id = 'dap-grid-assembly';
        this.grid.innerHTML = `
            <div class="dap-grid-header">
                <h2 id="dap-grid-title">Decision Assembly</h2>
                <span class="dap-close-grid" id="dap-close-grid">&times;</span>
            </div>
            <div id="dap-grid-content">
                <div class="dap-loading">Gathering the details for you...</div>
            </div>
        `;
        document.body.appendChild(this.grid);

        // Create Rationale Panel (PRD FR-023)
        this.rationalePanel = document.createElement('div');
        this.rationalePanel.id = 'dap-rationale-panel';
        document.body.appendChild(this.rationalePanel);

        // Events
        document.getElementById('dap-open-menu')?.addEventListener('click', () => this.showIntentMenu());
        document.getElementById('dap-close-grid')?.addEventListener('click', () => this.hideGrid());
        overlay.addEventListener('click', () => {
            this.hideIntentMenu();
            this.hideRationale();
        });

        // Initialize Behavioral Tracking
        this.initBehaviorTracking();
    }

    private extractWebsiteName(): string {
        // 1. Try to get from config (Single Source of Truth)
        const config = (window as any).DAP?.config;
        if (config?.site_name) return config.site_name;
        if (config?.name) return config.name; // Alternative key

        // 2. Try to extract from document title (Legacy/Fallback)
        const title = document.title;

        // Common patterns to extract brand name from title
        // e.g., "Product Name | Brand Name" or "Brand Name - Tagline"
        if (title) {
            // Split by common separators and take the last meaningful part
            const parts = title.split(/[|\-–—]/);
            if (parts.length > 1) {
                // Usually the brand is at the end or beginning
                const lastPart = parts[parts.length - 1].trim();
                const firstPart = parts[0].trim();

                // Prefer shorter, cleaner names (likely brand names)
                if (lastPart.length < 30 && lastPart.length > 0) {
                    return lastPart;
                }
                if (firstPart.length < 30 && firstPart.length > 0) {
                    return firstPart;
                }
            }

            // If no separator, use the full title if it's short enough
            if (title.length < 40) {
                return title;
            }
        }

        // Fallback to domain name
        const hostname = window.location.hostname;
        // Remove www. and common TLDs
        const domain = hostname.replace(/^www\./, '').split('.')[0];
        // Capitalize first letter
        return domain.charAt(0).toUpperCase() + domain.slice(1);
    }

    private initBehaviorTracking() {
        console.log('[DAP] Initializing Behavioral Tracking...');

        // 1. Hover Tracking (More responsive)
        let hoverTimer: any = null;
        document.addEventListener('mouseover', (e) => {
            const target = e.target as HTMLElement;
            if (!target || target.id?.startsWith('dap-')) return;
            // console.log('[DAP] Mouseover event trigger'); // Reduced noise

            clearTimeout(hoverTimer);
            hoverTimer = setTimeout(() => {
                const text = target.innerText?.trim().substring(0, 150); // Increased context slightly
                if (text && text.length > 3) {
                    this.logBehavior('hover', text);
                }
            }, 200); // Reduced to 200ms for snappier feel
        });

        // 2. Selection Tracking
        document.addEventListener('mouseup', () => {
            const selection = window.getSelection();
            const text = selection?.toString().trim();
            if (text && text.length > 2) {
                this.logBehavior('select', text);
            }
        });

        // 3. Scroll Tracking (Debounced)
        let scrollTimer: any = null;
        window.addEventListener('scroll', () => {
            clearTimeout(scrollTimer);
            scrollTimer = setTimeout(() => {
                const scrollPct = Math.round((window.scrollY / (document.documentElement.scrollHeight - window.innerHeight)) * 100);
                this.logBehavior('scroll', `Scrolled to ${scrollPct}%`);
            }, 500); // Reduced to 500ms
        });

        // 3. Click Tracking
        document.addEventListener('click', (e) => {
            const target = e.target as HTMLElement;
            if (!target || target.id?.startsWith('dap-')) return;

            const text = target.innerText?.trim().substring(0, 50);
            if (text) {
                this.logBehavior('click', text);
            }
        });
    }

    private async logBehavior(type: string, metadata: string) {
        if (this.isProcessing) {
            console.log('[DAP] Behavior log already in progress, skipping...');
            return;
        }

        // Avoid duplicate spam
        const actionKey = `${type}:${metadata}`;
        if (this.lastAction === actionKey) return;
        this.lastAction = actionKey;

        this.isProcessing = true;
        console.log(`[DAP] Analyzing Behavior: ${type} - ${metadata}`);

        // OPTIMISTIC UI: Show thinking state immediately
        this.setThinking(true);

        try {
            const siteId = (window as any).DAP?.siteId;
            const controller = new AbortController();
            const timeoutId = setTimeout(() => controller.abort(), 60000);

            const response = await fetch('http://localhost:8000/behavior/analyze', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                signal: controller.signal,
                body: JSON.stringify({
                    site_id: siteId,
                    type,
                    metadata,
                    url: window.location.href
                })
            });

            clearTimeout(timeoutId);

            if (response.ok) {
                const data = await response.json();
                if (data.commentary) {
                    this.updateStripText(data.commentary);
                }
            } else {
                console.warn(`[DAP] Backend returned status: ${response.status}`);
            }
        } catch (e) {
            console.error('[DAP] Behavior log failed:', e);
        } finally {
            this.setThinking(false);
            this.isProcessing = false;
        }
    }

    private setThinking(isThinking: boolean) {
        const pulse = this.strip?.querySelector('.dap-pulse');
        if (pulse) {
            if (isThinking) {
                pulse.classList.add('thinking');
                // Optional: distinct color or speed handled in CSS
                (pulse as HTMLElement).style.backgroundColor = '#34c759'; // Ensure green
                (pulse as HTMLElement).style.animationDuration = '0.5s'; // Fast pulse
            } else {
                pulse.classList.remove('thinking');
                (pulse as HTMLElement).style.animationDuration = '2s'; // Normal pulse
            }
        }
    }

    public async showIntentMenu() {
        document.getElementById('dap-overlay')?.classList.add('active');
        this.intentMenu?.classList.add('active');

        // Fetch specific intents for this site
        await this.loadDynamicIntents();
    }

    private async loadDynamicIntents() {
        const grid = document.getElementById('dap-intent-grid');
        if (!grid) return;

        // Use siteId from global DAP object
        const siteId = (window as any).DAP?.siteId;
        if (!siteId) return;

        try {
            const response = await fetch(`http://localhost:8000/rationales/${siteId}`);
            if (response.ok) {
                const templates = await response.json();

                if (templates.length > 0) {
                    grid.innerHTML = ''; // Clear loading
                    templates.forEach((t: any) => {
                        const div = document.createElement('div');
                        div.className = 'dap-intent-option';
                        div.setAttribute('data-intent', t.intent);
                        const label = t.intent.replace(/_/g, ' ').replace(/\b\w/g, (l: string) => l.toUpperCase());
                        // Clean template for display (remove placeholders)
                        const cleanText = t.template_text
                            .replace(/{{product_name}}/g, 'products')
                            .replace(/{{price}}/g, 'price')
                            .replace(/{{intent}}/g, label.toLowerCase())
                            .substring(0, 45) + '...';
                        div.innerHTML = `<h4>${label}</h4><p>${cleanText}</p>`;

                        div.addEventListener('click', () => {
                            const intent = div.getAttribute('data-intent');
                            this.hideIntentMenu();
                            const event = new CustomEvent('dap-request-assembly', {
                                bubbles: true,
                                detail: { intent }
                            });
                            window.dispatchEvent(event);
                        });

                        grid.appendChild(div);
                    });
                } else {
                    // Fallback if no specific intents found
                    this.renderDefaultIntents(grid);
                }
            } else {
                this.renderDefaultIntents(grid);
            }
        } catch (e) {
            console.error('[DAP] Failed to load intents', e);
            this.renderDefaultIntents(grid);
        }
    }

    private renderDefaultIntents(grid: HTMLElement) {
        grid.innerHTML = `
            <div class="dap-intent-option" data-intent="help_me_choose">
                <h4>Help me choose</h4>
                <p>Brief guide to top options</p>
            </div>
            <div class="dap-intent-option" data-intent="compare_options">
                <h4>Compare options</h4>
                <p>Detailed side-by-side diffs</p>
            </div>
        `;
        grid.querySelectorAll('.dap-intent-option').forEach(opt => {
            opt.addEventListener('click', () => {
                const intent = opt.getAttribute('data-intent');
                this.hideIntentMenu();
                const event = new CustomEvent('dap-request-assembly', {
                    bubbles: true,
                    detail: { intent }
                });
                window.dispatchEvent(event);
            });
        });
    }

    public hideIntentMenu() {
        document.getElementById('dap-overlay')?.classList.remove('active');
        this.intentMenu?.classList.remove('active');
    }

    public showRationale(title: string, content: string) {
        if (!this.rationalePanel) return;
        this.rationalePanel.innerHTML = `
            <div class="dap-rationale-header">
                <h3>Product Insights</h3>
                <span class="dap-close-grid" id="dap-close-rationale" style="position:static;">&times;</span>
            </div>
            <div class="dap-rationale-content">
                <p><strong>${title}</strong></p>
                <div class="dap-rationale-item">${content}</div>
            </div>
        `;
        this.rationalePanel.classList.add('active');
        document.getElementById('dap-close-rationale')?.addEventListener('click', () => this.hideRationale());
    }

    public hideRationale() {
        this.rationalePanel?.classList.remove('active');
    }

    public updateStripText(text: string) {
        const el = document.getElementById('dap-strip-text');
        if (el) el.innerText = text;

        // FR-024: Auto-reset behavior text to avoid "history" persistence
        clearTimeout(this.behaviorTimer);
        this.behaviorTimer = setTimeout(() => {
            if (el) el.innerText = `You're on ${this.extractWebsiteName()}.`;
            this.lastAction = '';
        }, 15000); // 15 seconds visibility
    }

    public showTriggerSuggestion(message: string, onAccept: () => void, onDismiss: () => void) {
        this.updateStripText(message);

        const actions = document.getElementById('dap-strip-actions');
        if (actions) {
            actions.innerHTML = `
                <button class="dap-intent-trigger" style="background:#34c759;" id="dap-accept-trigger">Get Help</button>
                <button class="dap-intent-trigger" style="background:none; color:#8e8e93; padding: 0 10px;" id="dap-dismiss-trigger">&times;</button>
            `;

            document.getElementById('dap-accept-trigger')?.addEventListener('click', () => {
                onAccept();
                this.resetTriggerActions();
            });

            document.getElementById('dap-dismiss-trigger')?.addEventListener('click', () => {
                onDismiss();
                this.resetTriggerActions();
            });
        }
    }

    private resetTriggerActions() {
        const actions = document.getElementById('dap-strip-actions');
        if (actions) {
            actions.innerHTML = `
                <span class="dap-pulse"></span>
                <button class="dap-intent-trigger" id="dap-open-menu">Help Me Choose</button>
            `;
            document.getElementById('dap-open-menu')?.addEventListener('click', () => this.showIntentMenu());
        }
        this.updateStripText(`You're on ${this.extractWebsiteName()}.`);
    }

    public updateGridContent(data: any) {
        const content = document.getElementById('dap-grid-content');
        if (!content) return;

        const { blocks, rationales, intent } = data;
        const title = intent.replace(/_/g, ' ').toUpperCase();

        const titleEl = document.getElementById('dap-grid-title');
        if (titleEl) titleEl.innerText = title;

        // Restore State from Session
        const stateStr = sessionStorage.getItem('dap_grid_state');
        const state = stateStr ? JSON.parse(stateStr) : { order: [], collapsed: [], removed: [] };

        content.innerHTML = '';

        // Filter and Sort blocks based on state
        let activeBlocks = blocks.filter((b: any) => !state.removed.includes(b.type));
        if (state.order.length > 0) {
            activeBlocks.sort((a: any, b: any) => {
                const idxA = state.order.indexOf(a.type);
                const idxB = state.order.indexOf(b.type);
                if (idxA === -1 && idxB === -1) return 0;
                if (idxA === -1) return 1;
                if (idxB === -1) return -1;
                return idxA - idxB;
            });
        }

        activeBlocks.forEach((block: any) => {
            const isCollapsed = state.collapsed.includes(block.type);
            const blockEl = this.renderBlock(block, rationales, isCollapsed);
            content.appendChild(blockEl);
        });

        this.showGrid();
        this.bindGridEvents();
    }

    private renderBlock(block: any, rationales: any, isCollapsed: boolean): HTMLElement {
        const div = document.createElement('div');
        div.className = `dap-grid-block ${isCollapsed ? 'collapsed' : ''}`;
        div.setAttribute('data-block-type', block.type);
        div.setAttribute('draggable', 'true');

        const blockTitle = block.type.replace(/-/g, ' ').replace(/\b\w/g, (l: string) => l.toUpperCase());

        div.innerHTML = `
            <div class="dap-block-header" style="display:flex; align-items:center;">
                <h3 class="dap-block-title">${blockTitle}</h3>
                <div class="dap-block-controls">
                    <span class="dap-block-control dap-drag-handle" title="Drag to reorder">⠿</span>
                    <span class="dap-block-control dap-toggle-collapse" title="Collapse">${isCollapsed ? '+' : '−'}</span>
                    <span class="dap-block-control dap-remove-block" title="Remove">&times;</span>
                </div>
            </div>
            ${block.message ? `<p class="dap-block-message" style="margin: -10px 0 20px 0; color: #636366; font-size: 14px;">${block.message}</p>` : ''}
            
            ${this.renderBlockBody(block, rationales)}
        `;

        return div;
    }

    private renderBlockBody(block: any, rationales: any): string {
        if (block.type === 'custom-query') {
            return `
                <div class="dap-custom-query-block">
                    <p style="font-size:14px; color:#636366;">Ask a specific question about these products (e.g. "Which is cheapest?")</p>
                    <div class="dap-custom-query-form">
                        <input type="text" class="dap-query-input" placeholder="Type your query...">
                        <button class="dap-query-btn">Ask</button>
                    </div>
                </div>
            `;
        }

        if (!block.products || block.products.length === 0) {
            const chips = ['Pricing', 'Benefits', 'Eligibility', 'Technical Specs', 'Comparison'];
            return `
                <div class="dap-empty-block">
                    <p>Want more specific details? Select a topic below to populate this block.</p>
                    <div class="dap-pull-chips">
                        ${chips.map(c => `<span class="dap-pull-chip" data-topic="${c.toLowerCase()}">${c}</span>`).join('')}
                    </div>
                </div>
            `;
        }

        return `
            <div class="dap-products-grid">
                ${block.products.map((p: any) => this.renderProductCardHtml(p, rationales[p.id])).join('')}
            </div>
        `;
    }

    private renderProductCardHtml(p: any, rationale: string): string {
        return `
            <div class="dap-product-card">
                <div class="dap-product-title">${p.title}</div>
                <div class="dap-product-price">${p.price}</div>
                <button class="dap-intent-trigger dap-why-this" 
                    style="margin: 0 0 16px 0; width: 100%; border:1px solid #000; background:none; color:#000;" 
                    data-title="${p.title}" data-rationale="${rationale || 'Tailored for your needs.'}">Why this?</button>
                <a href="${p.url}" target="_blank" class="dap-view-btn">View Details</a>
            </div>
        `;
    }

    private bindGridEvents() {
        // Rationale buttons
        document.querySelectorAll('.dap-why-this').forEach(btn => {
            btn.addEventListener('click', (e: any) => {
                const title = e.currentTarget.getAttribute('data-title');
                const rat = e.currentTarget.getAttribute('data-rationale');
                this.showRationale(title, rat);
            });
        });

        // Block Controls
        document.querySelectorAll('.dap-toggle-collapse').forEach(btn => {
            btn.addEventListener('click', (e: any) => {
                const block = e.target.closest('.dap-grid-block');
                const type = block.getAttribute('data-block-type');
                block.classList.toggle('collapsed');
                const isCollapsed = block.classList.contains('collapsed');
                e.target.innerText = isCollapsed ? '+' : '−';
                this.updateState('collapsed', type, isCollapsed);
            });
        });

        document.querySelectorAll('.dap-remove-block').forEach(btn => {
            btn.addEventListener('click', (e: any) => {
                const block = e.target.closest('.dap-grid-block');
                const type = block.getAttribute('data-block-type');
                if (confirm(`Remove the ${type} block?`)) {
                    block.remove();
                    this.updateState('removed', type, true);
                }
            });
        });

        // Pull chips
        document.querySelectorAll('.dap-pull-chip').forEach(chip => {
            chip.addEventListener('click', (e: any) => {
                const topic = e.target.getAttribute('data-topic');
                const block = e.target.closest('.dap-grid-block');
                const type = block.getAttribute('data-block-type');

                const event = new CustomEvent('dap-request-assembly', {
                    bubbles: true,
                    detail: { intent: `${type}_${topic}`, isPull: true, blockType: type }
                });
                window.dispatchEvent(event);

                (e.target as HTMLElement).innerText = 'Loading...';
                (e.target as HTMLElement).style.opacity = '0.5';
            });
        });

        // Custom Query
        document.querySelectorAll('.dap-query-btn').forEach(btn => {
            btn.addEventListener('click', (e: any) => {
                const input = (e.target as HTMLElement).previousElementSibling as HTMLInputElement;
                const query = input.value;
                if (!query) return;

                (e.target as HTMLElement).innerText = 'Searching...';
                const event = new CustomEvent('dap-request-assembly', {
                    bubbles: true,
                    detail: { intent: 'custom_query', query }
                });
                window.dispatchEvent(event);
            });
        });

        // Drag & Drop
        const content = document.getElementById('dap-grid-content');
        if (!content) return;

        let draggedBlock: HTMLElement | null = null;

        content.addEventListener('dragstart', (e: any) => {
            draggedBlock = e.target.closest('.dap-grid-block');
            if (draggedBlock) draggedBlock.classList.add('dragging');
        });

        content.addEventListener('dragend', () => {
            if (draggedBlock) draggedBlock.classList.remove('dragging');
            draggedBlock = null;
            this.saveBlockOrder();
        });

        content.addEventListener('dragover', (e: any) => {
            e.preventDefault();
            const afterElement = this.getDragAfterElement(content, e.clientY);
            const draggable = document.querySelector('.dragging');
            if (draggable) {
                if (afterElement == null) {
                    content.appendChild(draggable);
                } else {
                    content.insertBefore(draggable, afterElement);
                }
            }
        });
    }

    private getDragAfterElement(container: HTMLElement, y: number) {
        const draggableElements = Array.from(container.querySelectorAll('.dap-grid-block:not(.dragging)'));

        return draggableElements.reduce((closest: any, child: any) => {
            const box = child.getBoundingClientRect();
            const offset = y - box.top - box.height / 2;
            if (offset < 0 && offset > closest.offset) {
                return { offset: offset, element: child };
            } else {
                return closest;
            }
        }, { offset: Number.NEGATIVE_INFINITY }).element;
    }

    private updateState(key: 'collapsed' | 'removed', type: string, add: boolean) {
        const stateStr = sessionStorage.getItem('dap_grid_state');
        const state = stateStr ? JSON.parse(stateStr) : { order: [], collapsed: [], removed: [] };

        if (add) {
            if (!state[key].includes(type)) state[key].push(type);
        } else {
            state[key] = state[key].filter((t: string) => t !== type);
        }

        sessionStorage.setItem('dap_grid_state', JSON.stringify(state));
    }

    private saveBlockOrder() {
        const stateStr = sessionStorage.getItem('dap_grid_state');
        const state = stateStr ? JSON.parse(stateStr) : { order: [], collapsed: [], removed: [] };

        const blocks = Array.from(document.querySelectorAll('.dap-grid-block'));
        state.order = blocks.map(b => (b as HTMLElement).getAttribute('data-block-type'));

        sessionStorage.setItem('dap_grid_state', JSON.stringify(state));
    }

    public showGrid() {
        this.grid?.classList.add('open');
        this.isOpen = true;
    }

    public hideGrid() {
        this.grid?.classList.remove('open');
        this.isOpen = false;
    }

    public getIsOpen(): boolean {
        return this.isOpen;
    }

    /**
     * Refresh the presence message (e.g., after config is loaded)
     */
    public refreshPresence() {
        const el = document.getElementById('dap-strip-text');
        if (el) {
            el.innerText = `You're on ${this.extractWebsiteName()}.`;
        }
    }
}
