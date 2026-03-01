import { TriggerThresholds } from '../types';

export interface TriggerEvent {
    type: 'multi_product' | 'hesitation' | 'cta_hover' | 'nav_loop' | 'explicit';
    timestamp: number;
    metadata?: any;
}

export class TriggerSystem {
    private siteId: string;
    private config: TriggerThresholds;
    private eventBuffer: TriggerEvent[] = [];
    private lastTriggerTime: number = 0;
    private ctaHoverCount: number = 0;
    private hasClickedCTA: boolean = false;
    private startTime: number = Date.now();
    private isSuppressed: boolean = false;

    constructor(siteId: string, config?: TriggerThresholds) {
        this.siteId = siteId;
        this.config = config || {
            multi_product_min: 2,
            multi_product_window_min: 5,
            dwell_sec: 45,
            cta_hover_min: 2
        };

        this.loadState();
    }

    private get storageKey() {
        return `dap_trigger_state_${this.siteId}`;
    }

    private loadState() {
        const stored = sessionStorage.getItem(this.storageKey);
        if (stored) {
            try {
                const state = JSON.parse(stored);
                this.lastTriggerTime = state.lastTriggerTime || 0;
                this.isSuppressed = state.isSuppressed || false;
            } catch (e) {
                console.warn('[DAP] Trigger state load failed');
            }
        }
    }

    private saveState() {
        sessionStorage.setItem(this.storageKey, JSON.stringify({
            lastTriggerTime: this.lastTriggerTime,
            isSuppressed: this.isSuppressed
        }));
    }

    public reportCTAInteraction(type: 'hover' | 'click') {
        if (type === 'click') {
            this.hasClickedCTA = true;
        } else if (type === 'hover' && !this.hasClickedCTA) {
            this.ctaHoverCount++;
            this.checkTriggers();
        }
    }

    public checkTriggers(): { type: string, message: string } | null {
        if (this.isSuppressed) return null;

        const now = Date.now();
        const cooldown = 30 * 1000; // 30s cooldown from PRD FR-010C

        if (now - this.lastTriggerTime < cooldown) return null;

        // 1. Multiple Product Views (FR-006)
        const products = this.getViewedProducts();
        if (products.length >= this.config.multi_product_min) {
            return this.fireTrigger('multi_product', `You've viewed ${products.length} options — want help comparing?`);
        }

        // 2. CTA Hover Pattern (FR-008)
        if (this.ctaHoverCount >= this.config.cta_hover_min && !this.hasClickedCTA) {
            return this.fireTrigger('cta_hover', "Considering your options? I can help you decide.");
        }

        // 3. Hesitation Detection (FR-007)
        const dwellTime = (now - this.startTime) / 1000;
        const scrollPct = (window.scrollY / (document.documentElement.scrollHeight - window.innerHeight)) * 100;

        if (dwellTime > this.config.dwell_sec && !this.hasClickedCTA && scrollPct > 60) {
            return this.fireTrigger('hesitation', "Spending some time here? Want a quick summary?");
        }

        return null;
    }

    private fireTrigger(type: string, message: string) {
        this.lastTriggerTime = Date.now();
        this.saveState();
        console.log(`[DAP] Trigger Fired: ${type}`);
        return { type, message };
    }

    private getViewedProducts(): string[] {
        const stored = localStorage.getItem(`dap_views_${this.siteId}`);
        if (!stored) return [];
        try {
            const parsed = JSON.parse(stored);
            const now = Date.now();
            const windowMs = (this.config.multi_product_window_min || 5) * 60 * 1000;
            return parsed
                .filter((p: any) => (now - p.timestamp) < windowMs)
                .map((p: any) => p.url);
        } catch (e) {
            return [];
        }
    }

    public dismiss() {
        this.lastTriggerTime = Date.now() + 30000; // Add 30s penalty to cooldown for dismissal
        this.saveState();
    }
}
