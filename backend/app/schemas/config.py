from pydantic import BaseModel
from typing import Optional
from uuid import UUID

class ProductPageRules(BaseModel):
    url_patterns: list[str] = []
    dom_selectors: list[str] = []
    product_id_source: str = "url_path"

class TriggerThresholds(BaseModel):
    multi_product_min: int = 2
    multi_product_window_min: int = 5
    dwell_sec: int = 45
    cta_hover_min: int = 2
    cooldown_after_trigger_sec: int = 30
    cooldown_after_dismiss_sec: int = 60
    cooldown_after_grid_close_sec: int = 45

class WhiteLabel(BaseModel):
    brand_name: Optional[str] = None
    primary_color: Optional[str] = None
    font_family: Optional[str] = None
    logo_url: Optional[str] = None
    copy_tone: Optional[str] = None

class SiteConfig(BaseModel):
    site_id: UUID
    product_page_rules: dict
    cta_selectors: list[str] = []
    help_me_choose_selector: Optional[str] = None
    trigger_thresholds: dict
    commentary_templates: list[str] = []
    block_mapping: dict
    white_label: dict = {}
    excluded_url_patterns: list[str] = []
    allowed_origins: list[str] = []
    session_timeout_min: int = 30
    restoration_window_min: int = 5
