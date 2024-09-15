from fastapi import FastAPI, HTTPException, Depends
from fastapi.responses import JSONResponse
from fastapi.requests import Request
from fastapi.security import OAuth2PasswordBearer, Security
from fastapi.security.utils import get_authorization_scheme_param
from pydantic import BaseModel
from sqlalchemy.orm import Session
from models import Fruit, FruitModel, User, UserModel
from database import SessionLocal, engine

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def authenticate_user(username: str, password: str, db: Session):
    user = db.query(User).filter(User.username == username).first()
    if not user or not user.password == password:
        return None
    return user

def authenticate_user_from_token(token: str, db: Session):
    user_id = get_authorization_scheme_param(token)
    user = db.query(User).filter(User.id == user_id).first()
    return user

def create_access_token(data: dict):
    # Implement your access token creation logic here
    # Return the access token
    return "access_token"

@app.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = authenticate_user(form_data.username, form_data.password, db)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid username or password")
    access_token = create_access_token({"sub": user.id})
    return {"access_token": access_token, "token_type": "bearer"}

@app.get("/fruits/")
async def read_fruits(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    user = authenticate_user_from_token(token, db)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid token")
    fruits = db.query(Fruit).all()
    return {"fruits": [FruitModel.from_orm(fruit) for fruit in fruits]}

@app.get("/fruits/{fruit_id}")
async def read_fruit(fruit_id: int, token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    user = authenticate_user_from_token(token, db)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid token")
    fruit = db.query(Fruit).filter(Fruit.id == fruit_id).first()
    if fruit is None:
        raise HTTPException(status_code=404, detail="Fruit not found")
    return FruitModel.from_orm(fruit)

@app.post("/fruits/")
async def create_fruit(fruit: FruitModel, token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    user = authenticate_user_from_token(token, db)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid token")
    db_fruit = Fruit(**fruit.dict())
    db.add(db_fruit)
    db.commit()
    db.refresh(db_fruit)
    return JSONResponse(status_code=201, content={"fruit_id": db_fruit.id})

@app.put("/fruits/{fruit_id}")
async def update_fruit(fruit_id: int, fruit: FruitModel, token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    user = authenticate_user_from_token(token, db)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid token")
    db_fruit = db.query(Fruit).filter(Fruit.id == fruit_id).first()
    if db_fruit is None:
        raise HTTPException(status_code=404, detail="Fruit not found")
    db_fruit.name = fruit.name
    db_fruit.description = fruit.description
    db.commit()
    return JSONResponse(status_code=200, content={"message": "Fruit updated"})

@app.delete("/fruits/{fruit_id}")
async def delete_fruit(fruit_id: int, token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    user = authenticate_user_from_token(token, db)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid token")
    db_fruit = db.query(Fruit).filter(Fruit.id == fruit_id).first()
    if db_fruit is None:
        raise HTTPException(status_code=404, detail="Fruit not found")
    db.delete(db_fruit)
    db.commit()
    return JSONResponse(status_code=200, content={"message": "Fruit deleted"})