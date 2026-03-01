export interface SiteConfig {
    product_page_rules: ProductPageRules;
    trigger_thresholds: TriggerThresholds;
    commentary_templates: string[];
    block_mapping: Record<string, string[]>;
    white_label: WhiteLabel;
}

export interface ProductPageRules {
    url_patterns: string[];
    dom_selectors: string[];
    product_id_source: 'url_path' | 'data_attribute' | 'meta';
}

export interface TriggerThresholds {
    multi_product_min: number;
    multi_product_window_min: number;
    dwell_sec: number;
    cta_hover_min: number;
}

export interface WhiteLabel {
    brand_name?: string;
    primary_color?: string;
}
