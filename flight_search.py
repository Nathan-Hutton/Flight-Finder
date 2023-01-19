import os
import requests
import datetime
from dotenv import load_dotenv
load_dotenv('/Users/natha/PycharmProjects/info.env')


class FlightSearch:

    def __init__(self):
        self.headers = {
            'apikey': os.getenv('FLIGHT_SOLUTION_KEY'),
        }
        self.search_endpoint = 'http://tequila-api.kiwi.com/v2/search?'
        self.start_date = (datetime.date.today() + datetime.timedelta(days=1)).strftime('%d/%m/%Y')
        self.end_date = (datetime.date.today() + datetime.timedelta(days=6*30)).strftime('%d/%m/%Y')
        self.search_params = {
            'fly_from': 'SLC',
            'fly_to': '[PLACEHOLDER]',
            'date_from': self.start_date,
            'date_to': self.end_date,
            'nights_in_dst_from': 7,
            'nights_in_dst_to': 28,
            'flight_type': 'round',
            'curr': 'USD',
            'one_for_city': 1,
            "max_stopovers": 0,
        }
        self.flights_key = os.getenv('FLIGHT_SOLUTION_KEY')
        self.flight_endpoint = "http://tequila-api.kiwi.com/locations/query"

    def get_city_code(self, city):
        location_params = {
            'term': city.title(),
            'location_types': 'city'
        }
        response = requests.get(url=self.flight_endpoint, params=location_params, headers=self.headers)
        return response.json()['locations'][0]['code']

    def search_cheap_flights(self, city):
        city_iata = self.get_city_code(city)
        self.search_params['fly_to'] = city_iata
        self.search_params['max_stopovers'] = 5
        response = requests.get(url=self.search_endpoint, params=self.search_params, headers=self.headers)
        data = response.json()
        try:
            return data['data'][0]
        except IndexError:
            self.search_params['max_stopovers'] = 1
            response = requests.get(url=self.search_endpoint, params=self.search_params, headers=self.headers)
            data = response.json()
            try:
                return data['data'][0]
            except IndexError:
                print(f"{city}: No flights")
