import urllib.request, json

API_URL = "http://localhost:8000/assemble/"
SITE_ID = "88888888-8888-4888-8888-888888888888"

def test_strict_intent():
    payload = {
        "site_id": SITE_ID,
        "intent": "compare_options",
        "context": {} # No viewed products
    }
    req = urllib.request.Request(API_URL, data=json.dumps(payload).encode(), headers={'Content-Type': 'application/json'})
    try:
        response = urllib.request.urlopen(req)
        res = json.loads(response.read())
        products = res.get("products", [])
        print(f"INTENT: compare_options")
        print(f"PRODUCTS RETURNED: {len(products)}")
        if len(products) == 0:
            print("SUCCESS: Strict filtering is working (0 products for empty context).")
        else:
            print(f"FAILURE: RAG fallback occurred. products: {[p.get('title') for p in products]}")
    except Exception as e:
        print(f"ERROR: {e}")

if __name__ == "__main__":
    test_strict_intent()
