from selenium import webdriver
from selenium.webdriver.common.by import By


def scrape_data(url: str):
    """Scrapes data from a specified webpage using Selenium.

    This function navigates to a given URL and extracts data from a table present on the webpage. The extracted data is returned as a list of rows, where each row contains the values of the table cells.

    Args:
        url (str): The URL of the webpage to scrape data from.

    Returns:
        list: A list of rows containing the scraped data, where each row is a list of cell values.

    Raises:
        WebDriverException: If there is an issue with the Selenium WebDriver.
    """

    # Configurar Selenium
    driver = (
        webdriver.Chrome()
    )  # Asegúrate de tener Chromedriver instalado y configurado
    # driver.get(
    #    "https://data.wa.gov/Transportation/Electric-Vehicle-Population-Data/f6w7-q2d2"
    # )  # Cambia por la URL del sitio web

    driver.get(f"{url}")

    # Extraer datos usando Selenium (ejemplo)
    elements = driver.find_elements(
        By.CSS_SELECTOR, "table tr"
    )  # Ajusta el selector CSS
    data = []

    for element in elements:
        if row := [cell.text for cell in element.find_elements(By.TAG_NAME, "td")]:
            data.append(row)

    driver.quit()  # Cierra el navegador

    return data
