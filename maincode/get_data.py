import requests
import json
import os

retailers = {
    "Applegreen UK": "https://applegreenstores.com/fuel-prices/data.json",
    "Ascona Group": "https://fuelprices.asconagroup.co.uk/newfuel.json",
    "Asda": "https://storelocator.asda.com/fuel_prices_data.json",
    "bp": "https://www.bp.com/en_gb/united-kingdom/home/fuelprices/fuel_prices_data.json",
    "Esso Tesco Alliance": "https://fuelprices.esso.co.uk/latestdata.json",
    "JET Retail UK": "https://jetlocal.co.uk/fuel_prices_data.json",
    "Morrisons": "https://www.morrisons.com/fuel-prices/fuel.json",
    "Moto": "https://moto-way.com/fuel-price/fuel_prices.json",
    "Motor Fuel Group": "https://fuel.motorfuelgroup.com/fuel_prices_data.json",
    "Rontec": "https://www.rontec-servicestations.co.uk/fuel-prices/data/fuel_prices_data.json",
    "Sainsbury's": "https://api.sainsburys.co.uk/v1/exports/latest/fuel_prices_data.json",
    "SGN": "https://www.sgnretail.uk/files/data/SGN_daily_fuel_prices.json"
}


def get_data():
    for retailer, url in retailers.items():
        response = requests.get(url)
        data = response.json()

        file_name = f"{retailer.lower().replace(' ', '_')}.json"  # Generate the file name from the retailer name
        file_path = os.path.join("data", file_name)  # Save the file in the "data" folder

        # Save the JSON data to the file
        with open(file_path, "w") as file:
            json.dump(data, file)

        print("JSON data saved to", file_path)


print("This run")
get_data()
