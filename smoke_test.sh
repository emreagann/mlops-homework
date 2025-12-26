#!/bin/bash

set -e  # herhangi bir hata olursa script dursun

echo "Sending smoke test request..."

curl -f -X POST http://localhost:8000/predict \
  -H "Content-Type: application/json" \
  -d '{"user_id": "user_123", "item_id": "item_456"}'

echo "Smoke test passed ✅"
