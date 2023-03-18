import mongomock
import pytest
from database.connect import damacana_db, damacana_storage

@pytest.fixture
def db():
    # Create a fake database and collection using mongomock
    client = mongomock.MongoClient()
    db = client[damacana_db]
    yield db
    client.close()


def test_create_damacana(db):
    # Create a test damacana object
    damacana = {
                "name": "Erikli 19 Liter",
                "description": "Erikli 19 Liter Damacana",
                "image": "https://www.example.com/image.jpg",
                "price": 23.99,
                "quantity": 30,
            }

    # Call the create_damacana function with the test damacana object
    result = db[damacana_storage].insert_one(damacana)

    # Check that the result is successful and the damacana object has been created
    assert result.acknowledged
    assert db[damacana_storage].count_documents({}) == 1
    assert db[damacana_storage].find_one({"_id": result.inserted_id}) == {
                "_id": result.inserted_id,
                "name": "Erikli 19 Liter",
                "description": "Erikli 19 Liter Damacana",
                "image": "https://www.example.com/image.jpg",
                "price": 23.99,
                "quantity": 30,
            }

