from db.config import SessionLocal
from users.models import User
from sqlalchemy import select


def create_user(name:str, email:str):
    with SessionLocal() as session:
        user = User(name=name, email=email)
        session.add(user)
        session.commit()
        
def all_user():
    with SessionLocal() as session:
        stmt = select(User)
        users = session.scalar(stmt)
        return users.all()