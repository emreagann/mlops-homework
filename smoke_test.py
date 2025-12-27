import requests
import time

import os

def verify_service():
    url = os.environ.get("API_URL", "http://localhost:8000/predict")
    print(f"Testing Service at: {url}")
    data = {"feature": "test_value"}
    
    for _ in range(5):  # Retry while container boots
        try:
            response = requests.post(url, json=data)
            if response.status_code == 200:
                print("Smoke Test Passed!")
                return True
        except:
            time.sleep(2)
    
    print("Smoke Test Failed")
    exit(1)

if __name__ == "__main__":
    verify_service()
