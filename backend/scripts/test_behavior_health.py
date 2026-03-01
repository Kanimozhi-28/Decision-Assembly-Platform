import requests
import json
import time

url = "http://localhost:8000/behavior/analyze"
payload = {
    "site_id": "99999999-9999-4999-9999-999999999999",
    "type": "hover",
    "metadata": "Basic Savings Account",
    "url": "http://localhost:8000/test-sites/banking/savings.html"
}
headers = {
    "Content-Type": "application/json"
}

print(f"Sending request to {url}...")
start = time.time()
try:
    response = requests.post(url, json=payload, headers=headers, timeout=10)
    elapsed = time.time() - start
    print(f"Status Code: {response.status_code}")
    print(f"Time Taken: {elapsed:.2f}s")
    print("Response:", response.json())
except Exception as e:
    print(f"Error: {e}")
