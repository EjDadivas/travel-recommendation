from pycountry import countries
from dotenv import load_dotenv
import json
import openai
import os

load_dotenv()

openai.api_key = os.getenv('OPENAI_API_KEY')

def validate_travel_params(country: str, season: str) ->list:
    errors = []
    if country:
        try:
            # TODO: Fix Countries search Fuzzy  ``
            result = countries.search_fuzzy(country)
            if (len(result)) != 1:
                errors.append("Invalid Country")
        except:
            errors.append("Invalid Country")
    else:
        errors.append("Invalid Country")

    if season is None or season.lower() not in {"winter", "summer", "spring", "autumn"}:
        errors.append("Invalid Season")
    
    return errors

def get_recommendations(country, season):
    # Create prompt text with user input
    prompt = f"Recommend three exciting travel destinations, along with suggested activities and map links, for a memorable trip in {country} during a {season} season."

    schema = {
        "type": "object",
        "properties": {
            "country": {
                "type": "string",
                "description": "Name of the country (e.g. Canada)"
            },
            "season": {
                "type": "string",
                "description": "Season (e.g. Winter)"
            },
            "recommendations": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "location": {
                            "type": "string",
                            "description": "Name of the location (e.g. Whistler, British Columbia)"
                        },
                        "activity": {
                            "type": "string",
                            "description": "Describe the kind of activity, (e.g. Go skiing or snowboarding on the beautiful slopes.)"
                        },
                        "map_link": {
                            "type": "string",
                            "description": "Link to a map for the location (e.g. \"https://www.google.com/maps?q=Old+Quebec+City+Quebec)"
                        }
                    },
                }
            }
        }, 
        "required": ["country", "season"]
    }
    
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-0613",
        messages=[
            {"role": "system", "content": "You are a travel recommender."},
            {"role": "user", "content": prompt}
        ],
        functions=[{"name": "set_travel_params", "parameters": schema}],
        function_call={"name": "set_travel_params"}
    )


    generated_text = response['choices'][0]['message']['function_call']['arguments']
    
    return json.loads(generated_text)