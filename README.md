# Web Scraper API Visualization with FastAPI

Este proyecto es una aplicación que realiza web scraping, desarrolla una API y visualiza los datos extraídos utilizando FastAPI, Selenium, y Seaborn.

## Características

- **Web Scraping:** Extrae datos de un sitio web utilizando Selenium.
- **API REST:** Implementa una API con FastAPI para exponer los datos scrapeados.
- **Análisis de Datos:** Procesa y visualiza los datos utilizando Pandas y Seaborn.
- **Contenerización:** Configurado para ejecutarse en un contenedor Docker.

## Requisitos

1. **Python 3.11**
2. **Chromedriver:** Para Selenium. Asegúrate de tenerlo en tu PATH.
3. **Docker (opcional):** Para contenerizar la aplicación.

## Instalación

1. **Clonar el repositorio:**
   ```bash
   git clone https://github.com/FerretoDev/web-scraper-api-visualization.git
   cd web-scraper-api-visualization
   ```

2. **Configurar el entorno virtual:**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # En Windows usa .venv\Scripts\activate
   ```

3. **Instalar las dependencias:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configurar Chromedriver:**
   - Descarga Chromedriver desde su sitio oficial y asegúrate de que esté en el PATH.

## Uso

1. **Ejecutar la API localmente:**
   ```bash
   fastapi dev app/main.py
   ```

2. **Acceder a los endpoints:**
   - **GET /**: Página de bienvenida.
   - **GET /scrape**: Ejecuta el scraping y devuelve los datos extraídos.

## Contenerización (opcional)

Si prefieres ejecutar la aplicación en un contenedor Docker:

1. **Construir la imagen Docker:**
   ```bash
   docker build -t web-scraper-api .
   ```

2. **Ejecutar el contenedor:**
   ```bash
   docker run -d -p 8000:8000 web-scraper-api
   ```

3. **Acceder a la aplicación:**
   - Visita `http://localhost:8000` para acceder a la API.

## Estructura del Proyecto

```plaintext
web-scraper-api-visualization/
│
├── app/                        # Código de la aplicación
│   ├── main.py                 # Archivo principal de FastAPI
│   ├── routes.py               # Rutas y endpoints de la API
│   ├── scraping/               # Lógica de scraping y limpieza de datos
│   ├── api/                    # Controladores de la API
│   └── utils/                  # Configuraciones y utilidades
│
├── data/                       # Almacena los datos extraídos y procesados
│
├── docs/                       # Documentación adicional
│   ├── README.md               # Explicación general del proyecto (este archivo)
│   └── tutorial.md             # Tutorial detallado
│
├── tests/                      # Pruebas automatizadas
│
├── notebooks/                  # Notebooks para análisis exploratorio
│
├── requirements.txt            # Dependencias del proyecto
├── Dockerfile                  # Configuración de Docker
└── .gitignore                  # Archivos ignorados en Git
```

## Pruebas

Para ejecutar las pruebas unitarias:

```bash
pytest
```

## Reflexión

Este proyecto permitió integrar diversas técnicas, desde la automatización del scraping hasta la creación de visualizaciones de datos. A lo largo del desarrollo, fue esencial asegurar la estabilidad del scraping, la eficiencia en el procesamiento de datos, y la creación de una API robusta.

## Contribuciones

Si deseas contribuir a este proyecto, por favor, haz un fork del repositorio y envía un pull request. ¡Todas las contribuciones son bienvenidas!

## Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo `LICENSE` para más detalles.
