from pydantic import BaseModel


class UserBase(BaseModel):
    id: int
    email: str

    class Config:
        orm_mode = True


class UserInLogin(BaseModel):
    email: str
    password: str


class UserInResponse(BaseModel):
    token: str
