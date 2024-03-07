import requests, json, polars as pl
url = "https://storelocator.asda.com/fuel_prices_data.json"

response = requests.get(url)
data = response.json()

json_string = json.dumps(data)

df = pl.read_csv("data.json")

lowest_e10_price = float('inf')
lowest_location = None

for station in data["stations"]:
    prices = station['prices']
    location = station['location']

    if 'E10' in prices and prices['E10'] < lowest_e10_price:
        lowest_e10_price = prices['E10']
        lowest_location = location

print("Location with the lowest E10 price:", lowest_location)
print("Lowest E10 price:", lowest_e10_price)

#with open ("data.json", "w") as file:
#    file.write(json_string)