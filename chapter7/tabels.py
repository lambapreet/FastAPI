from db import engine
from sqlalchemy import MetaData, Table, Column, Integer, String, DateTime, ForeignKey

metadata = MetaData()

users = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String(length=50), nullable=False),
    Column("email", String, nullable=False, unique=True),
    Column("phone", Integer, unique=True, nullable=False)
)

post = Table(
    "post",  # ✅ Missing table name added
    metadata,
    Column("id", Integer, primary_key=True),
    Column("user_id", Integer, ForeignKey(users.c.id, ondelete="CASCADE"), nullable=False),  # ✅ use users.c.id
    Column("title", String, nullable=False),
    Column("content", String, nullable=False),
)

profile = Table(
    "profile",  
    metadata,
    Column("id", Integer, primary_key=True),
    Column("user_id", Integer, ForeignKey(users.c.id, ondelete="CASCADE"), nullable=False),  
    Column("bio", String, nullable=False),
    Column("address", String, nullable=False),
)

address = Table(
    "address",  
    metadata,
    Column("id", Integer, primary_key=True), 
    Column("city", String, nullable=False),
    Column("country", String, nullable=False),
)

user_address_association = Table(
    "user_address_association",
    metadata,
    Column("user_id", Integer, ForeignKey(users.c.id, ondelete="CASCADE"), primary_key=True),
    Column("address_id", Integer, ForeignKey(address.c.id, ondelete="CASCADE"), primary_key=True),  
)

def create_table():
    metadata.create_all(engine)

# def drop_table():
#     metadata.drop_all(engine)
