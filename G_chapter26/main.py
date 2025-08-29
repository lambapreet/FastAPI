from fastapi import FastAPI
from user.models import User
from product.models import Product
from db.config import create_tables
from contextlib import asynccontextmanager
from user.services import *

@asynccontextmanager
async def lifespan(app: FastAPI):
    create_tables()
    yield

app = FastAPI(lifespan=lifespan)

@app.post("/user")
async def user_create(new_user:dict):
    user = create_user(name=new_user["name"], email=new_user["email"])
    return user

@app.get("/user")
async def get_all_users():
    users = all_users()
    return users