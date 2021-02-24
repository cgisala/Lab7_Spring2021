import requests
import os
from datetime import datetime, date
from pprint import pprint

# Variables
key = os.environ.get('WEATHER_KEY')



def main():
    lat, lon = location()
    data = get_request(lat,lon)
    get_temparature(data)


def location():
    # lattitue and longtitude for minneapolis
    lat = 44.986656
    lon = -93.258133
    return lat, lon


def get_temparature(data):
    forecast_items = data['list']

    today = str(date.today())
    temperature = []
    count = 0
    avgTemp = 0

    for forecast in forecast_items:
        timestamp = forecast['dt'] #Unix timestamp
        date = datetime.utcfromtimestamp(timestamp).strftime('%Y-%m-%d') # Convert to a datetime, for humans

        if date == today:
            
            temp = forecast['main']['temp'] # float value
            temperature.append(temp)
    for temp in temperature:
        count += 1
        avgTemp += temp
    avgTemp = avgTemp/count
    avgTempFar = (avgTemp * 1.8) - 459.67 # converts kelvin to Farenheit
    deg_sym = '°'
    print(f'\nAverage Temperature for {today} is {round(avgTempFar, 2)}{deg_sym}F\n')
    

def get_description():
    pass

def get_wind_speed():
    pass

def get_request(lat, lon):
    part = 'current,minutely,hourly,alerts'
    query = f'lat={lat}&lon={lon}&exclude={part}&appid={key}'
    url = 'https://api.openweathermap.org/data/2.5/forecast?'
    data = requests.get(f'{url}{query}').json()

if __name__=='__main__':
    main()