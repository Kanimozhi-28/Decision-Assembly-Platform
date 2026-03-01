
import urllib.request
import json
import uuid

def verify_config_api():
    site_id = "99999999-9999-4999-9999-999999999999"
    url = f"http://localhost:8000/sites/{site_id}/config"
    try:
        response = urllib.request.urlopen(url)
        data = json.loads(response.read())
        print(f"API SUCCESS:")
        print(f" - site_name: {data.get('site_name')}")
        print(f" - white_label: {data.get('white_label')}")
    except Exception as e:
        print(f"API FAILED: {e}")

if __name__ == "__main__":
    verify_config_api()
