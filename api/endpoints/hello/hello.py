from fastapi import APIRouter
from api.models.damacana import DamacanaGeneralModel

router = APIRouter()


@router.post("/hello")
async def hello_user(damacana: DamacanaGeneralModel):
    return {"message": f"Hello {damacana.name}"}
