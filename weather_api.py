import datetime as dt
import requests
import json

BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"

API_KEY = "d955f4b880ca3afee325a0a64a3b8e4a"

#kalibo latitude and longitude
lat = "11.706"
long =  "122.364"

weather_url = BASE_URL + "lat=" + lat + "&lon=" + long + "&appid=" + API_KEY

response = requests.get(weather_url).json()


