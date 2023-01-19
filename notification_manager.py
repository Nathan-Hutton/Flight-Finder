from twilio.rest import Client
from dotenv import load_dotenv
import os
load_dotenv('/Users/natha/PycharmProjects/info.env')

class NotificationManager:
    def __init__(self):
        self.sid = os.getenv('TWILIO_SID')
        self.auth_token = os.getenv('OWM_AUTH_TOKEN')
        self.recipient_phone = os.getenv('TWILIO_RECEIVER')
        self.sender_phone = os.getenv('TWILIO_SENDER')

        self.client = Client(self.sid, self.auth_token)

    def send_message(self, price, depart_city, depart_airport, city, arrival_airport, outbound_date, inbound_date, flight_no):
        # text = f"Flight from {depart_city}({depart_airport}) to {city}({arrival_airport}) price has dropped to ${price} on {outbound_date}, " \
        #        f"arrival: {inbound_date}. Flight number: {flight_no}"
        #
        # message = self.client.messages \
        #     .create(
        #     body=text,
        #     from_=self.sender_phone,
        #     to=self.recipient_phone
        # )
        # print(message.status)
        pass