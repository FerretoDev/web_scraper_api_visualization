from fastapi import APIRouter

from app.scraping.data_cleaner import clean_data
from app.scraping.scraper import scrape_data

router = APIRouter()


@router.get("/data")
def get_data():
    raw_data = scrape_data()
    cleaned_data = clean_data(raw_data)
    return {"cleaned_data": cleaned_data.to_dict(orient="records")}
