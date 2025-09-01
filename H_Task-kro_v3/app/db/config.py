from sqlmodel import SQLModel, create_engine, Session
import os
from fastapi import Depends
from typing import Annotated


BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# print(BASE_DIR)

db_path = os.path.join(BASE_DIR, "sqlite.db")


DATABASE_URL = f"sqlite:///{db_path}"

engine = create_engine(DATABASE_URL, echo=True)


def create_tables():
    SQLModel.metadata.create_all(engine)
    
    
def get_session():
    with Session(engine) as session:
        yield
        
DependSession = Annotated[Session, Depends(get_session)]