PSX_COMPANY_LISTINGS_URL = (
    "https://www.psx.com.pk/psx/resources-and-tools/listings/listed-companies"
)
SEARCH_COMPANY_URL = (
    "https://www.psx.com.pk/psx/custom-templates/companiesSearch-sector"
)

HEADERS = {
    "User-Agent": "Mozilla/5.0",
    "Accept": "application/json",
    "X-Requested-With": "XMLHttpRequest",
    "Referer": PSX_COMPANY_LISTINGS_URL,
}

SECTOR_CONTAINER_CLASS = "notice-update-div"
