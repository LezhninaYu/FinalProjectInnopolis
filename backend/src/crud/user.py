from src.core.security import get_password_hash
from src.models.user import UserBase
from src.database.database import User, get_db, Session
from src.helpers.exceptions import EntityDoesNotExist
from fastapi import Depends


async def create_user(user, db: Session):
    if db.query(User).filter(User.email == user.email).first() == None:
        user.password = get_password_hash(user.password)
        new_user = User(email=user.email, password=user.password)
        db.add(new_user)
        db.commit()
        return UserBase(id=new_user.id, email=user.email)
    else:
        return None


async def get_user(id: int, db: Session):
    dbuser = db.query(User).filter(User.id == id).first()
    if dbuser is not None:
        return UserBase.from_orm(dbuser)
    return None
