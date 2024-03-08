import requests
import json
import polars as pl
from flask import Flask, render_template



url = "https://storelocator.asda.com/fuel_prices_data.json"
response = requests.get(url)
data = response.json()

lowest_e10_price = float('inf')
lowest_location = None

for station in data["stations"]:
    prices = station['prices']
    location = station['location']

    if 'E10' in prices and prices['E10'] < lowest_e10_price:
        lowest_e10_price = prices['E10']
        lowest_location = location

print("Lowest location" , lowest_location, "Lowest price" , lowest_e10_price)

f = open("lowest_price.txt", "w")
f.write(str(lowest_e10_price))
f.close()




