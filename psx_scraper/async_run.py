import asyncio
import os
import time

from aiohttp import ClientSession
from dotenv import load_dotenv
from symbols import symbols

load_dotenv()
api_key = os.getenv("ALPHAVANTAGE_API_KEY")
url = "https://www.alphavantage.co/query?function=OVERVIEW&symbol={}&apikey={}"

results = []


def get_tasks(session: ClientSession):
    tasks = []
    for symbol in symbols:
        tasks.append(
            asyncio.create_task(session.get(url.format(symbol, api_key), ssl=False))
        )
    return tasks


async def get_symbols():
    async with ClientSession() as session:
        tasks = get_tasks(session)
        responses = await asyncio.gather(*tasks)
        for response in responses:
            results.append(await response.json())


start = time.time()
loop = asyncio.run(get_symbols())
end = time.time()

total_time = end - start

print("\nYou did it!")
print(f"It took {total_time:.2f} seconds to make {len(symbols)} API calls.")
