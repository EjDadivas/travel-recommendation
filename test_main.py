from fastapi.testclient import TestClient
from .main import app

client = TestClient(app)


def test_redirect_to_recommend():
    response = client.get("/travel-recommendations")
    assert response.status_code == 200
    assert response.json() == {"home": "this is the home page"}


def test_recommend_inexistant_season():
    response = client.get("/travel-recommendations?season=raining")
    assert response.status_code == 404
    assert response.json() == {"home": "this is the home page"}

# def test_recomommend_inexistant_season:
