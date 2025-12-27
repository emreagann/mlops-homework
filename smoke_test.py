import requests
import time
import os
import sys

def verify_service():
    """
    Part 2 Requirement: Smoke Test.
    Verifies different environment endpoints (CI vs Local).
    """
    # Use API_URL env if present (for CI), else localhost
    url = os.environ.get("API_URL", "http://localhost:8000/predict")
    print(f"Running Smoke Test against: {url}")
    
    data = {"feature": "smoke_test_val"}
    
    # Retry mechanism waiting for container boot
    max_retries = 10
    for i in range(max_retries):
        try:
            response = requests.post(url, json=data, timeout=5)
            if response.status_code == 200:
                print(f"Smoke Test Passed! Response: {response.json()}")
                return True
            else:
                print(f"Attempt {i+1}: Status {response.status_code}")
        except Exception as e:
            print(f"Attempt {i+1}: Failed to connect ({e})")
        
        time.sleep(2)
    
    print("Smoke Test Failed: Service not reachable or error response.")
    sys.exit(1)

if __name__ == "__main__":
    verify_service()
