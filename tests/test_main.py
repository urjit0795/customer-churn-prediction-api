
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}


def test_high_risk_prediction():
    response = client.post("/predict", json={
        "customer_id": 101,
        "tenure_months": 6,
        "monthly_spend": 80
    })

    assert response.status_code == 200
    assert response.json()["risk_level"] == "high"


def test_negative_tenure():
    response = client.post("/predict", json={
        "customer_id": 101,
        "tenure_months": -5,
        "monthly_spend": 80
    })

    assert response.status_code == 422



def test_low_risk_prediction():
    response = client.post("/predict", json={
        "customer_id": 102,
        "tenure_months": 24,
        "monthly_spend": 120
    })

    assert response.status_code == 200
    assert response.json()["risk_level"] == "low"


def test_missing_field():
    response = client.post("/predict", json={
        "customer_id": 103,
        "tenure_months": 6
    })

    assert response.status_code == 422
