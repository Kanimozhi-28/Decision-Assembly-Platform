import urllib.request, json

API_URL = "http://localhost:8000/assemble/"
SITE_ID = "99999999-9999-4999-9999-999999999999"

def verify_api():
    payload = {
        "site_id": SITE_ID,
        "intent": "help_me_choose",
        "context": {}
    }
    req = urllib.request.Request(API_URL, data=json.dumps(payload).encode(), headers={'Content-Type': 'application/json'})
    try:
        response = urllib.request.urlopen(req)
        res = json.loads(response.read())
        print(f"STATUS: SUCCESS")
        print(f"INTENT: {res.get('intent')}")
        print(f"BLOCKS: {len(res.get('blocks', []))}")
        for i, block in enumerate(res.get('blocks', [])):
            print(f"  Block {i+1}: {block.get('type')} ({len(block.get('products', []))} products)")
        
        if len(res.get('blocks', [])) > 0:
            print("VERIFICATION: PASSED (Grid is working properly with block structure)")
        else:
            print("VERIFICATION: FAILED (No blocks returned)")
            
    except Exception as e:
        print(f"STATUS: ERROR - {e}")

if __name__ == "__main__":
    verify_api()
