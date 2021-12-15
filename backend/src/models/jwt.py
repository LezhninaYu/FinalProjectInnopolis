from pydantic import BaseModel


class JWTMeta(BaseModel):
    expire: str
    subject: str


class JWTUser(BaseModel):
    user_id: int
