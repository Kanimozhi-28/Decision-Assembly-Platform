import asyncio
import httpx
import json

async def test_assemble():
    base_url = "http://localhost:8000"
    sites = [
        {"id": "88888888-8888-4888-8888-888888888888", "name": "E-commerce", "url": "http://localhost:8000/test-sites/ecommerce/mobiles.html"},
        {"id": "99999999-9999-4999-9999-999999999999", "name": "Banking", "url": "http://localhost:8000/test-sites/banking/loans.html"},
        {"id": "77777777-7777-4777-7777-777777777777", "name": "Healthcare", "url": "http://localhost:8000/test-sites/healthcare/cardiology.html"}
    ]
    
    intents = ["help_me_choose", "compare_options"]
    
    async with httpx.AsyncClient(follow_redirects=True) as client:
        for site in sites:
            print(f"\n=== Testing Assembly for {site['name']} ===")
            for intent in intents:
                payload = {
                    "site_id": site["id"],
                    "intent": intent,
                    "context": {
                        "url": site["url"],
                        "page_title": f"{site['name']} Page",
                        "visible_product_urls": [
                            f"{site['url'].rsplit('/', 1)[0]}/product-phox-8-pro.html",
                            f"{site['url'].rsplit('/', 1)[0]}/product-galax-s24-ultra.html"
                        ] if site['name'] == "E-commerce" else [
                            f"{site['url'].rsplit('/', 1)[0]}/banking-basic-savings.html",
                            f"{site['url'].rsplit('/', 1)[0]}/banking-platinum-rewards-card.html"
                        ] if site['name'] == "Banking" else [
                            f"{site['url'].rsplit('/', 1)[0]}/service-angioplasty.html",
                            f"{site['url'].rsplit('/', 1)[0]}/service-heart-bypass-surgery.html"
                        ]
                    }
                }
                
                try:
                    response = await client.post(f"{base_url}/assemble/", json=payload, timeout=120.0)
                    if response.status_code == 200:
                        data = response.json()
                        blocks = data.get("blocks", [])
                        products = data.get("products", [])
                        print(f"  Intent: {intent}")
                        print(f"    - Status: ✅ SUCCESS")
                        print(f"    - Blocks Found: {len(blocks)}")
                        print(f"    - Products Returned: {len(products)}")
                        if products:
                            print(f"    - Sample Product: {products[0]['title']}")
                    else:
                        print(f"  Intent: {intent} -> ❌ FAILED ({response.status_code}): {response.text}")
                except Exception as e:
                    import traceback
                    print(f"  Intent: {intent} -> 💥 EXCEPTION: {e}")
                    traceback.print_exc()

if __name__ == "__main__":
    asyncio.run(test_assemble())
