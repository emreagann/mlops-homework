import requests
import sys

URL = "http://localhost:8000/predict"

payload = {
    "user_id": "user_123",
    "item_id": "item_456"
}

try:
    response = requests.post(URL, json=payload, timeout=5)
except Exception as e:
    print(f"Request failed: {e}")
    sys.exit(1)

if response.status_code != 200:
    print(f"Smoke test failed. Status code: {response.status_code}")
    sys.exit(1)

print("Smoke test passed ✅")
