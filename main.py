from typing import Union
from uvicorn import run
from fastapi import FastAPI, HTTPException
from fastapi.responses import RedirectResponse

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

seasons = {"winter", "summer", "spring", "autumn"}


@app.get("/")
def redirect_to_recommend():
    return RedirectResponse(url="/travel-recommendations")


@app.get("/travel-recommendations")
def recommend(country: Union[str, None] = None, season: Union[str, None] = None):

    # if both are none return something
    if country is None and season is None:
        return {"home": "this is the home page"}

    if country is None:
        raise HTTPException(status_code=404, detail="Invalid Country")

    if season is None or season.lower() not in seasons:
        raise HTTPException(
            status_code=404, detail="Invalid Season")

    return {"country": country, "season": season}


if __name__ == '__main__':
    run("main:app", host="localhost", port=3000,
        reload=True, access_log=False)
