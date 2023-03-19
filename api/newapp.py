from fastapi import FastAPI, Depends, APIRouter
from api.endpoints.database.damacana_db import router as damacana_db_router
from api.endpoints.auth.auth import get_current_user
from api.endpoints.database.users_db import router as users_db_router
from api.middlewares.sanitizer.sanitizer import (
    SanitizerMiddleware as sanitizer_middleware,
)

testrouter = APIRouter()


@testrouter.get("/test")
async def test(current_user: dict = Depends(get_current_user)):
    return {"message": f'Hello {current_user["username"]}'}


def new_app():
    app = FastAPI()
    app.include_router(
        damacana_db_router,
    )
    app.include_router(testrouter)
    app.include_router(users_db_router)
    app.add_middleware(sanitizer_middleware, some_attribute="sanitizer")
    app.title = "Damacansu Sepeti"
    app.description = "caner bir şeyler yapıyor"
    return app
