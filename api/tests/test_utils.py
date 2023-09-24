# tests/test_utils.py
from travelRecommendation.api.utils import validate_travel_params, get_recommendations


def test_validate_travel_params_valid():
    errors = validate_travel_params("Japan", "spring") 
    assert errors== []
    
def test_validate_travel_params_invalid():
    assert "Invalid Country" in validate_travel_params("Invalid_country", "spring")
    assert "Invalid Season" in validate_travel_params("Japan", "invalid_season")
    assert validate_travel_params("Invalid_country", "invalid_season") == ["Invalid Country", "Invalid Season"]

def test_get_recommendations():
    data = get_recommendations("Japan", "Spring")
    assert isinstance(data, dict)
    assert "country" in data
    assert "season" in data
    assert "recommendations" in data
    assert len(data["recommendations"]) == 3
    
    for recommendation in data["recommendations"]:
        assert isinstance(recommendation, dict)
        assert "location" in recommendation
        assert "activity" in recommendation
        assert "map_link" in recommendation