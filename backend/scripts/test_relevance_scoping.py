import asyncio
import httpx
import json

async def test_relevance():
    base_url = "http://localhost:8000"
    
    # Test cases with page titles that should trigger specific categories
    test_cases = [
        {
            "site_id": "77777777-7777-4777-7777-777777777777",
            "name": "Cardiology Section (Strict)",
            "url": "http://localhost:8000/test-sites/healthcare/cardiology.html",
            "page_title": "Cardiology Department",
            "expected_category": "cardiology"
        },
        {
            "site_id": "77777777-7777-4777-7777-777777777777",
            "name": "Heart Surgery Section",
            "url": "http://localhost:8000/test-sites/healthcare/heart-surgery.html",
            "page_title": "Specialized Heart Surgery",
            "expected_category": "cardiology"
        }
    ]
    
    async with httpx.AsyncClient(follow_redirects=True) as client:
        print("=== Relevance & Scoping Verification ===")
        for tc in test_cases:
            print(f"\nTesting: {tc['name']}")
            payload = {
                "site_id": tc["site_id"],
                "intent": "help_me_choose",
                "context": {
                    "url": tc["url"],
                    "page_title": tc["page_title"],
                    "visible_product_urls": [] # Force RAG fallback to check category scoping
                }
            }
            
            try:
                response = await client.post(f"{base_url}/assemble/", json=payload, timeout=300.0)
                if response.status_code == 200:
                    data = response.json()
                    products = data.get("products", [])
                    print(f"  - Products Found: {len(products)}")
                    
                    mismatches = []
                    for p in products:
                        p_cat = p.get("category", "").lower()
                        print(f"    - {p['title']} [{p_cat}]")
                        if p_cat != tc["expected_category"] and p_cat != "general":
                            mismatches.append(f"{p['title']} ({p_cat})")
                    
                    if not mismatches:
                        print(f"  ✅ SUCCESS: All products match '{tc['expected_category']}' or 'general'.")
                    else:
                        print(f"  ❌ FAILURE: Found irrelevant products: {', '.join(mismatches)}")
                else:
                    print(f"  ❌ ERROR: {response.status_code} - {response.text}")
            except Exception as e:
                import traceback
                print(f"  💥 EXCEPTION: {e}")
                traceback.print_exc()

if __name__ == "__main__":
    asyncio.run(test_relevance())
