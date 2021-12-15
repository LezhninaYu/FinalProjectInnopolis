from src.models.message import MessageBase
from src.core.security import get_password_hash
from src.database.database import get_db, Session, Post
from src.helpers.exceptions import EntityDoesNotExist
from fastapi import Depends
from fastapi.exceptions import HTTPException


async def create_post(post, db: Session):
    postdb = Post()
    postdb.name = post.name
    postdb.text = post.text
    postdb.user_id = post.user_id
    db.add(postdb)
    db.commit()
    return postdb


async def update_post(post, post_id, db: Session):
    postdb = db.query(Post).filter(Post.id == post_id).first()
    if postdb is None:
        raise HTTPException(status_code=404, detail="post does not exists")
    if post.name != None:
        postdb.name = post.name
    if post.text != None:
        postdb.text = post.text
    db.commit()
    return postdb


async def delete_post(post_id, db: Session):
    postdb = db.query(Post).filter(Post.id == post_id).first()
    if postdb is None:
        raise HTTPException(status_code=404, detail="post does not exists")
    db.delete(postdb)
    db.commit()
    return "Success"


async def get_post(post_id, db: Session):
    postdb = db.query(Post).filter(Post.id == post_id).first()
    if postdb is None:
        raise HTTPException(status_code=404, detail="post does not exists")
    return postdb


async def get_post_list(db: Session):
    return db.query(Post).all()
