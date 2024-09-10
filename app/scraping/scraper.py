from selenium import webdriver
from selenium.webdriver.common.by import By


def scrape_data():
    # Configurar Selenium
    driver = (
        webdriver.Chrome()
    )  # Asegúrate de tener Chromedriver instalado y configurado
    driver.get(
        "https://data.wa.gov/Transportation/Electric-Vehicle-Population-Data/f6w7-q2d2"
    )  # Cambia por la URL del sitio web

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
