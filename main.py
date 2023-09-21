from typing import Union
from uvicorn import run
from fastapi import FastAPI, HTTPException
from fastapi.responses import RedirectResponse
from pycountry import countries
app = FastAPI()


sampleData = {
    "country": "Canada",
    "season": "winter",
    "recommendations": [
        {
            "location": "Ramen Restaurant, Toronto",
            "activity": "Eat special ramen noodles with spicy beef",
            "map_link": "https://www.google.com/maps?q=Ramen+Restaurant+Toronto"
        },
        {
            "location": "Whistler, British Columbia",
            "activity": "Go skiing or snowboarding on the beautiful slopes",
            "map_link": "https://www.google.com/maps?q=Whistler+British+Columbia"
        },
        {
            "location": "Old Quebec City, Quebec",
            "activity": "Explore the charming streets and enjoy winter festivals",
            "map_link": "https://www.google.com/maps?q=Old+Quebec+City+Quebec"
        }
    ]
}


@app.get("/")
def redirect_to_recommend():
    return RedirectResponse(url="/travel-recommendations")


@app.get("/travel-recommendations")
async def recommend(country: Union[str, None] = None, season: Union[str, None] = None):
    if country is None and season is None:
        return {"home": "this is the home page"}

    errors = []
    if country:
        try:
            result = countries.search_fuzzy(country)
            if len(result) != 1:
                errors.append("Invalid country")
        except:
            errors.append("Invalid Country")
    else:
        errors.append("Invalid country")

    if season is None or season.lower() not in {"winter", "summer", "spring", "autumn"}:
        errors.append("Invalid season")

    if errors:
        raise HTTPException(status_code=400, detail={"errors": errors})

    return {"country": country, "season": season}


if __name__ == '__main__':
    run("main:app", host="localhost", port=3000,
        reload=True, access_log=False)
