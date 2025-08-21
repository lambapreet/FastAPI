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

    # One-to-many: User -> Posts
    posts: Mapped[list["Post"]] = relationship(
        "Post", back_populates="user", cascade="all, delete-orphan"
    )

    def __repr__(self) -> str:
        return f"<User(id={self.id}, name={self.name}, email={self.email})>"


# ------------------------
# Post Model (One-to-Many with User)
# ------------------------
class Post(Base):
    __tablename__ = "posts"   

    id: Mapped[int] = mapped_column(primary_key=True)
    
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    title: Mapped[str] = mapped_column(String(200), nullable=False)
    content: Mapped[str] = mapped_column(Text, nullable=False)

    # Many-to-one: Post -> User
    user: Mapped["User"] = relationship("User", back_populates="posts")

    def __repr__(self) -> str:
        return f"<Post(id={self.id}, title={self.title}, content={self.content})>"



# ------------------------
# Helper Functions
# ------------------------
def create_table():
    """Create all database tables."""
    Base.metadata.create_all(engine)


def drop_table():
    """Drop all database tables."""
    Base.metadata.drop_all(engine)
