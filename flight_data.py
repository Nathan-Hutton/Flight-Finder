from dotenv import load_dotenv
load_dotenv('/Users/natha/PycharmProjects/info.env')


class FlightData:
    def __init__(self):
        self.price = None
        self.departure_airport_code = None
        self.departure_city = None

