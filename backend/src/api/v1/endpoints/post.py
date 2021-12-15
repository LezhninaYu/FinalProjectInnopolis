from fastapi.responses import ORJSONResponse
from src.models.message import MessageBase
from src.models.post import ListPostBase, PostBase, PostCreateBase, PostUpdateBase
from src.crud.post import create_post, delete_post, get_post, get_post_list, update_post
from ....database.database import User, get_db, Session
from fastapi import APIRouter, Body, Depends
from fastapi.exceptions import HTTPException
from starlette.status import HTTP_200_OK, HTTP_202_ACCEPTED
from src.crud.user import get_user

router = APIRouter()


@router.post(
    "/post",
    tags=["Post"],
    status_code=HTTP_200_OK,
    response_model=PostBase,
    response_class=ORJSONResponse,
)
async def create(post: PostCreateBase = Body(...), db: Session = Depends(get_db)):
    return await create_post(post=post, db=db)


@router.put(
    "/post/{id}",
    tags=["Post"],
    status_code=HTTP_200_OK,
    response_model=PostBase,
    response_class=ORJSONResponse,
)
async def update(id: int, post: PostUpdateBase = Body(...), db: Session = Depends(get_db)):
    return await update_post(post=post, post_id=id, db=db)


@router.delete(
    "/post/{id}",
    tags=["Post"],
    status_code=HTTP_200_OK,
    response_model=MessageBase,
    response_class=ORJSONResponse,
)
async def delete(id: int, db: Session = Depends(get_db)):
    return MessageBase(message=await delete_post(post_id=id, db=db))


@router.get(
    "/post/{id}",
    tags=["Post"],
    status_code=HTTP_200_OK,
    response_model=PostBase,
    response_class=ORJSONResponse,
)
async def get(id: int, db: Session = Depends(get_db)):
    return await get_post(post_id=id, db=db)


@router.get(
    "/post",
    tags=["Post"],
    status_code=HTTP_200_OK,
    response_model=ListPostBase,
    response_class=ORJSONResponse,
)
async def get_list(db: Session = Depends(get_db)):
    return ListPostBase(posts=await get_post_list(db=db))
