import asyncio
from typing import Optional

from requests import Response, Session


def http_get_sync(
    session: Session,
    url: str,
    headers: Optional[dict[str, str]] = None,
    params: Optional[dict[str, str]] = None,
) -> Response:
    response = session.get(url, headers=headers, params=params)
    response.raise_for_status()
    return response


async def http_get_async(
    session: Session,
    url: str,
    headers: Optional[dict[str, str]] = None,
    params: Optional[dict[str, str]] = None,
) -> Response:
    return await asyncio.to_thread(http_get_sync, session, url, headers, params)
