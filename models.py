from pydantic import BaseModel
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Fruit(Base):
    __tablename__ = "fruits"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)

class FruitModel(BaseModel):
    id: int
    name: str
    description: str

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(String)
    password = Column(String)

class UserModel(BaseModel):
    id: int
    username: str
    password: str