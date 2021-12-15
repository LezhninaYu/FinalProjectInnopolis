from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, ForeignKey


engine_sql_lite = create_engine("sqlite:///database.db", connect_args={
    "check_same_thread": False})
Session = sessionmaker(bind=engine_sql_lite)
Base = declarative_base(bind=engine_sql_lite)


def get_db():
    """Auto closed"""
    db = Session()
    try:
        yield db
    finally:
        db.close()


class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    email = Column(String(128))
    password = Column(String(256))
    posts = relationship("Post", back_populates="user")


class Post(Base):
    __tablename__ = "post"
    id = Column(Integer, primary_key=True)
    name = Column(String(256))
    text = Column(String(1024))
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship("User", back_populates='posts')


Base.metadata.create_all(engine_sql_lite)
