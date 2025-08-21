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

    # One-to-one: User -> Profile
    profile: Mapped["Profile"] = relationship(
        "Profile", back_populates="user", uselist=False, cascade="all, delete-orphan"
    )

    # Many-to-many: User <-> Address (via association_table)
    addresses: Mapped[list["Address"]] = relationship(
        "Address", secondary="association_table", back_populates="users"
    )

    def __repr__(self) -> str:
        return f"<User(id={self.id}, name={self.name}, email={self.email})>"


# ------------------------
# Post Model (One-to-Many with User)
# ------------------------
class Post(Base):
    __tablename__ = "posts"   

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id", ondelete="CASCADE"), nullable=False
    )
    title: Mapped[str] = mapped_column(String(200), nullable=False)
    content: Mapped[str] = mapped_column(Text, nullable=False)

    # Many-to-one: Post -> User
    user: Mapped["User"] = relationship("User", back_populates="posts")

    def __repr__(self) -> str:
        return f"<Post(id={self.id}, title={self.title}, content={self.content})>"


# ------------------------
# Profile Model (One-to-One with User)
# ------------------------
class Profile(Base):
    __tablename__ = "profiles"   

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id", ondelete="CASCADE"), nullable=False, unique=True
    )
    bio: Mapped[str] = mapped_column(String(200), nullable=False)

    # One-to-one: Profile -> User
    user: Mapped["User"] = relationship("User", back_populates="profile")

    def __repr__(self) -> str:
        return f"<Profile(id={self.id}, bio={self.bio})>"


# ------------------------
# Address Model (Many-to-Many with User)
# ------------------------
class Address(Base):
    __tablename__ = "addresses"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    street: Mapped[str] = mapped_column(String(200), nullable=False)
    country: Mapped[str] = mapped_column(String(200), nullable=False)

    # Many-to-many: Address <-> Users
    users: Mapped[list["User"]] = relationship(
        "User", secondary="association_table", back_populates="addresses"
    )

    def __repr__(self) -> str:
        return f"<Address(id={self.id}, street={self.street}, country={self.country})>"


# ------------------------
# Association Table for Many-to-Many (User <-> Address)
# ------------------------
association_table = Table(
    "association_table",
    Base.metadata,
    Column("user_id", Integer, ForeignKey("users.id", ondelete="CASCADE"), primary_key=True),
    Column("address_id", Integer, ForeignKey("addresses.id", ondelete="CASCADE"), primary_key=True),
)


# ------------------------
# Helper Functions
# ------------------------
def create_table():
    """Create all database tables."""
    Base.metadata.create_all(engine)


def drop_table():
    """Drop all database tables."""
    Base.metadata.drop_all(engine)
