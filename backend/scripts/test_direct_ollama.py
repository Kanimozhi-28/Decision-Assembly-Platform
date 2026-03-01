import requests
import time

URL = "http://10.100.20.76:11434/api/generate"
PAYLOAD = {
    "model": "llama3.1:8b",
    "prompt": "Say hello in 5 words.",
    "stream": False
}

def test_ollama():
    print(f"Testing Ollama at {URL}...")
    start = time.time()
    try:
        resp = requests.post(URL, json=PAYLOAD, timeout=60)
        elapsed = time.time() - start
        print(f"Status: {resp.status_code}")
        print(f"Time: {elapsed:.2f}s")
        print(f"Response: {resp.text[:200]}")
    except Exception as e:
        print(f"FAILED: {e}")

if __name__ == "__main__":
    test_ollama()
