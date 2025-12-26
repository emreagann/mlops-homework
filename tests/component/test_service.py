from fastapi.testclient import TestClient
from src.app import app

client = TestClient(app)

def test_read_root():
    """Test the health check endpoint."""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}

def test_predict_endpoint_integration():
    """
    Integration test:
    Verifies that the /predict endpoint correctly integrates with the hashing logic
    and returns a valid response model.
    """
    payload = {"feature_value": "integration_test"}
    response = client.post("/predict", json=payload)
    
    assert response.status_code == 200
    data = response.json()
    assert "bucket_index" in data
    assert "message" in data
    assert data["message"] == "Prediction successful"
    assert isinstance(data["bucket_index"], int)
