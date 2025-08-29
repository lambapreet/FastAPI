from sqlmodel import SQLModel, Field,Relationship


# Association table for many-to-many relationship between User and Address
class UserAddressLink(SQLModel, table=True):
    user_id: int = Field(foreign_key="user.id", primary_key=True)       # FK to User
    address_id: int = Field(foreign_key="address.id", primary_key=True) # FK to Address


# User table
class User(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)  # Auto-increment PK
    name: str                                             # User name
    email: str                                            # User email
    
    profiile: "Profile" | None = Relationship(back_populates="user")
    post = list["Post"] = Relationship(back_populates="user")
    address = list["Address"] = Relationship(back_populates="user",link_model=UserAddressLink)


# Profile table (One-to-One with User)
class Profile(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)   # Auto-increment PK
    user_id: int = Field(foreign_key="user.id", unique=True) # One user → one profile
    bio: str                                                 # User bio
    
    user: "User"  = Relationship(back_populates="profile")


# Post table (One-to-Many with User)
class Post(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)  # Auto-increment PK
    user_id: int = Field(foreign_key="user.id")             # FK to User
    title: str                                              # Post title
    content: str                                            # Post content
    
    user: "User" = Relationship(back_populates="post")


# Address table
class Address(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)  # Auto-increment PK
    street: str                                             # Address field
    user = list["User"] = Relationship(back_populates="address",link_model=UserAddressLink)
