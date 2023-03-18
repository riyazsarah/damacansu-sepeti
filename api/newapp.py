from fastapi import FastAPI
from api.endpoints.database.damacana_db import router as damacana_db_router


def new_app():
    app = FastAPI()
    app.include_router(damacana_db_router)
    app.title = "Damacansu Sepeti"
    app.description = "caner bir şeyler yapıyor"
    return app
