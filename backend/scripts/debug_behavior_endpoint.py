import requests
import json
import time

url = "http://localhost:8000/behavior/analyze"
payload = {
    "site_id": "test-site",
    "type": "hover",
    "metadata": "Test Product",
    "url": "http://localhost:8000/test"
}
headers = {
    "Content-Type": "application/json"
}

print(f"Sending request to {url}...")
start_time = time.time()
try:
    response = requests.post(url, json=payload, headers=headers)
    end_time = time.time()
    duration = end_time - start_time
    
    print(f"Status Code: {response.status_code}")
    print(f"Time Taken: {duration:.2f} seconds")
    print("Response:")
    print(json.dumps(response.json(), indent=2))
except Exception as e:
    print(f"Error: {e}")
