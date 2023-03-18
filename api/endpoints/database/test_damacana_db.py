import mongomock
import pytest
from database.connect import damacana_db, damacana_storage
from bson import raw_bson

testCases = [
    {
        "name": "Erikli 19 Liter",
        "description": "Erikli 19 Liter Damacana",
        "image": "https://www.example.com/image.jpg",
        "price": 23.99,
        "quantity": 30,
    }
]


# put your mock database here
@pytest.fixture
def db():
    # Create a fake database and collection using mongomock
    client = mongomock.MongoClient()
    db = client[damacana_db]
    yield db
    client.close()


# put your testcases here
@pytest.fixture
def damacana_cache():
    damacana = [
        {
            "name": "Erikli 19 Liter",
            "description": "Erikli 19 Liter Damacana",
            "image": "https://www.example.com/image.jpg",
            "price": 23.99,
            "quantity": 30,
        }
    ]
    yield damacana


def test_create_damacana(db, damacana_cache):
    # Call the create_damacana function with the test damacana object
    result = db[damacana_storage].insert_many(damacana_cache)

    # Check that the result is successful and the damacana object has been created
    assert db[damacana_storage].count_documents({}) == len(damacana_cache)
    try:
        # The enumerate function in Python converts a data collection object into an enumerate object.
        # Enumerate returns an object that contains a counter as a key for each value within an object,
        # making items within the collection easier to access.
        for index, damacana_sample_id in enumerate(result.inserted_ids):
            if damacana_sample_id is not None:
                assert (
                        db[damacana_storage].find_one({"_id": damacana_sample_id})
                        == damacana_cache[index]
                )
            else:
                print(f"Case on {index} is null.")
    except TypeError as e:
        print(f"Error unpacking inserted_ids: {e}")



def test_retrieve_damacana_from_id(db, damacana_cache):
    """
    Does basically same thing with create_damacana.
    Inserts testcases.
    Assures that inserted data is equal to damacana_cache's length.
    Iterate over every damacana in cache. If damacana is none, find the ID from result array (which contains inserted ids)
    And then query the ID, then assure that result is equal to damacana.
    """
    # Create a test damacana object
    result = db[damacana_storage].insert_many(damacana_cache).inserted_ids
    # Check that the result is successful and the damacana object has been created
    assert db[damacana_storage].count_documents({}) == len(damacana_cache)
    try:
        for index, damacana in enumerate(damacana_cache):
            if damacana is not None:
                assert (
                        db[damacana_storage].find_one({
                            "_id":result[index]
                        }) == damacana
                )
            else:
                print(f"Case on {index} is null.")
    except TypeError as e:
        print(f"Error unpacking inserted_ids: {e}")