import asyncio
from time import perf_counter

import requests
from company import fetch_sector_companies
from constants import (
    HEADERS,
    PSX_COMPANY_LISTINGS_URL,
    SEARCH_COMPANY_URL,
    SECTOR_CONTAINER_CLASS,
)
from req_http import http_get_sync
from soup import extract_sectors, fetch_page_content, get_element_by_class, get_xid


async def main():
    print("Starting the PSX scraper...")

    print("Fetching page content...")
    with requests.Session() as session:
        soup = fetch_page_content(http_get_sync(session, url=PSX_COMPANY_LISTINGS_URL))
    print("Page content fetched successfully.")

    print("Extracting sectors...")
    sector_container = get_element_by_class(soup, class_name=SECTOR_CONTAINER_CLASS)
    xid = get_xid(sector_container)
    sectors = extract_sectors(sector_container)
    print("Sectors extracted successfully.")

    print("Fetching companies...")
    with requests.Session() as session:
        tasks = [
            fetch_sector_companies(session, sector, SEARCH_COMPANY_URL, HEADERS, xid)
            for sector in sectors
        ]
        results = await asyncio.gather(*tasks)
    companies = [company for result in results for company in result]
    print("Companies fetched successfully.")


if __name__ == "__main__":
    start_time = perf_counter()
    asyncio.run(main())
    end_time = perf_counter()
    print(f"Time taken: {end_time - start_time:.2f} seconds.")
