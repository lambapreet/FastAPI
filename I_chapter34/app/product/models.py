from sqlmodel import SQLModel, Field

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

    class Config:
        orm_mode = True   # allows returning ORM objects directly

# Table model
class Product(ProductBase, table=True):
    id: int = Field(primary_key=True)
