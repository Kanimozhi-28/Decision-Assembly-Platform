import asyncio
import json
import sys
import os

# Add parent directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.services.assemble import AssembleService

async def verify_ecommerce():
    service = AssembleService()
    site_id = "88888888-8888-4888-8888-888888888888" # E-commerce
    
    # These URLs are exactly what we expect the SDK to send on the Mobiles page
    # based on the Qdrant payloads I saw earlier
    visible_urls = [
        "http://localhost:8000/test-sites/ecommerce/product-phox-8-pro.html",
        "http://localhost:8000/test-sites/ecommerce/product-galax-s24-ultra.html",
        "http://localhost:8000/test-sites/ecommerce/product-ipone-15.html",
        "http://localhost:8000/test-sites/ecommerce/product-oneplus-12r.html"
    ]
    
    print(f"Testing Assembly for Site: {site_id}")
    print(f"Context URLs ({len(visible_urls)}):")
    for u in visible_urls:
        print(f" - {u}")
        
    result = await service.assemble_experience(
        site_id=site_id,
        intent="help_me_choose",
        context={
            "page_title": "E-Life | Mobiles",
            "url": "http://localhost:8000/test-sites/ecommerce/mobiles.html",
            "visible_product_urls": visible_urls
        }
    )
    
    print("\n--- RESULT ---")
    print(f"Products Found: {len(result['products'])}")
    for p in result['products']:
        print(f" [FOUND] {p['title']} ({p['url']})")
        
    print(f"\nBlocks: {len(result['blocks'])}")
    for b in result['blocks']:
        print(f" [{b['type']}] {len(b['products'])} items: {b['message']}")

if __name__ == "__main__":
    asyncio.run(verify_ecommerce())
