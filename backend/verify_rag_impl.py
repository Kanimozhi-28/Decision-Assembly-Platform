import asyncio
import aiohttp
import json

async def test_rag():
    url = "http://localhost:8000/assemble/"
    
    # Use one of the seeded site IDs (E-Life Store)
    site_id = "88888888-8888-4888-8888-888888888888"
    
    payload = {
        "site_id": site_id,
        "intent": "help_me_choose",
        "context": {
            "page_title": "Looking for a specialized computer",
            "product_ids": [] # INTENTIONALLY EMPTY to force RAG
        }
    }
    
    print(f"Sending RAG request to {url}...")
    async with aiohttp.ClientSession() as session:
        async with session.post(url, json=payload) as response:
            print(f"Status: {response.status}")
            if response.status == 200:
                data = await response.json()
                products = data.get("products", [])
                print(f"Found {len(products)} products:")
                for p in products:
                    print(f"- {p['title']} ({p['price']})")
                    print(f"  Features: {p.get('features')}")
            else:
                print(await response.text())

if __name__ == "__main__":
    asyncio.run(test_rag())
