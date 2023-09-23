from fastapi import APIRouter, HTTPException, Request, Response
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from typing import Union
from .utils import validate_travel_params, convert_to_dict, get_data

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/")
def redirect_to_recommend():
    return RedirectResponse(url="/travel-recommendations")

@router.get("/travel-recommendations")
async def recommend(request: Request, country: Union[str, None] = None, season: Union[str, None] = None):
    if country is None and season is None:
        return templates.TemplateResponse("home.html",  {"request": request})

    # Validation of query params
    errors: list = validate_travel_params(country, season)
    if errors:
        raise HTTPException(status_code=400, detail={"errors": errors})

    # openAI integration
    data = get_data(country, season);

    return templates.TemplateResponse("home.html", {"request": request, "data" : data})
    

