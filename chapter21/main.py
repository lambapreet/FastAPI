from fastapi import FastAPI
from users import services as user_service
from pydantic import BaseModel


app = FastAPI()

class UserCreate(BaseModel):
    name: str
    email: str

class UserOut(BaseModel):
    id: int
    name: str
    email: str

    class Config:
        from_attributes = True 


@app.post("/user")
def user_create(user: UserCreate):
    user_service.create_user(name=user.name, email=user.email)
    return {"status": "created user"}


@app.get("/users", response_model=list[UserOut])
def users_all():
    users = user_service.all_user()
    return users
