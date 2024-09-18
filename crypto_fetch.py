import requests
import csv
from datetime import datetime

# API endpoint
url = 'https://api.coindesk.com/v1/bpi/currentprice.json'

# Send a GET request to the API
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON data
    data = response.json()

    # Extract relevant information
    time_updated = data['time']['updated']
    usd_rate = data['bpi']['USD']['rate']
    gbp_rate = data['bpi']['GBP']['rate']
    eur_rate = data['bpi']['EUR']['rate']

    # Print extracted data (optional)
    print(f"Time Updated: {time_updated}")
    print(f"USD Rate: {usd_rate}")
    print(f"GBP Rate: {gbp_rate}")
    print(f"EUR Rate: {eur_rate}")

    # Save the data into a CSV file
    with open('bitcoin_prices.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        # Write the header
        writer.writerow(['Time Updated', 'USD Rate', 'GBP Rate', 'EUR Rate'])
        # Write the data
        writer.writerow([time_updated, usd_rate, gbp_rate, eur_rate])

    print("Data successfully written to bitcoin_prices.csv")

else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")