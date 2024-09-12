from fastapi import APIRouter

from app.scraping.scraper import scrape_data  # Importar la función de scraping

router = APIRouter()


@router.get("/scrape")
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
        return {"data": data}
    except Exception as e:
        return {"error": str(e)}
