from motor import motor_asyncio

client = motor_asyncio.AsyncIOMotorClient("mongodb://localhost:27017")

damacana_db = "damacana_db"
damacana_storage = "damacana_storage"

def get_db(db_name: str):
    return client[db_name]
