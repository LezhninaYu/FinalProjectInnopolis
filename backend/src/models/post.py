from typing import List, Optional
from pydantic import BaseModel


class PostBase(BaseModel):
    id: int
    name: str
    text: str
    user_id: int

    class Config:
        orm_mode = True


class PostCreateBase(BaseModel):
    name: str
    text: str
    user_id: int


class PostUpdateBase(BaseModel):
    name: Optional[str] = None
    text: Optional[str] = None
    user_id: Optional[int] = None


class ListPostBase(BaseModel):
    posts: List[PostBase]
