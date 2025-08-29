from sqlmodel import SQLModel, Session, select
from db.config import engine
from .models import User


def create_user(name:str, email:str):
    user = User(name=name, email=email)
    with Session(engine) as session:
        session.add(user)
        session.commit()
        session.refresh(user)
        return user
    
def all_users():
    with Session(engine) as session:
        stmt = select(User)
        users = session.exec(stmt)
        return users.all()