import requests
import os
from datetime import datetime
from requests.exceptions import HTTPError
from pprint import pprint

# Variables
key = os.environ.get('WEATHER_KEY')

def main():
    lat, lon = location()
    data = get_request(lat,lon)
    weather= get_weather(data)
    print_weather(weather)

def location():
    # lattitue and longtitude for minneapolis
    lat = 44.986656
    lon = -93.258133
    return lat, lon

def get_weather(data):
    from datetime import date
    forecast_items = data['list']
    deg_sym = '°'
    forecast = []

    for items in forecast_items:
        timestamp = items['dt'] #Unix timestamp
        date = datetime.utcfromtimestamp(timestamp).strftime('%Y-%m-%d') # Convert to a datetime, for humans
        temp = kelvin_to_Celsius(items['main']['temp']) # converts Kelvin to Celsius
        description = items['weather'][0]['description'] # Gets weather description
        wind = knots_to_mph(items['wind']['speed']) # converts knots to mph
        weather = f'\nDate: {date}, \nTemp: {temp}{deg_sym}F, \nDescription: {description}, \nWind: {wind} mph'
        forecast.append(weather)
    
    return forecast

def get_request(lat, lon):
    part = 'current,minutely,hourly,alerts'
    query = f'lat={lat}&lon={lon}&exclude={part}&appid={key}'
    url = 'https://api.openweathermap.org/data/2.5/forecast?'

    try:
        response = requests.get(f'{url}{query}')
        response.raise_for_status()
        return response.json()
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')  
    except Exception as err:
        print(f'Other error occurred: {err}') 

def kelvin_to_Celsius(temp):
    return round(((temp * 1.8) - 459.67), 2) # converts kelvin to Farenheit

def knots_to_mph(knot):
    return round((knot * 1.15078), 2)

def print_weather(forecast):
    for weather in forecast:
        print(weather)

if __name__=='__main__':
    main()