from fastapi import APIRouter, HTTPException, Request, Response
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from typing import Union
from .utils import validate_travel_params, get_recommendations

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/")
def redirect_to_recommend():
    return RedirectResponse(url="/travel-recommendations")

@router.get("/travel-recommendations")
async def recommend(request: Request, country: Union[str, None] = None, season: Union[str, None] = None):
    data = None
    if country is None and season is None:
        return templates.TemplateResponse("home.html",  {"request": request})

    errors: list = validate_travel_params(country, season)
    if not errors:
        data = get_recommendations(country, season)
        
    return templates.TemplateResponse("home.html", {"request": request, "data" : data, "errors": errors})
    

