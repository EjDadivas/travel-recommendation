import json
import openai
from pycountry import countries
from dotenv import load_dotenv
import os
load_dotenv()

openai.api_key = os.getenv('OPENAI_API_KEY')

def validate_travel_params(country: str, season: str) ->list:
    errors = []
    if country:
        try:
            # TODO: Fix Countries search Fuzzy  ``
            result = countries.search_fuzzy(country)
            # if result.length != 1:
            #     errors.append("Invalid Country")
                
        except:
            errors.append("Invalid Country")
    else:
        errors.append("Invalid country")

    if season is None or season.lower() not in {"winter", "summer", "spring", "autumn"}:
        errors.append("Invalid Season")

    return errors

def convert_to_dict(string: str) -> dict:
    json_objects = string.split("\n}\n{")
    json_array_string = "[" + ",\n".join(json_objects) + "]"
    json_data = json.loads(json_array_string)[0]
    return json_data
def get_travel_recommendations(country: str, season: str):
     """Recommend travel destinations, along with suggested activities and map links, for a memorable trip in country based on season."""
     travel_info = {
        "country": country,
        "season": season,
        "recommendations" :[
            {
            "location": "Mt. Okura Observatory, Hokkaido",
            "activity": "Enjoy panoramic views of the snow-covered city of Sapporo from the Mt. Okura Observatory.",
            "map_link": "https://www.google.com/maps?q=Mt.+Okura+Observatory,+Hokkaido"
            },
        ]
    }
    
     return json.dumps(travel_info)
 
function_descriptions = [
        {
            "name": "get_travel_recommendations",
            "description": "Gets travel information based on country and season",
            "parameters": {
                "type": "object",
                "properties": {
                    "country": {
                        "type": "string",
                        "description": "The country for which you want travel recommendations (e.g., 'Japan')."
                    },
                    "season": {
                        "type": "string",
                         "description": "The season for which you want travel recommendations (e.g., 'Autumn')."
                    },
                },
                "required" : ["country", "season"],
            },  
        }
    ]
 
def get_data(country: str, season: str) -> dict:
    prompt= [{"role": "user", "content":
    f"""Recommend three exciting travel destinations, along with suggested activities and map links, for a memorable trip in {country} during a {season} season.
    -Respond in json format.
    -Here is the format you need to follow: 
    {str(get_travel_recommendations(country, season))} 
    """}]

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-0613",
        messages=prompt,
        functions=function_descriptions,
        function_call="auto"
    )
    response_message = response["choices"][0]["message"]

    if response_message.get("function_call"):
        available_functions = {
            "get_travel_recommendations": get_travel_recommendations,
        } 
        function_name = response_message["function_call"]["name"]
        fuction_to_call = available_functions[function_name]
        function_args = json.loads(response_message["function_call"]["arguments"])
        function_response = fuction_to_call(
            country=function_args.get("country"),
            season=function_args.get("season"),
        )
        prompt.append(response_message)
        prompt.append(
            {
                "role": "function",
                "name": function_name,
                "content": function_response,
            }
        )
        second_response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-0613",
            messages=prompt,
            functions=function_descriptions
        )
        recommendations = second_response.choices[0].message.content
        data = convert_to_dict(recommendations)

        return data