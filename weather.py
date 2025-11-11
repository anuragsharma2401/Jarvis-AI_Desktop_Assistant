import requests
import os 
from dotenv import load_dotenv

load_dotenv()

def Weather():
     
    BASE_URL = 'http://api.weatherapi.com/v1/current.json'

    city="Amritsar"
    params = {
        'key': os.getenv('WEATHER_API_KEY'),
        'q': city,
        'aqi': 'no'
    }

    try:
        response = requests.get(BASE_URL, params=params)
        data = response.json()

        if "error" in data:
            return f"Error: {data['error']['message']}"

        location = data['location']['name']
        temp_c = data['current']['temp_c']
        condition = data['current']['condition']['text']
        data=[location,temp_c,condition]
        return data
    except Exception as e:
        return f"An error occurred"


  
