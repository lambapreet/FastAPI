from db import engine
from sqlalchemy import MetaData, Table, Column, Integer, String, DateTime, ForeignKey

metadata = MetaData()

users = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String(length=50), nullable=False),
    Column("email", String, nullable=False, unique=True),
)

post = Table(
    "post",  
    metadata,
    Column("id", Integer, primary_key=True),
    Column("user_id", Integer, ForeignKey(users.c.id, ondelete="CASCADE"), nullable=False),  # ✅ use users.c.id
    Column("title", String, nullable=False),
    Column("content", String, nullable=False),
)



def create_table():
    metadata.create_all(engine)


