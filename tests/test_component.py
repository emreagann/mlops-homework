from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_predict_endpoint_integration():
    """
    Part 2 Requirement: Component/Integration Test.
    Verifies interaction between API and Feature logic without spinning up full server.
    """
    response = client.post("/predict", json={"feature": "test_feature"})
    assert response.status_code == 200
    data = response.json()
    assert "bucket_index" in data
    assert data["status"] == "success"

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}
