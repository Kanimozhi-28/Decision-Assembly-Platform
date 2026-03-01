export class EventRecorder {
    private siteId: string;
    private sessionEvents: any[] = [];
    private lastInteraction: number = Date.now();

    constructor(siteId: string) {
        this.siteId = siteId;
        this.setupListeners();
        console.log('[DAP] EventRecorder initialized');
    }

    private setupListeners() {
        // Track all clicks
        document.addEventListener('click', (e) => {
            const target = e.target as HTMLElement;
            const clickData = {
                type: 'click',
                tag: target.tagName,
                text: target.innerText?.substring(0, 50),
                id: target.id,
                class: target.className,
                timestamp: Date.now(),
                url: window.location.href
            };
            this.recordEvent(clickData);
        }, true);

        // Track active time vs idle
        ['mousemove', 'keydown', 'scroll'].forEach(evt => {
            window.addEventListener(evt, () => {
                this.lastInteraction = Date.now();
            }, { passive: true });
        });
    }

    private recordEvent(event: any) {
        this.sessionEvents.push(event);
        console.log('[DAP] Event Recorded:', event.type, event.text || '');

        // Keep only last 50 events in memory
        if (this.sessionEvents.length > 50) {
            this.sessionEvents.shift();
        }
    }

    public getSessionSummary() {
        return {
            eventCount: this.sessionEvents.length,
            idleTimeMs: Date.now() - this.lastInteraction,
            history: this.sessionEvents
        };
    }
}
