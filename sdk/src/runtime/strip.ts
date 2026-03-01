/**
 * The Strip: Privacy/PII Redaction Service
 * Ensures sensitive data like prices or emails aren't sent to the backend.
 */
export class Stripper {
    private static PII_PATTERNS = [
        /[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}/g, // Email
        /\b\d{4}[- ]?\d{4}[- ]?\d{4}[- ]?\d{4}\b/g,        // Credit Card (simple)
        /\$\d+(?:\.\d{2})?/g,                             // Prices ($12.34)
    ];

    /**
     * Redacts text by replacing PII with [REDACTED]
     */
    static redactText(text: string): string {
        let sanitized = text;
        this.PII_PATTERNS.forEach(pattern => {
            sanitized = sanitized.replace(pattern, '[REDACTED]');
        });
        return sanitized;
    }

    /**
     * Clones an element's text content while redacting it.
     */
    static redactElement(el: HTMLElement): string {
        return this.redactText(el.innerText || '');
    }
}
