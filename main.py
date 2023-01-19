from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager
from dotenv import load_dotenv

load_dotenv('/Users/natha/PycharmProjects/info.env')

data_manager = DataManager()
cities = data_manager.get_cities()
search = FlightSearch()
notification_manager = NotificationManager()
flights = []
for city in cities:
    cheap_flight = search.search_cheap_flights(city)
    if cheap_flight != None:
        flights.append(cheap_flight)

for flight in flights:
    print(flight['cityTo'])
    if data_manager.get_price(flight['cityTo']) > flight['price']:
        data_manager.update_info(flight['cityTo'], flight['price'], flight['route'][0]['local_departure'].split("T")[0],
                                 flight['route'][len(flight['route'])-1]['local_arrival'].split("T")[0], len(flight['route']) - 2)
        notification_manager.send_message(price=flight["price"], depart_city="London", depart_airport=flight['flyFrom'],
                                          city=flight['cityTo'], arrival_airport=flight['flyTo'],
                                          outbound_date=flight['local_departure'], inbound_date=flight['local_arrival'],
                                          flight_no=flight['route'][0]['flight_no'])


print('done')
