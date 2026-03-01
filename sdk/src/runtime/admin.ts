export class AdminToolbar {
    private container: HTMLElement | null = null;
    private siteId: string;
    private baseUrl: string = 'http://localhost:8000';

    constructor(siteId: string) {
        this.siteId = siteId;
    }

    public render() {
        if (this.container) return;

        const style = document.createElement('style');
        style.textContent = `
            #dap-admin-toolbar {
                position: fixed;
                top: 20px;
                right: 20px;
                background: #1c1c1e;
                color: #fff;
                padding: 12px;
                border-radius: 12px;
                z-index: 1000001;
                font-family: -apple-system, system-ui, sans-serif;
                box-shadow: 0 4px 12px rgba(0,0,0,0.5);
                display: flex;
                flex-direction: column;
                gap: 8px;
                width: 200px;
            }
            .dap-admin-btn {
                background: #34495e;
                color: white;
                border: none;
                padding: 8px;
                border-radius: 6px;
                cursor: pointer;
                font-weight: 600;
                font-size: 12px;
            }
            .dap-admin-btn:hover { background: #2c3e50; }
            .dap-admin-title { font-size: 14px; font-weight: 700; border-bottom: 1px solid #333; padding-bottom: 8px; }
            .dap-admin-status { font-size: 10px; color: #aaa; }
        `;
        document.head.appendChild(style);

        this.container = document.createElement('div');
        this.container.id = 'dap-admin-toolbar';
        this.container.innerHTML = `
            <div class="dap-admin-title">DAP Admin Mode</div>
            <div class="dap-admin-status">Site ID: ${this.siteId}</div>
            <button class="dap-admin-btn" id="dap-sync-site">Sync Site (Universal DAG)</button>
            <button class="dap-admin-btn" id="dap-debug-selectors" style="background: #e67e22;">Debug Selectors</button>
        `;
        document.body.appendChild(this.container);

        document.getElementById('dap-sync-site')?.addEventListener('click', () => this.syncSite());
        document.getElementById('dap-debug-selectors')?.addEventListener('click', () => this.debugSelectors());
    }

    private async syncSite() {
        const btn = document.getElementById('dap-sync-site') as HTMLButtonElement;
        if (btn) {
            btn.innerText = 'Syncing...';
            btn.disabled = true;
        }

        try {
            const response = await fetch(`${this.baseUrl}/crawl/universal`, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({
                    url: window.location.href,
                    site_id: this.siteId
                })
            });

            if (response.ok) {
                alert('Universal Sync started! Refresh in a few seconds.');
            } else {
                alert('Sync failed. Check console.');
            }
        } catch (e) {
            console.error('[DAP Admin] Sync error:', e);
        } finally {
            if (btn) {
                btn.innerText = 'Sync Site (Universal DAG)';
                btn.disabled = false;
            }
        }
    }

    private debugSelectors() {
        alert('Selector debugging overlay coming soon!');
    }
}
