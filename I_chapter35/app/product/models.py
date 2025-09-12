from sqlmodel import SQLModel, Field
from pydantic import ConfigDict

# Base class
class ProductBase(SQLModel):
    title: str
    description: str


# Create schema
class ProductCreate(ProductBase):
    pass


# Full update (PUT) → requires all fields
class ProductUpdate(ProductBase):
    pass


# Partial update (PATCH) → optional fields
class ProductPatch(SQLModel):
    title: str | None = None
    description: str | None = None


# Response schema
class ProductResponse(ProductBase):
    id: int

    model_config = ConfigDict(from_attributes=True)


# Table model
class Product(ProductBase, table=True):
    id: int | None = Field(default=None, primary_key=True)  # ✅ correct PK
