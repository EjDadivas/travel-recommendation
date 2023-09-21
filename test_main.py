from fastapi.testclient import TestClient
from .main import app

client = TestClient(app)


def test_redirect_to_recommend():
    response = client.get("/travel-recommendations")
    assert response.status_code == 200
    assert response.json() == {"home": "this is the home page"}


def test_recommend_inexistant_country():
    response = client.get("travel-recommendations?country=Not+A+Country")
    assert response.status_code == 400


def test_recommend_inexistant_season():
    response = client.get("/travel-recommendations?season=raining")
    assert response.status_code == 400
    # assert response.json() == {
    #     "detail": {
    #         "errors": [
    #             "Invalid Country",
    #             "Invalid season"
    #         ]
    #     }
    # }


def test_recommend_wrong_country_season():
    response = client.get(
        "/travel-recommendations?season=raining&country=Not+A+Country")
    assert response.status_code == 400


def test_recommend_get_recommendations(): pass
