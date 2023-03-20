from datetime import datetime, timedelta
from fastapi.testclient import TestClient
import jwt
import mongomock
import pytest
from motor.motor_asyncio import AsyncIOMotorCollection

from api.auth.auth import (
    sign_up_handler,
    compare_plain_hashed_password,
)
from api.newapp import new_app
from api.endpoints.database.users_db import return_db_struct
from api.models.users import UserSignup
from api.endpoints.database.connect import users_db, users_collection
from api.endpoints.database.models import UserDBModel


# generate user login object yourself, after signing up.

@pytest.fixture
def test_http_client():
    client = TestClient(new_app())
    yield client

@pytest.fixture
def user_details():
    user_signup_details = UserSignup(
        email="example@gmail.com",
        password="password",
    )
    yield user_signup_details


@pytest.fixture
def db():
    # Create a fake database and collection using mongomock
    client = mongomock.MongoClient()
    db = client[users_db][users_collection]
    yield db
    client.close()


@pytest.fixture
def db_fields():
    yield UserDBModel.DBFields


def tokens_dict(
    user_details: UserSignup = None, db_fields: UserDBModel.DBFields = None, exp_time: datetime = None
):
    tokens = sign_up_handler(user_details.email, user_details.password, exp_time)
    assert tokens.get(db_fields.ACCESS_TOKEN.value) is not None
    assert tokens.get(db_fields.SECRET_TOKEN.value) is not None
    assert tokens.get(db_fields.REFRESH_TOKEN.value) is not None
    return tokens


def clean_db(db):
    db.delete_many({})
    #  to make sure if the database is empty.
    assert db.count_documents({}) == 0


def create_new_user(
    db: AsyncIOMotorCollection = None,
    user_details: UserSignup = None,
    db_fields: UserDBModel.DBFields = None,
    exp_time: datetime = datetime.utcnow() + timedelta(hours=24)
) -> tuple:
    f"""
    Creates a new user in the database and then pulls the user from the database with the same email.
    :param exp_time: Expiration time of auth key.
    :param db: {AsyncIOMotorCollection}
    :param user_details: {UserSignup}
    :param db_fields: {UserDBModel.DBFields}
    :return: tuple => (inserted_dict, tokens), inserted_dict is the inserted document in the database 
    (which retrieved from DB), tokens is the tokens returned by the sign_up_handler.
    """
    # we dont need to check if the user is already signed up, because we are using a mock database.
    tokens = tokens_dict(user_details, db_fields, exp_time)
    db.insert_one(return_db_struct(tokens, user_details))
    inserted = db.find_one(
        {
            db_fields.EMAIL.value: user_details.email,
        }
    )
    inserted_dict = dict(inserted)
    return inserted_dict, tokens


def test_user_signup(db, user_details, db_fields, test_http_client):
    f"""
    Tests:
    -> If the user is added to the database.
    -> If password is correctly hashed and salted.
    :param db: {AsyncIOMotorCollection}
    :param user_details: {UserSignup}
    :param db_fields: {UserDBModel.DBFields}
    """
    # we dont need to check if the user is already signed up, because we are using a mock database.
    s, tokens = create_new_user(db=db, user_details=user_details, db_fields=db_fields)
    # assert that all the fields are the same.
    assert s.get(db_fields.EMAIL.value) == user_details.email
    assert s.get(db_fields.ACCESS_TOKEN.value) == tokens.get(
        db_fields.ACCESS_TOKEN.value
    )
    assert s.get(db_fields.SECRET_TOKEN.value) == tokens.get(
        db_fields.SECRET_TOKEN.value
    )
    assert s.get(db_fields.REFRESH_TOKEN.value) == tokens.get(
        db_fields.REFRESH_TOKEN.value
    )
    # assert that hashed password corresponds to the plain password.
    assert compare_plain_hashed_password(
        user_details.password, s.get(db_fields.PASSWORD.value)
    )
    # now hit real endpoint
    response = test_http_client.post("/user/signup", json=user_details.dict())
    # assure that status code is 200
    assert response.status_code == 200
    # and that is it. we already tested the database operations in this test.
    clean_db(db)


def test_user_login(db, user_details, db_fields):
    f"""
    Tests:
    -> If the user is able to login.
    -> If expiration time of the access token's behaviour is correct.
    :param db:  {AsyncIOMotorCollection}
    :param user_details: {UserSignup}
    :param db_fields: {UserDBModel.DBFields}
    """
    s, tokens = create_new_user(db=db, user_details=user_details, db_fields=db_fields)
    assert compare_plain_hashed_password(user_details.password, s.get(db_fields.PASSWORD.value))
    # clean the db
    clean_db(db)
    # now create an auth key for the user with the 1 second expiration time.
    s, tokens = create_new_user(db=db, user_details=user_details, db_fields=db_fields, exp_time=datetime.utcnow() + timedelta(seconds=1))
    try:
        jwt.decode(tokens.get(db_fields.ACCESS_TOKEN.value), tokens.get(db_fields.SECRET_TOKEN.value), algorithms=["HS256"])
    except jwt.ExpiredSignatureError:
        pass # this is the expected behavior.
    except jwt.InvalidTokenError as e:
        pytest.fail(f"Invalid token error: {e}")
    # clean the db
    clean_db(db)

def test_refresh_auth_token(db, user_details, db_fields):
    s, tokens = create_new_user(db=db, user_details=user_details, db_fields=db_fields)
    new_auth_token = sign_up_handler(user_details.email, user_details.password, datetime.utcnow() + timedelta(hours=24))
    result = db.update_one(
        {
            "$and": [
                {
                    db_fields.ACCESS_TOKEN.value: tokens.get(db_fields.ACCESS_TOKEN.value)
                },
                {
                    db_fields.REFRESH_TOKEN.value: tokens.get(db_fields.REFRESH_TOKEN.value)
                },
            ]
        },
        {"$set": {db_fields.ACCESS_TOKEN.value: new_auth_token }},
    )
    assert result.modified_count == 1
    new_user = db.find_one(
        {
            db_fields.EMAIL.value: user_details.email,
        }
    )
    assert new_user.get(db_fields.ACCESS_TOKEN.value) != tokens.get(db_fields.ACCESS_TOKEN.value)
    assert new_user.get(db_fields.ACCESS_TOKEN.value) == new_auth_token
    assert new_user.get(db_fields.REFRESH_TOKEN.value) == tokens.get(db_fields.REFRESH_TOKEN.value)
    clean_db(db)