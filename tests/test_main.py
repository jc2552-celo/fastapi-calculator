from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_add_api():
    response = client.get("/add?a=1&b=2")
    assert response.status_code == 200
    assert response.json() == {"result": 3.0}

def test_divide_by_zero_api():
    response = client.get("/divide?a=10&b=0")
    assert response.status_code == 200
    assert response.json() == {"error": "Cannot divide by zero."}
