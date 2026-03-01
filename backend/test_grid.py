import asyncio
import httpx

async def test_grid():
    """Test the simplified grid assembly"""
    
    # Test with E-commerce site
    site_id = "88888888-8888-4888-8888-888888888888"
    
    # Simulate SDK sending 2 product URLs
    payload = {
        "site_id": site_id,
        "intent": "help_me_choose",
        "context": {
            "page_title": "E-Life Store",
            "url": "http://127.0.0.1:8000/test-sites/ecommerce/index.html",
            "product_ids": [
                "http://127.0.0.1:8000/test-sites/ecommerce/product-laptop.html",
                "http://127.0.0.1:8000/test-sites/ecommerce/product-phone.html"
            ]
        }
    }
    
    print("Testing Grid Assembly with 2 products...")
    print(f"Site: {site_id}")
    print(f"Products: {len(payload['context']['product_ids'])}")
    print("=" * 60)
    
    async with httpx.AsyncClient() as client:
        response = await client.post(
            "http://localhost:8000/assemble/",
            json=payload,
            timeout=30.0
        )
        
        if response.status_code == 200:
            data = response.json()
            print(f"\nSUCCESS!")
            print(f"Products returned: {len(data.get('products', []))}")
            print(f"Message: {data.get('message', 'N/A')}")
            print("\nProducts:")
            for p in data.get('products', []):
                print(f"  - {p.get('title')} ({p.get('price')})")
                print(f"    URL: {p.get('url')}")
        else:
            print(f"\nFAILED: {response.status_code}")
            print(response.text)

if __name__ == "__main__":
    asyncio.run(test_grid())
