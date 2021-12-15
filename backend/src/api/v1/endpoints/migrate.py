from fastapi import APIRouter
from fastapi.responses import ORJSONResponse

from src.database.migrate import migrate

from starlette.status import HTTP_200_OK


router = APIRouter()


@router.post(
    "/migrate/start",
    tags=["Migrate"],
    status_code=HTTP_200_OK,
    response_class=ORJSONResponse,
)
async def reviews_get():
    await migrate()
