from bs4 import BeautifulSoup
from company import Sector
from requests import Response


def fetch_page_content(response: Response, parser="lxml") -> BeautifulSoup:
    return BeautifulSoup(response.text, parser)


def get_element_by_class(soup: BeautifulSoup, class_name: str) -> BeautifulSoup:
    element = soup.find(class_=class_name)
    if element is None:
        raise ValueError(f"Class '{class_name}' not found in the provided HTML.")
    return element  # type: ignore


def get_xid(soup: BeautifulSoup) -> str:
    xid_container = soup.find("input", attrs={"id": "XID"})
    if not xid_container:
        raise ValueError("Error! Could not find the 'XID' input field.")

    xid = xid_container.get("value")  # type: ignore
    if not xid:
        raise ValueError("Error! 'XID' input field is present but has no value.")

    return xid  # type: ignore


def extract_sectors(sector_container: BeautifulSoup) -> list[Sector]:
    sector_options = sector_container.find("select", attrs={"name": "sector"})
    if not sector_options:
        raise ValueError("Error! Could not find the sector options.")

    sectors = sector_options.find_all("option")  # type: ignore
    if not sectors:
        raise ValueError("Error! There aren't any sectors in the sector options.")

    sectors = [
        Sector(id=sector.get("value"), name=sector.text.strip())
        for sector in sectors
        if sector.get("value") != "0"
    ]
    return sectors
