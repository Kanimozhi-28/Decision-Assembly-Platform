import urllib.request
import json
import sys


SITES = {
    "E-commerce": "88888888-8888-4888-8888-888888888888",
    "Banking": "99999999-9999-4999-9999-999999999999",
    "Healthcare": "77777777-7777-4777-7777-777777777777"
}
API_URL = "http://localhost:8000/assemble/"

def post_json(url, data):
    req = urllib.request.Request(url)
    req.add_header('Content-Type', 'application/json')
    jsondata = json.dumps(data).encode('utf-8')
    req.add_header('Content-Length', len(jsondata))
    try:
        response = urllib.request.urlopen(req, jsondata, timeout=30)
        return json.loads(response.read())
    except Exception as e:
        print(f"FAILED: {e}")
        return None

def verify_all_sites():
    for name, s_id in SITES.items():
        print(f"\n{'='*20} VERIFYING SITE: {name} ({s_id}) {'='*20}")
        
        # TEST 1: Help Me Choose
        print(f"\n--- [{name}] TEST 1: Help Me Choose ---")
        payload = {
            "site_id": s_id,
            "intent": "help_me_choose", 
            "context": {"page_title": f"{name} Home Page"}
        }
        res = post_json(API_URL, payload)
        if res:
            prods = res.get("products", [])
            blocks = res.get("blocks", [])
            print(f"Products Found: {len(prods)}")
            print(f"Blocks Found: {len(blocks)}")
            for p in prods:
                print(f" - {p.get('title')} ({p.get('category')})")
            
            # CHECK SITE ISOLATION
            other_sites_products = False
            for p in prods:
                # Simple check: Bank products have 'Nexus', E-comm have 'E-Life', Health have 'CarePoint' or medical terms
                title = p.get('title', '').lower()
                if name == "Banking" and "nexus" not in title: other_sites_products = True
                if name == "E-commerce" and "e-life" not in title: other_sites_products = True
                if name == "Healthcare" and not any(k in title for k in ["cardiac", "neurological", "pediatric", "mri", "carepoint"]):
                    other_sites_products = True
            
            if other_sites_products:
                print("!! WARNING: Potential Site Isolation Leak Detected!")
            else:
                print("OK: Site Isolation Verified")

if __name__ == "__main__":
    verify_all_sites()
