from fastapi import FastAPI

from app.routes import router

app = FastAPI()

# Incluir rutas desde el router
app.include_router(router)


@app.get("/")
def read_root():
    return {"message": "Welcome to the Web Scraping API with FastAPI!"}
