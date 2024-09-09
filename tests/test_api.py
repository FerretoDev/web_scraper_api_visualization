from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {
        "message": "Welcome to the Web Scraping API with FastAPI!"
    }


def test_scrape_endpoint():
    response = client.get("/scrape")
    assert response.status_code == 200
    assert "data" in response.json()
    assert "data" in response.json()
