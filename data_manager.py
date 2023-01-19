import pandas
from dotenv import load_dotenv
load_dotenv('/Users/natha/PycharmProjects/info.env')


class DataManager:

    def __init__(self):
        self.df = pandas.read_csv("flights.csv")


    def get_cities(self):
        cities = []
        for city in self.df.get("City"):
            cities.append(city)
        return cities

    def get_hawaii_cities(self):
        hawaii_cities = []
        for i in range(9,17):
            hawaii_cities.append(self.df.loc[[i]])
        return hawaii_cities

    def update_price(self, city, price):
        index = self.df.index[self.df['City'] == city].tolist()[0]
        self.df.loc[index, 'Lowest Price'] = price
        self.df.to_csv("flights.csv", index=False)

    def update_aita(self, city, iata):
        index = self.df.index[self.df['City'] == city].tolist()[0]
        self.df.loc[index, 'IATA'] = iata
        self.df.to_csv("flights.csv", index=False)

    def get_price(self, city):
        index = self.df.index[self.df["City"] == city].tolist()[0]
        return self.df.loc[index, 'Lowest Price']

    def get_file_city_code(self, city):
        index = self.df.index[self.df["City"] == city].tolist()[0]
        return self.df.loc[index, 'IATA']

    def get_stopovers(self, city):
        index = self.df.index[self.df["City"] == city].tolist()[0]
        return self.df.loc[index, 'Stopovers']

    def update_stopovers(self, city, stopovers):
        index = self.df.index[self.df['City'] == city].tolist()[0]
        self.df.loc[index, 'Stopovers'] = stopovers
        self.df.to_csv("flights.csv", index=False)

    def update_from_date(self, city, date):
        index = self.df.index[self.df['City'] == city].tolist()[0]
        self.df.loc[index, 'FromDate'] = date
        self.df.to_csv("flights.csv", index=False)

    def update_to_date(self, city, date):
        index = self.df.index[self.df['City'] == city].tolist()[0]
        self.df.loc[index, 'ToDate'] = date
        self.df.to_csv("flights.csv", index=False)

    def update_info(self, city, price, from_date, to_date, stopovers):
        self.update_price(city, price)
        self.update_from_date(city, from_date)
        self.update_to_date(city, to_date)
        self.update_stopovers(city, stopovers)