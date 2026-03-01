import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))

from app.services.rules_engine import RulesEngine

def test_rules():
    engine = RulesEngine()
    
    config = {
        "product_page_rules": {
            "url_patterns": [r"/p/", r"/product/"],
            "product_id_source": "url_path"
        }
    }
    
    test_urls = [
        ("https://shop.com/p/blue-shirt-123", True, "blue-shirt-123"),
        ("https://shop.com/product/shoes-99?color=red", True, "shoes-99"),
        ("https://shop.com/category/mens", False, None),
        ("https://shop.com/", False, None)
    ]
    
    print("Running Rules Engine Tests...")
    for url, expected_match, expected_id in test_urls:
        matches = engine.is_product_page(url, config)
        prod_id = engine.get_product_id(url, config) if matches else None
        
        status = "PASS" if matches == expected_match and prod_id == expected_id else "FAIL"
        print(f"[{status}] URL: {url}")
        if status == "FAIL":
            print(f"   Expected Match: {expected_match}, Got: {matches}")
            print(f"   Expected ID: {expected_id}, Got: {prod_id}")

if __name__ == "__main__":
    test_rules()
