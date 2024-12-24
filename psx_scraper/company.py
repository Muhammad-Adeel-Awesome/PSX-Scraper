from dataclasses import dataclass

from req_http import http_get_async, http_get_sync
from requests import Session


@dataclass
class Sector:
    id: str
    name: str


@dataclass
class ListedCompany:
    sector_id: str
    symbol: str
    name: str


def fetch_sector_companies_sync(
    session: Session,
    sector: Sector,
    url: str,
    headers: dict[str, str],
    xid: str,
) -> list[ListedCompany]:
    params = {"sector": sector.id, "XID": xid}
    response = http_get_sync(session, url, headers, params)
    companies_list = response.json()
    return [
        ListedCompany(
            sector_id=sector.id,
            symbol=company["symbol_code"],
            name=company["company_name"],
        )
        for company in companies_list
    ]


async def fetch_sector_companies(
    session: Session,
    sector: Sector,
    url: str,
    headers: dict[str, str],
    xid: str,
) -> list[ListedCompany]:
    params = {"sector": sector.id, "XID": xid}
    response = await http_get_async(session, url, headers, params)
    companies_list = response.json()
    return [
        ListedCompany(
            sector_id=sector.id,
            symbol=company["symbol_code"],
            name=company["company_name"],
        )
        for company in companies_list
    ]
