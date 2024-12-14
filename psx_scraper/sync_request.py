import os
import time

import requests
from dotenv import load_dotenv
from symbols import symbols

load_dotenv()
api_key = os.getenv("ALPHAVANTAGE_API_KEY")
url = "https://www.alphavantage.co/query?function=OVERVIEW&symbol={}&apikey={}"

results = []


def get_symbols():
    for symbol in symbols:
        print(f"Working on symbol: {symbol}")
        response = requests.get(url.format(symbol, api_key))
        results.append(response.json())


start = time.time()
get_symbols()
end = time.time()

total_time = end - start

print("\nYou did it!")
print(f"It took {total_time:.2f} seconds to make {len(symbols)} API calls.")
