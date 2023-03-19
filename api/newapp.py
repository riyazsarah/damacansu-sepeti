from fastapi import FastAPI
from api.endpoints.database.damacana_db import router as damacana_db_router
from api.middlewares.sanitizer.sanitizer import (
    SanitizerMiddleware as sanitizer_middleware,
)


def new_app():
    app = FastAPI()
    app.include_router(damacana_db_router)
    app.add_middleware(sanitizer_middleware, some_attribute="sanitizer")
    app.title = "Damacansu Sepeti"
    app.description = "caner bir şeyler yapıyor"
    return app
