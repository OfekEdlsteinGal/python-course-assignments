from fastapi.testclient import TestClient
from app import app

client = TestClient(app)


def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert "message" in response.json()


def test_classify_endpoint():
    response = client.get("/classify/1.5")
    assert response.status_code == 200
    assert response.json()["classification"] == "semiconductor"


def test_analyze_endpoint():
    data = [
        {
            "material_id": "mp-1",
            "formula": "Li2O",
            "band_gap_eV": 4.2,
            "density_g_cm3": 2.1,
            "energy_above_hull_eV_atom": 0.0,
            "is_stable": True
        }
    ]

    response = client.post("/analyze", json=data)

    assert response.status_code == 200
    assert response.json()["number_of_materials"] == 1
    assert response.json()["results"][0]["band_gap_class"] == "insulator"