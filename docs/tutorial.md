# Tutorial

Este documento proporciona una guía paso a paso sobre cómo configurar y ejecutar este proyecto.

### Requisitos previos

1. Python 3.11
2. `Chromedriver` instalado y en la ruta de tu sistema.
3. Conexión a internet para acceder al sitio web que vas a scrapear.

### Configuración

1. Configura tu entorno virtual.
2. Instala las dependencias desde `requirements.txt`.
3. Asegúrate de tener `Chromedriver` configurado correctamente.

### Ejecución

- Inicia la aplicación con `uvicorn app.main:app --reload`.
- Usa las rutas API expuestas para obtener los datos scrapeados y analizados.

### Pruebas

Para ejecutar las pruebas, usa `pytest` en la raíz del proyecto.
