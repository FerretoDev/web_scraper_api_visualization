import unittest

from app.scraping.scraper import scrape_data


class TestScraper(unittest.TestCase):
    def test_scrape_data(self):
        data = scrape_data()
        self.assertIsNotNone(data)  # Verificar que se obtienen datos
        self.assertGreater(len(data), 0)  # Verificar que la lista no esté vacía


if __name__ == "__main__":
    unittest.main()
