import requests
from requests.exceptions import HTTPError
from datetime import datetime

def main():
    data = get_request()
    hours, minutes = get_time(data)
    print_time(hours, minutes)

def get_time(data):
    time = datetime.fromtimestamp(data) # converts unix time to human readable
    hours = time.strftime('%H') # filter the hours 
    minutes = time.strftime('%M') # filter the minutes
    return hours, minutes

def print_time(hours, minutes):
    print(f'\nToday\'s Time: {hours}:{minutes}\n') # prints the hours and minutes

def get_request():
    url = 'https://showcase.api.linx.twenty57.net/UnixTime/tounix?date=now'

    try:
        response = requests.get(f'{url}')  # request currnt time api
        return response.json() # converts the data into json format 
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')  
    except Exception as err:
        print(f'Other error occurred: {err}') 

if __name__=='__main__':
    main()
