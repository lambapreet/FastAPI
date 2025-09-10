from sqlmodel import SQLModel,Field

class ProductBase(SQLModel):
    title:str
    description:str
    
class ProductCreate(ProductBase):
    pass

class ProductUpdate(ProductBase):
    pass

class ProductPatch(SQLModel):
    title:str | None = None
    description:str | None = None
    
    
class ProductResponse(ProductBase):
    id:int

 
class Product(ProductBase,table=True):
    id: int = Field(primary_key=True)
