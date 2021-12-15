from fastapi.responses import ORJSONResponse
from src.models.user import UserBase
from ....database.database import User, get_db, Session
from fastapi import APIRouter, Body, Depends
from fastapi.exceptions import HTTPException
from starlette.status import HTTP_200_OK, HTTP_202_ACCEPTED
from src.crud.user import get_user


router = APIRouter()


@router.get(
    "/user/{id}",
    tags=["User"],
    status_code=HTTP_200_OK,
    response_model=UserBase,
    response_class=ORJSONResponse,
)
async def get(id: int, db: Session = Depends(get_db)):
    return await get_user(id=id, db=db)
