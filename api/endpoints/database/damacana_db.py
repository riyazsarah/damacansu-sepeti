from http import HTTPStatus as status
from fastapi import APIRouter, Body, HTTPException, Depends
from fastapi.encoders import jsonable_encoder
from motor.motor_asyncio import AsyncIOMotorCollection
from starlette.responses import JSONResponse
from typing import List
from database.connect import damacana_storage, get_db, damacana_db
from database.models import DamacanaDBModel

router = APIRouter()


@router.post(
    "/damacana/new",
    response_description="Adds new damacana to the database.",
    response_model=DamacanaDBModel,
)
async def create_damacana(
    damacana: DamacanaDBModel = Body(...),
    db: AsyncIOMotorCollection = Depends(get_db(database_name=damacana_db, collection_name=damacana_storage)),
):
    f"""
    Adds new damacana to the database.
    :param db: {AsyncIOMotorCollection}
    :param damacana: {str}
    :return: {DamacanaDBModel}
    """
    damacana = jsonable_encoder(damacana)
    new_damacana = await db.insert_one(damacana)
    created_damacana = await db.find_one({"_id": new_damacana.inserted_id})
    return JSONResponse(status_code=status.CREATED, content=created_damacana)


@router.get(
    "/damacana/{id}",
    response_description="Retrieves damacana from it's ID.",
    response_model=DamacanaDBModel,
)
async def get_damacana_from_id(
    damacana_id: str,
        db: AsyncIOMotorCollection = Depends(get_db(database_name=damacana_db, collection_name=damacana_storage)),
):
    f"""
    Retrieves damacana from it's ID.
    :param db: {AsyncIOMotorCollection}
    :param damacana_id: {str}
    :return:  {DamacanaDBModel}
    """
    if (
        damacana := await db.find_one({"_id": damacana_id})
    ) is not None:
        return damacana
    elif damacana is None:
        return HTTPException(
            status_code=status.BAD_REQUEST,
            detail=f"no damacana found with specified id: {damacana_id}",
        )
    return HTTPException(
        status_code=status.INTERNAL_SERVER_ERROR, detail="please contact admins"
    )


@router.get(
    "/damacana/search/",
    response_description="Retrieves a list of damacana that contains the specified name.",
    response_model=List[DamacanaDBModel],
)
async def get_damacana_from_name(
    damacana_name: str,
    db: AsyncIOMotorCollection = Depends(get_db(database_name=damacana_db, collection_name=damacana_storage)),
):
    f"""
    Retrieves a list of damacana that contains the specified name.
    :param db: {AsyncIOMotorCollection}
    :param damacana_name: {str}
    :return: {List[DamacanaDBModel]}
    """
    # $regex => if string contains
    # $options => regex options, i => lowercase regex search
    # to_list is necessary. it converts the search result to a list, with 1000 length limit.
    damacana_list = (
        await db.find({"name": {"$regex": damacana_name, "$options": "i"}})
        .to_list(1000)
    )
    if damacana_list:
        return JSONResponse(status_code=status.OK, content=damacana_list)
    else:
        raise HTTPException(
            status_code=status.BAD_REQUEST,
            detail=f"no damacana contains the name {damacana_name}",
        )


@router.get(
    "/damacana/",
    response_description="Returns everything in damacana storage.",
    response_model=List[DamacanaDBModel],
)
async def list_damacana_storage(
    db: AsyncIOMotorCollection = Depends(get_db(database_name=damacana_db, collection_name=damacana_storage)),
):
    f"""
    Returns everything in damacana storage.
    :return:  {List[DamacanaDBModel]}
    """
    try:
        damacana_list = await db.find().to_list(1000)
        if not damacana_list:
            raise HTTPException(
                status.BAD_REQUEST, detail="no existing damacana in storage"
            )
        return JSONResponse(status_code=status.OK, content=damacana_list)
    except HTTPException as e:
        raise HTTPException(
            status_code=status.INTERNAL_SERVER_ERROR, detail=str(e)
        )
