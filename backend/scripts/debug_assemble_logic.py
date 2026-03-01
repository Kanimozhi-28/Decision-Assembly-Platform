import asyncio
import json
from app.services.assemble import AssembleService
import os
import sys

# Ensure app can be imported
sys.path.append(os.getcwd())

async def test_category_scoping():
    service = AssembleService()
    site_id = "99999999-9999-4999-9999-999999999999" # Nexus Bank
    
    # Test case 1: Savings page -> Expected category: savings
    print("\n--- TEST 1: Savings Page Scoping ---")
    context_savings = {
        "page_title": "Savings Solutions | Nexus Bank",
        "url": "http://localhost:8000/test-sites/banking/savings.html",
        "visible_product_urls": ["http://localhost:8000/test-sites/banking/banking-max-saver-account.html"] # Won't match exact DB URL
    }
    result_savings = await service.assemble_experience(site_id, "help_me_choose", context_savings)
    products_savings = result_savings.get("products", [])
    print(f"Detected Category should be 'savings'")
    print(f"Products found: {[p['title'] for p in products_savings]}")
    for p in products_savings:
        print(f" - {p['title']} ({p.get('category')})")

    # Test case 2: Insurance page -> Expected category: insurance
    print("\n--- TEST 2: Insurance Page Scoping ---")
    context_insurance = {
        "page_title": "Insurance Solutions | Nexus Bank",
        "url": "http://localhost:8000/test-sites/banking/insurance.html",
        "visible_product_urls": ["http://localhost:8000/test-sites/banking/banking-home-secure.html"]
    }
    result_insurance = await service.assemble_experience(site_id, "help_me_choose", context_insurance)
    products_insurance = result_insurance.get("products", [])
    print(f"Detected Category should be 'insurance'")
    print(f"Products found: {[p['title'] for p in products_insurance]}")
    for b in result_insurance.get("blocks", []):
        print(f" - Block '{b['type']}': {[p['title'] for p in b['products']]}")

if __name__ == "__main__":
    asyncio.run(test_category_scoping())
