from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import String, ForeignKey, Text, Table, Column, Integer
from db import engine


# Base class for all models
class Base(DeclarativeBase):
    pass


# ------------------------
# User Model
# ------------------------
class User(Base):
    __tablename__ = "users"   

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    email: Mapped[str] = mapped_column(String(100), nullable=False, unique=True)
    phone : Mapped[int] = mapped_column(Integer, unique=True)


    def __repr__(self) -> str:
        return f"<User(id={self.id}, name={self.name}, email={self.email})>"




