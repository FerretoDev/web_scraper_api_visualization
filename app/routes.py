from fastapi import APIRouter

from app.scraping.scraper import scrape_data  # Importar la función de scraping

router = APIRouter()


@router.get("/scrape")
def scrape_endpoint():
    try:
        data = scrape_data()  # Ejecutar la función de scraping
        return {"data": data}
    except Exception as e:
        return {"error": str(e)}
