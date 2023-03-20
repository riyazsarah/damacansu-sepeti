import motor.motor_asyncio
from fastapi import HTTPException, Depends
from starlette.requests import Request
from starlette.types import Scope
from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorCollection

mongo_url = "mongodb://localhost:27017"

damacana_db = "damacana_db"
damacana_storage = "damacana_storage"
users_db = "users_db"
users_collection = "users_collection"


async def get_database_client() -> AsyncIOMotorClient:
    client = AsyncIOMotorClient(mongo_url)
    try:
        yield client
    finally:
        client.close()


# If function returns a coroutine function, write what that function returns after ->.
def get_db(database_name: str, collection_name: str) -> AsyncIOMotorCollection:
    def get_database(client: AsyncIOMotorClient = Depends(get_database_client)):
        try:
            return client[database_name][collection_name]
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"database error: {e}")

    return get_database
