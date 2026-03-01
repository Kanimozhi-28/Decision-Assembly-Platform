
import urllib.request
import json
import uuid

def verify_section_lock():
    site_id = "99999999-9999-4999-9999-999999999999" # Banking
    url = "http://localhost:8000/assemble/"
    
    # Simulate being on a section with exactly 2 specific products
    visible_urls = [
        "http://localhost:8000/test-sites/banking/banking-max-saver-account.html",
        "http://localhost:8000/test-sites/banking/banking-platinum-rewards-card.html"
    ]
    
    payload = {
        "site_id": site_id,
        "intent": "compare_options",
        "context": {
            "page_title": "Banking | Insurance Solutions",
            "url": "http://localhost/banking/insurance.html",
            "visible_product_urls": visible_urls
        }
    }
    
    try:
        req = urllib.request.Request(url, data=json.dumps(payload).encode('utf-8'), headers={'Content-Type': 'application/json'})
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read())
            
            print(f"VERIFICATION RESULT:")
            print(f" - Products count: {len(data['products'])}")
            
            error = False
            for p in data['products']:
                print(f"   - Found: {p['title']} ({p['url']})")
                if p['url'] not in visible_urls:
                    print(f"   !!! VIOLATION: Product {p['url']} was not in visible list!")
                    error = True
            
            if not error and len(data['products']) == 2:
                print("\nSUCCESS: Section Visibility Lock enforced. No cross-section leakage.")
            elif len(data['products']) == 0:
                 print("\nFAIL: No products returned. Check if URLs match indexed data.")
            else:
                print("\nFAIL: Logic violation.")
                
    except Exception as e:
        print(f"VERIFICATION FAILED: {e}")

if __name__ == "__main__":
    verify_section_lock()
