import re
from typing import Optional
from app.schemas.config import SiteConfig

class RulesEngine:
    @staticmethod
    def is_product_page(url: str, config: dict) -> bool:
        """
        Checks if the URL matches any of the product page patterns.
        """
        rules = config.get("product_page_rules", {})
        patterns = rules.get("url_patterns", [])
        
        for pattern in patterns:
            # Simple glob-to-regex conversion if needed, but we'll assume regex for now
            try:
                if re.search(pattern, url):
                    return True
            except re.error:
                print(f"Invalid regex pattern: {pattern}")
                continue
        
        return False

    @staticmethod
    def get_product_id(url: str, config: dict) -> Optional[str]:
        """
        Extracts product ID from the URL based on the defined source.
        """
        rules = config.get("product_page_rules", {})
        source = rules.get("product_id_source", "url_path")
        
        if source == "url_path":
            # Very common pattern: /product/12345 or /p/slug-id
            # We'll look for the last numeric or mixed segment
            parts = url.strip('/').split('/')
            if parts:
                last_segment = parts[-1]
                # If there's a query param, strip it
                last_segment = last_segment.split('?')[0]
                return last_segment
        
        return None
