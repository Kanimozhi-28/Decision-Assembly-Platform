import requests
import json

url = "http://localhost:8000/assemble/"
payload = {
    "site_id": "99999999-9999-4999-9999-999999999999",
    "intent": "help_me_choose",
    "context": {
        "page_title": "Savings | Nexus Bank",
        "url": "http://localhost:8000/test-sites/banking/savings.html",
        "visible_product_urls": [
            "http://localhost:8000/test-sites/banking/banking-kids-junior-account.html",
            "http://localhost:8000/test-sites/banking/banking-women-empowerment-savings.html"
        ]
    }
}
headers = {
    "Content-Type": "application/json"
}

print(f"Sending request to {url}...")
try:
    response = requests.post(url, json=payload, headers=headers)
    print(f"Status Code: {response.status_code}")
    data = response.json()
    
    print("Blocks returned:")
    for block in data.get("blocks", []):
        print(f"Block: {block.get('type')}")
        for p in block.get("products", []):
            print(f" - {p.get('title')} ({p.get('url')})")
            
    print("\n[BACKEND LOGS]")
    for log in data.get("debug_logs", []):
        print(log)
            
except Exception as e:
    print(f"Error: {e}")
