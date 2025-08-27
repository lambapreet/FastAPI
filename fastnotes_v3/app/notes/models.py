from sqlalchemy.orm import Mapped, mapped_column
from app.db.base import Base
from sqlalchemy import String, Integer,Text


class Note(Base):
    __tablename__="notes"
    
    id:Mapped[int] = mapped_column(primary_key=True)
    tittle:Mapped[str] = mapped_column(String)
    cotent:Mapped[str] = mapped_column(Text)