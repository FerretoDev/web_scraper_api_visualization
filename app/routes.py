from typing import List, Union

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from app.scraping.scraper import scrape_data  # Importar la función de scraping

router = APIRouter()


class DataItem(BaseModel):
    key: str
    value: Union[str, List[str]]


class ScrapeResponse(BaseModel):
    data: List[DataItem]


@router.get("/scrape", response_model=ScrapeResponse)
async def scrape_endpoint(url: str) -> dict[str, str]:
    """Handles the scraping of data from a specified URL via an HTTP GET request.

    This asynchronous endpoint receives a URL as a query parameter, invokes the scraping function to retrieve data from that URL, and returns the data in a JSON format. If an error occurs during the scraping process, an error message is returned instead.

    Args:
        url (str): The URL to scrape data from.

    Returns:
        dict: A dictionary containing either the scraped data or an error message.
    """

    try:
        data = scrape_data(url)  # Ejecutar la función de scraping
        if not isinstance(data, list):
            raise ValueError("Data returned from scraping must be a list.")

        structured_data = [
            {"key": item[0], "value": item[1]}
            for item in data
            if isinstance(item, list) and len(item) == 2
        ]

        return {"data": structured_data}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
