import requests
import time

BASE_URL = "http://localhost:8000"
SITE_ID = "99999999-9999-4999-9999-999999999999"

def check_endpoint(name, url, method="GET", payload=None):
    print(f"Checking {name} ({url})...")
    start = time.time()
    try:
        if method == "GET":
            resp = requests.get(url, timeout=10)
        else:
            resp = requests.post(url, json=payload, timeout=10)
        
        elapsed = time.time() - start
        print(f"  Status: {resp.status_code}")
        print(f"  Time: {elapsed:.4f}s")
        if resp.status_code != 200:
            print(f"  Error: {resp.text[:200]}")
    except Exception as e:
        print(f"  FAILED: {e}")

if __name__ == "__main__":
    check_endpoint("Health", f"{BASE_URL}/health")
    check_endpoint("SDK Loader", f"{BASE_URL}/sdk/loader.js")
    check_endpoint("SDK Runtime", f"{BASE_URL}/sdk/dap-sdk.js")
    check_endpoint("Site Config", f"{BASE_URL}/sites/{SITE_ID}/config")
    
    behavior_payload = {
        "site_id": SITE_ID,
        "type": "hover",
        "metadata": "Test Metadata",
        "url": "http://localhost:8000/test-sites/banking/index.html"
    }
    check_endpoint("Behavior Analyze", f"{BASE_URL}/behavior/analyze", method="POST", payload=behavior_payload)
